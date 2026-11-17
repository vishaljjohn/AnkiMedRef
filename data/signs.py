"""Clinical signs & eponyms and alternate names (tier 0.5m).

Edit freely — see data/__init__.py for how files are loaded."""
from ..formatters import _sg


_SIGNS = {
    # ── Abdomen / GI ──────────────────────────────────────────────────────────
    "murphy sign": _sg(
        "Inspiratory arrest from pain while palpating under the right costal margin",
        "Acute cholecystitis",
        "Sonographic Murphy sign = maximal tenderness when the probe presses on the gallbladder. Often absent in the elderly."),
    "mcburney sign": _sg(
        "Maximal tenderness at McBurney point — one-third of the way from the right ASIS to the umbilicus",
        "Acute appendicitis"),
    "rovsing sign": _sg(
        "Pressure in the left lower quadrant causes pain in the right lower quadrant",
        "Acute appendicitis (peritoneal irritation)"),
    "psoas sign": _sg(
        "RLQ pain on passive extension of the right hip (patient lying on the left side) or on flexion against resistance",
        "Retrocecal appendicitis; also psoas abscess"),
    "obturator sign": _sg(
        "RLQ / pelvic pain on passive internal rotation of the flexed right hip",
        "Pelvic appendicitis (inflamed appendix touching obturator internus)"),
    "blumberg sign": _sg(
        "Rebound tenderness — pain is worse when pressure is suddenly released",
        "Peritonitis"),
    "rebound tenderness": _sg(
        "Pain is worse when pressure on the abdomen is suddenly released (Blumberg sign)",
        "Peritonitis"),
    "kehr sign": _sg(
        "Referred pain to the tip of the left shoulder",
        "Splenic rupture or other blood/irritation under the left hemidiaphragm (phrenic nerve, C3–C5)"),
    "cullen sign": _sg(
        "Periumbilical ecchymosis",
        "Intra-/retroperitoneal hemorrhage — hemorrhagic pancreatitis, ruptured ectopic pregnancy",
        "Grey Turner = flank bruising; both appear 24–48 h after bleeding starts."),
    "grey turner sign": _sg(
        "Flank ecchymosis",
        "Retroperitoneal hemorrhage — hemorrhagic pancreatitis, ruptured AAA",
        "Cullen = periumbilical bruising. Both are late signs (24–48 h)."),
    "courvoisier sign": _sg(
        "Palpable, non-tender gallbladder in a jaundiced patient",
        "Malignant distal CBD obstruction (pancreatic head cancer, cholangiocarcinoma) rather than stones",
        "Gallstones cause chronic fibrosis, so a stone-filled gallbladder rarely distends."),
    "charcot triad": _sg(
        "Fever + jaundice + RUQ pain",
        "Ascending cholangitis",
        "Add hypotension + altered mental status → Reynolds pentad (suppurative cholangitis) → urgent biliary decompression (ERCP)."),
    "reynolds pentad": _sg(
        "Charcot triad (fever, jaundice, RUQ pain) + hypotension + altered mental status",
        "Acute suppurative (obstructive) cholangitis — septic, needs urgent ERCP decompression"),
    "caput medusae": _sg(
        "Dilated veins radiating from the umbilicus",
        "Portal hypertension (paraumbilical ↔ superficial epigastric veins)"),
    "asterixis": _sg(
        "Flapping tremor of the outstretched, dorsiflexed hands (lapses in posture)",
        "Metabolic encephalopathy — hepatic encephalopathy, uremia, CO2 retention"),
    "dance sign": _sg(
        "Empty right lower quadrant on palpation, often with a sausage-shaped RUQ mass",
        "Intussusception (ileocolic)",
        "Classic triad: colicky pain, sausage-shaped mass, currant-jelly stool; target sign on ultrasound."),
    "hamman sign": _sg(
        "Crunching sound synchronous with the heartbeat (mediastinal crunch)",
        "Pneumomediastinum — e.g. Boerhaave esophageal rupture, asthma, trauma"),
    "virchow node": _sg(
        "Enlarged left supraclavicular lymph node (Troisier sign)",
        "Abdominal malignancy, classically gastric cancer (drains via the thoracic duct)"),
    "sister mary joseph nodule": _sg(
        "Hard periumbilical nodule",
        "Metastatic intra-abdominal or pelvic cancer — gastric, ovarian, pancreatic, colorectal"),
    "leser-trelat sign": _sg(
        "Sudden eruption of many seborrheic keratoses",
        "Internal malignancy, usually GI adenocarcinoma"),
    # ── Cardiovascular ────────────────────────────────────────────────────────
    "beck triad": _sg(
        "Hypotension + distended neck veins (↑JVP) + muffled heart sounds",
        "Cardiac tamponade",
        "Also pulsus paradoxus and electrical alternans. Treat with pericardiocentesis."),
    "pulsus paradoxus": _sg(
        "Inspiratory fall in systolic BP > 10 mmHg",
        "Cardiac tamponade; also severe asthma/COPD, less often constrictive pericarditis"),
    "kussmaul sign": _sg(
        "Paradoxical rise in JVP on inspiration",
        "Constrictive pericarditis, restrictive cardiomyopathy, right ventricular infarct",
        "Classically ABSENT in tamponade (distinguishes it from constriction). Not the same as Kussmaul respirations."),
    "cushing triad": _sg(
        "Hypertension (widened pulse pressure) + bradycardia + irregular respirations",
        "Raised intracranial pressure with impending brainstem herniation"),
    "levine sign": _sg(
        "Patient describes chest pain with a clenched fist over the sternum",
        "Ischemic chest pain (angina / MI)"),
    "janeway lesions": _sg(
        "Painless, flat erythematous macules on the palms and soles",
        "Infective endocarditis (septic microemboli)",
        "Janeway = painless; Osler = 'Ouch' (painful)."),
    "osler nodes": _sg(
        "Painful, raised, red nodules on the pads of fingers and toes",
        "Infective endocarditis (immune-complex vasculitis)",
        "Osler = 'Ouch'; Janeway lesions are painless."),
    "roth spots": _sg(
        "Retinal hemorrhages with pale centers",
        "Infective endocarditis; also leukemia, severe anemia"),
    "splinter hemorrhages": _sg(
        "Thin linear hemorrhages under the nails",
        "Infective endocarditis (nonspecific — also trauma)"),
    "de musset sign": _sg(
        "Head bobbing with each heartbeat",
        "Aortic regurgitation (wide pulse pressure)"),
    "corrigan pulse": _sg(
        "Water-hammer pulse — forceful upstroke with rapid collapse",
        "Aortic regurgitation"),
    "quincke pulse": _sg(
        "Visible capillary pulsation in the nail bed with light pressure",
        "Aortic regurgitation"),
    "carvallo sign": _sg(
        "Holosystolic murmur at the left lower sternal border that gets louder with inspiration",
        "Tricuspid regurgitation (right-sided murmurs ↑ with inspiration)"),
    "ewart sign": _sg(
        "Dullness, bronchial breathing and egophony below the left scapula",
        "Large pericardial effusion compressing the left lower lobe"),
    "homans sign": _sg(
        "Calf pain on passive dorsiflexion of the foot",
        "Suggests DVT, but unreliable — use Wells score + D-dimer / compression ultrasound instead"),
    "allen test": _sg(
        "Compress radial and ulnar arteries, then release the ulnar — palm should flush within ~5–10 s",
        "Adequate ulnar collateral flow before radial artery puncture/cannulation"),
    "pemberton sign": _sg(
        "Facial plethora and distended neck veins when both arms are raised",
        "Thoracic inlet obstruction — substernal goiter, SVC obstruction"),
    # ── Neurology ─────────────────────────────────────────────────────────────
    "kernig sign": _sg(
        "With the hip flexed to 90°, resistance/pain on extending the knee",
        "Meningeal irritation (meningitis, subarachnoid hemorrhage)",
        "Low sensitivity, high specificity — a negative sign does not rule out meningitis."),
    "brudzinski sign": _sg(
        "Passive neck flexion causes involuntary flexion of the hips and knees",
        "Meningeal irritation (meningitis, subarachnoid hemorrhage)",
        "Like Kernig: specific but insensitive."),
    "babinski sign": _sg(
        "Stroking the lateral sole makes the great toe extend (upgoing) and the toes fan",
        "Upper motor neuron (corticospinal tract) lesion",
        "Normal in infants up to about 1–2 years."),
    "hoffmann sign": _sg(
        "Flicking the distal phalanx of the middle finger makes the thumb and index finger flex",
        "Upper motor neuron lesion, e.g. cervical myelopathy"),
    "romberg sign": _sg(
        "Stable with eyes open, sways or falls with eyes closed",
        "Loss of proprioception (dorsal columns — B12 deficiency, tabes dorsalis) or vestibular loss",
        "Cerebellar ataxia is unsteady even with eyes open, so Romberg is not 'positive'."),
    "lhermitte sign": _sg(
        "Electric-shock sensation down the spine and limbs on neck flexion",
        "Cervical cord lesion — multiple sclerosis; also B12 deficiency, cervical spondylosis"),
    "uhthoff phenomenon": _sg(
        "Neurological symptoms temporarily worsen with heat (hot shower, exercise, fever)",
        "Multiple sclerosis (heat slows conduction in demyelinated axons)"),
    "marcus gunn pupil": _sg(
        "Swinging flashlight test: the affected pupil dilates when the light swings to it (relative afferent pupillary defect)",
        "Optic nerve lesion — e.g. optic neuritis (MS), severe retinal disease"),
    "argyll robertson pupil": _sg(
        "Small pupils that constrict with accommodation but not to light",
        "Neurosyphilis (tertiary syphilis); also diabetes",
        "'Prostitute's pupil' — accommodates but does not react."),
    "gowers sign": _sg(
        "Child 'climbs up' the legs with the hands to stand from the floor",
        "Proximal (pelvic girdle) muscle weakness, classically Duchenne muscular dystrophy"),
    "trendelenburg sign": _sg(
        "Standing on one leg, the pelvis drops on the opposite (unsupported) side",
        "Weak hip abductors (gluteus medius/minimus) of the standing leg — superior gluteal nerve injury"),
    "tinel sign": _sg(
        "Tapping over a nerve reproduces tingling in its distribution",
        "Nerve compression or regeneration, e.g. median nerve in carpal tunnel syndrome"),
    "phalen test": _sg(
        "Holding the wrists fully flexed for 60 s reproduces numbness in the median nerve distribution",
        "Carpal tunnel syndrome"),
    "battle sign": _sg(
        "Bruising over the mastoid process",
        "Basilar skull fracture (temporal bone / middle cranial fossa)",
        "Raccoon eyes = anterior fossa. Look for CSF otorrhea/rhinorrhea and hemotympanum."),
    "raccoon eyes": _sg(
        "Bilateral periorbital ecchymosis",
        "Basilar skull fracture (anterior cranial fossa); also neuroblastoma metastases, AL amyloidosis"),
    "hutchinson sign": _sg(
        "Zoster vesicles on the tip or side of the nose",
        "Herpes zoster ophthalmicus with nasociliary (V1) involvement → high risk of eye involvement — urgent ophthalmology"),
    "chvostek sign": _sg(
        "Tapping the facial nerve in front of the ear causes twitching of the facial muscles",
        "Hypocalcemia (also hypomagnesemia)",
        "Present in up to 10–25% of normal people — Trousseau sign is more specific."),
    "trousseau sign": _sg(
        "BP cuff inflated above systolic pressure for 3 min causes carpal spasm",
        "Hypocalcemia (more specific than Chvostek)",
        "Not the same as Trousseau syndrome (migratory thrombophlebitis with occult cancer)."),
    "trousseau syndrome": _sg(
        "Recurrent migratory superficial thrombophlebitis",
        "Occult visceral malignancy, classically pancreatic adenocarcinoma (hypercoagulability)"),
    "kussmaul respirations": _sg(
        "Deep, rapid, labored breathing",
        "Respiratory compensation for metabolic acidosis, classically DKA"),
    "kayser-fleischer rings": _sg(
        "Golden-brown ring at the edge of the cornea (copper in Descemet membrane)",
        "Wilson disease — present in ~95% with neurological involvement"),
    "virchow triad": _sg(
        "Stasis + endothelial injury + hypercoagulability",
        "The three factors that promote thrombosis (DVT, PE)"),
    # ── Skin / musculoskeletal ────────────────────────────────────────────────
    "nikolsky sign": _sg(
        "Lateral pressure on the skin makes the epidermis slide off",
        "Intraepidermal / full-thickness separation — pemphigus vulgaris, SSSS, SJS/TEN",
        "NEGATIVE in bullous pemphigoid (subepidermal blister)."),
    "auspitz sign": _sg(
        "Pinpoint bleeding when a scale is scraped off",
        "Psoriasis"),
    "koebner phenomenon": _sg(
        "New lesions appear along lines of skin trauma",
        "Psoriasis, lichen planus, vitiligo, warts"),
    "darier sign": _sg(
        "Rubbing a lesion makes it swell and redden (urticate)",
        "Mastocytosis (urticaria pigmentosa) — mast cell degranulation"),
    "lachman test": _sg(
        "Anterior translation of the tibia with the knee in 20–30° flexion, with a soft end point",
        "Anterior cruciate ligament (ACL) tear",
        "More sensitive than the anterior drawer test."),
    "anterior drawer sign": _sg(
        "Anterior translation of the tibia with the knee flexed 90°",
        "ACL tear (in the ankle: anterior talofibular ligament tear)"),
    "mcmurray test": _sg(
        "Painful click when the flexed knee is rotated and extended",
        "Meniscal tear (external rotation → medial meniscus; internal → lateral)"),
    # ── Obstetric / gynecologic signs ──
    'chadwick sign': _sg(
        'Bluish-purple discoloration of the cervix, vagina and vulva',
        'Early pregnancy (~6–8 weeks) from venous congestion; a PRESUMPTIVE/probable sign — also with pelvic congestion or tumors',
        'Probable signs of pregnancy: Chadwick, Goodell, Hegar, uterine enlargement, positive hCG. Positive signs: fetal heart tones, fetal movement felt by an examiner, ultrasound visualization.',
    ),
    'goodell sign': _sg(
        'Softening of the cervix (feels like lips rather than the tip of the nose)',
        'Early pregnancy (~4–6 weeks) from increased vascularity and edema; also with OCP use',
        'Probable — not diagnostic — sign of pregnancy.',
    ),
    'hegar sign': _sg(
        'Softening of the lower uterine segment (isthmus) on bimanual exam, so the cervix and fundus feel almost separate',
        'Early pregnancy (~6–12 weeks)',
        'Probable sign of pregnancy; Ladin sign is a related softening at the anterior midline.',
    ),
    'chandelier sign': _sg(
        "Severe pain with cervical motion on bimanual exam — the patient 'reaches for the chandelier'",
        'CERVICAL MOTION TENDERNESS — pelvic inflammatory disease (a minimum criterion); also ectopic pregnancy, appendicitis, ovarian torsion',
        'Sexually active woman with pelvic pain and cervical motion tenderness → check hCG, then treat empirically for PID if no other cause.',
    ),
    'strawberry cervix': _sg(
        'Punctate hemorrhages and red papules on the cervix (colpitis macularis)',
        'TRICHOMONAS VAGINALIS infection (seen in a minority, but highly specific)',
        'Strawberry TONGUE, by contrast, suggests scarlet fever or Kawasaki disease.',
    ),
    'clue cells': _sg(
        "Vaginal squamous epithelial cells with borders obscured ('stippled') by adherent coccobacilli on saline wet mount",
        'BACTERIAL VAGINOSIS (Gardnerella vaginalis) — one of the Amsel criteria (>20% of epithelial cells)',
        'Amsel 3 of 4: thin gray discharge, pH >4.5, positive whiff test, clue cells.',
    ),
    'whiff test': _sg(
        'Fishy (amine) odor released when 10% KOH is added to vaginal discharge',
        'BACTERIAL VAGINOSIS (also trichomoniasis)',
        'Positive whiff test is one of the four Amsel criteria.',
    ),
    'turtle sign': _sg(
        'The fetal head delivers and then retracts back against the perineum',
        'SHOULDER DYSTOCIA (anterior shoulder impacted behind the pubic symphysis)',
        'Call for help → McRoberts maneuver + suprapubic pressure; never fundal pressure.',
    ),
    'lochia': _sg(
        'Normal postpartum uterine discharge: rubra (red, days 1–4), serosa (pink-brown, days 4–10), alba (yellow-white, up to 6 weeks)',
        'Normal involution of the placental site',
        'FOUL-smelling lochia + fever + uterine tenderness → endometritis; persistent heavy red lochia beyond 2 weeks → retained products or subinvolution.',
    ),
}

_SIGN_ALIASES = {
    "mcburney point": "mcburney sign", "mcburney's point": "mcburney sign",
    "grey-turner sign": "grey turner sign", "gray turner sign": "grey turner sign",
    "troisier sign": "virchow node", "virchow's node": "virchow node",
    "sister mary joseph's nodule": "sister mary joseph nodule",
    "leser-trélat sign": "leser-trelat sign",
    "water hammer pulse": "corrigan pulse", "water-hammer pulse": "corrigan pulse",
    "corrigan's pulse": "corrigan pulse", "quincke's pulse": "quincke pulse",
    "musset sign": "de musset sign", "de musset's sign": "de musset sign",
    "gower sign": "gowers sign", "gower's sign": "gowers sign", "gowers' sign": "gowers sign",
    "rapd": "marcus gunn pupil", "relative afferent pupillary defect": "marcus gunn pupil",
    "marcus-gunn pupil": "marcus gunn pupil",
    "kussmaul breathing": "kussmaul respirations", "kussmaul respiration": "kussmaul respirations",
    "kf rings": "kayser-fleischer rings", "kayser fleischer rings": "kayser-fleischer rings",
    "virchow's triad": "virchow triad",
    "phalen sign": "phalen test", "phalen's test": "phalen test", "phalen's sign": "phalen test",
    "lachman's test": "lachman test", "mcmurray's test": "mcmurray test",
    "anterior drawer test": "anterior drawer sign",
    "uhthoff's phenomenon": "uhthoff phenomenon", "koebner's phenomenon": "koebner phenomenon",
    "köbner phenomenon": "koebner phenomenon",
    "battle's sign": "battle sign", "raccoon sign": "raccoon eyes",
    "allen's test": "allen test",
    "chadwick's sign": 'chadwick sign',
    "goodell's sign": 'goodell sign',
    "hegar's sign": 'hegar sign',
    'cervical motion tenderness': 'chandelier sign',
    'cmt': 'chandelier sign',
    'colpitis macularis': 'strawberry cervix',
    'clue cell': 'clue cells',
    'amine test': 'whiff test',
    'turtling': 'turtle sign',
    'lochia rubra': 'lochia',
    'lochia serosa': 'lochia',
    'lochia alba': 'lochia',
}
