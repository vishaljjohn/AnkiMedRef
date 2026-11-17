# ─────────────────────────────────────────────────────────────────────────────
#  Anki Add-on: Medical Quick Reference  v8.26
#
#  NEW in v8.26 (efficiency):
#    - Network lookups are skipped once you've hovered another word (they
#      were still fired for the old word), drug APIs only get 1–2-word
#      phrases, and Wikipedia "(medicine)" titles only single words: a missed
#      word now costs ≤15 requests instead of ≤21, and none if superseded.
#    - Config cache also holds an empty config; "B12" no longer gets the
#      green ICD-10 underline.
#
#  NEW in v8.25 (code/data split):
#    - Layout: __init__.py = code only; formatters.py = the HTML formatters
#      (_dd, _dr, _ob, _pc …); data/*.py = one file per dictionary group
#      (diseases, drugs, obgyn, primary_care, labs, related …).  Each data file
#      loads on its own: a typo in one disables only that file's entries and
#      Anki shows a warning naming the file and line.  No content changed.
#
#  NEW in v8.24 (bug hunt + symptoms/labs/drugs):
#    - Fixed: definition cache ignored letter case, so after hovering "PAD",
#      "MAP", "HIT" or "TIPS" the everyday words pad/map/hit/tips showed the
#      acronym's card.  Hover phrases no longer join words across line breaks.
#      Letter+digit terms (S3, S4, T4, B12) are now looked up.  Settings help
#      for deck_profiles pointed at a Config button the add-on replaces.
#      Related chips resolve anatomy alternate names; T4 units printed twice.
#    - ~30 symptom/sign work-up cards (fever, stridor, wheeze, murmurs, heart
#      sounds, lung exam, AMS, dyspnea, abdominal pain by location, dysphagia,
#      jaundice, pruritus, splenomegaly, petechiae/purpura, diplopia, polyuria,
#      joint pain, hoarseness, N/V) and test-interpretation cards (HBV
#      serology, autoantibodies, thrombophilia, urinalysis, smear, syphilis).
#    - 14 lab cards (CK, retic, MMA, BHB, C-peptide, renin/ARR, CD4, SPEP,
#      metanephrines, 5-HIAA, calcitonin, thyroglobulin, calprotectin, ASO).
#    - 27 drug cards (argatroban, teriparatide, omalizumab, dupilumab,
#      nirsevimab, surfactant, IVIG, acetazolamide, nimodipine, antidotes,
#      terlipressin, tolvaptan, PCC, IV iron, EPO…); OB periviability and
#      third-stage management; ~650 new alternate names.
#
#  NEW in v8.23 (shelf dictionaries, round 5 — ~360 new cards):
#    - Internal medicine (~105): acid-base (AGMA/NAGMA/RTA, alkalosis, respiratory),
#      electrolytes (Na, K, Ca, Mg, phosphate), glomerular diseases, AKI types,
#      cardiomyopathies, AV block, valve disease, PAD, pulmonary HTN/ILD, GI bleeds,
#      liver (PBC/PSC/AIH/ALF), heme-onc emergencies, vasculitides, toxicology.
#    - Pediatrics (~58): neonatal (PPHN, BPD, IVH, ROP, apnea of prematurity),
#      congenital heart disease, airway (TEF, laryngomalacia, foreign body),
#      exanthems, infantile spasms, SMA, short stature, SIDS/BRUE, dehydration/ORT.
#    - Psychiatry (~45): mood/psychotic/anxiety disorders by DSM-5-TR timelines,
#      personality-disorder clusters, substance intoxication/withdrawal, EPS/TD,
#      catatonia, ethics & law (capacity, consent, duty to warn, commitment), ECT.
#    - Neurology (~55): stroke syndromes by territory, tPA/thrombectomy criteria,
#      ICP/herniation, coma/brain death, cranial nerve palsies, INO, cord syndromes,
#      neuropathies, brain tumors, CNS infections, movement disorders.
#    - Family medicine (~45): USPSTF screening cards (diabetes, AAA, osteoporosis,
#      HCV, HIV, STI, depression, aspirin), symptom work-ups (hematuria,
#      proteinuria, LFTs, edema, palpitations, fatigue, lymphadenopathy, falls),
#      outpatient derm/ortho/urology.
#    - OB/GYN: antenatal steroids, Mg neuroprotection/toxicity, BRCA/HBOC,
#      FNAIT, incontinence, tachysystole + ~100 new aliases.
#    - Deck profiles for Internal Medicine, Psychiatry and Neurology; more
#      redirects for OB (ICP, PPD, steroids), Family Medicine and Pediatrics.
#
#  NEW in v8.22 (deck priority):
#    - Lookups follow the deck/tags of the card on screen.  On OB/GYN cards the
#      OB/GYN topics are checked first and general words open the pregnancy card
#      (HTN → hypertensive disorders of pregnancy, anemia → anemia in pregnancy,
#      UTI → asymptomatic bacteriuria, DVT/PE → VTE in pregnancy…); Family
#      Medicine and Peds decks do the same for primary-care cards.  The general
#      card stays one click away as the first chip.  Matches deck names, parent
#      decks, filtered decks and AnKing-style tags.  Toggle under Settings →
#      Deck Priority; profiles editable as "deck_profiles" in config.json.
#
#  NEW in v8.21 (OB/GYN shelf, round 4):
#    - Shelf comparison cards: previa vs abruption vs vasa previa vs rupture,
#      complete vs partial mole, vaginitis table, ovarian tumors by cell type and
#      marker, hypertensive disorders spectrum, uterotonics, contraindications to
#      labor/tocolysis; plus malpresentation, intrapartum procedures, obstetric
#      ultrasound, fetal anomalies, birth injuries, HIE, neonatal sepsis,
#      postpartum complications, lactation problems, common complaints,
#      lifestyle counseling, psychiatric/neurologic disease and cancer in
#      pregnancy, twin complications, placental abnormalities
#    - New cards: pregestational diabetes, dermatoses of pregnancy (PUPPP,
#      pemphigoid gestationis), thrombocytopenia in pregnancy, kidney disease in
#      pregnancy, toxic shock syndrome, postcoital bleeding/ectropion
#    - Upgraded: preeclampsia (expectant vs delivery criteria, magnesium dosing,
#      postpartum), ectopic (methotrexate day 4/7 protocol, contraindications),
#      misoprostol doses, β-hCG (35–50% rise, discriminatory zone), maternal
#      serum AFP causes, pregnancy norms for fibrinogen and platelets
#    - Related chips for ~150 OB/GYN and primary-care entries; alternate names
#      (PPH, Pitocin…) now show the chips of the entry they point to
#
#  NEW in v8.20 (OB/GYN NBME shelf, family medicine):
#    - +42 OB/GYN cards: cervicitis, genital herpes, condyloma, varicella /
#      parvovirus / toxoplasmosis / Listeria in pregnancy, hyperprolactinemia,
#      hirsutism, POI, delayed puberty, Müllerian anomalies, polyps, chronic
#      pelvic pain, IC, vulvodynia, sexual dysfunction, IPV, sexual assault,
#      fistula, vaginal cancer, uterine sarcoma, PUL, stillbirth, cord anomalies,
#      acute abdomen / trauma / VTE / cardiac / epilepsy / lupus / sickle cell /
#      asthma / obesity / substance use in pregnancy, maternal sepsis, puerperal
#      hematoma, neonatal hypoglycemia, NOWS, pediatric gyn, ectopic variants
#    - OB/GYN tier: first- and third-trimester bleeding, pelvic mass,
#      postmenopausal bleeding, breast mass, acute pelvic pain workups, imaging in
#      pregnancy, newborn care, NRP, ethics, gyn procedures, menstrual cycle,
#      puberty, antepartum testing, preconception and carrier screening, TORCH
#    - New Primary Care tier (Tier 0.5p): USPSTF, vaccines, milestones, well-child
#      and adolescent care, preop evaluation, travel, sports physicals, geriatrics,
#      advance directives, PrEP/PEP, febrile infant, chest pain / dizziness /
#      anemia / weight-loss approaches, hypertension and statin topics
#    - +50 family medicine cards (MSK, ENT, derm, GI, GU, sleep, obesity, tobacco)
#      with 24 drugs and 8 screening scores (AUDIT-C, GAD-7, FRAX, Mini-Cog…)
#    - Fixes: mono-di twin delivery timing; simple ovarian cyst follow-up sizes
#
#  NEW in v8.19 (shelf exams / USMLE Step 2 CK, OB/GYN rotation):
#    - New OB/GYN tier (Tier 0.5o): stages of labor, arrest disorders, fetal
#      heart tracings (early/late/variable decels, categories), prenatal care and
#      genetic screening, GTPAL, teratogens, cesarean/TOLAC, contraception, Pap
#      and mammography screening, menopause therapy, GBS prophylaxis, PPH bundle
#    - ~205 new disease cards: obstetrics, gynecology, breast, plus core Step 2
#      medicine, neurology, psychiatry, pediatrics, surgery and emergency topics
#      (each with a next-best-step pearl); ~750 alternate names
#    - OB drugs (oxytocin, methylergonovine, carboprost, TXA, betamethasone,
#      RhoGAM, contraceptives…), reproductive labs (FSH, LH, AMH, bile acids,
#      Kleihauer-Betke…), OB signs, EPDS/BPP/BI-RADS scores, prenatal US signs;
#      milestones, vaccine schedules, USPSTF screening, HTN and statin topics
#    - Eclampsia, HELLP, abruption, vasa previa, accreta and adenomyosis now have
#      their own cards instead of opening the preeclampsia/previa/endometriosis one
#    - Abbreviations are checked last, so DKA, COPD, TSH, SSRI… open the full card
#    - Lookups that find nothing are remembered for 5 minutes (no repeat burst of
#      network requests); only enabled dictionaries underline words
#    - Fixed: TIA opened the stroke card; skin SCC opened basal cell carcinoma;
#      stale entry counts in Settings
#
#  NEW in v8.18:
#    - Tooltip theme: Auto (follows Anki night mode) / Dark / Light
#    - Wikipedia images: the article's picture is shown above a definition
#    - Clinical signs & eponyms dictionary (Tier 0.5m): Murphy, Kernig, Beck's
#      triad, Janeway, Courvoisier, Nikolsky … with possessive spellings
#    - Anatomy: 169 entries (was 31) — gross anatomy, neuroanatomy, embryology
#      and basic histology for first-year students; ~850 alternate names;
#      factual corrections, duplicate entries merged
#    - Offline dictionaries match singular/plural (dermatome ↔ dermatomes)
#    - DB / web text is HTML-escaped before display; DB opened read-only
#    - Fixed: OpenFDA boxed warnings never shown (wrong field name)
#    - Dictionaries reviewed for accuracy and currency (~80 fixes: 2024 DKA/HHS
#      criteria, GOLD/GINA, IDSA C. diff, ACG H. pylori, ACR gout, dosing errors…)
#    - +32 diseases, +9 pathology concepts, +4 organisms and ~100 disease-name
#      aliases, +5 syndromes, +5 scores, new Basic Sciences tier (pharmacology,
#      immunology, biochemistry)
#    - Lookups try the surrounding phrase before the single hovered word
#      ('ischemic stroke' no longer shows the entry for 'stroke')
#    - Every drug, drug-class and microbiology entry re-read line by line
#      (~260 fixes: mechanisms, trial names, boxed warnings, guideline updates)
#    - Lab ranges show SI units (mmol/L, μmol/L, g/L …) under the normal range
#    - +24 ECG findings, +19 radiology signs, +16 genetics topics, +20
#      biostatistics concepts, +98 abbreviations, ~70 alternate names
#
#  NEW in v8.17:
#    - Words split by formatting (<u>M</u>ultiparity) are recognised whole
#    - Mnemonics: hover an acronym (MMAPP) to see the list it spells on the card
#    - Everyday words (prior, multiple, severe…) and function words (the, with,
#      may…) are no longer looked up or underlined on their own
#    - Online sources are queried in parallel (~1–3 s instead of 5–27 s)
#    - UMLS uses the API key directly (2 requests instead of 4), English only
#    - Fixed: RxNorm and MedlinePlus never returned results; crash when lookups
#      shared one DB connection; Python 3.9 startup crash; Related / Did-you-mean
#      chips discarded their result; saved max-length / min-word settings ignored
#      after restart; abbreviation false positives (all, men, ten, per)
#    - Offline tiers driven by one table (_OFFLINE_TIERS) instead of 14 copies
#
#  NEW in v8.16:
#    - Efficiency: _get_user_cfg() 2-second TTL cache (eliminates ~40 disk reads/lookup)
#    - Efficiency: _inject_with_retry() skips JS rebuild when config unchanged
#    - Efficiency: _lookup_candidates() uses single config snapshot (was 15+ reads)
#    - Bug fix: tier 0.5b (lab range) now loops all candidates like every other tier
#    - Feature: _sugg_pairs_cache expanded with brand/alias/related dicts
#    - Refactor: _send_lookup_result() shared helper; rel_js precomputed on worker
#    - Bug fix: 15 _MICRO entries had missing 4th arg (treatment) in _mo() calls
#
#  NEW in v8.15:
#    - Bug fixes: UMLS TGT reset now always holds _umls_tgt_lock (race condition)
#    - DB connection errors now logged to stderr instead of silently swallowed
#    - Dictionary expansion: +79 entries across ECG, biostats, micro, genetics,
#      pathology, radiology, syndromes; _SCORE_ALIASES for 36 score name variants
#    - _DISEASE_ALIASES: cirrhosis/pancreatitis/pe/ra/dka all resolve to canonical entry
#    - _RELATED expanded to 99 cross-references
#    - Code cleanup: stale tier counts updated, inline imports removed
#  NEW in v8.14:
#    - Cmd+S / Ctrl+S: highlight text → opens Google in your default browser instantly
#      (removed old in-tooltip lookup; no more tooltip conflict/spaz)
#    - Tooltip is now scrollable (max-height: 75vh) for long definitions
#    - Tooltip positions accurately using real rendered height (no more clipping)
#    - mouseleave listener registered only once (no listener accumulation on card flips)
#    - Config changes (hover delay, min word length) take effect without Anki restart
#    - Lookup cache capped at 500 entries with FIFO eviction (no more memory leak)
#    - Source label no longer duplicated when badge already shows the source
#    - HTML-escaped phrase in tooltip title (special chars no longer break layout)
#  NEW in v8.13:
#    - OMIM integration (Tier 6.5): genetic disease lookups via OMIM REST API
#      (add your free key at omim.org/api — stored in Settings)
#    - Google Search replaces Google Scholar everywhere
#    - Code cleanup: dead code removed, waterfall standardised
#  NEW in v8.12:
#    - Genetics dictionary (Tier 0.5j): 30 entries — inheritance, trinucleotide
#      repeats, genomic imprinting, BRCA1/2, Li-Fraumeni, Lynch, Fragile X, etc.
#    - Radiology dictionary (Tier 0.5k): 27 entries — GGO, crazy paving, Hampton's
#      hump, Westermark, Codman triangle, apple core, coffee bean, steeple, etc.
#    - Pathology dictionary (Tier 0.5l): 22 entries — necrosis types, Lewy/Negri/
#      Mallory/Psammoma bodies, Reed-Sternberg, Auer rods, Congo red, signet ring, etc.
#    - Related terms chips at tooltip bottom: click to look up a related term
#    - Auto-suggest: 'Did you mean X, Y?' chips shown when term not found
#    - ⌘ hold-to-lock: hold Cmd (Mac) or Ctrl (Win) to freeze tooltip instead of pin
#  NEW in v8.11:
#    - Abbreviation dictionary (Tier 0.1): 100 medical abbreviations (ACEi, DKA, GFR, etc.)
#    - Clinical Syndromes dictionary (Tier 0.5h): 59 syndromes (Wernicke's, ODS, MEN, Marfan, etc.)
#    - ECG Findings dictionary (Tier 0.5i): 32 findings (STEMI, Brugada, Torsades, heart blocks, etc.)
#    - 5-second lookup timeout: shows PubMed/Scholar if network lookup takes too long
#    - Pin button (📌) on tooltip to lock it open while reading
#  NEW in v8.10:
#    - Fixed Cmd+Shift+D hover: Qt shortcut now checks hovered word as fallback
#      (Qt ApplicationShortcut was consuming the keypress before JS could see it)
#  NEW in v8.9:
#    - Settings: hover delay slider, min word length & tooltip max chars controls
#    - Settings: network tier toggles (RxNorm, OpenFDA, MedlinePlus, Wikipedia)
#    - Settings: keyboard shortcut reminder panel
#  NEW in v8.8:
#    - 'No definition found' tooltip now shows PubMed and Google Scholar links
#    - Links open in your default browser directly from the card
#  NEW in v8.7:
#    - UMLS search uses normalizedString (case-insensitive, finds more terms)
#    - Removed redundant semantic-type API call (faster lookups)
#    - Tooltip shows 'No definition found' instead of silently disappearing
#  NEW in v8.6:
#    - Cmd+Shift+D now works by hovering over a word (no click-drag needed)
#    - Fixed AttributeError on Anki 25.09.2 (setConfig compatibility wrapper)
#  NEW in v8.5:
#    - Config button in Add-ons manager now opens the custom settings UI
#  NEW in v8.4:
#    - Fixed Cmd+Shift+D shortcut (was silently broken when webview had focus)
#    - Shortcut now uses in-JS keydown listener + ApplicationShortcut Qt context
#  NEW in v8.3:
#    - Redesigned settings dialog: pill toggle switches, tier badges, UMLS API key field with live test button
#  NEW in v8.2:
#    - Biostatistics & epidemiology dictionary (~35 entries: sensitivity, specificity, PPV/NPV, NNT, p-value, biases, etc.)
#    - Drug dictionary expanded to ~195 drugs (biologics, HIV ARVs, checkpoint inhibitors, reversal agents, respiratory drugs)
#  NEW in v8.1:
#    - Individual drug lookup (~130 drugs: MOA, uses, adverse effects, pearls)
#  NEW in v8.0:
#  • Disease dictionary expanded: 18 → 70+ entries (ARDS, COPD, asthma,
#    pneumothorax, hypothyroidism, hyperthyroidism, thyroid storm, myxedema coma,
#    Addison disease, Cushing syndrome, pheochromocytoma, primary hyperaldosteronism,
#    SIADH, TTP, HUS, DIC, ITP, sickle cell disease, gout, rheumatoid arthritis,
#    AF, infective endocarditis, pericarditis, cardiac tamponade, status epilepticus,
#    myasthenia gravis, Guillain-Barré, liver cirrhosis, nephrotic/nephritic syndrome,
#    hypertensive emergency, and more)
#  • Microbiology dictionary expanded: 25 → 54 entries (GBS, S. epidermidis,
#    Enterococcus, C. diphtheriae, C. perfringens, C. botulinum, C. tetani,
#    Bacteroides fragilis, Salmonella, Shigella, Campylobacter, H. pylori,
#    Vibrio cholerae, Borrelia burgdorferi, T. pallidum, Rickettsia,
#    Chlamydia trachomatis, Mycoplasma pneumoniae, Bordetella pertussis,
#    EBV, VZV, Influenza, Toxoplasma, Giardia, Histoplasma, Mucor, HAV, HPV)
#  • Anatomy & Physiology tier (Tier 0.5f): brachial plexus, cranial nerves,
#    circle of Willis, femoral triangle, inguinal canal, carpal tunnel,
#    spinal cord tracts, coronary arteries, O2-Hgb curve, RAAS, Frank-Starling,
#    loop of Henle, coagulation cascade, action potential
#  • All offline tiers (0.5a–f) now gated by per-tier config switches
#
#  NEW in v7.8:
#  • Disease / condition dictionary (Tier 0.5c) — diagnostic criteria, key features,
#    treatment, and Step 1 pearls for ~18 high-yield conditions (DKA, HHS, sepsis,
#    PE, MI, heart failure, SLE, CKD, pneumonia, meningitis, stroke, pancreatitis,
#    DVT, aortic dissection, ACS, SIADH, adrenal insufficiency, thyroid storm)
#  • Microbiology organism dictionary (Tier 0.5d) — gram/morph, virulence factors,
#    diseases caused, treatment, and pearls for ~23 high-yield organisms (S. aureus,
#    MRSA, GAS, S. pneumoniae, N. meningitidis, N. gonorrhoeae, E. coli, Pseudomonas,
#    Klebsiella, H. influenzae, Listeria, C. difficile, M. tuberculosis, HIV, HBV,
#    HCV, HSV, CMV, Candida, Aspergillus, Cryptococcus, PCP, Plasmodium)
#  • Both new tiers wired into lookup waterfall before network calls
#
#  NEW in v7.7:
#  • Drug→class reverse lookup — hover any individual drug (metoprolol, atorvastatin,
#    doxorubicin...) to see its class card with 'Member of: [Class Name]' header
#  • 20 more drug classes: α1-blockers, central α2 agonists, digoxin, PPIs, H2-blockers,
#    bisphosphonates, benzodiazepines, barbiturates, lithium, ARVs (NRTI/NNRTI/PI/INSTI),
#    insulin, anticholinesterases, anticholinergics, alkylating agents, antimetabolites,
#    anthracyclines, taxanes, platinum analogs, TKIs, anti-VEGF, rifamycins, polymyxins
#  • 25 more lab ranges: lactate, PCT, haptoglobin, ceruloplasmin, fibrinogen, cortisol,
#    ACTH, aldosterone, PTH, VitD, B12, folate, homocysteine, AFP, β-hCG, PSA, CA-125,
#    CEA, ANA, anti-dsDNA, C3, C4, RF, anti-CCP, ANCA
#
#  NEW in v7.6:
#  • Drug class hover dictionary (Tier 0.5a) — MOA, members, uses, CI/ADR, pearl
#    for ~40 drug classes (instant, offline)
#  • Lab reference ranges dictionary (Tier 0.5b) — normal range, critical values,
#    high/low clinical meaning, pearls for 50+ lab tests (instant, offline)
#
#  NEW in v7.5:
#  • Term highlighting — recognized medical terms are underlined on card load
#
#  NEW in v7.4:
#  • OpenFDA drug label API (Tier 4.5) — MOA, indications, boxed warnings,
#    contraindications, adverse reactions for every FDA-approved drug
#
#  NEW in v7.3:
#  • FA2023 + Pathoma 2019 terms merged directly into main database
#
#  NEW in v7.0:
#  • Medical abbreviation dictionary — 200+ terms, zero latency (Tier 0)
#  • UMLS REST API fallback — paste your API key in CFG below
#  • RxNorm drug identification — automatic, no key required
#  • ICD-10 code highlighting — green underline on card codes
#  • Semantic type badge — Disease / Drug / Anatomy / Lab / etc.
#  • Digit-aware word detection — HbA1c, SpO2, FiO2, COVID19 ...
#  • Tooltip cap raised to 450 chars
#
#  Lookup tier order (fastest → network):
#    0. Abbreviation dict    (instant, offline)
#    1. In-memory cache      (instant)
#    2. Local MeSH/UMLS DB   (~5 ms, offline) — 1.2M+ terms
#    2.5. Morphological variants (offline)
#    3. UMLS REST API        (network, if api_key set)
#    4. RxNorm API           (network, drugs)
#    5. NLM MedlinePlus      (network)
#    6. Wikipedia            (network)
# ─────────────────────────────────────────────────────────────────────────────

import html
import os
import pathlib
import re
import sys
import json
import sqlite3
import threading
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# SSL fix for macOS — the add-on's own web requests use certifi's
# certificates.  Passed to each urlopen() call instead of replacing Python's
# global default, which would change HTTPS for Anki and every other add-on.
try:
    import ssl, certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _SSL_CTX = None  # certifi not installed; SSL uses system defaults


def _urlopen(req, timeout):
    return urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX)

from aqt import mw, gui_hooks
from aqt.reviewer import Reviewer
from aqt.qt import QTimer

# ─────────────────────────────────────────────────────────────────────────────
# 1 · Configuration
#     API keys are stored only in config.json (managed via the Settings dialog).
#     Do NOT paste keys here — they would be exposed in the source file.
#     To add your UMLS key: Tools → Medical Quick Reference Settings → UMLS API Key
#     To add your OMIM key: Tools → Medical Quick Reference Settings → OMIM API Key
# ─────────────────────────────────────────────────────────────────────────────

CFG = {
    "hover_delay_ms":          300,
    "min_word_len":            3,
    "tooltip_max_chars":       450,
    "inject_initial_delay_ms": 80,
    "inject_max_retries":      18,
    # API keys intentionally absent — loaded at runtime from config.json only.
}

_cfg_cache: dict = {}
_cfg_cache_ts: float = 0.0
_CFG_CACHE_TTL: float = 2.0   # seconds

def _get_user_cfg() -> dict:
    """Read addon config; cached up to _CFG_CACHE_TTL seconds."""
    global _cfg_cache, _cfg_cache_ts
    now = time.time()
    if _cfg_cache_ts and (now - _cfg_cache_ts) < _CFG_CACHE_TTL:
        return _cfg_cache
    try:
        cfg = mw.addonManager.getConfig(__name__) or {}
    except Exception:
        cfg = {}
    _cfg_cache = cfg
    _cfg_cache_ts = now
    return cfg

def _user_cfg_save(cfg):
    """Write user config — compatible with Anki 2.1.x and 25.x."""
    mgr = mw.addonManager
    if hasattr(mgr, 'writeConfig'):
        mgr.writeConfig(__name__, cfg)
    elif hasattr(mgr, 'setConfig'):
        mgr.setConfig(__name__, cfg)
    else:
        import json as _json, os as _os
        _path = _os.path.join(mgr.addonsFolder(__name__), "config.json")
        with open(_path, "w", encoding="utf-8") as _f:
            _json.dump(cfg, _f, indent=4)


def _user_cfg_get(key, default=True):
    return _get_user_cfg().get(key, default)


def _max_chars() -> int:
    """Saved tooltip length limit (CFG only holds the built-in default)."""
    try:
        return int(_user_cfg_get("tooltip_max_chars", CFG["tooltip_max_chars"]))
    except (TypeError, ValueError):
        return CFG["tooltip_max_chars"]


def _min_word_len() -> int:
    """Saved minimum word length (CFG only holds the built-in default)."""
    try:
        return int(_user_cfg_get("min_word_len", CFG["min_word_len"]))
    except (TypeError, ValueError):
        return CFG["min_word_len"]

# ─────────────────────────────────────────────────────────────────────────────
# 2 · Local MeSH / UMLS database
# ─────────────────────────────────────────────────────────────────────────────

_ADDON_DIR = os.path.dirname(os.path.abspath(__file__))
_DB_PATH   = os.path.join(_ADDON_DIR, "med_terms.db")
# One connection per thread.  Lookups run on several worker threads at once
# (hover lookups, the card-load underline check); sharing a single connection
# between them could crash the whole process (segfault) under load.
_db_local  = threading.local()


def _get_db():
    conn = getattr(_db_local, "conn", None)
    if conn is None and os.path.exists(_DB_PATH):
        try:
            # Read-only and immutable: the add-on never writes to the DB, so
            # per-thread connections read concurrently without locks, and the
            # file is never modified (no -wal / -shm files next to it).
            conn = sqlite3.connect(
                pathlib.Path(_DB_PATH).as_uri() + "?mode=ro&immutable=1",
                uri=True)
            _db_local.conn = conn
        except Exception as _e:
            print(f"[MQR] DB connection error: {_e}", file=sys.stderr)
            conn = None
    return conn


def _case_ok(db_term, text):
    """An all-caps acronym entry (PER, GET, ABA, CAT) matches only text that
    is also written in capitals — otherwise "per" showed a rare syndrome."""
    t = db_term.strip()
    if len(t) > 1 and t.isupper() and t.replace("-", "").isalpha():
        return text.strip().isupper()
    return True


def _lookup_local_db(phrase):
    """Returns (definition, sem_type) or ('', '').  Supports both old and new schema."""
    db = _get_db()
    if not db:
        return "", ""
    try:
        try:
            row = db.execute(
                "SELECT definition, sem_type, term FROM terms "
                "WHERE term = ? COLLATE NOCASE LIMIT 1",
                (phrase.strip(),),
            ).fetchone()
            if row and _case_ok(row[2], phrase):
                return _plain_html(row[0]), (row[1] or "")
        except sqlite3.OperationalError:
            # Old DB without sem_type column
            row = db.execute(
                "SELECT definition, term FROM terms "
                "WHERE term = ? COLLATE NOCASE LIMIT 1",
                (phrase.strip(),),
            ).fetchone()
            if row and _case_ok(row[1], phrase):
                return _plain_html(row[0]), ""
    except Exception:
        pass
    return "", ""

# ─────────────────────────────────────────────────────────────────────────────
# 3 · Medical abbreviation dictionary  (Tier 0.1 — zero latency)
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# Offline dictionaries — loaded from data/*.py, formatted by formatters.py.
# Each file is loaded on its own, so a typo in one dictionary only disables
# that file's entries (with a warning after Anki starts) instead of the
# whole add-on.
# ─────────────────────────────────────────────────────────────────────────────
import importlib
from .formatters import _LAB_LBL

_DATA_ERRORS: list = []


def _load_data(module, *names):
    """The named dictionaries from data/<module>.py, or empty ones if the
    file is missing or has an error."""
    try:
        mod = importlib.import_module(f"{__name__}.data.{module}")
        return tuple(getattr(mod, n) for n in names)
    except Exception as _e:
        _DATA_ERRORS.append(f"data/{module}.py — {type(_e).__name__}: {_e}")
        print(f"[MQR] could not load data/{module}.py: {_e}", file=sys.stderr)
        return tuple({} for _ in names)


_ABBREVS, _ABBREV_TERMS = _load_data('abbrevs', '_ABBREVS', '_ABBREV_TERMS')
_DRUG_CLASSES, _DRUG_CLASS_ALIASES = _load_data('drug_classes', '_DRUG_CLASSES', '_DRUG_CLASS_ALIASES')
_LAB_RANGES, _LAB_SI, _LAB_ALIASES = _load_data('labs', '_LAB_RANGES', '_LAB_SI', '_LAB_ALIASES')
_BIOSTATS, = _load_data('biostats', '_BIOSTATS')
_DRUGS, _DRUG_BRAND_ALIASES = _load_data('drugs', '_DRUGS', '_DRUG_BRAND_ALIASES')
_DISEASES, _DISEASE_ALIASES = _load_data('diseases', '_DISEASES', '_DISEASE_ALIASES')
_MICRO, _MICRO_ALIASES = _load_data('micro', '_MICRO', '_MICRO_ALIASES')
_SCORES, _SCORE_ALIASES = _load_data('scores', '_SCORES', '_SCORE_ALIASES')
_ANATOMY, _ANATOMY_ALIASES = _load_data('anatomy', '_ANATOMY', '_ANATOMY_ALIASES')
_SYNDROMES, = _load_data('syndromes', '_SYNDROMES')
_ECG_FINDINGS, = _load_data('ecg', '_ECG_FINDINGS')
_GENETICS, = _load_data('genetics', '_GENETICS')
_RADIOLOGY, = _load_data('radiology', '_RADIOLOGY')
_PATHOLOGY, _PATHOLOGY_ALIASES = _load_data('pathology', '_PATHOLOGY', '_PATHOLOGY_ALIASES')
_SIGNS, _SIGN_ALIASES = _load_data('signs', '_SIGNS', '_SIGN_ALIASES')
_BASIC_SCIENCE, _BASIC_SCIENCE_ALIASES = _load_data('basic_science', '_BASIC_SCIENCE', '_BASIC_SCIENCE_ALIASES')
_OBGYN, _OBGYN_ALIASES = _load_data('obgyn', '_OBGYN', '_OBGYN_ALIASES')
_PRIMARY_CARE, _PRIMARY_CARE_ALIASES = _load_data('primary_care', '_PRIMARY_CARE', '_PRIMARY_CARE_ALIASES')
_RELATED, = _load_data('related', '_RELATED')


def _add_aliases(target, aliases):
    """target[alias] = target[key] for each pair.  Pairs whose entry is
    missing (e.g. its data file failed to load) are skipped, so one broken
    file cannot stop the whole add-on from starting."""
    for alias, key in aliases.items():
        if key in target:
            target[alias] = target[key]



# ─────────────────────────────────────────────────────────────────────────────
# 3b.5 · Drug class dictionary  (Tier 0.5a — instant, offline)
# ─────────────────────────────────────────────────────────────────────────────


def _build_drug_to_class():
    """Build reverse map: individual drug name → class key (built once at import)."""
    mapping = {}
    for class_key, entry in _DRUG_CLASSES.items():
        members = re.findall(r'>([^<]+)</span>', entry)
        in_members = False
        for m in members:
            upper = m.upper()
            if upper in ("MOA", "MEMBERS", "USES", "CI / ADR", "PEARL",
                         "\u2191 HIGH", "\u2193 LOW", "NORMAL", "CRITICAL"):
                in_members = (upper == "MEMBERS")
                continue
            if in_members:
                clean = re.sub(r'\s*\([^)]*\)', '', m).strip().lower()
                if clean and clean not in mapping:
                    mapping[clean] = class_key
    return mapping

_DRUG_TO_CLASS = _build_drug_to_class()

# Aliases map alternate spellings / abbreviations → canonical _DRUG_CLASSES key.
# Add new entries here instead of duplicating full _dc() definitions above.

def _lookup_drug_class(phrase):
    """Tier 0.5a: Check drug class dictionary OR member-drug reverse lookup.
    Returns HTML string or empty string."""
    key = phrase.strip().lower()
    # 1. Direct class-name hit (e.g. "beta blocker")
    hit = _DRUG_CLASSES.get(key, "")
    if hit:
        return hit
    # 1b. Alias hit — resolve to canonical key then look up (e.g. "beta-blocker" → "beta blocker")
    canonical = _DRUG_CLASS_ALIASES.get(key, "")
    if canonical:
        hit = _DRUG_CLASSES.get(canonical, "")
        if hit:
            return hit
    # 2. Individual drug member hit (e.g. "metoprolol" → beta blocker card)
    class_key = _DRUG_TO_CLASS.get(key, "")
    if class_key:
        LBL = ('<span style="color:var(--mqr-lbl);font-size:11px;font-weight:600;'
               'text-transform:uppercase;letter-spacing:0.5px">')
        header = (f'<div style="margin-bottom:4px;font-size:11px;color:var(--mqr-muted4)">'
                  f'Member of: {LBL}{class_key.title()}</span></div>')
        return header + _DRUG_CLASSES[class_key]
    return ""
# ─────────────────────────────────────────────────────────────────────────────
# 3b.6 · Lab reference ranges dictionary  (Tier 0.5b — instant, offline)
# ─────────────────────────────────────────────────────────────────────────────



# SI equivalents of the conventional ranges above, shown as a second row ("SI")
for _k, _si in _LAB_SI.items():
    if _k not in _LAB_RANGES:
        continue
    _LAB_RANGES[_k] = _LAB_RANGES[_k].replace("<br>", f"<br>{_LAB_LBL}SI</span> {_si}<br>", 1)

# Alias keys that redirect to canonical lab entries (parallel to _DISEASE_ALIASES)

def _lookup_lab_range(phrase):
    """Tier 0.5b: Check lab reference ranges. Returns HTML string or empty."""
    key = phrase.strip().lower()
    key = _LAB_ALIASES.get(key, key)
    return _LAB_RANGES.get(key, "")
# ─────────────────────────────────────────────────────────────────────────────
# Tier 0.5c · Disease / condition dictionary  (instant, offline)
# ─────────────────────────────────────────────────────────────────────────────





# Bare "power" only matches when written POWER (see _ACRONYM_WORDS)
_add_aliases(_BIOSTATS, {'statistical power': 'power'})
_add_aliases(_BIOSTATS, {
    'standard error': 'standard error of the mean',
    'gaussian distribution': 'normal distribution',
    'bell curve': 'normal distribution',
    'right skew': 'positive skew',
    'positively skewed': 'positive skew',
    'left skew': 'negative skew',
    'negatively skewed': 'negative skew',
    't test': 't-test',
    'student t-test': 't-test',
    "student's t-test": 't-test',
    'paired t-test': 't-test',
    'analysis of variance': 'anova',
    'chi square': 'chi-square test',
    'chi-squared test': 'chi-square test',
    'chi square test': 'chi-square test',
    'chi-square': 'chi-square test',
    'pearson correlation': 'correlation coefficient',
    'pretest probability': 'pre-test probability',
    'posttest probability': 'post-test probability',
    'receiver operating characteristic': 'roc curve',
    'crossover trial': 'crossover study',
    'noninferiority trial': 'non-inferiority trial',
    'phase 1 trial': 'clinical trial phases',
    'phase i trial': 'clinical trial phases',
    'phase 2 trial': 'clinical trial phases',
    'phase ii trial': 'clinical trial phases',
    'phase 3 trial': 'clinical trial phases',
    'phase iii trial': 'clinical trial phases',
    'phase 4 trial': 'clinical trial phases',
    'phase iv trial': 'clinical trial phases',
    'case fatality': 'case fatality rate',
    'pygmalion effect': 'observer bias',
})


def _looks_like_abbrev(word):
    """True when a word is written like an abbreviation (2+ capitals, e.g. COPD,
    SpO2, ACEi).  Prevents everyday words such as "all", "men", "ten" or "Art"
    from matching the upper-case abbreviation keys ALL, MEN, TEN, ART."""
    return sum(c.isupper() for c in word) >= 2


def _lookup_abbrev(phrase):
    """Tier 0.1: medical abbreviation lookup — checks both dicts.

    Priority: _ABBREV_TERMS first (richer clinical summaries for drug classes,
    conditions, procedures) then _ABBREVS fallback (short definitions for
    abbreviations not covered by _ABBREV_TERMS).  This order ensures that the
    69+ terms present in both dicts always surface their longer, clinically
    richer _ABBREV_TERMS entry rather than the short _ABBREVS stub.
    """
    LBL = ('<span style="color:var(--mqr-lbl-gold);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    word = phrase.strip()
    # Check _ABBREV_TERMS first — richer drug-class / condition summaries
    # (keys are lowercase, so normalise the input)
    entry = _ABBREV_TERMS.get(word.lower(), "")
    if entry:
        return f'{LBL}Abbreviation</span> {entry}'
    # Fall back to core _ABBREVS dict (BP, HR, SpO2, Na, K …)
    entry = _ABBREVS.get(word) or (
        _ABBREVS.get(word.upper()) if _looks_like_abbrev(word) else "")
    if entry:
        return f'{LBL}Abbreviation</span> {entry}'
    return ""







def _lookup_biostats(phrase):
    """Return biostatistics card from _BIOSTATS dict, or empty string."""
    key = phrase.strip().lower()
    return _BIOSTATS.get(key, "")



# Brand name → generic drug key aliases

def _lookup_drug(phrase):
    """Return individual drug card from _DRUGS dict, or empty string."""
    key = phrase.strip().lower()
    # Resolve brand name to generic key
    key = _DRUG_BRAND_ALIASES.get(key, key)
    return _DRUGS.get(key, "")


# Alias keys that redirect to canonical disease entries

def _lookup_disease(phrase):
    """Tier 0.5c: Check disease/condition dictionary. Returns HTML or empty."""
    key = phrase.strip().lower()
    # Resolve alias to canonical key
    key = _DISEASE_ALIASES.get(key, key)
    return _DISEASES.get(key, "")
# ─────────────────────────────────────────────────────────────────────────────
# Tier 0.5d · Microbiology organism dictionary  (instant, offline)
# ─────────────────────────────────────────────────────────────────────────────


# Disease names and full species names → organism entries (keys written the
# way _lookup_micro normalizes them: lowercase, no dots)


def _lookup_micro(phrase):
    """Tier 0.5d: Check microbiology organism dictionary. Returns HTML or empty."""
    # Normalize: strip dots (S. aureus → s aureus) and collapse spaces
    key = phrase.strip().lower().replace(".", "")
    key = " ".join(key.split())
    return _MICRO.get(_MICRO_ALIASES.get(key, key), "")
# ─────────────────────────────────────────────────────────────────────────────
# Tier 0.5e · Clinical scoring systems dictionary  (instant, offline)
# ─────────────────────────────────────────────────────────────────────────────



# Alias keys that redirect to canonical scoring system entries

def _lookup_score(phrase):
    """Tier 0.5e: Check clinical scoring systems dictionary. Returns HTML or empty."""
    key = phrase.strip().lower()
    # Resolve alias to canonical key
    key = _SCORE_ALIASES.get(key, key)
    return _SCORES.get(key, "")

# ─────────────────────────────────────────────────────────────────────────────
# Tier 0.5f · Anatomy & Physiology dictionary  (instant, offline)
# ─────────────────────────────────────────────────────────────────────────────


# Other names for the _ANATOMY entries, as they are written on cards


def _lookup_anatomy(phrase):
    """Tier 0.5f: Check anatomy/physiology dictionary. Returns HTML or empty."""
    key = phrase.strip().lower()
    return _ANATOMY.get(_ANATOMY_ALIASES.get(key, key), "")


# ─────────────────────────────────────────────────────────────────────────────
# 3b · Morphological variants — catch adjective/plural forms
#      e.g. asplenic→asplenia, septic→sepsis, metastases→metastasis
# ─────────────────────────────────────────────────────────────────────────────

# Curated high-yield medical adjective → noun mappings
_MED_WORD_FORMS = {
    "asplenic": "asplenia", "ischemic": "ischemia", "hypoxic": "hypoxia",
    "septic": "sepsis", "anemic": "anemia", "anaemic": "anaemia",
    "hypertensive": "hypertension", "hypotensive": "hypotension",
    "hypothyroid": "hypothyroidism", "hyperthyroid": "hyperthyroidism",
    "diabetic": "diabetes mellitus", "nephrotic": "nephrotic syndrome",
    "cirrhotic": "cirrhosis", "fibrotic": "fibrosis", "necrotic": "necrosis",
    "stenotic": "stenosis", "thrombotic": "thrombosis", "embolic": "embolism",
    "edematous": "edema", "oedematous": "oedema", "acidotic": "acidosis",
    "alkalotic": "alkalosis", "tachycardic": "tachycardia",
    "bradycardic": "bradycardia", "febrile": "fever",
    "dyspneic": "dyspnea", "dyspnoeic": "dyspnoea",
    "anuric": "anuria", "oliguric": "oliguria", "polyuric": "polyuria",
    "jaundiced": "jaundice", "icteric": "icterus", "cyanotic": "cyanosis",
    "cachectic": "cachexia", "ataxic": "ataxia", "aphasic": "aphasia",
    "hemiplegic": "hemiplegia", "paraplegic": "paraplegia",
    "epileptic": "epilepsy", "psychotic": "psychosis", "manic": "mania",
    "schizophrenic": "schizophrenia", "leukemic": "leukemia",
    "leukaemic": "leukaemia", "metastatic": "metastasis",
    "arthritic": "arthritis", "osteoporotic": "osteoporosis",
    "asthmatic": "asthma", "emphysematous": "emphysema",
    "pneumonic": "pneumonia", "pleuritic": "pleuritis",
    "hepatitic": "hepatitis", "colitic": "colitis", "nephritic": "nephritis",
    "meningitic": "meningitis", "encephalitic": "encephalitis",
    "neuropathic": "neuropathy", "myopathic": "myopathy",
    "cardiomyopathic": "cardiomyopathy", "atrophic": "atrophy",
    "hypertrophic": "hypertrophy", "dystrophic": "dystrophy",
    "dysplastic": "dysplasia", "hyperplastic": "hyperplasia",
    "aplastic": "aplasia", "sclerotic": "sclerosis",
    "atherosclerotic": "atherosclerosis", "cholestatic": "cholestasis",
    "uremic": "uremia", "uraemic": "uraemia", "azotemic": "azotemia",
    "hyponatremic": "hyponatremia", "hypernatremic": "hypernatremia",
    "hypokalemic": "hypokalemia", "hyperkalemic": "hyperkalemia",
    "hypocalcemic": "hypocalcemia", "hypercalcemic": "hypercalcemia",
    "hypoglycemic": "hypoglycemia", "hyperglycemic": "hyperglycemia",
    "hypothermic": "hypothermia", "hyperthermic": "hyperthermia",
    "tachypneic": "tachypnea", "bradypneic": "bradypnea",
    "cholecystitic": "cholecystitis", "pancreatitic": "pancreatitis",
    "diverticulitic": "diverticulitis", "appendicitic": "appendicitis",
    "pericarditic": "pericarditis", "endocarditic": "endocarditis",
    "myocarditic": "myocarditis", "aortic": "aorta",
    "splenic": "spleen", "hepatic": "liver", "renal": "kidney",
    "pulmonary": "lung", "cerebral": "cerebrum", "cerebellar": "cerebellum",
    "thyroidal": "thyroid", "adrenal": "adrenal gland",
    "pancreatic": "pancreas", "gastric": "stomach", "colonic": "colon",
    "dysphasic": "dysphasia", "dysarthric": "dysarthria",
    "afebrile": "afebrile state",
    "hypoxemic": "hypoxemia", "hypercapnic": "hypercapnia",
    "hypocapnic": "hypocapnia", "tachyarrhythmic": "tachyarrhythmia",
    "bradyarrhythmic": "bradyarrhythmia",
    # ── Movement / anatomical verb forms ──────────────────────────────────────
    "innervates": "innervation", "innervating": "innervation",
    "innervate": "innervation", "innervated": "innervation",
    "supinates": "supination", "supinating": "supination",
    "pronates": "pronation", "pronating": "pronation",
    "flexes": "flexion", "flexing": "flexion", "flexed": "flexion",
    "extends": "extension", "extending": "extension", "extended": "extension",
    "abducts": "abduction", "abducting": "abduction",
    "adducts": "adduction", "adducting": "adduction",
    "rotates": "rotation", "rotating": "rotation",
    "elevates": "elevation", "elevating": "elevation",
    "depresses": "depression", "depressing": "depression",
    "everts": "eversion", "everting": "eversion",
    "inverts": "inversion", "inverting": "inversion",
    "dorsiflexes": "dorsiflexion", "dorsiflexing": "dorsiflexion",
    "plantarflexes": "plantarflexion", "plantarflexing": "plantarflexion",
    "circumducts": "circumduction", "circumducting": "circumduction",
    "protracts": "protraction", "retracts": "retraction",
    "opposes": "opposition", "opposing": "opposition",
    "articulates": "articulation", "articulating": "articulation",
    "anastomoses": "anastomosis", "anastomosing": "anastomosis",
    "perforates": "perforation", "perforating": "perforation",
    "bifurcates": "bifurcation", "bifurcating": "bifurcation",
    "originates": "origin", "originating": "origin",
    "inserts": "insertion", "inserting": "insertion",
    "compresses": "compression", "compressing": "compression",
    "depolarizes": "depolarization", "depolarizing": "depolarization",
    "repolarizes": "repolarization", "repolarizing": "repolarization",
    "contracts": "contraction", "contracting": "contraction",
    "relaxes": "relaxation", "relaxing": "relaxation",
    "dilates": "dilation", "dilating": "dilation",
    "constricts": "constriction", "constricting": "constriction",
    "secretes": "secretion", "secreting": "secretion",
    "stimulates": "stimulation", "stimulating": "stimulation",
    "inhibits": "inhibition", "inhibiting": "inhibition",
    "mediates": "mediation", "mediating": "mediation",
    "regulates": "regulation", "regulating": "regulation",
    "activates": "activation", "activating": "activation",
    "phosphorylates": "phosphorylation", "phosphorylating": "phosphorylation",
    "metabolizes": "metabolism", "metabolizing": "metabolism",
    "synthesizes": "synthesis", "synthesizing": "synthesis",
    "degrades": "degradation", "degrading": "degradation",
    "proliferates": "proliferation", "proliferating": "proliferation",
    "differentiates": "differentiation", "differentiating": "differentiation",
    "migrates": "migration", "migrating": "migration",
    "invades": "invasion", "invading": "invasion",
    "metastasizes": "metastasis", "metastasizing": "metastasis",
    "inflames": "inflammation", "inflaming": "inflammation",
    "calcifies": "calcification", "calcifying": "calcification",
    "ossifies": "ossification", "ossifying": "ossification",
    "lyses": "lysis", "lysing": "lysis",
    "hydrolyzes": "hydrolysis", "hydrolyzing": "hydrolysis",
    "opsonizes": "opsonization", "opsonizing": "opsonization",
    "agglutinates": "agglutination", "agglutinating": "agglutination",
    "precipitates": "precipitation", "precipitating": "precipitation",
    "coagulates": "coagulation", "coagulating": "coagulation",
    "fibrinolyzes": "fibrinolysis",
    "suppurates": "suppuration", "suppurating": "suppuration",
    "ulcerates": "ulceration", "ulcerating": "ulceration",
    "necrotizes": "necrosis", "necrotizing": "necrosis",
    "demyelinates": "demyelination", "demyelinating": "demyelination",
    "degenerates": "degeneration", "degenerating": "degeneration",
    "regenerates": "regeneration", "regenerating": "regeneration",
}

# General suffix transformation rules
_SUFFIX_RULES = [
    # Disease/condition adjective → noun
    ("tic",   ["sis", "tis"]),       # septic→sepsis, necrotic→necrosis
    ("ical",  ["ic", "y", "ics"]),   # anatomical→anatomy
    ("ic",    ["ia", "ism", "y"]),   # asplenic→asplenia
    ("ous",   ["osis", "a", "e"]),   # edematous→edema
    ("ive",   ["ion", "ity", "e"]),  # obstructive→obstruction
    ("ent",   ["ence", "ency"]),     # deficient→deficiency
    ("ant",   ["ance", "ancy"]),     # malignant→malignance
    # Verb forms → noun
    ("ating", ["ation", "ate"]),     # supinating→supination
    ("ates",  ["ation", "ate"]),     # innervates→innervation
    ("izing", ["ization", "ize"]),   # metabolizing→metabolism (approx)
    ("izes",  ["ization", "ize"]),   # metabolizes→metabolism
    ("ing",   ["ion", "e"]),         # flexing→flexion, extending→extension
    ("es",    ["e", "ion"]),         # flexes→flex
    # Plural/Latin forms
    ("ses",   ["sis"]),              # metastases→metastasis
    ("mata",  ["ma"]),               # carcinomata→carcinoma
    ("ae",    ["a"]),                # vertebrae→vertebra
    ("i",     ["us"]),               # bronchi→bronchus
]


def _medical_variants(word):
    """Return morphological variants to try in the database."""
    w = word.lower().strip()
    variants = []
    # Curated mappings first (most reliable)
    if w in _MED_WORD_FORMS:
        variants.append(_MED_WORD_FORMS[w])
    # Suffix rules
    for suffix, replacements in _SUFFIX_RULES:
        if w.endswith(suffix) and len(w) > len(suffix) + 2:
            base = w[:-len(suffix)]
            for rep in replacements:
                candidate = base + rep
                if candidate != w and candidate not in variants:
                    variants.append(candidate)
    # Simple plural
    if w.endswith("s") and not w.endswith("ss") and len(w) > 4:
        singular = w[:-1]
        if singular not in variants:
            variants.append(singular)
    return variants


def _number_variants(phrase):
    """Singular/plural forms of a phrase's last word, for the offline
    dictionaries: "dermatome" → "dermatomes", "coronary arteries" →
    "coronary artery".  Case is kept so "PVCs" → "PVC" still works."""
    head, _, last = phrase.strip().rpartition(" ")
    lw = last.lower()
    if len(lw) < 4:
        return []
    if lw.endswith("ies"):
        forms = [last[:-3] + "y"]
    elif lw.endswith("s") and not lw.endswith(("ss", "us", "is")):
        forms = [last[:-1]]
    elif lw.endswith("y") and lw[-2] not in "aeiou":
        forms = [last[:-1] + "ies"]
    elif lw.endswith(("s", "x", "z", "ch", "sh")):
        forms = []
    else:
        forms = [last + "s"]
    return [f"{head} {f}" if head else f for f in forms]


# ─────────────────────────────────────────────────────────────────────────────
# 4 · Semantic-type → tooltip badge mapping
# ─────────────────────────────────────────────────────────────────────────────

_SEM_BADGE = {
    "Disease or Syndrome":                  "Disease",
    "Neoplastic Process":                   "Cancer",
    "Sign or Symptom":                      "Symptom",
    "Finding":                              "Finding",
    "Laboratory or Test Result":            "Lab",
    "Diagnostic Procedure":                 "Procedure",
    "Therapeutic or Preventive Procedure":  "Procedure",
    "Laboratory Procedure":                 "Lab",
    "Pharmacologic Substance":              "Drug",
    "Antibiotic":                           "Drug",
    "Clinical Drug":                        "Drug",
    "Biologically Active Substance":        "Drug",
    "Immunologic Factor":                   "Immunology",
    "Hormone":                              "Hormone",
    "Enzyme":                               "Enzyme",
    "Amino Acid, Peptide, or Protein":      "Protein",
    "Nucleic Acid, Nucleoside, or Nucleotide": "Nucleic Acid",
    "Gene or Genome":                       "Gene",
    "Body Part, Organ, or Organ Component": "Anatomy",
    "Tissue":                               "Anatomy",
    "Cell":                                 "Anatomy",
    "Body System":                          "Anatomy",
    "Anatomical Abnormality":               "Anatomy",
    "Congenital Abnormality":               "Congenital",
    "Acquired Abnormality":                 "Disease",
    "Mental or Behavioral Dysfunction":     "Psychiatry",
    "Injury or Poisoning":                  "Injury",
    "Physiologic Function":                 "Physiology",
    "Pathologic Function":                  "Pathology",
    "Organism":                             "Organism",
    "Bacterium":                            "Bacterium",
    "Virus":                                "Virus",
    "Vitamin":                              "Vitamin",
    "Element, Ion, or Isotope":             "Chemistry",
    "Organic Chemical":                     "Chemistry",
    "Inorganic Chemical":                   "Chemistry",
}

# ─────────────────────────────────────────────────────────────────────────────
# 5 · Definition cache
# ─────────────────────────────────────────────────────────────────────────────

_cache: dict = {}
_cache_lock = threading.Lock()   # guards all reads + writes to _cache


def _cache_key(candidates, primary=None):
    """One key per whole request.  Keying by a single phrase made a cached
    "plexus" answer every later hover of "brachial plexus".  Case is kept:
    "PAD"/"pad" and "MAP"/"map" resolve differently (acronym words)."""
    norm = lambda p: " ".join(str(p or "").split())
    return (norm(primary),) + tuple(norm(c) for c in candidates)


def _cache_get(key):
    with _cache_lock:
        return _cache.get(key)   # (phrase, defn, url, src, badge)


_CACHE_MAX = 500   # maximum entries before FIFO eviction

# Lookups that found nothing, with the time they ran.  Re-hovering the same
# unknown word would otherwise start the whole set of network requests again.
_miss_cache: dict = {}
_MISS_TTL = 300    # seconds
_MISS_MAX = 500


def _miss_recent(key):
    with _cache_lock:
        t = _miss_cache.get(key)
        if t is None:
            return False
        if time.monotonic() - t < _MISS_TTL:
            return True
        del _miss_cache[key]
        return False


def _miss_set(key):
    with _cache_lock:
        if key not in _miss_cache and len(_miss_cache) >= _MISS_MAX:
            _miss_cache.pop(next(iter(_miss_cache)))
        _miss_cache[key] = time.monotonic()

def _cache_set(key, result):
    """Cache a full lookup result so a repeat hover shows the same badge and
    source link as the first one."""
    with _cache_lock:
        if key in _cache:
            # Refresh existing entry without growing the cache
            _cache[key] = result
            return
        if len(_cache) >= _CACHE_MAX:
            # Evict the oldest entry (insertion-order guaranteed in Python 3.7+)
            if _cache:
                _cache.pop(next(iter(_cache)))
        _cache[key] = result

# ─────────────────────────────────────────────────────────────────────────────
# 6 · Hover injection JavaScript
#     Changes vs v6: digit-aware WORD_RE, ICD-10 green highlight,
#     badge param in mqrUpdate, min-length bypass for all-caps abbreviations.
# ─────────────────────────────────────────────────────────────────────────────

_HOVER_JS_TEMPLATE = r"""
(function() {
    'use strict';
    const cardRoot = document.getElementById('qa')
                  || document.querySelector('.card')
                  || document.body;
    if (!cardRoot || cardRoot.textContent.trim().length < 2) {
        pycmd('mqr:__retry__');
        return;
    }
    const DELAY      = HOVER_DELAY_MS;
    const MIN_LEN    = MIN_WORD_LEN;
    const NET_TIMEOUT = LOOKUP_TIMEOUT_MS;  // ms before showing "not found" for slow network
    const CLS     = 'mqr-w';
    const TIP_ID  = 'mqr-tip';

    document.querySelectorAll('.' + CLS).forEach(el => {
        el.replaceWith(document.createTextNode(el.textContent));
    });
    cardRoot.normalize();

    let tip = document.getElementById(TIP_ID);
    if (!tip) {
        tip = document.createElement('div');
        tip.id = TIP_ID;
        document.body.appendChild(tip);
        // Hide tooltip when mouse leaves it (unless cmd-locked)
        // Registered once here to avoid listener accumulation on card flips
        tip.addEventListener('mouseleave', function() {
            if (!window._mqrCmdHeld) setTimeout(hideTip, 300);
        });
    }
    // Theme: every tooltip color is a CSS variable, defined for dark and light.
    // "Auto" follows Anki's night mode (class on <body>).
    let tipStyle = document.getElementById('mqr-style');
    if (!tipStyle) {
        tipStyle = document.createElement('style');
        tipStyle.id = 'mqr-style';
        (document.head || document.documentElement).appendChild(tipStyle);
    }
    tipStyle.textContent = TIP_STYLE_CSS;
    const THEME = 'TOOLTIP_THEME';
    function nightMode() {
        const b = document.body, h = document.documentElement;
        return ['nightMode', 'night_mode', 'night-mode'].some(
            c => b.classList.contains(c) || h.classList.contains(c));
    }
    tip.classList.toggle('mqr-light', THEME === 'Light' || (THEME !== 'Dark' && !nightMode()));
    tip.style.cssText = `
        position: fixed !important;
        background: var(--mqr-bg);
        color: var(--mqr-fg);
        border: 1px solid var(--mqr-border);
        border-radius: 10px;
        padding: 11px 15px;
        max-width: 340px;
        min-width: 200px;
        max-height: 75vh;
        overflow-y: auto;
        font-size: TOOLTIP_FONT_SIZEpx;
        line-height: 1.65;
        z-index: 2147483647;
        display: none;
        box-shadow: 0 10px 36px var(--mqr-shadow);
        pointer-events: auto;
        font-family: 'SF Pro Text','Segoe UI','Helvetica Neue',sans-serif;
    `;

    // Matches: digits-in-words (HbA1c, SpO2), all-caps abbreviations,
    // normal words, and ICD-10 codes (E11.9, J18.0).  Single letters are
    // words too, so "Hepatitis A", "vitamin K" or "group B strep" can be
    // built as phrases; on their own they are too short to be looked up.
    const WORD_RE   = /([A-Z]\d{2}(?:\.\d{1,4})?(?=[^A-Za-z0-9]|$)|[A-Za-z][A-Za-z0-9'\u2019\-]*[A-Za-z0-9]|[A-Za-z])/g;
    const ICD10_RE  = /^(?!B12$)[A-Z]\d{2}(?:\.\d{1,4})?$/;   // B12 = the vitamin
    // Abbreviations: COPD, SpO2-style caps runs, and letter+digit terms (S3, T4, B12)
    const ALLCAPS_RE = /^(?:[A-Z]{2,}[0-9]*|[A-Z][0-9]{1,2})$/;
    // Function words ("with", "the") stay wrapped so phrases like
    // "tetralogy of Fallot" can be built, but hovering them does nothing.
    const STOP = new Set(STOPWORDS_JSON);
    function isStop(w) {
        return STOP.has(w.toLowerCase()) && !(w.length > 1 && w === w.toUpperCase());
    }
    // Everyday words ("prior", "multiple") have no definition of their own, so
    // hovering one stays silent unless a medical phrase around it is found.
    const EVERYDAY = new Set(EVERYDAY_JSON);
    function isEveryday(w) {
        return EVERYDAY.has(w.toLowerCase()) && !(w.length > 1 && w === w.toUpperCase());
    }
    const SKIP_TAGS = new Set(['SCRIPT','STYLE','INPUT','TEXTAREA',
                                'SELECT','BUTTON','A','CODE','PRE','SVG']);
    // Inline formatting tags a single word can be split across, e.g.
    // <u>M</u>ultiparity or Hb<b>A1c</b> — text on both sides is joined
    // before matching so the whole word is recognised.
    const INLINE_TAGS = new Set(['U','B','I','EM','STRONG','SPAN','FONT','MARK',
                                 'SMALL','BIG','S','STRIKE','DEL','INS','SUB','SUP',
                                 'ABBR','CITE','DFN','Q','TT','VAR','KBD','SAMP']);
    // One entry per logical word (its first piece). A word split across inline
    // tags is wrapped as several .mqr-w pieces sharing the same data-idx/data-w.
    const allSpans  = [];

    // Group text nodes into runs of contiguous inline text (no block element,
    // <br>, image or skipped tag between them).
    function collectRuns(root) {
        const runs = [];
        let cur = [];
        function flush() { if (cur.length) runs.push(cur); cur = []; }
        function walk(node) {
            if (node.nodeType === 3) { cur.push(node); return; }
            if (node.nodeType !== 1) return;
            if (SKIP_TAGS.has(node.tagName)
                || (node.classList && node.classList.contains(CLS))) { flush(); return; }
            const inline = INLINE_TAGS.has(node.tagName);
            if (!inline) flush();
            Array.from(node.childNodes).forEach(walk);
            if (!inline) flush();
        }
        walk(root);
        flush();
        return runs;
    }

    // Text of every non-empty run (≈ one line of the card), in order
    const RUNS = [];

    function wrapRun(nodes) {
        const starts = [];
        let text = '';
        nodes.forEach(n => { starts.push(text.length); text += n.nodeValue; });
        if (!text.trim()) return;
        const runIdx = RUNS.length;
        RUNS.push(text);
        const segs = nodes.map(() => []);
        let m;
        WORD_RE.lastIndex = 0;
        while ((m = WORD_RE.exec(text)) !== null) {
            const w = m[0];
            const isIcd   = ICD10_RE.test(w);
            const isCaps  = ALLCAPS_RE.test(w);
            // Short words ("of", "a") are wrapped too so phrases such as
            // "tetralogy of Fallot" can be built, but they never trigger a lookup.
            const isShort = w.length < MIN_LEN && !isIcd && !isCaps;
            const word = { w: w, isIcd: isIcd, isShort: isShort, idx: allSpans.length };
            allSpans.push(null);
            const mStart = m.index, mEnd = m.index + w.length;
            for (let i = 0; i < nodes.length; i++) {
                const ns = starts[i], ne = ns + nodes[i].nodeValue.length;
                if (ne <= mStart || ns >= mEnd) continue;
                segs[i].push({ s: Math.max(mStart, ns) - ns, e: Math.min(mEnd, ne) - ns, word: word });
            }
        }
        nodes.forEach((node, i) => {
            if (!segs[i].length) return;
            const t = node.nodeValue, frag = document.createDocumentFragment();
            let last = 0;
            segs[i].forEach(seg => {
                if (seg.s > last) frag.appendChild(document.createTextNode(t.slice(last, seg.s)));
                const sp = document.createElement('span');
                sp.className = CLS;
                sp.textContent = t.slice(seg.s, seg.e);
                sp.dataset.w   = seg.word.w;
                sp.dataset.idx = seg.word.idx;
                sp.dataset.run = runIdx;
                if (seg.word.isShort) sp.dataset.short = '1';
                sp.style.cursor = 'default';
                if (seg.word.isIcd) {
                    sp.style.borderBottom = '1px dotted #7aaf7a';
                }
                frag.appendChild(sp);
                if (!allSpans[seg.word.idx]) allSpans[seg.word.idx] = sp;
                last = seg.e;
            });
            if (last < t.length) frag.appendChild(document.createTextNode(t.slice(last)));
            node.parentNode.replaceChild(frag, node);
        });
    }

    collectRuns(cardRoot).forEach(wrapRun);

    // ── Mnemonics: an all-caps word whose letters start the items of a list
    //    on the card (MMAPP → Multiparity, Multiple gestations, …) ───────────
    const MNEMONIC_RE = /^[A-Z]{3,12}$/;
    function firstLetter(t) {
        const m = t.match(/[A-Za-z]/);
        return m ? m[0].toUpperCase() : '';
    }
    function cleanItem(t) {
        return t.replace(/^[^A-Za-z]+/, '').replace(/[\s.;:,)]+$/, '').trim();
    }
    function listMatches(items, letters) {
        return items.length === letters.length
            && items.every((it, i) => firstLetter(it) === letters[i]);
    }
    function findMnemonic(acr, runIdx) {
        if (!MNEMONIC_RE.test(acr)) return null;
        const letters = acr.split('');
        const n = letters.length;
        // 1. The next n lines (list under the mnemonic, as on most cards)
        let items = RUNS.slice(runIdx + 1, runIdx + 1 + n);
        if (listMatches(items, letters)) return items.map(cleanItem);
        // 2. The same line, after the mnemonic: "MMAPP: Multiparity, Multiple …"
        const line = RUNS[runIdx] || '';
        const hit  = new RegExp('(^|[^A-Za-z0-9])' + acr + '(?![A-Za-z0-9])').exec(line);
        const pos  = hit ? hit.index + hit[1].length : -1;
        if (pos >= 0) {
            const tail = line.slice(pos + acr.length).replace(/^[\s:=\-–—(]+/, '');
            items = tail.split(/[,;]/).map(t => t.replace(/^\s*(and|or)\s+/i, ''))
                        .filter(t => t.trim()).slice(0, n);
            if (items.length === n) {
                // the last item may run on into the next sentence
                items[n - 1] = items[n - 1].split(/[.)]/)[0];
                if (listMatches(items, letters)) return items.map(cleanItem);
            }
        }
        // 3. The n lines just before the mnemonic
        if (runIdx >= n) {
            items = RUNS.slice(runIdx - n, runIdx);
            if (listMatches(items, letters)) return items.map(cleanItem);
        }
        return null;
    }
    allSpans.forEach(sp => {
        if (!sp) return;
        const items = findMnemonic(sp.dataset.w, parseInt(sp.dataset.run));
        if (items) {
            document.querySelectorAll('.' + CLS + '[data-idx="' + sp.dataset.idx + '"]')
                .forEach(p => { p.dataset.mn = JSON.stringify(items); });
        }
    });

    function showMnemonic(acr, items, x, y) {
        clearTimeout(window._mqrLookupTimeout);
        nextReqId();                       // any lookup still in flight is now stale
        const chip = 'cursor:pointer;color:var(--mqr-mn-fg);font-size:12px;padding:2px 9px;'
                   + 'border:1px solid var(--mqr-mn-border);border-radius:9px;background:var(--mqr-mn-bg);'
                   + 'display:block;margin:4px 0 0 0;';
        tip.innerHTML =
            '<div style="font-weight:700;font-size:13px;color:var(--mqr-title);margin-bottom:6px;'
            + 'border-bottom:1px solid var(--mqr-divider);padding-bottom:5px;">' + escHtml(acr)
            + '<span style="font-size:10px;padding:1px 7px;border-radius:10px;background:var(--mqr-mn-badge-bg);'
            + 'color:var(--mqr-mn-fg);font-weight:600;margin-left:7px;vertical-align:middle">Mnemonic</span></div>'
            + items.map(function(it) {
                return '<span class="mqr-mn-item" data-item="' + escHtml(it) + '" style="' + chip + '">'
                     + '<b style="color:var(--mqr-mn-strong);text-decoration:underline">' + escHtml(it.charAt(0))
                     + '</b>' + escHtml(it.slice(1)) + '</span>';
              }).join('')
            + '<div style="font-size:10px;color:var(--mqr-muted);margin-top:6px">Click an item to look it up</div>';
        tip.style.display = 'block';
        tip.querySelectorAll('.mqr-mn-item').forEach(function(el) {
            el.onmouseenter = function() { this.style.opacity = '0.65'; };
            el.onmouseleave = function() { this.style.opacity = '1'; };
            el.onclick = function() { lookupChip(this.getAttribute('data-item')); };
        });
        positionTip(x, y);
    }

    // ── Batch highlight: ask Python which words have definitions ──────────────
    (function() {
        const unique = [...new Set(allSpans.filter(sp => sp && !sp.dataset.short && !sp.dataset.mn
                                                        && !isStop(sp.dataset.w) && !isEveryday(sp.dataset.w))
                                           .map(sp => sp.dataset.w))];
        if (unique.length > 0) {
            pycmd('mqr:__batch__:' + JSON.stringify(unique) + ':underline=' + (window.mqrUnderline ? '1' : '0'));
        }
    })();

    window.mqrHighlight = function(recognized) {
        if (!window.mqrUnderline) return;
        const rset = new Set(recognized);
        document.querySelectorAll('.' + CLS).forEach(sp => {
            if (sp.dataset.mn) {
                sp.style.borderBottom = '1px dotted #b08fd8';
            } else if (rset.has(sp.dataset.w)) {
                sp.style.borderBottom = '1px dotted #5a8fbf';
                sp.style.textDecorationSkipInk = 'auto';
            }
        });
    };

    function getSentence(idx) {
        const start = Math.max(0, idx - 10);
        const end   = Math.min(allSpans.length - 1, idx + 10);
        return Array.from({length: end - start + 1}, (_, i) => allSpans[start+i].dataset.w).join(' ');
    }

    let timer = null;

    function positionTip(x, y) {
        // Use actual rendered dimensions; fall back to safe estimates
        var tw = tip.offsetWidth  || 350;
        var th = tip.offsetHeight || 220;
        // Clamp to the window; never past the left/top edge on narrow windows
        tip.style.left = Math.max(8, Math.min(x + 14, window.innerWidth  - tw - 8)) + 'px';
        tip.style.top  = Math.max(8, Math.min(y + 20, window.innerHeight - th - 8)) + 'px';
    }
    window._mqrPositionTip = positionTip;

    function hideTip() {
        if (window._mqrTipLocked) return;
        if (tip.matches && tip.matches(':hover')) return;
        tip.style.display = 'none'; tip.innerHTML = ''; window._mqrCmdHeld = false;
    }

    function escHtml(s) {
        return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
                        .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // Every lookup gets an id; results for an older id are ignored so a slow
    // answer for a previous word never overwrites the current tooltip.
    function nextReqId() {
        window._mqrReqId = (window._mqrReqId || 0) + 1;
        return window._mqrReqId;
    }
    function isStale(rid) {
        return rid !== undefined && rid !== null && rid !== window._mqrReqId;
    }

    // Related / "Did you mean" chip: look the term up in place, keeping the
    // tooltip open (and locked) until the result arrives.
    function lookupChip(t) {
        const rid = nextReqId();
        window._mqrCmdHeld = false;
        window._mqrTipLocked = true;
        window._mqrActiveWord = t;
        tip.innerHTML = '<span style="color:var(--mqr-info);font-style:italic">Looking up…</span>';
        tip.style.display = 'block';
        pycmd('mqr:shortcut:' + JSON.stringify({rid: rid, text: t}));
        clearTimeout(window._mqrLookupTimeout);
        window._mqrLookupTimeout = setTimeout(function() {
            if (tip.style.display === 'block' && rid === window._mqrReqId) {
                window.mqrNotFound(t, [], rid);
            }
        }, LOOKUP_TIMEOUT_MS);
    }

    // True when the pointer moved between two pieces of the same split word
    function samePieceWord(el, other) {
        const o = other && other.closest ? other.closest('.' + CLS) : null;
        return !!o && o !== el && o.dataset.idx === el.dataset.idx;
    }

    document.querySelectorAll('.' + CLS).forEach(sp => {
        sp.addEventListener('mouseenter', function(e) {
            if (samePieceWord(this, e.relatedTarget)) return;
            if (this.dataset.short || isStop(this.dataset.w)) return;
            // Don't show tooltip while the user has text selected (e.g. highlighting)
            if (window.getSelection && window.getSelection().toString().trim()) return;
            clearTimeout(timer);
            window._mqrTipLocked = false;
            window._mqrCmdHeld = false;
            var _lk = document.getElementById('mqr-cmd-lock'); if (_lk) _lk.remove();
            const idx  = parseInt(this.dataset.idx);
            const word = this.dataset.w;
            const x = e.clientX, y = e.clientY;
            window._mqrActiveWord = word; window._mqrActiveX = x; window._mqrActiveY = y;
            const mn = this.dataset.mn;
            timer = setTimeout(() => {
                if (mn) { showMnemonic(word, JSON.parse(mn), x, y); return; }
                const silent = isEveryday(word);
                if (!silent) {
                    tip.innerHTML = '<span style="color:var(--mqr-info);font-style:italic">Looking up…</span>';
                    tip.style.display = 'block';
                    positionTip(x, y);
                }
                // Neighbours only from the same line, so a phrase is never
                // built across a line break or list item
                const run = this.dataset.run;
                const nb = function(j) {
                    const s = allSpans[j];
                    return (s && s.dataset.run === run) ? s.dataset.w : '';
                };
                const prev  = nb(idx - 1);
                const next  = nb(idx + 1);
                const prev2 = prev ? nb(idx - 2) : '';
                const next2 = next ? nb(idx + 2) : '';
                const candidates = [];
                if (prev2 && prev) candidates.push(prev2+' '+prev+' '+word);
                if (prev  && next) candidates.push(prev +' '+word+' '+next);
                if (next  && next2) candidates.push(word+' '+next+' '+next2);
                if (prev)  candidates.push(prev +' '+ word);
                if (next)  candidates.push(word +' '+ next);
                candidates.push(word);
                const sentence = getSentence(idx);
                window._mqrActiveCands = candidates; window._mqrActiveSentence = sentence;
                const rid = nextReqId();
                window._mqrSilentRid = silent ? rid : null;
                pycmd('mqr:' + JSON.stringify({candidates, sentence, rid}));
                clearTimeout(window._mqrLookupTimeout);
                if (silent) return;            // no "not found" for everyday words
                window._mqrLookupTimeout = setTimeout(function() {
                    if (tip.style.display === 'block' && !window._mqrTipLocked
                        && rid === window._mqrReqId) {
                        window.mqrNotFound(window._mqrActiveWord || word);
                    }
                }, LOOKUP_TIMEOUT_MS);
            }, DELAY);
        });
        sp.addEventListener('mousemove', function(e) {
            if (tip.style.display === 'block' && !window._mqrTipLocked) positionTip(e.clientX, e.clientY);
        });
        sp.addEventListener('mouseleave', function(e) {
            if (samePieceWord(this, e.relatedTarget)) return;
            clearTimeout(timer);
            window._mqrActiveWord = null;
            if (!window._mqrTipLocked) setTimeout(hideTip, 200);
        });
    });

    // badge: optional short category string, e.g. "Disease" / "Drug" / "Abbrev"
    window.mqrUpdate = function(phrase, defn, srcHtml, badge, related, rid) {
        // Ignore results for a lookup that has since been superseded
        if (isStale(rid)) return;
        clearTimeout(window._mqrLookupTimeout);
        window._mqrTipLocked = false;
        window._mqrCmdHeld = false;
        // Silent (everyday-word) lookup that found a phrase: show it now, if
        // the pointer is still on the word
        if (tip.style.display === 'none' && rid != null && rid === window._mqrSilentRid
            && window._mqrActiveWord) {
            tip.style.display = 'block';
        }
        // Abort if user moved away before the async result arrived
        if (tip.style.display === 'none') return;
        var enc = encodeURIComponent(phrase);
        const badgeHtml = badge
            ? `<span style="font-size:10px;padding:1px 7px;border-radius:10px;
               background:var(--mqr-badge-bg);color:var(--mqr-badge-fg);font-weight:600;
               margin-left:7px;vertical-align:middle;letter-spacing:0.3px">${badge}</span>`
            : '';
        var relatedHtml = '';
        if (related && related.length) {
            var rcs = 'cursor:pointer;color:var(--mqr-rel-fg);font-size:10px;padding:1px 7px;'
                    + 'border:1px solid var(--mqr-rel-border);border-radius:9px;background:var(--mqr-rel-bg);'
                    + 'display:inline-block;margin:2px 4px 0 0;';
            relatedHtml = '<div style="margin-top:5px;border-top:1px solid var(--mqr-divider);padding-top:4px;">'
                + '<span style="color:var(--mqr-muted);font-size:10px">Related: </span>'
                + related.map(function(t) {
                    return '<span class="mqr-rel-chip" data-rel="' + escHtml(t) + '" style="' + rcs + '">' + escHtml(t) + '</span>';
                  }).join('')
                + '</div>';
        }
        var lnk = 'cursor:pointer;color:var(--mqr-link);font-size:10px;margin-right:8px;opacity:0.9;';
        var searchHtml =
            '<div style="margin-top:5px;padding-top:4px;border-top:1px solid var(--mqr-divider);">'
            + '<span style="color:var(--mqr-muted);font-size:10px">Search: </span>'
            + '<span class="mqr-search-link" data-url="https://pubmed.ncbi.nlm.nih.gov/?term=' + enc + '" style="' + lnk + '">PubMed ↗</span>'
            + '<span class="mqr-search-link" data-url="SEARCH_ENGINE_URL' + enc + '" style="' + lnk + '">Web ↗</span>'
            + '<span class="mqr-search-link" data-url="IMAGE_SEARCH_ENGINE_URL' + enc + '" style="' + lnk + '">Images ↗</span>'
            + '</div>';
        var safePhrase = phrase
            .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        tip.innerHTML =
            `<div style="font-weight:700;font-size:13px;color:var(--mqr-title);
             margin-bottom:6px;border-bottom:1px solid var(--mqr-divider);padding-bottom:5px;">`
            + safePhrase + badgeHtml + '</div>'
            + `<div class="mqr-defn" style="color:var(--mqr-fg2);font-size:TOOLTIP_FONT_SIZEpx">${defn}</div>`
            + (srcHtml
                ? `<div style="font-size:10px;color:var(--mqr-muted);margin-top:6px;
                   border-top:1px solid var(--mqr-divider);padding-top:5px;">${srcHtml}</div>`
                : '')
            + relatedHtml + searchHtml;
        document.querySelectorAll('.mqr-rel-chip').forEach(function(el) {
            el.onmouseenter = function() { this.style.opacity = '0.65'; };
            el.onmouseleave = function() { this.style.opacity = '1'; };
            el.onclick = function() { lookupChip(this.getAttribute('data-rel')); };
        });
        document.querySelectorAll('.mqr-search-link').forEach(function(el) {
            el.onmouseenter = function() { this.style.opacity = '0.65'; };
            el.onmouseleave = function() { this.style.opacity = '1'; };
            el.onclick = function() {
                var u = this.getAttribute('data-url');
                window._mqrTipLocked = false; window._mqrCmdHeld = false;
                tip.style.display = 'none'; tip.innerHTML = '';
                pycmd('mqr:open:' + u);
            };
        });
        // Re-position after content is rendered so offsetHeight is accurate
        if (window._mqrActiveX !== undefined) positionTip(window._mqrActiveX, window._mqrActiveY);
    };
    // Picture for the term (Wikipedia thumbnail), sent after the definition.
    // Click it to toggle full size.
    window.mqrImage = function(src, rid) {
        if (isStale(rid) || tip.style.display === 'none') return;
        const box = tip.querySelector('.mqr-defn');
        if (!box || tip.querySelector('.mqr-img')) return;
        const img = document.createElement('img');
        img.className = 'mqr-img';
        img.alt = '';
        img.style.cssText = 'display:block;max-width:100%;max-height:170px;margin:0 auto 8px;'
                          + 'border-radius:6px;background:#fff;cursor:zoom-in;';
        img.onload = function() {
            if (window._mqrActiveX !== undefined) positionTip(window._mqrActiveX, window._mqrActiveY);
        };
        img.onerror = function() { img.remove(); };
        img.onclick = function() {
            const big = img.style.maxHeight === 'none';
            img.style.maxHeight = big ? '170px' : 'none';
            img.style.cursor = big ? 'zoom-in' : 'zoom-out';
        };
        img.src = src;
        box.parentNode.insertBefore(img, box);
    };
    window.mqrQuiet = function(rid) {
        if (isStale(rid)) return;
        clearTimeout(window._mqrLookupTimeout);
        if (!window._mqrTipLocked) { tip.style.display = 'none'; tip.innerHTML = ''; }
    };
    window.mqrNotFound = function(searchTerm, suggestions, rid) {
        if (isStale(rid)) return;
        clearTimeout(window._mqrLookupTimeout);
        window._mqrTipLocked = false;
        window._mqrCmdHeld = false;
        var term = searchTerm || (window._mqrActiveWord || '');
        if (!term) {
            tip.innerHTML = '<span style="color:var(--mqr-muted2);font-style:italic">No definition found</span>';
            setTimeout(hideTip, 2000);
            return;
        }
        // Abort if user moved away before result arrived
        if (tip.style.display === 'none') return;
        var enc = encodeURIComponent(term);
        var btnStyle = 'cursor:pointer;color:var(--mqr-link);font-size:11px;padding:2px 10px;'
                     + 'border:1px solid var(--mqr-divider);border-radius:10px;background:var(--mqr-chip-bg);'
                     + 'display:inline-block;margin-right:6px;';
        var suggHtml = '';
        if (suggestions && suggestions.length) {
            var scs = 'cursor:pointer;color:var(--mqr-link);font-size:10px;padding:1px 7px;'
                    + 'border:1px solid var(--mqr-divider);border-radius:9px;background:var(--mqr-chip-bg);'
                    + 'display:inline-block;margin:2px 4px 0 0;';
            suggHtml = '<div style="margin-bottom:7px;">'
                + '<span style="color:var(--mqr-muted2);font-size:10px">Did you mean: </span>'
                + suggestions.map(function(t) {
                    return '<span class="mqr-sugg-chip" data-sugg="' + escHtml(t) + '" style="' + scs + '">' + escHtml(t) + '</span>';
                  }).join('')
                + '</div>';
        }
        tip.innerHTML =
            '<div style="color:var(--mqr-muted2);font-style:italic;font-size:12px;margin-bottom:8px">'
            + 'No definition found for <b style="color:var(--mqr-muted3);font-style:normal">' + escHtml(term) + '</b></div>'
            + suggHtml
            + '<div>'
            + '<span id="mqr-pubmed-btn" style="' + btnStyle + '">PubMed ↗</span>'
            + '<span id="mqr-scholar-btn" style="' + btnStyle + '">Google ↗</span>'
            + '</div>';
        var pb = document.getElementById('mqr-pubmed-btn');
        var sb = document.getElementById('mqr-scholar-btn');
        document.querySelectorAll('.mqr-sugg-chip').forEach(function(el) {
            el.onmouseenter = function() { this.style.opacity = '0.65'; };
            el.onmouseleave = function() { this.style.opacity = '1'; };
            el.onclick = function() { lookupChip(this.getAttribute('data-sugg')); };
        });
        if (pb) pb.onclick = function() {
            window._mqrTipLocked = false; window._mqrCmdHeld = false;
            tip.style.display = 'none'; tip.innerHTML = '';
            pycmd('mqr:open:https://pubmed.ncbi.nlm.nih.gov/?term=' + enc);
        };
        if (sb) sb.onclick = function() {
            window._mqrTipLocked = false; window._mqrCmdHeld = false;
            tip.style.display = 'none'; tip.innerHTML = '';
            pycmd('mqr:open:SEARCH_ENGINE_URL' + enc);
        };
        // Re-position after content is rendered so offsetHeight is accurate
        if (window._mqrActiveX !== undefined) positionTip(window._mqrActiveX, window._mqrActiveY);
    };

    // ── Keyboard shortcuts ────────────────────────────────────────────────────
    // Current search settings live on window (refreshed on every injection) so
    // the once-registered listeners below pick up changes made in Settings.
    window._mqrSearchUrl    = 'SEARCH_ENGINE_URL';
    window._mqrImageUrl     = 'IMAGE_SEARCH_ENGINE_URL';
    window._mqrSearchPrefix = 'SEARCH_PREFIX';
    // Guard prevents duplicate listeners on repeated injections into same page.
    if (!window._mqrKbRegistered) {
        window._mqrKbRegistered = true;
        // Cmd+S / Ctrl+S — open highlighted text (or hovered word) in configured search engine
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && !e.shiftKey && !e.altKey &&
                (e.key === 'S' || e.key === 's')) {
                e.preventDefault();
                var selTxt = window.getSelection ? window.getSelection().toString().trim() : '';
                var searchFor = selTxt || window._mqrActiveWord || '';
                if (!searchFor) return;
                var prefix = window._mqrSearchPrefix;
                var query = prefix ? (prefix + ' ' + searchFor) : searchFor;
                pycmd('mqr:open:' + window._mqrSearchUrl + encodeURIComponent(query));
            }
        });
        // Cmd+I / Ctrl+I — image search for highlighted text or hovered word
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && !e.shiftKey && !e.altKey &&
                (e.key === 'I' || e.key === 'i')) {
                e.preventDefault();
                var selTxt = window.getSelection ? window.getSelection().toString().trim() : '';
                var searchFor = selTxt || window._mqrActiveWord || '';
                if (!searchFor) return;
                pycmd('mqr:open:' + window._mqrImageUrl + encodeURIComponent(searchFor));
            }
        });
        // ⌘ / Ctrl hold → lock tooltip open; release → unlock
        document.addEventListener('keydown', function(e) {
            if ((e.key === 'Meta' || e.key === 'Control') && !e.shiftKey) {
                if (tip.style.display === 'block' && !window._mqrCmdHeld) {
                    window._mqrCmdHeld = true;
                    window._mqrTipLocked = true;
                    var lk = document.createElement('div');
                    lk.id = 'mqr-cmd-lock';
                    lk.style.cssText = 'position:absolute;top:5px;right:7px;font-size:10px;color:var(--mqr-rel-fg);opacity:0.75;user-select:none;';
                    lk.textContent = '⌘';
                    tip.appendChild(lk);
                }
            }
        });
        document.addEventListener('keyup', function(e) {
            if ((e.key === 'Meta' || e.key === 'Control') && window._mqrCmdHeld) {
                window._mqrCmdHeld = false;
                window._mqrTipLocked = false;
                var lk = document.getElementById('mqr-cmd-lock');
                if (lk) lk.remove();
                setTimeout(hideTip, 200);
            }
        });
    }
})();
"""

# ─────────────────────────────────────────────────────────────────────────────
# 7 · DOM-ready injection with retry
# ─────────────────────────────────────────────────────────────────────────────

# Tooltip palette: every color in the tooltip HTML is var(--mqr-<name>).
# name: (dark, light)
_TIP_PALETTE = {
    "bg": ("#0d1b2a", "#ffffff"),            "fg": ("#d0daea", "#1f2933"),
    "fg2": ("#c8d8ea", "#24313f"),           "border": ("#2a3f5f", "#c9d3e0"),
    "divider": ("#1e3a5a", "#dbe3ec"),       "shadow": ("rgba(0,0,0,0.75)", "rgba(15,30,50,0.18)"),
    "title": ("#7aaee8", "#1d5fa6"),
    "badge-fg": ("#7aafe8", "#1d5fa6"),      "badge-bg": ("#1a3d5c", "#e3eefa"),
    "muted": ("#4a6a8e", "#66788c"),         "muted2": ("#6a7a8a", "#66727f"),
    "muted3": ("#8a9aaa", "#3f4b58"),        "muted4": ("#7090b0", "#5a6f86"),
    "info": ("#7a9fd4", "#3767ad"),          "link": ("#7ab8e8", "#1f6fb8"),
    "link2": ("#5a9fd4", "#1f6fb8"),         "chip-bg": ("#0d2035", "#eef4fb"),
    "rel-fg": ("#5abf8a", "#2e7d4f"),        "rel-border": ("#1e4a2a", "#b9dcc6"),
    "rel-bg": ("#0d2018", "#eef8f1"),
    "mn-fg": ("#c9a8e8", "#6b3fa0"),         "mn-border": ("#3a2a55", "#d8c8ee"),
    "mn-bg": ("#1a1228", "#f6f1fc"),         "mn-badge-bg": ("#2a1d40", "#ece3f8"),
    "mn-strong": ("#e8d4ff", "#4b2380"),
    # Section labels and "pearl" boxes of the offline dictionaries
    "lbl": ("#5a8fbf", "#2b6cb0"),           "lbl-teal": ("#3fa89e", "#1d7f75"),
    "lbl-purple": ("#9c7fc1", "#6b46a3"),    "lbl-gold": ("#c8a84b", "#8a6d1a"),
    "lbl-amber": ("#b07d3a", "#9a5b12"),     "lbl-rose": ("#d77a8f", "#a8324e"),
    "pill-bg": ("#112233", "#eef3f9"),       "pill-fg": ("#a0c0e0", "#234a73"),
    "pearl-bg": ("#0a1a10", "#eef7ee"),      "pearl-border": ("#2e7d32", "#2e7d32"),
    "pearl-fg": ("#80c080", "#25602a"),
    "teal-bg": ("#041a19", "#e9f7f6"),       "teal-fg": ("#6dd5ce", "#17665f"),
    "purple-bg": ("#130e1a", "#f5f0fb"),
    "amber-bg": ("#1a1200", "#fbf4e6"),      "amber-fg": ("#d4a843", "#7a5410"),
    "rose-bg": ("#1f0d12", "#fcf0f3"),       "rose-fg": ("#e3a3b2", "#8c2a42"),
    "crit-bg": ("#3a0a0a", "#fde8e8"),       "crit-fg": ("#ff6b6b", "#b42318"),
    "gene": ("#9b59b6", "#7d3c98"),
}


def _tip_style_css():
    def block(i):
        return ";".join(f"--mqr-{k}:{v[i]}" for k, v in _TIP_PALETTE.items())
    return f"#mqr-tip{{{block(0)}}}#mqr-tip.mqr-light{{{block(1)}}}"


_THEMES = ("Auto", "Dark", "Light")

_SEARCH_ENGINES = {
    "Google":     "https://www.google.com/search?q=",
    "Bing":       "https://www.bing.com/search?q=",
    "DuckDuckGo": "https://duckduckgo.com/?q=",
    "PubMed":     "https://pubmed.ncbi.nlm.nih.gov/?term=",
}
_IMAGE_SEARCH_ENGINES = {
    "Google Images":     "https://www.google.com/search?tbm=isch&q=",
    "Bing Images":       "https://www.bing.com/images/search?q=",
    "DuckDuckGo Images": "https://duckduckgo.com/?iax=images&ia=images&q=",
}


_last_injected_js: str = ""
_last_js_cfg_key: str = ""

def _inject_with_retry():
    global _last_injected_js, _last_js_cfg_key
    if not (mw.reviewer and mw.reviewer.web):
        return
    _cfg = _get_user_cfg()
    _cfg_key = "|".join(str(_cfg.get(k, d)) for k, d in [
        ("search_engine", "Google"), ("image_search_engine", "Google Images"),
        ("search_prefix", ""), ("tooltip_font_size", 12.5),
        ("hover_delay_ms", 300), ("min_word_len", 3), ("tooltip_theme", "Auto"),
        ("umls_timeout", 8), ("rxnorm_timeout", 6),
        ("openfda_timeout", 6), ("medlineplus_timeout", 5),
        ("wikipedia_timeout", 5), ("omim_timeout", 6),
    ])
    if _cfg_key == _last_js_cfg_key and _last_injected_js:
        mw.reviewer.web.eval(_last_injected_js)
        return
    # Build JS using config snapshot (already fetched above)
    _se  = _SEARCH_ENGINES.get(
               _cfg.get("search_engine", "Google"),
               "https://www.google.com/search?q=")
    _ise = _IMAGE_SEARCH_ENGINES.get(
               _cfg.get("image_search_engine", "Google Images"),
               "https://www.google.com/search?tbm=isch&q=")
    # Sanitize prefix for safe injection into a JS single-quoted string literal
    _prefix = str(_cfg.get("search_prefix", "")).strip()
    _prefix = _prefix.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ").replace("\r", "")
    _fsize  = str(_cfg.get("tooltip_font_size", 12.5))
    # Lookup timeout: give JS slightly more headroom than the slowest API tier
    _net_timeout_ms = (max(
        _cfg.get("umls_timeout",       8),
        _cfg.get("rxnorm_timeout",     6),
        _cfg.get("openfda_timeout",    6),
        _cfg.get("medlineplus_timeout", 5),
        _cfg.get("wikipedia_timeout",  5),
        _cfg.get("omim_timeout",       6),
    ) * 1000) + 1000
    _theme = _cfg.get("tooltip_theme", "Auto")
    if _theme not in _THEMES:
        _theme = "Auto"
    js = (_HOVER_JS_TEMPLATE
          .replace("TIP_STYLE_CSS",           json.dumps(_tip_style_css()))
          .replace("TOOLTIP_THEME",           _theme)
          .replace("HOVER_DELAY_MS",         str(_cfg.get("hover_delay_ms", 300)))
          .replace("MIN_WORD_LEN",            str(_cfg.get("min_word_len",   3)))
          .replace("TOOLTIP_FONT_SIZE",       _fsize)
          .replace("LOOKUP_TIMEOUT_MS",       str(_net_timeout_ms))
          # IMAGE_SEARCH_ENGINE_URL must be replaced BEFORE SEARCH_ENGINE_URL
          # because the latter is a substring of the former.
          .replace("IMAGE_SEARCH_ENGINE_URL", _ise)
          .replace("SEARCH_ENGINE_URL",       _se)
          .replace("STOPWORDS_JSON",          json.dumps(sorted(_STOPWORDS)))
          .replace("EVERYDAY_JSON",           json.dumps(sorted(_EVERYDAY)))
          .replace("SEARCH_PREFIX",           _prefix))
    _last_injected_js = js
    _last_js_cfg_key  = _cfg_key
    mw.reviewer.web.eval(js)


def _schedule_inject():
    QTimer.singleShot(CFG["inject_initial_delay_ms"], _inject_with_retry)

# ─────────────────────────────────────────────────────────────────────────────
# 8 · UMLS REST API  (API key sent directly with each request)
# ─────────────────────────────────────────────────────────────────────────────
#     UTS accepts ?apiKey=… on every REST call, so the old CAS sign-in
#     (ticket-granting ticket + one service ticket per request) is not needed:
#     a lookup is now 2 requests instead of 4.

def _umls_api_key():
    return (_get_user_cfg().get("umls_api_key") or CFG.get("umls_api_key", "")).strip()

# ─────────────────────────────────────────────────────────────────────────────
# 9 · API lookups
# ─────────────────────────────────────────────────────────────────────────────

_HEADERS = {"User-Agent": "AnkiMedQuickRef/7.0"}

# Function words that are never medical terms on their own.  A phrase that
# starts or ends with one ("with the mnemonic", "the best") is not a term
# either.  Upper-case forms (OR, ALL, AS) are still treated as abbreviations.
_STOPWORDS = frozenset("""
a an the and or but nor of in on at to for from by with without as is are was
were be been being am it its this that these those which who whom whose what
when where why how not no can could may might must shall should will would do
does did has have had if then than so such also very more most less least best
better all any some each every both either neither into onto over under after
before about between during through via per our your their his her they them
we you he she there here only just even often usually becomes become became
""".split())


def _is_stopword(word):
    return word.lower() in _STOPWORDS and not (len(word) > 1 and word.isupper())


# Everyday English words whose database / Wikipedia entries are plain
# dictionary senses ("Prior" → "Earlier in time or order.").  They are never
# looked up or underlined on their own, but still count inside a medical
# phrase ("Advanced maternal age", "Prior uterine surgery").
_EVERYDAY = frozenset("""
able above across actual actually add added adding additional affect affected
again against ago ahead aim allow allowed almost alone along already although
always among amount another answer apart appear appears applied apply approach
approximately area around arrive ask asked associated assume attempt available
average avoid away back bad based basic basis became begin beginning begins
behind believe below beside besides beyond big bigger biggest bring brings
brought build call called came cannot carry case cases cause certain certainly
chance change changed changes changing check choice choose clear clearly close
closely come comes coming common commonly compare compared complete completely
concern consider considered contain contains continue continued correct could
create current currently daily decide decrease decreased decreases decreasing
define defined definitely degree depend depends describe described despite
detail details develop developed develops did differ difference different
difficult directly done double down due early earlier easily easy effect else
end ended ending ends enough entire entirely equal especially essential even
event events eventually ever every everything exact exactly example except
exist exists expect expected explain extra extremely fact fail fails
far fast feature features few fewer final finally find finding fine first
follow followed following follows form forms forward found four free frequent
frequently full fully further gain general generally get gets give given gives
giving go goes going gone good got great greater greatest group grow half hand
happen happens hard help helps high higher highest highly hold however huge
idea identify immediate immediately important include included includes
including increase increased increases increasing indeed indicate indicates
instead involve involved involves keep kept key kind know known large largely
larger largest last late later latter learn least leave led less let
level levels like likely limit limited line little long longer look looks lot
low lower lowest made main mainly make makes making many mark marked matter
mean means measure meet mild mildly minor moderate moderately moment much
multiple must name named near nearly necessary need needed needs never new next
nine none normally note noted nothing notice now number numbers obvious occur
occurred occurring occurs offer old older once one ones open order other others
otherwise out outside overall own part partial partially particular particularly
past perhaps place placed plus point points possible possibly potential prefer
preferred present presence presents previous previously primarily prior
probably problem problems produce produced proper properly prove provide
provided provides put quick quickly quite rapid rapidly rare rarely rate rather
reach read ready real really reason recent recently reduce reduced reduces
reducing regarding related relatively remain remains remember remembered remove
removed require required requires result resulted results return returns reveal
right rise rises same say says second seem seems seen select send separate
serious set seven several severe severely shall short show showed showing shown
shows side significant significantly similar similarly simple simply since
single situation six size slight slightly slow slowly small smaller smallest
sometimes soon sort specific specifically start started starts state stated
step still stop strong strongly sudden suddenly suggest suggests support sure
take taken takes taking tend tends term terms third though thought three
throughout thus together told too took total toward towards true try trying
turn turns twice two type types typical typically unable under understand
unless unlike unlikely until unusual upon use used useful uses using usual
value various versus view want way ways well went whether while whole widely
within word words work works worse worst write yet
""".split())


def _is_everyday(word):
    return (word.lower() in _EVERYDAY and " " not in word.strip()
            and not (len(word) > 1 and word.isupper()))


def _is_stop_phrase(phrase):
    words = phrase.split()
    if not words:
        return True
    if not (_is_stopword(words[0]) or _is_stopword(words[-1])):
        return False
    # Real terms that begin or end with a function word ("hepatitis A",
    # "vitamin A", "bundle of His", "living will", "HAS BLED") are kept when
    # an enabled offline dictionary has them.
    return phrase.strip().lower().replace("’", "'") not in _get_offline_keys()


# Offline keys that are acronyms but also ordinary words: they only match
# when written in capitals, so "heart", "map" or "muscle power" are not
# answered with the HEART score, Mean Arterial Pressure or statistical power.
_ACRONYM_WORDS = frozenset("""
alp alt ana ast bun cage cap grace heart honk lama map meld news nexus pac power pud sofa
hit mds pad pan taco tips
""".split())


def _acronym_mismatch(phrase):
    p = (phrase or "").strip()
    return " " not in p and p.lower() in _ACRONYM_WORDS and not p.isupper()


# Salt and formulation words: "metoprolol succinate" or "warfarin sodium"
# should show the drug's own entry, not a bare database definition of the salt.
_DRUG_FORM_WORDS = frozenset("""
sodium potassium calcium magnesium hydrochloride hcl sulfate citrate maleate mesylate
tartrate succinate besylate acetate phosphate bromide chloride fumarate monohydrate
er xr sr xl cr dr la tablet tablets capsule capsules injection oral iv
""".split())


# Generic qualifiers: "serum sodium", "elevated troponin" or "high-dose
# aspirin" are still the curated sodium / troponin / aspirin entries.
_QUALIFIER_WORDS = frozenset("""
serum plasma blood urine level levels value values concentration test total
high low elevated raised increased decreased reduced normal abnormal
dose doses dosing high-dose low-dose therapy treatment drug
""".split()) - {"urine"}   # "urine sodium" has its own lab entry


def _curated_core(phrase):
    """The single curated term inside a qualified phrase ("serum sodium" →
    "sodium", "metoprolol succinate" → "metoprolol"), or ""."""
    core = [w for w in phrase.split() if w.lower() not in _QUALIFIER_WORDS]
    if (len(core) > 1 and core[0].lower() in _DRUGS
            and all(w.lower() in _DRUG_FORM_WORDS for w in core[1:])):
        core = core[:1]
    return core[0] if len(core) == 1 and core[0] != phrase.strip() else ""


_COMMON_ENGLISH = {
    "with","that","this","from","have","been","will","they","their","them",
    "when","what","which","where","into","over","more","some","none","also",
    "just","only","even","here","there","after","before","about","through",
    "each","such","both","many","most","very","then","than","does","your",
    "were","would","could","should","make","take","come","give","know",
    "time","year","back","good","high","long","look","turn","hand","part",
    "case","same","well","work","life","form","body","cell","base","lead",
    "type","rate","side","test","drug","dose","risk","sign","like","name",
    "note","left","right","loss","free","pain","level","early","late","mild",
    "next","first","last","other","under","often","seen","found","used","shown",
    "small","large","upper","lower","inner","outer","major","minor","normal",
}


def _get_json(url, timeout=8):
    req = urllib.request.Request(url, headers=_HEADERS)
    try:
        with _urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None


# Real tags only: "<p>", "</b>", "<br/>" — not "<36 degrees C" or "< 5 microns"
_TAG_RE = re.compile(r"</?[A-Za-z][A-Za-z0-9]*(?:\s[^<>]*)?/?>")


def _plain_html(text, limit=None):
    """Text from the DB or a web API, made safe for the tooltip: markup is
    dropped, then the text is HTML-escaped so a stray "<" (or injected
    markup) cannot break the tooltip or run in the reviewer."""
    text = " ".join(html.unescape(_TAG_RE.sub(" ", text or "")).split())
    if limit:
        text = text[:limit]
    return html.escape(text, quote=False)


# ── UMLS REST API ─────────────────────────────────────────────────────────────

_UMLS_DEF_PRIORITY = {
    "MSH": 1, "NCI": 2, "MEDLINEPLUS": 3, "CSP": 4, "HPO": 5,
    "SNOMEDCT_US": 6, "RXNORM": 7, "GO": 8,
}


_UMLS_NON_ENGLISH = re.compile(
    r"(CZE|NOR|POR|SPA|SWE|FRE|GER|ITA|JPN|DUT|FIN|RUS|KOR|CHI|POL|HUN|TUR|LAV|"
    r"EST|SCR|BAQ|HEB|GRE|DAN|UKR|ARA|PER|HRV)$")


def _lookup_umls_api(phrase):
    """Search UMLS REST API for phrase.  Returns (defn, url, sem_type) or ('','','')."""
    api_key = _umls_api_key()
    if not api_key:
        return "", "", ""
    _to = _user_cfg_get("umls_timeout", 8)
    k = urllib.parse.quote(api_key)
    data = _get_json(
        "https://uts-ws.nlm.nih.gov/rest/search/current"
        f"?string={urllib.parse.quote(phrase)}&searchType=normalizedString"
        f"&returnIdType=concept&pageSize=1&apiKey={k}",
        timeout=_to
    )
    if not data:
        return "", "", ""
    results = (data.get("result") or {}).get("results", [])
    if not results or results[0].get("ui") in ("NONE", None, ""):
        return "", "", ""

    cui = results[0]["ui"]
    concept_url = f"https://uts.nlm.nih.gov/uts/umls/concept/{cui}"
    sem_type = ""

    def_data = _get_json(
        f"https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{cui}"
        f"/definitions?pageSize=100&apiKey={k}",
        timeout=_to
    )
    if def_data and def_data.get("result"):
        best_defn, best_pri = "", 999
        for d in def_data["result"]:
            src = d.get("rootSource", "")
            # Translated vocabularies (MSHCZE, MSHPOR, SCTSPA …) are not English
            if _UMLS_NON_ENGLISH.search(src):
                continue
            pri = _UMLS_DEF_PRIORITY.get(src, 50)
            if pri < best_pri and d.get("value"):
                best_defn = d["value"]
                best_pri  = pri
        if best_defn:
            return _plain_html(best_defn, _max_chars()), concept_url, sem_type

    return "", concept_url, sem_type


# ── RxNorm drug identification ────────────────────────────────────────────────

def _lookup_rxnorm(phrase):
    """Returns (definition, url) or ('', ''). No API key needed."""
    _to  = _user_cfg_get("rxnorm_timeout", 6)
    q    = urllib.parse.quote(phrase)
    # drugs.json only returns dose forms (SCD/SBD…), never the IN/BN groups
    # used below — resolve the RxCUI first, then ask for its ingredient + brands.
    ids  = _get_json(f"https://rxnav.nlm.nih.gov/REST/rxcui.json?name={q}&search=2", timeout=_to)
    rxcuis = ((ids or {}).get("idGroup") or {}).get("rxnormId") or []
    if not rxcuis:
        return "", ""
    data = _get_json(
        f"https://rxnav.nlm.nih.gov/REST/rxcui/{rxcuis[0]}/related.json?tty=IN+BN",
        timeout=_to)
    if not data:
        return "", ""
    groups = (data.get("relatedGroup") or {}).get("conceptGroup") or []
    ingredients, brands = [], []
    for grp in groups:
        tty = grp.get("tty", "")
        for prop in grp.get("conceptProperties") or []:
            name  = prop.get("name", "")
            rxcui = prop.get("rxcui", "")
            if tty == "IN"  and name: ingredients.append((name, rxcui))
            elif tty == "BN" and name: brands.append(name)
    if not ingredients and not brands:
        return "", ""
    if ingredients:
        name, rxcui = ingredients[0]
        brand_str   = f" · Brands: {', '.join(brands[:3])}" if brands else ""
        defn = html.escape(f"Drug (ingredient: {name}{brand_str}).", quote=False)
        return defn, f"https://mor.nlm.nih.gov/RxNav/search?searchBy=RXCUI&searchTerm={rxcui}"
    return "Prescription drug (brand name).", ""


# ── NLM MedlinePlus ───────────────────────────────────────────────────────────

def _lookup_medlineplus(phrase):
    """MedlinePlus health-topic summary via the NLM search web service (XML).
    Only accepts a topic whose title, alternate title or MeSH heading matches
    the phrase, so e.g. "placenta previa" is not answered with a general
    "Childbirth Problems" summary."""
    _to = _user_cfg_get("medlineplus_timeout", 5)
    url = ("https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&retmax=5&term="
           + urllib.parse.quote(phrase))
    try:
        req = urllib.request.Request(url, headers=_HEADERS)
        with _urlopen(req, timeout=_to) as resp:
            root = ET.fromstring(resp.read())
    except Exception:
        return "", ""
    want = " ".join(phrase.lower().split())
    for doc in root.iter("document"):
        names, summary, snippet = set(), "", ""
        for item in doc.findall("content"):
            kind = item.get("name", "")
            text = "".join(item.itertext())
            if kind in ("title", "altTitle", "mesh"):
                # Titles carry search-highlight markup: <span class="qt0">Asthma</span>
                text = re.sub(r"<[^>]+>", "", text)
                names.add(" ".join(text.lower().split()))
            elif kind == "FullSummary":
                summary = text
            elif kind == "snippet":
                snippet = text
        if want not in names:
            continue
        clean = " ".join(_TAG_RE.sub(" ", html.unescape(summary or snippet)).split())
        clean = re.sub(r"\s+([?.,;:!])", r"\1", clean)   # "asthma ?" → "asthma?"
        if len(clean) > 60:
            return _plain_html(clean, _max_chars()), doc.get("url", "")
    return "", ""


# ── Wikipedia ─────────────────────────────────────────────────────────────────

_WIKI_NON_MED = ("in physics", "in chemistry", "in mathematics", "in engineering",
                 "in music", "in computing", "is a film", "is a novel", "is a song",
                 "is an album", "is a video game", "is a television")

# phrase (lowercase) → thumbnail URL, or "" when the article has none
_thumb_cache: dict = {}
_thumb_lock = threading.Lock()


def _wiki_summary(slug):
    """Wikipedia page summary for a title, or None if it is missing, a
    disambiguation page, or plainly not a medical article."""
    data = _get_json(
        "https://en.wikipedia.org/api/rest_v1/page/summary/"
        + urllib.parse.quote(slug, safe=""),
        timeout=_user_cfg_get("wikipedia_timeout", 5)
    )
    if not data or not data.get("extract") or data.get("type") == "disambiguation":
        return None
    if any(p in data["extract"].lower() for p in _WIKI_NON_MED):
        return None
    return data


def _wiki_thumb_url(data):
    """Thumbnail URL from a page summary — Wikimedia's own image hosts only."""
    src = ((data or {}).get("thumbnail") or {}).get("source", "")
    ok = src.startswith(("https://upload.wikimedia.org/", "https://thumb.wikimedia.org/"))
    return src if ok else ""


def _lookup_wikipedia(phrase):
    base = phrase.replace(" ", "_")
    # Plain title first: most terms have their own article.  The suffixed
    # titles ("Shock_(medicine)") are only tried for single words — multi-word
    # phrases almost never need them, and each costs another request.
    slugs = (base,) if " " in phrase.strip() else (base, base + "_(medicine)", base + "_(disease)")
    for slug in slugs:
        data = _wiki_summary(slug)
        if data:
            with _thumb_lock:
                _thumb_cache[phrase.lower()] = _wiki_thumb_url(data)
            url = ((data.get("content_urls") or {}).get("desktop", {}).get("page", ""))
            return _plain_html(data["extract"], _max_chars()), url
    return "", ""


def _wiki_thumb(phrase):
    """Wikipedia thumbnail URL for a looked-up term ('' if none).  "liver
    anatomy" falls back to the "Liver" article.  Results (including misses)
    are cached, so each term costs at most one request per session."""
    key = (phrase or "").strip().lower()
    if not key:
        return ""
    with _thumb_lock:
        if key in _thumb_cache:
            return _thumb_cache[key]
    url = ""
    titles = [key]
    if key.endswith(" anatomy"):
        titles.append(key[:-len(" anatomy")])
    for title in titles:
        url = _wiki_thumb_url(_wiki_summary(title.replace(" ", "_")))
        if url:
            break
    with _thumb_lock:
        if len(_thumb_cache) >= 2000:   # long sessions: keep memory bounded
            _thumb_cache.clear()
        _thumb_cache[key] = url
    return url


def _send_image(phrase, rid):
    """Worker thread: fetch the term's picture and add it to the tooltip."""
    if not _user_cfg_get("wikipedia_images", True):
        return
    src = _wiki_thumb(phrase)
    if not src:
        return
    rid_js = json.dumps(rid if isinstance(rid, int) else None)
    def _push():
        web = mw.reviewer.web if mw.reviewer else None
        if web:
            web.eval(f"if(window.mqrImage) mqrImage({json.dumps(src)}, {rid_js});")
    mw.taskman.run_on_main(_push)


# ── OMIM genetic disease lookup (Tier 6.5) ───────────────────────

_OMIM_GENETICS_KW = frozenset([
    "syndrome", "disease", "disorder", "deficiency", "dystrophy",
    "atrophy", "dysplasia", "mutation", "gene", "chromosome",
    "trisomy", "monosomy", "deletion", "anemia", "aciduria",
    "acidemia", "neuropathy", "myopathy", "leukemia", "lymphoma",
    "fibrosis", "sclerosis", "malformation", "tumor", "carcinoma",
])


def _lookup_omim(phrase):
    """Tier 6.5: OMIM genetic disease lookup. Returns (defn, url) or ('', '').

    Quality-gated: only queries OMIM when the phrase contains a gene-symbol-like
    token (all-caps, 2-8 alphanumeric chars e.g. BRCA1, TP53) or a recognised
    genetic-disease keyword.  This prevents OMIM's broad full-text search from
    matching random symptom phrases like "profound hypotonia".
    """
    api_key = (_get_user_cfg().get("omim_api_key") or CFG.get("omim_api_key", "")).strip()
    if not api_key:
        return "", ""
    # Gate: only proceed for gene-symbol-like tokens or genetics keywords
    _words_lc = phrase.lower().split()
    _has_gene_sym = any(
        re.match(r'^[A-Z][A-Z0-9]{1,7}$', w)
        for w in phrase.split()
    )
    _has_kw = bool(set(_words_lc) & _OMIM_GENETICS_KW)
    if not (_has_gene_sym or _has_kw):
        return "", ""
    q = urllib.parse.quote(phrase)
    url = (
        f"https://api.omim.org/api/entry/search?search={q}"
        f"&format=json&apiKey={urllib.parse.quote(api_key)}&retrieve=title,geneMap&start=0&limit=1"
    )
    data = _get_json(url, timeout=_user_cfg_get("omim_timeout", 6))
    if not data:
        return "", ""
    try:
        results = data["omim"]["searchResponse"]["entryList"]
        if not results:
            return "", ""
        entry = results[0]["entry"]
        mim   = entry.get("mimNumber", "")
        title = entry.get("titles", {}).get("preferredTitle", "")
        gene  = ""
        gm    = entry.get("geneMap", {})
        if gm:
            gene = gm.get("geneName", "") or gm.get("geneSymbols", "")
        if not title:
            return "", ""
        defn = f"<b>{html.escape(title, quote=False)}</b>"
        if gene:
            defn += f"<br><span style='color:var(--mqr-gene);font-size:11px'>Gene: {html.escape(str(gene), quote=False)}</span>"
        if mim:
            defn += f"<br><span style='color:var(--mqr-muted2);font-size:10px'>MIM# {mim}</span>"
        omim_url = f"https://www.omim.org/entry/{mim}" if mim else "https://www.omim.org"
        return defn, omim_url
    except (KeyError, IndexError, TypeError):
        return "", ""

# ── OpenFDA Drug Labels (mechanism, indications, warnings, adverse effects) ───

def _lookup_openfda(phrase):
    """
    Queries the OpenFDA drug label API.
    Returns (definition, url) or ('', '').
    Extracts: mechanism of action, indications, contraindications,
              boxed warnings, adverse reactions — formatted for Step 1/2/3.
    """
    def _clean(text, max_len=200):
        """Strip legal boilerplate, excessive whitespace, section numbers."""
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'^\d+(\.\d+)*\s+', '', text)   # strip leading "1.1 "
        # Labels repeat their section heading: "Mechanism of Action Warfarin…"
        text = re.sub(r'^(mechanism of action|indications (and|&) usage|'
                      r'contraindications|boxed warning|warning|adverse reactions)'
                      r'\s*:?\s*', '', text, flags=re.I)
        text = re.sub(r'\(see [^\)]+\)', '', text, flags=re.I)
        return text[:max_len].rsplit(' ', 1)[0] + '…' if len(text) > max_len else text

    _to = _user_cfg_get("openfda_timeout", 6)
    q = urllib.parse.quote(f'"{phrase}"')
    # One OR query over generic / brand / substance name (was 3 requests)
    search = "+".join(f"{f}:{q}" for f in
                      ("openfda.generic_name", "openfda.brand_name", "openfda.substance_name"))
    data = _get_json(f"https://api.fda.gov/drug/label.json?search={search}&limit=5",
                     timeout=_to)
    if not data or not data.get("results"):
        return "", ""
    # Field search matches any label whose name merely *contains* the words,
    # so require the name to be the phrase itself ("warfarin" → "WARFARIN SODIUM").
    want = " ".join(phrase.lower().split())
    # Extra words allowed after the drug name: salt / release forms only,
    # so "warfarin" matches "WARFARIN SODIUM" but "the" never matches "THE BEST CREAM".
    salts = {"sodium", "potassium", "calcium", "magnesium", "hydrochloride", "hcl",
             "sulfate", "citrate", "maleate", "mesylate", "tartrate", "succinate",
             "besylate", "acetate", "phosphate", "bromide", "chloride", "fumarate",
             "monohydrate", "dihydrate", "trihydrate", "er", "xr", "sr", "xl",
             "extended-release", "delayed-release"}
    def _is_name(n):
        n = " ".join(n.lower().split())
        if n == want:
            return True
        return n.startswith(want + " ") and all(w in salts for w in n[len(want):].split())
    def _name_match(res):
        of = res.get("openfda") or {}
        names = of.get("generic_name", []) + of.get("brand_name", []) + of.get("substance_name", [])
        return any(_is_name(n) for n in names)
    r = next((res for res in data["results"] if _name_match(res)), None)
    if r is None:
        return "", ""

    def first(key):
        val = r.get(key, [])
        return val[0].strip() if val else ""

    parts = []

    # Drug class from openfda
    classes = (r.get("openfda") or {}).get("pharm_class_epc", [])
    if classes:
        parts.append(f"Class: {classes[0].replace(' [EPC]','')}")

    # Mechanism of action — most important
    moa = first("mechanism_of_action")
    if moa:
        parts.append(f"MOA: {_clean(moa, 220)}")

    # Indications
    ind = first("indications_and_usage")
    if ind:
        # Trim to first sentence or 150 chars
        sent = re.split(r'(?<=[.!?])\s', ind)
        parts.append(f"Use: {_clean(sent[0], 150)}")

    # Boxed warning (if any)
    bw = first("boxed_warning")
    if bw:
        parts.append(f"⚠ {_clean(bw, 120)}")

    # Contraindications
    ci = first("contraindications")
    if ci:
        parts.append(f"CI: {_clean(ci, 120)}")

    # Key adverse reactions
    ar = first("adverse_reactions")
    if ar:
        # Just grab first sentence
        sent = re.split(r'(?<=[.!?])\s', ar)
        parts.append(f"ADR: {_clean(sent[0], 120)}")

    if not parts:
        return "", ""

    defn = _plain_html(" | ".join(parts))
    openfda = r.get("openfda", {})
    rxcui = (openfda.get("rxcui") or [""])[0]
    url = f"https://mor.nlm.nih.gov/RxNav/search?searchBy=RXCUI&searchTerm={rxcui}" if rxcui else ""
    return defn, url


# ─────────────────────────────────────────────────────────────────────────────
# 9b · Batch term-existence check (for card highlighting)
# ─────────────────────────────────────────────────────────────────────────────

_offline_keys_cache: dict = {}   # enabled-tier tuple → set of lowercase keys
_offline_keys_lock = threading.Lock()   # prevents double-build from concurrent threads


def _tier_key_dicts():
    """Dictionaries (entries + alternate names) behind each offline tier."""
    return {
        "tier_01_abbrev":          (_ABBREV_TERMS,),
        "tier_05_drug_individual": (_DRUGS, _DRUG_BRAND_ALIASES),
        "tier_05a_drug_class":     (_DRUG_CLASSES, _DRUG_CLASS_ALIASES),
        "tier_05b_lab_range":      (_LAB_RANGES, _LAB_ALIASES),
        "tier_05c_disease":        (_DISEASES, _DISEASE_ALIASES),
        "tier_05d_micro":          (_MICRO, _MICRO_ALIASES),
        "tier_05e_scoring":        (_SCORES, _SCORE_ALIASES),
        "tier_05f_anatomy":        (_ANATOMY, _ANATOMY_ALIASES),
        "tier_05g_biostats":       (_BIOSTATS,),
        "tier_05h_syndromes":      (_SYNDROMES,),
        "tier_05i_ecg":            (_ECG_FINDINGS,),
        "tier_05j_genetics":       (_GENETICS,),
        "tier_05k_radiology":      (_RADIOLOGY,),
        "tier_05l_pathology":      (_PATHOLOGY, _PATHOLOGY_ALIASES),
        "tier_05m_signs":          (_SIGNS, _SIGN_ALIASES),
        "tier_05n_basic_science":  (_BASIC_SCIENCE, _BASIC_SCIENCE_ALIASES),
        "tier_05o_obgyn":          (_OBGYN, _OBGYN_ALIASES),
        "tier_05p_primary_care":   (_PRIMARY_CARE, _PRIMARY_CARE_ALIASES),
    }


def _get_offline_keys() -> set:
    """Lowercase keys of every ENABLED offline dictionary (entries and
    alternate names), so only terms that can be answered get underlined.
    Built once per combination of enabled tiers."""
    cfg = _get_user_cfg()
    enabled = tuple(k for k, _, _, _ in _OFFLINE_TIERS if cfg.get(k, True))
    keys = _offline_keys_cache.get(enabled)
    if keys is not None:
        return keys
    with _offline_keys_lock:
        keys = _offline_keys_cache.get(enabled)
        if keys is None:
            dicts = _tier_key_dicts()
            keys = set()
            for tier in enabled:
                for d in dicts.get(tier, ()):
                    keys.update(k.lower() for k in d)
            _offline_keys_cache[enabled] = keys
    return keys


def _batch_check(words):
    """
    Given a list of words/phrases, return the subset that have definitions
    in any offline tier or the local SQLite DB.  Network tiers skipped
    intentionally — this runs on every card load and must be fast.
    """
    recognized = set()
    db          = _get_db()
    offline     = _get_offline_keys()
    needs_db    = []                        # words that need SQLite lookup
    min_len     = _min_word_len()
    abbrev_on   = _get_user_cfg().get("tier_01_abbrev", True)
    for w in words:
        if _is_stopword(w) or _is_everyday(w):
            continue
        wl = w.lower().replace("\u2019", "'")   # curly → straight apostrophe
        # check uppercase abbreviation dict (BP, HR, SpO2 …)
        if abbrev_on and (w in _ABBREVS or (_looks_like_abbrev(w) and w.upper() in _ABBREVS)):
            recognized.add(w)
            continue
        # check all other offline dicts (lowercase keys), singular or plural
        if not _acronym_mismatch(w) and (
                wl in offline or any(v.lower() in offline and not _acronym_mismatch(v)
                                     for v in _number_variants(w))):
            recognized.add(w)
            continue
        if len(w) < min_len:
            continue
        # queue for single batch SQLite lookup below
        if db:
            needs_db.append(w)
    # ── single IN (…) query — ~80-90 % faster than N individual round-trips ──
    if db and needs_db:
        try:
            matched = set()
            # Chunked: older SQLite builds allow at most 999 bound variables
            for i in range(0, len(needs_db), 900):
                chunk = [w.replace("\u2019", "'") for w in needs_db[i:i + 900]]
                ph    = ",".join("?" * len(chunk))
                rows  = db.execute(
                    f"SELECT term FROM terms WHERE term IN ({ph})", chunk
                ).fetchall()
                matched.update((r[0].lower(), r[0]) for r in rows)
            matched = dict(matched)
            for w in needs_db:
                db_term = matched.get(w.lower().replace("\u2019", "'"))
                if db_term and _case_ok(db_term, w):
                    recognized.add(w)
        except Exception as _e:
            print(f"[MQR] DB term recognition error: {_e}", file=sys.stderr)
    return list(recognized)


# ─────────────────────────────────────────────────────────────────────────────
# 10 · Lookup orchestration — tiers 0–6
# ─────────────────────────────────────────────────────────────────────────────


# ── Syndrome dictionary (offline, instant) ────────────────────────────────────


_add_aliases(_SYNDROMES, {"tumor lysis": "tumor lysis syndrome"})

def _lookup_syndrome(phrase):
    """Tier 0.5h: Check syndrome dictionary. Returns HTML or empty."""
    return _SYNDROMES.get(phrase.strip().lower(), "")


# ── ECG findings dictionary (offline, instant) ────────────────────────────────
_add_aliases(_ECG_FINDINGS, {
    'left ventricular hypertrophy': 'lvh',
    'right ventricular hypertrophy': 'rvh',
    'wellens sign': 'wellens syndrome',
    'de winter pattern': 'de winter t waves',
    'u waves': 'u wave',
    'low voltage': 'low voltage qrs',
    'aivr': 'accelerated idioventricular rhythm',
    'capture beat': 'fusion beat',
    'fusion beats': 'fusion beat',
    'capture beats': 'fusion beat',
    'corrected qt': 'qtc',
    'lpfb': 'left posterior fascicular block',
    'second-degree av block': 'second degree av block',
    '2nd degree av block': 'second degree av block',
})


def _lookup_ecg(phrase):
    """Tier 0.5i: Check ECG findings dictionary. Returns HTML or empty."""
    return _ECG_FINDINGS.get(phrase.strip().lower(), "")


# ── Genetics dictionary (offline, instant) ───────────────────────────────────
_add_aliases(_GENETICS, {
    'hardy-weinberg equilibrium': 'hardy-weinberg',
    'hardy weinberg': 'hardy-weinberg',
    'hardy weinberg equilibrium': 'hardy-weinberg',
    'trisomy 18': 'edwards syndrome',
    'trisomy 13': 'patau syndrome',
    'cri du chat': 'cri du chat syndrome',
    'cri-du-chat syndrome': 'cri du chat syndrome',
    'lyonization': 'x-inactivation',
    'barr body': 'x-inactivation',
    'x inactivation': 'x-inactivation',
    'dmd': 'duchenne muscular dystrophy',
    'myotonic dystrophy type 1': 'myotonic dystrophy',
    "friedreich's ataxia": 'friedreich ataxia',
    "edwards' syndrome": 'edwards syndrome',
    'de novo mutations': 'de novo mutation',
})


def _lookup_genetics(phrase):
    """Tier 0.5j: Check genetics dictionary. Returns HTML or empty."""
    return _GENETICS.get(phrase.strip().lower(), "")


# ── Radiology dictionary (offline, instant) ──────────────────────────────────
_add_aliases(_RADIOLOGY, {
    'ring enhancing lesions': 'ring enhancing lesion',
    'ring-enhancing lesion': 'ring enhancing lesion',
    'pencil in cup': 'pencil-in-cup deformity',
    'pencil-in-cup': 'pencil-in-cup deformity',
    'dense mca sign': 'hyperdense mca sign',
    'thumbprinting sign': 'thumbprinting',
    'free air': 'pneumoperitoneum',
    'lead pipe sign': 'lead pipe colon',
})


def _lookup_radiology(phrase):
    """Tier 0.5k: Check radiology dictionary. Returns HTML or empty."""
    return _RADIOLOGY.get(phrase.strip().lower(), "")

_add_aliases(_RADIOLOGY, {
    'lambda sign': 'twin peak sign',
    't sign': 'twin peak sign',
    'necklace sign': 'string of pearls sign',
    'cluster of grapes': 'snowstorm pattern',
    'snowstorm appearance': 'snowstorm pattern',
    'tubal ring sign': 'ring of fire sign',
})

# ── Pathology dictionary (offline, instant) ──────────────────────────────────



def _lookup_pathology(phrase):
    """Tier 0.5l: Check pathology dictionary. Returns HTML or empty."""
    key = phrase.strip().lower()
    return _PATHOLOGY.get(_PATHOLOGY_ALIASES.get(key, key), "")


# ── Tier 0.5m · Clinical signs & eponyms (offline, instant) ──────────────────



# Possessive and alternate spellings, as cards write them
# "murphy's sign", "beck's triad", "osler's nodes" … for every two-word key
for _k in list(_SIGNS):
    _first, _, _rest = _k.partition(" ")
    if _rest and " " not in _rest and not _first.endswith("s"):
        _SIGN_ALIASES.setdefault(f"{_first}'s {_rest}", _k)


def _lookup_sign(phrase):
    """Tier 0.5m: Check clinical signs dictionary. Returns HTML or empty."""
    key = phrase.strip().lower()
    return _SIGNS.get(_SIGN_ALIASES.get(key, key), "")


# ── Tier 0.5n · Basic sciences: pharmacology, immunology, biochemistry ───────



def _lookup_basic_science(phrase):
    """Tier 0.5n: Check the basic-sciences dictionary. Returns HTML or empty."""
    key = phrase.strip().lower()
    return _BASIC_SCIENCE.get(_BASIC_SCIENCE_ALIASES.get(key, key), "")

# ── Tier 0.5o · OB/GYN topics: labor, fetal monitoring, prenatal care, screening ──





def _lookup_obgyn(phrase):
    """Tier 0.5o: Check the OB/GYN topics dictionary. Returns HTML or empty."""
    key = phrase.strip().lower()
    return _OBGYN.get(_OBGYN_ALIASES.get(key, key), "")

# ── Tier 0.5p · Primary care: screening, prevention, office approaches ──





def _lookup_primary_care(phrase):
    """Tier 0.5p: Check the primary-care topics dictionary. Returns HTML or empty."""
    key = phrase.strip().lower()
    return _PRIMARY_CARE.get(_PRIMARY_CARE_ALIASES.get(key, key), "")

# ── Related terms map (term → [related, …]) ──────────────────────────────────


# Lowercase index — _RELATED has mixed-case keys (INR, HbA1c, BNP …) but
# lookups use phrase.lower().
_RELATED_LC = {k.lower(): v for k, v in _RELATED.items()}


def _related_for(phrase):
    """Related-term chips for a looked-up phrase.  Alternate names ("PPH",
    "Pitocin") use the chips of the entry they point to."""
    key = (phrase or "").strip().lower()
    hit = _RELATED_LC.get(key)
    if hit is None:
        for aliases in (_DISEASE_ALIASES, _OBGYN_ALIASES, _PRIMARY_CARE_ALIASES, _DRUG_BRAND_ALIASES,
                        _LAB_ALIASES, _SCORE_ALIASES, _SIGN_ALIASES, _MICRO_ALIASES,
                        _BASIC_SCIENCE_ALIASES, _PATHOLOGY_ALIASES, _DRUG_CLASS_ALIASES,
                        _ANATOMY_ALIASES):
            canon = aliases.get(key)
            if canon and canon.lower() in _RELATED_LC:
                hit = _RELATED_LC[canon.lower()]
                break
    return [r for r in (hit or []) if r.lower() != key]


_sugg_pairs_cache: list = []   # built lazily, cleared if dicts reload

def _find_suggestions(candidates):
    """Fuzzy-match candidates against all offline dicts to suggest alternatives."""
    global _sugg_pairs_cache
    if not _sugg_pairs_cache:
        all_dicts = [
            _ABBREVS, _ABBREV_TERMS, _DRUGS, _DRUG_CLASSES, _DISEASES, _MICRO,
            _LAB_RANGES, _ANATOMY, _BIOSTATS, _SCORES, _SYNDROMES, _ECG_FINDINGS,
            _GENETICS, _RADIOLOGY, _PATHOLOGY, _SIGNS, _BASIC_SCIENCE, _OBGYN, _PRIMARY_CARE,
            # Alias dicts — brand names, disease shorthand, score/lab variants, related terms
            _DRUG_BRAND_ALIASES, _DISEASE_ALIASES, _SCORE_ALIASES, _LAB_ALIASES, _RELATED,
            _ANATOMY_ALIASES, _SIGN_ALIASES, _MICRO_ALIASES, _PATHOLOGY_ALIASES,
            _BASIC_SCIENCE_ALIASES, _DRUG_CLASS_ALIASES, _OBGYN_ALIASES, _PRIMARY_CARE_ALIASES,
        ]
        _sugg_pairs_cache = [(k.lower(), k) for d in all_dicts for k in d]
    # (lowercase_key, original_key) pairs for case-insensitive matching
    all_pairs = _sugg_pairs_cache
    query = (candidates[-1] if candidates else "").lower().strip()
    if not query or len(query) < 3:
        return []
    prefix  = [k for lk, k in all_pairs if lk.startswith(query) and lk != query]
    taken   = set(prefix)
    substr  = [k for lk, k in all_pairs if query in lk and k not in taken and lk != query]
    taken.update(substr)
    qwords  = set(query.split())
    overlap = [k for lk, k in all_pairs
               if qwords & set(lk.split()) and k not in taken and lk != query]
    results = prefix[:3] + substr[:2] + overlap[:2]
    seen, unique = set(), []
    for r in results:
        if r not in seen:
            seen.add(r)
            unique.append(r)
    return unique[:5]


# Offline dictionary tiers, checked in this order:
#   (config key, lookup function, source label, badge)
# Abbreviations come last: a one-line "DKA = diabetic ketoacidosis" must not
# hide the full DKA / COPD / TSH card from the curated tiers.
_OFFLINE_TIERS = [
    ("tier_05_drug_individual", _lookup_drug,        "Drug",        "Drug"),
    ("tier_05a_drug_class",     _lookup_drug_class,  "Drug Class",  "Drug Class"),
    ("tier_05b_lab_range",      _lookup_lab_range,   "Lab Range",   "Lab"),
    ("tier_05c_disease",        _lookup_disease,     "Disease",     "Dx"),
    ("tier_05d_micro",          _lookup_micro,       "Micro",       "Micro"),
    ("tier_05e_scoring",        _lookup_score,       "Score",       "Score"),
    ("tier_05f_anatomy",        _lookup_anatomy,     "Anatomy",     "A&P"),
    ("tier_05g_biostats",       _lookup_biostats,    "Biostats",    "Stats"),
    ("tier_05h_syndromes",      _lookup_syndrome,    "Syndromes",   "Syndrome"),
    ("tier_05i_ecg",            _lookup_ecg,         "ECG",         "ECG"),
    ("tier_05j_genetics",       _lookup_genetics,    "Genetics",    "Genetics"),
    ("tier_05k_radiology",      _lookup_radiology,   "Radiology",   "Radiology"),
    ("tier_05l_pathology",      _lookup_pathology,   "Pathology",   "Pathology"),
    ("tier_05m_signs",          _lookup_sign,        "Signs",       "Sign"),
    ("tier_05n_basic_science",  _lookup_basic_science, "Basic Sciences", "Basic Sci"),
    ("tier_05o_obgyn",          _lookup_obgyn,       "OB/GYN",      "OB/GYN"),
    ("tier_05p_primary_care",   _lookup_primary_care, "Primary Care", "Primary Care"),
    ("tier_01_abbrev",          _lookup_abbrev,      "Abbrev",      "Abbrev"),
]


# ── Deck / tag priority profiles ─────────────────────────────────────────────
# On an OB/GYN card the OB/GYN topics are tried before the other dictionaries,
# on a family-medicine card the primary-care topics, and so on.  A profile
# matches when one of its words appears in the card's deck names (including
# parent decks) or note tags — compared without spaces, underscores or
# punctuation, so "Family_Medicine", "FamilyMedicine" and "Family Medicine"
# all match "family medicine".  Tiers not listed keep their usual order.
# Users can replace the list with "deck_profiles" in the add-on config.
_DEFAULT_DECK_PROFILES = [
    {"name": "OB/GYN",
     "match": ["ob/gyn", "obgyn", "ob-gyn", "obstetric", "gynecolog", "gynaecolog", "women's health"],
     "tiers": ["tier_05o_obgyn", "tier_05c_disease", "tier_05_drug_individual",
               "tier_05b_lab_range", "tier_05e_scoring", "tier_05m_signs"],
     # General words that open the pregnancy-specific card on OB/GYN cards
     "prefer": {
         'hypertension': 'hypertensive disorders of pregnancy',
         'htn': 'hypertensive disorders of pregnancy',
         'high blood pressure': 'hypertensive disorders of pregnancy',
         'proteinuria': 'hypertensive disorders of pregnancy', 'anemia': 'anemia in pregnancy',
         'iron deficiency anemia': 'anemia in pregnancy',
         'thrombocytopenia': 'thrombocytopenia in pregnancy',
         'low platelets': 'thrombocytopenia in pregnancy',
         'uti': 'asymptomatic bacteriuria in pregnancy',
         'urinary tract infection': 'asymptomatic bacteriuria in pregnancy',
         'bacteriuria': 'asymptomatic bacteriuria in pregnancy',
         'pyelonephritis': 'asymptomatic bacteriuria in pregnancy',
         'hypothyroidism': 'thyroid disease in pregnancy',
         'hyperthyroidism': 'thyroid disease in pregnancy',
         'graves disease': 'thyroid disease in pregnancy',
         'thyroid': 'thyroid disease in pregnancy', 'dvt': 'venous thromboembolism in pregnancy',
         'pe': 'venous thromboembolism in pregnancy',
         'pulmonary embolism': 'venous thromboembolism in pregnancy',
         'deep vein thrombosis': 'venous thromboembolism in pregnancy',
         'vte': 'venous thromboembolism in pregnancy',
         'anticoagulation': 'venous thromboembolism in pregnancy',
         'asthma': 'asthma in pregnancy', 'epilepsy': 'epilepsy in pregnancy',
         'seizure': 'epilepsy in pregnancy', 'seizures': 'epilepsy in pregnancy',
         'sle': 'lupus in pregnancy', 'lupus': 'lupus in pregnancy',
         'systemic lupus erythematosus': 'lupus in pregnancy',
         'antiphospholipid syndrome': 'lupus in pregnancy',
         'sickle cell disease': 'sickle cell disease in pregnancy',
         'obesity': 'obesity in pregnancy', 'appendicitis': 'acute abdomen in pregnancy',
         'cholecystitis': 'acute abdomen in pregnancy',
         'abdominal pain': 'acute abdomen in pregnancy', 'trauma': 'trauma in pregnancy',
         'headache': 'neurologic disorders in pregnancy',
         'migraine': 'neurologic disorders in pregnancy',
         'stroke': 'neurologic disorders in pregnancy',
         'depression': 'psychiatric medications in pregnancy',
         'bipolar disorder': 'psychiatric medications in pregnancy',
         'lithium': 'psychiatric medications in pregnancy', 'hiv': 'hiv in pregnancy',
         'hepatitis b': 'hepatitis b in pregnancy', 'hbv': 'hepatitis b in pregnancy',
         'syphilis': 'congenital syphilis', 'varicella': 'varicella in pregnancy',
         'chickenpox': 'varicella in pregnancy', 'parvovirus': 'parvovirus b19 in pregnancy',
         'parvovirus b19': 'parvovirus b19 in pregnancy',
         'toxoplasmosis': 'congenital toxoplasmosis', 'listeria': 'listeriosis in pregnancy',
         'listeriosis': 'listeriosis in pregnancy', 'cmv': 'congenital cmv',
         'herpes': 'genital herpes', 'hsv': 'genital herpes', 'fever': 'infections in pregnancy',
         'heart disease': 'cardiac disease in pregnancy',
         'mitral stenosis': 'cardiac disease in pregnancy',
         'kidney disease': 'kidney disease in pregnancy', 'ckd': 'kidney disease in pregnancy',
         'diabetes': 'pregestational diabetes', 'type 1 diabetes': 'pregestational diabetes',
         'type 2 diabetes': 'pregestational diabetes', 'dka': 'pregestational diabetes',
         'sepsis': 'maternal sepsis', 'cardiomyopathy': 'peripartum cardiomyopathy',
         'pruritus': 'dermatoses of pregnancy', 'itching': 'dermatoses of pregnancy',
         'rash': 'dermatoses of pregnancy', 'radiation': 'imaging in pregnancy',
         'ct scan': 'imaging in pregnancy', 'imaging': 'imaging in pregnancy',
         'vaccines': 'lifestyle in pregnancy', 'vaccination': 'lifestyle in pregnancy',
         'nutrition': 'lifestyle in pregnancy', 'exercise': 'lifestyle in pregnancy',
         'smoking': 'substance use in pregnancy', 'alcohol': 'substance use in pregnancy',
         'cocaine': 'substance use in pregnancy', 'opioids': 'substance use in pregnancy',
         'mastitis': 'lactational mastitis', 'jaundice': 'neonatal jaundice',
         'hypoglycemia': 'neonatal hypoglycemia', 'cancer': 'cancer in pregnancy',
         'breast mass': 'breast mass workup', 'pelvic mass': 'pelvic mass workup',
         'steroids': 'antenatal corticosteroids', 'corticosteroids': 'antenatal corticosteroids',
         'betamethasone': 'antenatal corticosteroids', 'incontinence': 'urinary incontinence',
         'depression screening': 'postpartum depression',
         'icp': 'cholestasis of pregnancy', 'ppd': 'postpartum depression',
         'epidural': 'labor analgesia', 'viability': 'periviability', 'inversion': 'third stage of labor management',
     }},
    {"name": "Family medicine",
     "match": ["family medicine", "family med", "primary care", "ambulatory", "preventive medicine"],
     "tiers": ["tier_05p_primary_care", "tier_05c_disease", "tier_05e_scoring",
               "tier_05_drug_individual", "tier_05b_lab_range"],
     "prefer": {
         'hypertension': 'hypertension management', 'htn': 'hypertension management',
         'high blood pressure': 'hypertension management', 'hyperlipidemia': 'statin therapy',
         'cholesterol': 'statin therapy', 'dyslipidemia': 'statin therapy',
         'ldl': 'statin therapy', 'vaccines': 'adult vaccination schedule',
         'vaccination': 'adult vaccination schedule',
         'immunizations': 'adult vaccination schedule', 'screening': 'uspstf screening',
         'cancer screening': 'uspstf screening', 'anemia': 'anemia evaluation',
         'chest pain': 'chest pain evaluation', 'dizziness': 'dizziness evaluation',
         'weight loss': 'unintentional weight loss',
         'smoking': 'tobacco use disorder', 'uti': 'acute cystitis',
         'falls': 'falls in older adults', 'aspirin': 'aspirin for primary prevention',
         'hepatitis c': 'hepatitis c screening', 'hiv': 'hiv screening',
         'edema': 'peripheral edema evaluation', 'fatigue': 'fatigue evaluation',
         'hematuria': 'hematuria evaluation', 'proteinuria': 'proteinuria evaluation',
         'palpitations': 'palpitations evaluation', 'headache': 'headache evaluation',
         'lymphadenopathy': 'lymphadenopathy evaluation',
         'osteoporosis': 'osteoporosis screening', 'chlamydia': 'sti screening',
         'gonorrhea': 'sti screening',
     }},
    {"name": "Pediatrics",
     "match": ["pediatric", "paediatric", "peds"],
     "tiers": ["tier_05p_primary_care", "tier_05c_disease", "tier_05o_obgyn"],
     "prefer": {
         'vaccines': 'childhood vaccination schedule',
         'vaccination': 'childhood vaccination schedule',
         'immunizations': 'childhood vaccination schedule',
         'development': 'developmental milestones', 'milestones': 'developmental milestones',
         'fever': 'fever in infants', 'jaundice': 'neonatal jaundice',
         'hypoglycemia': 'neonatal hypoglycemia', 'sepsis': 'neonatal sepsis',
         'screening': 'well-child care',
         'constipation': 'functional constipation in children',
         'uti': 'urinary tract infection in children',
         'urinary tract infection': 'urinary tract infection in children',
         'reflux': 'gastroesophageal reflux in infants',
         'gerd': 'gastroesophageal reflux in infants', 'murmur': 'innocent murmur',
         'dehydration': 'dehydration in children', 'diaper rash': 'diaper dermatitis',
         'hypothyroidism': 'congenital hypothyroidism', 'brain tumor': 'pediatric brain tumors',
         'diabetes': 'dka', 'rheumatic fever': 'acute rheumatic fever',
         'heart disease': 'congenital heart disease', 'vomiting': 'pyloric stenosis',
     }},
    {"name": 'Internal medicine',
     "match": ['internal medicine', 'shelf::im', 'medicine clerkship', 'medicine rotation', 'inpatient medicine'],
     "tiers": ['tier_05c_disease', 'tier_05b_lab_range', 'tier_05_drug_individual', 'tier_05e_scoring', 'tier_05i_ecg'],
     "prefer": {
         'acidosis': 'acid-base interpretation', 'alkalosis': 'acid-base interpretation',
         'heart block': 'av block', 'shock': 'cardiogenic shock',
         'cholestasis': 'elevated liver enzymes', 'lfts': 'elevated liver enzymes',
         'overdose': 'acetaminophen overdose',
     }},
    {"name": 'Psychiatry',
     "match": ['psychiatry', 'psych', 'behavioral health', 'mental health'],
     "tiers": ['tier_05c_disease', 'tier_05_drug_individual', 'tier_05a_drug_class', 'tier_05p_primary_care'],
     "prefer": {
         'depression': 'major depressive disorder', 'capacity': 'decision-making capacity',
         'mania': 'bipolar disorder', 'anxiety': 'generalized anxiety disorder',
         'panic': 'panic disorder', 'withdrawal': 'alcohol withdrawal',
         'dystonia': 'extrapyramidal symptoms', 'tremor': 'lithium toxicity',
         'intoxication': 'stimulant intoxication', 'psychosis': 'schizophrenia',
         'obsessions': 'obsessive-compulsive disorder',
         'compulsions': 'obsessive-compulsive disorder', 'consent': 'informed consent',
         'neglect': 'child abuse', 'suicide': 'suicide risk assessment',
         'personality': 'cluster b personality disorders',
     }},
    {"name": 'Neurology',
     "match": ['neurology', 'neuro shelf', 'shelf::neuro', 'neurology clerkship'],
     "tiers": ['tier_05c_disease', 'tier_05f_anatomy', 'tier_05m_signs', 'tier_05k_radiology', 'tier_05_drug_individual'],
     "prefer": {
         'neglect': 'hemispatial neglect', 'weakness': 'upper vs lower motor neuron lesions',
         'numbness': 'peripheral neuropathy', 'ptosis': 'oculomotor nerve palsy',
         'diplopia': 'abducens nerve palsy', 'nystagmus': 'cerebellar lesions',
         'tremor': 'movement disorders', 'seizures': 'first unprovoked seizure',
         'pupil': 'oculomotor nerve palsy', 'back pain': 'lumbar radiculopathy',
         'vision loss': 'central retinal artery occlusion',
     }},
    {"name": "Anatomy",
     "match": ["anatomy", "embryology", "histology"],
     "tiers": ["tier_05f_anatomy"]},
    {"name": "Pharmacology",
     "match": ["pharmacology", "pharm"],
     "tiers": ["tier_05_drug_individual", "tier_05a_drug_class"]},
    {"name": "Microbiology",
     "match": ["microbiology", "infectious disease"],
     "tiers": ["tier_05d_micro"]},
]

# (profile name, tier keys in priority order, {word: preferred entry}) for the
# card on screen, or None
_active_profile = None


def _norm_match(text):
    return re.sub(r"[^a-z0-9]+", "", (text or "").lower())


def _deck_profiles():
    profiles = _get_user_cfg().get("deck_profiles")
    return profiles if isinstance(profiles, list) and profiles else _DEFAULT_DECK_PROFILES


def _profile_from_text(names, tags):
    """The first profile whose words appear in the deck names or tags."""
    hay = _norm_match(" ".join(list(names) + list(tags)))
    for prof in _deck_profiles():
        if not isinstance(prof, dict):
            continue
        words = [_norm_match(m) for m in prof.get("match", []) if isinstance(m, str)]
        if any(w and w in hay for w in words):
            tiers = tuple(t for t in prof.get("tiers", []) if isinstance(t, str))
            prefer = prof.get("prefer") if isinstance(prof.get("prefer"), dict) else {}
            prefer = {str(k).lower(): str(v) for k, v in prefer.items()}
            return (str(prof.get("name", "")), tiers, prefer)
    return None


def _profile_for_card(card):
    if card is None or not _get_user_cfg().get("deck_priority", True):
        return None
    try:
        names = [mw.col.decks.name(card.did)]
        if getattr(card, "odid", 0):            # filtered deck: original deck too
            names.append(mw.col.decks.name(card.odid))
        tags = list(card.note().tags)
    except Exception:
        return None
    return _profile_from_text(names, tags)


_TITLE_ACRONYMS = {"hiv", "cmv", "b19", "uspstf", "vte", "dka"}


def _redirect_origin(candidates, phrase, profile=None):
    """The hovered word a profile redirected to `phrase`, or "" — shown as a
    chip so the general card stays one click away."""
    prefer = profile[2] if profile and len(profile) > 2 else {}
    target = (phrase or "").strip().lower()
    for c in candidates or []:
        if prefer.get(str(c).strip().lower(), "").lower() == target:
            return str(c).strip()
    return ""


def _ordered_tiers(profile=None):
    """_OFFLINE_TIERS with the profile's tiers moved to the front (stable)."""
    order = profile[1] if profile else ()
    if not order:
        return _OFFLINE_TIERS
    rank = {k: i for i, k in enumerate(order)}
    return sorted(_OFFLINE_TIERS, key=lambda t: rank.get(t[0], len(order)))


def _run_parallel(calls):
    """Start every (fn, args) call on its own daemon thread.  Returns one
    getter per call, in the same order; each getter blocks until that call
    finishes and returns its result (None if it raised).  Daemon threads so a
    slow request never delays Anki shutting down; requests still running after
    an earlier hit simply finish in the background and are ignored."""
    getters = []
    for fn, args in calls:
        box, done = [None], threading.Event()
        def _run(fn=fn, args=args, box=box, done=done):
            try:
                box[0] = fn(*args)
            except Exception as _e:
                print(f"[MQR] network lookup error in {fn.__name__}: {_e}", file=sys.stderr)
            finally:
                done.set()
        threading.Thread(target=_run, daemon=True).start()
        getters.append(lambda box=box, done=done: (done.wait(), box[0])[1])
    return getters


class _Superseded(Exception):
    """The user moved on to another word before the network was needed."""


def _lookup_uncached(candidates, sentence, primary=None, profile=None, cancel=None):
    """
    Try each candidate phrase using the tier waterfall.
    Returns (phrase, defn, url, src_label, badge).
    """
    # Snapshot config once — avoids 15+ separate disk reads per lookup
    _cfg = _get_user_cfg()
    # Drop phrases that begin/end with a function word ("the", "with the
    # mnemonic") — they matched unrelated drug labels and eponyms (May, Best).
    if not primary and candidates and _is_stopword(candidates[-1]):
        return "", "", "", "", ""          # hovered word itself is "with", "the" …
    candidates = [c for c in candidates
                  if not _is_stop_phrase(c) and not _is_everyday(c)]
    # A clicked chip / selected phrase is always tried, even if it was filtered
    if primary and primary not in candidates:
        candidates.insert(0, primary)
    if not candidates and not primary:
        return "", "", "", "", ""
    # The hovered word, or for chip / shortcut lookups the whole selected
    # phrase (so "vitamin K" is not answered with the entry for "vitamin").
    single_word = primary or (candidates[-1] if candidates else "")

    # ── Tiers 0.1–0.5n: offline dictionaries (instant) ────────────────────────
    # Phrases are tried before the single word, across all dictionaries, so
    # "ischemic stroke", "ST depression" or "celiac trunk" win over the
    # entries for "stroke", "depression" or "celiac".  For each phrase the
    # dictionaries are tried in priority order.
    active = [(lookup, src, badge) for cfg_key, lookup, src, badge in _ordered_tiers(profile)
              if _cfg.get(cfg_key, True)]

    def _offline(phrase):
        if not phrase or _acronym_mismatch(phrase):
            return ""
        for lookup, src, badge in active:
            defn = lookup(phrase)
            if defn:
                return defn, src, badge
        return ""

    # ── Tier 2: local SQLite MeSH/UMLS database ───────────────────────────────
    def _db(phrase):
        defn, sem_type = _lookup_local_db(phrase)
        if defn:
            return phrase, defn, "", "MeSH/UMLS", _SEM_BADGE.get(sem_type, "MeSH/UMLS")
        return None

    def _first(seq):
        out = []
        for p in seq:
            if p and p not in out:
                out.append(p)
        return out
    phrases = _first(([primary] if primary and " " in primary.strip() else [])
                     + [c for c in candidates if " " in c.strip()])
    words = [w for w in _first([single_word] + list(candidates)) if w not in phrases]

    prefer = profile[2] if profile and len(profile) > 2 and not primary else {}

    def _offline_or_variant(phrase):
        target = prefer.get(phrase.strip().lower()) if prefer else None
        if target and not _acronym_mismatch(phrase):
            hit = _offline(target)
            if hit:
                # Title shows the entry actually displayed ("HIV in pregnancy")
                title = " ".join(w.upper() if w in _TITLE_ACRONYMS else w
                                 for w in target.split())
                return (title[:1].upper() + title[1:], hit[0], "") + hit[1:]
        hit = _offline(phrase)
        if not hit:
            # Singular/plural forms: "dermatome" → the "dermatomes" entry
            # (the DB's own "dermatome" is a surgical skin-cutting device)
            for variant in _number_variants(phrase):
                hit = _offline(variant)
                if hit:
                    break
        # Report the phrase as written on the card
        return (phrase, hit[0], "") + hit[1:] if hit else None

    # 1. Curated phrases around the hovered word (longest first), so
    #    "ischemic stroke" or "celiac trunk" beat "stroke" or "celiac".
    for phrase in phrases:
        hit = _offline_or_variant(phrase)
        if hit:
            return hit
    # 2. Database phrases, before any single word — "portal hypertension" or
    #    "respiratory depression" is not answered with the curated entry for
    #    "hypertension" or "depression".  Qualified phrases ("serum sodium",
    #    "warfarin sodium") show the curated entry of their core term instead.
    for phrase in phrases:
        core = _curated_core(phrase)
        hit = _offline(core) if core else ""
        if hit:
            return (phrase, hit[0], "") + hit[1:]
        hit = _db(phrase)
        if hit:
            return hit
    # 3. The hovered word itself: curated, then database
    for word in words:
        hit = _offline_or_variant(word) or _db(word)
        if hit:
            return hit

    # ── Tier 2.5: local DB with morphological variants ───────────────────────────
    single = words[0] if words else ""
    if single and " " not in single:      # variants only make sense for one word
        for variant in _medical_variants(single):
            defn, sem_type = _lookup_local_db(variant)
            if defn:
                badge = _SEM_BADGE.get(sem_type, "MeSH/UMLS")
                return variant, defn, "", "MeSH/UMLS", badge

    # ── Tiers 3-6 are network — filter common English words first ─────────────
    net_candidates = [
        p for p in candidates
        if not all(w in _COMMON_ENGLISH or w in _EVERYDAY for w in p.lower().split())
    ]
    if not net_candidates:
        return "", "", "", "", ""
    # A newer hover/chip lookup has started: don't fire network requests
    # (up to ~15 per word) for a tooltip nobody will see.
    if cancel is not None and cancel():
        raise _Superseded()
    # Longest phrases first, at most 4 (the JS sends up to 6 candidates)
    net_candidates = net_candidates[:4]

    # ── Tiers 3–6.5: network sources, queried in parallel ─────────────────────
    # Every (source, phrase) request starts at once; results are then read in
    # the original priority order (UMLS → RxNorm → OpenFDA → MedlinePlus →
    # Wikipedia → OMIM, longest phrase first), so the answer is the same as the
    # old one-after-another waterfall but arrives in roughly the time of the
    # slowest single request instead of the sum of all of them.
    def _umls(p):
        defn, url, sem_type = _lookup_umls_api(p)
        return defn, url, _SEM_BADGE.get(sem_type, "UMLS")
    sources = []   # (lookup fn returning (defn, url[, badge]), src label, badge)
    if _umls_api_key():
        sources.append((_umls, "UMLS", None))
    if _cfg.get("tier_rxnorm", True):
        sources.append((_lookup_rxnorm, "RxNorm", "Drug"))
    if _cfg.get("tier_openfda", True):
        sources.append((_lookup_openfda, "OpenFDA", "Drug"))
    if _cfg.get("tier_medlineplus", True):
        sources.append((_lookup_medlineplus, "NLM MedlinePlus", ""))
    if _cfg.get("tier_wikipedia", True):
        sources.append((_lookup_wikipedia, "Wikipedia", ""))
    if _cfg.get("tier_omim", False):  # disabled by default — full-text search too noisy
        sources.append((_lookup_omim, "OMIM", "Genetics"))

    # Drug APIs only for names of one or two words ("metoprolol succinate")
    drug_fns = (_lookup_rxnorm, _lookup_openfda)
    jobs = [(fn, phrase, src, badge)
            for fn, src, badge in sources for phrase in net_candidates
            if fn not in drug_fns or len(phrase.split()) <= 2]
    results = _run_parallel([(fn, (phrase,)) for fn, phrase, _, _ in jobs])
    for (fn, phrase, src, badge), get in zip(jobs, results):
        res = get()   # waits only for this request
        if res and res[0]:
            return phrase, res[0], res[1], src, (res[2] if badge is None else badge)

    return "", "", "", "", ""

# ─────────────────────────────────────────────────────────────────────────────


def _lookup_candidates(candidates, sentence, primary=None, cancel=None):
    """Cached front-end for the tier waterfall (Tier 1: in-memory cache)."""
    # Deck profile of the card on screen: part of the cache key, since the same
    # word can resolve to a different dictionary on an OB/GYN card
    profile = _active_profile
    key = _cache_key(candidates, primary) + ((profile[0] if profile else ""),)
    hit = _cache_get(key)
    if hit:
        phrase, defn, url, src, badge = hit
        return phrase, defn, url, src + " ·cached", badge
    if _miss_recent(key):
        return "", "", "", "", ""
    try:
        result = _lookup_uncached(candidates, sentence, primary, profile, cancel)
    except _Superseded:
        return "", "", "", "", ""        # not cached: the word may be hovered again
    if result[1]:
        _cache_set(key, result)
    else:
        _miss_set(key)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 11 · JS message handler
# ─────────────────────────────────────────────────────────────────────────────

# Bumped every time a question or answer is shown.  Identifies "the card on
# screen now" for discarding stale results and counting retries; id(card) was
# unreliable because Python reuses object addresses for the next card.
_render_gen   = 0
_retry_counts: dict = {}   # render generation → injection attempts
_lookup_seq   = 0          # bumped by every hover/chip lookup; older ones are superseded


def _next_lookup():
    """Start a lookup: returns a function telling whether a newer one began."""
    global _lookup_seq
    _lookup_seq += 1
    mine = _lookup_seq
    return lambda: mine != _lookup_seq

def _send_lookup_result(phrase, defn, url, src, badge, rel_js, cands, rid=None, term=None,
                        quiet=False):
    """Push a lookup result (or not-found) to the reviewer WebView on the main thread.

    Must be called via mw.taskman.run_on_main — reads mw.reviewer on the main thread.
    rel_js is JSON-serialised on the worker thread so the main thread stays fast.
    """
    web = mw.reviewer.web if mw.reviewer else None
    if not web:
        return
    def _sf(s):
        return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    rid_js = json.dumps(rid if isinstance(rid, int) else None)
    if not defn and quiet:
        # Hovered an everyday word with nothing medical around it: just hide
        web.eval(f"if(window.mqrQuiet) mqrQuiet({rid_js});")
        return
    if not defn:
        # The hovered word (last candidate) or the clicked/selected phrase
        _best    = term or (cands[-1] if cands else "")
        _suggs   = _find_suggestions([_best])   # the whole selection, not its first word
        _sugg_js = json.dumps(_suggs)
        web.eval(f"if(window.mqrNotFound) mqrNotFound(`{_sf(_best)}`, {_sugg_js}, {rid_js});")
        return
    src_html = (f'<a href="{html.escape(url)}" style="color:var(--mqr-link2)">{html.escape(src)}</a>'
                if url else '')
    web.eval(
        f"if(window.mqrUpdate) mqrUpdate("
        f"`{_sf(phrase)}`,`{_sf(defn)}`,`{_sf(src_html)}`,`{_sf(badge)}`, {rel_js}, {rid_js});"
    )


def _on_js_message(handled, message, context):
    if not isinstance(context, Reviewer):
        return handled
    if not message.startswith("mqr:"):
        return handled

    payload_str = message[4:].strip()

    # Open external URL (PubMed / Scholar fallback links)
    if payload_str.startswith("open:"):
        url = payload_str[5:]
        # Only web links — card content must not be able to open local files/apps
        if not url.lower().startswith(("https://", "http://")):
            return (True, None)
        try:
            from aqt.utils import openLink
            openLink(url)
        except Exception:
            import webbrowser
            webbrowser.open(url)
        return (True, None)

    if payload_str.startswith("__batch__:"):
        raw = payload_str[len("__batch__:"):]
        if ":underline=" in raw:
            raw, _ = raw.rsplit(":underline=", 1)
        try:
            words = json.loads(raw)
        except Exception:
            return (True, None)
        def _batch_worker(_gen=_render_gen):
            recognized = _batch_check(words)
            def _push():
                # Discard stale results if the user navigated to a different card
                if not mw.reviewer or _render_gen != _gen:
                    return
                web = mw.reviewer.web if mw.reviewer else None
                if web:
                    safe_list = json.dumps(recognized)
                    ul_flag = "true" if _user_cfg_get("underline_terms", True) else "false"
                    web.eval(f"window.mqrUnderline={ul_flag}; if(window.mqrHighlight) mqrHighlight({safe_list});")
            mw.taskman.run_on_main(_push)
        threading.Thread(target=_batch_worker, daemon=True).start()
        return (True, None)

    if payload_str == "__retry__":
        card_id = _render_gen
        attempt = _retry_counts.get(card_id, 0) + 1
        _retry_counts[card_id] = attempt
        if attempt <= CFG["inject_max_retries"]:
            delay = 60 * attempt
            mw.taskman.run_on_main(lambda: QTimer.singleShot(delay, _inject_with_retry))
        return (True, None)

    # ── Chip / hover lookup (selected text or hover word) ─────────────────
    if payload_str.startswith("shortcut:"):
        raw = payload_str[len("shortcut:"):].strip()
        rid = None
        selected_text = raw
        if raw.startswith("{"):
            try:
                _p = json.loads(raw)
                rid = _p.get("rid")
                selected_text = str(_p.get("text", "")).strip()
            except Exception:
                pass
        # Curly apostrophes → straight; drop punctuation around a selection
        # ("Murphy's sign." or "(ACE inhibitor)")
        selected_text = " ".join(selected_text.replace("\u2019", "'").split())
        selected_text = selected_text.strip(".,;:!?()[]{}\"'")
        if not selected_text:
            return (True, None)
        candidates = [selected_text]
        words = selected_text.split()
        for n in range(len(words), 0, -1):
            phrase = " ".join(words[:n])
            if phrase not in candidates:
                candidates.append(phrase)
        cancel = _next_lookup()
        def _shortcut_worker(cands=candidates):
            phrase, defn, url, src, badge = _lookup_candidates(
                cands, selected_text, primary=selected_text, cancel=cancel)
            if cancel():
                return
            rel_js = json.dumps(_related_for(phrase))
            mw.taskman.run_on_main(
                lambda: _send_lookup_result(phrase, defn, url, src, badge, rel_js, cands, rid,
                                            selected_text)
            )
            if defn:
                _send_image(phrase, rid)
        threading.Thread(target=_shortcut_worker, daemon=True).start()
        return (True, None)

    rid = None
    try:
        payload    = json.loads(payload_str)
        candidates = payload.get("candidates", [payload_str])
        sentence   = payload.get("sentence", "")
        rid        = payload.get("rid")
    except Exception:
        candidates = [payload_str]
        sentence   = ""
    if not isinstance(candidates, list):   # card scripts can send anything
        candidates = [str(candidates)]
    # Dictionary keys use straight apostrophes (wilson's disease)
    candidates = [str(c).replace("\u2019", "'") for c in candidates]

    if not candidates:
        return (True, None)

    quiet = bool(candidates) and (_is_everyday(candidates[-1]) or _is_stopword(candidates[-1]))

    cancel = _next_lookup()

    def _worker():
        profile = _active_profile
        phrase, defn, url, src, badge = _lookup_candidates(candidates, sentence, cancel=cancel)
        if cancel():
            return                       # superseded by a newer hover
        related = _related_for(phrase)
        origin = _redirect_origin(candidates, phrase, profile)
        if origin:
            related = [origin] + [r for r in related if r.lower() != origin.lower()]
        rel_js = json.dumps(related)
        mw.taskman.run_on_main(
            lambda: _send_lookup_result(phrase, defn, url, src, badge, rel_js, candidates, rid,
                                        quiet=quiet)
        )
        if defn:
            _send_image(phrase, rid)

    threading.Thread(target=_worker, daemon=True).start()
    return (True, None)


gui_hooks.webview_did_receive_js_message.append(_on_js_message)

# ─────────────────────────────────────────────────────────────────────────────
# 12 · Card hooks
# ─────────────────────────────────────────────────────────────────────────────

def _new_render():
    global _render_gen
    _render_gen += 1
    _retry_counts.clear()          # only the current render can still retry
    _retry_counts[_render_gen] = 0
    _schedule_inject()


def _set_profile(card):
    global _active_profile
    _active_profile = _profile_for_card(card)


def _on_question(card):
    _set_profile(card)
    _new_render()


def _on_answer(card):
    _set_profile(card)
    _new_render()


gui_hooks.reviewer_did_show_question.append(_on_question)
gui_hooks.reviewer_did_show_answer.append(_on_answer)

# ─────────────────────────────────────────────────────────────────────────────
# 13 · Settings dialog
# ─────────────────────────────────────────────────────────────────────────────
def _open_settings():
    from aqt.qt import (
        QDialog, QVBoxLayout, QHBoxLayout, QWidget, QPushButton,
        QLabel, QGroupBox, QLineEdit, QFrame, QSlider, QSpinBox, QScrollArea,
        QComboBox, QPainter, QColor, Qt,
    )

    def _rgba(hex_color, alpha):
        """'#rrggbb' + alpha → 'rgba(…)'.  Qt reads 8-digit hex as #AARRGGBB,
        so appending alpha digits to a color scrambles it."""
        h = hex_color.lstrip("#")
        return f"rgba({int(h[0:2], 16)},{int(h[2:4], 16)},{int(h[4:6], 16)},{alpha})"

    # ── Pill toggle switch widget ─────────────────────────────────────────
    class _Toggle(QWidget):
        """A custom pill-shaped on/off toggle switch."""
        def __init__(self, parent=None):
            super().__init__(parent)
            self._on = True
            self.setFixedSize(46, 26)
            try:
                self.setCursor(Qt.CursorShape.PointingHandCursor)
            except AttributeError:
                self.setCursor(Qt.PointingHandCursor)

        def isChecked(self):  return self._on
        def setChecked(self, v):
            self._on = bool(v)
            self.update()

        def mousePressEvent(self, _event):
            self._on = not self._on
            self.update()

        def paintEvent(self, _event):
            p = QPainter(self)
            try:
                p.setRenderHint(QPainter.RenderHint.Antialiasing)
                p.setPen(Qt.PenStyle.NoPen)
            except AttributeError:
                p.setRenderHint(QPainter.Antialiasing)
                p.setPen(Qt.NoPen)
            # Track
            p.setBrush(QColor("#4CAF50" if self._on else "#4a4a4a"))
            p.drawRoundedRect(0, 4, 46, 18, 9, 9)
            # Thumb
            p.setBrush(QColor("#ffffff"))
            p.drawEllipse(24 if self._on else 2, 2, 22, 22)
            p.end()

    # ── Tier definitions ──────────────────────────────────────────────────
    # (cfg_key, display_name, tier_id, badge_color, description)
    _TIERS = [
        ("tier_01_abbrev",          "Abbreviations / Acronyms","Tier 0.1",  "#c8a84b",
         f"{len(_ABBREVS) + len(_ABBREV_TERMS)} entries — ACEi, ARB, SIADH, GFR, ECG… (checked last, after the full cards)"),
        ("tier_05_drug_individual", "Individual Drugs",        "Tier 0.5",  "#9c7fc1",
         f"{len(_DRUGS)} drugs (+{len(_DRUG_BRAND_ALIASES)} brand names) — MOA, uses, adverse effects & pearls"),
        ("tier_05a_drug_class",     "Drug Classes",            "Tier 0.5a", "#5a9fd4",
         f"{len(_DRUG_CLASSES)} classes — mechanism, members, contraindications"),
        ("tier_05b_lab_range",      "Lab Reference Ranges",    "Tier 0.5b", "#4a9e6b",
         f"{len(_LAB_RANGES)} tests — normal values (with SI units), critical levels & clinical meaning"),
        ("tier_05c_disease",        "Disease Criteria",        "Tier 0.5c", "#e05c5c",
         f"{len(_DISEASES)} conditions + {len(_DISEASE_ALIASES)} alternate names — criteria, features & treatment"),
        ("tier_05d_micro",          "Microbiology Organisms",  "Tier 0.5d", "#c8a84b",
         f"{len(_MICRO)} organisms + {len(_MICRO_ALIASES)} disease names — gram stain, virulence & treatment"),
        ("tier_05e_scoring",        "Clinical Scoring",        "Tier 0.5e", "#7a9fd4",
         f"{len(_SCORES)} scores — Wells, CURB-65, CHA₂DS₂-VASc, MELD, Centor, PERC, CIWA, NEXUS…"),
        ("tier_05f_anatomy",        "Anatomy & Physiology",    "Tier 0.5f", "#b07d3a",
         f"{len(_ANATOMY)} entries + {len(_ANATOMY_ALIASES)} alternate names — nerves, vessels, "
         "spaces, joints, viscera, head & neck, neuro"),
        ("tier_05g_biostats",       "Biostatistics",           "Tier 0.5g", "#3fa89e",
         f"{len(_BIOSTATS)} entries — sensitivity, NNT, p-value, biases, tests & more"),
        ("tier_05h_syndromes",      "Clinical Syndromes",      "Tier 0.5h", "#e07050",
         f"{len(_SYNDROMES)} syndromes — Wernicke, serotonin syndrome, NMS, Goodpasture, MEN…"),
        ("tier_05i_ecg",            "ECG Findings",            "Tier 0.5i", "#5abf8a",
         f"{len(_ECG_FINDINGS)} findings — STEMI territories, Brugada, Wenckebach, Torsades, and more"),
        ("tier_05j_genetics",       "Genetics",                "Tier 0.5j", "#9b59b6",
         f"{len(_GENETICS)} entries — inheritance patterns, trinucleotide repeats, BRCA1/2, Down, Fragile X, CF, etc."),
        ("tier_05k_radiology",      "Radiology",               "Tier 0.5k", "#3498db",
         f"{len(_RADIOLOGY)} entries — GGO, Hampton hump, Westermark, Codman triangle, apple core, steeple sign, etc."),
        ("tier_05l_pathology",      "Pathology",               "Tier 0.5l", "#e74c3c",
         f"{len(_PATHOLOGY)} entries — cell injury, inflammation, neoplasia, necrosis types, inclusion bodies…"),
        ("tier_05m_signs",          "Clinical Signs & Eponyms", "Tier 0.5m", "#d77a8f",
         f"{len(_SIGNS)} signs — Murphy, Kernig, Beck's triad, Janeway, Courvoisier, Nikolsky…"),
        ("tier_05n_basic_science",  "Basic Sciences",          "Tier 0.5n", "#3fa89e",
         f"{len(_BASIC_SCIENCE)} topics — pharmacokinetics, toxidromes, antidotes, hypersensitivity, "
         "immunoglobulins, complement, metabolic pathways, vitamins"),
        ("tier_05o_obgyn",          "OB/GYN Topics",           "Tier 0.5o", "#c45b8a",
         f"{len(_OBGYN)} topics — stages of labor, fetal heart tracings, prenatal care and screening, "
         "contraception, cervical screening, menopause, bleeding/mass workups, newborn care, ethics"),
        ("tier_05p_primary_care",   "Primary Care",            "Tier 0.5p", "#3fa89e",
         f"{len(_PRIMARY_CARE)} topics — USPSTF screening, vaccines, milestones, well-child and adolescent care, "
         "preop evaluation, travel, geriatrics, symptom work-ups, ethics & law (capacity, consent), psychotherapy"),
    ]

    class _SettingsDlg(QDialog):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Medical Quick Reference — Settings")
            self.setMinimumWidth(600)
            self.setMinimumHeight(500)
            self.resize(640, 780)
            self._toggles = {}   # cfg_key → _Toggle instance

            root = QVBoxLayout(self)
            root.setSpacing(8)
            root.setContentsMargins(14, 14, 14, 14)

            # ── Header bar ─────────────────────────────────────────────────
            hdr = QFrame()
            hdr.setStyleSheet(
                "background:#1a2332;border-radius:8px;"
            )
            hdr_lay = QHBoxLayout(hdr)
            hdr_lay.setContentsMargins(14, 10, 14, 10)
            title_lbl = QLabel("🩺  Medical Quick Reference")
            title_lbl.setStyleSheet(
                "color:#e8f0fe;font-size:15px;font-weight:700;background:transparent;"
            )
            ver_lbl = QLabel("v8.26")
            ver_lbl.setStyleSheet(
                "color:#4a9fd4;font-size:11px;font-weight:600;"
                "background:#0d1825;border-radius:4px;padding:2px 7px;"
            )
            hdr_lay.addWidget(title_lbl)
            hdr_lay.addStretch()
            hdr_lay.addWidget(ver_lbl)
            root.addWidget(hdr)

            # ── Scrollable content area ────────────────────────────────
            _scroll = QScrollArea()
            _scroll.setWidgetResizable(True)
            _scroll.setFrameShape(QFrame.Shape.NoFrame)
            _scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            _scroll.setStyleSheet(
                "QScrollArea{background:transparent;border:none;}"
                "QScrollBar:vertical{background:#1a1a1a;width:8px;border-radius:4px;}"
                "QScrollBar::handle:vertical{background:#3a3a3a;border-radius:4px;min-height:20px;}"
                "QScrollBar::handle:vertical:hover{background:#4a9fd4;}"
                "QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical{height:0;}"
            )
            _scroll_w = QWidget()
            _scroll_w.setStyleSheet("background:transparent;")
            _scroll_lay = QVBoxLayout(_scroll_w)
            _scroll_lay.setSpacing(8)
            _scroll_lay.setContentsMargins(0, 0, 6, 0)
            _scroll.setWidget(_scroll_w)
            root.addWidget(_scroll, 1)

            # ── Term highlighting ──────────────────────────────────────────
            hl_box = QGroupBox("Term Highlighting")
            hl_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                 "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            hl_row = QHBoxLayout(hl_box)
            hl_row.setContentsMargins(12, 6, 12, 8)
            hl_txt = QVBoxLayout()
            hl_txt.setSpacing(2)
            hl_lbl  = QLabel("Underline recognized medical terms")
            hl_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            hl_sub  = QLabel("Hoverable terms get a subtle underline on card load")
            hl_sub.setStyleSheet("color:#888;font-size:11px;")
            hl_txt.addWidget(hl_lbl)
            hl_txt.addWidget(hl_sub)
            self._tog_underline = _Toggle()
            hl_row.addLayout(hl_txt, 1)
            hl_row.addWidget(self._tog_underline)

            _scroll_lay.addWidget(hl_box)

            # ── Deck priority ──────────────────────────────────────────────
            dp_box = QGroupBox("Deck Priority")
            dp_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                 "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            dp_row = QHBoxLayout(dp_box)
            dp_row.setContentsMargins(12, 6, 12, 8)
            dp_txt = QVBoxLayout()
            dp_txt.setSpacing(2)
            dp_lbl = QLabel("Match lookups to the deck you're studying")
            dp_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            _names = ", ".join(str(p.get("name", "")) for p in _deck_profiles()
                               if isinstance(p, dict))
            _now = _active_profile[0] if _active_profile else "none"
            dp_sub = QLabel("On OB/GYN, Family Medicine, Peds… decks or tags, that "
                            "rotation's cards are checked first, and general words "
                            "(HTN, anemia, UTI) open the rotation-specific card. "
                            f"Profiles: {_names}. Current card: {_now}. "
                            "Advanced: edit \"deck_profiles\" in config.json (Tools → Add-ons → "
                            "select this add-on → View Files).")
            dp_sub.setWordWrap(True)
            dp_sub.setStyleSheet("color:#888;font-size:11px;")
            dp_txt.addWidget(dp_lbl)
            dp_txt.addWidget(dp_sub)
            self._tog_deck_priority = _Toggle()
            dp_row.addLayout(dp_txt, 1)
            dp_row.addWidget(self._tog_deck_priority)

            _scroll_lay.addWidget(dp_box)

            # ── Behavior ───────────────────────────────────────────────────
            beh_box = QGroupBox("Behavior")
            beh_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                  "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            beh_lay = QVBoxLayout(beh_box)
            beh_lay.setContentsMargins(12, 8, 12, 10)
            beh_lay.setSpacing(10)

            # Hover delay slider
            hd_row = QHBoxLayout()
            hd_lbl = QLabel("Hover delay")
            hd_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            hd_lbl.setFixedWidth(110)
            self._delay_slider = QSlider()
            try:
                self._delay_slider.setOrientation(Qt.Orientation.Horizontal)
            except AttributeError:
                self._delay_slider.setOrientation(Qt.Horizontal)
            self._delay_slider.setMinimum(100)
            self._delay_slider.setMaximum(1500)
            self._delay_slider.setSingleStep(50)
            self._delay_slider.setPageStep(100)
            self._delay_slider.setStyleSheet(
                "QSlider::groove:horizontal{height:4px;background:#2a2a2a;border-radius:2px;}"
                "QSlider::handle:horizontal{width:14px;height:14px;margin:-5px 0;"
                "background:#4a9fd4;border-radius:7px;}"
                "QSlider::sub-page:horizontal{background:#1e4a6a;border-radius:2px;}"
            )
            self._delay_val_lbl = QLabel("600 ms")
            self._delay_val_lbl.setFixedWidth(52)
            self._delay_val_lbl.setStyleSheet("color:#4a9fd4;font-size:11px;font-weight:600;")
            def _on_delay(v):
                self._delay_val_lbl.setText(f"{v} ms")
            self._delay_slider.valueChanged.connect(_on_delay)
            hd_sub = QLabel("How long to hover before the tooltip appears")
            hd_sub.setStyleSheet("color:#666;font-size:10px;")
            hd_row.addWidget(hd_lbl)
            hd_row.addWidget(self._delay_slider, 1)
            hd_row.addWidget(self._delay_val_lbl)
            hd_col = QVBoxLayout()
            hd_col.setSpacing(2)
            hd_col.addLayout(hd_row)
            hd_col.addWidget(hd_sub)
            beh_lay.addLayout(hd_col)

            # Min word length + Tooltip max chars (side by side)
            misc_row = QHBoxLayout()
            misc_row.setSpacing(16)

            # Min word length
            mwl_col = QVBoxLayout()
            mwl_col.setSpacing(3)
            mwl_lbl = QLabel("Min word length")
            mwl_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            mwl_sub = QLabel("Shorter words are ignored")
            mwl_sub.setStyleSheet("color:#666;font-size:10px;")
            mwl_row = QHBoxLayout()
            self._min_word_spin = QSpinBox()
            self._min_word_spin.setMinimum(2)
            self._min_word_spin.setMaximum(8)
            self._min_word_spin.setFixedWidth(60)
            self._min_word_spin.setStyleSheet(
                "QSpinBox{background:#111;color:#ddd;border:1px solid #3a3a3a;"
                "border-radius:4px;padding:3px 5px;font-size:12px;}"
                "QSpinBox:focus{border-color:#4a9fd4;}"
                "QSpinBox::up-button,QSpinBox::down-button{width:16px;background:#1e1e1e;"
                "border:none;border-radius:2px;}"
            )
            mwl_row.addWidget(self._min_word_spin)
            mwl_row.addWidget(QLabel("chars"), 1)
            mwl_col.addWidget(mwl_lbl)
            mwl_col.addLayout(mwl_row)
            mwl_col.addWidget(mwl_sub)

            # Tooltip max chars
            tmc_col = QVBoxLayout()
            tmc_col.setSpacing(3)
            tmc_lbl = QLabel("Tooltip max length")
            tmc_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            tmc_sub = QLabel("Length limit for online sources (UMLS, MedlinePlus, Wikipedia)")
            tmc_sub.setStyleSheet("color:#666;font-size:10px;")
            tmc_row = QHBoxLayout()
            self._max_chars_spin = QSpinBox()
            self._max_chars_spin.setMinimum(100)
            self._max_chars_spin.setMaximum(1500)
            self._max_chars_spin.setSingleStep(50)
            self._max_chars_spin.setFixedWidth(75)
            self._max_chars_spin.setStyleSheet(
                "QSpinBox{background:#111;color:#ddd;border:1px solid #3a3a3a;"
                "border-radius:4px;padding:3px 5px;font-size:12px;}"
                "QSpinBox:focus{border-color:#4a9fd4;}"
                "QSpinBox::up-button,QSpinBox::down-button{width:16px;background:#1e1e1e;"
                "border:none;border-radius:2px;}"
            )
            tmc_row.addWidget(self._max_chars_spin)
            tmc_row.addWidget(QLabel("chars"), 1)
            tmc_col.addWidget(tmc_lbl)
            tmc_col.addLayout(tmc_row)
            tmc_col.addWidget(tmc_sub)

            misc_row.addLayout(mwl_col, 1)
            misc_row.addLayout(tmc_col, 1)
            beh_lay.addLayout(misc_row)

            # Tooltip font size (inline with min word / max chars row style)
            fs_row = QHBoxLayout()
            fs_row.setSpacing(16)
            fs_col = QVBoxLayout()
            fs_col.setSpacing(3)
            fs_lbl = QLabel("Tooltip font size")
            fs_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            fs_sub = QLabel("Body text size inside the tooltip")
            fs_sub.setStyleSheet("color:#666;font-size:10px;")
            fs_spin_row = QHBoxLayout()
            from aqt.qt import QDoubleSpinBox
            self._font_size_spin = QDoubleSpinBox()
            self._font_size_spin.setMinimum(9.0)
            self._font_size_spin.setMaximum(20.0)
            self._font_size_spin.setSingleStep(0.5)
            self._font_size_spin.setDecimals(1)
            self._font_size_spin.setFixedWidth(72)
            self._font_size_spin.setStyleSheet(
                "QDoubleSpinBox{background:#111;color:#ddd;border:1px solid #3a3a3a;"
                "border-radius:4px;padding:3px 5px;font-size:12px;}"
                "QDoubleSpinBox:focus{border-color:#4a9fd4;}"
                "QDoubleSpinBox::up-button,QDoubleSpinBox::down-button{width:16px;"
                "background:#1e1e1e;border:none;border-radius:2px;}"
            )
            fs_spin_row.addWidget(self._font_size_spin)
            fs_spin_row.addWidget(QLabel("px"), 1)
            fs_col.addWidget(fs_lbl)
            fs_col.addLayout(fs_spin_row)
            fs_col.addWidget(fs_sub)
            fs_row.addLayout(fs_col, 1)

            th_col = QVBoxLayout()
            th_col.setSpacing(3)
            th_lbl = QLabel("Tooltip theme")
            th_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            th_sub = QLabel("Auto follows Anki's night mode")
            th_sub.setStyleSheet("color:#666;font-size:10px;")
            self._theme_combo = QComboBox()
            for name in _THEMES:
                self._theme_combo.addItem(name)
            self._theme_combo.setFixedWidth(110)
            self._theme_combo.setStyleSheet(
                "QComboBox{background:#111;color:#ddd;border:1px solid #3a3a3a;"
                "border-radius:4px;padding:4px 8px;font-size:12px;}"
                "QComboBox:focus{border-color:#4a9fd4;}"
                "QComboBox::drop-down{border:none;width:20px;}"
                "QComboBox QAbstractItemView{background:#1a1a1a;color:#ddd;"
                "selection-background-color:#1e3a5a;border:1px solid #3a3a3a;}"
            )
            th_col.addWidget(th_lbl)
            th_col.addWidget(self._theme_combo)
            th_col.addWidget(th_sub)
            fs_row.addLayout(th_col, 1)
            beh_lay.addLayout(fs_row)

            _scroll_lay.addWidget(beh_box)

            # ── Search & Display ───────────────────────────────────────────
            srch_box = QGroupBox("Search && Shortcuts")
            srch_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                   "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            srch_lay = QVBoxLayout(srch_box)
            srch_lay.setContentsMargins(12, 8, 12, 10)
            srch_lay.setSpacing(10)

            # Search prefix
            sp_col = QVBoxLayout()
            sp_col.setSpacing(3)
            sp_lbl = QLabel("Cmd+S search prefix")
            sp_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            sp_sub = QLabel('Prepended to every Cmd+S query (e.g. "explain" → "explain aspirin")')
            sp_sub.setStyleSheet("color:#666;font-size:10px;")
            sp_sub.setWordWrap(True)
            self._search_prefix_edit = QLineEdit()
            self._search_prefix_edit.setPlaceholderText('e.g.  explain   or   USMLE   or leave blank')
            self._search_prefix_edit.setStyleSheet(
                "QLineEdit{background:#111;color:#ddd;border:1px solid #3a3a3a;"
                "border-radius:4px;padding:5px 8px;font-size:12px;}"
                "QLineEdit:focus{border:1px solid #4a9fd4;}"
            )
            sp_col.addWidget(sp_lbl)
            sp_col.addWidget(self._search_prefix_edit)
            sp_col.addWidget(sp_sub)
            srch_lay.addLayout(sp_col)

            # Search engine dropdowns side-by-side
            eng_row = QHBoxLayout()
            eng_row.setSpacing(16)

            se_col = QVBoxLayout()
            se_col.setSpacing(3)
            se_lbl = QLabel("Cmd+S search engine")
            se_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            self._search_engine_combo = QComboBox()
            for name in ["Google", "Bing", "DuckDuckGo", "PubMed"]:
                self._search_engine_combo.addItem(name)
            self._search_engine_combo.setStyleSheet(
                "QComboBox{background:#111;color:#ddd;border:1px solid #3a3a3a;"
                "border-radius:4px;padding:4px 8px;font-size:12px;}"
                "QComboBox:focus{border-color:#4a9fd4;}"
                "QComboBox::drop-down{border:none;width:20px;}"
                "QComboBox QAbstractItemView{background:#1a1a1a;color:#ddd;"
                "selection-background-color:#1e3a5a;border:1px solid #3a3a3a;}"
            )
            se_col.addWidget(se_lbl)
            se_col.addWidget(self._search_engine_combo)

            ise_col = QVBoxLayout()
            ise_col.setSpacing(3)
            ise_lbl = QLabel("Cmd+I image engine")
            ise_lbl.setStyleSheet("font-weight:500;font-size:12px;")
            self._image_engine_combo = QComboBox()
            for name in ["Google Images", "Bing Images", "DuckDuckGo Images"]:
                self._image_engine_combo.addItem(name)
            self._image_engine_combo.setStyleSheet(
                "QComboBox{background:#111;color:#ddd;border:1px solid #3a3a3a;"
                "border-radius:4px;padding:4px 8px;font-size:12px;}"
                "QComboBox:focus{border-color:#4a9fd4;}"
                "QComboBox::drop-down{border:none;width:20px;}"
                "QComboBox QAbstractItemView{background:#1a1a1a;color:#ddd;"
                "selection-background-color:#1e3a5a;border:1px solid #3a3a3a;}"
            )
            ise_col.addWidget(ise_lbl)
            ise_col.addWidget(self._image_engine_combo)

            eng_row.addLayout(se_col, 1)
            eng_row.addLayout(ise_col, 1)
            srch_lay.addLayout(eng_row)
            _scroll_lay.addWidget(srch_box)

            # ── Offline tiers ──────────────────────────────────────────────
            tier_box = QGroupBox("Offline Lookup Tiers")
            tier_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                   "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            tier_outer = QVBoxLayout(tier_box)
            tier_outer.setContentsMargins(10, 6, 10, 10)
            tier_outer.setSpacing(4)

            # Sub-header row with bulk enable/disable buttons
            sub_row = QHBoxLayout()
            sub_row.setSpacing(6)
            sub_note = QLabel("All tiers are instant & offline — zero network cost")
            sub_note.setStyleSheet("color:#888;font-size:11px;")
            en_btn = QPushButton("Enable All")
            en_btn.setFixedHeight(22)
            en_btn.setStyleSheet(
                "QPushButton{font-size:11px;padding:0 8px;"
                "background:#1e3a1e;color:#4CAF50;"
                "border:1px solid rgba(76,175,80,0.47);border-radius:4px;}"
                "QPushButton:hover{background:#284228;}"
            )
            dis_btn = QPushButton("Disable All")
            dis_btn.setFixedHeight(22)
            dis_btn.setStyleSheet(
                "QPushButton{font-size:11px;padding:0 8px;"
                "background:#3a1e1e;color:#e05c5c;"
                "border:1px solid rgba(224,92,92,0.47);border-radius:4px;}"
                "QPushButton:hover{background:#4a2a2a;}"
            )
            def _enable_all():
                for t in self._toggles.values():
                    t.setChecked(True)
            def _disable_all():
                for t in self._toggles.values():
                    t.setChecked(False)
            en_btn.clicked.connect(_enable_all)
            dis_btn.clicked.connect(_disable_all)
            sub_row.addWidget(sub_note)
            sub_row.addStretch()
            sub_row.addWidget(en_btn)
            sub_row.addWidget(dis_btn)
            tier_outer.addLayout(sub_row)

            # Divider
            div = QFrame()
            try:
                div.setFrameShape(QFrame.Shape.HLine)
            except AttributeError:
                div.setFrameShape(QFrame.HLine)
            div.setStyleSheet("color:#333;margin:2px 0;")
            tier_outer.addWidget(div)

            # One row per tier
            for cfg_key, name, tier_id, color, desc in _TIERS:
                row_w = QWidget()
                row_w.setStyleSheet(
                    "QWidget{border-radius:5px;}"
                    "QWidget:hover{background:#1a1a1a;}"
                )
                row = QHBoxLayout(row_w)
                row.setContentsMargins(4, 4, 6, 4)
                row.setSpacing(10)

                # Tier ID badge
                badge = QLabel(tier_id)
                badge.setFixedWidth(64)
                try:
                    badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
                except AttributeError:
                    badge.setAlignment(Qt.AlignCenter)
                badge.setStyleSheet(
                    f"background:{_rgba(color, 0.1)};color:{color};"
                    f"font-size:10px;font-weight:700;"
                    f"border-radius:4px;padding:2px 3px;"
                    f"border:1px solid {_rgba(color, 0.33)};"
                )

                # Name + description
                txt_w = QVBoxLayout()
                txt_w.setSpacing(1)
                name_lbl = QLabel(name)
                name_lbl.setStyleSheet("font-weight:600;font-size:12px;")
                desc_lbl = QLabel(desc)
                desc_lbl.setWordWrap(True)   # long descriptions pushed toggles off-screen
                desc_lbl.setStyleSheet("color:#777;font-size:11px;")
                txt_w.addWidget(name_lbl)
                txt_w.addWidget(desc_lbl)

                tog = _Toggle()
                self._toggles[cfg_key] = tog

                row.addWidget(badge)
                row.addLayout(txt_w, 1)
                row.addWidget(tog)
                tier_outer.addWidget(row_w)


            _scroll_lay.addWidget(tier_box)

            # ── Network Tiers ──────────────────────────────────────────────
            net_box = QGroupBox("Online Sources  (searched at the same time)")
            net_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                  "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            net_outer = QVBoxLayout(net_box)
            net_outer.setContentsMargins(10, 6, 10, 10)
            net_outer.setSpacing(4)

            _NET_TIERS = [
                ("tier_omim",        "OMIM",         "Tier 6.5", "#9b59b6",
                 "Genetic disease DB — MIM numbers, gene symbols, inheritance (needs API key)"),
                ("tier_rxnorm",      "RxNorm",       "Tier 4",   "#5a9fd4",
                 "Drug identification — generic names, brand names, RxCUI links"),
                ("tier_openfda",     "OpenFDA",      "Tier 4.5", "#9c7fc1",
                 "Full drug labels — MOA, indications, warnings, adverse reactions"),
                ("tier_medlineplus", "MedlinePlus",  "Tier 5",   "#4a9e6b",
                 "NLM consumer health summaries — diseases, procedures, conditions"),
                ("tier_wikipedia",   "Wikipedia",    "Tier 6",   "#888888",
                 "Broad fallback — medical articles filtered for clinical relevance"),
                ("wikipedia_images", "Wikipedia images", "Images", "#888888",
                 "Show the article's picture above any definition (click it to enlarge)"),
            ]
            self._net_toggles = {}
            for cfg_key, name, tier_id, color, desc in _NET_TIERS:
                row_w = QWidget()
                row_w.setStyleSheet(
                    "QWidget{border-radius:5px;}"
                    "QWidget:hover{background:#1a1a1a;}"
                )
                row = QHBoxLayout(row_w)
                row.setContentsMargins(4, 4, 6, 4)
                row.setSpacing(10)
                badge = QLabel(tier_id)
                badge.setFixedWidth(64)
                try:
                    badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
                except AttributeError:
                    badge.setAlignment(Qt.AlignCenter)
                badge.setStyleSheet(
                    f"background:{_rgba(color, 0.1)};color:{color};"
                    f"font-size:10px;font-weight:700;"
                    f"border-radius:4px;padding:2px 3px;"
                    f"border:1px solid {_rgba(color, 0.33)};"
                )
                txt_w = QVBoxLayout()
                txt_w.setSpacing(1)
                name_lbl = QLabel(name)
                name_lbl.setStyleSheet("font-weight:600;font-size:12px;")
                desc_lbl = QLabel(desc)
                desc_lbl.setWordWrap(True)   # long descriptions pushed toggles off-screen
                desc_lbl.setStyleSheet("color:#777;font-size:11px;")
                txt_w.addWidget(name_lbl)
                txt_w.addWidget(desc_lbl)
                tog = _Toggle()
                self._net_toggles[cfg_key] = tog
                row.addWidget(badge)
                row.addLayout(txt_w, 1)
                row.addWidget(tog)
                net_outer.addWidget(row_w)
            _scroll_lay.addWidget(net_box)

            # ── UMLS API Key ───────────────────────────────────────────────
            api_box = QGroupBox("UMLS API Key  (optional)")
            api_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                  "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            api_lay = QVBoxLayout(api_box)
            api_lay.setContentsMargins(12, 6, 12, 10)
            api_lay.setSpacing(6)

            info_lbl = QLabel(
                "Get a free key at <b>uts.nlm.nih.gov</b> — enables the full "
                "3.7M-term UMLS vocabulary as a network fallback tier."
            )
            info_lbl.setWordWrap(True)
            info_lbl.setStyleSheet("color:#999;font-size:11px;")
            api_lay.addWidget(info_lbl)

            key_row = QHBoxLayout()
            key_row.setSpacing(6)
            self._api_field = QLineEdit()
            self._api_field.setPlaceholderText("Paste UMLS API key here…")
            try:
                self._api_field.setEchoMode(QLineEdit.EchoMode.Password)
            except AttributeError:
                self._api_field.setEchoMode(QLineEdit.Password)
            self._api_field.setStyleSheet(
                "QLineEdit{"
                "  background:#111111;color:#dddddd;"
                "  border:1px solid #3a3a3a;border-radius:5px;"
                "  padding:5px 8px;font-family:monospace;font-size:12px;"
                "}"
                "QLineEdit:focus{border:1px solid #4a9fd4;}"
            )

            self._show_btn = QPushButton("Show")
            self._show_btn.setFixedWidth(54)
            self._show_btn.setCheckable(True)
            self._show_btn.setStyleSheet(
                "QPushButton{background:#222;color:#999;"
                "border:1px solid #444;border-radius:5px;"
                "padding:5px;font-size:11px;}"
                "QPushButton:checked{color:#4a9fd4;border-color:#4a9fd4;}"
                "QPushButton:hover{background:#2a2a2a;}"
            )
            self._show_btn.toggled.connect(self._toggle_key_vis)

            self._test_btn = QPushButton("Test ▶")
            self._test_btn.setFixedWidth(60)
            self._test_btn.setStyleSheet(
                "QPushButton{background:#0d1e2e;color:#4a9fd4;"
                "border:1px solid #4a9fd4;border-radius:5px;"
                "padding:5px;font-size:11px;font-weight:600;}"
                "QPushButton:hover{background:#0d2a3e;}"
                "QPushButton:disabled{color:#555;border-color:#333;}"
            )
            self._test_btn.clicked.connect(self._test_key)

            key_row.addWidget(self._api_field, 1)
            key_row.addWidget(self._show_btn)
            key_row.addWidget(self._test_btn)
            api_lay.addLayout(key_row)

            self._api_status = QLabel("")
            self._api_status.setStyleSheet("font-size:11px;min-height:16px;")
            api_lay.addWidget(self._api_status)
            _scroll_lay.addWidget(api_box)

            # ── OMIM API Key ──────────────────────────────────────────────
            omim_box = QGroupBox("OMIM API Key  (genetic diseases — Tier 6.5)")
            omim_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                   "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            omim_lay = QVBoxLayout(omim_box)
            omim_lay.setContentsMargins(12, 6, 12, 10)
            omim_lay.setSpacing(6)
            omim_info = QLabel(
                "Free key at <b>omim.org/api</b> — enables OMIM genetic disease lookups "
                "(MIM number, gene symbol) as an online fallback tier."
            )
            omim_info.setWordWrap(True)
            omim_info.setStyleSheet("color:#999;font-size:11px;")
            omim_lay.addWidget(omim_info)
            omim_key_row = QHBoxLayout()
            omim_key_row.setSpacing(6)
            self._omim_field = QLineEdit()
            self._omim_field.setPlaceholderText("Paste OMIM API key here…")
            try:
                self._omim_field.setEchoMode(QLineEdit.EchoMode.Password)
            except AttributeError:
                self._omim_field.setEchoMode(QLineEdit.Password)
            self._omim_field.setStyleSheet(
                "QLineEdit{background:#111111;color:#dddddd;"
                "border:1px solid #3a3a3a;border-radius:5px;"
                "padding:5px 8px;font-family:monospace;font-size:12px;}"
                "QLineEdit:focus{border:1px solid #9b59b6;}"
            )
            self._omim_show = QPushButton("Show")
            self._omim_show.setFixedWidth(54)
            self._omim_show.setCheckable(True)
            self._omim_show.setStyleSheet(
                "QPushButton{background:#222;color:#999;border:1px solid #444;"
                "border-radius:5px;padding:5px;font-size:11px;}"
                "QPushButton:checked{color:#9b59b6;border-color:#9b59b6;}"
                "QPushButton:hover{background:#2a2a2a;}"
            )
            def _toggle_omim_vis(show, f=self._omim_field, b=self._omim_show):
                try:
                    f.setEchoMode(QLineEdit.EchoMode.Normal if show else QLineEdit.EchoMode.Password)
                except AttributeError:
                    f.setEchoMode(QLineEdit.Normal if show else QLineEdit.Password)
                b.setText("Hide" if show else "Show")
            self._omim_show.toggled.connect(_toggle_omim_vis)
            omim_key_row.addWidget(self._omim_field, 1)
            omim_key_row.addWidget(self._omim_show)
            self._omim_test_btn = QPushButton("Test ▶")
            self._omim_test_btn.setFixedWidth(60)
            self._omim_test_btn.setStyleSheet(
                "QPushButton{background:#1a2a3a;color:#7ab8e8;border:1px solid #2a4a6a;"
                "border-radius:4px;font-size:11px;padding:3px 6px;}"
                "QPushButton:hover{background:#1e3450;}"
                "QPushButton:disabled{color:#555;}"
            )
            omim_key_row.addWidget(self._omim_test_btn)
            omim_lay.addLayout(omim_key_row)
            self._omim_status = QLabel("")
            self._omim_status.setStyleSheet("color:#888;font-size:11px;")
            _omim_stat_row = QHBoxLayout()
            _omim_stat_row.addStretch()
            _omim_stat_row.addWidget(self._omim_status)
            omim_lay.addLayout(_omim_stat_row)
            self._omim_test_btn.clicked.connect(self._test_omim_key)
            _scroll_lay.addWidget(omim_box)

            # ── Network Timeouts ──────────────────────────────────────────
            to_box = QGroupBox("Network Timeouts  (seconds per tier)")
            to_box.setStyleSheet("QGroupBox{font-weight:600;margin-top:6px;}"
                                 "QGroupBox::title{subcontrol-origin:margin;left:8px;}")
            to_lay = QVBoxLayout(to_box)
            to_lay.setContentsMargins(12, 6, 12, 10)
            to_lay.setSpacing(6)
            to_info = QLabel(
                "Reduce timeouts for snappier tooltips on fast connections; "
                "increase if you see frequent lookup failures."
            )
            to_info.setWordWrap(True)
            to_info.setStyleSheet("color:#999;font-size:11px;")
            to_lay.addWidget(to_info)
            _to_cfg = _get_user_cfg()
            _to_grid = QHBoxLayout()
            _to_grid.setSpacing(16)
            self._to_spins = {}
            for _lbl, _key, _def in [
                ("UMLS",        "umls_timeout",       8),
                ("RxNorm",      "rxnorm_timeout",      6),
                ("OpenFDA",     "openfda_timeout",     6),
                ("MedlinePlus", "medlineplus_timeout", 5),
                ("Wikipedia",   "wikipedia_timeout",   5),
                ("OMIM",        "omim_timeout",        6),
            ]:
                _col = QVBoxLayout()
                _col.setSpacing(2)
                _sp = QSpinBox()
                _sp.setRange(2, 30)
                _sp.setSuffix(" s")
                _sp.setValue(int(_to_cfg.get(_key, _def)))
                _sp.setFixedWidth(68)
                _sp.setStyleSheet(
                    "QSpinBox{background:#141414;color:#ccc;border:1px solid #333;"
                    "border-radius:4px;padding:2px 4px;font-size:12px;}"
                )
                _lbl_w = QLabel(_lbl)
                _lbl_w.setStyleSheet("color:#8a9aaa;font-size:10px;")
                _lbl_w.setAlignment(Qt.AlignmentFlag.AlignCenter
                                    if hasattr(Qt, 'AlignmentFlag')
                                    else Qt.AlignCenter)
                _col.addWidget(_sp)
                _col.addWidget(_lbl_w)
                _to_grid.addLayout(_col)
                self._to_spins[_key] = _sp
            _to_grid.addStretch()
            to_lay.addLayout(_to_grid)
            _scroll_lay.addWidget(to_box)

            # ── Keyboard shortcut reminder ────────────────────────────────
            sc_frame = QFrame()
            sc_frame.setStyleSheet(
                "background:#0d1825;border-radius:6px;border:1px solid #1e3a5a;"
            )
            sc_lay = QHBoxLayout(sc_frame)
            sc_lay.setContentsMargins(12, 8, 12, 8)
            sc_icon = QLabel("⌨")
            sc_icon.setStyleSheet("font-size:16px;background:transparent;")
            sc_txt = QVBoxLayout()
            sc_txt.setSpacing(1)
            sc_title = QLabel("Keyboard Shortcuts")
            sc_title.setStyleSheet("font-weight:600;font-size:12px;color:#7ab8e8;background:transparent;")
            sc_desc = QLabel(
                "⌘ S      — Search selected text (or hovered word) in configured search engine\n"
                "⌘ I       — Image search selected text (or hovered word)\n"
                "⌘ hold  — While a tooltip is open, hold Cmd/Ctrl to freeze it (⌘ icon appears)\n"
                "Hover    — Move over any underlined word for an instant definition\n"
                "Mnemonic — Hover an acronym like MMAPP to see the list it stands for on the card"
            )
            sc_desc.setWordWrap(True)
            sc_desc.setStyleSheet("color:#8a9aaa;font-size:11px;background:transparent;")
            sc_txt.addWidget(sc_title)
            sc_txt.addWidget(sc_desc)
            sc_lay.addWidget(sc_icon)
            sc_lay.addLayout(sc_txt, 1)
            _scroll_lay.addWidget(sc_frame)

            # ── Network note ───────────────────────────────────────────────
            net_note = QLabel(
                "⚡  RxNorm · OpenFDA · MedlinePlus · Wikipedia need no API key. "
                "Turn any source off above; OMIM needs its own key."
            )
            net_note.setWordWrap(True)
            net_note.setStyleSheet("color:#555;font-size:11px;")
            _scroll_lay.addWidget(net_note)

            # ── Save / Cancel ──────────────────────────────────────────────
            _scroll_lay.addStretch()

            foot = QHBoxLayout()
            foot.setSpacing(8)
            cancel_btn = QPushButton("Cancel")
            save_btn   = QPushButton("Save Settings")
            cancel_btn.setFixedHeight(32)
            save_btn.setFixedHeight(32)
            cancel_btn.setStyleSheet(
                "QPushButton{background:#242424;color:#aaa;"
                "border:1px solid #444;border-radius:6px;padding:0 18px;}"
                "QPushButton:hover{background:#2e2e2e;}"
            )
            save_btn.setStyleSheet(
                "QPushButton{background:#1a3a1a;color:#4CAF50;"
                "border:1px solid #4CAF50;border-radius:6px;"
                "padding:0 22px;font-weight:600;}"
                "QPushButton:hover{background:#1e4a1e;}"
            )
            cancel_btn.clicked.connect(self.reject)
            save_btn.clicked.connect(self._save)
            foot.addStretch()
            foot.addWidget(cancel_btn)
            foot.addWidget(save_btn)
            root.addLayout(foot)

            self._load()

        # ── helpers ────────────────────────────────────────────────────────
        def _toggle_key_vis(self, show):
            try:
                mode = QLineEdit.EchoMode.Normal if show else QLineEdit.EchoMode.Password
            except AttributeError:
                mode = QLineEdit.Normal if show else QLineEdit.Password
            self._api_field.setEchoMode(mode)
            self._show_btn.setText("Hide" if show else "Show")

        def _test_key(self):
            key = self._api_field.text().strip()
            if not key:
                self._api_status.setText("⚠  Enter a key first.")
                self._api_status.setStyleSheet("color:#c8a84b;font-size:11px;")
                return
            self._api_status.setText("⏳  Connecting to UMLS…")
            self._api_status.setStyleSheet("color:#888;font-size:11px;")
            self._test_btn.setEnabled(False)
            import threading, urllib.request, urllib.parse
            def _check(k=key):
                ok = False
                try:
                    req = urllib.request.Request(
                        "https://uts-ws.nlm.nih.gov/rest/search/current"
                        "?string=asthma&pageSize=1&apiKey=" + urllib.parse.quote(k),
                        headers=_HEADERS)
                    with _urlopen(req, timeout=8) as r:
                        ok = (r.status == 200)    # invalid keys get 401
                except Exception:
                    pass
                def _upd():
                    try:
                        self._test_btn.setEnabled(True)
                    except RuntimeError:   # dialog closed before the answer came back
                        return
                    if ok:
                        self._api_status.setText("✅  Valid key — UMLS tier is active.")
                        self._api_status.setStyleSheet("color:#4CAF50;font-size:11px;")
                    else:
                        self._api_status.setText("❌  Invalid key or network error.")
                        self._api_status.setStyleSheet("color:#e05c5c;font-size:11px;")
                mw.taskman.run_on_main(_upd)
            threading.Thread(target=_check, daemon=True).start()

        def _test_omim_key(self):
            key = self._omim_field.text().strip()
            if not key:
                self._omim_status.setText("⚠  Enter a key first.")
                self._omim_status.setStyleSheet("color:#c8a84b;font-size:11px;")
                return
            self._omim_status.setText("⏳  Connecting to OMIM…")
            self._omim_status.setStyleSheet("color:#888;font-size:11px;")
            self._omim_test_btn.setEnabled(False)
            import threading, urllib.request, json as _json
            def _check(k=key):
                ok = False
                try:
                    _url = (
                        f"https://api.omim.org/api/entry/search"
                        f"?search=BRCA1&format=json&apiKey={urllib.parse.quote(k)}&limit=1"
                    )
                    _req = urllib.request.Request(_url, headers=_HEADERS)
                    with _urlopen(_req, timeout=8) as _r:
                        _body = _json.loads(_r.read().decode())
                        ok = bool(
                            _body.get("omim", {})
                                 .get("searchResponse", {})
                                 .get("entryList")
                        )
                except Exception:
                    pass
                def _upd():
                    try:
                        self._omim_test_btn.setEnabled(True)
                    except RuntimeError:   # dialog closed before the answer came back
                        return
                    if ok:
                        self._omim_status.setText("✅  Valid key — OMIM tier is active.")
                        self._omim_status.setStyleSheet("color:#4CAF50;font-size:11px;")
                    else:
                        self._omim_status.setText("❌  Invalid key or network error.")
                        self._omim_status.setStyleSheet("color:#e05c5c;font-size:11px;")
                mw.taskman.run_on_main(_upd)
            threading.Thread(target=_check, daemon=True).start()

        def _load(self):
            cfg = _get_user_cfg()
            self._tog_underline.setChecked(cfg.get("underline_terms", True))
            self._tog_deck_priority.setChecked(cfg.get("deck_priority", True))
            for key, tog in self._toggles.items():
                tog.setChecked(cfg.get(key, True))
            # tier_omim defaults False everywhere else — keep the UI consistent
            _net_defaults = {
                "tier_omim": False,
            }
            for key, tog in self._net_toggles.items():
                tog.setChecked(cfg.get(key, _net_defaults.get(key, True)))
            # Behavior fields
            delay = cfg.get("hover_delay_ms", CFG.get("hover_delay_ms", 300))
            self._delay_slider.setValue(int(delay))
            self._delay_val_lbl.setText(f"{int(delay)} ms")
            self._min_word_spin.setValue(cfg.get("min_word_len", CFG.get("min_word_len", 3)))
            self._max_chars_spin.setValue(cfg.get("tooltip_max_chars", CFG.get("tooltip_max_chars", 450)))
            self._font_size_spin.setValue(float(cfg.get("tooltip_font_size", 12.5)))
            self._search_prefix_edit.setText(cfg.get("search_prefix", ""))
            _se_idx = self._search_engine_combo.findText(cfg.get("search_engine", "Google"))
            self._search_engine_combo.setCurrentIndex(max(0, _se_idx))
            _ise_idx = self._image_engine_combo.findText(cfg.get("image_search_engine", "Google Images"))
            self._image_engine_combo.setCurrentIndex(max(0, _ise_idx))
            self._theme_combo.setCurrentIndex(max(0, self._theme_combo.findText(
                cfg.get("tooltip_theme", "Auto"))))
            saved_key = (cfg.get("umls_api_key") or "").strip()
            self._api_field.setText(saved_key)
            omim_key = (cfg.get("omim_api_key") or "").strip()
            self._omim_field.setText(omim_key)
            # Timeout spinboxes
            _to_defaults = {
                "umls_timeout": 8, "rxnorm_timeout": 6, "openfda_timeout": 6,
                "medlineplus_timeout": 5, "wikipedia_timeout": 5, "omim_timeout": 6,
            }
            for _k, _sp in self._to_spins.items():
                _sp.setValue(int(cfg.get(_k, _to_defaults.get(_k, 6))))

        def _save(self):
            # Copy: _get_user_cfg() returns the shared cached dict
            cfg = dict(_get_user_cfg())
            cfg["underline_terms"] = self._tog_underline.isChecked()
            cfg["deck_priority"] = self._tog_deck_priority.isChecked()
            for key, tog in self._toggles.items():
                cfg[key] = tog.isChecked()
            for key, tog in self._net_toggles.items():
                cfg[key] = tog.isChecked()
            # Behavior values — save and apply live
            delay = self._delay_slider.value()
            min_w = self._min_word_spin.value()
            max_c = self._max_chars_spin.value()
            cfg["hover_delay_ms"]      = delay
            cfg["min_word_len"]        = min_w
            cfg["tooltip_max_chars"]   = max_c
            CFG["hover_delay_ms"]      = delay
            CFG["min_word_len"]        = min_w
            CFG["tooltip_max_chars"]   = max_c
            cfg["tooltip_font_size"]   = self._font_size_spin.value()
            CFG["tooltip_font_size"]   = self._font_size_spin.value()
            cfg["search_prefix"]       = self._search_prefix_edit.text().strip()
            CFG["search_prefix"]       = cfg["search_prefix"]
            cfg["search_engine"]       = self._search_engine_combo.currentText()
            CFG["search_engine"]       = cfg["search_engine"]
            cfg["image_search_engine"] = self._image_engine_combo.currentText()
            cfg["tooltip_theme"]       = self._theme_combo.currentText()
            CFG["image_search_engine"] = cfg["image_search_engine"]
            api_key = self._api_field.text().strip()
            cfg["umls_api_key"] = api_key
            CFG["umls_api_key"] = api_key
            omim_key = self._omim_field.text().strip()
            cfg["omim_api_key"] = omim_key
            CFG["omim_api_key"] = omim_key
            # Per-tier timeouts
            for _k, _sp in self._to_spins.items():
                cfg[_k] = _sp.value()
            # Flush config cache so next read returns fresh values
            global _cfg_cache, _cfg_cache_ts, _last_js_cfg_key
            _cfg_cache = {}
            _cfg_cache_ts = 0.0
            _last_js_cfg_key = ""   # force JS rebuild on next card flip
            # Drop cached definitions so tier on/off and length changes apply now
            with _cache_lock:
                _cache.clear()
                _miss_cache.clear()
            _user_cfg_save(cfg)
            # Apply the deck-priority switch to the card already on screen
            _set_profile(getattr(getattr(mw, "reviewer", None), "card", None))
            self.accept()

    dlg = _SettingsDlg(mw)
    dlg.exec()

# ─────────────────────────────────────────────────────────────────────────────
# 14 · Tools menu & add-on config button
# ─────────────────────────────────────────────────────────────────────────────

def _add_menu():
    from aqt.qt import QAction
    action = QAction("Medical Quick Reference Settings…", mw)
    action.triggered.connect(_open_settings)
    mw.form.menuTools.addAction(action)
    # Wire the "Config" button in Tools → Add-ons to open the custom UI
    # instead of Anki's default raw-JSON editor.
    mw.addonManager.setConfigAction(__name__, _open_settings)
    if _DATA_ERRORS:
        # A broken dictionary file: say which one, keep everything else working
        from aqt.utils import showWarning
        QTimer.singleShot(1500, lambda: showWarning(
            "Medical Quick Reference could not load some of its dictionary files, "
            "so their entries are unavailable until the file is fixed:\n\n"
            + "\n".join(_DATA_ERRORS)))

gui_hooks.main_window_did_init.append(_add_menu)

