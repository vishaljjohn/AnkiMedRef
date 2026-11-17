"""Anatomy & physiology and alternate names (tier 0.5f).

Edit freely — see data/__init__.py for how files are loaded."""
from ..formatters import _af


_ANATOMY = {
    # ── Brachial Plexus ───────────────────────────────────────────────────
    "brachial plexus": _af(
        "Peripheral Nerve — C5–T1 roots (mnemonics: Roots Trunks Divisions Cords Branches = 'Randy Travis Drinks Cold Beer'; cords named for relation to axillary artery)",
        "Roots: C5, C6, C7, C8, T1. Trunks: Upper (C5–C6), Middle (C7), Lower (C8–T1). Each trunk → anterior + posterior divisions. Cords: Lateral (C5–C7 anterior), Posterior (all posterior divisions), Medial (C8–T1 anterior). Branches: Musculocutaneous (lateral cord — C5–C7), Axillary (posterior cord — C5–C6), Radial (posterior cord — C5–T1), Median (lateral + medial cords — C5–T1), Ulnar (medial cord — C8–T1)",
        "Erb's palsy (C5–C6 injury — shoulder dystocia/traction): 'waiter's tip' posture (shoulder adducted/internally rotated, elbow extended/pronated, wrist flexed). Klumpke palsy (C8–T1 — forceful arm abduction or Pancoast tumor): 'claw hand' + Horner syndrome (if T1 ramus communicans damaged — ptosis, miosis, anhidrosis, enophthalmos). Long thoracic nerve (C5–C7 — serratus anterior): 'winged scapula' after axillary lymph node dissection/mastectomy."
    ),
    # ── Cranial Nerves ────────────────────────────────────────────────────
    "cranial nerves": _af(
        "Peripheral Nerve — 12 pairs emerging from brain/brainstem (mnemonic: 'Oh Oh Oh To Touch And Feel Very Good Velvet — Ah Heaven' = CN I–XII)",
        "CN I (Olfactory — smell; cribriform plate). CN II (Optic — vision; optic canal). CN III (Oculomotor — most EOM + pupillary constriction + lens accommodation; parasympathetic). CN IV (Trochlear — superior oblique — 'down and in'; longest intracranial course). CN V (Trigeminal — face sensation V1/V2/V3 + muscles of mastication; herpes zoster → V1 ophthalmic division). CN VI (Abducens — lateral rectus — abduction). CN VII (Facial — muscles of facial expression + taste ant 2/3 tongue + lacrimation/salivation; stylomastoid foramen). CN VIII (Vestibulocochlear — hearing + balance). CN IX (Glossopharyngeal — taste post 1/3 tongue + carotid body/sinus + parotid gland; stylopharyngeus). CN X (Vagus — larynx/pharynx + parasympathetic viscera). CN XI (Accessory — trapezius + sternocleidomastoid). CN XII (Hypoglossal — tongue muscles — deviation TOWARD lesion)",
        "CN III palsy: 'down and out' (unopposed CN IV/VI) + ptosis + mydriasis (blown pupil — if compressive — PCom [posterior communicating artery] aneurysm). SURGICAL CN III (PCom aneurysm/uncal herniation): pupil INVOLVED (parasympathetics on outside of nerve → compressed first). MEDICAL CN III (DM, HTN): pupil SPARED (ischemia spares outer parasympathetic fibers). CN VII: Bell's palsy (LMN — entire ipsilateral face involved including forehead). CN VII UMN (stroke): contralateral lower face weakness, FOREHEAD SPARED (bilateral cortical representation of forehead)."
    ),
    "circle of willis": _af(
        "Vascular Anatomy — arterial anastomotic ring at base of brain (anterior + posterior circulation)",
        "Internal carotid arteries (ICAs) → Anterior Cerebral Arteries (ACAs) connected by anterior communicating artery (ACoA) — anterior circulation. Basilar artery (from vertebral arteries) → Posterior Cerebral Arteries (PCAs). PCAs connected to ICAs by posterior communicating arteries (PComAs). Components: ACA (bilateral) + ACoA (1) + ICA (bilateral) + PComA (bilateral) + PCA (bilateral) + basilar (1). Middle Cerebral Arteries (MCAs) — largest branches of ICA, largest territory — NOT part of circle itself",
        "Most common circle of Willis aneurysm: anterior communicating artery (ACoA — 30–35%) → rupture → SAH (thunderclap headache — 'worst headache of life'). Second most common: PCoA (20–25%) → CN III palsy (surgical, pupil-involved). Berry aneurysms (saccular) most common aneurysm type — associated with PKD, Marfan, connective tissue disorders. Watershed infarcts: between ACA/MCA and MCA/PCA territories — occur in severe hypotension/cardiac arrest (proximal limb weakness — 'man-in-a-barrel' syndrome)."
    ),
    "femoral triangle": _af(
        "Gross Anatomy — anterior thigh compartment bounded by inguinal ligament (superiorly), sartorius muscle (laterally), adductor longus muscle (medially). Floor: iliopsoas + pectineus",
        "Contents (lateral to medial = NAVEL): Nerve (femoral — lateral, outside femoral sheath), Artery (femoral — within femoral sheath), Vein (femoral — within femoral sheath), Empty space (lymphatics), Lymphatics (deep inguinal nodes). Femoral sheath (fascial tube) contains artery + vein + femoral canal (empty space medially — potential hernia orifice). Femoral nerve: L2–L4, lateral to sheath, NOT in sheath (NAVEL runs lateral → medial; read medial → lateral it is 'VAN')",
        "Femoral hernia: through femoral canal (medial compartment of femoral sheath) → BELOW and LATERAL to pubic tubercle. Inguinal hernia: ABOVE and MEDIAL to pubic tubercle. Femoral hernias more common in women (wider pelvis), higher strangulation risk (narrow neck). Femoral nerve injury (hip fracture/surgery → L2–L4): weak hip flexion + knee extension + ↓sensation anteromedial thigh + absent patellar reflex. Femoral vein catheterization: highest infection risk of central venous access sites."
    ),
    "inguinal canal": _af(
        "Gross Anatomy — oblique passageway in inguinal region (4 cm long in adults; runs from deep inguinal ring to superficial inguinal ring)",
        "Deep (internal) inguinal ring: defect in transversalis fascia, lateral to inferior epigastric vessels. Superficial (external) inguinal ring: defect in external oblique aponeurosis, above pubic tubercle. Roof: internal oblique + transversus abdominis (arching fibers). Floor: inguinal ligament + lacunar ligament. Anterior wall: external oblique aponeurosis + internal oblique (lateral). Posterior wall: transversalis fascia (lateral) + conjoint tendon — internal oblique + transversus abdominis (medial — reinforces area). Contents — male: spermatic cord (ductus deferens, testicular artery/pampiniform plexus, lymphatics, genital branch of genitofemoral nerve, cremasteric artery). Female: round ligament of uterus. Both: ilioinguinal nerve (runs in the canal but OUTSIDE the spermatic cord)",
        "Direct inguinal hernia: protrudes through Hesselbach's triangle (medial to inferior epigastric vessels, above inguinal ligament, lateral to rectus abdominis) — acquired weakness through posterior wall — does NOT pass through deep ring. Indirect inguinal hernia: passes through DEEP inguinal ring → inguinal canal → superficial ring (→ scrotum in males) — follows patent processus vaginalis — most common hernia (both sexes, especially males). Mnemonic 'MDs don't LIe': Medial to inferior epigastric vessels = Direct; Lateral = Indirect."
    ),
    "carpal tunnel": _af(
        "Peripheral Nerve Anatomy — fibro-osseous canal at wrist; floor/sides: carpal bones; roof: flexor retinaculum (transverse carpal ligament)",
        "Contents (10 structures): Flexor digitorum superficialis (4 tendons), Flexor digitorum profundus (4 tendons), Flexor pollicis longus (1 tendon), Median nerve (MOST VULNERABLE — compressive neuropathy). NOT in carpal tunnel: flexor carpi radialis (in own sheath), palmaris longus (superficial), ulnar nerve (Guyon's canal). Median nerve supplies: thumb, index, middle, radial half of ring finger (sensation); thenar muscles (opposition, flexion, abduction of thumb — LOAF: Lumbricals 1&2, Opponens pollicis, Abductor pollicis brevis, Flexor pollicis brevis)",
        "Carpal tunnel syndrome (CTS — most common peripheral compression neuropathy): tingling/numbness in median nerve distribution (thumb + index + middle + radial ring finger) + nocturnal symptoms + thenar wasting (late). Phalen test (wrist flexion 60 sec → reproduces symptoms) and Tinel sign (tapping over carpal tunnel → tingling). Risk factors: pregnancy, hypothyroidism, DM, rheumatoid arthritis, acromegaly, repetitive use, obesity. Treatment: wrist splinting (neutral, especially nocturnal) → corticosteroid injection → surgical carpal tunnel release."
    ),
    "spinal cord tracts": _af(
        "Neuroanatomy — major ascending (sensory) and descending (motor) pathways in spinal cord white matter",
        "ASCENDING (sensory): Dorsal columns (medial lemniscal pathway — ipsilateral: fine touch, vibration, proprioception → decussates in medulla → contralateral cortex). Spinothalamic tract (anterolateral: pain + temperature → decussates within 1–2 levels of entry → contralateral cortex). Spinocerebellar tracts (proprioception to cerebellum — coordination). DESCENDING (motor): Corticospinal (lateral corticospinal tract — decussates at pyramids → contralateral limbs — skilled voluntary movement). Anterior corticospinal (ipsilateral — axial muscles).",
        "Brown-Séquard syndrome (hemisection): IPSILATERAL loss of motor (corticospinal) + vibration/proprioception (dorsal column) + CONTRALATERAL loss of pain/temperature (spinothalamic) BELOW lesion. Syringomyelia: central canal expansion → bilateral loss of pain/temperature at level of lesion (crossing spinothalamic fibers) + preservation of dorsal columns ('cape-like' distribution over shoulders and upper limbs). Tabes dorsalis (syphilis — tertiary): dorsal column degeneration → loss of proprioception + vibration + Romberg sign + Charcot joints. ALS: combined UMN (corticospinal — spasticity, hyperreflexia) + LMN (anterior horn — fasciculations, atrophy) — NO sensory loss."
    ),
    "coronary arteries": _af(
        "Cardiac Anatomy — right (RCA) and left (LCA) coronary arteries arise from aortic sinuses of Valsalva just above aortic valve cusps",
        "Right coronary artery (RCA): supplies SA node (55%), AV node (90%), inferior wall (II, III, aVF), right ventricle, posterior descending artery (PDA) in right-dominant (85% of people). Left main coronary artery → Left Anterior Descending (LAD): anterior wall, interventricular septum (V1–V4), first diagonal branch → anterior papillary muscle → anterior LV wall. Left Circumflex (LCx): lateral wall (I, aVL, V5–V6), posterior wall (in left-dominant, 15%), AV node (in left-dominant), SA node (45%). Posterior Descending Artery (PDA): determines dominance (RCA in 85% = right dominant)",
        "STEMI territories: Inferior (II, III, aVF) = RCA occlusion — check for right-sided leads (RV infarct — avoid nitrates → preload-dependent RV → hypotension). Anterior (V1–V4) = LAD occlusion (worst territory — large mass of myocardium — highest mortality). Lateral (I, aVL, V5–V6) = LCx or Diagonal branch. Posterior MI (tall R wave in V1–V3 + ST depression): RCA or LCx — get posterior leads (V7–V9 → ST elevation). Papillary muscle rupture: posteromedial (most common — single blood supply from PDA, usually RCA) vs. anterolateral (dual LAD + LCx supply — less common)."
    ),
    # ── Physiology ────────────────────────────────────────────────────────
    "oxygen hemoglobin curve": _af(
        "Respiratory Physiology — sigmoidal (S-shaped) curve relating oxygen saturation (SaO2/SpO2) of hemoglobin to partial pressure of oxygen (PaO2)",
        "Normal P50 (PaO2 for 50% Hgb saturation) = 26–27 mmHg. Key points on curve: PaO2 60 mmHg = SpO2 ~90% (knee of curve — below this, saturation falls steeply). PaO2 100 mmHg = SpO2 ~97.5%. RIGHT SHIFT (↑P50 → ↓affinity → ↑O2 unloading to tissues): ↑T (fever), ↑CO2 (Bohr effect), ↑2,3-DPG (chronic hypoxia, anemia, altitude), ↑H+ (acidosis), sickle cell. LEFT SHIFT (↓P50 → ↑affinity → ↓O2 unloading): ↓T, ↓CO2, ↓2,3-DPG (stored blood), ↓H+ (alkalosis), fetal Hgb (HbF — has γ chains instead of β, binds 2,3-DPG less), CO poisoning (carboxyhemoglobin — left shift + functional anemia), methemoglobin",
        "Carbon monoxide (CO) poisoning: double effect — (1) CO competes with O2 for Hgb binding (250× higher affinity) → ↓functional Hgb; (2) CO binding SHIFTS curve LEFT → remaining Hgb releases O2 less readily → compounded tissue hypoxia. Treatment: 100% O2 (shortens CO-Hgb t1/2 from ~5 h to 60–90 min) → HBO for severe (t1/2 ~20 min). Fetal Hgb: ↑O2 affinity (↓2,3-DPG binding) → placental O2 transfer (fetus extracts O2 from maternal Hgb at lower PaO2). 2,3-DPG: stored blood depleted → left shift → old blood transfusions may not release O2 efficiently to tissues. Pulse oximetry reads HbCO as oxygenated → SpO2 falsely normal in CO poisoning (use co-oximetry). Methemoglobinemia (Fe³⁺ cannot bind O2): SpO2 plateaus ~85% with normal PaO2, chocolate-colored blood → treat with methylene blue."
    ),
    "raas": _af(
        "Cardiovascular/Renal Physiology — Renin-Angiotensin-Aldosterone System; activated by ↓renal perfusion pressure, ↓Na+ delivery to macula densa, sympathetic activation (β1 → ↑renin release from juxtaglomerular cells)",
        "Renin (JG cells → cleaves angiotensinogen → Angiotensin I) → ACE (pulmonary endothelium → converts Ang I → Angiotensin II) → Ang II: (1) vasoconstriction (↑BP, ↑GFR via efferent arteriole constriction — maintains GFR when renal perfusion ↓), (2) ↑aldosterone release (adrenal cortex zona glomerulosa → ↑Na+/H2O retention + ↑K+/H+ excretion), (3) ↑ADH (posterior pituitary → ↑H2O reabsorption in collecting duct), (4) ↑sympathetic activity, (5) cardiac + vascular remodeling (hypertrophy). Aldosterone: ↑ENaC (epithelial Na+ channels) + Na+/K+ ATPase in principal cells → Na+ retention + K+ excretion",
        "ACEi mechanism: block Ang I → Ang II conversion → ↓aldosterone + ↓efferent vasoconstriction → ↓GFR (↑K+, ↑Cr — especially in bilateral renal artery stenosis — relative CI). ACEi also blocks bradykinin degradation → bradykinin accumulation → dry cough (10–15%) + angioedema. ARBs: block AT1 receptor (all effects of Ang II blocked) — no bradykinin accumulation → no cough. Hyperaldosteronism (Conn): ↑aldosterone → hypokalemia + metabolic alkalosis + HTN + low plasma renin (negative feedback on JG cells). Primary hyperaldosteronism: low renin; secondary (renal artery stenosis): high renin."
    ),
    "frank starling": _af(
        "Cardiac Physiology — Frank-Starling law: stroke volume (SV) is directly related to end-diastolic volume (EDV)/preload — within physiologic range, greater ventricular filling → greater contractile force → ↑SV",
        "Mechanism: sarcomere length optimization (2.2 μm = optimal actin-myosin overlap → maximal cross-bridge formation → peak force generation). Calcium sensitization: as sarcomere stretches → titin (giant elastic protein) pulls thin filaments toward thick → ↑troponin-C calcium sensitivity → ↑force at same [Ca2+]. Starling curve: SV vs. EDV — steep rise (preload dependent range) → plateau (optimal) → decline (over-distension — rarely reached physiologically). Factors affecting curve: ↑contractility (NE, digoxin, Ca2+ sensitizers) shifts curve UP and LEFT; ↓contractility (heart failure, cardiomyopathy, ischemia, negative inotropes) shifts DOWN and RIGHT",
        "Heart failure: Frank-Starling mechanism initially COMPENSATES (↑EDV → ↑SV); as failure progresses, curve flattens → ↑EDV (↑LVEDP → pulmonary edema) with inadequate ↑SV. Laplace's law: wall stress = (P × r) / (2 × wall thickness) — dilated heart (↑r) requires MORE wall tension to generate same systolic pressure → ↑O2 demand → further dysfunction. Starling mechanism is why elevating legs (passive leg raise) → ↑venous return → immediate ↑SV → useful for fluid responsiveness assessment in ICU (>10% ↑CO = fluid responder). Preload ≈ LVEDV/LVEDP (estimated by PCWP); afterload ≈ SVR = (MAP − RAP)/CO × 80. Vasodilators (nitroprusside) ↓afterload → ↑SV in failing heart; diuretics move a failing patient left along a flat curve → ↓congestion with little ↓SV."
    ),
    "loop of henle": _af(
        "Renal Physiology — U-shaped tubular segment of nephron critical for urinary concentration; descending + ascending limbs have reciprocal permeabilities creating medullary interstitial gradient (countercurrent multiplication)",
        "Thin descending limb: permeable to H2O (aquaporin-1) + impermeable to solutes → as tubular fluid descends into hypertonic medulla → H2O leaves → tubular fluid becomes concentrated (↑osmolality, ↑[NaCl]). Thin ascending limb (inner medulla): impermeable to H2O + somewhat permeable to NaCl. Thick ascending limb (TAL — outer medulla): impermeable to H2O + actively reabsorbs NaCl (NKCC2 cotransporter — Na+/K+/2Cl- → builds medullary hypertonicity). TAL = site of action of LOOP DIURETICS (furosemide, bumetanide, torsemide — inhibit NKCC2 → ↓medullary gradient → ↓urine concentrating ability + ↓Na+ reabsorption → natriuresis + diuresis). Macula densa: specialized TAL cells sensing [NaCl] for tubuloglomerular feedback",
        "Furosemide mechanism: blocks NKCC2 in thick ascending limb → (1) ↑Na+ delivery to distal nephron → ↑K+ secretion (hypokalemia), (2) destroys medullary concentration gradient → ↓ADH effectiveness → ↓urine concentration, (3) ↑Ca2+ and Mg2+ excretion (hypocalcemia — unlike thiazides which ↑Ca2+ reabsorption). Bartter syndrome: inherited NKCC2/ROMK mutation → equivalent to chronic furosemide ingestion → hypokalemia + metabolic alkalosis + high renin + normal BP (salt wasting). Countercurrent multiplier (Henle) + Countercurrent exchanger (vasa recta) = together allow urine concentration up to 1200 mOsm/kg."
    ),
    "coagulation cascade": _af(
        "Hematology/Physiology — two interconnecting pathways of serine protease activation leading to fibrin clot formation; measured clinically by PT/INR (extrinsic) and aPTT (intrinsic)",
        "Extrinsic pathway (PT): tissue factor (TF/factor III) released by damaged subendothelial cells → TF binds FVII → TF-FVIIa complex (extrinsic tenase) → activates FX. Intrinsic pathway (aPTT): contact activation — FXII → FXIa → FIXa + FVIIIa (intrinsic tenase) → activates FX. Common pathway (both PT + aPTT): FXa + FVa (prothrombinase complex) → prothrombin (FII) → thrombin (FIIa) → fibrinogen → fibrin monomer → FXIIIa crosslinks → stable fibrin. Key amplification: thrombin activates FV, FVIII, FXIII (positive feedback) + protein C (anticoagulation). Anticoagulants: ATIII (inactivates thrombin + FXa — heparin cofactor), Protein C/S (inactivates FVa + FVIIIa), TFPI (inhibits TF-FVIIa)",
        "PT (Prothrombin Time): measures extrinsic + common pathway (Factors I, II, V, VII, X) — prolonged by warfarin (blocks vitamin K-dependent factors II, VII, IX, X, protein C, S — VII shortest half-life → PT rises first), liver failure, vitamin K deficiency. aPTT (activated Partial Thromboplastin Time): measures intrinsic + common pathway (Factors I, II, V, VIII, IX, X, XI, XII) — prolonged by heparin (activates ATIII → ↓FXa + thrombin), hemophilia A (FVIII ↓) or B (FIX ↓). Hemophilia A: ↑aPTT, normal PT, FVIII deficiency (X-linked). Hemophilia B: ↑aPTT, normal PT, FIX deficiency (X-linked). vWD: ↑bleeding time (defective platelet adhesion) ± ↑aPTT (vWF carries and protects FVIII), normal PT and platelet count."
    ),
    "action potential": _af(
        "Neurophysiology/Cardiac Physiology — rapid, transient reversal of membrane potential in excitable cells (neurons, cardiac + skeletal muscle)",
        "Resting membrane potential (RMP): −70 mV (neurons), −90 mV (cardiac — maintained by K+ leak channels + Na+/K+ ATPase). PHASES (cardiac): Phase 0 (rapid depolarization — fast Na+ channels open → Na+ influx — Vmax). Phase 1 (rapid repolarization — Na+ channels inactivate, transient K+ efflux — Ito). Phase 2 (plateau — Ca2+ influx via L-type channels = K+ efflux — unique to cardiac cells; prolonged plateau prevents tetany; absolute refractory period). Phase 3 (rapid repolarization — K+ efflux via IKr + IKs channels). Phase 4 (resting or pacemaker potential — SA node: funny current If pacemaker depolarization — automatically reaches threshold). Neuronal AP: depolarization threshold (−55 mV) → Na+ channels open (↑PNa) → peak +30 mV → K+ channels open (delayed) → repolarization → hyperpolarization → refractory period",
        "Absolute refractory period (cardiac): during phases 0–2 and early phase 3 — NO stimulus regardless of intensity can trigger AP (Na+ channels in inactivated state — cardiac muscle CANNOT tetanize → ensures complete relaxation between beats). Relative refractory period: late phase 3 — very strong stimulus can trigger AP (vulnerable period — R-on-T phenomenon → ventricular fibrillation risk). Class I antiarrhythmics: Na+ channel blockers (slow phase 0, ↑threshold). Class III (amiodarone, sotalol): K+ channel blockers (prolong phase 3 → ↑QT interval). Hypocalcemia: prolongs plateau phase → ↑QT interval. Hyperkalemia: ↑RMP toward threshold → ↓AP duration → peak: tent-peaked T waves → then progressive conduction slowing → sine wave → VF."
    ),

    # ── Renal ─────────────────────────────────────────────────────────────────
    "nephron": _af(
        "Renal Anatomy — functional unit of kidney (~1 million per kidney). Divided into glomerulus (filtration) + tubule (reabsorption/secretion/concentration)",
        "Glomerulus: afferent arteriole → glomerular capillary tuft → Bowman's capsule → filtration (GFR ~125 mL/min; filters everything <70 kDa — excludes proteins, cells). Proximal convoluted tubule (PCT): reabsorbs 65% filtered Na+, water, glucose (all), amino acids, phosphate, urate; secretes H+, organic acids/drugs. Loop of Henle: thin descending (water-permeable only — water absorbed, concentrates) → thin ascending (impermeable to water) → thick ascending (TAL: reabsorbs Na+/K+/2Cl⁻ via NKCC2 cotransporter; impermeable to water → dilutes tubular fluid; site of action of loop diuretics). Distal convoluted tubule (DCT): reabsorbs Na+/Cl⁻ via NCC cotransporter (thiazide site); regulated by parathyroid hormone (PTH → ↑Ca²⁺ reabsorption). Collecting duct (CD): aldosterone → ↑Na+ reabsorption (ENaC) + ↑K+ secretion; ADH → ↑water permeability (aquaporin-2 insertion); site of final urine concentration (1200 mOsm/kg in medullary CD)",
        "Sites of nephrotoxicity: PCT (aminoglycosides, contrast — acute tubular necrosis; cisplatin, ifosfamide, tenofovir, expired tetracyclines — Fanconi syndrome); distal tubule/collecting duct (amphotericin B — type 1 [distal] RTA; lithium — nephrogenic DI by blocking ADH effect on AQP2). Fanconi syndrome: generalized PCT dysfunction → wasting of glucose, amino acids, phosphate, urate, HCO3⁻ — type II RTA, hypophosphatemic rickets. Juxtaglomerular apparatus (JGA): macula densa (DCT cells sense NaCl delivery → regulate renin release) + JG cells (produce renin) → RAAS."
    ),
    "juxtaglomerular apparatus": _af(
        "Renal Physiology — specialized structure at afferent arteriole-DCT junction that regulates GFR and blood pressure via renin-angiotensin-aldosterone system (RAAS)",
        "Components: macula densa (modified DCT cells — sense luminal NaCl concentration → signal JG cells), juxtaglomerular (granular) cells (modified smooth muscle of afferent arteriole — contain renin granules), mesangial cells (intraglomerular — regulate glomerular blood flow; extraglomerular — phagocytic). Tubuloglomerular feedback (TGF): ↑NaCl at macula densa → afferent arteriole constriction → ↓GFR (autoregulation). Low NaCl → ↑renin release → angiotensin II → efferent arteriole constriction → maintains GFR",
        "RAAS: renin (cleaves angiotensinogen → angiotensin I) → ACE (lung — converts AI → AII) → AII (↑aldosterone, ↑ADH, ↑SNS, vasoconstriction, ↑proximal Na+ reabsorption). ACE inhibitors block AII formation → dilate efferent arteriole → ↓GFR (avoid in bilateral renal artery stenosis — removes AII-mediated efferent vasoconstriction → catastrophic ↓GFR). Prostaglandins: maintain afferent arteriole dilation in volume-depleted states — NSAIDs block → ↓GFR in susceptible patients (CHF, cirrhosis, CKD)."
    ),
    # ── Pulmonary ─────────────────────────────────────────────────────────────
    "lung anatomy": _af(
        "Pulmonary Anatomy — right lung (3 lobes: upper, middle, lower) and left lung (2 lobes: upper, lower; lingula = part of LUL — equivalent to right middle lobe). 18–19 total bronchopulmonary segments",
        "Right lung: RUL (3 segments: apical, posterior, anterior) — posterior segment is an aspiration site when supine; RML (2 segments: medial, lateral); RLL (5 segments: superior, medial basal, anterior basal, lateral basal, posterior basal). Left lung: LUL (upper division: apical-posterior, anterior; lower division/lingula: superior lingular, inferior lingular); LLL (4–5 segments — similar to RLL). Bronchial tree: mainstem bronchi → lobar → segmental → subsegmental → terminal bronchioles (no cartilage, gas exchange begins with respiratory bronchioles). Carina at T4/T5 level. Right mainstem bronchus: shorter, wider, more vertical → foreign bodies and aspirate preferentially enter the right lung (right lower lobe if upright; posterior RUL or superior RLL if supine)",
        "Aspiration pneumonia: right lower lobe (basal segments) most common in upright/semi-recumbent; superior segment of RLL or posterior segment of RUL in supine/obtunded. Lobectomy: remove lobe (most common oncologic lung resection). Pneumonectomy: remove entire lung (higher complication rate). Pleural fissures: horizontal (minor — separates RUL from RML), oblique (major — both lungs, separates lower from upper lobes). Silhouette sign on CXR: loss of border = adjacent consolidation (e.g., loss of right heart border = RML consolidation; obscured diaphragm = lower lobe)."
    ),
    "diaphragm": _af(
        "Thoracic/Abdominal Anatomy — primary muscle of inspiration; dome-shaped, divides thorax and abdomen. Motor: phrenic nerve (C3–C5; 'C3, 4, 5 keeps the diaphragm alive'). Sensory: phrenic nerve (central) + lower intercostal nerves T7–T11 and subcostal nerve (peripheral rim)",
        "Three major openings (mnemonic 'I 8 10 Eggs At 12': IVC T8, (o)Esophagus T10, Aorta T12): Caval hiatus at T8 (IVC + right phrenic nerve), Esophageal hiatus at T10 (esophagus + vagus nerves [CN X] — CN X goes through with esophagus), Aortic hiatus at T12 (aorta + thoracic duct + azygos vein — posterior to diaphragm, not through it). Crura: right crus originates L1–L3 (larger — forms esophageal hiatus), left crus L1–L2. Central tendon: non-muscular center, fuses with fibrous pericardium",
        "Hiatal hernia: sliding (Type I — GEJ slides into chest — 95% — associated with GERD) vs. paraesophageal (Type II — fundus herniates beside a normally placed GEJ; Type III — mixed, GEJ also displaced — risk of volvulus/strangulation). Diaphragmatic hernia: congenital (Bochdalek — posterior/left — most common; Morgagni — anterior/right — rare) → bowel in thorax → ipsilateral lung hypoplasia → neonatal respiratory distress. Phrenic nerve palsy: elevated hemidiaphragm on CXR + fluoroscopy ('sniff test'). Referred pain: diaphragmatic irritation (e.g., subphrenic abscess, splenic rupture, ectopic pregnancy) → shoulder tip pain (C4 referred)."
    ),
    "mediastinum": _af(
        "Thoracic Anatomy — central compartment of thorax, between the two pleural sacs. Divided into superior and inferior (anterior, middle, posterior) mediastinum",
        "Superior mediastinum (above angle of Louis/T4): thymus, great vessels (aortic arch + branches, SVC, brachiocephalic veins), trachea, esophagus, thoracic duct, phrenic + vagus nerves. Anterior mediastinum (front of pericardium): thymus (children — can persist in adults), lymph nodes, fat. Mnemonic: 'The Four Ts' — Thymoma, Teratoma (and germ cell tumors), Terrible lymphoma (lymphoma), Thyroid (substernal goiter). Middle mediastinum: pericardium + heart + great vessel roots + carina + mainstem bronchi + phrenic nerves. Posterior mediastinum (behind pericardium): esophagus, descending thoracic aorta, azygos/hemiazygos veins, thoracic duct, sympathetic chain, posterior lymph nodes",
        "Widened mediastinum (>8 cm on PA CXR): aortic dissection/rupture (most important to exclude — trauma mechanism), thoracic aortic aneurysm, lymphoma, thymoma, massive lymphadenopathy. Anterior mediastinal mass in adults (4 Ts): Thymoma (#1 adult — associated with myasthenia gravis, pure red cell aplasia), Teratoma/germ cell, Terrible lymphoma (Hodgkin > NHL), Thyroid. Posterior mediastinal mass: neurogenic tumors (schwannoma, neurofibroma, neuroblastoma — 'Paravertebral mass' = posterior mediastinum until proven otherwise). Superior vena cava (SVC) syndrome: SVC obstruction → facial/arm edema, plethora, dilated neck veins, headache — malignancy most common cause."
    ),
    # ── Gastrointestinal ──────────────────────────────────────────────────────
    "liver anatomy": _af(
        "Hepatic Anatomy — largest solid organ (1.4–1.6 kg). Functional division (Couinaud — 8 segments based on portal pedicles + hepatic veins) differs from surface anatomy (right/left lobes by falciform ligament)",
        "Couinaud segments (I–VIII): Segment I = caudate lobe (independent vascular supply + drainage directly to IVC). Segments II–IV = left liver. Segments V–VIII = right liver. Hepatic veins (right, middle, left) divide liver into territories: right → segments V–VIII; middle → separates right from left; left → II–IV. Portal triad (periportal area): portal vein branch + hepatic artery branch + bile ductule. In the hepatoduodenal ligament: portal vein posterior, common bile duct lateral (right), proper hepatic artery medial (left). Hepatic acinus zones: Zone 1 (periportal — first to receive O2/nutrients — last to undergo ischemic necrosis — affected first by viral hepatitis and ingested toxins such as cocaine); Zone 3 (centrilobular — most ischemia-prone — richest in CYP450 → acetaminophen, alcohol, halothane toxicity — congestive hepatopathy in RHF — 'nutmeg liver')",
        "Portal hypertension collaterals: Paraumbilical veins → caput medusae (left portal vein → umbilical vein → paraumbilical → abdominal wall veins). Esophageal varices (left gastric vein). Rectal varices (inferior mesenteric → superior rectal). Splenorenal (retroperitoneal) shunts. Riedel's lobe: normal variant — tongue-like extension of right lobe. Morrison's pouch (hepatorenal space): most dependent space in peritoneal cavity in supine position — first site of free fluid accumulation on US."
    ),
    "portal circulation": _af(
        "Hepatic Vascular Anatomy — portal venous system carries nutrient-rich blood from GI tract and spleen to liver before systemic circulation. Dual blood supply: portal vein (75% of hepatic blood flow, 50% of O2) + hepatic artery (25% flow, 50% O2)",
        "Portal vein (PV) formation: splenic vein + superior mesenteric vein (SMV) at level of neck of pancreas (L2). IMV drains into splenic vein (or SMV junction). Portal blood → hepatic sinusoids (mixes with hepatic arterial blood) → central veins → hepatic veins → IVC (bile flows the opposite way: canaliculi → bile ducts → CBD → ampulla of Vater). Hepatic venous pressure gradient (HVPG): normal 1–5 mmHg; portal hypertension >5, clinically significant ≥10 (varices/ascites), variceal bleeding risk >12 mmHg. Portosystemic anastomoses (sites of portocaval connection that enlarge in portal HTN): esophagogastric junction (left gastric → esophageal veins), rectum (superior rectal → middle/inferior rectal), paraumbilical (umbilical vein → paraumbilical → abdominal wall), retroperitoneum (Retzius veins)",
        "Budd-Chiari syndrome: hepatic vein or IVC thrombosis → post-sinusoidal portal hypertension → hepatomegaly, RUQ pain, ascites. Causes: hypercoagulable (polycythemia vera — JAK2 mutation — most common, APS, pregnancy, OCP, PNH). Doppler US: absent hepatic vein flow. Treatment: anticoagulation + TIPS + liver transplant. Pylephlebitis: septic portal vein thrombosis (appendicitis, diverticulitis) — abdominal pain + fever + bacteremia → IV antibiotics + anticoagulation. TIPS: creates artificial portosystemic shunt (interventional radiology) → reduces portal pressure → treats refractory ascites and variceal bleeding → risk of encephalopathy."
    ),
    "stomach anatomy": _af(
        "Gastrointestinal Anatomy — hollow muscular organ from gastroesophageal junction (GEJ) to pylorus. Regions: cardia, fundus (superior), body (corpus), antrum, pylorus",
        "Layers (inside out): mucosa (epithelium + lamina propria + muscularis mucosae) → submucosa (Meissner's plexus) → muscularis propria (inner oblique — unique to stomach, middle circular, outer longitudinal; Auerbach's/myenteric plexus between circular and longitudinal) → serosa. Cell types: fundus/body parietal cells (HCl + intrinsic factor — IF), chief cells (pepsinogen), ECL cells (histamine — stimulate parietal), G cells (antrum — gastrin secretion). Gastric acid stimulation: ACh (vagus → M3), histamine (H2), gastrin (CCK-B receptor on parietal cell). Inhibition: somatostatin (D cells), prostaglandins, secretin. Blood supply: lesser curvature (left + right gastric aa. from celiac + hepatic), greater curvature (left + right gastroepiploic), fundus (short gastric from splenic artery)",
        "Peptic ulcer disease: H. pylori (~90% of duodenal, ~70% of gastric ulcers) + NSAIDs. Duodenal ulcer: INCREASED acid (Hp → ↑gastrin → ↑HCl); pain RELIEVED by food (buffer). Gastric ulcer: impaired mucosal defense; pain WORSENED by food. Virchow's node (supraclavicular LN — left) + Sister Mary Joseph nodule (periumbilical) + Blumer's shelf (rectal) = gastric cancer metastatic disease. Gastric cancer: H. pylori (#1 risk factor), signet ring cells (diffuse type — poor prognosis; Lauren classification: diffuse vs. intestinal). Zollinger-Ellison syndrome: gastrinoma (duodenum/pancreas) → massive HCl secretion → multiple/refractory/distal ulcers + diarrhea."
    ),
    "pancreas anatomy": _af(
        "Gastrointestinal/Endocrine Anatomy — retroperitoneal gland; head (in duodenal C-loop), neck (over SMA/SMV), body, tail (to splenic hilum). Exocrine (95%) + endocrine (islets of Langerhans, 5%)",
        "Exocrine: acinar cells (digestive enzymes — amylase, lipase, proteases as zymogens), ductal cells (bicarbonate-rich fluid). Main pancreatic duct (Wirsung) + accessory duct (Santorini). Ampulla of Vater: junction of CBD + main pancreatic duct → enters duodenum at major papilla. Sphincter of Oddi: controls flow of bile + pancreatic juice. Pancreas divisum: incomplete fusion of dorsal + ventral pancreatic buds (common variant ~10% — dorsal duct drains via minor papilla — may cause recurrent pancreatitis). Annular pancreas: ventral bud encircles duodenum → duodenal obstruction (double-bubble sign in neonates). Endocrine: Islets of Langerhans — alpha cells (glucagon — periphery), beta cells (insulin — center), delta cells (somatostatin), PP cells (pancreatic polypeptide), epsilon cells (ghrelin)",
        "Pancreatic cancer: 90% ductal adenocarcinoma; head (70% — present early with obstructive jaundice); body/tail (late presentation — worse prognosis). CA 19-9: tumor marker (not screening). Whipple procedure (pancreaticoduodenectomy): for resectable head of pancreas cancer — removes head + duodenum + common bile duct + gallbladder + distal stomach. Uncinate process: extension of the head posterior to the SMV. 'Double-duct sign' (dilated CBD + pancreatic duct) on imaging is classic for a pancreatic head mass. VIPoma: VIP-secreting tumor → profuse watery diarrhea + hypokalemia + achlorhydria (Verner-Morrison/WDHA syndrome)."
    ),
    # ── Musculoskeletal ───────────────────────────────────────────────────────
    "dermatomes": _af(
        "Neuroanatomy — cutaneous sensory distribution of spinal nerve roots. Key landmarks for clinical localization of cord/root lesions",
        "Cervical: C2 (occiput — top of ear), C3 (neck below ear/jaw), C4 (shoulder cape), C5 (lateral arm to elbow), C6 (lateral forearm, thumb + index finger — C6 = thumb, 'C-6 like a gun with thumb up'), C7 (middle finger — 'C7 in middle'), C8 (medial forearm, ring + little finger). Thoracic: T4 (nipple line — 'T4 at nipple floor'), T6 (xiphoid process), T8 (costal margin), T10 (umbilicus — 'T10 at umbilicus'), T12 (suprapubic). Lumbar: L1 (inguinal ligament), L2 (anterior upper thigh), L3 (anterior lower thigh, medial knee), L4 (knee, medial leg, medial malleolus — 'down on all fours' = kneecap), L5 (lateral leg, dorsum of foot, great toe), S1 (posterior leg, lateral foot, small toe — S1 = plantar flexion, ankle jerk reflex), S2–S4 (perineum, genitalia, 'saddle area')",
        "Nerve root reflexes: biceps C5–C6 (musculocutaneous), brachioradialis C6 (radial), triceps C7 (radial), patellar L3–L4 (femoral), Achilles S1 (tibial). Dermatomal pain patterns: L4–L5 disc herniation (L5 root) → radiation to dorsal foot + great toe, weak great-toe extension/dorsiflexion (foot drop); L5–S1 disc (S1 root) → radiation to sole + plantar flexion weakness + absent ankle jerk. Shingles: dermatomal vesicular rash following nerve root — most common thoracic (T6–T9). Radiculopathy vs. peripheral neuropathy: dermatomal vs. stocking-glove distribution."
    ),
    "lumbar plexus": _af(
        "Peripheral Nerve Anatomy — formed by anterior rami of L1–L4 (±T12). Lies within psoas major muscle. Supplies anterior and medial thigh",
        "Branches: Iliohypogastric (L1 — sensory: inguinal region + lateral buttock), Ilioinguinal (L1 — sensory: upper medial thigh + scrotum/labia majora), Genitofemoral (L1–L2 — genital: cremasteric reflex; femoral: sensation over femoral triangle), Lateral cutaneous nerve of thigh (LCNT; L2–L3 — lateral thigh; compression → meralgia paresthetica), Femoral nerve (L2–L4 — motor: hip flexors + knee extensors [quadriceps]; sensory: anterior/medial thigh + medial leg via saphenous nerve), Obturator nerve (L2–L4 — motor: hip adductors; sensory: medial thigh). Femoral nerve injury (hip fracture/surgery, diabetes, retroperitoneal hematoma): weak hip flexion + knee extension + absent patellar reflex + ↓sensation anteromedial thigh",
        "Meralgia paresthetica: LCNT compression (inguinal ligament, obesity, tight belt, pregnancy) → burning, tingling, numbness lateral thigh (no motor deficit). Obturator nerve injury (pelvic surgery, obturator hernia): ↓hip adduction + medial thigh pain. Psoas hematoma (anticoagulants, hemophilia): femoral nerve compression → weak quadriceps + absent patellar reflex. Lumbosacral trunk (L4–L5): connects lumbar plexus to sacral plexus → contributes to sciatic nerve."
    ),
    "sciatic nerve": _af(
        "Peripheral Nerve Anatomy — largest nerve in body (L4–S3). Formed in pelvis from lumbosacral plexus, exits through greater sciatic foramen (below piriformis usually), descends posterior thigh, bifurcates at popliteal fossa",
        "Components: tibial division (L4–S3 — medial) + common peroneal division (L4–S2 — lateral). Posterior thigh motor supply (hamstrings — biceps femoris, semitendinosus, semimembranosus + adductor magnus). Popliteal fossa bifurcation: Tibial nerve (descends deep to soleus → plantar flexion, foot inversion, toe flexion; terminal branches = medial + lateral plantar nerves → foot intrinsics; tarsal tunnel syndrome: tibial nerve under flexor retinaculum → plantar burning, numbness, tingling). Common peroneal nerve (wraps around fibular head — most vulnerable peripheral nerve to compression injury → foot drop): divides into superficial peroneal (foot eversion + dorsal foot sensation) + deep peroneal (dorsiflexion + sensation between 1st–2nd toes)",
        "Piriformis syndrome: sciatic nerve irritation from piriformis muscle spasm → buttock pain radiating down posterior thigh (mimics disc herniation). Common peroneal nerve palsy: foot drop + weak eversion + ↓sensation dorsal foot/lateral leg — causes: fibular head fracture, prolonged squatting, tight cast, crossed legs. Treatment: ankle-foot orthosis (AFO), physical therapy. Sciatic nerve stretch test (straight leg raise — SLR): pain below knee at <60° → positive for L4–S1 nerve root compression. Lasègue's sign: hip flexion + knee extension while supine — reproduces radiculopathy."
    ),
    # ── Cardiovascular ────────────────────────────────────────────────────────
    "heart valves": _af(
        "Cardiac Anatomy — 4 heart valves prevent retrograde blood flow. Semilunar: aortic (AV) and pulmonic (PV). Atrioventricular: mitral (MV, bicuspid) and tricuspid (TV)",
        "Aortic valve: right, left, posterior cusps. Opens with systole (↑LV pressure → AV opens → ejection). Pulmonic valve: anterior, right, left cusps. Mitral valve: anterior + posterior leaflets; supported by chordae tendineae → papillary muscles (anterolateral, posteromedial). Posteromedial papillary muscle: single blood supply (RCA or LCx) — most prone to rupture post-MI. Anterolateral papillary muscle: dual supply (LAD + LCx) — less common rupture. Tricuspid valve: 3 leaflets (anterior, posterior, septal). Valve areas: aortic (3–4 cm²), pulmonic (similar), mitral (4–6 cm²), tricuspid (7–9 cm²). Heart sounds: S1 (MV + TV closure — systole begins), S2 (AV + PV closure — systole ends). S3 (rapid ventricular filling — normal <30 and pregnant; pathological in HF = 'KentuckY'). S4 (atrial kick against stiff ventricle — hypertension, AS)",
        "Valvular disease pearls: Aortic stenosis (AS): crescendo-decrescendo systolic murmur at RUSB, radiation to carotids, pulsus parvus et tardus (weak, delayed carotid upstroke), symptoms (angina, syncope, HF) → valve replacement when symptomatic. Aortic regurgitation (AR): blowing diastolic murmur at LUSB, wide pulse pressure, bounding pulses (Corrigan), head bob (de Musset), Austin Flint murmur (severe AR). Mitral stenosis (MS): low-pitched diastolic rumble at apex, opening snap, AF common. Mitral regurgitation (MR): holosystolic murmur at apex radiating to axilla. Tricuspid regurgitation (TR): holosystolic at LLSB, ↑with inspiration (Carvallo's sign)."
    ),
    "cardiac conduction system": _af(
        "Cardiac Electrophysiology — specialized cells that generate and propagate electrical impulses coordinating cardiac contraction",
        "SA node (sinoatrial): right atrium near SVC junction; normal pacemaker (60–100 bpm); blood supply — SA nodal artery (55% from RCA, 45% from LCx). Internodal tracts → AV node (atrioventricular): inferior interatrial septum (triangle of Koch — bounded by CS os, tendon of Todaro, tricuspid annulus); delays conduction (~100 ms) — allows atrial emptying before ventricular systole; blood supply — AV nodal artery (90% from RCA, 10% from LCx — therefore inferior MI [RCA] causes AVB). Bundle of His → right bundle branch (RBB: to RV) + left bundle branch (LBB: to LV — divides into left anterior fascicle [LAF] + left posterior fascicle [LPF]). Purkinje fibers: rapid conduction to ventricular myocardium",
        "ECG intervals: PR (AV conduction — normal 120–200 ms; >200 = 1st degree AVB; shortens with ↑HR, catecholamines; lengthens with calcium channel blockers, beta-blockers, digoxin, AV nodal disease). QRS (ventricular activation — normal <120 ms; >120 = BBB or aberrancy or ventricular origin). QT (ventricular repolarization — corrected QTc = QT/√RR; normal <440 ms men, <460 ms women; prolonged by medications [amiodarone, sotalol, antipsychotics, azithromycin, fluoroquinolones] → torsades de pointes risk). Ashman phenomenon: aberrant conduction of beat following long-short RR cycle — mimics VT (often RBBB morphology)."
    ),
    # ── Lymphatics ────────────────────────────────────────────────────────────
    "lymph node regions": _af(
        "Lymphatic Anatomy — regional lymph node drainage patterns. Critical for staging malignancy and understanding infection spread",
        "Head and neck: occipital (posterior scalp), pre-/post-auricular (ear/temporal scalp), parotid (face, scalp), submandibular (lips, gingiva, anterior tongue, floor of mouth), submental (anterior lower lip, chin, central tongue tip), anterior cervical (larynx, thyroid, trachea, esophagus), posterior cervical (posterior scalp, cervical spine), supraclavicular (thoracic and abdominal viscera — Virchow's node = left supraclavicular = abdominal malignancy sentinel). Axillary (levels I–III — breast, arm, lateral thorax): level I (lateral to pectoralis minor), II (posterior to PM), III (medial to PM = apical). Rotter's (interpectoral) nodes lie between pectoralis major and minor. Mediastinal: hilar (lung primary drainage). Abdominal: celiac (GEJ, stomach, proximal duodenum, liver, spleen), SMA (small bowel), IMA (distal third of transverse colon, descending + sigmoid colon, upper rectum), para-aortic (testes — NOT inguinal — why testicular cancer spreads to para-aortic LN, not inguinal; kidneys, adrenals, ovaries, uterine fundus). Inguinal: superficial (below inguinal ligament — penis, scrotum, vulva, lower vagina, perineum, lower anal canal, lower limb) vs. deep (deep to fascia lata along the femoral vein — receive superficial nodes, glans, deep lower limb → external iliac)",
        "Testicular cancer: lymph drainage to para-aortic nodes (retroperitoneal) — NOT inguinal (important for staging). Rectal cancer: upper rectum → IMA nodes; lower rectum → internal iliac nodes; anal canal below pectinate line → superficial inguinal nodes. Penile cancer: superficial inguinal (first echelon). Breast cancer sentinel lymph node (SLN): most common = anterior axillary (Level I — 75%); Rotter's interpectoral nodes may be missed if Level I not sampled. Virchow's node (Troisier sign): left supraclavicular adenopathy = metastatic abdominal malignancy (thoracic duct → left subclavian → left supraclavicular)."
    ),
    # ── Upper Limb ────────────────────────────────────────────────────────────
    "median nerve": _af(
        "Peripheral Nerve — Upper Limb (C5–T1; lateral + medial cords)",
        "Course: lateral to the brachial artery in the upper arm, crosses to its medial side at mid-arm → cubital fossa (medial to brachial artery) → between the two heads of pronator teres → between FDS and FDP → carpal tunnel. Motor: most forearm flexors (pronator teres, FCR, palmaris longus, FDS; FPL, lateral half of FDP and pronator quadratus via the anterior interosseous branch) + thenar muscles and lateral 2 lumbricals (LOAF: Lumbricals 1–2, Opponens pollicis, Abductor pollicis brevis, Flexor pollicis brevis). Sensory: palmar thumb, index, middle and lateral half of ring finger (+ their dorsal fingertips); palmar cutaneous branch (lateral palm) leaves proximal to the carpal tunnel",
        "Supracondylar humerus fracture (proximal lesion): 'hand of benediction' when trying to make a fist (index + middle stay extended), thenar wasting, sensory loss. Carpal tunnel syndrome: thenar weakness + finger numbness but palm sensation SPARED (palmar cutaneous branch runs superficial to the flexor retinaculum). Anterior interosseous nerve lesion: cannot make the 'OK' sign (FPL + lateral FDP), no sensory loss. Recurrent (thenar) branch cut in a superficial palm laceration → loss of thumb opposition ('ape hand')."
    ),
    "ulnar nerve": _af(
        "Peripheral Nerve — Upper Limb (C8–T1; medial cord)",
        "Course: medial arm → behind the medial epicondyle (cubital tunnel — 'funny bone') → between the two heads of FCU → with the ulnar artery deep to FCU → enters the hand SUPERFICIAL to the flexor retinaculum through Guyon canal. Motor: FCU, medial half of FDP (digits 4–5), most intrinsic hand muscles — hypothenar muscles, medial 2 lumbricals, all interossei, adductor pollicis, deep head of FPB. Sensory: medial 1½ fingers (palmar + dorsal) and medial hand (dorsal cutaneous branch leaves in the distal forearm)",
        "Medial epicondyle fracture / elbow lesion: radial deviation on wrist flexion (FCU lost); clawing of digits 4–5 is LESS obvious because FDP 4–5 is also weak ('ulnar paradox'). Guyon canal lesion (fall on outstretched hand, cycling, hook of hamate fracture): marked clawing of digits 4–5, dorsal hand sensation spared. Froment sign: thumb IP joint flexes (FPL substitutes) when pinching paper — weak adductor pollicis. Cannot cross fingers (interossei)."
    ),
    "radial nerve": _af(
        "Peripheral Nerve — Upper Limb (C5–T1; posterior cord)",
        "Course: behind the axillary artery → triangular interval with the profunda brachii artery → spirals in the radial (spiral) groove of the humerus → pierces the lateral intermuscular septum → anterior to the lateral epicondyle → divides at the elbow into the superficial branch (sensory) and the deep branch / posterior interosseous nerve (motor, passes through supinator). Motor: all posterior arm and forearm muscles — 'BEST': Brachioradialis, Extensors of wrist/fingers/thumb, Supinator, Triceps (+ anconeus, APL). Sensory: posterior arm and forearm, dorsolateral hand and dorsum of the lateral 3½ fingers (not the nail beds)",
        "Midshaft humerus fracture (spiral groove): wrist drop + numb dorsal first web space; triceps usually SPARED (its branches arise above the groove). Axillary compression ('Saturday night palsy', crutches): wrist drop + triceps weakness. Posterior interosseous nerve (radial head dislocation, supinator syndrome): finger drop without sensory loss; wrist still extends but deviates radially (ECRL spared). Superficial branch (tight watch/handcuffs): numbness over the dorsal first web space."
    ),
    "axillary nerve": _af(
        "Peripheral Nerve — Upper Limb (C5–C6; posterior cord)",
        "Passes posteriorly through the quadrangular space with the posterior circumflex humeral artery and winds around the surgical neck of the humerus. Motor: deltoid (abduction 15–90°) and teres minor (lateral rotation). Sensory: skin over the lower deltoid ('regimental badge' area) via the superior lateral cutaneous nerve of the arm",
        "Injured by surgical neck fracture or anterior shoulder dislocation → flattened shoulder contour, weak abduction beyond 15° (supraspinatus still starts it), numb regimental badge area. Test this sensation before and after reducing a dislocated shoulder."
    ),
    "musculocutaneous nerve": _af(
        "Peripheral Nerve — Upper Limb (C5–C7; lateral cord)",
        "Pierces coracobrachialis, then runs between biceps brachii and brachialis. Motor: anterior arm flexors — coracobrachialis, biceps brachii, brachialis (elbow flexion; supination by biceps). Sensory: continues as the lateral cutaneous nerve of the forearm (lateral antebrachial cutaneous nerve)",
        "Injury (upper trunk C5–C6 lesions, penetrating trauma): weak elbow flexion and supination (brachioradialis — radial nerve — still flexes), absent biceps reflex (C5–C6), numb lateral forearm. The lateral antebrachial cutaneous nerve lies next to the cephalic vein at the elbow — can be hit during venipuncture."
    ),
    "long thoracic nerve": _af(
        "Peripheral Nerve — Thoracic Wall (C5–C7 roots — 'C5, 6, 7 raise your wings to heaven')",
        "Arises directly from the roots and descends on the superficial (lateral) surface of serratus anterior along the mid-axillary line. Motor: serratus anterior — protracts the scapula, holds it against the chest wall and rotates it upward for abduction above 90°",
        "Injury (axillary lymph node dissection/mastectomy, chest tube, heavy shoulder loads): medial 'winged scapula' when pushing against a wall; cannot raise the arm above horizontal. Lateral winging instead points to trapezius weakness (spinal accessory nerve, CN XI)."
    ),
    "suprascapular nerve": _af(
        "Peripheral Nerve — Shoulder (C5–C6; upper trunk)",
        "Passes through the suprascapular notch UNDER the superior transverse scapular ligament, while the suprascapular artery passes OVER it ('the army [artery] goes over the bridge, the navy [nerve] goes under'). Motor: supraspinatus (abduction 0–15°) and infraspinatus (lateral rotation)",
        "Compression at the suprascapular or spinoglenoid notch (overhead athletes, ganglion cyst) → deep shoulder pain, weak start of abduction and lateral rotation, wasting above and below the scapular spine."
    ),
    "rotator cuff": _af(
        "Musculoskeletal — Shoulder (SITS muscles)",
        "Supraspinatus (suprascapular n.) — initiates abduction 0–15°; Infraspinatus (suprascapular n.) — lateral rotation; Teres minor (axillary n.) — lateral rotation; Subscapularis (upper + lower subscapular nn.) — medial rotation + adduction. Supraspinatus, infraspinatus and teres minor insert on the greater tubercle; subscapularis on the lesser tubercle. Together they hold the humeral head in the shallow glenoid fossa",
        "Supraspinatus is the most commonly injured (impingement under the acromion, tendinopathy, tears): painful arc ~60–120° of abduction, positive empty-can test. Infraspinatus: common in pitchers. Subscapularis: lift-off test. Degenerative cuff tears are common after age 40."
    ),
    "glenohumeral joint": _af(
        "Joint — Shoulder (ball-and-socket synovial joint; most mobile, least stable)",
        "Shallow glenoid fossa deepened by the glenoid labrum; stability comes mainly from the rotator cuff. The capsule is weakest inferiorly. The long head of biceps tendon runs inside the capsule to the supraglenoid tubercle",
        "Anterior (anteroinferior) dislocation is ~95% of dislocations (abduction + external rotation) → axillary nerve at risk. Posterior dislocation: seizures, electric shock ('light bulb' sign on X-ray). Bankart lesion = anteroinferior labral tear; Hill-Sachs lesion = posterolateral humeral head impaction."
    ),
    "axilla": _af(
        "Gross Anatomy — pyramidal space between the arm and chest wall",
        "Apex (cervicoaxillary canal) between the clavicle, 1st rib and scapula — passage from the neck. Walls: anterior — pectoralis major + minor; posterior — subscapularis, teres major, latissimus dorsi; medial — serratus anterior over ribs 1–4; lateral — intertubercular groove of the humerus. Contents: axillary artery and vein, cords and branches of the brachial plexus, axillary lymph nodes (pectoral, humeral, subscapular, central, apical), fat",
        "Axillary node dissection risks the long thoracic nerve on the medial wall (winged scapula), the thoracodorsal nerve on the posterior wall (weak latissimus dorsi — adduction, extension, medial rotation) and the intercostobrachial nerve (numb medial upper arm). Lymphatic removal → arm lymphedema."
    ),
    "axillary artery": _af(
        "Vascular — Upper Limb (continuation of the subclavian artery at the lateral border of the 1st rib; becomes the brachial artery at the lower border of teres major)",
        "Divided into 3 parts by pectoralis minor, with 1, 2 and 3 branches ('Screw The Lawyer Save A Patient'): part 1 — Superior thoracic; part 2 — Thoracoacromial, Lateral thoracic; part 3 — Subscapular, Anterior circumflex humeral, Posterior circumflex humeral. The brachial artery gives the profunda brachii (runs with the radial nerve in the spiral groove) and divides in the cubital fossa (at the neck of the radius) into the radial and ulnar arteries",
        "Scapular anastomosis (suprascapular, dorsal scapular and circumflex scapular arteries) keeps the arm perfused when the axillary artery is ligated between the thyrocervical trunk and the subscapular artery. Surgical neck fracture → posterior circumflex humeral artery; midshaft fracture → profunda brachii; supracondylar fracture → brachial artery."
    ),
    "quadrangular space": _af(
        "Gross Anatomy — posterior shoulder",
        "Borders: superior — teres minor; inferior — teres major; medial — long head of triceps; lateral — surgical neck of the humerus. Contents: axillary nerve + posterior circumflex humeral artery. Triangular space (teres minor, teres major, long head of triceps): circumflex scapular artery. Triangular interval (teres major, long head of triceps, humerus/lateral head): radial nerve + profunda brachii artery",
        "Quadrangular space syndrome (overhead athletes, fibrous bands): axillary nerve compression → posterior shoulder pain and deltoid/teres minor weakness."
    ),
    "humerus": _af(
        "Bone — Arm",
        "Nerve and artery in contact with each part: surgical neck — axillary nerve + posterior circumflex humeral artery; radial (spiral) groove at midshaft — radial nerve + profunda brachii artery; medial epicondyle — ulnar nerve; supracondylar region — median nerve + brachial artery. Greater tubercle: supraspinatus, infraspinatus, teres minor. Lesser tubercle: subscapularis. Intertubercular groove: long head of biceps tendon ('the lady between two majors' — latissimus dorsi inserts in the floor between pectoralis major and teres major)",
        "Fracture → nerve: surgical neck → deltoid weakness + numb regimental badge area; midshaft → wrist drop; supracondylar (children, fall on outstretched hand) → median/anterior interosseous nerve + brachial artery (check the radial pulse; risk of compartment syndrome / Volkmann contracture); medial epicondyle → ulnar nerve."
    ),
    "cubital fossa": _af(
        "Gross Anatomy — triangular space in front of the elbow",
        "Borders: superior — line between the humeral epicondyles; medial — pronator teres; lateral — brachioradialis. Roof: bicipital aponeurosis + deep fascia (median cubital vein lies superficial to it). Floor: brachialis + supinator. Contents lateral → medial: radial nerve (deep, between brachioradialis and brachialis), biceps tendon, brachial artery, median nerve ('Really Need Beer To Be At My Nicest')",
        "Median cubital vein is the usual venipuncture site — the bicipital aponeurosis shields the brachial artery and median nerve underneath. Supracondylar fracture (children) can injure the brachial artery (Volkmann ischemic contracture) and median nerve."
    ),
    "anatomical snuffbox": _af(
        "Surface Anatomy — radial side of the wrist",
        "Borders: lateral (radial) — tendons of abductor pollicis longus + extensor pollicis brevis; medial (ulnar) — extensor pollicis longus. Floor: scaphoid and trapezium. Contents: radial artery (palpable pulse); the cephalic vein begins here; the superficial branch of the radial nerve crosses it",
        "Snuffbox tenderness after a fall on an outstretched hand = scaphoid fracture until proven otherwise, even with a normal first X-ray — immobilize in a thumb spica and re-image (MRI). Blood enters the scaphoid distally, so proximal pole fractures risk avascular necrosis and non-union."
    ),
    "scaphoid": _af(
        "Bone — Wrist (carpal bone, proximal row)",
        "Carpal bones lateral → medial: proximal row Scaphoid, Lunate, Triquetrum, Pisiform; distal row Trapezium, Trapezoid, Capitate, Hamate ('Some Lovers Try Positions That They Can't Handle'). The scaphoid forms the floor of the anatomical snuffbox; its blood supply (radial artery) enters the distal pole and flows backward to the proximal pole",
        "Most commonly fractured carpal bone (fall on outstretched hand) → snuffbox tenderness; often missed on the first X-ray; the proximal fragment can undergo avascular necrosis. Lunate is the most commonly DISLOCATED carpal bone (can compress the median nerve → acute carpal tunnel). Hook of hamate fracture (golf, racket sports) → ulnar nerve injury in Guyon canal."
    ),
    "guyon canal": _af(
        "Fibro-osseous Tunnel — ulnar side of the wrist",
        "Between the pisiform (medial) and the hook of the hamate (lateral); roof — palmar carpal ligament; floor — flexor retinaculum (transverse carpal ligament). Contents: ulnar nerve and ulnar artery — NOT in the carpal tunnel",
        "Compression (cycling — 'handlebar palsy', hook of hamate fracture, ganglion): clawing of digits 4–5, weak interossei and hypothenar muscles; sensation of the dorsal medial hand is spared (dorsal cutaneous branch leaves above the canal)."
    ),
    "interossei": _af(
        "Intrinsic Hand Muscles — deep branch of the ulnar nerve",
        "Palmar interossei ADduct the fingers toward the middle finger (PAD); dorsal interossei ABduct them (DAB). Both flex the MCP joints and extend the IP joints. Lumbricals arise from the FDP tendons and also flex MCP + extend IP joints: lateral 2 — median nerve, medial 2 — ulnar nerve",
        "Card test: holding paper between the fingers tests palmar interossei (ulnar nerve). Ulnar nerve lesion → weak finger abduction/adduction, cannot cross fingers; loss of lumbricals 3–4 → clawing of digits 4–5. Klumpke palsy (C8–T1) → claw hand of all digits."
    ),
    # ── Lower Limb ────────────────────────────────────────────────────────────
    "femoral nerve": _af(
        "Peripheral Nerve — Lower Limb (L2–L4; lumbar plexus, posterior divisions)",
        "Forms within psoas major, runs in the groove between psoas and iliacus, and enters the thigh deep to the inguinal ligament LATERAL to the femoral sheath (not inside it). Motor: iliacus, pectineus, sartorius, quadriceps femoris (knee extension). Sensory: anterior thigh (anterior cutaneous branches) and medial leg/foot via the saphenous nerve (runs with the great saphenous vein below the knee)",
        "Injury (pelvic/hip surgery, retroperitoneal or psoas hematoma, femoral catheterization): knee buckles (weak extension), weak hip flexion, absent patellar reflex (L4), numb anterior thigh and medial leg. The saphenous nerve can be injured during great saphenous vein harvest."
    ),
    "obturator nerve": _af(
        "Peripheral Nerve — Lower Limb (L2–L4; lumbar plexus, anterior divisions)",
        "Runs along the lateral pelvic wall and leaves through the obturator canal to the medial thigh. Motor: adductor longus, adductor brevis, adductor part of adductor magnus, gracilis, obturator externus (hip adduction). Sensory: small area of the medial thigh",
        "Injury (pelvic surgery, anterior hip dislocation, pelvic tumors, obturator hernia): weak adduction — the leg swings outward when walking — and a numb medial thigh. Pelvic disease (ovary, obturator hernia) can refer pain to the medial thigh/knee (Howship-Romberg sign)."
    ),
    "tibial nerve": _af(
        "Peripheral Nerve — Lower Limb (L4–S3; medial terminal branch of the sciatic nerve)",
        "Runs vertically through the popliteal fossa, deep to gastrocnemius and soleus, then behind the medial malleolus through the tarsal tunnel, dividing into the medial and lateral plantar nerves. Motor: hamstrings (via the tibial division of the sciatic), posterior leg — gastrocnemius, soleus, plantaris, popliteus, tibialis posterior, FDL, FHL — and most foot intrinsics. Sensory: sole of the foot; contributes to the sural nerve (lateral foot)",
        "'TIP': Tibial nerve Inverts and Plantarflexes — injury → cannot stand on TIPtoes. Lesions (knee trauma, Baker cyst, tarsal tunnel syndrome): weak plantarflexion, inversion and toe flexion, numb sole, absent ankle reflex (S1)."
    ),
    "common peroneal nerve": _af(
        "Peripheral Nerve — Lower Limb (L4–S2; lateral terminal branch of the sciatic nerve; also called common fibular nerve)",
        "Follows the biceps femoris tendon along the lateral popliteal fossa, winds SUPERFICIALLY around the neck of the fibula and divides into: superficial fibular nerve — lateral compartment (fibularis longus + brevis → eversion) + sensation of most of the dorsum of the foot and lower lateral leg; deep fibular nerve — anterior compartment (tibialis anterior, EHL, EDL, fibularis tertius → dorsiflexion and toe extension) + extensor digitorum brevis + sensation of the first dorsal web space",
        "Most commonly injured nerve of the lower limb (fibular neck fracture, tight cast, leg crossing, prolonged squatting, knee dislocation) → foot drop with high-stepping 'steppage' gait, weak eversion, numb dorsum of foot/lateral leg. 'PED': Peroneal Everts and Dorsiflexes — injury → foot dropPED. An L5 radiculopathy also causes foot drop but adds weak INVERSION and hip abduction."
    ),
    "superior gluteal nerve": _af(
        "Peripheral Nerve — Gluteal Region (L4–S1; leaves the greater sciatic foramen ABOVE piriformis)",
        "Motor: gluteus medius, gluteus minimus and tensor fasciae latae — abduct the hip and keep the pelvis level when the opposite foot is lifted. Travels with the superior gluteal artery",
        "Injury (misplaced IM injection, hip surgery) → positive Trendelenburg sign: standing on the AFFECTED leg, the pelvis drops on the opposite side; waddling gait. Give gluteal injections in the superolateral quadrant (or the ventrogluteal site) to avoid this nerve and the sciatic nerve."
    ),
    "inferior gluteal nerve": _af(
        "Peripheral Nerve — Gluteal Region (L5–S2; leaves the greater sciatic foramen BELOW piriformis)",
        "Motor: gluteus maximus — powerful hip extension (rising from a chair, climbing stairs) and lateral rotation of the thigh",
        "Injury (posterior hip dislocation, surgery) → difficulty climbing stairs and rising from sitting; walking on level ground is largely preserved."
    ),
    "greater sciatic foramen": _af(
        "Gross Anatomy — gluteal region (greater sciatic notch closed by the sacrotuberous + sacrospinous ligaments)",
        "Piriformis passes through it and is the landmark. ABOVE piriformis: superior gluteal nerve, artery and vein. BELOW piriformis: inferior gluteal nerve and vessels, sciatic nerve, posterior femoral cutaneous nerve, pudendal nerve with internal pudendal vessels, nerve to obturator internus, nerve to quadratus femoris. Lesser sciatic foramen: obturator internus tendon, pudendal nerve and internal pudendal vessels re-entering the perineum (pudendal canal)",
        "Piriformis syndrome: the sciatic nerve (which passes through piriformis in ~10–15% of people) is compressed → buttock pain radiating down the back of the thigh. Pudendal nerve block is given at the ischial spine, where the nerve crosses the sacrospinous ligament."
    ),
    "hip joint": _af(
        "Joint — Hip (ball-and-socket synovial joint; very stable)",
        "Acetabulum (ilium + ischium + pubis, joined at the Y-shaped triradiate cartilage) deepened by the labrum. Iliofemoral ligament (Y ligament of Bigelow — strongest ligament in the body) prevents hyperextension. Femoral head blood supply: mainly the medial circumflex femoral artery (retinacular branches along the neck), plus the small artery of the ligamentum teres (obturator artery — more important in children)",
        "Displaced femoral neck (intracapsular) fracture tears the retinacular vessels → avascular necrosis; the leg is shortened and externally rotated. Posterior hip dislocation (dashboard injury, >90%) → leg shortened, flexed, adducted and internally rotated; sciatic nerve at risk. Hip disease can refer pain to the knee (obturator nerve)."
    ),
    "thigh compartments": _af(
        "Musculoskeletal — fascial compartments of the thigh",
        "Anterior: quadriceps femoris (rectus femoris, vastus lateralis, medialis, intermedius), sartorius, distal iliopsoas — knee extension, hip flexion; femoral nerve. Medial: adductor longus, brevis, magnus, gracilis, obturator externus (+ pectineus) — hip adduction; obturator nerve. Posterior: hamstrings (semitendinosus, semimembranosus, long head of biceps femoris) — hip extension, knee flexion; tibial division of the sciatic nerve (short head of biceps femoris: common fibular division)",
        "Hamstring strains (sprinters) usually involve biceps femoris. Pes anserinus ('SGT': Sartorius — femoral n., Gracilis — obturator n., semiTendinosus — tibial n.) inserts on the medial proximal tibia; pes anserine bursitis causes medial knee pain."
    ),
    "adductor canal": _af(
        "Gross Anatomy — medial thigh (Hunter / subsartorial canal)",
        "Runs from the apex of the femoral triangle to the adductor hiatus in adductor magnus. Roof: sartorius; anterolateral wall: vastus medialis; posterior wall: adductor longus and magnus. Contents: femoral artery and vein, saphenous nerve, nerve to vastus medialis. At the adductor hiatus the femoral vessels become the popliteal vessels; the saphenous nerve does NOT pass through the hiatus",
        "Adductor canal block (saphenous nerve) gives analgesia after knee surgery with less quadriceps weakness than a femoral nerve block. Atherosclerosis of the femoral artery often narrows it at the adductor hiatus."
    ),
    "popliteal fossa": _af(
        "Gross Anatomy — diamond-shaped space behind the knee",
        "Borders: superolateral — biceps femoris; superomedial — semimembranosus + semitendinosus; inferolateral and inferomedial — lateral and medial heads of gastrocnemius. Contents superficial → deep: tibial nerve, popliteal vein, popliteal artery (deepest, on the femur — feel the pulse with the knee flexed); common fibular nerve along the lateral border; small saphenous vein joins the popliteal vein; popliteal lymph nodes",
        "The popliteal artery is the deepest structure → injured by supracondylar femur fractures and posterior knee dislocations (check distal pulses / ankle-brachial index). Baker (popliteal) cyst lies between medial gastrocnemius and semimembranosus; rupture mimics a DVT. Popliteal artery aneurysm is the most common peripheral aneurysm, often bilateral."
    ),
    "knee ligaments": _af(
        "Joint — Knee (modified hinge synovial joint)",
        "ACL: anterior intercondylar tibia → lateral femoral condyle; prevents anterior translation of the tibia (anterior drawer, Lachman). PCL: posterior intercondylar tibia → medial femoral condyle; prevents posterior translation (posterior drawer; 'dashboard' injury). MCL (tibial collateral): attached to the medial meniscus, resists valgus force. LCL (fibular collateral): separate from the lateral meniscus, resists varus force. Menisci: C-shaped medial (less mobile, more often torn chronically) and O-shaped lateral fibrocartilage. 'LAMP': Lateral condyle — ACL, Medial condyle — PCL",
        "'Unhappy triad' (lateral blow to a planted knee): ACL + MCL + meniscus tear (lateral meniscus tears are actually more common with acute ACL injury). ACL tear: non-contact pivot, audible pop, rapid hemarthrosis. Meniscal tear: joint-line tenderness, locking, positive McMurray test."
    ),
    "ankle ligaments": _af(
        "Joint — Ankle (talocrural hinge joint)",
        "Lateral ligament complex: anterior talofibular (ATFL — weakest, most often torn), calcaneofibular, posterior talofibular. Medial: deltoid ligament (strong, 4 parts) — the medial malleolus often fractures before it tears. The joint is most stable in dorsiflexion (the wider front of the talus is wedged into the mortise)",
        "Inversion sprain of a plantarflexed foot tears the ATFL first, then the calcaneofibular ligament. Ottawa ankle rules for X-ray: bone tenderness at the posterior edge/tip of either malleolus or inability to bear weight for 4 steps. 'High ankle sprain' = tibiofibular syndesmosis injury."
    ),
    "leg compartments": _af(
        "Musculoskeletal — fascial compartments of the leg",
        "Anterior: tibialis anterior, EHL, EDL, fibularis tertius — dorsiflexion and toe extension; deep fibular nerve + anterior tibial artery. Lateral: fibularis longus and brevis — eversion; superficial fibular nerve (blood from fibular artery branches). Superficial posterior: gastrocnemius, soleus, plantaris — plantarflexion; tibial nerve. Deep posterior: tibialis posterior, FDL, FHL, popliteus — plantarflexion, inversion, toe flexion; tibial nerve + posterior tibial and fibular arteries",
        "Compartment syndrome (tibial fracture, crush, reperfusion) most often hits the anterior compartment: pain out of proportion and on passive stretch (plantarflexing the toes), then numbness of the first web space (deep fibular nerve); pulses are often still present. Treat with urgent fasciotomy of all four compartments."
    ),
    "tarsal tunnel": _af(
        "Fibro-osseous Tunnel — behind the medial malleolus (roof: flexor retinaculum)",
        "Contents anterior → posterior: Tibialis posterior tendon, flexor Digitorum longus tendon, posterior tibial Artery and Veins, tibial Nerve, flexor Hallucis longus tendon ('Tom, Dick And Very Nervous Harry'). The posterior tibial pulse is felt here",
        "Tarsal tunnel syndrome: tibial nerve compression → burning and numbness of the sole, worse at night or after standing, positive Tinel sign behind the medial malleolus (the heel can be spared — calcaneal branches may leave above the tunnel)."
    ),
    "great saphenous vein": _af(
        "Superficial Vein — Lower Limb",
        "Begins at the medial end of the dorsal venous arch → passes ANTERIOR to the medial malleolus (constant site for venous cutdown) → ascends along the medial leg (with the saphenous nerve) and thigh → joins the femoral vein at the saphenous opening, ~3–4 cm inferolateral to the pubic tubercle. Small saphenous vein: behind the lateral malleolus with the sural nerve → popliteal vein",
        "Used for coronary artery bypass grafts (reversed so the valves do not block flow). Incompetent valves → varicose veins. Emergency IV access by cutdown anterior to the medial malleolus."
    ),
    # ── Thorax ────────────────────────────────────────────────────────────────
    "intercostal space": _af(
        "Thoracic Wall",
        "Three muscle layers: external intercostals (inspiration; fibers run like 'hands in pockets'), internal intercostals (forced expiration), innermost intercostals. The neurovascular bundle runs between the internal and innermost layers in the costal groove on the INFERIOR border of each rib, superior → inferior: Vein, Artery, Nerve (VAN)",
        "Thoracentesis and chest tubes go just ABOVE the upper border of the rib below, to avoid the bundle. Chest tube 'triangle of safety': 4th–5th intercostal space at the mid-axillary line (between pectoralis major, latissimus dorsi and the nipple line). Herpes zoster and intercostal nerve blocks follow an intercostal nerve."
    ),
    "pleura": _af(
        "Thorax — serous membranes of the lungs",
        "Visceral pleura covers the lung (autonomic supply — insensitive to pain). Parietal pleura lines the chest wall, diaphragm and mediastinum (somatic: intercostal nerves for the costal part; phrenic nerve for the mediastinal and central diaphragmatic parts → pain referred to the shoulder). Lower borders at the midclavicular / mid-axillary / paravertebral lines: lung ribs 6–8–10, pleura ribs 8–10–12. Costodiaphragmatic recess: lowest part of the pleural cavity, where fluid collects. Cervical pleura (cupula) rises 2–3 cm above the medial clavicle",
        "Thoracentesis: posteriorly, 1–2 intercostal spaces below the top of the effusion but not below the 9th rib (liver/spleen), needle just above a rib. The cupula can be punctured during subclavian lines or supraclavicular blocks → pneumothorax."
    ),
    "pericardium": _af(
        "Thorax — middle mediastinum",
        "Fibrous pericardium (tough, fused to the central tendon of the diaphragm) + serous pericardium (parietal layer lining the fibrous layer; visceral layer = epicardium). The pericardial cavity between them holds ~15–50 mL of fluid. Transverse pericardial sinus: behind the aorta and pulmonary trunk, in front of the SVC and atria — used to clamp the great arteries in cardiac surgery. Oblique sinus: behind the left atrium, bounded by the pulmonary veins and IVC. Innervation: phrenic nerves (C3–C5, somatic)",
        "Pericarditis pain is sharp, worse lying flat, better leaning forward, and can radiate to the trapezius ridge (phrenic). Pericardiocentesis: subxiphoid approach, needle aimed at the left shoulder. Tamponade → Beck triad."
    ),
    "heart surfaces": _af(
        "Cardiac Anatomy — orientation in the chest and on chest X-ray",
        "Apex: left ventricle, 5th intercostal space at the midclavicular line. Anterior (sternocostal) surface: mostly the right ventricle. Inferior (diaphragmatic) surface: mostly the LV with some RV. Posterior surface (base): mostly the left atrium. Right border on CXR: right atrium (SVC above). Left border: aortic knob, pulmonary trunk, left auricle, left ventricle. Coronary sulcus = atrioventricular groove; the interventricular grooves carry the LAD (anterior) and PDA (posterior)",
        "The left atrium is the most posterior chamber, lying on the esophagus → an enlarged LA (mitral stenosis) can cause dysphagia or hoarseness (Ortner syndrome — left recurrent laryngeal nerve); transesophageal echo views it best. The right ventricle is most anterior → most often injured by anterior stab wounds."
    ),
    "phrenic nerve": _af(
        "Peripheral Nerve — Neck/Thorax (C3–C5; 'C3, 4, 5 keeps the diaphragm alive')",
        "Forms in the neck on the anterior surface of anterior scalene, enters the thorax between the subclavian artery and vein, and descends ANTERIOR to the lung root in the middle mediastinum (between fibrous pericardium and mediastinal pleura) with the pericardiacophrenic vessels. Motor: the only motor supply of its hemidiaphragm. Sensory: central diaphragmatic pleura and peritoneum, mediastinal pleura, pericardium",
        "Diaphragmatic irritation (subphrenic abscess, gallbladder, splenic rupture, blood) refers pain to the shoulder tip (C4 dermatome — Kehr sign on the left). Injury (cardiac surgery, tumor, interscalene block) → paralyzed, elevated hemidiaphragm with paradoxical movement on the sniff test. Cord injury above C3–C5 requires ventilation."
    ),
    "vagus nerve": _af(
        "Cranial Nerve X — mixed; parasympathetic supply to thoracic and abdominal viscera",
        "Leaves the skull through the jugular foramen and runs in the carotid sheath (posterior, between the carotid artery and internal jugular vein). Branches: pharyngeal (most pharyngeal and palatal muscles except stylopharyngeus [IX] and tensor veli palatini [V3]); superior laryngeal (internal — sensation above the vocal folds; external — cricothyroid); recurrent laryngeal (other intrinsic laryngeal muscles, sensation below the folds); cardiac, pulmonary and esophageal plexuses → anterior (left) and posterior (right) vagal trunks through the esophageal hiatus (T10) ('LARP'). Gut parasympathetic supply reaches the proximal 2/3 of the transverse colon",
        "Lesion: uvula deviates AWAY from the lesion, hoarseness, dysphagia, absent gag reflex on that side (efferent limb). Carotid sinus massage / Valsalva → ↑vagal tone → slows the SA and AV nodes (terminates some SVTs)."
    ),
    "recurrent laryngeal nerve": _af(
        "Peripheral Nerve — branch of the vagus (CN X)",
        "Right RLN hooks under the right subclavian artery; left RLN hooks under the aortic arch beside the ligamentum arteriosum (longer course). Both ascend in the tracheoesophageal groove, close to the inferior thyroid artery, and enter the larynx behind the cricothyroid joint. Supply all intrinsic laryngeal muscles except cricothyroid — including posterior cricoarytenoid, the ONLY abductor of the vocal folds — and sensation below the vocal folds",
        "Injury → hoarseness (unilateral) or stridor/airway obstruction (bilateral — folds stuck near the midline). Causes: thyroid surgery (RLN near the inferior thyroid artery; the external laryngeal nerve runs with the superior thyroid artery → weak, monotone high pitch), aortic arch aneurysm, left atrial enlargement (Ortner), apical lung tumor (Pancoast, right), left hilar/mediastinal nodes and lung cancer (left is affected more often — longer course)."
    ),
    "thoracic duct": _af(
        "Lymphatic — largest lymph vessel",
        "Begins at the cisterna chyli (L1–L2), passes through the aortic hiatus (T12) with the aorta and azygos vein, ascends in the posterior mediastinum between the aorta and azygos vein (behind the esophagus), crosses to the left at ~T4–T6, and drains into the left venous angle (junction of the left subclavian and internal jugular veins). Drains everything except the right head/neck, right upper limb and right thorax (right lymphatic duct)",
        "Injury (esophagectomy, thoracic surgery, trauma, lymphoma) → chylothorax: milky pleural fluid with triglycerides >110 mg/dL. Abdominal cancers spread up this route to the left supraclavicular (Virchow) node."
    ),
    "azygos vein": _af(
        "Venous — posterior mediastinum",
        "Arises from the ascending lumbar/subcostal veins, enters the thorax through the aortic hiatus (or right crus), ascends to the right of the vertebral bodies, and arches over the root of the right lung at T4 to drain into the SVC. Receives the right posterior intercostal veins, the hemiazygos and accessory hemiazygos veins (left side, crossing at ~T7–T9), and esophageal and bronchial veins",
        "Main collateral route between the IVC and SVC when either is blocked. Esophageal veins draining to the azygos anastomose with the left gastric (portal) vein → esophageal varices in portal hypertension. Azygos lobe of the right lung is a normal variant."
    ),
    "sternal angle": _af(
        "Surface Anatomy — angle of Louis (manubriosternal joint)",
        "Level of the 2nd costal cartilage (count ribs from here) and the T4/T5 intervertebral disc. The transverse thoracic plane through it marks: superior/inferior mediastinum boundary, start and end of the aortic arch, tracheal bifurcation (carina), azygos vein joining the SVC, left recurrent laryngeal nerve hooking under the arch, pulmonary trunk bifurcation, thoracic duct crossing to the left ('RATPLANT': Rib 2, Aortic arch, Trachea, Pulmonary trunk, Ligamentum arteriosum, Azygos, Nerve, Thoracic duct)",
        "Other landmarks: jugular notch T2/T3, xiphisternal joint T9, umbilicus L3/L4 disc (T10 dermatome), iliac crests L4 (lumbar puncture landmark)."
    ),
    "breast anatomy": _af(
        "Thoracic Wall — modified sweat gland over pectoralis major (ribs 2–6)",
        "Suspensory (Cooper) ligaments anchor the gland to the dermis. The axillary tail (of Spence) extends into the axilla. Lymph: ~75% to the axillary nodes (pectoral → central → apical); medial quadrants also to parasternal (internal thoracic) nodes; some crosses to the other breast and abdomen. Arteries: internal thoracic (perforating branches), lateral thoracic, thoracoacromial, posterior intercostal",
        "Cancer pulling on Cooper ligaments → skin dimpling; blocked dermal lymphatics → peau d'orange. Most cancers arise in the upper outer quadrant. Axillary dissection risks the long thoracic (winged scapula), thoracodorsal (latissimus dorsi) and intercostobrachial (numb medial arm) nerves."
    ),
    "aortic arch branches": _af(
        "Vascular — Thorax",
        "Ascending aorta: right and left coronary arteries. Arch, right → left: brachiocephalic trunk (→ right subclavian + right common carotid), left common carotid, left subclavian. Ligamentum arteriosum (ductus arteriosus remnant) joins the arch to the left pulmonary artery; the left recurrent laryngeal nerve hooks around it. Subclavian artery branches ('VIT C, D'): Vertebral, Internal thoracic, Thyrocervical trunk, Costocervical trunk, Dorsal scapular",
        "Common variant: 'bovine arch' (left common carotid from the brachiocephalic trunk). Subclavian steal: proximal subclavian stenosis → reversed flow in the vertebral artery → arm claudication + vertebrobasilar symptoms with arm use. Coarctation usually lies just beyond the left subclavian (near the ligamentum arteriosum) → rib notching from enlarged intercostal collaterals."
    ),
    # ── Abdomen ───────────────────────────────────────────────────────────────
    "peritoneum": _af(
        "Abdomen — serous membrane",
        "Parietal peritoneum: somatic nerves → sharp, well-localized pain. Visceral peritoneum: autonomic nerves → dull, poorly localized pain referred by embryologic origin (foregut — epigastric, midgut — periumbilical, hindgut — hypogastric). Intraperitoneal organs have a mesentery: stomach, 1st 2 cm of duodenum, jejunum, ileum, cecum/appendix, transverse and sigmoid colon, liver, spleen, tail of pancreas. Retroperitoneal — 'SAD PUCKER': Suprarenal glands, Aorta/IVC, Duodenum (parts 2–4), Pancreas (except tail), Ureters, Colon (ascending + descending), Kidneys, Esophagus (abdominal), Rectum (lower part)",
        "Appendicitis pain starts periumbilical (visceral, T10) and moves to the RLQ once the parietal peritoneum is inflamed (McBurney point). Retroperitoneal bleeding can be clinically silent (Grey Turner sign)."
    ),
    "lesser sac": _af(
        "Abdomen — omental bursa",
        "Space behind the stomach and lesser omentum, in front of the pancreas. Opens into the greater sac through the epiploic foramen (of Winslow): anterior — hepatoduodenal ligament (portal vein posterior, common bile duct to the right, hepatic artery to the left); posterior — IVC; superior — caudate lobe of the liver; inferior — 1st part of the duodenum. Lesser omentum = hepatogastric + hepatoduodenal ligaments; the greater omentum hangs from the greater curvature",
        "Pringle maneuver: squeeze the hepatoduodenal ligament through the epiploic foramen to control liver bleeding (hepatic artery + portal vein). Posterior gastric ulcers perforate into the lesser sac or erode the splenic artery; pancreatic pseudocysts often collect here."
    ),
    "celiac trunk": _af(
        "Vascular — foregut artery (from the aorta at T12)",
        "Three branches: left gastric (lesser curvature + esophageal branches); splenic (tortuous along the upper pancreas → short gastrics, left gastroepiploic, pancreatic branches); common hepatic (→ proper hepatic [right + left hepatic, right gastric; the cystic artery usually comes from the right hepatic] and gastroduodenal [→ right gastroepiploic, superior pancreaticoduodenal]). Supplies the foregut: lower esophagus → 2nd part of the duodenum (to the major papilla), liver, gallbladder, part of the pancreas; also the spleen (mesoderm, not gut-derived)",
        "Posterior duodenal ulcer → gastroduodenal artery bleed; posterior gastric ulcer → left gastric or splenic artery bleed. Short gastric arteries anastomose poorly → fundus is vulnerable if the splenic artery is blocked. Median arcuate ligament syndrome: celiac trunk compression → post-meal pain and weight loss."
    ),
    "superior mesenteric artery": _af(
        "Vascular — midgut artery (from the aorta at L1)",
        "Runs behind the neck of the pancreas, then in front of the 3rd part of the duodenum and the left renal vein. Branches: inferior pancreaticoduodenal, jejunal and ileal arteries (arcades + vasa recta), ileocolic (→ appendicular), right colic, middle colic. Supplies the midgut: duodenum beyond the major papilla → proximal 2/3 of the transverse colon",
        "Acute mesenteric ischemia (embolus from atrial fibrillation lodging in the SMA): pain out of proportion to the exam. SMA syndrome: 3rd part of the duodenum squeezed between the SMA and aorta (rapid weight loss) → intermittent obstruction. Nutcracker syndrome: left renal vein squeezed between SMA and aorta → hematuria, left varicocele."
    ),
    "inferior mesenteric artery": _af(
        "Vascular — hindgut artery (from the aorta at L3)",
        "Branches: left colic, sigmoid arteries, superior rectal artery. Supplies the hindgut: distal 1/3 of the transverse colon → upper rectum (above the pectinate line). The marginal artery (of Drummond) links SMA and IMA territories along the colon. The inferior mesenteric vein drains into the splenic vein (or SMV)",
        "Watershed areas prone to ischemic colitis: splenic flexure (SMA/IMA border) and rectosigmoid junction (IMA/internal iliac border). AAA repair can sacrifice the IMA → sigmoid ischemia if collaterals are poor."
    ),
    "abdominal aorta branches": _af(
        "Vascular — Abdomen",
        "Enters at T12 (aortic hiatus) and bifurcates at L4 (about the level of the umbilicus) into the common iliac arteries. Unpaired anterior: celiac trunk (T12), SMA (L1), IMA (L3). Paired lateral: inferior phrenic (T12), middle suprarenal (L1), renal (L1–L2), gonadal (L2). Posterior: lumbar arteries (L1–L4), median sacral",
        "AAA: usually below the renal arteries; ruptured → hypotension + back/flank pain + pulsatile mass. The left gonadal vein drains into the left renal vein (right → IVC), so varicoceles are more common on the left, and a new left varicocele can signal a left renal tumor."
    ),
    "hepatocystic triangle": _af(
        "Gross Anatomy — biliary (triangle of Calot)",
        "Borders: cystic duct (lateral), common hepatic duct (medial), inferior surface of the liver (superior). Contents: cystic artery (usually from the right hepatic artery), cystic lymph node (of Lund), often the right hepatic artery itself",
        "During cholecystectomy the 'critical view of safety' — only two structures, the cystic duct and cystic artery, entering the gallbladder — is obtained here to avoid cutting the common bile duct or right hepatic artery."
    ),
    "biliary tree": _af(
        "Gastrointestinal — bile ducts and gallbladder",
        "Right + left hepatic ducts → common hepatic duct; + cystic duct (spiral valves of Heister) → common bile duct (CBD). The CBD runs behind the 1st part of the duodenum and through the head of the pancreas, joins the main pancreatic duct at the hepatopancreatic ampulla (of Vater) and opens at the major duodenal papilla (2nd part of the duodenum), controlled by the sphincter of Oddi. Gallbladder: fundus, body, neck; fundus surface marking = tip of the right 9th costal cartilage (midclavicular line)",
        "Stone in the cystic duct → biliary colic / cholecystitis (no jaundice); in the CBD → obstructive jaundice ± cholangitis (Charcot triad); at the ampulla → gallstone pancreatitis. Gallbladder pain refers to the right shoulder/scapula. Hartmann pouch: bulge at the neck where stones lodge."
    ),
    "duodenum": _af(
        "Gastrointestinal — C-shaped first part of the small intestine (~25 cm)",
        "1st (superior) part: first 2 cm intraperitoneal (duodenal bulb/cap), rest retroperitoneal; the gastroduodenal artery lies behind it. 2nd (descending): major papilla (CBD + pancreatic duct) and minor papilla; foregut/midgut boundary. 3rd (horizontal): crosses between the SMA (in front) and aorta/IVC (behind) at L3. 4th (ascending): ends at the duodenojejunal flexure, held by the suspensory ligament (of Treitz)",
        "Most duodenal ulcers are in the 1st part: anterior ulcers perforate (free air), posterior ulcers bleed (gastroduodenal artery). The ligament of Treitz separates upper from lower GI bleeding. Duodenal atresia (trisomy 21) → 'double bubble' and bilious vomiting."
    ),
    "spleen": _af(
        "Abdomen — LUQ lymphoid organ (intraperitoneal; mesoderm, not gut)",
        "Lies under ribs 9–11 in the left mid-axillary line ('odd numbers': 1 × 3 × 5 inches, ~7 oz, ribs 9–11). Ligaments: gastrosplenic (short gastric + left gastroepiploic vessels) and splenorenal (splenic vessels + tail of pancreas). Splenic artery from the celiac trunk; the splenic vein joins the SMV behind the neck of the pancreas to form the portal vein. Red pulp filters old RBCs; white pulp = periarteriolar lymphoid sheath (T cells) + follicles (B cells)",
        "Most commonly injured organ in blunt abdominal trauma (rib 9–11 fractures) → LUQ pain + left shoulder pain (Kehr sign). After splenectomy: risk from encapsulated organisms (S. pneumoniae, H. influenzae, N. meningitidis) — vaccinate; Howell-Jolly bodies on smear. The tail of the pancreas can be injured during splenectomy."
    ),
    "kidney anatomy": _af(
        "Renal Anatomy — retroperitoneal, T12–L3 (right kidney sits lower because of the liver)",
        "Hilum (L1) structures anterior → posterior: renal Vein, renal Artery, Pelvis ('VAP'). Coverings inside → out: fibrous capsule, perirenal fat, renal (Gerota) fascia, pararenal fat. Posterior relations: diaphragm, psoas major, quadratus lumborum, 12th rib, subcostal/iliohypogastric/ilioinguinal nerves. The left renal vein is longer, passes between the SMA and aorta, and receives the left gonadal and left suprarenal veins. Arteries: renal → segmental → interlobar → arcuate → interlobular (cortical radiate) → afferent arteriole",
        "Horseshoe kidney: lower poles fuse and ascent is trapped under the IMA (Turner syndrome). The left kidney is preferred for living donation (longer renal vein). Kidney stones lodge at the narrowings of the ureter."
    ),
    "ureter": _af(
        "Urinary — retroperitoneal muscular tube (~25 cm), kidney → bladder",
        "Descends on psoas major, crosses the pelvic brim in front of the bifurcation of the common iliac artery, runs along the lateral pelvic wall, then passes UNDER the uterine artery (female) or the ductus deferens (male) before entering the bladder obliquely (a valve-like course). Three narrowings where stones lodge: ureteropelvic junction, pelvic brim (iliac vessels), ureterovesical junction (narrowest — most common)",
        "'Water (ureter) under the bridge (uterine artery / vas deferens)': at risk of being clamped or cut in hysterectomy (uterine vessels, infundibulopelvic ligament). Renal colic: loin-to-groin pain (T11–L2). On a plain X-ray (KUB) the ureter runs along the tips of the lumbar transverse processes."
    ),
    "adrenal gland": _af(
        "Endocrine — retroperitoneal, on the upper pole of each kidney (inside the renal fascia)",
        "Cortex (mesoderm) — 'GFR' makes 'salt, sugar, sex': zona Glomerulosa → aldosterone (RAAS), zona Fasciculata → cortisol (ACTH), zona Reticularis → androgens (DHEA). Medulla (neural crest) — chromaffin cells → epinephrine/norepinephrine; innervated directly by PREganglionic sympathetic fibers (thoracic splanchnic nerves). Arteries: superior (from inferior phrenic), middle (aorta), inferior (renal) suprarenal. Veins: right → IVC directly (very short); left → left renal vein",
        "The short right adrenal vein makes right adrenalectomy harder (IVC injury). Adrenal vein sampling localizes an aldosterone-producing adenoma. Medullary tumors: pheochromocytoma (adults), neuroblastoma (children)."
    ),
    "abdominal wall": _af(
        "Gross Anatomy — layers of the anterolateral abdominal wall",
        "Skin → superficial fascia (fatty Camper + membranous Scarpa) → external oblique (fibers 'hands in pockets'; aponeurosis forms the inguinal ligament) → internal oblique → transversus abdominis → transversalis fascia → extraperitoneal fat → parietal peritoneum. Rectus abdominis lies in the rectus sheath, the two separated by the linea alba. Nerves: thoracoabdominal T7–T11, subcostal (T12), iliohypogastric + ilioinguinal (L1) running between internal oblique and transversus abdominis",
        "Scarpa fascia continues as Colles fascia of the perineum → a ruptured spongy (penile) urethra leaks urine into the scrotum, penis and lower abdominal wall but not the thighs. Ilioinguinal nerve injury in appendectomy or hernia repair → numb anterior scrotum/labium and a weaker inguinal region."
    ),
    "rectus sheath": _af(
        "Abdominal Wall — aponeurotic sheath around rectus abdominis",
        "Above the arcuate line (about 1/3 of the way from the umbilicus to the pubis): anterior layer = external oblique + anterior half of the internal oblique aponeurosis; posterior layer = posterior half of the internal oblique + transversus abdominis aponeurosis. Below the arcuate line: ALL aponeuroses pass in front; behind the muscle there is only transversalis fascia. Contents: rectus abdominis, pyramidalis, superior + inferior epigastric vessels, T7–T12 nerves",
        "Rectus sheath hematoma (anticoagulation, coughing) usually comes from the inferior epigastric artery below the arcuate line → painful abdominal-wall mass that does not cross the midline and persists when the rectus is tensed (Fothergill sign). The inferior epigastric vessels separate direct (medial) from indirect (lateral) inguinal hernias."
    ),
    "umbilical folds": _af(
        "Abdominal Wall — peritoneal folds on the inner anterior wall",
        "Median umbilical fold: urachus remnant (median umbilical ligament; from the allantois). Medial umbilical folds (paired): obliterated umbilical arteries (medial umbilical ligaments). Lateral umbilical folds (paired): inferior epigastric vessels. Above the umbilicus, the falciform ligament carries the ligamentum teres hepatis (obliterated umbilical vein). Fossae: supravesical, medial inguinal (direct hernia — Hesselbach triangle), lateral inguinal (indirect hernia — deep ring)",
        "Patent urachus → urine leaking from the umbilicus; urachal cyst/sinus; urachal adenocarcinoma at the bladder dome. Patent vitelline duct → meconium from the umbilicus (Meckel diverticulum is its partial remnant)."
    ),
    "appendix": _af(
        "Gastrointestinal — vermiform appendix (posteromedial cecum)",
        "Its base is constant — where the three taeniae coli meet on the cecum; surface marking = McBurney point (1/3 of the way from the right ASIS to the umbilicus). The tip position varies: retrocecal (most common, ~65%), pelvic, subcecal, pre-/post-ileal. The appendicular artery (ileocolic branch of the SMA) runs in the mesoappendix and is an end artery. Visceral afferents enter at T10 (periumbilical pain)",
        "Appendicitis: periumbilical pain (visceral, T10) moving to the RLQ (parietal peritoneum). Retrocecal → psoas sign; pelvic → obturator sign and urinary/rectal symptoms. Because the appendicular artery is an end artery, obstruction quickly leads to gangrene and perforation."
    ),
    "pectinate line": _af(
        "Anal Canal — dentate line (junction of hindgut endoderm and ectoderm)",
        "ABOVE the line (endoderm): columnar epithelium; superior rectal artery (IMA); superior rectal vein → IMV → portal system; lymph → internal iliac nodes; visceral nerves (pain-insensitive). BELOW the line (ectoderm): stratified squamous epithelium; inferior rectal artery (internal pudendal); inferior rectal vein → internal pudendal → internal iliac → IVC (systemic); lymph → superficial inguinal nodes; somatic nerve — inferior rectal branch of the pudendal nerve (painful)",
        "Internal hemorrhoids (above): painless bleeding. External hemorrhoids (below): painful, especially when thrombosed. Anal fissure: below the line, usually posterior midline, very painful. Adenocarcinoma above, squamous cell carcinoma below. Portosystemic anastomosis: superior vs middle/inferior rectal veins."
    ),
    # ── Pelvis & Perineum ─────────────────────────────────────────────────────
    "pelvic floor": _af(
        "Pelvis — pelvic diaphragm",
        "Levator ani (pubococcygeus, puborectalis, iliococcygeus) + coccygeus. Nerves: nerve to levator ani (S3–S4) and the pudendal nerve (S2–S4). Supports the pelvic organs; puborectalis slings around the anorectal junction (anorectal angle — fecal continence). Perineal body: central tendon where the perineal muscles converge",
        "Stretching or tearing in vaginal delivery → pelvic organ prolapse and stress urinary incontinence. Mediolateral episiotomy avoids the perineal body and anal sphincter (a midline cut can extend into the anus)."
    ),
    "pudendal nerve": _af(
        "Peripheral Nerve — Perineum (S2–S4; sacral plexus)",
        "Leaves the pelvis through the greater sciatic foramen below piriformis, hooks around the ischial spine / sacrospinous ligament, re-enters through the lesser sciatic foramen and runs in the pudendal (Alcock) canal with the internal pudendal vessels. Branches: inferior rectal (external anal sphincter, perianal skin), perineal (perineal muscles, external urethral sphincter, scrotum/labia), dorsal nerve of the penis/clitoris",
        "Pudendal block: injection beside the ischial spine (transvaginal) for labor and perineal repair. Injury (prolonged cycling, childbirth) → perineal numbness, fecal/urinary incontinence, sexual dysfunction. Provides the painful sensation below the pectinate line."
    ),
    "pelvic splanchnic nerves": _af(
        "Autonomic — parasympathetic outflow S2–S4 (nervi erigentes)",
        "Preganglionic parasympathetic fibers from S2–S4 → inferior hypogastric plexus → hindgut (distal 1/3 of transverse colon → rectum), bladder (detrusor contraction — voiding) and erectile tissue (erection). Sympathetic (lumbar splanchnics, T11–L2 → hypogastric nerves): emission, internal urethral sphincter contraction. Somatic (pudendal nerve): external sphincters and ejaculation (bulbospongiosus)",
        "'Point, Squeeze and Shoot': Parasympathetic — erection; Sympathetic — emission; Somatic — ejaculation. Radical prostatectomy or rectal surgery can damage the cavernous nerves → erectile dysfunction. Sacral cord injury → flaccid, overflowing bladder."
    ),
    "uterine ligaments": _af(
        "Female Pelvis — supports of the uterus and ovaries",
        "Suspensory ligament of the ovary (infundibulopelvic): carries the ovarian artery and vein to the lateral pelvic wall. Ovarian ligament: ovary → uterine horn. Round ligament of the uterus: uterine horn → through the inguinal canal → labium majus (gubernaculum remnant). Cardinal (transverse cervical) ligament: cervix → lateral pelvic wall, carries the uterine vessels — main support. Uterosacral ligament: cervix → sacrum. Broad ligament: peritoneal fold (mesometrium, mesosalpinx, mesovarium) containing the uterine tube, round ligament and uterine/ovarian vessels",
        "The ureter passes under the uterine artery beside the cervix and close to the infundibulopelvic ligament → at risk in hysterectomy and oophorectomy. Ovarian torsion twists the suspensory ligament and its vessels. Round ligament pain in pregnancy: sharp groin pain."
    ),
    "prostate gland": _af(
        "Male Pelvis — fibromuscular gland around the prostatic urethra",
        "Zones: peripheral (~70% of glandular tissue, posterior/lateral — felt on digital rectal exam), central (around the ejaculatory ducts), transition (around the urethra), anterior fibromuscular stroma. The ejaculatory ducts (ductus deferens + seminal vesicle) open into the prostatic urethra at the seminal colliculus (verumontanum). The prostatic venous plexus drains to the internal iliac veins and the vertebral (Batson) venous plexus",
        "BPH arises in the transition (periurethral) zone → urinary obstruction, often not felt on DRE. Prostate cancer usually arises in the peripheral zone → hard nodule on DRE; spreads to the lumbar spine through Batson plexus (osteoblastic metastases)."
    ),
    "male urethra": _af(
        "Male Pelvis/Perineum — ~20 cm, four parts",
        "Preprostatic (bladder neck; internal urethral sphincter — sympathetic), prostatic (widest; ejaculatory and prostatic ducts open here), membranous (shortest, narrowest, least distensible — passes through the deep perineal pouch with the external urethral sphincter), spongy/penile (in the corpus spongiosum; bulbourethral gland ducts; navicular fossa)",
        "Pelvic fracture → posterior (membranous) urethral tear: blood at the meatus, high-riding prostate, urine in the retropubic space — do not pass a catheter before a retrograde urethrogram. Straddle injury → anterior (bulbar) urethra: urine tracks deep to Colles/Scarpa fascia into the scrotum, penis and lower abdominal wall."
    ),
    "rectouterine pouch": _af(
        "Female Pelvis — pouch of Douglas",
        "Lowest part of the peritoneal cavity in an upright woman, between the rectum and the back of the uterus/posterior vaginal fornix. The vesicouterine pouch lies in front of the uterus. In males the lowest point is the rectovesical pouch",
        "Fluid, blood (ruptured ectopic pregnancy), pus and metastases (Blumer shelf) collect here. Culdocentesis: needle through the posterior vaginal fornix. Endometriosis implants often sit here (painful defecation, deep dyspareunia)."
    ),
    "internal iliac artery": _af(
        "Vascular — Pelvis",
        "Arises at the pelvic brim (L5/S1). Anterior division: umbilical (→ superior vesical; the rest becomes the medial umbilical ligament), obturator, inferior vesical (male) / vaginal and uterine (female), middle rectal, internal pudendal, inferior gluteal. Posterior division: iliolumbar, lateral sacral, superior gluteal (largest branch). The external iliac artery becomes the femoral artery under the inguinal ligament (branches: inferior epigastric, deep circumflex iliac)",
        "Ligating or embolizing the anterior division controls severe postpartum or pelvic-fracture bleeding; rich collaterals keep the pelvis alive. 'Corona mortis': an obturator–external iliac (or inferior epigastric) anastomosis over the superior pubic ramus — bleeding risk in hernia and pelvic surgery."
    ),
    # ── Head & Neck ───────────────────────────────────────────────────────────
    "facial nerve": _af(
        "Cranial Nerve VII — mixed (2nd pharyngeal arch)",
        "Leaves the brainstem at the cerebellopontine angle → internal acoustic meatus → facial canal: geniculate ganglion (greater petrosal nerve → lacrimal, nasal and palatine glands), nerve to stapedius, chorda tympani (taste to the anterior 2/3 of the tongue; submandibular + sublingual glands via the lingual nerve) → exits the stylomastoid foramen → posterior auricular nerve → divides inside the parotid gland into 5 motor branches: Temporal, Zygomatic, Buccal, Marginal mandibular, Cervical ('To Zanzibar By Motor Car')",
        "UMN lesion (stroke): weak contralateral LOWER face, forehead spared. LMN lesion (Bell palsy): whole ipsilateral face including the forehead, ± hyperacusis (stapedius), loss of taste and dry eye depending on the level. The parotid's own secretomotor supply is CN IX, not VII. The marginal mandibular branch is at risk in submandibular surgery (drooping corner of the mouth)."
    ),
    "trigeminal nerve": _af(
        "Cranial Nerve V — 1st pharyngeal arch",
        "V1 ophthalmic (superior orbital fissure; sensory — forehead, upper eyelid, cornea, dorsum and tip of the nose). V2 maxillary (foramen rotundum; sensory — cheek, upper lip, upper teeth, palate). V3 mandibular (foramen ovale; sensory — lower face, lower lip, lower teeth, general sensation of the anterior 2/3 of the tongue via the lingual nerve; motor — muscles of mastication [masseter, temporalis, medial + lateral pterygoids], mylohyoid, anterior belly of digastric, tensor tympani, tensor veli palatini). Exits: 'Standing Room Only' = Superior orbital fissure, Rotundum, Ovale",
        "Corneal reflex: afferent V1, efferent VII. Jaw jerk: V3 both ways. The jaw deviates TOWARD the side of a V3 lesion (the opposite lateral pterygoid is unopposed). Trigeminal neuralgia: brief electric pain, usually V2/V3 — carbamazepine."
    ),
    "cavernous sinus": _af(
        "Dural Venous Sinus — either side of the sella turcica",
        "In the lateral wall (superior → inferior): CN III, CN IV, V1, V2. Inside the sinus itself: internal carotid artery (with its sympathetic plexus) and CN VI (most medial — most vulnerable). Receives the superior and inferior ophthalmic veins; drains to the petrosal sinuses. V3 is NOT in the sinus (it leaves through the foramen ovale below)",
        "Cavernous sinus thrombosis (spread from 'danger triangle' facial infections via the ophthalmic veins, or sinusitis): fever, proptosis, chemosis, ophthalmoplegia (CN VI first → lateral gaze palsy), V1/V2 numbness. Carotid-cavernous fistula: pulsating proptosis + bruit. Pituitary adenomas can grow sideways into it."
    ),
    "scalp layers": _af(
        "Head — five layers ('SCALP')",
        "Skin; Connective tissue (dense — its vessels cannot constrict when cut → heavy bleeding); Aponeurosis (galea aponeurotica, joining frontalis and occipitalis); Loose areolar tissue ('danger layer' — emissary veins connect it to the dural venous sinuses); Pericranium (periosteum)",
        "A scalp wound gapes when the galea is cut (frontalis and occipitalis pull the edges apart). Infection in the loose areolar layer can spread to the dural sinuses through emissary veins. Newborns: subgaleal hemorrhage (vacuum delivery) crosses suture lines; cephalohematoma (under the periosteum) does NOT."
    ),
    "pterion": _af(
        "Skull Landmark — H-shaped junction of the frontal, parietal, temporal (squamous) and sphenoid (greater wing) bones",
        "About two finger-breadths above the zygomatic arch and a thumb's breadth behind the frontal process of the zygomatic bone. Thinnest part of the lateral skull; the anterior branch of the middle meningeal artery runs just beneath it",
        "A blow to the side of the head fractures the pterion and tears the middle meningeal artery → epidural hematoma: lucid interval, then rapid decline; biconvex (lens-shaped) bleed on CT that does NOT cross sutures. Needs urgent surgical evacuation."
    ),
    "middle meningeal artery": _af(
        "Vascular — Head (branch of the maxillary artery, from the external carotid)",
        "Enters the skull through the foramen spinosum and runs outside the dura, grooving the inner skull; its anterior branch passes under the pterion. Supplies the dura and calvaria. Accompanied by the meningeal branch of V3",
        "Epidural hematoma: arterial, lucid interval, biconvex on CT, limited by sutures — usually after a temporal bone fracture. Compare subdural hematoma (torn bridging veins): crescent-shaped, crosses sutures — elderly, alcohol use, shaken infants."
    ),
    "dural venous sinuses": _af(
        "Head — venous channels between the periosteal and meningeal layers of dura",
        "Superior sagittal sinus (upper edge of the falx cerebri; arachnoid granulations return CSF to it) → confluence of sinuses → transverse sinuses → sigmoid sinuses → internal jugular vein (jugular foramen). Inferior sagittal sinus + great cerebral vein (of Galen) → straight sinus → confluence. Cavernous sinus → superior and inferior petrosal sinuses. Bridging (superior cerebral) veins cross the subdural space into the superior sagittal sinus",
        "Torn bridging veins → subdural hematoma (crescent, crosses sutures). Cerebral venous sinus thrombosis (pregnancy, OCPs, dehydration, thrombophilia): headache, papilledema, seizures; 'empty delta sign' on contrast CT."
    ),
    "neck triangles": _af(
        "Gross Anatomy — Neck (anterior and posterior triangles, divided by sternocleidomastoid)",
        "Anterior triangle: SCM (posterior), midline (anterior), mandible (superior); subdivided into submandibular, submental, carotid (carotid bifurcation, internal jugular vein, vagus, hypoglossal nerve, ansa cervicalis) and muscular triangles. Posterior triangle: SCM (anterior), trapezius (posterior), middle 1/3 of the clavicle (inferior); contains the spinal accessory nerve (CN XI), cutaneous branches of the cervical plexus (emerging at Erb point, mid-posterior border of SCM), trunks of the brachial plexus, 3rd part of the subclavian artery, external jugular vein, inferior belly of omohyoid",
        "CN XI runs superficially across the posterior triangle → injured in lymph node biopsy → trapezius weakness (shoulder droops, weak shrug, lateral scapular winging). The carotid triangle is where the carotid pulse is felt and carotid endarterectomy is done."
    ),
    "carotid sheath": _af(
        "Neck — fascial tube from the skull base to the aortic arch",
        "Contents: common/internal carotid artery (medial), internal jugular vein (lateral), vagus nerve (posterior, between them), deep cervical lymph nodes; ansa cervicalis lies in its anterior wall and the sympathetic trunk behind it. The common carotid bifurcates at the upper border of the thyroid cartilage (C3–C4). Carotid sinus (baroreceptor) and carotid body (chemoreceptor) sit at the bifurcation — afferents in CN IX (and X)",
        "Carotid sinus massage → ↑vagal tone → can stop SVT; carotid sinus hypersensitivity → syncope with a tight collar or head turning. Internal jugular central line: lateral to the carotid pulse, at the apex of the triangle between the two heads of SCM."
    ),
    "external carotid artery": _af(
        "Vascular — Head & Neck",
        "Begins at the carotid bifurcation (upper border of the thyroid cartilage, C3–C4). Branches ('Some Anatomists Like Freaking Out Poor Medical Students'): Superior thyroid, Ascending pharyngeal, Lingual, Facial, Occipital, Posterior auricular, then the terminal Maxillary (→ middle meningeal, inferior alveolar, sphenopalatine) and Superficial temporal. The internal carotid artery has NO branches in the neck (its first branch is the ophthalmic artery)",
        "Epistaxis: anterior bleeds (Kiesselbach plexus — anterior ethmoidal, sphenopalatine, greater palatine, superior labial arteries) are most common; posterior bleeds come from the sphenopalatine artery and are more serious. Superficial temporal artery biopsy for giant cell arteritis; its pulse is felt just in front of the tragus."
    ),
    "thyroid gland": _af(
        "Endocrine — Neck (isthmus over tracheal rings 2–4)",
        "Two lobes joined by the isthmus; a pyramidal lobe (thyroglossal duct remnant) in ~50%. Wrapped in pretracheal fascia → moves up with swallowing. Arteries: superior thyroid (external carotid; runs with the external laryngeal nerve), inferior thyroid (thyrocervical trunk; close to the recurrent laryngeal nerve), ± thyroid ima. Veins: superior + middle → internal jugular, inferior → brachiocephalic. Develops from the foramen cecum of the tongue and descends along the thyroglossal duct. Four parathyroids on the back: superior from the 4th pharyngeal pouch, inferior from the 3rd",
        "Thyroglossal duct cyst: midline mass that moves UP when the tongue is protruded (a branchial cleft cyst is lateral, in front of SCM). Thyroidectomy risks: recurrent laryngeal nerve (hoarseness), external laryngeal nerve (weak high pitch), parathyroids (hypocalcemia → tetany, Chvostek/Trousseau signs). Lingual thyroid = failed descent."
    ),
    "larynx": _af(
        "Neck — voice box (C3–C6)",
        "Cartilages: thyroid (laryngeal prominence), cricoid (the only complete ring, at C6), paired arytenoids, epiglottis. Cricothyroid membrane between the thyroid and cricoid cartilages. Muscles: posterior cricoarytenoid — the ONLY abductor (opens the airway); lateral cricoarytenoid and transverse/oblique arytenoids — adductors; cricothyroid — tenses the folds, raises pitch (external laryngeal nerve); thyroarytenoid/vocalis — relaxes. Nerves: superior laryngeal (internal branch — sensation above the folds, afferent limb of the cough reflex; external — cricothyroid) and recurrent laryngeal (all other muscles, sensation below the folds)",
        "Emergency airway: cricothyroidotomy through the cricothyroid membrane. Bilateral recurrent laryngeal nerve injury → both folds near the midline → stridor. A fish bone in the piriform recess can injure the internal laryngeal nerve (loss of cough reflex above the folds)."
    ),
    "extraocular muscles": _af(
        "Orbit — six muscles that move the eye",
        "'LR6 SO4, rest 3': lateral rectus — CN VI (abduction); superior oblique — CN IV (depresses, abducts, intorts; works best looking down and in); CN III — medial rectus (adduction), superior rectus (elevation), inferior rectus (depression), inferior oblique (elevates, abducts, extorts) and levator palpebrae superioris (raises the lid, helped by the sympathetic Müller muscle). Clinical testing: abduct the eye, then up/down tests SR/IR; adduct the eye, then up/down tests IO/SO",
        "CN III palsy: eye 'down and out' + ptosis ± dilated pupil. CN IV palsy: vertical diplopia worse looking down (stairs, reading); head tilts AWAY from the affected side. CN VI palsy: horizontal diplopia, cannot abduct — often from raised intracranial pressure (long intracranial course). Horner syndrome: mild ptosis (Müller), miosis, anhidrosis."
    ),
    "skull foramina": _af(
        "Skull Base — openings and what passes through them",
        "Cribriform plate: CN I. Optic canal: CN II + ophthalmic artery. Superior orbital fissure: CN III, IV, V1, VI, superior ophthalmic vein, sympathetic fibers. Foramen rotundum: V2. Foramen ovale: V3, lesser petrosal nerve, accessory meningeal artery. Foramen spinosum: middle meningeal artery. Internal acoustic meatus: CN VII, VIII, labyrinthine artery. Jugular foramen: CN IX, X, XI, internal jugular vein. Hypoglossal canal: CN XII. Foramen magnum: medulla/spinal cord, vertebral arteries, spinal roots of CN XI. Carotid canal: internal carotid artery (passes over the cartilage-filled foramen lacerum)",
        "Jugular foramen syndrome: CN IX, X and XI palsies together — dysphagia, hoarseness, absent gag, weak SCM/trapezius (glomus tumor, skull-base fracture). 'Standing Room Only' = V1 Superior orbital fissure, V2 Rotundum, V3 Ovale."
    ),
    "parotid gland": _af(
        "Head — largest salivary gland (serous)",
        "Lies over the masseter and the ramus of the mandible and wraps behind it. Structures inside it, superficial → deep: facial nerve branches (motor — they do not supply the gland), retromandibular vein, external carotid artery (dividing into maxillary + superficial temporal), auriculotemporal nerve. Parotid (Stensen) duct crosses the masseter, pierces buccinator and opens opposite the upper 2nd molar. Secretomotor supply: CN IX (lesser petrosal nerve → otic ganglion → auriculotemporal nerve)",
        "Parotid tumors are mostly benign (pleomorphic adenoma); facial nerve weakness suggests malignancy. Frey syndrome after parotidectomy: gustatory sweating over the cheek (auriculotemporal fibers regrow into sweat glands). Mumps parotitis: pain worse with chewing (tight capsule)."
    ),
    "tongue innervation": _af(
        "Head — nerves of the tongue",
        "Anterior 2/3: general sensation — lingual nerve (V3); taste — chorda tympani (CN VII). Posterior 1/3: general sensation + taste — glossopharyngeal nerve (CN IX). Root near the epiglottis: vagus (CN X, internal laryngeal). Motor: all tongue muscles — hypoglossal nerve (CN XII) — EXCEPT palatoglossus (vagus)",
        "CN XII lesion: the tongue deviates TOWARD the side of the lesion on protrusion (unopposed opposite genioglossus), with atrophy and fasciculations if LMN. The lingual nerve loops under the submandibular duct — at risk in submandibular gland surgery and lower third molar extraction."
    ),
    "pharyngeal arches": _af(
        "Embryology — Head & Neck (weeks 4–5)",
        "1st (mandibular): CN V3 — muscles of mastication, mylohyoid, anterior digastric, tensor tympani, tensor veli palatini; Meckel cartilage → malleus, incus, sphenomandibular ligament. 2nd (hyoid): CN VII — muscles of facial expression, stapedius, stylohyoid, posterior digastric; Reichert cartilage → stapes, styloid process, lesser horn and upper body of the hyoid. 3rd: CN IX — stylopharyngeus; greater horn and lower body of the hyoid. 4th + 6th: CN X (4th — superior laryngeal → cricothyroid, pharyngeal constrictors; 6th — recurrent laryngeal → intrinsic laryngeal muscles); laryngeal cartilages. Pouches: 1st — middle ear and auditory tube; 2nd — palatine tonsil; 3rd — thymus + inferior parathyroids; 4th — superior parathyroids, ultimobranchial body (thyroid C cells)",
        "1st arch neural crest failure → Treacher Collins syndrome (small mandible, ear defects). 3rd/4th pouch failure → DiGeorge syndrome (22q11.2 deletion): thymic aplasia (T-cell deficiency), hypoparathyroidism (hypocalcemia), conotruncal heart defects. Persistent 2nd cleft → branchial cleft cyst (lateral neck, in front of SCM)."
    ),
    # ── Back & Spine ──────────────────────────────────────────────────────────
    "vertebral column": _af(
        "Back — 33 vertebrae (7 cervical, 12 thoracic, 5 lumbar, 5 fused sacral, ~4 coccygeal)",
        "Cervical: transverse foramina (vertebral artery from C6 upward), bifid spines; C1 atlas (no body — 'yes' nodding), C2 axis (dens — 'no' rotation), C7 vertebra prominens. Thoracic: costal facets for the ribs, long downward spines. Lumbar: large bodies, no transverse foramina or costal facets. Curvatures: thoracic + sacral kyphosis (primary, present at birth); cervical + lumbar lordosis (secondary). Ligaments: anterior longitudinal (prevents hyperextension), posterior longitudinal (narrow, so discs herniate posterolaterally past it), ligamentum flavum (elastic, between laminae)",
        "Spondylolysis = pars interarticularis defect (young athletes, gymnasts; 'Scottie dog collar' on oblique X-ray); spondylolisthesis = forward slip, usually L5 on S1. Hangman fracture: bilateral pars fracture of C2 (hyperextension). Jefferson fracture: burst fracture of C1 (axial load). Dens fractures are common after falls in the elderly."
    ),
    "intervertebral disc": _af(
        "Back — fibrocartilaginous joint between vertebral bodies",
        "Annulus fibrosus (outer rings of fibrocartilage) surrounds the nucleus pulposus (gel; notochord remnant). Herniation is usually posterolateral because the posterior longitudinal ligament is narrow and strongest in the midline. Lumbar: a posterolateral herniation hits the root that exits BELOW (L4–L5 disc → L5 root). Cervical: roots exit ABOVE their vertebra, so the C5–C6 disc → C6 root",
        "Most common levels: L4–L5 and L5–S1, C5–C6 and C6–C7. L5 root: weak dorsiflexion and great-toe extension, numb dorsum of the foot. S1 root: weak plantarflexion, absent ankle jerk, numb lateral foot. Large central herniation → cauda equina syndrome (saddle anesthesia, urinary retention) — surgical emergency."
    ),
    "lumbar puncture": _af(
        "Procedural Anatomy — CSF sampling",
        "The spinal cord ends at the conus medullaris at L1–L2 in adults (about L3 in newborns); the dural sac and subarachnoid space end at S2. Insert the needle at L3–L4 or L4–L5 (the line joining the iliac crests — Tuffier line — crosses the L4 spinous process). Layers crossed: skin → subcutaneous tissue → supraspinous ligament → interspinous ligament → ligamentum flavum ('pop') → epidural space → dura → arachnoid → subarachnoid space (CSF). The pia is not pierced",
        "Epidural anesthesia stops in the epidural space (loss of resistance after the ligamentum flavum). Post-dural-puncture headache: worse sitting up, better lying flat → epidural blood patch. Rule out raised intracranial pressure from a mass (CT) before LP to avoid herniation."
    ),
    # ── Neuroanatomy ──────────────────────────────────────────────────────────
    "cerebral arteries": _af(
        "Neuroanatomy — territories of the anterior, middle and posterior cerebral arteries",
        "ACA: medial surface of the frontal and parietal lobes — leg/foot motor and sensory cortex (paracentral lobule). MCA: lateral convexity — face and arm motor/sensory cortex, Broca (inferior frontal) and Wernicke (superior temporal) areas in the dominant hemisphere; lenticulostriate branches supply the internal capsule and basal ganglia. PCA: occipital lobe (visual cortex), inferomedial temporal lobe, thalamus. Vertebral arteries (→ PICA) join to form the basilar artery (→ AICA, pontine, superior cerebellar, then the PCAs)",
        "ACA stroke: contralateral leg > arm weakness. MCA stroke: contralateral face + arm > leg weakness and numbness, aphasia (dominant side) or hemineglect (non-dominant), homonymous hemianopia. PCA stroke: contralateral homonymous hemianopia with macular sparing. PICA → lateral medullary (Wallenberg) syndrome. Lenticulostriate (hypertensive) lacunar infarct → pure motor stroke."
    ),
    "ventricular system": _af(
        "Neuroanatomy — CSF production and flow",
        "CSF is made by the choroid plexus (~500 mL/day; ~150 mL present at once). Lateral ventricles → interventricular foramina (of Monro) → third ventricle → cerebral aqueduct (of Sylvius) → fourth ventricle → median aperture (Magendie) and lateral apertures (Luschka) → subarachnoid space → reabsorbed by arachnoid granulations into the superior sagittal sinus",
        "Non-communicating (obstructive) hydrocephalus: aqueductal stenosis (most common congenital cause), tumors. Communicating: poor reabsorption (after meningitis or subarachnoid hemorrhage). Normal pressure hydrocephalus (elderly): 'wet, wobbly, wacky' — urinary incontinence, magnetic gait, dementia. Dandy-Walker: cystic 4th ventricle with absent cerebellar vermis."
    ),
    "internal capsule": _af(
        "Neuroanatomy — white matter between the thalamus/caudate (medial) and lentiform nucleus (lateral)",
        "Anterior limb: frontopontine and thalamocortical fibers. Genu: corticobulbar fibers (face). Posterior limb: corticospinal fibers (arm in front of leg) and sensory thalamocortical radiations; retrolenticular part: optic radiations. Blood supply: lenticulostriate branches of the MCA (most), anterior choroidal artery (posterior limb), recurrent artery of Heubner (ACA — anterior limb)",
        "A small lacunar infarct in the posterior limb (hypertension, lenticulostriate disease) → pure motor hemiparesis of the face, arm and leg equally on the opposite side. Hypertensive hemorrhage is most common in the putamen, next to the internal capsule."
    ),
    "basal ganglia": _af(
        "Neuroanatomy — deep nuclei that regulate movement",
        "Striatum = caudate + putamen; lentiform nucleus = putamen + globus pallidus; plus the subthalamic nucleus and substantia nigra (pars compacta — dopamine). Direct pathway (D1 receptors) facilitates movement; indirect pathway (D2 receptors) inhibits it. Dopamine from the substantia nigra excites the direct and inhibits the indirect pathway → net more movement",
        "Parkinson disease: loss of dopaminergic neurons in the substantia nigra pars compacta → bradykinesia, rigidity, resting tremor. Huntington disease: caudate atrophy (loss of indirect-pathway GABA neurons) → chorea. Hemiballismus: lacunar stroke of the contralateral subthalamic nucleus. Wilson disease: copper deposits in the putamen."
    ),
    "brainstem": _af(
        "Neuroanatomy — midbrain, pons, medulla",
        "Cranial nerve nuclei, 'rule of 4s': 4 nerves above the pons (I–IV; III and IV in the midbrain), 4 in the pons (V–VIII), 4 in the medulla (IX–XII). Structures near the MIDLINE start with M: Motor pathway (corticospinal), Medial lemniscus, Medial longitudinal fasciculus, Motor nuclei of the CNs that divide evenly into 12 (III, IV, VI, XII). LATERAL structures start with S: Spinocerebellar, Spinothalamic, Sensory nucleus of V, Sympathetic pathway. Blood supply: medial — paramedian branches (anterior spinal artery in the medulla, basilar in the pons); lateral — PICA (medulla), AICA (pons), superior cerebellar/PCA (midbrain)",
        "Medial medullary syndrome (anterior spinal artery): contralateral hemiparesis + loss of vibration/proprioception, tongue deviates toward the lesion (CN XII). Lateral medullary / Wallenberg (PICA): ipsilateral facial pain-temperature loss, Horner, dysphagia and hoarseness (nucleus ambiguus), vertigo, ataxia; contralateral body pain-temperature loss. Weber syndrome (midbrain, PCA branches): ipsilateral CN III palsy + contralateral hemiparesis."
    ),
    "cerebellum": _af(
        "Neuroanatomy — coordination and balance",
        "Vermis (midline): trunk posture and gait. Hemispheres (lateral): coordination of the IPSILATERAL limbs. Inputs: middle cerebellar peduncle (contralateral cortex via pontine nuclei), inferior peduncle (ipsilateral spinocerebellar and vestibular fibers; climbing fibers from the inferior olive). Output: deep nuclei, lateral → medial Dentate, Emboliform, Globose, Fastigial ('Don't Eat Greasy Foods'), mostly through the superior peduncle to the contralateral thalamus and cortex. Purkinje cells are the only output of the cerebellar cortex (inhibitory, GABA)",
        "Hemisphere lesion → ipsilateral limb ataxia, intention tremor, dysmetria (finger-nose test), dysdiadochokinesia; falls toward the lesion. Vermis lesion (alcohol, medulloblastoma in children) → truncal ataxia, wide-based gait. Cerebellar signs are ipsilateral because the pathways cross twice."
    ),
    "thalamus": _af(
        "Neuroanatomy — relay station of the diencephalon",
        "VPL: body sensation (spinothalamic tract + medial lemniscus) → primary somatosensory cortex. VPM: face sensation (trigeminal) and taste ('Makeup goes on the face'). LGN: vision → calcarine cortex ('Lateral = Light'). MGN: hearing → auditory cortex ('Medial = Music'). VL: motor (basal ganglia and cerebellum → motor cortex). Anterior nucleus: limbic system (Papez circuit). Medial dorsal nucleus: memory, prefrontal connections. Blood supply mainly from thalamoperforator branches of the PCA",
        "Thalamic (Dejerine-Roussy) syndrome: lacunar stroke of VPL/VPM → contralateral loss of all sensation, later burning neuropathic pain. Wernicke-Korsakoff damages the medial dorsal nuclei and mammillary bodies."
    ),
    "hypothalamus": _af(
        "Neuroanatomy — homeostasis and control of the pituitary",
        "Lateral nucleus — hunger (destroyed → anorexia: 'lateral lesion makes you shrink'). Ventromedial — satiety (destroyed → hyperphagia, obesity; craniopharyngioma). Anterior — cooling, parasympathetic ('A/C: anterior cooling'). Posterior — heat conservation, sympathetic. Suprachiasmatic — circadian rhythm. Supraoptic + paraventricular — ADH and oxytocin, carried down axons to the posterior pituitary. Arcuate — dopamine (inhibits prolactin) and GHRH. Preoptic — GnRH, thermoregulation",
        "Damage to the hypothalamus or pituitary stalk → central diabetes insipidus (↓ADH) and ↑prolactin (dopamine no longer reaches the anterior pituitary). The posterior pituitary is neural tissue (neuroectoderm); the anterior pituitary comes from Rathke pouch (oral ectoderm)."
    ),
    "limbic system": _af(
        "Neuroanatomy — emotion, memory and behavior",
        "Hippocampus, amygdala, mammillary bodies, fornix, cingulate gyrus and the anterior thalamic nucleus ('5 Fs': feeding, fleeing, fighting, feeling, sex). Papez circuit: hippocampus → fornix → mammillary bodies → mammillothalamic tract → anterior thalamic nucleus → cingulate gyrus → back to the hippocampus",
        "Bilateral hippocampal damage (HSV encephalitis of the temporal lobes, hypoxia) → anterograde amnesia. Bilateral amygdala lesions → Klüver-Bucy syndrome (hyperorality, hypersexuality, disinhibition). Mammillary body atrophy → Wernicke-Korsakoff syndrome (thiamine deficiency)."
    ),
    "visual pathway": _af(
        "Neuroanatomy — from retina to occipital cortex",
        "Retina → optic nerve → optic chiasm (fibers from the NASAL retina — temporal visual fields — cross) → optic tract → LGN of the thalamus → optic radiations: Meyer loop (inferior retina = superior visual field) through the temporal lobe, dorsal loop (superior retina = inferior field) through the parietal lobe → primary visual cortex (calcarine sulcus). Pupillary light reflex: CN II → pretectal nucleus → both Edinger-Westphal nuclei → CN III → both pupils constrict",
        "Optic nerve lesion → blindness of that eye. Chiasm (pituitary adenoma, craniopharyngioma) → bitemporal hemianopia. Optic tract → contralateral homonymous hemianopia. Meyer loop (temporal lobe) → contralateral superior quadrantanopia ('pie in the sky'); parietal radiations → inferior quadrantanopia ('pie on the floor'). PCA stroke → contralateral hemianopia with macular sparing."
    ),
    "cerebral cortex": _af(
        "Neuroanatomy — functional areas of the cerebral hemispheres",
        "Frontal: primary motor cortex (precentral gyrus, Brodmann 4), premotor area and frontal eye fields (8), prefrontal cortex (planning, personality), Broca area (44/45, dominant inferior frontal gyrus — speech production). Parietal: primary somatosensory cortex (postcentral gyrus, 3-1-2); non-dominant parietal lobe — spatial attention. Temporal: primary auditory cortex (41/42), Wernicke area (22, dominant superior temporal gyrus — language comprehension), hippocampus (memory). Occipital: primary visual cortex (17, calcarine sulcus). Homunculus: face and hand on the lateral surface (MCA), leg on the medial surface (ACA)",
        "Broca aphasia: non-fluent, comprehension intact, poor repetition (patient aware and frustrated). Wernicke aphasia: fluent 'word salad', poor comprehension and repetition. Conduction aphasia (arcuate fasciculus): poor repetition only. Non-dominant parietal lesion → hemispatial neglect; dominant angular gyrus → Gerstmann syndrome (agraphia, acalculia, finger agnosia, left-right confusion). Frontal lobe lesion → disinhibition and personality change."
    ),
    "meninges": _af(
        "Neuroanatomy — coverings of the brain and spinal cord",
        "Dura mater (outer periosteal + inner meningeal layer; folds: falx cerebri, tentorium cerebelli, falx cerebelli, diaphragma sellae), arachnoid mater, pia mater. Spaces: epidural (only a potential space in the skull — between bone and dura; a real space in the spinal canal, with fat and veins), subdural (potential — crossed by bridging veins), subarachnoid (CSF, cerebral arteries, cisterns). Dura above the tentorium: CN V; below: C2–C3 and CN X",
        "Epidural hematoma: middle meningeal artery, biconvex, lucid interval. Subdural hematoma: bridging veins, crescent-shaped, crosses sutures. Subarachnoid hemorrhage: ruptured berry aneurysm, 'worst headache of life', blood in the cisterns / xanthochromic CSF. Uncal herniation under the tentorium compresses CN III (blown pupil), the PCA, and the opposite cerebral peduncle against the tentorium (Kernohan notch → hemiparesis on the SAME side as the mass)."
    ),
    "spinal cord anatomy": _af(
        "Neuroanatomy — gross anatomy and blood supply of the spinal cord",
        "Ends at the conus medullaris (L1–L2); the filum terminale anchors it to the coccyx. Cervical (C5–T1) and lumbosacral (L1–S3) enlargements supply the limbs. Gray matter: dorsal horn (sensory), ventral/anterior horn (lower motor neurons), lateral horn T1–L2 (sympathetic preganglionics) and S2–S4 (parasympathetic). 31 pairs of spinal nerves: 8 cervical (C1–C7 exit ABOVE their vertebra, C8 below C7), 12 thoracic, 5 lumbar, 5 sacral, 1 coccygeal. Blood supply: one anterior spinal artery (anterior 2/3 of the cord) + two posterior spinal arteries (dorsal columns); the artery of Adamkiewicz (T9–L2, usually on the left) reinforces the anterior spinal artery in the lower cord",
        "Anterior spinal artery infarct (aortic aneurysm repair or dissection): paralysis and loss of pain/temperature below the lesion, with vibration and proprioception SPARED (dorsal columns). B12 deficiency (subacute combined degeneration): dorsal columns + lateral corticospinal tracts. Polio and spinal muscular atrophy: anterior horn cells (LMN signs only)."
    ),
    "autonomic nervous system": _af(
        "Neuroanatomy — sympathetic and parasympathetic divisions",
        "Sympathetic (thoracolumbar, T1–L2): short preganglionic fibers → paravertebral (sympathetic chain) or prevertebral ganglia (celiac, superior and inferior mesenteric, reached by the splanchnic nerves: greater T5–T9, lesser T10–T11, least T12) → long postganglionic fibers releasing norepinephrine (sweat glands use ACh). The adrenal medulla receives preganglionic fibers directly. Parasympathetic (craniosacral): CN III (ciliary ganglion → pupil, ciliary muscle), CN VII (pterygopalatine ganglion → lacrimal/nasal glands; submandibular ganglion → submandibular/sublingual glands), CN IX (otic ganglion → parotid), CN X (thoracic and abdominal viscera to the proximal 2/3 of the transverse colon), S2–S4 pelvic splanchnics; long preganglionic → ganglia in or near the organ → short postganglionic (ACh on muscarinic receptors). All preganglionic fibers release ACh onto nicotinic receptors",
        "Horner syndrome = interrupted sympathetic supply to the face (Pancoast tumor, carotid dissection, lateral medullary stroke): ptosis, miosis, anhidrosis. Visceral pain travels back with sympathetic fibers, so it is referred to the dermatomes of the same segments (heart → T1–T4, left arm and chest)."
    ),
    "deep tendon reflexes": _af(
        "Neurology — stretch reflexes and their nerve roots",
        "Biceps — C5–C6 (musculocutaneous n.); brachioradialis — C6 (radial n.); triceps — C7 (radial n.); patellar — L4 (L3–L4, femoral n.); Achilles — S1 (tibial n.). 'S1, 2 — buckle my shoe (ankle); L3, 4 — kick the door (knee); C5, 6 — pick up sticks (biceps); C7, 8 — lay them straight (triceps)'. Superficial reflexes: cremasteric L1–L2, anal wink S3–S4. Grading: 0 absent, 1+ reduced, 2+ normal, 3+ brisk, 4+ with clonus",
        "UMN lesion → hyperreflexia, clonus, spasticity, upgoing plantar (Babinski). LMN lesion → reduced or absent reflexes, flaccidity, atrophy, fasciculations. Reinforcement (Jendrassik maneuver) brings out weak reflexes. Hypothyroidism → slow relaxation phase of the ankle jerk."
    ),
    "cranial fossae": _af(
        "Skull Base — anterior, middle and posterior cranial fossae",
        "Anterior fossa: orbital roofs and cribriform plate — holds the frontal lobes and olfactory bulbs. Middle fossa: sella turcica (pituitary), temporal lobes; openings — optic canal, superior orbital fissure, foramina rotundum, ovale, spinosum and lacerum. Posterior fossa: cerebellum, pons and medulla; openings — internal acoustic meatus, jugular foramen, hypoglossal canal, foramen magnum",
        "Anterior fossa (basilar skull) fracture → raccoon eyes, CSF rhinorrhea, loss of smell (CN I). Middle fossa / petrous temporal fracture → Battle sign, hemotympanum, CSF otorrhea, facial palsy and hearing loss (CN VII, VIII). Posterior fossa masses → hydrocephalus (4th ventricle) and cerebellar signs."
    ),
    # ── Embryology ────────────────────────────────────────────────────────────
    "germ layers": _af(
        "Embryology — the three germ layers (formed at gastrulation, week 3)",
        "Ectoderm — surface ectoderm: epidermis, hair, nails, lens, anterior pituitary (Rathke pouch), tooth enamel, parotid and mammary glands; neuroectoderm (neural tube): brain, spinal cord, retina, optic nerve, posterior pituitary, pineal gland; neural crest (separate entry). Mesoderm: skeletal, cardiac and smooth muscle, bone, cartilage, connective tissue, dermis, heart and blood vessels, blood and lymphatics, spleen, kidneys and ureters, gonads, adrenal cortex, serous linings; notochord → nucleus pulposus. Endoderm: epithelium of the gut, liver, pancreas, lungs, thyroid follicular cells, parathyroids, thymus, bladder/urethra and auditory tube",
        "The primitive streak forms the trilaminar disc; a persistent primitive streak → sacrococcygeal teratoma. VACTERL association = mesodermal defects. The spleen is mesodermal, although it is supplied by the (foregut) celiac trunk."
    ),
    "neural crest": _af(
        "Embryology — cells that migrate from the crests of the neural folds",
        "Derivatives ('MOTEL PASS'): Melanocytes, Odontoblasts, Tracheal cartilage, Enterochromaffin cells, Laryngeal cartilage, Parafollicular (C) cells of the thyroid, Adrenal medulla and all autonomic and sensory (dorsal root, cranial) ganglia, Schwann cells, Spiral membrane of the cochlea. Also: pia and arachnoid, aorticopulmonary septum, endocardial cushions (in part), skull bones and pharyngeal arch cartilages",
        "Neural crest disorders: Hirschsprung disease (crest cells fail to reach the distal colon → no myenteric/submucosal plexus), neuroblastoma, pheochromocytoma, conotruncal heart defects (tetralogy of Fallot, transposition, persistent truncus — e.g. DiGeorge), Treacher Collins syndrome, neurofibromatosis, melanoma."
    ),
    "neural tube": _af(
        "Embryology — neurulation (weeks 3–4)",
        "The notochord induces the ectoderm to form the neural plate → neural folds → neural tube; the anterior neuropore closes ~day 25 and the posterior neuropore ~day 27–28. Brain vesicles: prosencephalon → telencephalon (cerebral hemispheres, lateral ventricles) + diencephalon (thalamus, hypothalamus, retina, third ventricle); mesencephalon → midbrain (cerebral aqueduct); rhombencephalon → metencephalon (pons, cerebellum) + myelencephalon (medulla) around the fourth ventricle. Alar plate (dorsal) → sensory neurons; basal plate (ventral) → motor neurons",
        "Neural tube defects (folate deficiency, valproate/carbamazepine, maternal diabetes): ↑AFP in maternal serum and amniotic fluid (+ acetylcholinesterase in open defects). Anencephaly — failed anterior neuropore (polyhydramnios). Spina bifida occulta (tuft of hair, normal AFP) → meningocele → myelomeningocele (with Chiari II and hydrocephalus). Prevent with periconceptional folic acid: 0.4 mg/day, 4 mg/day after a previous NTD."
    ),
    "fetal circulation": _af(
        "Embryology — circulation before birth and the remnants after it",
        "Placenta → umbilical vein (most oxygenated blood) → ductus venosus (bypasses the liver) → IVC → right atrium → most blood crosses the foramen ovale → left atrium → LV → aorta → head and upper body. SVC blood → RA → RV → pulmonary trunk → ductus arteriosus (pulmonary resistance is high) → descending aorta. Two umbilical arteries (from the internal iliacs) return blood to the placenta. Remnants: umbilical vein → ligamentum teres hepatis; ductus venosus → ligamentum venosum; foramen ovale → fossa ovalis; ductus arteriosus → ligamentum arteriosum; umbilical arteries → medial umbilical ligaments; allantois/urachus → median umbilical ligament; notochord → nucleus pulposus",
        "At birth the first breath ↓pulmonary resistance → ↑left atrial pressure closes the foramen ovale; ↑O2 and ↓prostaglandins close the ductus arteriosus within days. Indomethacin or ibuprofen closes a PDA; prostaglandin E1 keeps it open in duct-dependent lesions (transposition, critical coarctation). Patent foramen ovale (~25% of adults) → paradoxical emboli."
    ),
    "heart embryology": _af(
        "Embryology — development of the heart (weeks 3–8)",
        "Heart tube folds in week 4. Truncus arteriosus → ascending aorta + pulmonary trunk (spiral aorticopulmonary septum, from neural crest). Bulbus cordis → smooth outflow parts of the RV (conus) and LV (aortic vestibule). Primitive ventricle → trabeculated ventricles. Primitive atrium → trabeculated atria (auricles). Sinus venosus → smooth right atrium (sinus venarum), coronary sinus, SVC. Atrial septum: septum primum + septum secundum, leaving the foramen ovale. Endocardial cushions → AV septum and the mitral and tricuspid valves. Ventricular septum: muscular part + membranous part (from the endocardial cushions)",
        "Membranous VSD is the most common congenital heart defect; ostium secundum is the most common ASD. Aorticopulmonary septum fails to spiral → transposition of the great arteries (maternal diabetes); deviates anterosuperiorly → tetralogy of Fallot; fails to form → persistent truncus arteriosus. Endocardial cushion (AV canal) defects → Down syndrome."
    ),
    "aortic arch derivatives": _af(
        "Embryology — the pharyngeal arch arteries",
        "1st arch → part of the maxillary artery ('1st is MAXimal'). 2nd → stapedial and hyoid arteries ('Second = Stapedial'). 3rd → common carotid and proximal internal carotid arteries ('C is the 3rd letter'). 4th → left: aortic arch; right: proximal right subclavian artery ('4th = systemic'). 6th → proximal pulmonary arteries; left 6th → ductus arteriosus ('6th = pulmonary'). The 5th arch regresses",
        "The left recurrent laryngeal nerve stays hooked under the ductus arteriosus (left 6th arch), but on the right the distal 6th arch disappears, so the right nerve loops higher, around the subclavian artery (4th arch). Vascular rings (double aortic arch, aberrant right subclavian) compress the trachea or esophagus → stridor, dysphagia."
    ),
    "gut development": _af(
        "Embryology — foregut, midgut and hindgut",
        "Foregut (celiac trunk): esophagus → 2nd part of the duodenum, liver, gallbladder, pancreas. Midgut (SMA): distal duodenum → proximal 2/3 of the transverse colon. Hindgut (IMA): distal 1/3 of the transverse colon → upper anal canal (above the pectinate line). The midgut herniates through the umbilical ring in week 6, rotates 270° counterclockwise around the SMA, and returns by week 10. Pancreas: the ventral bud forms the uncinate process and part of the head and main duct; the dorsal bud forms the body, tail and most of the head. The vitelline duct normally closes by week 7",
        "Omphalocele: gut fails to return — midline, covered by peritoneum/amnion; associated with trisomies and Beckwith-Wiedemann. Gastroschisis: right of the umbilicus, uncovered. Malrotation → Ladd bands and midgut volvulus (bilious vomiting in a newborn). Meckel diverticulum (persistent vitelline duct) — rule of 2s: 2% of people, 2 feet from the ileocecal valve, 2 inches long, 2 kinds of ectopic tissue (gastric, pancreatic), symptoms before age 2. Annular pancreas: ventral bud encircles the duodenum. Duodenal atresia: failed recanalization (double bubble)."
    ),
    "urogenital development": _af(
        "Embryology — kidneys, gonads and genital ducts",
        "Kidney: pronephros (week 4, regresses) → mesonephros (interim kidney; its duct is the mesonephric/Wolffian duct) → metanephros (permanent kidney from week 5): the ureteric bud (from the mesonephric duct → ureter, renal pelvis, calyces, collecting ducts) induces the metanephric mesenchyme (→ glomerulus through distal convoluted tubule). The kidneys ascend from the pelvis. Genital ducts: SRY (Y chromosome) → testes; Sertoli cells make anti-Müllerian hormone (Müllerian ducts regress) and Leydig cells make testosterone (Wolffian duct → epididymis, ductus deferens, seminal vesicle, ejaculatory duct). Without SRY: Müllerian (paramesonephric) ducts → uterine tubes, uterus, cervix, upper 1/3 of the vagina; Wolffian ducts regress. DHT forms the male external genitalia and prostate",
        "Potter sequence: bilateral renal agenesis or severe ARPKD → oligohydramnios → flat face, limb deformities, pulmonary hypoplasia. The ureteropelvic junction is the last part to canalize → most common cause of congenital hydronephrosis. Horseshoe kidney is trapped under the IMA. 5α-reductase deficiency: ambiguous genitalia at birth, virilization at puberty. Bicornuate uterus: incomplete Müllerian fusion."
    ),
    # ── More gross anatomy ────────────────────────────────────────────────────
    "clavicle": _af(
        "Bone — Shoulder girdle",
        "S-shaped bone; the only bony link between the upper limb and the axial skeleton (sternoclavicular + acromioclavicular joints). First bone to start ossifying (membranous, week 5) and the last growth plate to fuse (medial end, ~25 years). The subclavian vessels and brachial plexus pass beneath it, protected by subclavius",
        "Most commonly fractured bone in children and in newborns (shoulder dystocia), usually in the middle third: the medial fragment is pulled up by SCM, the lateral fragment down by the weight of the arm. Rarely injures the subclavian vessels or brachial plexus. Absent or small clavicles: cleidocranial dysplasia (RUNX2)."
    ),
    "elbow joint": _af(
        "Joint — Elbow (hinge + pivot synovial joint)",
        "Humeroulnar and humeroradial articulations (hinge) plus the proximal radioulnar joint (pivot, for pronation/supination). The annular ligament holds the radial head against the ulna. Ulnar (medial) collateral ligament resists valgus stress; radial (lateral) collateral ligament resists varus. Carrying angle ~5–15° (larger in females)",
        "Nursemaid's elbow (pulled elbow, ages 1–4): the radial head slips out of the annular ligament when a child's arm is pulled — arm held pronated and still; reduce by supination-flexion or hyperpronation. Supracondylar fracture → brachial artery + median nerve injury. Throwing athletes tear the ulnar collateral ligament."
    ),
    "forearm compartments": _af(
        "Musculoskeletal — anterior and posterior forearm",
        "Anterior (flexor-pronator) compartment — median nerve, except FCU and the medial half of FDP (ulnar nerve). Superficial layer: pronator teres, FCR, palmaris longus, FCU; intermediate: FDS; deep: FDP, FPL, pronator quadratus. Most arise from the medial epicondyle (common flexor origin). Posterior (extensor) compartment — radial nerve / posterior interosseous nerve: brachioradialis, ECRL, ECRB, extensor digitorum, extensor digiti minimi, ECU, supinator, APL, EPB, EPL, extensor indicis; most arise from the lateral epicondyle (common extensor origin)",
        "Lateral epicondylitis ('tennis elbow'): ECRB origin — pain on resisted wrist extension. Medial epicondylitis ('golfer's elbow'): common flexor origin. Volkmann ischemic contracture: forearm compartment syndrome (often after supracondylar fracture) → fixed flexion of the wrist and fingers. De Quervain tenosynovitis: APL + EPB tendons (positive Finkelstein test)."
    ),
    "palmar arches": _af(
        "Vascular — Hand",
        "Superficial palmar arch: mainly the ulnar artery, completed by the superficial palmar branch of the radial artery; lies at the level of the distal border of the fully extended thumb and gives the common palmar digital arteries. Deep palmar arch: mainly the radial artery (which crosses the anatomical snuffbox and passes between the heads of the first dorsal interosseous), completed by the deep branch of the ulnar artery; lies ~1 cm proximal to the superficial arch, with the deep branch of the ulnar nerve",
        "The Allen test checks ulnar collateral flow before a radial arterial line or ABG. Deep palm lacerations can open an arch → brisk bleeding needing pressure on both radial and ulnar arteries. The radial pulse is felt just lateral to the FCR tendon at the wrist."
    ),
    "femoral artery": _af(
        "Vascular — Lower Limb",
        "Continuation of the external iliac artery below the inguinal ligament at the midinguinal point (halfway between the ASIS and pubic symphysis); lies in the femoral sheath, lateral to the femoral vein and medial to the femoral nerve. Branches: superficial epigastric, superficial circumflex iliac, external pudendal, and the profunda femoris (deep femoral → medial and lateral circumflex femoral arteries, perforating arteries — main supply of the thigh). Passes through the adductor canal and hiatus to become the popliteal artery",
        "Arterial access for angiography/catheterization at the femoral pulse; the femoral vein lies just medial (central lines), the femoral nerve lateral. Pseudoaneurysm after catheterization: pulsatile groin mass with a bruit."
    ),
    "sacral plexus": _af(
        "Peripheral Nerves — Pelvis (L4–S4)",
        "Lumbosacral trunk (L4–L5) + anterior rami of S1–S4, lying on the front of piriformis. Branches: superior gluteal (L4–S1), inferior gluteal (L5–S2), sciatic (L4–S3), posterior femoral cutaneous (S1–S3), pudendal (S2–S4), nerves to piriformis, obturator internus, quadratus femoris and levator ani; pelvic splanchnic nerves (S2–S4, parasympathetic to the bladder, hindgut and erectile tissue)",
        "Compression by pelvic tumors or the fetal head in labor, or sacral fractures → sciatica-like pain, foot drop, perineal numbness, bladder/bowel problems."
    ),
    "foot arches": _af(
        "Musculoskeletal — Foot",
        "Medial longitudinal arch (highest): calcaneus, talus, navicular, cuneiforms, medial 3 metatarsals — supported by the plantar aponeurosis, spring (plantar calcaneonavicular) ligament and tibialis posterior. Lateral longitudinal arch: calcaneus, cuboid, lateral 2 metatarsals — fibularis longus. Transverse arch: cuneiforms, cuboid, metatarsal bases — fibularis longus tendon. Plantar fascia (aponeurosis) runs from the calcaneal tuberosity to the toes (windlass mechanism)",
        "Plantar fasciitis: heel pain worst with the first steps in the morning, tender at the medial calcaneal tubercle. Adult acquired flatfoot: tibialis posterior tendon dysfunction. Achilles (calcaneal) tendon rupture: positive Thompson test (squeezing the calf does not plantarflex the foot); risk with fluoroquinolones and steroids."
    ),
    "esophagus": _af(
        "Gastrointestinal — ~25 cm, from the cricoid cartilage (C6) to the cardia (T11)",
        "Three narrowings: cricopharyngeus/upper sphincter (C6, ~15 cm from the incisors), where the aortic arch and left main bronchus cross (T4–T5, ~25 cm), and the diaphragm (T10, ~40 cm). Muscle: upper 1/3 skeletal, middle mixed, lower 1/3 smooth. Arteries: inferior thyroid (upper), aortic esophageal branches (middle), left gastric (lower). Veins: upper → inferior thyroid, middle → azygos, lower → left gastric (portal) — a portosystemic anastomosis. Lining: non-keratinized stratified squamous epithelium",
        "Swallowed objects and caustic strictures lodge at the narrowings. Esophageal varices form in the lower third (left gastric ↔ azygos). Zenker diverticulum: false diverticulum through Killian triangle just above cricopharyngeus. Boerhaave syndrome: full-thickness tear, usually of the distal left posterolateral wall. Squamous cell carcinoma in the upper/middle third; adenocarcinoma (Barrett) in the lower third."
    ),
    "small intestine": _af(
        "Gastrointestinal — duodenum, jejunum, ileum",
        "Jejunum (proximal 2/5, mostly upper left abdomen): thicker wall, wider, tall plicae circulares, long vasa recta, few large arcades, little mesenteric fat. Ileum (distal 3/5, lower right): thinner wall, short vasa recta, many arcades, more fat, Peyer patches (lymphoid follicles in the lamina propria/submucosa). Absorption: iron in the duodenum, folate in the jejunum, vitamin B12 and bile salts in the terminal ileum",
        "Terminal ileum resection or Crohn disease → B12 deficiency and bile acid loss (gallstones, oxalate kidney stones, fatty diarrhea). Meckel diverticulum lies in the ileum ~2 feet from the ileocecal valve. Peyer patches contain M cells that sample antigens; Salmonella and Yersinia invade here, and enlarged patches can be the lead point of intussusception in children."
    ),
    "colon anatomy": _af(
        "Gastrointestinal — large intestine",
        "Cecum (+ appendix), ascending colon (retroperitoneal), hepatic flexure, transverse colon (intraperitoneal, on the transverse mesocolon), splenic flexure, descending colon (retroperitoneal), sigmoid colon (intraperitoneal, sigmoid mesocolon), rectum. Features: taeniae coli (3 longitudinal muscle bands meeting at the appendix), haustra, epiploic appendices. Arteries: ileocolic, right colic, middle colic (SMA); left colic, sigmoid, superior rectal (IMA), linked by the marginal artery. Parasympathetic: vagus to the proximal 2/3 of the transverse colon, pelvic splanchnics (S2–S4) beyond",
        "Sigmoid volvulus (elderly, chronic constipation; 'coffee bean' sign) vs cecal volvulus (younger). Diverticulosis is most common in the sigmoid (highest pressure). Ischemic colitis at the splenic flexure watershed. Right-sided colon cancer → iron deficiency anemia from occult bleeding; left-sided → obstruction and narrower stools."
    ),
    "testis anatomy": _af(
        "Male Reproductive — testis and spermatic cord",
        "Develops on the posterior abdominal wall and descends through the inguinal canal (guided by the gubernaculum), carrying the processus vaginalis (→ tunica vaginalis). Artery: testicular artery from the aorta (L2). Veins: pampiniform plexus → right testicular vein → IVC; left → left renal vein. Lymph: para-aortic nodes (scrotal skin → superficial inguinal). Spermatic cord coverings: external spermatic fascia (from external oblique), cremasteric muscle and fascia (internal oblique), internal spermatic fascia (transversalis fascia)",
        "Left varicocele is more common (left vein enters the left renal vein at a right angle; nutcracker compression). Testicular cancer spreads to para-aortic nodes, not inguinal. Patent processus vaginalis → indirect inguinal hernia or communicating hydrocele. Undescended testis (cryptorchidism) → infertility and germ cell tumor risk — orchiopexy by ~1 year. Torsion: absent cremasteric reflex, high-riding horizontal testis."
    ),
    "female reproductive anatomy": _af(
        "Female Pelvis — ovaries, uterine tubes, uterus, vagina",
        "Ovary: held by the suspensory (infundibulopelvic) ligament, carrying the ovarian vessels, and the ovarian ligament; ovarian artery from the aorta; ovarian veins → IVC (right) / left renal vein (left); lymph → para-aortic nodes. Uterine tube: infundibulum (fimbriae), ampulla (usual site of fertilization), isthmus, intramural part. Uterus: fundus, body, cervix; usually anteverted and anteflexed; the uterine artery (internal iliac) crosses over the ureter. Vagina: upper 1/3 from the Müllerian ducts (lymph → iliac nodes), lower 2/3 from the urogenital sinus (lymph → superficial inguinal nodes)",
        "Ectopic pregnancy is most common in the ampulla; rupture → blood in the pouch of Douglas. Ovarian torsion twists the infundibulopelvic ligament. Cervical cancer spreads laterally along the cardinal ligaments → ureteral obstruction (hydronephrosis)."
    ),
    "bladder": _af(
        "Urinary — urinary bladder",
        "Detrusor smooth muscle; the trigone (between the two ureteric openings and the internal urethral orifice) is smooth-walled and comes from the mesonephric ducts. Nerves: parasympathetic S2–S4 (pelvic splanchnics) → detrusor contraction (voiding); sympathetic T11–L2 (hypogastric) → detrusor relaxation and internal sphincter contraction (storage); somatic pudendal nerve (S2–S4) → external urethral sphincter. The pontine micturition center coordinates voiding; the cortex inhibits it. The apex continues as the urachus (median umbilical ligament)",
        "Bladder rupture: at the dome (intraperitoneal — full bladder + blow → urinary ascites) or extraperitoneal (pelvic fracture). A full bladder rises above the pubis, so a suprapubic catheter avoids the peritoneum. Lesion above the sacral cord → spastic (reflex) bladder; sacral/cauda equina lesion → atonic overflow bladder. Urge incontinence = detrusor overactivity (antimuscarinics)."
    ),
    "perineum": _af(
        "Pelvis — region below the pelvic floor",
        "Diamond-shaped; a line between the ischial tuberosities divides it into the urogenital triangle (anterior) and anal triangle (posterior). Urogenital triangle: perineal membrane with the superficial perineal pouch (ischiocavernosus, bulbospongiosus, superficial transverse perineal muscles; crura and bulb of the penis/clitoris; greater vestibular [Bartholin] glands) and the deep perineal pouch (external urethral sphincter, deep transverse perineal muscle; bulbourethral glands in males). Anal triangle: ischioanal fossae (fat; pudendal canal in the lateral wall) and external anal sphincter. Nerve: pudendal (S2–S4); arteries: internal pudendal",
        "Ischioanal abscesses can spread around behind the anal canal ('horseshoe'). Bartholin gland cyst/abscess at the 4 or 8 o'clock position of the vaginal opening. Damage to the perineal body in childbirth → prolapse and fecal incontinence."
    ),
    "bony pelvis": _af(
        "Bone — Pelvis",
        "Each hip bone = ilium + ischium + pubis, fused at the acetabulum. The pelvic inlet (pelvic brim) separates the greater (false) from the lesser (true) pelvis. Female (gynecoid) pelvis: wider, round/oval inlet, subpubic angle ~90° or more, less prominent ischial spines; male (android): heart-shaped inlet, subpubic angle ~70°. Obstetric conjugate (sacral promontory → back of the pubic symphysis, ~11 cm) is the narrowest anteroposterior diameter of the inlet; the interspinous diameter (~10 cm) is the narrowest transverse diameter",
        "The ischial spines are the landmark for pudendal block and for fetal station (station 0 = head at the spines). Pelvic ring fractures usually break in two places and can bleed massively (internal iliac branches, venous plexus) and injure the bladder or urethra."
    ),
    "temporomandibular joint": _af(
        "Joint — Jaw (TMJ)",
        "Synovial joint between the mandibular condyle and the mandibular fossa/articular tubercle of the temporal bone, divided by an articular disc into an upper compartment (gliding/translation) and a lower compartment (hinge/rotation). Opening: lateral pterygoid (pulls the condyle and disc forward) + digastric/geniohyoid; closing: masseter, temporalis, medial pterygoid. Nerves: auriculotemporal and masseteric branches of V3",
        "TMJ dislocation (wide yawn): the condyle locks in front of the articular tubercle — reduce by pressing down and back on the lower molars. TMJ disorder: clicking, jaw pain, pain referred to the ear (auriculotemporal nerve). The jaw deviates toward a V3 lesion (weak lateral pterygoid)."
    ),
    "middle ear": _af(
        "Head — tympanic cavity",
        "Air-filled space between the tympanic membrane and the inner ear. Ossicles: malleus + incus (1st arch), stapes (2nd arch) — the stapes footplate sits in the oval window. Muscles: tensor tympani (V3) and stapedius (VII) damp loud sounds. The auditory (Eustachian) tube joins it to the nasopharynx to equalize pressure. Walls: roof — tegmen tympani (middle cranial fossa); floor — internal jugular vein; posterior — mastoid antrum; medial — promontory, round window, facial canal; lateral — tympanic membrane (crossed by the chorda tympani)",
        "Otitis media can spread to the mastoid air cells (mastoiditis) or through the tegmen to the brain (abscess, meningitis). Children have a shorter, more horizontal auditory tube → more otitis media. CN VII lesion → hyperacusis (stapedius). Otosclerosis fixes the stapes → conductive hearing loss (Rinne: bone > air; Weber lateralizes to the affected ear)."
    ),
    "paranasal sinuses": _af(
        "Head — air sinuses around the nasal cavity",
        "Frontal sinus → middle meatus (frontonasal duct). Maxillary sinus (largest) → middle meatus through an opening high on its medial wall (poor drainage by gravity). Ethmoid air cells: anterior/middle → middle meatus; posterior → superior meatus. Sphenoid sinus → sphenoethmoidal recess; the pituitary sits just above it. The nasolacrimal duct opens into the inferior meatus",
        "Maxillary sinusitis can feel like upper molar toothache (superior alveolar nerves). Ethmoid sinusitis in children can spread through the thin lamina papyracea → orbital cellulitis. Transsphenoidal surgery reaches the pituitary through the sphenoid sinus. Sphenoid/ethmoid sinusitis can lead to cavernous sinus thrombosis."
    ),
    "pharynx": _af(
        "Head & Neck — throat",
        "Nasopharynx (adenoids, auditory tube openings), oropharynx (palatine tonsils, base of the tongue), laryngopharynx/hypopharynx (piriform recesses; continues as the esophagus at C6). Muscles: superior, middle and inferior constrictors (circular) + stylopharyngeus (CN IX), palatopharyngeus, salpingopharyngeus (longitudinal). Motor: pharyngeal plexus (CN X) except stylopharyngeus; sensation: V2 (nasopharynx), CN IX (oropharynx — afferent of the gag reflex), CN X (laryngopharynx)",
        "Gag reflex: afferent CN IX, efferent CN X. Peritonsillar abscess: uvula pushed away, 'hot potato' voice, trismus. Tonsillectomy can injure CN IX (lost taste on the posterior tongue). Zenker diverticulum herniates through Killian triangle in the inferior constrictor."
    ),
    "eye anatomy": _af(
        "Head — the eyeball",
        "Layers: outer fibrous (sclera, cornea), middle vascular uvea (choroid, ciliary body, iris), inner retina. Aqueous humor is made by the ciliary body and drains at the anterior chamber angle through the trabecular meshwork into the canal of Schlemm. Iris: sphincter pupillae (parasympathetic, CN III → miosis) and dilator pupillae (sympathetic → mydriasis). The ciliary muscle (parasympathetic) contracts to relax the zonules so the lens rounds up for near vision (accommodation). Fovea: cones only, sharpest vision; optic disc: blind spot. Blood: ophthalmic artery (ICA) → central retinal artery",
        "Acute angle-closure glaucoma: painful red eye, fixed mid-dilated pupil, halos — avoid dilating drops. Open-angle glaucoma: painless loss of peripheral vision. Central retinal artery occlusion: sudden painless loss of vision in one eye, cherry-red spot. Retinal detachment: flashes, floaters, a 'curtain'. Lacrimal gland secretion: CN VII (greater petrosal nerve → pterygopalatine ganglion)."
    ),
    # ── Histology ─────────────────────────────────────────────────────────────
    "epithelium types": _af(
        "Histology — classification of epithelia",
        "Simple squamous: alveoli, endothelium, mesothelium, Bowman capsule. Simple cuboidal: kidney tubules, thyroid follicles, gland ducts. Simple columnar: stomach and intestines (goblet cells and microvilli in the small intestine), gallbladder, uterus. Pseudostratified ciliated columnar: trachea and bronchi (with goblet cells); epididymis and ductus deferens (with stereocilia). Stratified squamous: non-keratinized — esophagus, mouth, vagina, cornea, anal canal below the pectinate line; keratinized — skin. Transitional (urothelium): renal pelvis, ureter, bladder",
        "Metaplasia: Barrett esophagus (squamous → intestinal columnar with goblet cells), smokers' bronchi (ciliated columnar → squamous), cervical transformation zone (columnar → squamous; HPV infects here). Urothelium gives rise to urothelial carcinoma. Kartagener syndrome: defective dynein arms → immotile cilia (sinusitis, bronchiectasis, infertility, situs inversus)."
    ),
    "cell junctions": _af(
        "Histology — junctions between epithelial cells",
        "Tight junction (zonula occludens; claudins, occludin) — seals the space between cells, at the top. Adherens junction (zonula adherens; E-cadherin + actin) — just below it. Desmosome (macula adherens; desmogleins, desmoplakin + keratin intermediate filaments) — spot weld between cells. Gap junction (connexons) — lets ions and small molecules pass (cardiac and smooth muscle coupling). Hemidesmosome (integrins) — anchors cells to the basement membrane",
        "Pemphigus vulgaris: autoantibodies to desmogleins 3 (± 1) → intraepidermal blisters, Nikolsky positive. Bullous pemphigoid: autoantibodies to hemidesmosome proteins (BP180/BP230) → subepidermal tense blisters, Nikolsky negative. Loss of E-cadherin → invasive lobular breast and diffuse (signet ring) gastric cancers."
    ),
    "collagen types": _af(
        "Histology/Biochemistry — main collagen types",
        "Type I — bone, skin, tendon, ligament, dentin, cornea, late wound repair ('bONE'). Type II — cartilage, vitreous humor, nucleus pulposus ('carTWOlage'). Type III — reticular fibers: skin, blood vessels, uterus, granulation tissue, fetal tissue ('THREE-D': vascular Ehlers-Danlos). Type IV — basement membranes ('under the FLOOR'). Synthesis: preprocollagen → hydroxylation of proline and lysine (needs vitamin C) → glycosylation → triple helix (procollagen) → secreted, ends cleaved → cross-linked by lysyl oxidase (needs copper)",
        "Scurvy (vitamin C): weak collagen → bleeding gums, poor wound healing, corkscrew hairs. Osteogenesis imperfecta: type I collagen — fractures, blue sclerae, hearing loss. Ehlers-Danlos: joint hypermobility, stretchy skin (vascular type: type III → arterial/organ rupture). Alport syndrome: type IV collagen (hematuria, deafness, eye problems); Goodpasture: antibodies to type IV collagen. Menkes disease: copper transport defect → weak cross-linking."
    ),
    "muscle tissue types": _af(
        "Histology — skeletal, cardiac and smooth muscle",
        "Skeletal: long multinucleated striated fibers, nuclei at the edge, voluntary; T-tubules at the A–I junction form triads; satellite cells repair damage. Cardiac: branched cells with 1–2 central nuclei, striated, intercalated discs (gap junctions + desmosomes), dyads, pacemaker activity, calcium-induced calcium release. Smooth: spindle-shaped cells with one central nucleus, no striations, dense bodies; contraction via calmodulin → myosin light-chain kinase. Sarcomere (Z line to Z line): the A band (myosin) stays the same length; the I band and H zone shorten in contraction",
        "Skeletal muscle regenerates from satellite cells; cardiac muscle cannot (scar after MI). Duchenne muscular dystrophy: absent dystrophin. Malignant hyperthermia: RYR1 mutation triggered by volatile anesthetics or succinylcholine → treat with dantrolene."
    ),
}

_ANATOMY_ALIASES = {
    "cranial nerve": "cranial nerves",
    "cerebral arterial circle": "circle of willis",
    "hesselbach triangle": "inguinal canal", "hesselbach's triangle": "inguinal canal",
    "deep inguinal ring": "inguinal canal", "superficial inguinal ring": "inguinal canal",
    "flexor retinaculum": "carpal tunnel", "transverse carpal ligament": "carpal tunnel",
    "spinal tracts": "spinal cord tracts", "dorsal columns": "spinal cord tracts",
    "dorsal column": "spinal cord tracts", "spinothalamic tract": "spinal cord tracts",
    "corticospinal tract": "spinal cord tracts", "lateral corticospinal tract": "spinal cord tracts",
    "coronary artery": "coronary arteries", "coronary circulation": "coronary arteries",
    "right coronary artery": "coronary arteries", "left anterior descending artery": "coronary arteries",
    "left circumflex artery": "coronary arteries", "coronary dominance": "coronary arteries",
    "o2-hgb dissociation curve": "oxygen hemoglobin curve",
    "oxygen-hemoglobin curve": "oxygen hemoglobin curve",
    "oxygen hemoglobin dissociation curve": "oxygen hemoglobin curve",
    "oxygen-hemoglobin dissociation curve": "oxygen hemoglobin curve",
    "oxyhemoglobin dissociation curve": "oxygen hemoglobin curve",
    "oxygen dissociation curve": "oxygen hemoglobin curve",
    "hemoglobin dissociation curve": "oxygen hemoglobin curve",
    "renin-angiotensin-aldosterone system": "raas", "renin angiotensin aldosterone system": "raas",
    "renin-angiotensin system": "raas",
    "frank-starling": "frank starling", "frank-starling law": "frank starling",
    "frank-starling mechanism": "frank starling", "frank starling law": "frank starling",
    "frank starling mechanism": "frank starling", "starling curve": "frank starling",
    "thick ascending limb": "loop of henle", "henle loop": "loop of henle",
    "coagulation": "coagulation cascade", "clotting cascade": "coagulation cascade",
    "coagulation pathway": "coagulation cascade",
    "cardiac action potential": "action potential", "neuronal action potential": "action potential",
    "juxtaglomerular cells": "juxtaglomerular apparatus", "macula densa": "juxtaglomerular apparatus",
    "lung lobes": "lung anatomy", "bronchopulmonary segments": "lung anatomy",
    "bronchopulmonary segment": "lung anatomy",
    "esophageal hiatus": "diaphragm", "aortic hiatus": "diaphragm", "caval hiatus": "diaphragm",
    "anterior mediastinum": "mediastinum", "middle mediastinum": "mediastinum",
    "posterior mediastinum": "mediastinum", "superior mediastinum": "mediastinum",
    "couinaud segments": "liver anatomy", "hepatic acinus": "liver anatomy",
    "liver zones": "liver anatomy", "hepatic zones": "liver anatomy",
    "hepatic lobule": "liver anatomy", "liver lobule": "liver anatomy",
    "portal vein": "portal circulation", "hepatic portal system": "portal circulation",
    "portal venous system": "portal circulation",
    "portosystemic anastomoses": "portal circulation", "portocaval anastomoses": "portal circulation",
    "gastric anatomy": "stomach anatomy",
    "pancreatic anatomy": "pancreas anatomy", "islets of langerhans": "pancreas anatomy",
    "dermatomal map": "dermatomes",
    "cardiac valves": "heart valves", "valves of the heart": "heart valves",
    "conduction system": "cardiac conduction system", "sa node": "cardiac conduction system",
    "av node": "cardiac conduction system", "sinoatrial node": "cardiac conduction system",
    "atrioventricular node": "cardiac conduction system", "bundle of his": "cardiac conduction system",
    "purkinje fibers": "cardiac conduction system",
    "lymph node drainage": "lymph node regions", "lymphatic drainage": "lymph node regions",
    # Upper limb
    "hand of benediction": "median nerve", "ape hand": "median nerve",
    "anterior interosseous nerve": "median nerve", "thenar muscles": "median nerve",
    "recurrent branch of the median nerve": "median nerve",
    "cubital tunnel": "ulnar nerve", "funny bone": "ulnar nerve", "ulnar claw": "ulnar nerve",
    "claw hand": "ulnar nerve", "froment sign": "ulnar nerve", "hypothenar muscles": "ulnar nerve",
    "wrist drop": "radial nerve", "saturday night palsy": "radial nerve",
    "posterior interosseous nerve": "radial nerve", "radial groove": "radial nerve",
    "spiral groove": "radial nerve",
    "regimental badge": "axillary nerve",
    "lateral antebrachial cutaneous nerve": "musculocutaneous nerve",
    "winged scapula": "long thoracic nerve", "serratus anterior": "long thoracic nerve",
    "suprascapular notch": "suprascapular nerve",
    "sits muscles": "rotator cuff", "supraspinatus": "rotator cuff", "infraspinatus": "rotator cuff",
    "teres minor": "rotator cuff", "subscapularis": "rotator cuff",
    "shoulder joint": "glenohumeral joint", "shoulder dislocation": "glenohumeral joint",
    "glenoid labrum": "glenohumeral joint", "bankart lesion": "glenohumeral joint",
    "hill-sachs lesion": "glenohumeral joint",
    "axillary lymph nodes": "axilla", "axillary fossa": "axilla", "thoracodorsal nerve": "axilla",
    "brachial artery": "axillary artery", "scapular anastomosis": "axillary artery",
    "profunda brachii": "axillary artery", "profunda brachii artery": "axillary artery",
    "quadrilateral space": "quadrangular space", "triangular space": "quadrangular space",
    "triangular interval": "quadrangular space",
    "surgical neck of the humerus": "humerus", "surgical neck": "humerus",
    "intertubercular groove": "humerus", "supracondylar fracture": "humerus",
    "median cubital vein": "cubital fossa", "bicipital aponeurosis": "cubital fossa",
    "snuffbox": "anatomical snuffbox", "anatomic snuffbox": "anatomical snuffbox",
    "carpal bones": "scaphoid", "scaphoid fracture": "scaphoid", "lunate": "scaphoid",
    "hook of hamate": "scaphoid",
    "guyon's canal": "guyon canal", "ulnar tunnel": "guyon canal",
    "palmar interossei": "interossei", "dorsal interossei": "interossei",
    "interosseous muscles": "interossei", "lumbricals": "interossei",
    "lumbrical muscles": "interossei",
    # Lower limb
    "saphenous nerve": "femoral nerve",
    "common fibular nerve": "common peroneal nerve", "peroneal nerve": "common peroneal nerve",
    "fibular nerve": "common peroneal nerve", "deep peroneal nerve": "common peroneal nerve",
    "deep fibular nerve": "common peroneal nerve",
    "superficial peroneal nerve": "common peroneal nerve",
    "superficial fibular nerve": "common peroneal nerve", "foot drop": "common peroneal nerve",
    "trendelenburg gait": "superior gluteal nerve", "gluteus medius": "superior gluteal nerve",
    "gluteal injection": "superior gluteal nerve",
    "gluteus maximus": "inferior gluteal nerve",
    "lesser sciatic foramen": "greater sciatic foramen", "piriformis": "greater sciatic foramen",
    "femoral head": "hip joint", "femoral neck": "hip joint",
    "medial circumflex femoral artery": "hip joint", "iliofemoral ligament": "hip joint",
    "hip dislocation": "hip joint",
    "compartments of the thigh": "thigh compartments", "hamstrings": "thigh compartments",
    "hamstring muscles": "thigh compartments", "quadriceps": "thigh compartments",
    "quadriceps femoris": "thigh compartments", "pes anserinus": "thigh compartments",
    "hunter canal": "adductor canal", "hunter's canal": "adductor canal",
    "subsartorial canal": "adductor canal", "adductor hiatus": "adductor canal",
    "popliteal artery": "popliteal fossa",
    "acl": "knee ligaments", "anterior cruciate ligament": "knee ligaments",
    "pcl": "knee ligaments", "posterior cruciate ligament": "knee ligaments",
    "mcl": "knee ligaments", "medial collateral ligament": "knee ligaments",
    "lcl": "knee ligaments", "lateral collateral ligament": "knee ligaments",
    "meniscus": "knee ligaments", "menisci": "knee ligaments",
    "medial meniscus": "knee ligaments", "lateral meniscus": "knee ligaments",
    "unhappy triad": "knee ligaments", "knee joint": "knee ligaments",
    "atfl": "ankle ligaments", "anterior talofibular ligament": "ankle ligaments",
    "deltoid ligament": "ankle ligaments", "ankle joint": "ankle ligaments",
    "compartments of the leg": "leg compartments", "leg compartment": "leg compartments",
    "saphenous vein": "great saphenous vein", "long saphenous vein": "great saphenous vein",
    "small saphenous vein": "great saphenous vein",
    # Thorax
    "intercostal muscles": "intercostal space", "intercostal nerve": "intercostal space",
    "intercostal neurovascular bundle": "intercostal space", "costal groove": "intercostal space",
    "triangle of safety": "intercostal space",
    "parietal pleura": "pleura", "visceral pleura": "pleura", "pleural cavity": "pleura",
    "costodiaphragmatic recess": "pleura", "pleural reflections": "pleura", "cupula": "pleura",
    "transverse pericardial sinus": "pericardium", "oblique pericardial sinus": "pericardium",
    "transverse sinus of the pericardium": "pericardium",
    "fibrous pericardium": "pericardium", "serous pericardium": "pericardium",
    "pericardial cavity": "pericardium",
    "heart borders": "heart surfaces", "borders of the heart": "heart surfaces",
    "cardiac borders": "heart surfaces", "heart chambers": "heart surfaces",
    "phrenic nerves": "phrenic nerve",
    "cn x": "vagus nerve", "cranial nerve x": "vagus nerve", "vagal trunks": "vagus nerve",
    "recurrent laryngeal nerves": "recurrent laryngeal nerve",
    "inferior laryngeal nerve": "recurrent laryngeal nerve",
    "superior laryngeal nerve": "recurrent laryngeal nerve",
    "external laryngeal nerve": "recurrent laryngeal nerve",
    "cisterna chyli": "thoracic duct", "chylothorax": "thoracic duct",
    "azygos": "azygos vein", "hemiazygos vein": "azygos vein", "azygos system": "azygos vein",
    "angle of louis": "sternal angle", "manubriosternal joint": "sternal angle",
    "transverse thoracic plane": "sternal angle",
    "breast lymphatics": "breast anatomy", "mammary gland": "breast anatomy",
    "cooper ligaments": "breast anatomy", "cooper's ligaments": "breast anatomy",
    "axillary tail": "breast anatomy",
    "aortic arch": "aortic arch branches", "arch of the aorta": "aortic arch branches",
    "subclavian artery": "aortic arch branches", "brachiocephalic trunk": "aortic arch branches",
    "ligamentum arteriosum": "aortic arch branches",
    # Abdomen
    "retroperitoneal organs": "peritoneum", "intraperitoneal organs": "peritoneum",
    "retroperitoneum": "peritoneum", "peritoneal cavity": "peritoneum",
    "parietal peritoneum": "peritoneum", "visceral peritoneum": "peritoneum",
    "omental bursa": "lesser sac", "epiploic foramen": "lesser sac",
    "foramen of winslow": "lesser sac", "pringle maneuver": "lesser sac",
    "hepatoduodenal ligament": "lesser sac", "lesser omentum": "lesser sac",
    "greater omentum": "lesser sac", "greater sac": "lesser sac",
    "celiac artery": "celiac trunk", "celiac axis": "celiac trunk",
    "common hepatic artery": "celiac trunk", "splenic artery": "celiac trunk",
    "left gastric artery": "celiac trunk", "gastroduodenal artery": "celiac trunk",
    "marginal artery of drummond": "inferior mesenteric artery",
    "watershed areas": "inferior mesenteric artery",
    "abdominal aorta": "abdominal aorta branches", "aortic bifurcation": "abdominal aorta branches",
    "renal artery": "abdominal aorta branches", "gonadal artery": "abdominal aorta branches",
    "gonadal vein": "abdominal aorta branches",
    "calot triangle": "hepatocystic triangle", "calot's triangle": "hepatocystic triangle",
    "triangle of calot": "hepatocystic triangle", "cystohepatic triangle": "hepatocystic triangle",
    "cystic artery": "hepatocystic triangle", "critical view of safety": "hepatocystic triangle",
    "bile ducts": "biliary tree", "bile duct": "biliary tree", "common bile duct": "biliary tree",
    "cystic duct": "biliary tree", "common hepatic duct": "biliary tree",
    "ampulla of vater": "biliary tree", "hepatopancreatic ampulla": "biliary tree",
    "sphincter of oddi": "biliary tree", "gallbladder": "biliary tree",
    "biliary system": "biliary tree",
    "ligament of treitz": "duodenum", "duodenal bulb": "duodenum",
    "suspensory ligament of the duodenum": "duodenum",
    "splenic hilum": "spleen", "gastrosplenic ligament": "spleen",
    "splenorenal ligament": "spleen", "red pulp": "spleen", "white pulp": "spleen",
    "kidneys": "kidney anatomy", "renal anatomy": "kidney anatomy",
    "renal hilum": "kidney anatomy", "gerota fascia": "kidney anatomy",
    "gerota's fascia": "kidney anatomy", "renal fascia": "kidney anatomy",
    "left renal vein": "kidney anatomy",
    "ureters": "ureter", "water under the bridge": "ureter",
    "ureterovesical junction": "ureter", "ureteropelvic junction": "ureter",
    "adrenal glands": "adrenal gland", "suprarenal gland": "adrenal gland",
    "suprarenal glands": "adrenal gland", "adrenal cortex": "adrenal gland",
    "adrenal medulla": "adrenal gland", "zona glomerulosa": "adrenal gland",
    "zona fasciculata": "adrenal gland", "zona reticularis": "adrenal gland",
    "anterior abdominal wall": "abdominal wall", "abdominal wall layers": "abdominal wall",
    "scarpa fascia": "abdominal wall", "scarpa's fascia": "abdominal wall",
    "camper fascia": "abdominal wall", "linea alba": "abdominal wall",
    "external oblique": "abdominal wall", "internal oblique": "abdominal wall",
    "transversus abdominis": "abdominal wall", "transversalis fascia": "abdominal wall",
    "arcuate line": "rectus sheath", "rectus abdominis": "rectus sheath",
    "inferior epigastric artery": "rectus sheath", "inferior epigastric vessels": "rectus sheath",
    "median umbilical ligament": "umbilical folds", "medial umbilical ligament": "umbilical folds",
    "medial umbilical ligaments": "umbilical folds", "urachus": "umbilical folds",
    "falciform ligament": "umbilical folds", "ligamentum teres": "umbilical folds",
    "vermiform appendix": "appendix", "appendicular artery": "appendix",
    "mesoappendix": "appendix",
    "dentate line": "pectinate line", "anal canal": "pectinate line",
    # Pelvis
    "levator ani": "pelvic floor", "pelvic diaphragm": "pelvic floor",
    "perineal body": "pelvic floor", "puborectalis": "pelvic floor",
    "alcock canal": "pudendal nerve", "alcock's canal": "pudendal nerve",
    "pudendal canal": "pudendal nerve", "pudendal nerve block": "pudendal nerve",
    "nervi erigentes": "pelvic splanchnic nerves", "pelvic splanchnics": "pelvic splanchnic nerves",
    "point and shoot": "pelvic splanchnic nerves",
    "point, squeeze and shoot": "pelvic splanchnic nerves",
    "broad ligament": "uterine ligaments", "round ligament": "uterine ligaments",
    "round ligament of the uterus": "uterine ligaments", "cardinal ligament": "uterine ligaments",
    "uterosacral ligament": "uterine ligaments",
    "suspensory ligament of the ovary": "uterine ligaments",
    "infundibulopelvic ligament": "uterine ligaments", "ovarian ligament": "uterine ligaments",
    "prostate": "prostate gland", "prostate zones": "prostate gland",
    "peripheral zone": "prostate gland", "transition zone": "prostate gland",
    "urethra": "male urethra", "membranous urethra": "male urethra",
    "spongy urethra": "male urethra", "penile urethra": "male urethra",
    "prostatic urethra": "male urethra",
    "pouch of douglas": "rectouterine pouch", "rectovesical pouch": "rectouterine pouch",
    "vesicouterine pouch": "rectouterine pouch",
    "internal iliac arteries": "internal iliac artery", "uterine artery": "internal iliac artery",
    "external iliac artery": "internal iliac artery", "corona mortis": "internal iliac artery",
    # Head & neck
    "cn vii": "facial nerve", "cranial nerve vii": "facial nerve",
    "chorda tympani": "facial nerve", "facial nerve branches": "facial nerve",
    "cn v": "trigeminal nerve", "cranial nerve v": "trigeminal nerve",
    "ophthalmic nerve": "trigeminal nerve", "maxillary nerve": "trigeminal nerve",
    "mandibular nerve": "trigeminal nerve", "lingual nerve": "trigeminal nerve",
    "muscles of mastication": "trigeminal nerve",
    "danger triangle of the face": "cavernous sinus", "danger triangle": "cavernous sinus",
    "scalp": "scalp layers", "galea aponeurotica": "scalp layers",
    "epidural hematoma": "middle meningeal artery", "foramen spinosum": "middle meningeal artery",
    "venous sinuses": "dural venous sinuses", "superior sagittal sinus": "dural venous sinuses",
    "transverse sinus": "dural venous sinuses", "sigmoid sinus": "dural venous sinuses",
    "straight sinus": "dural venous sinuses", "confluence of sinuses": "dural venous sinuses",
    "bridging veins": "dural venous sinuses",
    "triangles of the neck": "neck triangles", "anterior triangle": "neck triangles",
    "posterior triangle": "neck triangles", "anterior triangle of the neck": "neck triangles",
    "posterior triangle of the neck": "neck triangles", "carotid triangle": "neck triangles",
    "spinal accessory nerve": "neck triangles", "accessory nerve": "neck triangles",
    "cn xi": "neck triangles", "erb point": "neck triangles", "erb's point": "neck triangles",
    "carotid sinus": "carotid sheath", "carotid body": "carotid sheath",
    "carotid bifurcation": "carotid sheath", "internal jugular vein": "carotid sheath",
    "common carotid artery": "carotid sheath", "internal carotid artery": "carotid sheath",
    "kiesselbach plexus": "external carotid artery", "maxillary artery": "external carotid artery",
    "superficial temporal artery": "external carotid artery",
    "facial artery": "external carotid artery",
    "thyroid anatomy": "thyroid gland", "thyroglossal duct": "thyroid gland",
    "parathyroid glands": "thyroid gland", "parathyroid gland": "thyroid gland",
    "inferior thyroid artery": "thyroid gland", "superior thyroid artery": "thyroid gland",
    "cricothyroid membrane": "larynx", "posterior cricoarytenoid": "larynx",
    "vocal folds": "larynx", "vocal cords": "larynx", "cricoid cartilage": "larynx",
    "thyroid cartilage": "larynx", "laryngeal muscles": "larynx",
    "eye muscles": "extraocular muscles", "extraocular movements": "extraocular muscles",
    "superior oblique": "extraocular muscles", "inferior oblique": "extraocular muscles",
    "lateral rectus": "extraocular muscles", "medial rectus": "extraocular muscles",
    "superior rectus": "extraocular muscles", "inferior rectus": "extraocular muscles",
    "levator palpebrae superioris": "extraocular muscles",
    "cranial foramina": "skull foramina", "foramina of the skull": "skull foramina",
    "jugular foramen": "skull foramina", "superior orbital fissure": "skull foramina",
    "foramen rotundum": "skull foramina", "internal acoustic meatus": "skull foramina",
    "foramen magnum": "skull foramina", "optic canal": "skull foramina",
    "cribriform plate": "skull foramina", "hypoglossal canal": "skull foramina",
    "parotid": "parotid gland", "parotid duct": "parotid gland",
    "stensen duct": "parotid gland", "stensen's duct": "parotid gland",
    "tongue": "tongue innervation", "hypoglossal nerve": "tongue innervation",
    "cn xii": "tongue innervation", "glossopharyngeal nerve": "tongue innervation",
    "cn ix": "tongue innervation",
    "branchial arches": "pharyngeal arches", "pharyngeal pouches": "pharyngeal arches",
    "pharyngeal arch": "pharyngeal arches", "branchial arch": "pharyngeal arches",
    "pharyngeal clefts": "pharyngeal arches", "pharyngeal pouch": "pharyngeal arches",
    # Back & spine
    "vertebrae": "vertebral column", "vertebra": "vertebral column",
    "spinal column": "vertebral column", "ligamentum flavum": "vertebral column",
    "anterior longitudinal ligament": "vertebral column",
    "posterior longitudinal ligament": "vertebral column",
    "spondylolisthesis": "vertebral column", "spondylolysis": "vertebral column",
    "intervertebral discs": "intervertebral disc", "nucleus pulposus": "intervertebral disc",
    "annulus fibrosus": "intervertebral disc", "disc herniation": "intervertebral disc",
    "herniated disc": "intervertebral disc",
    "spinal tap": "lumbar puncture", "conus medullaris": "lumbar puncture",
    "cauda equina": "lumbar puncture", "epidural space": "lumbar puncture",
    "subarachnoid space": "lumbar puncture", "tuffier line": "lumbar puncture",
    "tuffier's line": "lumbar puncture",
    # Neuroanatomy
    "anterior cerebral artery": "cerebral arteries", "middle cerebral artery": "cerebral arteries",
    "posterior cerebral artery": "cerebral arteries", "lenticulostriate arteries": "cerebral arteries",
    "basilar artery": "cerebral arteries", "vertebral artery": "cerebral arteries",
    "cerebral artery territories": "cerebral arteries",
    "ventricles of the brain": "ventricular system", "csf flow": "ventricular system",
    "csf circulation": "ventricular system", "cerebral aqueduct": "ventricular system",
    "foramen of monro": "ventricular system", "choroid plexus": "ventricular system",
    "fourth ventricle": "ventricular system", "third ventricle": "ventricular system",
    "lateral ventricles": "ventricular system", "arachnoid granulations": "ventricular system",
    "striatum": "basal ganglia", "caudate nucleus": "basal ganglia", "putamen": "basal ganglia",
    "globus pallidus": "basal ganglia", "substantia nigra": "basal ganglia",
    "subthalamic nucleus": "basal ganglia", "direct pathway": "basal ganglia",
    "indirect pathway": "basal ganglia",
    "brain stem": "brainstem", "rule of 4s": "brainstem", "rule of fours": "brainstem",
    "medulla oblongata": "brainstem", "medial medullary syndrome": "brainstem",
    "medial medullary": "brainstem",
    "weber syndrome": "brainstem",
    "cerebellar peduncles": "cerebellum", "deep cerebellar nuclei": "cerebellum",
    "purkinje cells": "cerebellum", "cerebellar vermis": "cerebellum",
    "vpl": "thalamus", "vpm": "thalamus", "lgn": "thalamus", "mgn": "thalamus",
    "lateral geniculate nucleus": "thalamus", "medial geniculate nucleus": "thalamus",
    "thalamic nuclei": "thalamus",
    "hypothalamic nuclei": "hypothalamus", "suprachiasmatic nucleus": "hypothalamus",
    "supraoptic nucleus": "hypothalamus", "paraventricular nucleus": "hypothalamus",
    "ventromedial nucleus": "hypothalamus", "arcuate nucleus": "hypothalamus",
    "hippocampus": "limbic system", "amygdala": "limbic system",
    "papez circuit": "limbic system", "mammillary bodies": "limbic system",
    "cingulate gyrus": "limbic system",
    "visual pathways": "visual pathway", "optic chiasm": "visual pathway",
    "optic tract": "visual pathway", "optic radiations": "visual pathway",
    "meyer loop": "visual pathway", "meyer's loop": "visual pathway",
    "visual field defects": "visual pathway", "bitemporal hemianopia": "visual pathway",
    "homonymous hemianopia": "visual pathway", "pupillary light reflex": "visual pathway",
    "broca area": "cerebral cortex", "broca's area": "cerebral cortex",
    "wernicke area": "cerebral cortex", "wernicke's area": "cerebral cortex",
    "brodmann areas": "cerebral cortex", "motor cortex": "cerebral cortex",
    "primary motor cortex": "cerebral cortex", "somatosensory cortex": "cerebral cortex",
    "homunculus": "cerebral cortex", "frontal lobe": "cerebral cortex",
    "parietal lobe": "cerebral cortex", "temporal lobe": "cerebral cortex",
    "occipital lobe": "cerebral cortex", "arcuate fasciculus": "cerebral cortex",
    "prefrontal cortex": "cerebral cortex", "broca aphasia": "cerebral cortex",
    "wernicke aphasia": "cerebral cortex",
    "dura mater": "meninges", "arachnoid mater": "meninges", "pia mater": "meninges",
    "falx cerebri": "meninges", "tentorium cerebelli": "meninges",
    "subdural hematoma": "meninges", "subdural space": "meninges",
    "uncal herniation": "meninges", "brain herniation": "meninges",
    "spinal cord": "spinal cord anatomy", "anterior spinal artery": "spinal cord anatomy",
    "artery of adamkiewicz": "spinal cord anatomy", "adamkiewicz artery": "spinal cord anatomy",
    "spinal nerves": "spinal cord anatomy", "spinal nerve": "spinal cord anatomy",
    "anterior horn": "spinal cord anatomy", "ventral horn": "spinal cord anatomy",
    "dorsal horn": "spinal cord anatomy", "lateral horn": "spinal cord anatomy",
    "anterior spinal artery syndrome": "spinal cord anatomy",
    "sympathetic nervous system": "autonomic nervous system",
    "parasympathetic nervous system": "autonomic nervous system",
    "sympathetic trunk": "autonomic nervous system", "sympathetic chain": "autonomic nervous system",
    "splanchnic nerves": "autonomic nervous system",
    "greater splanchnic nerve": "autonomic nervous system",
    "ciliary ganglion": "autonomic nervous system", "otic ganglion": "autonomic nervous system",
    "pterygopalatine ganglion": "autonomic nervous system",
    "submandibular ganglion": "autonomic nervous system", "referred pain": "autonomic nervous system",
    "reflexes": "deep tendon reflexes", "tendon reflexes": "deep tendon reflexes",
    "stretch reflex": "deep tendon reflexes", "patellar reflex": "deep tendon reflexes",
    "knee jerk": "deep tendon reflexes", "ankle jerk": "deep tendon reflexes",
    "achilles reflex": "deep tendon reflexes", "biceps reflex": "deep tendon reflexes",
    "triceps reflex": "deep tendon reflexes", "cremasteric reflex": "deep tendon reflexes",
    "anterior cranial fossa": "cranial fossae", "middle cranial fossa": "cranial fossae",
    "posterior cranial fossa": "cranial fossae", "sella turcica": "cranial fossae",
    "basilar skull fracture": "cranial fossae", "cranial fossa": "cranial fossae",
    # Embryology
    "ectoderm": "germ layers", "mesoderm": "germ layers", "endoderm": "germ layers",
    "gastrulation": "germ layers", "trilaminar disc": "germ layers",
    "primitive streak": "germ layers", "notochord": "germ layers",
    "germ layer derivatives": "germ layers",
    "neural crest cells": "neural crest", "neural crest derivatives": "neural crest",
    "neurulation": "neural tube", "neural tube defects": "neural tube",
    "neural tube defect": "neural tube", "spina bifida": "neural tube",
    "myelomeningocele": "neural tube", "anencephaly": "neural tube",
    "brain vesicles": "neural tube", "prosencephalon": "neural tube",
    "rhombencephalon": "neural tube",
    "fetal circulation remnants": "fetal circulation", "fetal remnants": "fetal circulation",
    "ductus venosus": "fetal circulation", "ductus arteriosus": "fetal circulation",
    "umbilical vein": "fetal circulation", "umbilical arteries": "fetal circulation",
    "fossa ovalis": "fetal circulation", "ligamentum venosum": "fetal circulation",
    "cardiac development": "heart embryology", "heart development": "heart embryology",
    "truncus arteriosus": "heart embryology", "bulbus cordis": "heart embryology",
    "sinus venosus": "heart embryology", "septum primum": "heart embryology",
    "septum secundum": "heart embryology", "endocardial cushions": "heart embryology",
    "aorticopulmonary septum": "heart embryology",
    "aortic arches": "aortic arch derivatives", "pharyngeal arch arteries": "aortic arch derivatives",
    "foregut": "gut development", "midgut": "gut development", "hindgut": "gut development",
    "midgut rotation": "gut development", "gut rotation": "gut development",
    "meckel diverticulum": "gut development", "meckel's diverticulum": "gut development",
    "vitelline duct": "gut development", "rule of 2s": "gut development",
    "kidney development": "urogenital development", "pronephros": "urogenital development",
    "mesonephros": "urogenital development", "metanephros": "urogenital development",
    "ureteric bud": "urogenital development", "wolffian duct": "urogenital development",
    "mesonephric duct": "urogenital development", "mullerian duct": "urogenital development",
    "müllerian duct": "urogenital development", "paramesonephric duct": "urogenital development",
    "genital development": "urogenital development",
    "sexual differentiation": "urogenital development",
    # More gross anatomy
    "collarbone": "clavicle", "clavicle fracture": "clavicle",
    "acromioclavicular joint": "clavicle", "sternoclavicular joint": "clavicle",
    "annular ligament": "elbow joint", "nursemaid elbow": "elbow joint",
    "nursemaid's elbow": "elbow joint", "pulled elbow": "elbow joint",
    "radial head subluxation": "elbow joint", "carrying angle": "elbow joint",
    "ulnar collateral ligament": "elbow joint",
    "forearm muscles": "forearm compartments", "tennis elbow": "forearm compartments",
    "golfer's elbow": "forearm compartments", "lateral epicondylitis": "forearm compartments",
    "medial epicondylitis": "forearm compartments", "volkmann contracture": "forearm compartments",
    "de quervain tenosynovitis": "forearm compartments",
    "common flexor origin": "forearm compartments", "common extensor origin": "forearm compartments",
    "superficial palmar arch": "palmar arches", "deep palmar arch": "palmar arches",
    "palmar arch": "palmar arches", "radial artery": "palmar arches",
    "ulnar artery": "palmar arches",
    "femoral pulse": "femoral artery", "profunda femoris": "femoral artery",
    "deep femoral artery": "femoral artery", "femoral vein": "femoral artery",
    "lumbosacral plexus": "sacral plexus", "lumbosacral trunk": "sacral plexus",
    "arches of the foot": "foot arches", "plantar fascia": "foot arches",
    "plantar aponeurosis": "foot arches", "plantar fasciitis": "foot arches",
    "achilles tendon": "foot arches", "calcaneal tendon": "foot arches",
    "flat foot": "foot arches", "flatfoot": "foot arches", "spring ligament": "foot arches",
    "thompson test": "foot arches",
    "esophageal constrictions": "esophagus", "lower esophageal sphincter": "esophagus",
    "upper esophageal sphincter": "esophagus", "killian triangle": "esophagus",
    "jejunum": "small intestine", "ileum": "small intestine", "terminal ileum": "small intestine",
    "peyer patches": "small intestine", "peyer's patches": "small intestine",
    "plicae circulares": "small intestine", "vasa recta": "small intestine",
    "colon": "colon anatomy", "large intestine": "colon anatomy",
    "large bowel": "colon anatomy", "taeniae coli": "colon anatomy",
    "haustra": "colon anatomy", "cecum": "colon anatomy", "sigmoid colon": "colon anatomy",
    "transverse colon": "colon anatomy", "splenic flexure": "colon anatomy",
    "hepatic flexure": "colon anatomy",
    "testis": "testis anatomy", "testes": "testis anatomy", "testicle": "testis anatomy",
    "spermatic cord": "testis anatomy", "pampiniform plexus": "testis anatomy",
    "gubernaculum": "testis anatomy", "processus vaginalis": "testis anatomy",
    "tunica vaginalis": "testis anatomy", "testicular descent": "testis anatomy",
    "testicular artery": "testis anatomy", "testicular vein": "testis anatomy",
    "ovary": "female reproductive anatomy", "ovaries": "female reproductive anatomy",
    "uterus": "female reproductive anatomy", "uterine tube": "female reproductive anatomy",
    "uterine tubes": "female reproductive anatomy",
    "fallopian tube": "female reproductive anatomy",
    "fallopian tubes": "female reproductive anatomy", "cervix": "female reproductive anatomy",
    "vagina": "female reproductive anatomy",
    "urinary bladder": "bladder", "detrusor": "bladder", "trigone": "bladder",
    "micturition": "bladder", "micturition reflex": "bladder",
    "urogenital triangle": "perineum", "anal triangle": "perineum",
    "ischioanal fossa": "perineum", "ischiorectal fossa": "perineum",
    "superficial perineal pouch": "perineum", "deep perineal pouch": "perineum",
    "perineal membrane": "perineum", "bartholin gland": "perineum",
    "pelvic bone": "bony pelvis", "hip bone": "bony pelvis",
    "pelvic inlet": "bony pelvis", "pelvic outlet": "bony pelvis",
    "ischial spine": "bony pelvis", "obstetric conjugate": "bony pelvis",
    "sacral promontory": "bony pelvis", "gynecoid pelvis": "bony pelvis",
    "tmj": "temporomandibular joint", "jaw joint": "temporomandibular joint",
    "articular disc": "temporomandibular joint",
    "ossicles": "middle ear", "malleus": "middle ear", "incus": "middle ear",
    "stapes": "middle ear", "tympanic membrane": "middle ear", "eardrum": "middle ear",
    "eustachian tube": "middle ear", "auditory tube": "middle ear",
    "tympanic cavity": "middle ear",
    "maxillary sinus": "paranasal sinuses", "frontal sinus": "paranasal sinuses",
    "ethmoid sinus": "paranasal sinuses", "ethmoid air cells": "paranasal sinuses",
    "sphenoid sinus": "paranasal sinuses", "nasolacrimal duct": "paranasal sinuses",
    "nasopharynx": "pharynx", "oropharynx": "pharynx", "laryngopharynx": "pharynx",
    "hypopharynx": "pharynx", "pharyngeal constrictors": "pharynx",
    "palatine tonsil": "pharynx", "tonsils": "pharynx", "gag reflex": "pharynx",
    "piriform recess": "pharynx", "adenoids": "pharynx",
    "eyeball": "eye anatomy", "retina": "eye anatomy", "iris": "eye anatomy",
    "cornea": "eye anatomy", "ciliary body": "eye anatomy", "aqueous humor": "eye anatomy",
    "canal of schlemm": "eye anatomy", "uvea": "eye anatomy", "fovea": "eye anatomy",
    "optic disc": "eye anatomy", "lacrimal gland": "eye anatomy",
    # Histology
    "epithelium": "epithelium types", "epithelial tissue": "epithelium types",
    "simple squamous epithelium": "epithelium types",
    "pseudostratified columnar epithelium": "epithelium types",
    "transitional epithelium": "epithelium types", "urothelium": "epithelium types",
    "stratified squamous epithelium": "epithelium types",
    "tight junction": "cell junctions", "tight junctions": "cell junctions",
    "desmosome": "cell junctions", "desmosomes": "cell junctions",
    "gap junction": "cell junctions", "gap junctions": "cell junctions",
    "hemidesmosome": "cell junctions", "hemidesmosomes": "cell junctions",
    "adherens junction": "cell junctions", "zonula occludens": "cell junctions",
    "e-cadherin": "cell junctions",
    "collagen": "collagen types", "type i collagen": "collagen types",
    "type iv collagen": "collagen types", "collagen synthesis": "collagen types",
    "skeletal muscle": "muscle tissue types", "cardiac muscle": "muscle tissue types",
    "smooth muscle": "muscle tissue types", "sarcomere": "muscle tissue types",
    "intercalated discs": "muscle tissue types", "muscle types": "muscle tissue types",
}
