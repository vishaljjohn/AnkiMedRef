"""Drug classes and their alternate names (tier 0.5a).

Edit freely — see data/__init__.py for how files are loaded."""
from ..formatters import _dc


_DRUG_CLASSES = {
    "beta blocker": _dc(
        "Competitively block β-adrenergic receptors → ↓HR, ↓contractility, ↓renin",
        ["Metoprolol","Atenolol","Carvedilol","Labetalol","Propranolol","Bisoprolol","Esmolol","Nadolol"],
        "HTN, angina, HFrEF, post-MI, rate control (AF/flutter), migraine prophylaxis, thyroid storm",
        "CI: decompensated HF, bradycardia, heart block, severe asthma. ADR: fatigue, cold extremities, impotence, mask hypoglycemia",
        "Carvedilol/labetalol also block α1 (vasodilation). Propranolol is non-selective (β1+β2). Esmolol ultra-short-acting IV."
    ),
    "ace inhibitor": _dc(
        "Block ACE → ↓Ang II → vasodilation, ↓aldosterone, ↓GFR (efferent dilation), ↑bradykinin",
        ["Lisinopril","Ramipril","Enalapril","Captopril","Benazepril","Fosinopril","Quinapril"],
        "HTN, HFrEF, post-MI, diabetic nephropathy, CKD proteinuria reduction",
        "CI: pregnancy (fetotoxic), bilateral renal artery stenosis, hyperkalemia, angioedema history. ADR: dry cough (bradykinin↑), angioedema, hyperkalemia, acute kidney injury",
        "ACEi cause cough → switch to ARB. Both block RAAS but ACEi ↑bradykinin (cough/angioedema)."
    ),
    "arb": _dc(
        "Block AT1 receptor → ↓vasoconstriction, ↓aldosterone. No effect on bradykinin → no cough",
        ["Losartan","Valsartan","Irbesartan","Candesartan","Olmesartan","Telmisartan"],
        "HTN, HFrEF (ARNi preferred), diabetic nephropathy, ACEi-induced cough (substitute)",
        "CI: pregnancy, bilateral RAS, hyperkalemia. ADR: hyperkalemia, AKI (similar to ACEi but no cough)",
        "Losartan also lowers uric acid (useful in gout + HTN)."
    ),
    "calcium channel blocker": _dc(
        "Block L-type Ca²⁺ channels. DHP (amlodipine): vascular > cardiac. Non-DHP (verapamil, diltiazem): cardiac = vascular",
        ["Amlodipine","Nifedipine","Felodipine","Verapamil","Diltiazem"],
        "HTN, angina (vasospastic & stable), rate control in AF (non-DHP), Raynaud phenomenon",
        "CI: non-DHP + HFrEF, heart block, bradycardia (verapamil/diltiazem). ADR: peripheral edema, flushing, constipation (verapamil), reflex tachycardia (DHP)",
        "DHP = dihydropyridines (amlodipine, nifedipine) — mostly vascular. Verapamil most cardio-selective."
    ),
    "statin": _dc(
        "Inhibit HMG-CoA reductase (rate-limiting step in cholesterol synthesis) → ↑LDL receptors → ↓LDL",
        ["Atorvastatin","Rosuvastatin","Simvastatin","Pravastatin","Lovastatin","Fluvastatin","Pitavastatin"],
        "Primary/secondary ASCVD prevention, hypercholesterolemia, ↓LDL (also ↓TG, ↑HDL mildly)",
        "CI: decompensated liver disease; stop in pregnancy (FDA removed the absolute contraindication in 2021). ADR: myopathy/rhabdomyolysis (↑with fibrates/niacin), hepatotoxicity (↑LFTs), new-onset DM2",
        "High-intensity: atorvastatin 40-80mg, rosuvastatin 20-40mg. Myopathy risk ↑with CYP3A4 inhibitors (grapefruit, azole antifungals)."
    ),
    "thiazide diuretic": _dc(
        "Block Na-Cl cotransporter (NCC) in DCT → ↓Na reabsorption → ↑Ca reabsorption (unlike loop diuretics)",
        ["Hydrochlorothiazide","Chlorthalidone","Metolazone","Indapamide"],
        "HTN (first-line), edema, hypercalciuria/nephrolithiasis, nephrogenic DI (paradox)",
        "CI: sulfa allergy (relative), gout, hypokalemia. ADR: hypokalemia, hyponatremia, hyperuricemia, hyperglycemia, hypercalcemia, hyperlipidemia",
        "HCTZ ↑Ca reabsorption — use in hypercalciuria. Chlorthalidone preferred for CV outcomes."
    ),
    "loop diuretic": _dc(
        "Block Na-K-2Cl cotransporter (NKCC2) in thick ascending loop of Henle → ↓Ca, Mg reabsorption",
        ["Furosemide","Bumetanide","Torsemide","Ethacrynic acid"],
        "Acute pulmonary edema, CHF edema, hypertensive emergency with volume overload, hypercalcemia (after saline), hyperkalemia",
        "CI: sulfa allergy (except ethacrynic acid). ADR: ototoxicity, hypokalemia, hypomagnesemia, metabolic alkalosis, hypocalcemia, hyperuricemia",
        "Ethacrynic acid: only loop diuretic safe in sulfa allergy. Torsemide has better oral bioavailability."
    ),
    "potassium-sparing diuretic": _dc(
        "Block aldosterone (spironolactone, eplerenone) or block ENaC (amiloride, triamterene) → ↓K excretion",
        ["Spironolactone","Eplerenone","Amiloride","Triamterene"],
        "HFrEF (spironolactone/eplerenone), hyperaldosteronism, hypokalemia, ascites, hirsutism",
        "CI: hyperkalemia, AKI, CKD stage 4-5. ADR: hyperkalemia, gynecomastia/anti-androgen effects (spironolactone)",
        "Spironolactone/eplerenone = MRA (mineralocorticoid receptor antagonist). Eplerenone more selective → less gynecomastia."
    ),
    "nitrate": _dc(
        "Release NO → activate guanylyl cyclase → ↑cGMP → smooth muscle relaxation → venodilation (predominantly) → ↓preload",
        ["Nitroglycerin","Isosorbide mononitrate","Isosorbide dinitrate","Nitroprusside"],
        "Angina (stable, vasospastic), acute MI, acute decompensated HF (↓preload), hypertensive emergency (nitroprusside)",
        "CI: PDE5 inhibitors (sildenafil etc.) — severe hypotension. CI: right ventricular infarction (preload-dependent). ADR: headache, reflex tachycardia, hypotension, tolerance (nitrate-free interval needed)",
        "Nitroprusside = NO donor, arterial + venous dilation → hypertensive emergency. Risk of cyanide toxicity."
    ),
    "anticoagulant": _dc(
        "Prevent clot formation: Heparin/LMWH (↑AT-III), Warfarin (↓II,VII,IX,X,C,S), DOACs (direct Xa or IIa inhibition)",
        ["Heparin","Enoxaparin","Warfarin","Rivaroxaban","Apixaban","Dabigatran","Fondaparinux"],
        "DVT/PE treatment & prophylaxis, AF (stroke prevention), mechanical heart valves (warfarin), ACS",
        "ADR: bleeding (major risk), heparin-induced thrombocytopenia (HIT) with UFH/LMWH, teratogenicity (warfarin). Monitor aPTT (UFH), INR (warfarin)",
        "HIT: ↓platelets + thrombosis → stop heparin, use argatroban/bivalirudin. Reversal: protamine (heparin), Vitamin K + 4-factor PCC (warfarin; FFP if PCC unavailable), andexanet alfa (Xa inhibitors)."
    ),
    "doac": _dc(
        "Direct oral anticoagulants: Factor Xa inhibitors (-xabans) or direct thrombin inhibitor (dabigatran)",
        ["Rivaroxaban","Apixaban","Edoxaban","Betrixaban","Dabigatran"],
        "AF stroke prevention, DVT/PE treatment & prophylaxis",
        "CI: severe renal/hepatic impairment, mechanical heart valves, triple-positive antiphospholipid syndrome. ADR: bleeding. Less monitoring needed than warfarin",
        "Apixaban ↓bleeding vs warfarin in AF (ARISTOTLE). Dabigatran reversal: idarucizumab. Xa inhibitor reversal: andexanet alfa."
    ),
    "antiplatelet": _dc(
        "Inhibit platelet aggregation: aspirin (COX-1), clopidogrel/ticagrelor (P2Y12 ADP receptor), GPIIb/IIIa inhibitors",
        ["Aspirin","Clopidogrel","Ticagrelor","Prasugrel","Abciximab","Eptifibatide","Dipyridamole"],
        "ACS (DAPT), secondary stroke prevention, PCI, PAD, AF (aspirin alone weak)",
        "ADR: bleeding, GI upset (aspirin). Clopidogrel requires CYP2C19 activation (poor metabolizers — check genetics). Ticagrelor: dyspnea",
        "DAPT (aspirin + P2Y12 inhibitor) × 12 months post-ACS. Ticagrelor preferred over clopidogrel post-ACS (PLATO trial)."
    ),
    "fibrinolytic": _dc(
        "Activate plasminogen → plasmin → dissolve fibrin clots (tPA/alteplase most common)",
        ["Alteplase (tPA)","Tenecteplase","Reteplase","Streptokinase"],
        "STEMI (if PCI unavailable within 120 min), massive PE with hemodynamic compromise, ischemic stroke (within 4.5h, no hemorrhage)",
        "CI: recent surgery/trauma, intracranial hemorrhage, hemorrhagic stroke, uncontrolled HTN, internal bleeding. ADR: bleeding, angioedema (ACEi + alteplase)",
        "Streptokinase is antigenic (prior exposure → resistance + allergic reaction). tPA preferred."
    ),
    "class ia antiarrhythmic": _dc(
        "Block fast Na⁺ channels (intermediate kinetics) + block K⁺ channels → ↑AP duration, ↑QRS, ↑QT",
        ["Quinidine","Procainamide","Disopyramide"],
        "AF, ventricular arrhythmias, WPW",
        "ADR: quinidine — cinchonism (tinnitus, headache), torsades de pointes. Procainamide — drug-induced lupus (anti-histone Ab). Disopyramide — anticholinergic"
    ),
    "class ic antiarrhythmic": _dc(
        "Block fast Na⁺ channels (slow kinetics) — greatest depression of conduction; minimal effect on repolarization",
        ["Flecainide","Propafenone"],
        "AF/flutter in structurally normal hearts, SVT, WPW",
        "CI: structural heart disease, post-MI (CAST trial — ↑mortality). ADR: proarrhythmia, CNS effects",
        "CAST trial: flecainide/encainide ↑mortality in post-MI patients despite suppressing PVCs. Avoid in structural heart disease."
    ),
    "class iii antiarrhythmic": _dc(
        "Block K⁺ channels → ↑AP duration, ↑effective refractory period → ↑QT",
        ["Amiodarone","Sotalol","Dofetilide","Ibutilide","Dronedarone"],
        "AF/flutter (cardioversion & maintenance), ventricular tachycardia, refractory SVT",
        "ADR: amiodarone — pulmonary toxicity, thyroid dysfunction (hypo- and hyper-), hepatotoxicity, photosensitivity, corneal deposits, blue-gray skin. Sotalol/ibutilide/dofetilide — torsades de pointes",
        "Amiodarone: class I+II+III+IV combined. Half-life 40-55 days. Monitor TFTs, LFTs, PFTs, eye exam annually."
    ),
    "sulfonylurea": _dc(
        "Close ATP-sensitive K⁺ channels on β-cells → depolarization → ↑insulin release (glucose-independent)",
        ["Glipizide","Glyburide","Glimepiride","Chlorpropamide","Tolbutamide"],
        "T2DM (1st-gen less used, 2nd-gen preferred)",
        "CI: renal impairment (avoid glyburide). ADR: hypoglycemia (most common), weight gain, SIADH (chlorpropamide)",
        "Stimulate insulin secretion regardless of glucose → hypoglycemia risk. 2nd gen: glipizide, glyburide, glimepiride."
    ),
    "sglt2 inhibitor": _dc(
        "Block SGLT2 in proximal tubule → ↑urinary glucose/Na excretion → ↓blood glucose, ↓weight, ↓BP, ↓preload",
        ["Empagliflozin","Dapagliflozin","Canagliflozin","Ertugliflozin"],
        "T2DM (CV benefit in established CVD), HFrEF, CKD (dapagliflozin, canagliflozin)",
        "CI: eGFR <20-45 (varies by drug). ADR: UTI/genital mycotic infections, DKA (euglycemic), Fournier gangrene, dehydration, volume depletion",
        "EMPA-REG: empagliflozin ↓CV death in T2DM+CVD. DAPA-HF: dapagliflozin ↓HF hospitalization in HFrEF regardless of DM."
    ),
    "glp-1 agonist": _dc(
        "Mimic GLP-1: ↑glucose-dependent insulin release, ↓glucagon, slow gastric emptying, ↑satiety → weight loss",
        ["Semaglutide","Liraglutide","Dulaglutide","Exenatide","Tirzepatide (GLP-1+GIP)"],
        "T2DM (CV benefit), obesity (semaglutide, liraglutide and tirzepatide approved for weight loss), NASH",
        "CI: personal/family history of MEN-2 or medullary thyroid cancer. ADR: nausea/vomiting/diarrhea (dose-limiting), pancreatitis, gallstones. NOT hypoglycemia (glucose-dependent)",
        "LEADER: liraglutide ↓MACE in T2DM. SUSTAIN-6: semaglutide ↓MACE. Weekly SC (semaglutide, dulaglutide) vs daily (liraglutide, exenatide)."
    ),
    "dpp-4 inhibitor": _dc(
        "Inhibit DPP-4 (degrades GLP-1 and GIP) → ↑incretin levels → ↑glucose-dependent insulin, ↓glucagon",
        ["Sitagliptin","Saxagliptin","Alogliptin","Linagliptin"],
        "T2DM (adjunct), weight-neutral, safe in renal impairment",
        "ADR: nasopharyngitis, pancreatitis (rare), joint pain. Saxagliptin/alogliptin — ↑HF hospitalizations",
        "Gliptins are weight-neutral. Less potent than GLP-1 agonists for A1c reduction. Linagliptin: no renal dose adjustment needed."
    ),
    "biguanide": _dc(
        "↓Hepatic gluconeogenesis (AMPK activation), ↑peripheral insulin sensitivity; does not stimulate insulin secretion",
        ["Metformin"],
        "T2DM first-line, PCOS (off-label), pre-diabetes prevention",
        "CI: eGFR <30, iodinated contrast (hold 48h), surgery, alcohol abuse. ADR: GI upset (N/D, metallic taste), lactic acidosis (rare), Vit B12 deficiency",
        "Metformin: weight-neutral or ↓weight. No hypoglycemia when used alone. Hold before iodinated contrast if eGFR <60."
    ),
    "thiazolidinedione": _dc(
        "Activate PPARγ → ↑insulin sensitivity in adipose/muscle/liver; ↑adiponectin, ↓free fatty acids",
        ["Pioglitazone","Rosiglitazone"],
        "T2DM (adjunct), NASH/NAFLD (pioglitazone)",
        "CI: NYHA class III-IV HF, bladder cancer (pioglitazone). ADR: weight gain, fluid retention/edema, HF exacerbation, ↑fracture risk, LFT monitoring (rosiglitazone)",
        "Pioglitazone ↓TG, ↑HDL. Rosiglitazone withdrawn in EU (CV concerns). TZDs require 6-12 weeks for full effect."
    ),
    "penicillin": _dc(
        "β-lactam — inhibit transpeptidase (PBP) → block peptidoglycan cross-linking → bactericidal",
        ["Amoxicillin","Ampicillin","Penicillin G/V","Nafcillin","Oxacillin","Piperacillin","Ticarcillin"],
        "Strep pharyngitis, syphilis (PCN G), Gram-positive infections, enterococcal endocarditis (ampicillin), Pseudomonas (pip-tazo)",
        "CI: penicillin allergy (cross-reactivity ~1-2% with cephalosporins). ADR: hypersensitivity (anaphylaxis, rash), diarrhea, interstitial nephritis (nafcillin)",
        "Nafcillin/oxacillin: penicillinase-resistant → MSSA. Add β-lactamase inhibitor (clavulanate, sulbactam, tazobactam) to extend coverage."
    ),
    "cephalosporin": _dc(
        "β-lactam — inhibit PBP → block peptidoglycan cross-linking; each generation has expanded Gram-negative coverage",
        ["Cephalexin (1st)","Cefazolin (1st)","Cefuroxime (2nd)","Cefoxitin (2nd)","Ceftriaxone (3rd)","Cefepime (4th)","Ceftaroline (5th)"],
        "1st: skin/bone/UTI (MSSA). 2nd: anaerobes (cefoxitin). 3rd: meningitis/gonorrhea/CAP (ceftriaxone). 4th: Pseudomonas (cefepime). 5th: MRSA (ceftaroline)",
        "CI: severe penicillin allergy (1-2% cross-reactivity; avoid with anaphylaxis). ADR: rash, diarrhea, C. diff, disulfiram-like (cefotetan), hypoprothrombinemia",
        "3rd-gen cephalosporins: best CSF penetration → meningitis. Ceftaroline and ceftobiprole (5th-gen): the only β-lactams active vs MRSA."
    ),
    "fluoroquinolone": _dc(
        "Inhibit DNA gyrase (topoisomerase II) in Gram-negatives and topoisomerase IV in Gram-positives → prevent DNA supercoiling → bactericidal",
        ["Ciprofloxacin","Levofloxacin","Moxifloxacin","Norfloxacin","Gemifloxacin"],
        "UTI, respiratory (CAP — levo/moxi), GI/typhoidal infections (cipro), STIs, anthrax prophylaxis",
        "CI: children/pregnancy (cartilage damage), myasthenia gravis. ADR: tendon rupture (Achilles — esp. with steroids), QT prolongation, peripheral neuropathy, C. diff, photosensitivity",
        "Black box: tendinitis/tendon rupture, peripheral neuropathy. Cipro: best for Pseudomonas among oral FQs. Moxi: anaerobe coverage, no UTI."
    ),
    "macrolide": _dc(
        "Bind 23S rRNA of 50S ribosomal subunit → inhibit translocation → bacteriostatic",
        ["Azithromycin","Clarithromycin","Erythromycin"],
        "CAP (atypicals: Mycoplasma, Chlamydia, Legionella), H. pylori (clarithromycin), MAC prophylaxis (azithromycin), pertussis, STIs",
        "ADR: GI (N/V — esp. erythromycin — prokinetic effect via motilin), QT prolongation, hepatotoxicity, CYP3A4 inhibition (clarithromycin >> erythromycin > azithromycin)",
        "Azithromycin: longest half-life (5-day Z-pack). Erythromycin: CYP3A4 inhibitor, strongest prokinetic → used off-label for gastroparesis."
    ),
    "aminoglycoside": _dc(
        "Bind 30S ribosomal subunit (16S rRNA) → misreading of mRNA → bactericidal; require O₂ for uptake → inactive in anaerobes",
        ["Gentamicin","Tobramycin","Amikacin","Streptomycin","Neomycin"],
        "Severe Gram-negative infections (Pseudomonas, E.coli, Klebsiella), synergy with β-lactams for endocarditis (streptomycin for TB)",
        "ADR: nephrotoxicity (proximal tubule), ototoxicity (vestibular > cochlear; irreversible), neuromuscular blockade. Monitor troughs",
        "Once-daily dosing (extended-interval) preferred — equal efficacy, less nephrotoxicity. Neomycin: oral only for hepatic encephalopathy."
    ),
    "tetracycline": _dc(
        "Bind 30S ribosomal subunit → block tRNA/aminoacyl binding → bacteriostatic; chelates Ca²⁺/Mg²⁺",
        ["Doxycycline","Minocycline","Tetracycline","Tigecycline"],
        "Atypicals (Mycoplasma, Chlamydia, Rickettsia, Borrelia), acne, rosacea, MRSA (doxycycline), malaria prophylaxis, H. pylori",
        "CI: pregnancy, children <8 (teeth discoloration, bone growth inhibition). ADR: GI, photosensitivity, esophageal irritation. Chelates with Ca/Mg/Fe → don't take with dairy/antacids",
        "Tigecycline: broadest spectrum tetracycline (including MRSA, VRE, MDR Gram-negatives) but ↑mortality in severe infections."
    ),
    "carbapenem": _dc(
        "β-lactam with broadest spectrum — inhibit PBP; cover ESBL-producing organisms, most anaerobes; NOT MRSA, VRE",
        ["Meropenem","Imipenem-cilastatin","Ertapenem","Doripenem"],
        "MDR Gram-negatives, polymicrobial/nosocomial infections, ESBL organisms, intra-abdominal",
        "ADR: seizures (imipenem > meropenem; avoid imipenem in CNS infections), C. diff, allergic reactions (~1% PCN cross-reactivity)",
        "Imipenem + cilastatin: cilastatin inhibits renal dehydropeptidase-I (prevents inactivation + ↓nephrotoxicity). Ertapenem: no Pseudomonas/Acinetobacter coverage."
    ),
    "glycopeptide": _dc(
        "Bind D-Ala-D-Ala terminus of peptidoglycan precursors → block cell wall synthesis; NOT a β-lactam",
        ["Vancomycin","Teicoplanin","Dalbavancin","Oritavancin"],
        "MRSA, C. diff (oral vancomycin), severe Gram-positive infections",
        "ADR: Vancomycin infusion reaction (formerly 'red man'; histamine release — slow infusion or pre-treat with diphenhydramine), nephrotoxicity, ototoxicity, thrombophlebitis",
        "Vancomycin now dosed by AUC/MIC (not trough alone). VRE = D-Ala-D-Lac → vancomycin resistance. Oral vanco NOT absorbed → use for C. diff colitis only."
    ),
    "lincosamide": _dc(
        "Bind 23S rRNA of 50S ribosomal subunit → inhibit peptide bond formation; same site as macrolides/chloramphenicol",
        ["Clindamycin"],
        "Anaerobic infections (aspiration pneumonia), skin/soft tissue (MRSA — skin only), Toxoplasma + Pneumocystis (salvage), dental prophylaxis",
        "ADR: C. difficile colitis (highest risk of any antibiotic), diarrhea, pseudomembranous colitis, maculopapular rash",
        "Clindamycin: excellent anaerobe coverage above the diaphragm. Does NOT cover Bacteroides fragilis reliably → use metronidazole for below-diaphragm."
    ),
    "azole antifungal": _dc(
        "Inhibit lanosterol 14α-demethylase (CYP51) → ↓ergosterol synthesis → fungistatic",
        ["Fluconazole","Itraconazole","Voriconazole","Posaconazole","Isavuconazole","Ketoconazole"],
        "Candida (fluconazole 1st-line for non-neutropenic), Aspergillus (voriconazole 1st-line), Coccidioides, Histoplasma, Blastomyces (itraconazole)",
        "ADR: hepatotoxicity, QT prolongation, CYP3A4 inhibition (↑warfarin, cyclosporine, statins), teratogenic",
        "Fluconazole: does NOT cover Aspergillus. Voriconazole: visual disturbances (photopsia — hallmark ADR). Posaconazole: prophylaxis in HSCT/AML."
    ),
    "echinocandin": _dc(
        "Inhibit β-1,3-glucan synthase → ↓cell wall glucan synthesis → fungicidal for Candida, fungistatic for Aspergillus",
        ["Caspofungin","Micafungin","Anidulafungin"],
        "Invasive candidiasis (1st-line for moderate-severe/neutropenic), Aspergillus (salvage), esophageal candidiasis",
        "CI: not for Cryptococcus or Mucor. ADR: hepatotoxicity, histamine-like flushing (caspofungin infusion)",
        "Fewest drug interactions among antifungals. Safe in renal failure. Caspofungin requires loading dose."
    ),
    "nucleoside analog": _dc(
        "Inhibit viral reverse transcriptase or DNA polymerase after intracellular phosphorylation to active triphosphate form",
        ["Acyclovir","Ganciclovir","Valganciclovir","Zidovudine (AZT)","Tenofovir","Emtricitabine","Lamivudine"],
        "HSV/VZV (acyclovir), CMV (ganciclovir/valganciclovir), HIV (NRTIs — tenofovir, emtricitabine), HBV (tenofovir, lamivudine)",
        "ADR: acyclovir — nephrotoxicity (crystalluria — hydrate), neurotoxicity. Ganciclovir — myelosuppression (neutropenia). AZT — bone marrow suppression, myopathy",
        "Acyclovir requires viral thymidine kinase for activation → specific for HSV/VZV infected cells. Ganciclovir: 50× more active vs CMV."
    ),
    "corticosteroid": _dc(
        "Bind intracellular glucocorticoid receptor → translocate to nucleus → alter gene transcription → anti-inflammatory + immunosuppressive",
        ["Prednisone","Prednisolone","Methylprednisolone","Dexamethasone","Hydrocortisone","Budesonide","Fludrocortisone"],
        "Inflammatory/autoimmune diseases, adrenal insufficiency (hydrocortisone), severe asthma/COPD exacerbation, cerebral edema (dexamethasone), septic shock + relative AI, croup",
        "ADR: HPA suppression, hyperglycemia, osteoporosis, avascular necrosis (femoral head), Cushingoid features, ↑infection, cataracts, glaucoma, mood changes, growth retardation",
        "Dexamethasone: highest anti-inflammatory potency, minimal mineralocorticoid effect → best for cerebral edema. Fludrocortisone: highest mineralocorticoid activity."
    ),
    "opioid": _dc(
        "Bind μ (mu) > κ (kappa) > δ (delta) opioid receptors (Gi-coupled) → ↓cAMP, ↑K⁺ conductance, ↓Ca²⁺ → ↓neuronal excitability",
        ["Morphine","Oxycodone","Hydromorphone","Fentanyl","Methadone","Codeine","Tramadol","Buprenorphine"],
        "Moderate-severe pain, opioid use disorder (methadone/buprenorphine MAT), cough suppression (codeine), diarrhea (loperamide)",
        "ADR: respiratory depression (most dangerous), constipation (no tolerance), miosis, urinary retention, pruritus, N/V, euphoria. Tolerance to analgesia but NOT constipation",
        "Reversal: naloxone (competitive μ antagonist, short half-life → may need repeat dosing). Methadone: long t½ → risk of QT prolongation + delayed respiratory depression."
    ),
    "nsaid": _dc(
        "Inhibit COX-1 and COX-2 → ↓prostaglandin/thromboxane synthesis → ↓inflammation, ↓pain, ↓fever",
        ["Ibuprofen","Naproxen","Indomethacin","Ketorolac","Celecoxib (COX-2)","Aspirin","Meloxicam"],
        "Pain/inflammation/fever, dysmenorrhea, gout (indomethacin/naproxen), PDA closure (indomethacin — neonates), pericarditis",
        "CI: GI ulcer, CKD/AKI, NSAID-sensitive asthma, last trimester pregnancy, anticoagulant use. ADR: GI ulceration/bleeding, AKI, HTN, fluid retention, ↑CV events",
        "Celecoxib: selective COX-2 → ↓GI risk but ↑CV risk. Indomethacin: most potent, most toxic. Ketorolac: strong parenteral NSAID."
    ),
    "antiepileptic": _dc(
        "Various: Na⁺ channel blockade (phenytoin, carbamazepine), GABA potentiation (valproate, barbiturates), Ca²⁺ channel blockade (ethosuximide — T-type), glutamate inhibition (lamotrigine)",
        ["Phenytoin","Carbamazepine","Valproate","Lamotrigine","Levetiracetam","Ethosuximide","Phenobarbital","Topiramate","Gabapentin"],
        "Focal seizures (carbamazepine, phenytoin), generalized (valproate, levetiracetam), absence (ethosuximide ± valproate), status epilepticus (BZD → fosphenytoin, levetiracetam or valproate — ESETT → anesthetic infusion)",
        "Phenytoin: gingival hyperplasia, hirsutism, megaloblastic anemia, zero-order kinetics. Carbamazepine: SIADH, aplastic anemia, SJS. Valproate: hepatotoxicity, neural tube defects, weight gain. Lamotrigine: SJS (slow titration!)",
        "Valproate: broad-spectrum (all seizure types). Ethosuximide: absence only. Levetiracetam: fewest drug interactions."
    ),
    "ssri": _dc(
        "Selectively inhibit serotonin reuptake transporter (SERT) → ↑synaptic serotonin",
        ["Fluoxetine","Sertraline","Paroxetine","Citalopram","Escitalopram","Fluvoxamine"],
        "MDD, anxiety disorders (GAD, panic disorder, social anxiety, OCD, PTSD), bulimia (fluoxetine), PMDD",
        "ADR: sexual dysfunction, GI (N/D), insomnia/drowsiness, weight gain, serotonin syndrome (+ MAOIs, tramadol, triptans), QT prolongation (citalopram at high doses), ↑suicidality in <25yo (black box)",
        "Fluoxetine: longest half-life (active metabolite 1-2 weeks) → least discontinuation syndrome, most drug interactions (CYP2D6 inhibitor). Paroxetine: most anticholinergic."
    ),
    "snri": _dc(
        "Inhibit both serotonin (SERT) and norepinephrine (NET) reuptake → ↑synaptic 5-HT and NE",
        ["Venlafaxine","Duloxetine","Desvenlafaxine","Levomilnacipran"],
        "MDD, GAD, panic disorder, neuropathic pain (duloxetine), fibromyalgia (duloxetine), diabetic peripheral neuropathy, stress urinary incontinence (duloxetine)",
        "ADR: sexual dysfunction, N/V, ↑BP/HR (NE effect), sweating, insomnia, serotonin syndrome. Discontinuation syndrome (venlafaxine — short half-life)",
        "Duloxetine: best evidence for neuropathic pain/fibromyalgia. Venlafaxine: dose-dependent NE effect (↑BP at high doses)."
    ),
    "tricyclic antidepressant": _dc(
        "Inhibit NE + serotonin reuptake; also block α1, H1, muscarinic receptors → many side effects",
        ["Amitriptyline","Nortriptyline","Imipramine","Clomipramine","Desipramine","Doxepin"],
        "MDD (2nd-line), neuropathic pain (amitriptyline), migraine prophylaxis, bedwetting (imipramine), OCD (clomipramine), fibromyalgia",
        "CI: MAOI use, recent MI, arrhythmias. ADR: anticholinergic (dry mouth, urinary retention, constipation), sedation (H1), orthostatic hypotension (α1), QRS widening → arrhythmia. LETHAL in overdose",
        "TCA overdose: anticholinergic + QRS widening + hypotension. Treat QRS with IV sodium bicarbonate."
    ),
    "maoi": _dc(
        "Irreversibly inhibit MAO-A (NE, 5-HT, dopamine) and MAO-B (dopamine) → ↑monoamine levels",
        ["Phenelzine","Tranylcypromine","Isocarboxazid","Selegiline (selective MAO-B)"],
        "Refractory MDD, atypical depression, Parkinson disease (selegiline — MAO-B selective), social anxiety disorder",
        "CI: concurrent SSRIs/SNRIs/TCAs/meperidine/dextromethorphan (serotonin syndrome), tyramine-rich foods (hypertensive crisis — cheese, wine, cured meats). ADR: hypertensive crisis, serotonin syndrome, orthostatic hypotension",
        "Tyramine normally degraded by MAO in gut/liver. With MAOI → ↑tyramine → catecholamine release → hypertensive crisis. Washout: wait 2 weeks after stopping an MAOI before a serotonergic drug, and 5 weeks after stopping fluoxetine before starting an MAOI."
    ),
    "typical antipsychotic": _dc(
        "Block D2 dopamine receptors in mesolimbic pathway → ↓positive symptoms; also nigrostriatal (EPS) and tuberoinfundibular (↑prolactin) pathways",
        ["Haloperidol","Chlorpromazine","Fluphenazine","Perphenazine","Thioridazine","Loxapine"],
        "Schizophrenia (positive symptoms), Tourette syndrome (haloperidol), acute agitation (haloperidol IM), nausea (prochlorperazine)",
        "ADR: EPS (akathisia, dystonia, parkinsonism, tardive dyskinesia — tx with benztropine), NMS (fever, rigidity, ↑CK — tx with dantrolene), hyperprolactinemia, QT prolongation, anticholinergic",
        "High potency (haloperidol): more EPS, less sedation. Low potency (chlorpromazine): more sedation, anticholinergic, metabolic. Thioridazine: retinal pigmentation."
    ),
    "atypical antipsychotic": _dc(
        "Block D2 (weaker) + 5-HT2A receptors → ↓EPS compared to typicals; each has unique receptor profile",
        ["Clozapine","Risperidone","Olanzapine","Quetiapine","Aripiprazole","Ziprasidone","Lurasidone"],
        "Schizophrenia (positive + negative symptoms), bipolar disorder, MDD augmentation, Parkinson-related psychosis (pimavanserin, quetiapine, clozapine)",
        "ADR: metabolic syndrome (worst: olanzapine, clozapine), QT prolongation (ziprasidone), EPS (risperidone), clozapine — agranulocytosis (ANC monitoring), myocarditis, seizures",
        "Clozapine: most effective for treatment-resistant schizophrenia; ANC monitoring still required (FDA ended the REMS in 2025). Aripiprazole: partial D2 agonist → less metabolic syndrome. Quetiapine: most sedating."
    ),
    "calcineurin inhibitor": _dc(
        "Inhibit calcineurin → prevent dephosphorylation of NFAT → ↓IL-2 transcription → ↓T-cell activation",
        ["Cyclosporine","Tacrolimus"],
        "Solid organ transplant rejection prevention, graft-versus-host disease, autoimmune disorders (cyclosporine for psoriasis, RA)",
        "ADR: nephrotoxicity (dose-limiting), hypertension, neurotoxicity (tremor — tacrolimus > cyclosporine), hyperkalemia, hirsutism + gingival hyperplasia (cyclosporine), DM (tacrolimus)",
        "Tacrolimus: 100× more potent than cyclosporine, more DM/neurotoxicity. Cyclosporine: more hirsutism, gingival hyperplasia, dyslipidemia. Both: CYP3A4 metabolism."
    ),
    "biologic dmard": _dc(
        "Target specific inflammatory mediators: TNF-α (adalimumab, etanercept, infliximab), IL-6 (tocilizumab), IL-17 (secukinumab), B-cells (rituximab); JAK inhibitors (tofacitinib) are targeted synthetic small molecules, not biologics",
        ["Adalimumab","Etanercept","Infliximab","Tocilizumab","Rituximab","Abatacept","Secukinumab","Tofacitinib"],
        "Rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, IBD (infliximab, adalimumab), psoriasis, GCA (tocilizumab)",
        "ADR: ↑infection risk (TB reactivation — screen with TST/IGRA before anti-TNF), ↑lymphoma risk, injection site reactions, demyelination (anti-TNF CI in MS), lupus-like syndrome",
        "Screen for TB, HBV, HCV before initiating biologics. Anti-TNF CI in: active infection, moderate-severe HF (NYHA III-IV), demyelinating disease."
    ),
    # ── Alpha-1 blockers ──────────────────────────────────────────────────
    "alpha-1 blocker": _dc(
        "Block α1-adrenergic receptors on vascular smooth muscle → vasodilation → ↓peripheral resistance; also relax prostatic smooth muscle",
        ["Prazosin","Doxazosin","Terazosin","Tamsulosin","Alfuzosin","Silodosin"],
        "HTN (doxazosin/terazosin), benign prostatic hyperplasia (BPH — tamsulosin, alfuzosin), pheochromocytoma (phenoxybenzamine — irreversible, preop)",
        "ADR: orthostatic hypotension (first-dose syncope — take at bedtime), reflex tachycardia, nasal congestion, inhibition of ejaculation (tamsulosin)",
        "Tamsulosin/alfuzosin: uro-selective (less hypotension). Phenoxybenzamine: irreversible → used for pheochromocytoma prep before surgery."
    ),
    # ── Central α2 agonists ───────────────────────────────────────────────
    "central alpha-2 agonist": _dc(
        "Activate α2-adrenergic receptors in brainstem (locus coeruleus) → ↓sympathetic outflow → ↓HR, ↓BP",
        ["Clonidine","Methyldopa","Guanfacine","Tizanidine"],
        "HTN (clonidine — refractory; methyldopa — pregnancy safe), ADHD (guanfacine, clonidine), opioid/alcohol withdrawal (clonidine), spasticity (tizanidine)",
        "CI: abrupt discontinuation (rebound hypertensive crisis). ADR: sedation, dry mouth, bradycardia, depression (methyldopa — positive Coombs test in 10-20%, hemolytic anemia <1%)",
        "Methyldopa: long used in pregnancy (labetalol and nifedipine are now first-line). Clonidine patch: useful for adherence. Rebound crisis on abrupt stop → taper slowly."
    ),
    # ── Cardiac glycosides ────────────────────────────────────────────────
    "cardiac glycoside": _dc(
        "Inhibit Na/K-ATPase → ↑intracellular Na → ↑Ca via NCX → ↑contractility (positive inotrope). Also ↑vagal tone → ↓AV conduction → ↓HR",
        ["Digoxin","Digitoxin"],
        "HFrEF (↓hospitalizations, not mortality), rate control in AF (especially HF + AF)",
        "CI: Wolff-Parkinson-White (↑accessory pathway conduction), ventricular arrhythmias, heart block (2nd/3rd degree). ADR: narrow therapeutic index — N/V, yellow-green halos (xanthopsia), arrhythmias (PVCs, AV block, bigeminy), bradycardia. Toxicity ↑ with hypoK, hypoMg, hyperCa",
        "Dig toxicity: hypokalemia (from diuretics) is the most common precipitant. Treat with digoxin Fab antibody fragments (DigiFab). Target serum level 0.5–0.9 ng/mL in HF."
    ),
    # ── Proton Pump Inhibitors ────────────────────────────────────────────
    "proton pump inhibitor": _dc(
        "Irreversibly inhibit H⁺/K⁺-ATPase (proton pump) on parietal cell canalicular membrane → ↓gastric acid (prodrug activated by acid)",
        ["Omeprazole","Pantoprazole","Esomeprazole","Lansoprazole","Rabeprazole","Dexlansoprazole"],
        "GERD, peptic ulcer disease, H. pylori (triple/quadruple therapy), Zollinger-Ellison syndrome (↑↑↑dose), NSAID-induced ulcer prophylaxis, stress ulcer prophylaxis (ICU)",
        "ADR: hypomagnesemia (chronic use — blocks Mg absorption), C. diff ↑risk, pneumonia ↑risk, osteoporosis/fractures (↓Ca absorption — achlorhydria), Vit B12 deficiency (chronic), drug interactions (clopidogrel — omeprazole ↓activation via CYP2C19)",
        "PPIs are prodrugs: absorbed → activated by parietal cell acid → bind pump irreversibly. Take 30–60 min before meals. Pantoprazole: least CYP2C19 interaction → preferred with clopidogrel."
    ),
    # ── H2 Blockers ───────────────────────────────────────────────────────
    "h2 blocker": _dc(
        "Competitively block H2 receptors on parietal cells → ↓histamine-stimulated gastric acid secretion (less potent than PPIs)",
        ["Famotidine","Cimetidine","Ranitidine (withdrawn)","Nizatidine"],
        "GERD (mild-moderate), peptic ulcer disease, stress ulcer prophylaxis, Zollinger-Ellison (adjunct)",
        "ADR: cimetidine — CYP inhibitor (warfarin, theophylline, phenytoin interactions), anti-androgen effects (gynecomastia, impotence), CNS (confusion in elderly), crosses BBB/placenta",
        "Cimetidine: first H2 blocker but most side effects and drug interactions — rarely used now. Famotidine: preferred (no CYP inhibition). Ranitidine: withdrawn (NDMA contamination)."
    ),
    # ── Bisphosphonates ───────────────────────────────────────────────────
    "bisphosphonate": _dc(
        "Analogues of pyrophosphate → bind hydroxyapatite in bone → inhibit osteoclast activity (↓bone resorption) → net ↑bone density",
        ["Alendronate","Risedronate","Ibandronate","Zoledronic acid","Pamidronate","Etidronate"],
        "Osteoporosis (prevention/treatment), Paget disease of bone, hypercalcemia of malignancy (IV zoledronic acid), bone metastases, osteogenesis imperfecta",
        "CI: esophageal abnormalities (oral), GFR <30–35 (IV — nephrotoxic). ADR: esophageal irritation/ulceration (take with full glass water, stay upright 30–60 min), jaw osteonecrosis (ONJ — rare, esp. IV + dental procedure), atypical femur fractures (long-term use), acute phase reaction (flu-like sx with IV)",
        "N-containing bisphosphonates (alendronate, risedronate, zoledronic acid): more potent than non-N-containing. ONJ risk ↑ with: IV administration, cancer patients, dental extractions, smoking."
    ),
    # ── Benzodiazepines ───────────────────────────────────────────────────
    "benzodiazepine": _dc(
        "Bind GABA-A receptor at distinct benzodiazepine site → ↑frequency of Cl⁻ channel opening (compare: barbiturates ↑duration) → ↑inhibitory tone → CNS depression",
        ["Diazepam","Lorazepam","Midazolam","Alprazolam","Clonazepam","Temazepam","Triazolam","Chlordiazepoxide"],
        "Anxiety disorders (GAD, panic disorder), alcohol withdrawal (CIWA protocol), seizures/status epilepticus (lorazepam IV), procedural sedation (midazolam), insomnia (temazepam), muscle relaxation, akathisia",
        "CI: sleep apnea (↑respiratory depression), severe hepatic failure, pregnancy (cleft palate risk). ADR: sedation, respiratory depression, anterograde amnesia, dependence/tolerance, withdrawal seizures (life-threatening), paradoxical agitation (elderly)",
        "Reversal: flumazenil (competitive antagonist — short t½ → resedation can occur). Alcohol withdrawal: use long-acting BZDs (diazepam, chlordiazepoxide). Midazolam: shortest acting, most amnestic → procedural sedation."
    ),
    # ── Barbiturates ──────────────────────────────────────────────────────
    "barbiturate": _dc(
        "Bind GABA-A receptor → ↑duration of Cl⁻ channel opening (vs BZDs which ↑frequency); also directly activate Cl⁻ channel at high doses",
        ["Phenobarbital","Pentobarbital","Thiopental","Secobarbital","Primidone"],
        "Seizures/status epilepticus (phenobarbital — 3rd-line), anesthesia induction (thiopental — historical), procedural sedation (pentobarbital), refractory status epilepticus (pentobarbital coma)",
        "CI: porphyria (↑ALA synthase → ↑heme precursors — precipitates attack). ADR: respiratory depression, CNS depression, dependence, severe withdrawal (life-threatening seizures), CYP enzyme induction (↓effectiveness of many drugs — warfarin, OCP, phenytoin)",
        "Barbiturate vs BZD: barbiturates can cause fatal respiratory depression alone (vs BZDs — safer in OD). Phenobarbital: longest t½, used in neonatal seizures and alcohol withdrawal."
    ),
    # ── Lithium ───────────────────────────────────────────────────────────
    "lithium": _dc(
        "Mechanism unclear: inhibit inositol monophosphatase → ↓phosphatidylinositol signaling; ↓GSK-3β activity; modulate Na/K-ATPase",
        ["Lithium carbonate","Lithium citrate"],
        "Bipolar disorder (1st-line for mania prevention and treatment), augmentation in MDD, cluster headache prevention, ↓suicide risk in mood disorders",
        "CI: renal failure, severe dehydration, pregnancy (Ebstein anomaly — low absolute risk). ADR: narrow therapeutic index (0.6–1.2 mEq/L), nephrogenic DI (polyuria/polydipsia), hypothyroidism, tremor (fine hand tremor), weight gain, acne, leukocytosis. Toxicity: coarse tremor, ataxia, confusion, seizures, cardiovascular collapse",
        "Toxicity precipitated by: dehydration, NSAIDs (↓renal clearance), thiazides, low-Na diet, ACEi/ARBs. Monitor: TFTs, renal function, serum Li level. Teratogen (Ebstein anomaly — tricuspid dysplasia)."
    ),
    # ── Antiretrovirals ───────────────────────────────────────────────────
    "nrti": _dc(
        "Nucleoside/Nucleotide Reverse Transcriptase Inhibitors: Incorporate into viral DNA as chain terminators → block HIV reverse transcriptase; require intracellular phosphorylation",
        ["Tenofovir (TDF/TAF)","Emtricitabine (FTC)","Abacavir (ABC)","Lamivudine (3TC)","Zidovudine (AZT)","Stavudine (d4T)"],
        "HIV treatment (backbone of all ART regimens), HBV (tenofovir, lamivudine), HIV PrEP (tenofovir + emtricitabine)",
        "ADR: class — lactic acidosis/hepatic steatosis (mitochondrial toxicity). Specific: AZT — bone marrow suppression, myopathy; Abacavir — HLA-B*5701 hypersensitivity (fatal if re-challenged — SCREEN FIRST); Tenofovir (TDF) — nephrotoxicity, osteoporosis; TAF — safer for kidneys/bone",
        "Backbone of all HIV regimens. Screen HLA-B*5701 before abacavir. Tenofovir/emtricitabine (Truvada): HIV PrEP. Tenofovir, lamivudine and emtricitabine also suppress HBV → in HIV/HBV co-infection use tenofovir + 3TC/FTC; stopping them can cause an HBV flare."
    ),
    "nnrti": _dc(
        "Non-Nucleoside Reverse Transcriptase Inhibitors: Directly bind reverse transcriptase at allosteric site → conformational change → ↓polymerase activity; no phosphorylation needed",
        ["Efavirenz","Rilpivirine","Doravirine","Etravirine","Nevirapine"],
        "HIV treatment (typically combined with 2 NRTIs)",
        "ADR: rash (Stevens-Johnson syndrome — esp. nevirapine), hepatotoxicity (nevirapine — avoid if CD4 >250♀ or >400♂). Efavirenz: CNS effects (vivid dreams, dizziness — take at bedtime), early concern for neural tube defects (human data reassuring — DHHS now allows use in pregnancy)",
        "Single mutation (K103N) → resistance to efavirenz and nevirapine; 2nd-gen agents (etravirine, rilpivirine, doravirine) usually stay active. Efavirenz: strong CYP3A4 inducer. Nevirapine: CYP inducer + hepatotoxic → avoid in women with CD4 >250 (↑liver toxicity)."
    ),
    "protease inhibitor": _dc(
        "HIV protease inhibitors: Block HIV aspartyl protease → prevent cleavage of gag-pol polyprotein → immature, non-infectious virions produced",
        ["Ritonavir","Lopinavir/r","Darunavir/r","Atazanavir","Cobicistat (booster)"],
        "HIV treatment (usually boosted with ritonavir or cobicistat — CYP3A4 inhibitors → ↑PI levels); HIV salvage therapy",
        "ADR: metabolic syndrome (lipodystrophy, hyperlipidemia, hyperglycemia/insulin resistance), GI (N/D/nausea), nephrolithiasis/hyperbilirubinemia (atazanavir — indirect bili↑, benign). Massive CYP3A4 inhibition → many drug interactions",
        "Ritonavir sub-therapeutic dose used as pharmacokinetic booster (CYP3A4 inhibitor). Cobicistat: similar boosting without antiviral activity. Atazanavir: once daily, benign jaundice (indirect bili — not hepatotoxic)."
    ),
    "integrase inhibitor": _dc(
        "Inhibit HIV integrase → prevent viral DNA integration into host genome; most effective class at viral load suppression",
        ["Raltegravir","Elvitegravir","Dolutegravir","Bictegravir","Cabotegravir"],
        "HIV treatment (now preferred first-line backbone with 2 NRTIs or as long-acting injectable with rilpivirine), HIV PrEP (cabotegravir LAI)",
        "ADR: well-tolerated class. Dolutegravir/bictegravir: weight gain, early neural-tube-defect signal (dolutegravir) not confirmed by later data — now preferred in pregnancy. Drug interactions via UGT1A1 and CYP (fewer than PIs)",
        "Tenofovir + lamivudine + dolutegravir (TLD): preferred first-line WHO regimen. High barrier to resistance (dolutegravir, bictegravir). Cabotegravir LAI monthly/bimonthly injection for adherence."
    ),
    # ── Insulins ──────────────────────────────────────────────────────────
    "insulin": _dc(
        "Bind insulin receptor (tyrosine kinase) → ↑GLUT4 translocation → ↑glucose uptake in muscle/adipose; ↑glycogen synthesis; ↑protein synthesis; ↓gluconeogenesis; ↓lipolysis; ↓ketogenesis",
        ["Lispro/Aspart/Glulisine (rapid)","Regular (short)","NPH (intermediate)","Glargine/Detemir (long)","Degludec (ultra-long)"],
        "T1DM (required), T2DM (when oral agents fail), diabetic ketoacidosis, HHS, hyperkalemia (drives K⁺ into cells), gestational diabetes",
        "ADR: hypoglycemia (most dangerous), weight gain, lipohypertrophy at injection sites (rotate sites), hypokalemia (K⁺ shift). Somogyi effect (nocturnal hypoglycemia → rebound morning hyperglycemia) is largely disproven by CGM — dawn phenomenon is far more common",
        "Rapid-acting (lispro/aspart): onset 15 min, peak 1h → inject with meals. Glargine: no peak (peakless) → less nocturnal hypoglycemia. Only regular insulin given IV. Dawn phenomenon: early AM hyperglycemia from GH/cortisol."
    ),
    # ── Anticholinesterases ───────────────────────────────────────────────
    "anticholinesterase": _dc(
        "Inhibit acetylcholinesterase (AChE) → ↑acetylcholine at cholinergic synapses (nicotinic + muscarinic); reversible (physostigmine, neostigmine) or irreversible (organophosphates)",
        ["Donepezil","Rivastigmine","Galantamine","Neostigmine","Pyridostigmine","Physostigmine","Edrophonium"],
        "Alzheimer disease (donepezil, rivastigmine, galantamine — symptomatic only, do not alter disease course), myasthenia gravis (neostigmine, pyridostigmine), reversal of NMJ blockade (neostigmine), glaucoma (historical), anticholinergic toxicity (physostigmine — tertiary amine, crosses BBB; avoid in TCA overdose)",
        "ADR: cholinergic toxidrome — DUMBELS: Diarrhea/Defecation, Urination, Miosis, Bradycardia/Bronchospasm, Emesis, Lacrimation, Salivation. Also: N/V, muscle cramps, fasciculations",
        "Organophosphate poisoning (irreversible AChE inhibition): treat with atropine (block muscarinic effects) + pralidoxime 2-PAM (reactivate AChE if given early, before 'aging'). Edrophonium: very short-acting; the Tensilon test for MG is now largely abandoned (antibody testing, ice-pack test)."
    ),
    # ── Anticholinergics ──────────────────────────────────────────────────
    "anticholinergic": _dc(
        "Block muscarinic acetylcholine receptors → ↓parasympathetic tone → 'can't see, can't spit, can't pee, can't shit, can't sweat'",
        ["Atropine","Scopolamine","Benztropine","Ipratropium","Tiotropium","Oxybutynin","Solifenacin","Glycopyrrolate"],
        "Bradycardia (atropine IV), motion sickness (scopolamine patch), Parkinson disease/EPS (benztropine), COPD/asthma (ipratropium — anticholinergic bronchodilator), overactive bladder (oxybutynin, solifenacin), organophosphate poisoning",
        "CI: glaucoma (angle-closure — ↑IOP), BPH (urinary retention), elderly (Beers criteria — cognitive impairment). ADR: tachycardia, mydriasis, dry mouth, urinary retention, constipation, anhidrosis, confusion/delirium (especially in elderly)",
        "Anticholinergic toxidrome: 'Hot as a hare, blind as a bat, dry as a bone, red as a beet, mad as a hatter.' Physostigmine antidote (crosses BBB). Ipratropium/tiotropium: inhaled → few systemic effects."
    ),
    # ── Chemotherapy ─────────────────────────────────────────────────────
    "alkylating agent": _dc(
        "Add alkyl groups to DNA → form intrastrand/interstrand cross-links → block DNA replication → cell death (cell-cycle non-specific)",
        ["Cyclophosphamide","Ifosfamide","Melphalan","Busulfan","Carmustine","Lomustine","Temozolomide","Dacarbazine","Procarbazine"],
        "Lymphomas (cyclophosphamide), multiple myeloma (melphalan), ALL/AML, solid tumors, conditioning regimen for HSCT (busulfan), brain tumors (carmustine, temozolomide)",
        "ADR: hemorrhagic cystitis (cyclophosphamide/ifosfamide — metabolite acrolein; prevent with mesna and hydration), myelosuppression, secondary leukemia/AML (long-term), SIADH (cyclophosphamide), sterility (ovarian failure/azoospermia), pulmonary fibrosis (busulfan — 'busulfan lung')",
        "Mesna (2-mercaptoethanesulfonate) neutralizes acrolein in bladder → prevents hemorrhagic cystitis. Cyclophosphamide requires hepatic activation. Temozolomide + radiation = standard for glioblastoma (Stupp protocol)."
    ),
    "antimetabolite": _dc(
        "Structural analogues of nucleotides or folate → inhibit DNA/RNA synthesis by competitive inhibition or false incorporation (cell-cycle specific — S phase)",
        ["Methotrexate","5-Fluorouracil (5-FU)","Capecitabine","Cytarabine (Ara-C)","Gemcitabine","6-Mercaptopurine (6-MP)","Hydroxyurea"],
        "Methotrexate: ALL, RA, psoriasis, ectopic pregnancy, medical abortion. 5-FU/Capecitabine: GI cancers (CRC, gastric) and breast cancer. Cytarabine: AML (backbone). Gemcitabine: pancreatic, lung, bladder cancers",
        "ADR: Methotrexate — myelosuppression, mucositis, hepatotoxicity (cirrhosis chronic use), pulmonary fibrosis, nephrotoxicity (high-dose), teratogenic. 5-FU — hand-foot syndrome (palmar-plantar erythrodysesthesia), mucositis, myelosuppression, cardiotoxicity (coronary vasospasm). Rescue: leucovorin (folinic acid) for methotrexate toxicity",
        "MTX inhibits DHFR → ↓THF → ↓purines and thymidylate. Rescue: leucovorin (bypasses DHFR). 5-FU inhibits thymidylate synthase (TS) — enhanced by leucovorin. Dihydropyrimidine dehydrogenase (DPD) deficiency → severe 5-FU toxicity."
    ),
    "anthracycline": _dc(
        "Intercalate into DNA + inhibit topoisomerase II → DNA strand breaks; also generate free radicals → cardiotoxicity",
        ["Doxorubicin","Daunorubicin","Epirubicin","Idarubicin","Mitoxantrone"],
        "Breast cancer, lymphomas (CHOP regimen), leukemias (AML — daunorubicin), sarcomas, ovarian cancer",
        "ADR: cardiotoxicity (dilated cardiomyopathy — cumulative dose-dependent; baseline ECHO/MUGA, then periodic monitoring), myelosuppression, alopecia, N/V, red-colored urine (normal — not hematuria), extravasation necrosis",
        "Cardiotoxicity: doxorubicin cumulative lifetime dose <550 mg/m² (450 if prior radiation). Prevention: dexrazoxane (iron chelator — ↓free radical formation). Liposomal doxorubicin (Doxil): ↓cardiotoxicity."
    ),
    "taxane": _dc(
        "Bind β-tubulin of polymerized microtubules → stabilize microtubules (prevent depolymerization) → ↓mitosis/cell division (M-phase specific; opposite of vinca alkaloids)",
        ["Paclitaxel","Docetaxel","Cabazitaxel","Nab-paclitaxel (Abraxane)"],
        "Breast cancer (adjuvant, metastatic), ovarian cancer (paclitaxel + carboplatin = standard), NSCLC, prostate cancer (docetaxel, cabazitaxel), Kaposi sarcoma",
        "ADR: peripheral neuropathy (dose-limiting, cumulative — paclitaxel > docetaxel), myelosuppression (neutropenia), alopecia, hypersensitivity reactions (paclitaxel — Cremophor EL vehicle; premedicate with dexamethasone, diphenhydramine, H2 blocker), fluid retention/edema (docetaxel)",
        "Vinca alkaloids (vincristine, vinblastine): PREVENT polymerization (opposite of taxanes). Both cause neuropathy. Nab-paclitaxel (albumin-bound): no hypersensitivity → no premedication needed."
    ),
    "platinum analog": _dc(
        "Cross-link DNA (intra- and inter-strand cross-links at guanine N7) → block DNA replication → apoptosis (similar to alkylating agents, cell-cycle non-specific)",
        ["Cisplatin","Carboplatin","Oxaliplatin"],
        "Testicular cancer (cisplatin + bleomycin + etoposide = BEP — curative), ovarian cancer (carboplatin + paclitaxel), NSCLC, bladder, head/neck, CRC (oxaliplatin — FOLFOX regimen)",
        "ADR: cisplatin — nephrotoxicity (acute tubular necrosis — prevent with aggressive IV hydration + amifostine), ototoxicity (high-frequency hearing loss — irreversible), peripheral neuropathy, N/V (most emetogenic chemo — ondansetron + aprepitant). Carboplatin: less nephro/oto/neuro but more myelosuppression. Oxaliplatin: cold-induced peripheral neuropathy (hallmark)",
        "Cisplatin toxicity mnemonic: Nausea, nephrotoxicity, Neurotoxicity, Ototoxicity. Prevent nephrotoxicity: aggressive saline hydration + mannitol. Oxaliplatin: cold-induced dysesthesias (avoid cold beverages/touching cold objects)."
    ),
    # ── Targeted therapy ──────────────────────────────────────────────────
    "tyrosine kinase inhibitor": _dc(
        "Inhibit specific receptor or non-receptor tyrosine kinases involved in tumor growth signaling (EGFR, BCR-ABL, VEGFR, KIT, PDGFR, ALK, etc.)",
        ["Imatinib","Dasatinib","Erlotinib","Gefitinib","Osimertinib","Crizotinib","Lapatinib","Sorafenib","Sunitinib","Ibrutinib"],
        "CML/GIST (imatinib — BCR-ABL/KIT), EGFR-mutant NSCLC (erlotinib, osimertinib), ALK-rearranged NSCLC (crizotinib), HER2+ breast (lapatinib), RCC/HCC (sorafenib, sunitinib), CLL/MCL (ibrutinib — BTK inhibitor)",
        "ADR: skin rash (EGFR inhibitors — acneiform rash correlates with efficacy), GI (N/D), peripheral edema (imatinib), hepatotoxicity, QT prolongation, pneumonitis (TKIs), hand-foot syndrome (sorafenib), hypertension (anti-VEGFR), bleeding (ibrutinib)",
        "Imatinib: first small-molecule tyrosine kinase inhibitor (CML, 2001). Resistance often via kinase domain mutations → switch to next-gen (dasatinib, nilotinib). Osimertinib: 3rd-gen EGFR TKI, overcomes T790M resistance mutation."
    ),
    # ── Monoclonal antibodies (oncology) ──────────────────────────────────
    "anti-vegf": _dc(
        "Block VEGF (vascular endothelial growth factor) → ↓tumor angiogenesis → ↓tumor blood supply; also used in neovascular eye disease",
        ["Bevacizumab","Ramucirumab","Ranibizumab","Aflibercept"],
        "Colorectal cancer (bevacizumab + FOLFOX/FOLFIRI), NSCLC, RCC, cervical cancer, glioblastoma; Wet AMD/DME (ranibizumab, aflibercept — intravitreal)",
        "ADR: hypertension (↑systemic vascular resistance), proteinuria, impaired wound healing (hold perioperatively), GI perforation, thromboembolic events, hemorrhage, posterior reversible encephalopathy syndrome (PRES)",
        "Bevacizumab: wait ≥28 days after surgery (↓wound healing). Usually combined with chemotherapy (monotherapy approved in recurrent glioblastoma). Ranibizumab/aflibercept: INTRAOCULAR injection for AMD."
    ),
    # ── Rifamycins ────────────────────────────────────────────────────────
    "rifamycin": _dc(
        "Inhibit bacterial DNA-dependent RNA polymerase (β subunit) → ↓mRNA synthesis → bactericidal; potent CYP450 inducer",
        ["Rifampin","Rifabutin","Rifaximin","Rifapentine"],
        "TB treatment (RIPE: Rifampin + Isoniazid + Pyrazinamide + Ethambutol), MAC prophylaxis (rifabutin — less CYP induction → safer with HIV PIs), hepatic encephalopathy and traveler's diarrhea (rifaximin — oral, not absorbed → gut-selective), H. pylori, Neisseria meningitidis prophylaxis",
        "ADR: orange-red discoloration of body fluids (urine, tears, sweat, semen — warn patients; stains contacts), hepatotoxicity, flulike syndrome (intermittent dosing), CYP450 induction (↓warfarin, OCP, methadone, antiretrovirals, corticosteroids, many others)",
        "Rifampin: most potent CYP3A4/2C9 inducer → watch drug interactions. TB treatment 6 months (2 months RIPE + 4 months RI). Rifaximin: minimal systemic absorption → hepatic encephalopathy, traveler's diarrhea, IBS-D."
    ),
    # ── Antimycobacterials (non-rifamycin) ────────────────────────────────
    "antimycobacterial": _dc(
        "Various mechanisms targeting M. tuberculosis: INH (↓mycolic acid synthesis — KatG activation), PZA (disrupts membrane potential — acidic pH), EMB (↓arabinosyl transferase → ↓arabinogalactan), Streptomycin (30S inhibitor)",
        ["Isoniazid (INH)","Pyrazinamide (PZA)","Ethambutol (EMB)","Streptomycin","Bedaquiline","Linezolid"],
        "Active TB (RIPE × 6 months), latent TB (3HP, 4R or 3HR preferred; isoniazid 6–9 months as an alternative), drug-resistant TB (bedaquiline, linezolid)",
        "ADR: INH — peripheral neuropathy (↓B6, give pyridoxine prophylactically), hepatotoxicity, drug-induced lupus, sideroblastic anemia. PZA — hyperuricemia, hepatotoxicity. EMB — optic neuritis (red-green color blindness — visual acuity monitoring monthly). Streptomycin — ototoxicity, nephrotoxicity",
        "RIPE mnemonic side effects: Rash (all), INH-neuropathy (give B6), PZA-hyperuricemia, EMB-Eyes (optic neuritis). INH fast vs slow acetylators (NAT2 gene) → toxicity in slow acetylators."
    ),
    # ── Oxazolidinones ────────────────────────────────────────────────────
    "oxazolidinone": _dc(
        "Bind 23S rRNA of 50S ribosomal subunit at P-site → inhibit initiation complex formation (unique mechanism vs other 50S inhibitors) → bacteriostatic for most, bactericidal for Streptococcus",
        ["Linezolid","Tedizolid"],
        "MRSA (pneumonia, skin/soft tissue — alternative to vancomycin; bacteriostatic, so not first-line for endocarditis), VRE (UTI, bacteremia), Nocardia, drug-resistant TB (linezolid)",
        "ADR: myelosuppression (thrombocytopenia — check CBC weekly; reversible), peripheral/optic neuropathy (long-term), serotonin syndrome (MAO-A inhibitor → avoid SSRIs, SNRIs, opioids), lactic acidosis",
        "Linezolid: weak MAO-A inhibitor → serotonin syndrome risk with serotonergic agents. No dose adjustment needed for renal/hepatic impairment. Oral bioavailability ~100% → IV = oral efficacy."
    ),
    # ── Vasopressors / Inotropes ─────────────────────────────────────────
    "vasopressor": _dc(
        "Cause vasoconstriction (↑SVR) ± ↑cardiac output to restore perfusion pressure in shock. Act on α1 (vasoconstriction), β1 (↑HR/contractility), β2 (vasodilation), V1 (vasoconstriction) receptors",
        ["Norepinephrine","Epinephrine","Dopamine","Vasopressin","Phenylephrine","Angiotensin II"],
        "Distributive shock (septic — NE first-line), neurogenic shock, refractory shock (add vasopressin to NE), anaphylaxis (epinephrine IM first-line), cardiogenic shock (norepinephrine ± inotrope)",
        "ADR: peripheral ischemia/necrosis (extravasation — use central line; treat with phentolamine), arrhythmias, myocardial ischemia, mesenteric ischemia",
        "Norepinephrine: α1>>β1 → ↑SVR + mild ↑contractility; first-line for septic shock. Vasopressin: V1 receptor (non-adrenergic) → useful in catecholamine-resistant shock. Phenylephrine: pure α1 → reflex bradycardia."
    ),
    "inotrope": _dc(
        "↑Cardiac contractility: β1 agonists (dobutamine, dopamine), PDE3 inhibitors (milrinone), cardiac glycosides (digoxin), calcium sensitizers (levosimendan)",
        ["Dobutamine","Milrinone","Digoxin","Levosimendan","Dopamine (high dose)"],
        "Acute decompensated HF with low cardiac output/cardiogenic shock, bridge to transplant/LVAD, acute MI with cardiogenic shock",
        "ADR: arrhythmias (proarrhythmic — all inotropes), hypotension (milrinone — vasodilatory; dobutamine — mild vasodilation), tachycardia (dobutamine), tolerance (dobutamine — down-regulation of β receptors)",
        "Dobutamine: β1>>β2 → ↑CO + ↓SVR (vasodilation) — use in HF with preserved BP. Milrinone: PDE3 inhibitor → ↑cAMP → ↑contractility + vasodilation; useful when β-blockers on board."
    ),
    # ── Antithyroid agents ────────────────────────────────────────────────
    "antithyroid agent": _dc(
        "Thionamides: inhibit thyroid peroxidase → ↓organification of iodide → ↓thyroid hormone synthesis. PTU also inhibits T4→T3 peripheral conversion",
        ["Methimazole","Propylthiouracil (PTU)","Potassium iodide (Lugol solution)","Radioactive iodine (RAI)"],
        "Hyperthyroidism (Graves disease — RAI or thionamides), thyroid storm (PTU + beta-blocker + iodide + steroids), preop thyroidectomy prep (potassium iodide — Wolff-Chaikoff effect)",
        "CI: methimazole in 1st trimester (teratogenic — aplasia cutis, choanal atresia) → use PTU in 1st trimester, switch to methimazole 2nd/3rd. ADR: agranulocytosis (most serious — check ANC if fever/sore throat), rash, hepatotoxicity (PTU > methimazole), ANCA-vasculitis (PTU)",
        "Thyroid storm: PTU (blocks synthesis + conversion) + propranolol (↓symptoms + ↓T4→T3 conversion) + iodide (1h after PTU — blocks hormone release) + steroids (↓T4→T3 conversion, ↑stress response)."
    ),
    # ── Urate-lowering therapy ────────────────────────────────────────────
    "urate-lowering therapy": _dc(
        "↓Serum uric acid: xanthine oxidase inhibitors (↓uric acid synthesis) or uricosurics (↑renal uric acid excretion) or recombinant uricase (convert urate to allantoin)",
        ["Allopurinol","Febuxostat","Probenecid","Pegloticase","Rasburicase"],
        "Chronic gout prophylaxis (target uric acid <6 mg/dL), tumor lysis syndrome prophylaxis (allopurinol/rasburicase), uric acid nephrolithiasis",
        "CI: allopurinol — azathioprine/6-MP (allopurinol ↓xanthine oxidase → ↑toxic 6-MP levels → myelosuppression). Probenecid CI in renal failure and uric acid kidney stones. ADR: allopurinol — DRESS syndrome/SJS (HLA-B*5801 in Asians — screen first), rash",
        "Start urate-lowering therapy during or after a flare (ACR 2020 allows starting during a flare, with prophylaxis). Colchicine/NSAID prophylaxis for first 3–6 months of ULT. Febuxostat: ↑CV death vs allopurinol (CARES; not seen in FAST). Rasburicase and pegloticase are CONTRAINDICATED in G6PD deficiency (hemolysis, methemoglobinemia)."
    ),
    # ── Phosphodiesterase inhibitors ─────────────────────────────────────
    "pde5 inhibitor": _dc(
        "Inhibit PDE5 → ↑cGMP → smooth muscle relaxation in corpus cavernosum and pulmonary vasculature → vasodilation",
        ["Sildenafil","Tadalafil","Vardenafil","Avanafil"],
        "Erectile dysfunction, pulmonary arterial hypertension (sildenafil, tadalafil), Raynaud phenomenon",
        "CI: nitrates (severe synergistic hypotension), α-blockers (relative — hypotension), severe hepatic failure. ADR: headache, flushing, visual disturbances (blue tinge — PDE6 inhibition), priapism, hearing loss",
        "Tadalafil: longest-acting (t½ ~17.5h, effect up to 36h — 'weekend pill'). Sildenafil: 4–6h duration. All CI with nitrates — NO → ↑cGMP → PDE5i prevent breakdown → profound vasodilation + hypotension."
    ),
    # ── Antiemetics ───────────────────────────────────────────────────────
    "antiemetic": _dc(
        "Multiple mechanisms: 5-HT3 antagonists (ondansetron), D2 antagonists (metoclopramide, prochlorperazine, haloperidol), NK1 antagonists (aprepitant), H1 antagonists (promethazine), anticholinergics (scopolamine)",
        ["Ondansetron","Metoclopramide","Prochlorperazine","Aprepitant","Dexamethasone","Scopolamine","Dronabinol"],
        "CINV (chemo-induced N/V: ondansetron + aprepitant + dex — triple therapy), PONV (post-op), pregnancy nausea (B6 + doxylamine), gastroparesis (metoclopramide), motion sickness (scopolamine, meclizine)",
        "ADR: ondansetron — QT prolongation, serotonin syndrome (with other serotonergic drugs), headache. Metoclopramide — EPS/tardive dyskinesia (D2 antagonism — limit to <3 months), akathisia. Promethazine — sedation, respiratory depression",
        "Ondansetron: most commonly used antiemetic for CINV and PONV. Aprepitant (NK1 antagonist): particularly useful for delayed CINV (24–120h post-chemo). Dronabinol (THC): synthetic cannabinoid — used for refractory CINV."
    ),
    # ── Beta-2 agonists (bronchodilators) ────────────────────────────────
    "beta-2 agonist": _dc(
        "Selectively activate β2-adrenergic receptors on bronchial smooth muscle → ↑cAMP → bronchodilation; SABA (short-acting, rescue) vs LABA (long-acting, maintenance)",
        ["Albuterol (SABA)","Levalbuterol (SABA)","Salmeterol (LABA)","Formoterol (LABA)","Indacaterol (LABA)","Terbutaline"],
        "Asthma (SABA — rescue; LABA — with ICS for maintenance), COPD (SABA + LABA + LAMA triple therapy), hyperkalemia (albuterol nebulization → K+ shift into cells), preterm labor tocolysis (terbutaline)",
        "CI: LABA monotherapy in asthma (without ICS — ↑mortality, black box). ADR: tachycardia/arrhythmias, tremor, hypokalemia, hyperglycemia",
        "Asthma: LABA must always be combined with ICS; SMART = ICS-formoterol as both maintenance and reliever. COPD: LABA + LAMA (dual bronchodilation). Albuterol in hyperkalemia: onset 30 min, K+ ↓0.5–1.0 mEq/L, lasts 2h."
    ),
    # ── Muscarinic antagonist (inhaled) ───────────────────────────────────
    "lama": _dc(
        "Long-acting muscarinic antagonist: block M3 receptors on airway smooth muscle → ↓bronchoconstriction, ↓mucus secretion → bronchodilation (LAMA = long-acting, SAMA = short-acting ipratropium)",
        ["Tiotropium","Umeclidinium","Aclidinium","Glycopyrrolate (inhaled)","Ipratropium (SAMA)"],
        "COPD (first-line maintenance — tiotropium ↓exacerbations), asthma (add-on therapy), COPD triple therapy (ICS + LABA + LAMA)",
        "ADR: dry mouth (most common), urinary retention (watch in BPH), constipation, blurred vision (if powder contacts eyes). Less systemic effects than systemic anticholinergics",
        "Tiotropium: once-daily LAMA — reduces COPD exacerbations (UPLIFT trial). GOLD guidelines: LABA + LAMA preferred dual therapy for Group B/E COPD. Ipratropium (SAMA): acute COPD exacerbation + severe acute asthma."
    ),
    # ── Inhaled corticosteroids ───────────────────────────────────────────
    "inhaled corticosteroid": _dc(
        "Locally suppress airway inflammation via glucocorticoid receptor activation → ↓cytokines, ↓eosinophils, ↓mast cells; minimal systemic absorption when used correctly",
        ["Fluticasone","Budesonide","Beclomethasone","Mometasone","Ciclesonide"],
        "Asthma (controller therapy — all persistent asthma), COPD (triple therapy with LABA + LAMA, or in eosinophilic COPD)",
        "ADR: oral candidiasis (rinse mouth after use), dysphonia, adrenal suppression (high doses), growth retardation in children (high doses, less with once-daily). NOT for acute bronchospasm",
        "ICS are mainstay of asthma control — reduce ER visits and hospitalizations. ICS/LABA combos (e.g., fluticasone/salmeterol — Advair; budesonide/formoterol — Symbicort) preferred over ICS alone in moderate-severe asthma."
    ),
    # ── Hormonal contraceptives ───────────────────────────────────────────
    "combined oral contraceptive": _dc(
        "Estrogen (ethinyl estradiol) + progestin: ↓FSH/LH (via negative feedback) → ↓ovulation; progestin thickens cervical mucus + atrophies endometrium",
        ["Ethinyl estradiol + levonorgestrel","Ethinyl estradiol + norethindrone","Ethinyl estradiol + drospirenone","Ethinyl estradiol + desogestrel"],
        "Contraception (>99% effective with perfect use), dysmenorrhea, endometriosis, PCOS (↓androgens), acne (drospirenone/desogestrel), ↓ovarian cancer risk, ↓menorrhagia (↓iron-def anemia)",
        "CI: smoking >35yo (↑VTE/stroke), personal history VTE/PE/CVA, active liver disease, uncontrolled HTN, migraine with aura (↑stroke risk), breast cancer, pregnancy. ADR: N/V, breast tenderness, breakthrough bleeding, ↑VTE risk (3-4× baseline), ↑BP, ↑triglycerides, ↓libido",
        "Remember: COC ↑risk of VTE (thrombosis — progestin type matters: desogestrel/drospirenone > levonorgestrel). Progestin-only pill ('mini-pill'): safe in breastfeeding, smokers >35, VTE history. Drospirenone has antimineralocorticoid activity → ↓BP, ↓fluid retention."
    ),
    # ── Emergency contraception ───────────────────────────────────────────
    "emergency contraception": _dc(
        "Levonorgestrel: delays/inhibits ovulation; copper IUD: prevents fertilization and implantation (most effective); ulipristal: selective PR modulator → delays ovulation",
        ["Levonorgestrel (Plan B)","Ulipristal acetate (ella)","Copper IUD (Paragard)"],
        "Emergency contraception within 72h (levonorgestrel — up to 120h, less effective), 5 days (ulipristal, copper IUD — most effective ≥99%)",
        "CI: levonorgestrel — none (OTC). Ulipristal — pause breastfeeding after use (label advice ranges from 36h to 1 week). Copper IUD — copper allergy, Wilson disease, uterine anomaly. ADR: N/V, menstrual irregularities",
        "Effectiveness: Copper IUD >99% > ulipristal (~98%) > levonorgestrel (~89%). Levonorgestrel less effective in women >75kg → prefer ulipristal or copper IUD."
    ),
    # ── Tocolytics ────────────────────────────────────────────────────────
    "tocolytic": _dc(
        "Inhibit/delay uterine contractions to postpone preterm labor (goal: 48h delay for steroid administration and maternal transfer)",
        ["Nifedipine (CCB)","Magnesium sulfate (neuroprotection)","Indomethacin (NSAID)","Terbutaline (β2 agonist)"],
        "Preterm labor (24-34 weeks) — delay delivery 48h for betamethasone (fetal lung maturity) and maternal transport. Magnesium sulfate: neonatal neuroprotection if <32 weeks",
        "CI: magnesium — myasthenia gravis (↑neuromuscular blockade). Indomethacin CI >32 weeks (premature PDA closure, oligohydramnios). ADR: mag — flushing, diplopia, loss of DTRs → respiratory arrest (toxicity); monitor DTRs + UO. Nifedipine: hypotension, flushing",
        "Betamethasone (steroid): given IM × 2 doses 24h apart to mother → matures fetal lungs (↓RDS, ↓IVH, ↓NEC). Magnesium toxicity: first sign = loss of patellar reflex. Treat with IV calcium gluconate."
    ),
    # ── Immunomodulators (non-biologic DMARDs) ───────────────────────────
    "conventional dmard": _dc(
        "Modify disease process in inflammatory arthritis: MTX (↓purine synthesis), HCQ (↑lysosomal pH → ↓antigen presentation), leflunomide (↓pyrimidine synthesis), sulfasalazine (↓prostaglandins + anti-bacterial)",
        ["Methotrexate (MTX)","Hydroxychloroquine (HCQ)","Leflunomide","Sulfasalazine","Azathioprine"],
        "Rheumatoid arthritis (MTX — anchor drug), SLE (HCQ — reduces flares, ↓organ damage, ↓mortality), psoriatic arthritis, IBD (azathioprine, 6-MP), organ transplant immunosuppression (azathioprine)",
        "MTX: folate-deficient toxicity (give folic acid daily — ↓mucositis/hepatotoxicity). HCQ: retinopathy (baseline exam, then annual visual field + OCT after 5 years). Leflunomide: hepatotoxicity, teratogenic (active metabolite t½ 2 years — cholestyramine washout before pregnancy). Sulfasalazine: sulfa allergy, oligospermia (reversible)",
        "MTX is anchor DMARD for RA — start within 3-6 months of diagnosis. HCQ: only DMARD that ↓mortality in SLE. Check G6PD before HCQ in high-risk populations (hemolytic anemia risk)."
    ),
    # ── Vasodilators (direct) ────────────────────────────────────────────
    "direct vasodilator": _dc(
        "Directly relax vascular smooth muscle independent of autonomic nervous system → ↓SVR → ↓BP. Cause reflex tachycardia + sodium/water retention → combine with β-blocker + diuretic",
        ["Hydralazine","Minoxidil","Diazoxide","Fenoldopam"],
        "Hydralazine: severe HTN in pregnancy (drug of choice with labetalol), HFrEF (hydralazine + isosorbide dinitrate — alternative to ACEi/ARB in African Americans, or if ACEi/ARB intolerant). Minoxidil: refractory HTN, topical alopecia. Diazoxide: hyperinsulinemic hypoglycemia/insulinoma (opens K-ATP channels; formerly hypertensive emergency)",
        "ADR: reflex tachycardia, fluid retention, headache, flushing. Hydralazine: drug-induced lupus (anti-histone Ab — esp. slow acetylators, high dose). Minoxidil: hypertrichosis (hair growth — basis for topical Rogaine), pericardial effusion",
        "Hydralazine + nitrate: A-HeFT trial showed ↓mortality in self-identified African American HF patients. Minoxidil: combined with furosemide + beta-blocker to prevent fluid retention and reflex tachycardia."
    ),
    # ── Phosphate binders ─────────────────────────────────────────────────
    "phosphate binder": _dc(
        "Bind dietary phosphate in GI tract → prevent absorption → ↓serum phosphate; essential in CKD/ESRD to prevent renal osteodystrophy and vascular calcification",
        ["Calcium carbonate","Calcium acetate","Sevelamer (non-Ca)","Lanthanum carbonate","Sucroferric oxyhydroxide"],
        "Hyperphosphatemia in CKD/ESRD, secondary hyperparathyroidism prevention, renal osteodystrophy prevention",
        "CI: hypercalcemia (calcium-based binders). ADR: calcium-based — hypercalcemia, vascular calcification (limit if Ca >10.2). Sevelamer: GI side effects (N/D/constipation), metabolic acidosis, ↓absorption fat-soluble vitamins",
        "Non-calcium binders (sevelamer, lanthanum) preferred in patients with hypercalcemia, vascular calcification, or Ca × PO4 product >55. Sevelamer also ↓LDL (bile acid sequestrant effect)."
    ),

    # ── Polymyxins ────────────────────────────────────────────────────────
    "polymyxin": _dc(
        "Disrupt outer membrane of Gram-negative bacteria (detergent-like → pore formation → membrane instability → bactericidal); last-resort agents",
        ["Colistin (polymyxin E)","Polymyxin B"],
        "MDR Gram-negative infections: carbapenem-resistant Enterobacteriaceae (CRE), Acinetobacter baumannii, Pseudomonas aeruginosa; inhaled colistin for CF pulmonary exacerbations",
        "ADR: nephrotoxicity (dose-limiting — acute tubular injury, monitor Cr closely), neurotoxicity (paresthesias, neuromuscular blockade, dizziness)",
        "Polymyxins: agents of last resort for pan-drug-resistant (PDR) Gram-negatives. Used in combination (synergy with carbapenems/rifampin). Inhaled colistin: local lung delivery minimizes systemic toxicity."
    ),
}

_DRUG_CLASS_ALIASES = {
    "beta-blocker":               "beta blocker",
    "beta blockers":              "beta blocker",
    "beta-blockers":              "beta blocker",
    "bb":                         "beta blocker",
    "acei":                       "ace inhibitor",
    "ace-inhibitor":              "ace inhibitor",
    "ace inhibitors":             "ace inhibitor",
    "angiotensin converting enzyme inhibitor": "ace inhibitor",
    "angiotensin receptor blocker": "arb",
    "angiotensin receptor blockers": "arb",
    "arbs":                       "arb",
    "ccb":                        "calcium channel blocker",
    "calcium channel blockers":   "calcium channel blocker",
    "ccbs":                       "calcium channel blocker",
    "hmg-coa reductase inhibitor":  "statin",
    "hmg coa reductase inhibitor":  "statin",
    "statins":                    "statin",
    "ppi":                        "proton pump inhibitor",
    "ppis":                       "proton pump inhibitor",
    "benzo":                      "benzodiazepine",
    "benzos":                     "benzodiazepine",
    "bzd":                        "benzodiazepine",
    "bzds":                       "benzodiazepine",
}
