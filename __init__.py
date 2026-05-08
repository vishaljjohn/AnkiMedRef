# ─────────────────────────────────────────────────────────────────────────────
#  Anki Add-on: Medical Quick Reference  v7.3
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

import os
import re
import json
import sqlite3
import threading
import time
import urllib.request
import urllib.parse

# SSL fix for macOS — ensures UMLS API calls work
try:
    import ssl, certifi
    ssl._create_default_https_context = lambda: ssl.create_default_context(
        cafile=certifi.where()
    )
except ImportError:
    pass  # certifi not installed; SSL will use system defaults

from aqt import mw, gui_hooks
from aqt.reviewer import Reviewer
from aqt.qt import QTimer

# ─────────────────────────────────────────────────────────────────────────────
# 1 · Configuration
#     ► Paste your UMLS API key (from https://uts.nlm.nih.gov) between the
#       quotes next to "umls_api_key" to unlock the UMLS REST API fallback.
# ─────────────────────────────────────────────────────────────────────────────

CFG = {
    "hover_delay_ms":          300,
    "min_word_len":            3,
    "tooltip_max_chars":       450,
    "inject_initial_delay_ms": 80,
    "inject_max_retries":      18,
    "umls_api_key":            "",   # ← paste your UMLS API key here
}

# ─────────────────────────────────────────────────────────────────────────────
# 2 · Local MeSH / UMLS database
# ─────────────────────────────────────────────────────────────────────────────

_ADDON_DIR = os.path.dirname(os.path.abspath(__file__))
_DB_PATH   = os.path.join(_ADDON_DIR, "med_terms.db")
_db_conn   = None


def _get_db():
    global _db_conn
    if _db_conn is None and os.path.exists(_DB_PATH):
        try:
            _db_conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
        except Exception:
            pass
    return _db_conn


def _lookup_local_db(phrase):
    """Returns (definition, sem_type) or ('', '').  Supports both old and new schema."""
    db = _get_db()
    if not db:
        return "", ""
    try:
        try:
            row = db.execute(
                "SELECT definition, sem_type FROM terms "
                "WHERE term = ? COLLATE NOCASE LIMIT 1",
                (phrase.strip(),),
            ).fetchone()
            if row:
                return row[0], (row[1] or "")
        except sqlite3.OperationalError:
            # Old DB without sem_type column
            row = db.execute(
                "SELECT definition FROM terms "
                "WHERE term = ? COLLATE NOCASE LIMIT 1",
                (phrase.strip(),),
            ).fetchone()
            if row:
                return row[0], ""
    except Exception:
        pass
    return "", ""

# ─────────────────────────────────────────────────────────────────────────────
# 3 · Medical abbreviation dictionary  (Tier 0 — zero latency)
# ─────────────────────────────────────────────────────────────────────────────

_ABBREVS = {
    # ── Vital signs & monitoring ─────────────────────────────────────────────
    "BP":    "Blood Pressure.",
    "HR":    "Heart Rate (beats per minute).",
    "RR":    "Respiratory Rate (breaths/min). Also: Relative Risk in stats.",
    "SpO2":  "Peripheral Oxygen Saturation via pulse oximetry. Normal ≥95%.",
    "SaO2":  "Arterial Oxygen Saturation from ABG. Normal ≥95%.",
    "MAP":   "Mean Arterial Pressure = (SBP + 2×DBP)/3. Target ≥65 mmHg in sepsis.",
    "SBP":   "Systolic Blood Pressure. Also: Spontaneous Bacterial Peritonitis.",
    "DBP":   "Diastolic Blood Pressure.",
    "CVP":   "Central Venous Pressure — reflects right atrial preload. Normal 2–8 mmHg.",
    "JVD":   "Jugular Venous Distension — sign of elevated CVP or right HF.",
    "PEEP":  "Positive End-Expiratory Pressure — prevents alveolar collapse on ventilator.",
    "TV":    "Tidal Volume — air per breath (~500 mL in adults). Also: Tidal Volume on vent.",
    "FiO2":  "Fraction of Inspired Oxygen (0.21 = room air, 1.0 = 100%).",
    # ── Labs — haematology ───────────────────────────────────────────────────
    "CBC":   "Complete Blood Count — WBC, RBC, Hgb, Hct, MCV, platelets.",
    "WBC":   "White Blood Cell count. Normal 4.5–11 × 10³/µL.",
    "RBC":   "Red Blood Cell count. Normal M: 4.7–6.1, F: 4.2–5.4 × 10⁶/µL.",
    "Hgb":   "Hemoglobin. Normal M: 13.5–17.5, F: 12–16 g/dL.",
    "Hct":   "Hematocrit — % RBC volume. Normal M: 41–53%, F: 36–46%.",
    "MCV":   "Mean Corpuscular Volume — RBC size. Normal 80–100 fL.",
    "MCH":   "Mean Corpuscular Hemoglobin. Normal 27–33 pg.",
    "MCHC":  "Mean Corpuscular Hemoglobin Concentration. Normal 33–36 g/dL.",
    "PLT":   "Platelets. Normal 150–400 × 10³/µL.",
    "PT":    "Prothrombin Time — extrinsic pathway. Normal 11–13.5 s.",
    "INR":   "International Normalized Ratio — standardised PT. Therapeutic 2–3.",
    "aPTT":  "Activated Partial Thromboplastin Time — intrinsic pathway. Normal 25–40 s.",
    "DIC":   "Disseminated Intravascular Coagulation — simultaneous clotting and bleeding.",
    # ── Labs — metabolic ────────────────────────────────────────────────────
    "BMP":   "Basic Metabolic Panel — Na, K, Cl, HCO3, BUN, Cr, glucose.",
    "CMP":   "Comprehensive Metabolic Panel — BMP + LFTs, albumin, Ca.",
    "BUN":   "Blood Urea Nitrogen — renal/hepatic marker. Normal 7–20 mg/dL.",
    "Cr":    "Creatinine — renal function marker. Normal M: 0.7–1.3, F: 0.6–1.1 mg/dL.",
    "eGFR":  "Estimated Glomerular Filtration Rate — CKD staging. Normal >90 mL/min/1.73m².",
    "Na":    "Sodium. Normal 135–145 mEq/L.",
    "K":     "Potassium. Normal 3.5–5.0 mEq/L.",
    "Ca":    "Calcium. Normal 8.5–10.5 mg/dL (correct for albumin).",
    "Mg":    "Magnesium. Normal 1.7–2.2 mg/dL.",
    "Phos":  "Phosphorus. Normal 2.5–4.5 mg/dL.",
    "HCO3":  "Bicarbonate. Normal 22–26 mEq/L.",
    "LDH":   "Lactate Dehydrogenase — tissue damage marker. Normal 140–280 U/L.",
    "Lac":   "Lactate — tissue hypoperfusion marker. Normal <2 mmol/L; >4 = shock.",
    "ABG":   "Arterial Blood Gas — pO2, pCO2, pH, HCO3, SaO2.",
    "PaO2":  "Partial pressure of O2 in arterial blood. Normal 80–100 mmHg.",
    "PaCO2": "Partial pressure of CO2 in arterial blood. Normal 35–45 mmHg.",
    "pH":    "Hydrogen ion concentration. Normal blood pH 7.35–7.45.",
    # ── Labs — endocrine/other ───────────────────────────────────────────────
    "HbA1c": "Glycated Hemoglobin — reflects ~3-month glucose average. Diabetes ≥6.5%.",
    "TSH":   "Thyroid-Stimulating Hormone. Normal 0.4–4.0 mIU/L.",
    "T3":    "Triiodothyronine — active thyroid hormone. Normal free T3 2.3–4.1 pg/mL.",
    "T4":    "Thyroxine — predominant thyroid hormone. Normal free T4 0.8–1.8 ng/dL.",
    "PTH":   "Parathyroid Hormone — calcium regulator. Normal 15–65 pg/mL.",
    "ADH":   "Antidiuretic Hormone (Vasopressin) — water reabsorption in collecting duct.",
    "ACTH":  "Adrenocorticotropic Hormone — drives cortisol from adrenal cortex.",
    "GH":    "Growth Hormone — anabolic hormone from anterior pituitary.",
    "LH":    "Luteinizing Hormone — triggers ovulation / testosterone synthesis.",
    "FSH":   "Follicle-Stimulating Hormone — follicle development / spermatogenesis.",
    "PRL":   "Prolactin — promotes lactation. Elevated in prolactinoma.",
    "CD4":   "CD4+ T-lymphocyte count — immune function in HIV. Normal >500/µL.",
    # ── Labs — liver/lipids ──────────────────────────────────────────────────
    "LFT":   "Liver Function Tests — ALT, AST, ALP, GGT, bilirubin, albumin.",
    "AST":   "Aspartate Aminotransferase. Normal 10–40 U/L. Elevated in liver/muscle injury.",
    "ALT":   "Alanine Aminotransferase — liver-specific. Normal 7–56 U/L.",
    "ALP":   "Alkaline Phosphatase — liver/bone. Normal 44–147 U/L.",
    "GGT":   "Gamma-Glutamyltransferase — sensitive to alcohol. Normal 8–61 U/L.",
    "LDL":   "Low-Density Lipoprotein. Target <70 mg/dL (high CV risk).",
    "HDL":   "High-Density Lipoprotein. Protective; target >60 mg/dL.",
    "TG":    "Triglycerides. Normal <150 mg/dL.",
    "PSA":   "Prostate-Specific Antigen — prostate cancer screening marker.",
    "CRP":   "C-Reactive Protein — acute phase reactant, inflammation marker.",
    "ESR":   "Erythrocyte Sedimentation Rate — non-specific inflammation marker.",
    "ANA":   "Antinuclear Antibody — screen for SLE and other autoimmune diseases.",
    "RF":    "Rheumatoid Factor — IgM vs Fc of IgG; elevated in RA.",
    # ── Cardiovascular ───────────────────────────────────────────────────────
    "MI":    "Myocardial Infarction — cardiac muscle death from occluded coronary artery.",
    "HTN":   "Hypertension — persistent BP ≥130/80 mmHg.",
    "CAD":   "Coronary Artery Disease — atherosclerotic coronary narrowing.",
    "CHF":   "Congestive Heart Failure — inadequate cardiac output ± fluid congestion.",
    "HF":    "Heart Failure — cardiac output insufficient for metabolic demands.",
    "ACS":   "Acute Coronary Syndrome — spectrum of UA, NSTEMI, STEMI.",
    "STEMI": "ST-Elevation MI — full-thickness MI; ST elevation on ECG; emergent reperfusion.",
    "NSTEMI":"Non-ST-Elevation MI — partial-thickness MI without ST elevation.",
    "AF":    "Atrial Fibrillation — disorganised atrial activity; irregularly irregular rhythm.",
    "AFib":  "Atrial Fibrillation (see AF).",
    "DVT":   "Deep Vein Thrombosis — thrombus in deep vein, usually lower limb.",
    "PE":    "Pulmonary Embolism — obstruction of pulmonary arteries by thrombus.",
    "VTE":   "Venous Thromboembolism — DVT and/or PE.",
    "CABG":  "Coronary Artery Bypass Grafting — surgical coronary revascularization.",
    "PCI":   "Percutaneous Coronary Intervention — catheter-based coronary revascularization.",
    "EF":    "Ejection Fraction — % of blood ejected per beat. Normal ≥55%.",
    "CO":    "Cardiac Output = HR × SV. Normal 4–8 L/min. Also: Carbon Monoxide.",
    "SVR":   "Systemic Vascular Resistance — LV afterload.",
    "PAD":   "Peripheral Artery Disease — atherosclerosis of non-coronary arteries.",
    "ABI":   "Ankle-Brachial Index — PAD screen. Normal 0.9–1.3; <0.9 = PAD.",
    "AAA":   "Abdominal Aortic Aneurysm. Repair when ≥5.5 cm; rupture is fatal.",
    "VSD":   "Ventricular Septal Defect — congenital hole between ventricles.",
    "ASD":   "Atrial Septal Defect — congenital hole between atria.",
    "PDA":   "Patent Ductus Arteriosus — persistent fetal shunt; close with indomethacin.",
    "TOF":   "Tetralogy of Fallot — VSD, overriding aorta, pulmonary stenosis, RV hypertrophy.",
    "WPW":   "Wolff-Parkinson-White — accessory AV pathway; risk of SVT and VF.",
    "SVT":   "Supraventricular Tachycardia — rapid rhythm above the bundle of His.",
    "VT":    "Ventricular Tachycardia — rapid ventricular rhythm ≥3 beats.",
    "VF":    "Ventricular Fibrillation — chaotic ventricular rhythm; cardiac arrest.",
    "PVC":   "Premature Ventricular Contraction — ectopic ventricular beat.",
    "PAC":   "Premature Atrial Contraction — ectopic atrial beat.",
    "LBBB":  "Left Bundle Branch Block — delayed LV depolarization; wide QRS; notched R in V5/V6.",
    "RBBB":  "Right Bundle Branch Block — delayed RV depolarization; RSR' in V1.",
    "ICD":   "Implantable Cardioverter Defibrillator — detects VT/VF and delivers shock.",
    "PPM":   "Permanent Pacemaker.",
    "CRT":   "Cardiac Resynchronization Therapy — biventricular pacing for HF + LBBB.",
    "TAVR":  "Transcatheter Aortic Valve Replacement.",
    "IE":    "Infective Endocarditis — infection of cardiac valves/endocardium.",
    "MVP":   "Mitral Valve Prolapse — posterior billowing of mitral leaflet(s); mid-systolic click.",
    "AV":    "Atrioventricular — junction between atria and ventricles.",
    "SA":    "Sinoatrial (node) — primary cardiac pacemaker (60–100 bpm).",
    # ── Pulmonary ────────────────────────────────────────────────────────────
    "COPD":  "Chronic Obstructive Pulmonary Disease — emphysema + chronic bronchitis; FEV1/FVC <0.70.",
    "SOB":   "Shortness of Breath (Dyspnea).",
    "PFT":   "Pulmonary Function Tests — spirometry, lung volumes, DLCO.",
    "FEV1":  "Forced Expiratory Volume in 1 second — obstructive disease marker.",
    "FVC":   "Forced Vital Capacity. FEV1/FVC <0.70 = obstruction.",
    "DLCO":  "Diffusing Capacity of Lung for CO — gas transfer. Reduced in emphysema/fibrosis.",
    "ARDS":  "Acute Respiratory Distress Syndrome — diffuse lung injury; P/F <300 (mild), <200 (mod), <100 (severe).",
    "IPF":   "Idiopathic Pulmonary Fibrosis — progressive honeycombing; median survival 3–5 yr.",
    "OSA":   "Obstructive Sleep Apnea — upper airway collapse; treated with CPAP.",
    "CPAP":  "Continuous Positive Airway Pressure — first-line OSA treatment.",
    # ── Neurology ────────────────────────────────────────────────────────────
    "CVA":   "Cerebrovascular Accident (Stroke) — sudden neurological deficit from vascular cause.",
    "TIA":   "Transient Ischemic Attack — neurological symptoms <24 h; no infarction on MRI.",
    "GCS":   "Glasgow Coma Scale — eye (4) + verbal (5) + motor (6) = 3–15. ≤8 = severe injury.",
    "LOC":   "Loss of Consciousness.",
    "AMS":   "Altered Mental Status.",
    "ICP":   "Intracranial Pressure. Normal <15 mmHg; treat >20 mmHg.",
    "LP":    "Lumbar Puncture — CSF sampling at L3/L4.",
    "CSF":   "Cerebrospinal Fluid — cushions CNS; sampled by LP.",
    "EEG":   "Electroencephalogram — brain electrical activity; used for seizure diagnosis.",
    "ALS":   "Amyotrophic Lateral Sclerosis — UMN + LMN degeneration; progressive paralysis.",
    "PD":    "Parkinson's Disease — dopaminergic nigrostriatal loss; tremor, rigidity, bradykinesia.",
    "AD":    "Alzheimer's Disease — most common dementia; amyloid + tau pathology.",
    # ── Endocrine ────────────────────────────────────────────────────────────
    "DM":    "Diabetes Mellitus — chronic impaired glucose regulation.",
    "DKA":   "Diabetic Ketoacidosis — DM1 emergency: hyperglycemia + ketoacidosis + dehydration.",
    "HHS":   "Hyperosmolar Hyperglycemic State — DM2 emergency: extreme hyperglycemia, no ketosis.",
    "SIADH": "Syndrome of Inappropriate ADH — hyponatremia from excess ADH despite low osmolality.",
    "DI":    "Diabetes Insipidus — polyuria from ADH deficiency (central) or resistance (nephrogenic).",
    "CAH":   "Congenital Adrenal Hyperplasia — 21-hydroxylase deficiency most common.",
    "MEN":   "Multiple Endocrine Neoplasia — hereditary endocrine tumor syndrome (1, 2A, 2B).",
    "PCOS":  "Polycystic Ovary Syndrome — anovulation, hyperandrogenism, polycystic ovaries.",
    # ── Renal ────────────────────────────────────────────────────────────────
    "CKD":   "Chronic Kidney Disease — eGFR <60 for >3 months. Staged G1–G5.",
    "AKI":   "Acute Kidney Injury — Cr rise ≥0.3 mg/dL or ≥50% from baseline within 48 h.",
    "ESRD":  "End-Stage Renal Disease — eGFR <15; requires dialysis or transplant.",
    "FSGS":  "Focal Segmental Glomerulosclerosis — nephrotic syndrome; podocyte injury.",
    "GN":    "Glomerulonephritis — immune-mediated glomerular inflammation.",
    "UTI":   "Urinary Tract Infection.",
    # ── GI & Hepatology ──────────────────────────────────────────────────────
    "GERD":  "Gastroesophageal Reflux Disease — LES incompetence; heartburn.",
    "IBD":   "Inflammatory Bowel Disease — Crohn's disease or ulcerative colitis.",
    "UC":    "Ulcerative Colitis — mucosal inflammation from rectum proximally.",
    "PUD":   "Peptic Ulcer Disease — gastric/duodenal ulcers; H. pylori or NSAIDs.",
    "HCC":   "Hepatocellular Carcinoma — primary liver cancer; complication of cirrhosis.",
    "NAFLD": "Non-Alcoholic Fatty Liver Disease — hepatic steatosis without excess alcohol.",
    "NASH":  "Non-Alcoholic Steatohepatitis — NAFLD with hepatic inflammation.",
    "GI":    "Gastrointestinal.",
    "FOB":   "Fecal Occult Blood.",
    "DRE":   "Digital Rectal Exam.",
    # ── Rheumatology ─────────────────────────────────────────────────────────
    "RA":    "Rheumatoid Arthritis — symmetric erosive polyarthritis; anti-CCP positive.",
    "SLE":   "Systemic Lupus Erythematosus — multisystem autoimmune; malar rash, ANA positive.",
    "OA":    "Osteoarthritis — degenerative cartilage loss, especially weight-bearing joints.",
    "PsA":   "Psoriatic Arthritis — seronegative inflammatory arthritis + psoriasis.",
    "PMR":   "Polymyalgia Rheumatica — proximal girdle pain in >50 yo; dramatic steroid response.",
    "GCA":   "Giant Cell Arteritis — large vessel vasculitis; blindness risk; jaw claudication.",
    "JIA":   "Juvenile Idiopathic Arthritis — chronic childhood inflammatory arthritis.",
    "SJS":   "Stevens-Johnson Syndrome — mucocutaneous drug reaction; <10% BSA involvement.",
    "TEN":   "Toxic Epidermal Necrolysis — severe SJS; >30% BSA skin detachment; high mortality.",
    # ── Oncology ─────────────────────────────────────────────────────────────
    "CLL":   "Chronic Lymphocytic Leukemia — mature B-cell malignancy; most common adult leukemia.",
    "CML":   "Chronic Myeloid Leukemia — BCR-ABL1 / Philadelphia chromosome; imatinib is first-line.",
    "ALL":   "Acute Lymphoblastic Leukemia — most common childhood malignancy.",
    "AML":   "Acute Myeloid Leukemia — most common acute leukemia in adults.",
    "NHL":   "Non-Hodgkin Lymphoma — heterogeneous group of lymphoid malignancies.",
    "MM":    "Multiple Myeloma — plasma cell malignancy; CRAB criteria.",
    "CRAB":  "Calcium↑, Renal failure, Anemia, Bone lesions — myeloma diagnostic criteria.",
    "HER2":  "Human Epidermal growth factor Receptor 2 — oncogene amplified in breast/gastric cancer.",
    "BRCA":  "Breast Cancer gene — BRCA1/2 mutations ↑ risk of breast, ovarian, and other cancers.",
    # ── Infectious disease ───────────────────────────────────────────────────
    "HIV":   "Human Immunodeficiency Virus — retrovirus causing AIDS.",
    "AIDS":  "Acquired Immunodeficiency Syndrome — HIV with CD4 <200/µL or AIDS-defining illness.",
    "ART":   "Antiretroviral Therapy — combination HIV treatment.",
    "TB":    "Tuberculosis — Mycobacterium tuberculosis; primary pulmonary infection.",
    "MRSA":  "Methicillin-Resistant Staphylococcus aureus — hospital and community pathogen.",
    "VRE":   "Vancomycin-Resistant Enterococcus.",
    "PJP":   "Pneumocystis jirovecii Pneumonia — opportunistic lung infection (formerly PCP).",
    "CMV":   "Cytomegalovirus — dangerous in transplant recipients and HIV patients.",
    "EBV":   "Epstein-Barr Virus — causes infectious mononucleosis; EBV-associated malignancies.",
    "HSV":   "Herpes Simplex Virus — HSV-1 (oral/CNS), HSV-2 (genital).",
    "VZV":   "Varicella-Zoster Virus — chickenpox (1°) and shingles (reactivation).",
    "RSV":   "Respiratory Syncytial Virus — leading bronchiolitis cause in infants.",
    "STI":   "Sexually Transmitted Infection.",
    "SIRS":  "Systemic Inflammatory Response Syndrome — 2+ of: temp, HR, RR, WBC criteria.",
    # ── Pharmacology ─────────────────────────────────────────────────────────
    "NSAID": "Non-Steroidal Anti-Inflammatory Drug — COX inhibitor; analgesic, antipyretic.",
    "PPI":   "Proton Pump Inhibitor — H⁺/K⁺-ATPase inhibitor; reduces gastric acid.",
    "ACE":   "Angiotensin-Converting Enzyme inhibitor — blocks Ang I→Ang II; reduces afterload.",
    "ARB":   "Angiotensin Receptor Blocker — blocks AT1 receptor; alternative to ACEi.",
    "BB":    "Beta-Blocker — blocks β-adrenergic receptors; ↓HR, ↓BP, anti-arrhythmic.",
    "CCB":   "Calcium Channel Blocker — DHP (amlodipine: vascular) vs non-DHP (rate control).",
    "SSRI":  "Selective Serotonin Reuptake Inhibitor — first-line for depression/anxiety.",
    "SNRI":  "Serotonin-Norepinephrine Reuptake Inhibitor — antidepressant.",
    "TCA":   "Tricyclic Antidepressant — older antidepressant; anticholinergic, cardiac toxicity.",
    "MAOI":  "Monoamine Oxidase Inhibitor — avoid tyramine (hypertensive crisis).",
    "BZD":   "Benzodiazepine — GABA-A positive allosteric modulator; sedative/anxiolytic.",
    "LMWH":  "Low Molecular Weight Heparin (enoxaparin) — subcutaneous anticoagulant.",
    "UFH":   "Unfractionated Heparin — IV anticoagulant; monitored by aPTT.",
    "NOAC":  "Non-Vitamin K Oral Anticoagulant (rivaroxaban, apixaban, dabigatran, edoxaban).",
    "DOAC":  "Direct Oral Anticoagulant — same class as NOAC.",
    "ASA":   "Aspirin (Acetylsalicylic acid) — antiplatelet, analgesic, antipyretic.",
    "tPA":   "Tissue Plasminogen Activator — thrombolytic; used in STEMI and ischemic stroke.",
    "GLP1":  "Glucagon-Like Peptide-1 receptor agonist — incretin mimetic; DM2 + weight loss.",
    "SGLT2": "Sodium-Glucose Cotransporter 2 inhibitor — reduces glucosuria; cardioprotective.",
    "DPP4":  "Dipeptidyl Peptidase-4 inhibitor (gliptin) — increases incretin activity in DM2.",
    "DMARDs":"Disease-Modifying Antirheumatic Drugs — slow RA progression (MTX, biologics).",
    "MTX":   "Methotrexate — folate antagonist; used in RA, psoriasis, cancer, ectopic.",
    # ── Procedures & settings ────────────────────────────────────────────────
    "ICU":   "Intensive Care Unit.",
    "NICU":  "Neonatal Intensive Care Unit.",
    "PICU":  "Pediatric Intensive Care Unit.",
    "ED":    "Emergency Department.",
    "PACU":  "Post-Anesthesia Care Unit.",
    "ETT":   "Endotracheal Tube — placed for mechanical ventilation.",
    "LMA":   "Laryngeal Mask Airway — supraglottic airway device.",
    "RSI":   "Rapid Sequence Intubation — induction + paralytic for emergency intubation.",
    "CVC":   "Central Venous Catheter.",
    "PICC":  "Peripherally Inserted Central Catheter.",
    "NGT":   "Nasogastric Tube.",
    "NPO":   "Nil Per Os — nothing by mouth.",
    # ── Imaging & diagnostics ────────────────────────────────────────────────
    "MRI":   "Magnetic Resonance Imaging.",
    "CT":    "Computed Tomography.",
    "CXR":   "Chest X-Ray.",
    "ECG":   "Electrocardiogram — records cardiac electrical activity (also EKG).",
    "EKG":   "Electrocardiogram (from German Elektrokardiogramm).",
    "Echo":  "Echocardiogram — cardiac ultrasound; assesses structure and function.",
    "DXA":   "Dual-energy X-ray Absorptiometry — bone density measurement for osteoporosis.",
    # ── Dosing ───────────────────────────────────────────────────────────────
    "PRN":  "Pro Re Nata — as needed.",
    "QD":   "Once daily.",
    "BID":  "Twice daily.",
    "TID":  "Three times daily.",
    "QID":  "Four times daily.",
    "QHS":  "Every bedtime.",
    "IV":   "Intravenous.",
    "IM":   "Intramuscular.",
    "SC":   "Subcutaneous.",
    "SL":   "Sublingual.",
    "PO":   "Per Os — by mouth.",
    # ── History & exam ───────────────────────────────────────────────────────
    "Hx":   "History — clinical history.",
    "Dx":   "Diagnosis.",
    "Tx":   "Treatment or Therapy.",
    "Rx":   "Prescription or Treatment.",
    "Sx":   "Symptoms.",
    "PMH":  "Past Medical History.",
    "FH":   "Family History.",
    "SH":   "Social History.",
    "CC":   "Chief Complaint.",
    "HPI":  "History of Present Illness.",
    "ROS":  "Review of Systems.",
    "SOAP": "Subjective, Objective, Assessment, Plan — clinical note format.",
    "SBAR": "Situation, Background, Assessment, Recommendation — handoff communication tool.",
    # ── Obstetrics ───────────────────────────────────────────────────────────
    "LMP":  "Last Menstrual Period.",
    "EDD":  "Estimated Date of Delivery — 40 weeks from LMP.",
    "GDM":  "Gestational Diabetes Mellitus.",
    "PPH":  "Postpartum Hemorrhage — >500 mL (vaginal) or >1000 mL (C-section).",
    "PROM": "Premature Rupture of Membranes.",
    "PPROM":"Preterm Premature Rupture of Membranes — before 37 weeks.",
    "HELLP":"Hemolysis, Elevated Liver enzymes, Low Platelets — severe preeclampsia variant.",
    "APGAR":"Appearance, Pulse, Grimace, Activity, Respiration — neonatal score 0–10.",
    # ── Stats & EBM ──────────────────────────────────────────────────────────
    "RCT":  "Randomized Controlled Trial — gold standard for causality.",
    "NNT":  "Number Needed to Treat = 1/ARR.",
    "NNH":  "Number Needed to Harm.",
    "ARR":  "Absolute Risk Reduction — control rate minus treatment rate.",
    "RRR":  "Relative Risk Reduction = 1 − RR.",
    "OR":   "Odds Ratio (stats). Also: Operating Room.",
    "PPV":  "Positive Predictive Value — P(disease | positive test).",
    "NPV":  "Negative Predictive Value — P(no disease | negative test).",
    "BMI":  "Body Mass Index = weight(kg) / height(m²). Obese ≥30.",
    "BSA":  "Body Surface Area — used for chemotherapy dosing.",
    "DNR":  "Do Not Resuscitate.",
    "DNI":  "Do Not Intubate.",
    "EHR":  "Electronic Health Record.",
}


def _lookup_abbreviation(phrase):
    """Exact abbreviation match (case-sensitive first, then upper-case)."""
    word = phrase.strip()
    return _ABBREVS.get(word) or _ABBREVS.get(word.upper()) or ""
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
    "anuric": "anuria", "oliguric": "oliguria",
    "cholecystitic": "cholecystitis", "pancreatitic": "pancreatitis",
    "diverticulitic": "diverticulitis", "appendicitic": "appendicitis",
    "pericarditic": "pericarditis", "endocarditic": "endocarditis",
    "myocarditic": "myocarditis", "aortic": "aorta",
    "splenic": "spleen", "hepatic": "liver", "renal": "kidney",
    "pulmonary": "lung", "cerebral": "cerebrum", "cerebellar": "cerebellum",
    "thyroidal": "thyroid", "adrenal": "adrenal gland",
    "pancreatic": "pancreas", "gastric": "stomach", "colonic": "colon",
    "dysphasic": "dysphasia", "dysarthric": "dysarthria",
    "febrile": "fever", "afebrile": "afebrile state",
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


def _cache_key(phrase: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", phrase.lower().strip())


def _cache_get(phrase):
    return _cache.get(_cache_key(phrase))   # (defn, src_label, sem_type)


def _cache_set(phrase, defn, src, sem_type=""):
    _cache[_cache_key(phrase)] = (defn, src, sem_type)

# ─────────────────────────────────────────────────────────────────────────────
# 6 · Hover injection JavaScript
#     Changes vs v6: digit-aware WORD_RE, ICD-10 green highlight,
#     badge param in mqrUpdate, min-length bypass for all-caps abbreviations.
# ─────────────────────────────────────────────────────────────────────────────

_HOVER_JS = r"""
(function() {
    'use strict';
    const cardRoot = document.getElementById('qa')
                  || document.querySelector('.card')
                  || document.body;
    if (!cardRoot || cardRoot.textContent.trim().length < 2) {
        pycmd('mqr:__retry__');
        return;
    }
    const DELAY   = HOVER_DELAY_MS;
    const MIN_LEN = MIN_WORD_LEN;
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
    }
    tip.style.cssText = `
        position: fixed !important;
        background: #0d1b2a;
        color: #d0daea;
        border: 1px solid #2a3f5f;
        border-radius: 10px;
        padding: 11px 15px;
        max-width: 340px;
        min-width: 200px;
        font-size: 12.5px;
        line-height: 1.65;
        z-index: 2147483647;
        display: none;
        box-shadow: 0 10px 36px rgba(0,0,0,0.75);
        pointer-events: none;
        font-family: 'SF Pro Text','Segoe UI','Helvetica Neue',sans-serif;
    `;

    // Matches: digits-in-words (HbA1c, SpO2), all-caps abbreviations,
    // normal words, and ICD-10 codes (E11.9, J18.0)
    const WORD_RE   = /([A-Z]\d{2}(?:\.\d{1,4})?(?=[^A-Za-z0-9]|$)|[A-Za-z][A-Za-z0-9''\-]*[A-Za-z0-9]|[A-Za-z]{2,})/g;
    const ICD10_RE  = /^[A-Z]\d{2}(?:\.\d{1,4})?$/;
    const ALLCAPS_RE = /^[A-Z]{2,}[0-9]*$/;
    const SKIP_TAGS = new Set(['SCRIPT','STYLE','INPUT','TEXTAREA',
                                'SELECT','BUTTON','A','CODE','PRE','SVG']);
    const allSpans  = [];

    function wrapTextNode(node) {
        const text = node.textContent;
        let lastIdx = 0, m, frag = document.createDocumentFragment(), changed = false;
        WORD_RE.lastIndex = 0;
        while ((m = WORD_RE.exec(text)) !== null) {
            const w = m[0];
            const isIcd   = ICD10_RE.test(w);
            const isCaps  = ALLCAPS_RE.test(w);
            if (w.length < MIN_LEN && !isIcd && !isCaps) continue;
            if (m.index > lastIdx)
                frag.appendChild(document.createTextNode(text.slice(lastIdx, m.index)));
            const sp = document.createElement('span');
            sp.className = CLS;
            sp.textContent = w;
            sp.dataset.w   = w;
            sp.style.cursor = 'default';
            if (isIcd) {
                sp.style.borderBottom = '1px dotted #7aaf7a';
                sp.style.color        = '#b0e8b0';
            }
            frag.appendChild(sp);
            allSpans.push(sp);
            lastIdx = WORD_RE.lastIndex;
            changed = true;
        }
        if (!changed) return;
        if (lastIdx < text.length)
            frag.appendChild(document.createTextNode(text.slice(lastIdx)));
        node.parentNode.replaceChild(frag, node);
    }

    function walkDOM(node) {
        if (node.nodeType === 3) { if (node.textContent.trim()) wrapTextNode(node); return; }
        if (node.nodeType !== 1 || SKIP_TAGS.has(node.tagName)) return;
        if (node.classList && node.classList.contains(CLS)) return;
        Array.from(node.childNodes).forEach(walkDOM);
    }
    walkDOM(cardRoot);
    allSpans.forEach((sp, i) => { sp.dataset.idx = i; });

    function getSentence(idx) {
        const start = Math.max(0, idx - 10);
        const end   = Math.min(allSpans.length - 1, idx + 10);
        return Array.from({length: end - start + 1}, (_, i) => allSpans[start+i].textContent).join(' ');
    }

    let timer = null;

    function positionTip(x, y) {
        const tw = 350, th = 160;
        tip.style.left = Math.min(x + 14, window.innerWidth  - tw - 8) + 'px';
        tip.style.top  = Math.min(y + 20, window.innerHeight - th - 8) + 'px';
    }

    function hideTip() { tip.style.display = 'none'; tip.innerHTML = ''; }

    document.querySelectorAll('.' + CLS).forEach(sp => {
        sp.addEventListener('mouseenter', function(e) {
            clearTimeout(timer);
            const idx  = parseInt(this.dataset.idx);
            const word = this.dataset.w;
            const x = e.clientX, y = e.clientY;
            timer = setTimeout(() => {
                tip.innerHTML = '<span style="color:#7a9fd4;font-style:italic">Looking up…</span>';
                tip.style.display = 'block';
                positionTip(x, y);
                const prev  = idx > 0                    ? allSpans[idx-1].dataset.w : '';
                const next  = idx < allSpans.length - 1 ? allSpans[idx+1].dataset.w : '';
                const prev2 = idx > 1                    ? allSpans[idx-2].dataset.w : '';
                const next2 = idx < allSpans.length - 2 ? allSpans[idx+2].dataset.w : '';
                const candidates = [];
                if (prev2 && prev) candidates.push(prev2+' '+prev+' '+word);
                if (prev  && next) candidates.push(prev +' '+word+' '+next);
                if (next  && next2) candidates.push(word+' '+next+' '+next2);
                if (prev)  candidates.push(prev +' '+ word);
                if (next)  candidates.push(word +' '+ next);
                candidates.push(word);
                const sentence = getSentence(idx);
                pycmd('mqr:' + JSON.stringify({candidates, sentence}));
            }, DELAY);
        });
        sp.addEventListener('mousemove', function(e) {
            if (tip.style.display === 'block') positionTip(e.clientX, e.clientY);
        });
        sp.addEventListener('mouseleave', function() {
            clearTimeout(timer);
            setTimeout(hideTip, 200);
        });
    });

    // badge: optional short category string, e.g. "Disease" / "Drug" / "Abbrev"
    window.mqrUpdate = function(phrase, defn, srcHtml, badge) {
        if (tip.style.display === 'none') return;
        const badgeHtml = badge
            ? `<span style="font-size:10px;padding:1px 7px;border-radius:10px;
               background:#1a3d5c;color:#7aafe8;font-weight:600;
               margin-left:7px;vertical-align:middle;letter-spacing:0.3px">${badge}</span>`
            : '';
        tip.innerHTML =
            `<div style="font-weight:700;font-size:13px;color:#7aaee8;
             margin-bottom:6px;border-bottom:1px solid #1e3a5a;padding-bottom:5px;">`
            + phrase + badgeHtml + '</div>'
            + `<div style="color:#c8d8ea;font-size:12.5px">${defn}</div>`
            + (srcHtml
                ? `<div style="font-size:10px;color:#4a6a8e;margin-top:6px;
                   border-top:1px solid #1e3a5a;padding-top:5px;">${srcHtml}</div>`
                : '');
    };
    window.mqrNotFound = function() { hideTip(); };
})();
""".replace("HOVER_DELAY_MS", str(CFG["hover_delay_ms"])) \
   .replace("MIN_WORD_LEN",   str(CFG["min_word_len"]))

# ─────────────────────────────────────────────────────────────────────────────
# 7 · DOM-ready injection with retry
# ─────────────────────────────────────────────────────────────────────────────

def _inject_with_retry():
    if mw.reviewer and mw.reviewer.web:
        mw.reviewer.web.eval(_HOVER_JS)


def _schedule_inject():
    QTimer.singleShot(CFG["inject_initial_delay_ms"], _inject_with_retry)

# ─────────────────────────────────────────────────────────────────────────────
# 8 · UMLS REST API  (TGT / CAS authentication)
# ─────────────────────────────────────────────────────────────────────────────

_umls_tgt_url    = None
_umls_tgt_expiry = 0.0   # unix timestamp


def _umls_get_tgt():
    """Obtain or re-use a TGT from the UMLS CAS service. Returns URL or None."""
    global _umls_tgt_url, _umls_tgt_expiry
    api_key = CFG.get("umls_api_key", "").strip()
    if not api_key:
        return None
    now = time.time()
    if _umls_tgt_url and now < _umls_tgt_expiry:
        return _umls_tgt_url
    try:
        data = urllib.parse.urlencode({"apikey": api_key}).encode()
        req  = urllib.request.Request(
            "https://utslogin.nlm.nih.gov/cas/v1/api-key",
            data=data,
            headers={"User-Agent": "AnkiMedQuickRef/7.0",
                     "Content-Type": "application/x-www-form-urlencoded"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode("utf-8", errors="replace")
        m = re.search(r'action="(https://[^"]+)"', body)
        if m:
            _umls_tgt_url    = m.group(1)
            _umls_tgt_expiry = now + 7 * 3600   # TGT lasts 8 h; refresh after 7
            return _umls_tgt_url
    except Exception:
        pass
    return None


def _umls_get_ticket():
    """Get a single-use service ticket from the TGT. Returns ticket string or None."""
    tgt_url = _umls_get_tgt()
    if not tgt_url:
        return None
    try:
        data = urllib.parse.urlencode(
            {"service": "http://umlsks.nlm.nih.gov"}
        ).encode()
        req = urllib.request.Request(
            tgt_url, data=data,
            headers={"User-Agent": "AnkiMedQuickRef/7.0",
                     "Content-Type": "application/x-www-form-urlencoded"},
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            return resp.read().decode("utf-8").strip()
    except Exception:
        global _umls_tgt_url, _umls_tgt_expiry
        _umls_tgt_url = None   # force re-auth on next call
        _umls_tgt_expiry = 0.0
        return None

# ─────────────────────────────────────────────────────────────────────────────
# 9 · API lookups
# ─────────────────────────────────────────────────────────────────────────────

_HEADERS = {"User-Agent": "AnkiMedQuickRef/7.0"}

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
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None


# ── UMLS REST API ─────────────────────────────────────────────────────────────

_UMLS_DEF_PRIORITY = {
    "MSH": 1, "NCI": 2, "CSP": 3, "HPO": 4,
    "SNOMEDCT_US": 5, "RXNORM": 6, "GO": 7,
}


def _lookup_umls_api(phrase):
    """Search UMLS REST API for phrase.  Returns (defn, url, sem_type) or ('','','')."""
    ticket = _umls_get_ticket()
    if not ticket:
        return "", "", ""
    q = urllib.parse.quote(phrase)
    data = _get_json(
        f"https://uts-ws.nlm.nih.gov/rest/search/current"
        f"?string={q}&searchType=exact&returnIdType=concept&ticket={ticket}"
    )
    if not data:
        return "", "", ""
    results = (data.get("result") or {}).get("results", [])
    if not results or results[0].get("ui") in ("NONE", None, ""):
        return "", "", ""

    cui      = results[0]["ui"]
    cui_name = results[0].get("name", phrase)

    # Get semantic type
    ticket2 = _umls_get_ticket()
    sem_type = ""
    if ticket2:
        sem_data = _get_json(
            f"https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{cui}"
            f"/semanticTypes?ticket={ticket2}"
        )
        if sem_data and sem_data.get("result"):
            sem_type = sem_data["result"][0].get("name", "")

    # Get definitions
    ticket3 = _umls_get_ticket()
    if not ticket3:
        return "", f"https://uts.nlm.nih.gov/uts/umls/concept/{cui}", sem_type

    def_data = _get_json(
        f"https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{cui}"
        f"/definitions?ticket={ticket3}"
    )
    if def_data and def_data.get("result"):
        best_defn, best_pri = "", 999
        for d in def_data["result"]:
            pri = _UMLS_DEF_PRIORITY.get(d.get("rootSource", ""), 50)
            if pri < best_pri:
                best_defn = d.get("value", "")
                best_pri  = pri
        if best_defn:
            return (best_defn[:CFG["tooltip_max_chars"]],
                    f"https://uts.nlm.nih.gov/uts/umls/concept/{cui}",
                    sem_type)

    return "", f"https://uts.nlm.nih.gov/uts/umls/concept/{cui}", sem_type


# ── RxNorm drug identification ────────────────────────────────────────────────

def _lookup_rxnorm(phrase):
    """Returns (definition, url) or ('', ''). No API key needed."""
    q    = urllib.parse.quote(phrase)
    data = _get_json(f"https://rxnav.nlm.nih.gov/REST/drugs.json?name={q}")
    if not data:
        return "", ""
    groups = (data.get("drugGroup") or {}).get("conceptGroup", [])
    ingredients, brands = [], []
    for grp in groups:
        tty = grp.get("tty", "")
        for prop in grp.get("conceptProperties", []):
            name  = prop.get("name", "")
            rxcui = prop.get("rxcui", "")
            if tty == "IN"  and name: ingredients.append((name, rxcui))
            elif tty == "BN" and name: brands.append(name)
    if not ingredients and not brands:
        return "", ""
    if ingredients:
        name, rxcui = ingredients[0]
        brand_str   = f" · Brands: {', '.join(brands[:3])}" if brands else ""
        defn = f"Drug (ingredient: {name}{brand_str})."
        return defn, f"https://mor.nlm.nih.gov/RxNav/search?searchBy=RXCUI&searchTerm={rxcui}"
    return "Prescription drug (brand name).", ""


# ── NLM MedlinePlus ───────────────────────────────────────────────────────────

def _lookup_medlineplus(phrase):
    q    = urllib.parse.quote(phrase)
    data = _get_json(
        f"https://connect.nlm.nih.gov/v1/query?terms={q}&responseType=json"
    )
    if not data:
        return "", ""
    docs = (data.get("nlmSearchResult", {}).get("list", {}).get("document", []))
    for doc in docs[:3]:
        for item in doc.get("content", []):
            if item.get("name") in ("FullSummary", "snippet"):
                raw   = item.get("value", "")
                clean = re.sub(r"<[^>]+>", "", raw).strip()
                if len(clean) > 60:
                    return clean[:CFG["tooltip_max_chars"]], doc.get("url", "")
    return "", ""


# ── Wikipedia ─────────────────────────────────────────────────────────────────

def _lookup_wikipedia(phrase):
    NON_MED = ("in physics","in chemistry","in mathematics","in engineering",
               "in music","in computing","is a film","is a novel","is a song",
               "is an album","is a video game","is a television")
    def _fetch(slug):
        data = _get_json(
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + urllib.parse.quote(slug)
        )
        if data and data.get("extract") and data.get("type") != "disambiguation":
            ext = data["extract"]
            if not any(p in ext.lower() for p in NON_MED):
                url = ((data.get("content_urls") or {}).get("desktop", {}).get("page", ""))
                return ext[:CFG["tooltip_max_chars"]], url
        return "", ""
    base = phrase.replace(" ", "_")
    for suffix in ("_(medicine)","_(medical_condition)","_(disease)",
                   "_(anatomy)","_(pharmacology)",""):
        defn, url = _fetch(base + suffix)
        if defn:
            return defn, url
    return "", ""

# ─────────────────────────────────────────────────────────────────────────────
# 10 · Lookup orchestration — tiers 0–6
# ─────────────────────────────────────────────────────────────────────────────

def _lookup_candidates(candidates, sentence):
    """
    Try each candidate phrase using the tier waterfall.
    Returns (phrase, defn, url, src_label, badge).
    """
    single_word = candidates[-1] if candidates else ""

    # ── Tier 0: abbreviation dictionary (instant, offline) ───────────────────
    abbr_defn = _lookup_abbreviation(single_word)
    if abbr_defn:
        _cache_set(single_word, abbr_defn, "Abbrev", "Abbreviation")
        return single_word, abbr_defn, "", "Abbrev", "Abbrev"

    # ── Tier 1: in-memory cache ───────────────────────────────────────────────
    for phrase in candidates:
        hit = _cache_get(phrase)
        if hit:
            defn, src, sem_type = hit
            badge = _SEM_BADGE.get(sem_type, src.split()[0] if src else "")
            return phrase, defn, "", src + " ·cached", badge

    # ── Tier 2: local SQLite MeSH/UMLS database ───────────────────────────────
    for phrase in candidates:
        defn, sem_type = _lookup_local_db(phrase)
        if defn:
            badge = _SEM_BADGE.get(sem_type, "MeSH/UMLS")
            _cache_set(phrase, defn, "MeSH/UMLS", sem_type)
            return phrase, defn, "", "MeSH/UMLS", badge

    # ── Tier 2.5: local DB with morphological variants ───────────────────────────
    single = candidates[-1] if candidates else ""
    if single:
        for variant in _medical_variants(single):
            defn, sem_type = _lookup_local_db(variant)
            if defn:
                badge = _SEM_BADGE.get(sem_type, "MeSH/UMLS")
                _cache_set(single, defn, "MeSH/UMLS", sem_type)
                return variant, defn, "", "MeSH/UMLS", badge

    # ── Tiers 3-6 are network — filter common English words first ─────────────
    net_candidates = [
        p for p in candidates
        if not all(w in _COMMON_ENGLISH for w in p.lower().split())
    ]
    if not net_candidates:
        return "", "", "", "", ""

    # ── Tier 3: UMLS REST API ─────────────────────────────────────────────────
    if CFG.get("umls_api_key", "").strip():
        for phrase in net_candidates:
            defn, url, sem_type = _lookup_umls_api(phrase)
            if defn:
                badge = _SEM_BADGE.get(sem_type, "UMLS")
                _cache_set(phrase, defn, "UMLS API", sem_type)
                return phrase, defn, url, "UMLS", badge

    # ── Tier 4: RxNorm (drug identification) ──────────────────────────────────
    for phrase in net_candidates:
        defn, url = _lookup_rxnorm(phrase)
        if defn:
            _cache_set(phrase, defn, "RxNorm", "Pharmacologic Substance")
            return phrase, defn, url, "RxNorm", "Drug"

    # ── Tier 5: NLM MedlinePlus ───────────────────────────────────────────────
    for phrase in net_candidates:
        defn, url = _lookup_medlineplus(phrase)
        if defn:
            _cache_set(phrase, defn, "NLM MedlinePlus", "")
            return phrase, defn, url, "NLM MedlinePlus", ""

    # ── Tier 6: Wikipedia ─────────────────────────────────────────────────────
    for phrase in net_candidates:
        defn, url = _lookup_wikipedia(phrase)
        if defn:
            _cache_set(phrase, defn, "Wikipedia", "")
            return phrase, defn, url, "Wikipedia", ""

    return "", "", "", "", ""

# ─────────────────────────────────────────────────────────────────────────────
# 11 · JS message handler
# ─────────────────────────────────────────────────────────────────────────────

_retry_counts: dict = {}


def _on_js_message(handled, message, context):
    if not isinstance(context, Reviewer):
        return handled
    if not message.startswith("mqr:"):
        return handled

    payload_str = message[4:].strip()

    if payload_str == "__retry__":
        card_id = id(mw.reviewer.card) if (mw.reviewer and mw.reviewer.card) else 0
        attempt = _retry_counts.get(card_id, 0) + 1
        _retry_counts[card_id] = attempt
        if attempt <= CFG["inject_max_retries"]:
            delay = 60 * attempt
            mw.taskman.run_on_main(lambda: QTimer.singleShot(delay, _inject_with_retry))
        return (True, None)

    try:
        payload    = json.loads(payload_str)
        candidates = payload.get("candidates", [payload_str])
        sentence   = payload.get("sentence", "")
    except Exception:
        candidates = [payload_str]
        sentence   = ""

    if not candidates:
        return (True, None)

    def _worker():
        phrase, defn, url, src, badge = _lookup_candidates(candidates, sentence)

        def _push():
            web = mw.reviewer.web if mw.reviewer else None
            if not web:
                return
            if not defn:
                web.eval("if(window.mqrNotFound) mqrNotFound();")
                return
            src_html = (
                f'<a href="{url}" style="color:#5a9fd4">{src}</a>'
                if url else src
            )
            safe = lambda s: (
                s.replace("\\", "\\\\")
                 .replace("`", "\\`")
                 .replace("${", "\\${")
            )
            web.eval(
                f"if(window.mqrUpdate) mqrUpdate("
                f"`{safe(phrase)}`,`{safe(defn)}`,`{safe(src_html)}`,`{safe(badge)}`);"
            )

        mw.taskman.run_on_main(_push)

    threading.Thread(target=_worker, daemon=True).start()
    return (True, None)


gui_hooks.webview_did_receive_js_message.append(_on_js_message)

# ─────────────────────────────────────────────────────────────────────────────
# 12 · Card hooks
# ─────────────────────────────────────────────────────────────────────────────

def _on_question(reviewer):
    card    = mw.reviewer.card if mw.reviewer else None
    card_id = id(card) if card else 0
    _retry_counts[card_id] = 0
    _schedule_inject()


def _on_answer(card):
    _retry_counts[id(card)] = 0
    _schedule_inject()


gui_hooks.reviewer_did_show_question.append(_on_question)
gui_hooks.reviewer_did_show_answer.append(_on_answer)
