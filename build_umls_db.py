#!/usr/bin/env python3
"""
Medical Quick Reference — UMLS Database Builder  v2.0
======================================================
Parses MRCONSO.RRF, MRDEF.RRF, and MRSTY.RRF from the UMLS release,
merges with existing MeSH data, and builds a unified SQLite database
covering 400,000+ medical terms with semantic type labels.

Files accepted in the add-on folder (plain or .gz):
  MRCONSO.RRF  (.gz)  — concept names and synonyms
  MRDEF.RRF    (.gz)  — definitions
  MRSTY.RRF    (.gz)  — semantic types  (NEW — enables category badges)

How to get UMLS files:
  1. Log in at https://uts.nlm.nih.gov
  2. Download the current UMLS Full Release (Metathesaurus)
  3. Extract and copy MRCONSO.RRF, MRDEF.RRF, MRSTY.RRF to this folder

Run once from Terminal:
  python3 ~/Library/Application\ Support/Anki2/addons21/med_quick_ref/build_umls_db.py

Time:   ~5-10 min depending on machine
Space:  ~400 MB final database
"""

import gzip
import os
import sqlite3
import sys

# ── Paths ─────────────────────────────────────────────────────────────────────

ADDON_DIR   = os.path.dirname(os.path.abspath(__file__))
DB_PATH     = os.path.join(ADDON_DIR, "med_terms.db")
DB_TMP      = os.path.join(ADDON_DIR, "med_terms_new.db")

# Candidate file paths (plain or gzip)
def _rrf(name):
    plain = os.path.join(ADDON_DIR, name)
    gz    = plain + ".gz"
    if os.path.exists(plain): return plain
    if os.path.exists(gz):    return gz
    return plain  # will fail with a clean error below

MRCONSO_PATH = _rrf("MRCONSO.RRF")
MRDEF_PATH   = _rrf("MRDEF.RRF")
MRSTY_PATH   = _rrf("MRSTY.RRF")

# ── Definition source priority ────────────────────────────────────────────────
# Lower number = higher priority.

DEF_PRIORITY = {
    "MSH":          1,   # MeSH — gold standard
    "NCI":          2,   # National Cancer Institute thesaurus
    "CSP":          3,   # CRISP thesaurus (NIH)
    "HPO":          4,   # Human Phenotype Ontology
    "SNOMEDCT_US":  5,   # SNOMED CT
    "RXNORM":       6,   # RxNorm — drugs
    "ICF":          7,   # International Classification of Functioning
    "GO":           8,   # Gene Ontology
}
DEFAULT_PRIORITY = 99

# ── Semantic type priority (when a CUI has multiple types) ────────────────────

SEM_PRIORITY = {
    "Disease or Syndrome":                  1,
    "Neoplastic Process":                   2,
    "Sign or Symptom":                      3,
    "Finding":                              4,
    "Pharmacologic Substance":              5,
    "Antibiotic":                           5,
    "Clinical Drug":                        5,
    "Therapeutic or Preventive Procedure":  6,
    "Diagnostic Procedure":                 7,
    "Laboratory Procedure":                 7,
    "Body Part, Organ, or Organ Component": 8,
    "Gene or Genome":                       9,
    "Amino Acid, Peptide, or Protein":      10,
    "Enzyme":                               10,
    "Organism":                             11,
    "Bacterium":                            11,
    "Virus":                                11,
}
DEFAULT_SEM_PRIORITY = 50

# ── Term type filter (MRCONSO) ────────────────────────────────────────────────

INCLUDE_TTY = {
    # Preferred terms
    "PT", "MH", "NM", "PEP", "PTGB",
    # Synonyms / entries
    "SY", "ET", "HT", "CE", "EP", "EQ", "OP",
    # Drug-specific (RxNorm)
    "IN", "BN", "PIN", "MIN", "SBD", "SCD", "SBDF", "SCDF",
    # Clinical / abbreviations
    "FN", "AB", "ACR", "MTH_ACR",
}

# ─────────────────────────────────────────────────────────────────────────────

def _progress(msg):
    sys.stdout.write(f"\r  {msg:<70}")
    sys.stdout.flush()


def _fmt(n):
    return f"{n:,}"


def _open_rrf(path):
    """Open an RRF file whether it is plain text or gzip-compressed."""
    if path.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return open(path, "r", encoding="utf-8", errors="replace")


def _check_files():
    missing = []
    for path, label in [
        (MRCONSO_PATH, "MRCONSO.RRF"),
        (MRDEF_PATH,   "MRDEF.RRF"),
    ]:
        exists = os.path.exists(path) or os.path.exists(path + ".gz")
        if not exists:
            missing.append(label)
    return missing


def build():
    print("=" * 62)
    print("  Medical Quick Ref — UMLS Database Builder  v2.0")
    print("=" * 62)

    missing = _check_files()
    if missing:
        print(f"\n✗ Missing required files in: {ADDON_DIR}")
        for m in missing:
            print(f"    • {m}  (or {m}.gz)")
        print("\nDownload the UMLS Full Release from https://uts.nlm.nih.gov")
        sys.exit(1)

    for path, label in [
        (MRCONSO_PATH, "MRCONSO.RRF"),
        (MRDEF_PATH,   "MRDEF.RRF"),
        (MRSTY_PATH,   "MRSTY.RRF"),
    ]:
        actual = path if os.path.exists(path) else path + ".gz"
        if os.path.exists(actual):
            mb = os.path.getsize(actual) / 1_000_000
            tag = " (gzip)" if actual.endswith(".gz") else ""
            print(f"  ✓ {label}{tag} ({mb:.0f} MB)")
        else:
            print(f"  – {label} not found (semantic types will be omitted)")

    # ── Phase 0: MRSTY → CUI → semantic type ─────────────────────────────────
    print("\n[1/4] Reading semantic types (MRSTY)...")
    cui_sem   = {}   # CUI → (sem_type_name, priority)
    sty_count = 0

    sty_path = MRSTY_PATH if os.path.exists(MRSTY_PATH) else MRSTY_PATH + ".gz"
    if os.path.exists(sty_path):
        with _open_rrf(sty_path) as f:
            for line in f:
                parts = line.rstrip("\n").split("|")
                if len(parts) < 4:
                    continue
                cui = parts[0]
                sty = parts[3].strip()   # STY = semantic type name
                if not sty:
                    continue
                pri = SEM_PRIORITY.get(sty, DEFAULT_SEM_PRIORITY)
                existing = cui_sem.get(cui)
                if existing is None or pri < existing[1]:
                    cui_sem[cui] = (sty, pri)
                sty_count += 1
                if sty_count % 200_000 == 0:
                    _progress(f"{_fmt(sty_count)} types read, "
                              f"{_fmt(len(cui_sem))} unique concepts...")
        print(f"\n     {_fmt(sty_count)} type assignments, "
              f"{_fmt(len(cui_sem))} unique concepts")
    else:
        print("\n     (MRSTY not found — semantic types skipped)")

    # ── Phase 1: MRDEF → CUI → best definition ───────────────────────────────
    print("\n[2/4] Reading definitions (MRDEF)...")
    cui_def   = {}   # CUI → (definition, priority)
    def_count = 0

    with _open_rrf(MRDEF_PATH) as f:
        for line in f:
            parts = line.rstrip("\n").split("|")
            if len(parts) < 6:
                continue
            cui  = parts[0]
            sab  = parts[4]
            defn = parts[5].strip()
            if not defn or len(defn) < 10:
                continue
            pri = DEF_PRIORITY.get(sab, DEFAULT_PRIORITY)
            existing = cui_def.get(cui)
            if existing is None or pri < existing[1]:
                cui_def[cui] = (defn, pri)
            def_count += 1
            if def_count % 50_000 == 0:
                _progress(f"{_fmt(def_count)} definitions, "
                          f"{_fmt(len(cui_def))} unique concepts...")

    print(f"\n     {_fmt(def_count)} definitions, "
          f"{_fmt(len(cui_def))} unique concepts")

    # ── Phase 2: MRCONSO → English terms → (CUI, display term) ──────────────
    print("\n[3/4] Reading terms (MRCONSO — English only)...")
    term_map   = {}   # normalised_lower → (display_term, CUI)
    read_count = 0

    with _open_rrf(MRCONSO_PATH) as f:
        for line in f:
            parts = line.rstrip("\n").split("|")
            if len(parts) < 15:
                continue
            cui  = parts[0]
            lang = parts[1]
            tty  = parts[12]
            term = parts[14].strip()

            if lang != "ENG":
                continue
            if tty not in INCLUDE_TTY:
                continue
            if not term or len(term) < 2:
                continue
            if cui not in cui_def:
                continue

            norm = term.lower()
            if norm not in term_map:
                term_map[norm] = (term, cui)

            read_count += 1
            if read_count % 100_000 == 0:
                _progress(f"{_fmt(read_count)} terms mapped...")

    print(f"\n     {_fmt(read_count)} terms with definitions, "
          f"{_fmt(len(term_map))} unique (normalised)")

    # ── Phase 3: Build SQLite ─────────────────────────────────────────────────
    print("\n[4/4] Building SQLite database...")

    if os.path.exists(DB_TMP):
        os.remove(DB_TMP)

    conn = sqlite3.connect(DB_TMP)
    c    = conn.cursor()

    c.executescript("""
        CREATE TABLE terms (
            term       TEXT PRIMARY KEY COLLATE NOCASE,
            definition TEXT NOT NULL,
            source     TEXT DEFAULT 'UMLS',
            sem_type   TEXT DEFAULT ''
        );
        CREATE INDEX idx_term_lower ON terms (term COLLATE NOCASE);
    """)

    # Migrate existing MeSH entries (preserve priority over UMLS entries)
    if os.path.exists(DB_PATH):
        print("     Migrating existing MeSH database...")
        old  = sqlite3.connect(DB_PATH)
        # Try to read sem_type if the old DB has it
        try:
            rows = old.execute(
                "SELECT term, definition, source, sem_type FROM terms"
            ).fetchall()
        except sqlite3.OperationalError:
            rows = [
                (r[0], r[1], r[2], "")
                for r in old.execute(
                    "SELECT term, definition, source FROM terms"
                ).fetchall()
            ]
        old.close()
        c.executemany(
            "INSERT OR IGNORE INTO terms (term, definition, source, sem_type) "
            "VALUES (?,?,?,?)",
            rows,
        )
        conn.commit()
        migrated = c.execute("SELECT COUNT(*) FROM terms").fetchone()[0]
        print(f"     Migrated {_fmt(migrated)} MeSH terms")

    # Insert UMLS terms (don't overwrite existing MeSH)
    batch    = []
    inserted = 0

    for norm, (display, cui) in term_map.items():
        defn, _ = cui_def[cui]
        sem     = cui_sem.get(cui, ("", 0))[0]
        batch.append((display, defn[:500], "UMLS", sem))

        if len(batch) >= 5_000:
            c.executemany(
                "INSERT OR IGNORE INTO terms (term, definition, source, sem_type) "
                "VALUES (?,?,?,?)",
                batch,
            )
            conn.commit()
            inserted += len(batch)
            batch = []
            _progress(f"{_fmt(inserted)} UMLS terms written...")

    if batch:
        c.executemany(
            "INSERT OR IGNORE INTO terms (term, definition, source, sem_type) "
            "VALUES (?,?,?,?)",
            batch,
        )
        conn.commit()
        inserted += len(batch)

    total = c.execute("SELECT COUNT(*) FROM terms").fetchone()[0]

    sources = c.execute(
        "SELECT source, COUNT(*) FROM terms "
        "GROUP BY source ORDER BY COUNT(*) DESC"
    ).fetchall()

    top_sem = c.execute(
        "SELECT sem_type, COUNT(*) FROM terms "
        "WHERE sem_type != '' "
        "GROUP BY sem_type ORDER BY COUNT(*) DESC LIMIT 8"
    ).fetchall()

    conn.close()

    # ── Finalize ──────────────────────────────────────────────────────────────
    print(f"\n     Finalising...")
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    os.rename(DB_TMP, DB_PATH)

    # Clean up source RRF files
    deleted = []
    for path in [MRCONSO_PATH, MRDEF_PATH, MRSTY_PATH]:
        for p in [path, path + ".gz"]:
            if os.path.exists(p):
                os.remove(p)
                deleted.append(os.path.basename(p))

    db_mb = os.path.getsize(DB_PATH) / 1_000_000

    print(f"\n{'=' * 62}")
    print(f"  ✓  Complete!")
    print(f"     Total terms           : {_fmt(total)}")
    print(f"     By source:")
    for src, cnt in sources:
        print(f"       {src:<12}  {_fmt(cnt):>10} terms")
    if top_sem:
        print(f"     Top semantic types:")
        for sty, cnt in top_sem:
            print(f"       {sty:<40}  {_fmt(cnt):>8}")
    print(f"     Database size         : {db_mb:.0f} MB")
    print(f"     Location              : {DB_PATH}")
    if deleted:
        print(f"     Deleted source files  : {', '.join(deleted)}")
    print(f"{'=' * 62}")
    print("\nRestart Anki — hover now uses the full UMLS database.\n")


if __name__ == "__main__":
    build()
