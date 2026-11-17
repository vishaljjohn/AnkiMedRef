"""Basic sciences and alternate names (tier 0.5n).

Edit freely — see data/__init__.py for how files are loaded."""
from ..formatters import _af


_BASIC_SCIENCE = {
    # ── Pharmacology ──────────────────────────────────────────────────────────
    "pharmacokinetics": _af(
        "Pharmacology — what the body does to a drug (absorption, distribution, metabolism, excretion)",
        "Bioavailability (F): fraction of an oral dose that reaches the circulation (IV = 100%; ↓ by first-pass liver metabolism — nitroglycerin, morphine, propranolol). Volume of distribution Vd = amount in body / plasma concentration — low Vd (~4–8 L) stays in plasma (large, charged or protein-bound drugs: heparin, warfarin); high Vd goes into tissues (lipophilic drugs: amiodarone, digoxin, TCAs). Clearance CL = elimination rate / plasma concentration. Half-life t½ = 0.693 × Vd / CL. Steady state after 4–5 half-lives (1 t½ = 50%, 2 = 75%, 3 = 87.5%). Loading dose = Cp × Vd / F; maintenance dose = Cp × CL × dosing interval / F",
        "Kidney or liver failure ↓clearance → lower the MAINTENANCE dose; the loading dose usually stays the same (it depends on Vd). Low albumin raises the free fraction of highly protein-bound drugs (phenytoin, warfarin). Weak acids are trapped in alkaline urine — sodium bicarbonate speeds removal of aspirin and phenobarbital."
    ),
    "zero-order kinetics": _af(
        "Pharmacology — elimination kinetics",
        "First-order (most drugs): a constant FRACTION is eliminated per unit time; half-life is constant; levels fall exponentially. Zero-order: a constant AMOUNT is eliminated per unit time (enzymes saturated); half-life is not constant; levels fall linearly and small dose increases cause large rises. Zero-order at therapeutic or high doses ('PEA'): Phenytoin, Ethanol, Aspirin (in overdose) — capacity-limited (Michaelis-Menten) kinetics",
        "Phenytoin: increase doses in small steps and check levels (correct for low albumin). Ethanol is cleared at roughly one standard drink per hour regardless of how much was drunk."
    ),
    "pharmacodynamics": _af(
        "Pharmacology — what a drug does to the body",
        "Potency = the dose needed for an effect (EC50; lower EC50 = more potent, curve shifted left). Efficacy = the maximal effect (Emax). Full agonist: maximal response. Partial agonist: lower Emax even at full occupancy (buprenorphine, aripiprazole, varenicline, pindolol) and acts as an antagonist when a full agonist is present. Competitive antagonist: reversible and surmountable — curve shifts RIGHT, same Emax (naloxone, atropine). Noncompetitive antagonist: insurmountable — ↓Emax (phenoxybenzamine). Inverse agonist: produces the opposite effect of an agonist. Therapeutic index = TD50/ED50 — narrow-index drugs need level monitoring: warfarin, digoxin, lithium, theophylline, phenytoin, aminoglycosides, vancomycin, tacrolimus/cyclosporine",
        "Tachyphylaxis = rapid tolerance after repeated doses (nitrates, ephedrine). Spare receptors allow a full response with only partial receptor occupancy."
    ),
    "cyp450 interactions": _af(
        "Pharmacology — cytochrome P450 drug interactions",
        "INDUCERS (↓levels of other drugs → e.g. contraceptive or warfarin failure): 'Chronic alcoholics Steal Phen-Phen and Never Refuse Greasy Carbs' — Chronic alcohol use, St John's wort, Phenytoin, Phenobarbital, Nevirapine, Rifampin, Griseofulvin, Carbamazepine (also efavirenz, modafinil). INHIBITORS (↑levels → toxicity): amiodarone, protease inhibitors and ritonavir, azole antifungals (ketoconazole, itraconazole, voriconazole, fluconazole), cimetidine, clarithromycin and erythromycin (not azithromycin), diltiazem and verapamil, grapefruit juice, isoniazid, fluoxetine and paroxetine (CYP2D6). CYP3A4 handles ~50% of drugs (statins, tacrolimus, cyclosporine, DOACs, many CCBs)",
        "Classic interactions: rifampin + oral contraceptive → contraceptive failure; clarithromycin + simvastatin → rhabdomyolysis; azole or macrolide + warfarin → bleeding; carbamazepine induces its own metabolism. Pharmacogenetics: CYP2D6 ultrarapid metabolizers turn codeine and tramadol into dangerous morphine levels; CYP2C19 poor metabolizers get less benefit from clopidogrel."
    ),
    "autonomic receptors": _af(
        "Pharmacology — receptor signaling of the autonomic nervous system",
        "Gq (↑IP3/DAG → ↑Ca2+) — 'HAVe 1 M&M': H1, α1, V1, M1, M3 → smooth muscle contraction (vasoconstriction; bronchoconstriction via M3) and gland secretion. Gs (↑cAMP): β1 (↑heart rate, contractility, renin), β2 (bronchodilation, vasodilation, uterine relaxation, glycogenolysis), D1, H2 (gastric acid), V2 (aquaporin-2 insertion). Gi (↓cAMP) — 'MAD 2s': M2 (↓heart rate), α2 (↓sympathetic outflow, ↓insulin), D2. Nicotinic receptors are ligand-gated ion channels (neuromuscular junction — NM; autonomic ganglia and adrenal medulla — NN). Sympathetic postganglionic fibers release norepinephrine (except sweat glands — ACh); parasympathetic fibers release ACh on muscarinic receptors",
        "Low-dose epinephrine acts mainly on β receptors; high doses add α1 vasoconstriction. Phenylephrine (pure α1) causes reflex bradycardia; isoproterenol (β1 + β2) causes tachycardia with ↓diastolic pressure. Nonselective β-blockers can cause bronchospasm (β2) and mask hypoglycemia."
    ),
    "toxidromes": _af(
        "Toxicology — recognizable poisoning syndromes",
        "Anticholinergic (TCAs, antihistamines, atropine, jimson weed): 'hot as a hare, dry as a bone, red as a beet, blind as a bat, mad as a hatter, full as a flask' — hyperthermia, DRY skin, flushing, dilated pupils, delirium, urinary retention, ↓bowel sounds, tachycardia. Cholinergic (organophosphates, nerve agents, some mushrooms): DUMBELS — Diarrhea, Urination, Miosis, Bronchorrhea/bronchospasm/bradycardia, Emesis, Lacrimation, Salivation/sweating; plus nicotinic weakness and fasciculations. Sympathomimetic (cocaine, amphetamines): tachycardia, hypertension, hyperthermia, dilated pupils, SWEATING, agitation, seizures. Opioid: pinpoint pupils, respiratory depression, sedation, ↓bowel sounds. Sedative-hypnotic (benzodiazepines, barbiturates, alcohol): CNS depression with near-normal vital signs and pupils. Serotonin syndrome: hyperthermia, clonus and hyperreflexia (legs), agitation, diarrhea",
        "Sweaty skin separates sympathomimetic (wet) from anticholinergic (dry) poisoning — both have dilated pupils and tachycardia. Cholinergic crisis kills through bronchorrhea and bronchospasm — give atropine until secretions dry, plus pralidoxime."
    ),
    "antidotes": _af(
        "Toxicology — specific antidotes",
        "Acetaminophen → N-acetylcysteine (best within 8 h; Rumack-Matthew nomogram from 4 h). Opioids → naloxone. Benzodiazepines → flumazenil (can cause seizures in chronic users — rarely used). Organophosphates → atropine + pralidoxime. Anticholinergics → physostigmine. Digoxin → digoxin immune Fab. TCAs → sodium bicarbonate (QRS >100 ms). β-blockers → glucagon (± high-dose insulin). Calcium channel blockers → calcium, high-dose insulin with glucose. Warfarin → vitamin K + 4-factor PCC. Heparin → protamine. Dabigatran → idarucizumab. Factor Xa inhibitors → andexanet alfa (or 4F-PCC). Thrombolytics → aminocaproic or tranexamic acid. Methanol/ethylene glycol → fomepizole (± dialysis). Cyanide → hydroxocobalamin. Methemoglobinemia → methylene blue (not in G6PD deficiency). Carbon monoxide → 100% or hyperbaric O2. Iron → deferoxamine. Lead → succimer, EDTA, dimercaprol. Isoniazid → pyridoxine. Salicylates → sodium bicarbonate ± dialysis. Malignant hyperthermia → dantrolene. Sulfonylurea hypoglycemia → octreotide + dextrose",
        "Activated charcoal (within ~1–2 h) does NOT bind 'PHAILS': Pesticides, Hydrocarbons, Acids/alkalis/alcohols, Iron, Lithium, Solvents. Dialyzable poisons 'I STUMBLE': Isopropanol, Salicylates, Theophylline, Uremia, Methanol, Barbiturates, Lithium, Ethylene glycol."
    ),
    # ── Immunology ────────────────────────────────────────────────────────────
    "hypersensitivity reactions": _af(
        "Immunology — Gell and Coombs types (mnemonic ACID)",
        "Type I — Anaphylactic/immediate (IgE on mast cells → histamine, leukotrienes; minutes): anaphylaxis, allergic asthma, hay fever, urticaria; skin-prick testing. Type II — Cytotoxic (IgG/IgM against cell-surface or matrix antigens → complement, ADCC, phagocytosis): autoimmune hemolytic anemia, ITP, transfusion reactions, hemolytic disease of the newborn, Goodpasture, rheumatic fever, pemphigus, bullous pemphigoid; also receptor antibodies — Graves (stimulating), myasthenia gravis (blocking); direct Coombs test. Type III — Immune complex (deposited complexes → complement → neutrophils; ↓C3): SLE, post-streptococcal GN, serum sickness (fever, rash, joint pain 1–2 weeks after a drug or foreign protein), Arthus reaction (local), polyarteritis nodosa, cryoglobulinemia. Type IV — Delayed, T-cell mediated (48–72 h; no antibodies): contact dermatitis (poison ivy, nickel), TB skin test, acute cellular transplant rejection, MS, type 1 diabetes, SJS/TEN",
        "Anaphylaxis: IM epinephrine 0.3–0.5 mg (1 mg/mL) into the thigh FIRST; antihistamines and steroids are only add-ons. A raised serum tryptase supports anaphylaxis. Types I–III are antibody-mediated; only type IV is mediated by T cells."
    ),
    "immunoglobulins": _af(
        "Immunology — antibody classes",
        "IgG — most abundant in serum, crosses the placenta (newborn passive immunity), opsonizes, fixes complement, main secondary (memory) response. IgA — mucosal secretions and breast milk; dimer with J chain + secretory component; most produced overall. IgM — first antibody made (primary response), pentamer, best at activating complement, does not cross the placenta; naive B-cell receptor (with IgD). IgE — binds mast cells and basophils (type I hypersensitivity), defends against helminths with eosinophils. IgD — B-cell receptor, unclear function. Structure: 2 heavy + 2 light chains; Fab binds antigen (variable region), Fc binds complement and Fc receptors. Class switching needs CD40–CD40L (T-cell help) + cytokines",
        "Selective IgA deficiency (most common primary immunodeficiency): sinopulmonary and GI infections, celiac disease, giardiasis, anaphylaxis to IgA in transfused blood, falsely negative IgA tTG. Hyper-IgM syndrome: CD40L defect → no class switching. Raised IgM in a newborn suggests a congenital (TORCH) infection."
    ),
    "mhc": _af(
        "Immunology — major histocompatibility complex (HLA)",
        "MHC class I (HLA-A, -B, -C): on ALL nucleated cells (not RBCs); presents endogenous peptides (viral, tumor) to CD8+ cytotoxic T cells; paired with β2-microglobulin; peptides loaded in the ER via TAP. MHC class II (HLA-DP, -DQ, -DR): on antigen-presenting cells (dendritic cells, macrophages, B cells); presents exogenous (phagocytosed) peptides to CD4+ helper T cells; loaded in endosomes after the invariant chain is removed. 'Rule of 8': MHC I × CD8 = 8, MHC II × CD4 = 8",
        "Viruses (CMV, HSV) and tumors reduce MHC I to escape CD8 cells — NK cells then kill cells lacking MHC I. Bare lymphocyte syndrome: no MHC II → no CD4 help. Drug-safety HLA alleles: B*57:01 (abacavir hypersensitivity), B*58:01 (allopurinol SJS), B*15:02 (carbamazepine SJS in Asian patients)."
    ),
    "complement system": _af(
        "Immunology — the complement cascade",
        "Pathways: classical (C1q binds IgG or IgM on antigen — 'GM makes classic cars'), lectin (mannose-binding lectin on microbes), alternative (spontaneous C3 activation on microbial surfaces). All lead to C3 convertase → C3a + C3b → C5 convertase → C5a + C5b → membrane attack complex (C5b–C9). Functions: C3b — opsonization; C3a, C4a, C5a — anaphylatoxins; C5a — neutrophil chemotaxis; MAC — cell lysis (especially Neisseria). Regulators: C1 esterase inhibitor, decay-accelerating factor (CD55), CD59, factor H",
        "Terminal complement (C5–C9) deficiency or eculizumab therapy → recurrent Neisseria infections (vaccinate against meningococcus). C1 esterase inhibitor deficiency → hereditary angioedema (↓C4, no urticaria; avoid ACE inhibitors; treat with C1-inhibitor concentrate, icatibant or ecallantide). CD55/CD59 loss (PIGA mutation) → paroxysmal nocturnal hemoglobinuria. Early classical deficiency (C1–C4) → SLE; C3 deficiency → severe pyogenic infections."
    ),
    "cytokines": _af(
        "Immunology — key cytokines",
        "IL-1: fever, acute inflammation. IL-2: T-cell growth (its receptor CD25 marks Tregs). IL-3: bone-marrow stem cells. IL-4: class switch to IgE, Th2 differentiation. IL-5: eosinophils, IgA. IL-6: fever, acute-phase proteins (CRP, hepcidin). IL-8 (CXCL8): neutrophil chemotaxis. IL-10: anti-inflammatory. IL-12: Th1 differentiation, NK activation. IL-13: IgE, airway hyperresponsiveness. IL-17: neutrophil recruitment (Th17). TNF-α: fever, cachexia, septic shock, keeps granulomas intact. IFN-γ (Th1, NK cells): activates macrophages, ↑MHC. Type I interferons (α, β): antiviral. TGF-β: anti-inflammatory, fibrosis. 'Hot T-bone stEAK': IL-1 fever, IL-2 T cells, IL-3 bone marrow, IL-4 IgE, IL-5 IgA, IL-6 acute-phase proteins",
        "Cytokine-targeting drugs: anti-TNF (infliximab, adalimumab, etanercept — reactivate latent TB, screen first), anti-IL-6 receptor (tocilizumab — RA, giant cell arteritis, cytokine release syndrome), anti-IL-1 (anakinra), anti-IL-5 (mepolizumab — eosinophilic asthma), anti-IL-4Rα (dupilumab — atopic dermatitis, asthma), anti-IL-17A (secukinumab), anti-IL-12/23 (ustekinumab)."
    ),
    "t cells": _af(
        "Immunology — T-lymphocyte subsets",
        "Mature in the thymus: positive selection in the cortex (cells that recognize self-MHC survive) and negative selection in the medulla (cells that bind self-antigen strongly die; AIRE). CD4+ helper T cells (see MHC II): Th1 (IL-12 → IFN-γ, IL-2: macrophage activation, granulomas, intracellular pathogens), Th2 (IL-4 → IL-4, IL-5, IL-13: IgE, eosinophils, helminths, allergy), Th17 (IL-6 + TGF-β → IL-17, IL-22: neutrophils, mucosal defense, autoimmunity), Treg (FOXP3+, CD25+; IL-10 and TGF-β — self-tolerance), T follicular helper cells (germinal centers). CD8+ cytotoxic T cells (see MHC I) kill infected and tumor cells with perforin, granzymes and Fas ligand. Activation needs two signals: TCR + MHC-peptide AND costimulation (CD28 with B7/CD80/86)",
        "AIRE deficiency → autoimmune polyendocrine syndrome type 1 (hypoparathyroidism, adrenal insufficiency, chronic candidiasis). FOXP3 mutation → IPEX syndrome. HIV destroys CD4 cells (CD4 <200 = AIDS). Abatacept (CTLA-4-Ig) blocks costimulation; checkpoint inhibitors (anti-PD-1, anti-CTLA-4) release the brakes on T cells."
    ),
    "primary immunodeficiencies": _af(
        "Immunology — inherited immune defects",
        "B cell: X-linked (Bruton) agammaglobulinemia (BTK — boys after 6 months, no B cells, all Ig ↓, tiny tonsils; bacterial and enteroviral infections), selective IgA deficiency (most common), CVID (onset after age 2, often adults; autoimmunity, lymphoma). T cell: DiGeorge syndrome (22q11 — thymic aplasia, hypocalcemia, heart defects), IL-12 receptor deficiency (disseminated mycobacteria), hyper-IgE / Job syndrome (STAT3 — coarse face, cold staphylococcal abscesses, retained baby teeth, eczema, ↑IgE). Combined: SCID (X-linked IL-2Rγ, ADA deficiency — failure to thrive, chronic diarrhea, thrush, no thymic shadow; stem-cell transplant), Wiskott-Aldrich syndrome (WAS — thrombocytopenia with small platelets, eczema, recurrent infections), ataxia-telangiectasia (ATM — ataxia, telangiectasias, IgA deficiency, ↑AFP, cancer), hyper-IgM syndrome (CD40L). Phagocyte: chronic granulomatous disease (NADPH oxidase — catalase-positive organisms: S. aureus, Aspergillus, Burkholderia, Serratia, Nocardia; abnormal dihydrorhodamine test), leukocyte adhesion deficiency (CD18 — delayed umbilical cord separation, no pus, very high neutrophils), Chédiak-Higashi syndrome (LYST — giant granules, albinism, neuropathy). Complement: C5–C9 (Neisseria), C1 inhibitor (hereditary angioedema)",
        "Match the infection to the defect: encapsulated bacteria → antibody (B cell) or complement defect; viruses, fungi, Pneumocystis, mycobacteria → T-cell defect; catalase-positive bacteria and fungi with abscesses → phagocyte defect (CGD). Live vaccines are contraindicated in SCID and most T-cell defects."
    ),
    "transplant rejection": _af(
        "Immunology — graft rejection and graft-versus-host disease",
        "Hyperacute (minutes–hours): preformed antibodies (ABO, HLA) → complement and thrombosis in graft vessels — prevented by crossmatching. Acute (weeks–months): cellular — CD8 T cells against donor MHC (lymphocytic infiltrate, vasculitis); antibody-mediated — donor-specific antibodies with C4d deposits; reversible with more immunosuppression. Chronic (months–years): T cells + antibodies → fibrosis and narrowing of vessels (bronchiolitis obliterans in lung, accelerated coronary disease in heart, interstitial fibrosis in kidney) — irreversible. Graft-versus-host disease: donor T cells attack the host (after stem-cell or liver transplant, or non-irradiated blood) → rash including palms and soles, jaundice/↑liver enzymes, diarrhea",
        "Immunosuppressants: calcineurin inhibitors (tacrolimus, cyclosporine — nephrotoxicity, hypertension, hyperkalemia, tremor; tacrolimus → diabetes), mTOR inhibitors (sirolimus — poor wound healing, not nephrotoxic), mycophenolate (GI upset, cytopenias), azathioprine (dangerous with allopurinol), steroids, belatacept (costimulation blocker). Irradiate blood for immunocompromised recipients to prevent transfusion GVHD."
    ),
    "vaccine types": _af(
        "Immunology — kinds of vaccines",
        "Live attenuated (strong cellular + humoral immunity, often lifelong): MMR, varicella, yellow fever, oral polio (Sabin), intranasal influenza, rotavirus, BCG, oral typhoid — contraindicated in pregnancy and severe immunodeficiency. Inactivated: injected polio (Salk), hepatitis A, rabies, injected influenza. Subunit/recombinant: hepatitis B, HPV, recombinant zoster (Shingrix), acellular pertussis, RSV. Toxoid: tetanus, diphtheria. Polysaccharide-protein conjugate (T-cell dependent → works in infants): Hib, pneumococcal (PCV15/20/21), meningococcal (MenACWY). mRNA and viral-vector: COVID-19",
        "Plain polysaccharide vaccines (PPSV23) are T-cell independent → poor response before age 2. HIV-positive patients with CD4 ≥200 can receive MMR and varicella. Egg allergy is no longer a reason to withhold influenza vaccine."
    ),
    # ── Biochemistry ──────────────────────────────────────────────────────────
    "glycolysis": _af(
        "Biochemistry — glucose → pyruvate (cytoplasm)",
        "Net 2 ATP + 2 NADH per glucose. Rate-limiting enzyme: phosphofructokinase-1 (activated by AMP and fructose-2,6-bisphosphate; inhibited by ATP and citrate). Irreversible steps: hexokinase/glucokinase (glucokinase in liver and β cells — high Km, induced by insulin), PFK-1, pyruvate kinase. Pyruvate fates: → acetyl-CoA (pyruvate dehydrogenase — needs thiamine B1, lipoic acid, CoA from B5, FAD from B2, NAD from B3), → lactate (anaerobic; RBCs depend on this), → alanine, → oxaloacetate (pyruvate carboxylase, biotin — gluconeogenesis)",
        "Pyruvate kinase deficiency → hemolytic anemia (RBCs have no mitochondria). Pyruvate dehydrogenase deficiency → lactic acidosis and neurologic problems — ketogenic diet (lysine and leucine are purely ketogenic). Thiamine deficiency blocks PDH → give thiamine BEFORE glucose to alcohol-dependent patients. Arsenic inhibits lipoic acid."
    ),
    "gluconeogenesis": _af(
        "Biochemistry — making glucose from non-carbohydrate sources (liver > kidney)",
        "Substrates: lactate (Cori cycle), alanine (glucose-alanine cycle), glycerol, propionyl-CoA (odd-chain fatty acids). EVEN-chain fatty acids cannot make glucose (acetyl-CoA cannot be converted). Bypass enzymes: pyruvate carboxylase (mitochondria; biotin; activated by acetyl-CoA), PEP carboxykinase, fructose-1,6-bisphosphatase (RATE-LIMITING; inhibited by fructose-2,6-bisphosphate and AMP), glucose-6-phosphatase (ER; liver and kidney only — muscle lacks it, so muscle glycogen cannot release free glucose). Driven by glucagon, cortisol and epinephrine; inhibited by insulin",
        "Fasting: glycogen supplies glucose for ~12–24 h, then gluconeogenesis takes over and ketones increasingly fuel the brain. Alcohol blocks gluconeogenesis (↑NADH/NAD+) → fasting hypoglycemia in heavy drinkers. Von Gierke disease (glucose-6-phosphatase deficiency) → severe fasting hypoglycemia, lactic acidosis, big liver."
    ),
    "tca cycle": _af(
        "Biochemistry — Krebs (citric acid) cycle in the mitochondrial matrix",
        "Acetyl-CoA + oxaloacetate → citrate → isocitrate → α-ketoglutarate → succinyl-CoA → succinate → fumarate → malate → oxaloacetate ('Can I Keep Selling Sex For Money, Officer?'). Rate-limiting enzyme: isocitrate dehydrogenase (activated by ADP; inhibited by ATP and NADH). Per acetyl-CoA: 3 NADH, 1 FADH2, 1 GTP, 2 CO2 (~10 ATP). α-Ketoglutarate dehydrogenase uses the same cofactors as pyruvate dehydrogenase (B1, B2, B3, B5, lipoic acid). Succinyl-CoA feeds heme synthesis",
        "Thiamine deficiency blocks both pyruvate dehydrogenase and α-ketoglutarate dehydrogenase → energy failure in the brain (Wernicke) and heart (wet beriberi). Fluoroacetate (a rodent poison) inhibits aconitase."
    ),
    "electron transport chain": _af(
        "Biochemistry — oxidative phosphorylation on the inner mitochondrial membrane",
        "NADH feeds complex I and FADH2 feeds complex II → coenzyme Q → complex III → cytochrome c → complex IV (cytochrome c oxidase) → O2 + H+ → H2O. The proton gradient drives ATP synthase (complex V). ~2.5 ATP per NADH and ~1.5 per FADH2; ~32 ATP per glucose aerobically vs 2 anaerobically. Inhibitors: complex I — rotenone (metformin weakly); complex III — antimycin A; complex IV — cyanide, carbon monoxide, azide, hydrogen sulfide; ATP synthase — oligomycin. Uncouplers (more O2 use and heat, less ATP): 2,4-dinitrophenol, high-dose aspirin, thermogenin (UCP-1) in brown fat",
        "Cyanide (house fires, nitroprusside) → lactic acidosis with oxygen-rich venous blood; treat with hydroxocobalamin. Aspirin overdose uncouples → hyperthermia. Mitochondrial DNA encodes some chain subunits → maternally inherited disorders (MELAS, MERRF)."
    ),
    "urea cycle": _af(
        "Biochemistry — ammonia disposal in the liver (mitochondria + cytoplasm)",
        "NH3 + CO2 → carbamoyl phosphate (carbamoyl phosphate synthetase I — RATE-LIMITING; needs N-acetylglutamate) + ornithine → citrulline (ornithine transcarbamylase) → argininosuccinate (+ aspartate) → arginine (releases fumarate) → urea + ornithine (arginase). 'Ordinarily, Careless Crappers Are Also Frivolous About Urination': Ornithine, Carbamoyl phosphate, Citrulline, Aspartate, Argininosuccinate, Fumarate, Arginine, Urea",
        "Ornithine transcarbamylase (OTC) deficiency — most common urea cycle disorder, X-linked: hyperammonemia in infancy (vomiting, lethargy, cerebral edema) with ↑urinary orotic acid but NO megaloblastic anemia (unlike orotic aciduria). Treat hyperammonemia with a low-protein diet, lactulose, sodium benzoate/phenylbutyrate and dialysis. CPS I deficiency has no orotic acid rise."
    ),
    "beta oxidation": _af(
        "Biochemistry — fatty acid oxidation and ketone bodies (mitochondria)",
        "Long-chain fatty acids enter mitochondria through the carnitine shuttle (carnitine palmitoyltransferase I — inhibited by malonyl-CoA, so synthesis and breakdown do not run together). Each cycle removes 2 carbons → acetyl-CoA + NADH + FADH2. In fasting or diabetes, excess acetyl-CoA in the liver becomes ketone bodies (acetoacetate, β-hydroxybutyrate) used by brain, heart and muscle; the liver itself cannot use ketones (lacks thiophorase). Fatty acid SYNTHESIS happens in the cytoplasm: acetyl-CoA carboxylase (biotin; rate-limiting; activated by insulin), with the citrate shuttle carrying acetyl-CoA out of mitochondria",
        "MCAD deficiency (most common fatty-acid oxidation defect, AR): fasting → hypoKETOtic hypoglycemia, lethargy, can mimic sudden infant death — avoid fasting, give carbohydrate. Carnitine deficiency → weakness, hypoketotic hypoglycemia. Urine ketone dipsticks detect acetoacetate, not β-hydroxybutyrate (the main ketone in DKA)."
    ),
    "pentose phosphate pathway": _af(
        "Biochemistry — hexose monophosphate (HMP) shunt in the cytoplasm",
        "Oxidative (irreversible) phase: glucose-6-phosphate dehydrogenase (G6PD — RATE-LIMITING) → NADPH + ribulose-5-phosphate. Non-oxidative (reversible) phase: transketolase (needs thiamine) makes ribose-5-phosphate for nucleotides and recycles glycolytic intermediates. NADPH is used for glutathione reduction (protects RBCs from oxidants), fatty acid and steroid synthesis, the respiratory burst (NADPH oxidase) and cytochrome P450. No ATP made or used. Active in RBCs, liver, adrenal cortex, lactating breast",
        "G6PD deficiency (X-linked) → ↓NADPH → ↓reduced glutathione → oxidant hemolysis (fava beans, sulfonamides, primaquine, dapsone, nitrofurantoin, rasburicase, infection) with Heinz bodies and bite cells; protects against malaria. Measure G6PD weeks after a hemolytic episode (young RBCs have more enzyme). RBC transketolase activity tests for thiamine deficiency."
    ),
    "glycogen storage diseases": _af(
        "Biochemistry — inherited defects of glycogen metabolism (mostly AR)",
        "Type I von Gierke (glucose-6-phosphatase): severe fasting hypoglycemia, lactic acidosis, high uric acid and triglycerides, big liver and kidneys — frequent cornstarch feeds, avoid fructose and galactose. Type II Pompe (lysosomal acid α-glucosidase / acid maltase): cardiomegaly, hypotonia, large tongue, early death in the infantile form — enzyme replacement (alglucosidase alfa); 'Pompe trashes the pump'. Type III Cori (debranching enzyme): milder von Gierke-like picture with NORMAL lactate. Type V McArdle (muscle glycogen phosphorylase): exercise cramps, myoglobinuria, 'second wind', no lactate rise on exercise. Order of types I–V: 'Very Poor Carbohydrate Metabolism' — Von Gierke, Pompe, Cori, McArdle",
        "Glycogen = α-1,4 chains with α-1,6 branches; glycogen phosphorylase (needs vitamin B6) is rate-limiting for breakdown and glycogen synthase for synthesis. Hers disease (type VI, liver phosphorylase) is mild."
    ),
    "lysosomal storage diseases": _af(
        "Biochemistry — sphingolipidoses and mucopolysaccharidoses",
        "Tay-Sachs (hexosaminidase A; GM2) — neurodegeneration, cherry-red macula, NO hepatosplenomegaly, onion-skin lysosomes. Niemann-Pick A/B (sphingomyelinase) — cherry-red spot WITH hepatosplenomegaly, foam cells. Gaucher (glucocerebrosidase) — most common; hepatosplenomegaly, pancytopenia, bone crises, Erlenmeyer-flask femur, 'crumpled tissue paper' macrophages — enzyme replacement (imiglucerase). Fabry (α-galactosidase A; X-linked) — burning pain in hands and feet, angiokeratomas, reduced sweating, later kidney failure and cardiomyopathy. Krabbe (galactocerebrosidase) — globoid cells, optic atrophy, neuropathy. Metachromatic leukodystrophy (arylsulfatase A) — central and peripheral demyelination. Hurler (α-L-iduronidase) — corneal clouding, coarse facial features, developmental delay. Hunter (iduronate-2-sulfatase; X-linked) — like Hurler but NO corneal clouding, aggressive behavior",
        "All are autosomal recessive EXCEPT Fabry and Hunter (X-linked recessive) — 'Hunters see clearly (no corneal clouding) and aim for the X'. I-cell disease: no mannose-6-phosphate tag (phosphotransferase defect) → enzymes are secreted instead of reaching lysosomes; coarse features, ↑plasma lysosomal enzymes."
    ),
    "water-soluble vitamins": _af(
        "Biochemistry — B vitamins and vitamin C",
        "B1 thiamine (pyruvate dehydrogenase, α-ketoglutarate dehydrogenase, transketolase): Wernicke-Korsakoff, beriberi (dry — neuropathy; wet — high-output heart failure). B2 riboflavin (FAD/FMN): cheilosis, angular stomatitis, corneal vascularization. B3 niacin (NAD; made from tryptophan): pellagra — Diarrhea, Dermatitis (sun-exposed, Casal necklace), Dementia — seen with Hartnup disease, carcinoid syndrome, isoniazid; high doses → flushing (aspirin prevents it), hyperglycemia, hyperuricemia. B5 pantothenate (CoA): dermatitis. B6 pyridoxine (transaminases, heme synthesis, neurotransmitters): deficiency with isoniazid → neuropathy, seizures, sideroblastic anemia. B7 biotin (carboxylases): raw egg whites (avidin) → hair loss, dermatitis. B9 folate: megaloblastic anemia without neurologic signs, neural tube defects. B12 cobalamin: megaloblastic anemia + subacute combined degeneration, ↑methylmalonic acid. C ascorbic acid (collagen hydroxylation, iron absorption, dopamine β-hydroxylase): scurvy — bleeding gums, perifollicular hemorrhages, corkscrew hairs, poor wound healing",
        "Too much B6 → sensory neuropathy; too much vitamin C → calcium oxalate stones and worse iron overload in hemochromatosis. Except for B12 and folate, water-soluble vitamins have small stores, so deficiencies develop quickly."
    ),
    "fat-soluble vitamins": _af(
        "Biochemistry — vitamins A, D, E and K",
        "Absorption needs bile and pancreatic lipase → deficiency with fat malabsorption (cystic fibrosis, celiac disease, cholestasis, orlistat, bariatric surgery). Vitamin A (retinol): vision (rhodopsin) and epithelial health — deficiency → night blindness, Bitot spots, xerophthalmia, poor immunity (give in measles); excess → idiopathic intracranial hypertension, liver toxicity, birth defects (isotretinoin — cleft palate, heart defects). Vitamin D: deficiency → rickets/osteomalacia; excess → hypercalcemia. Vitamin E (antioxidant): deficiency → hemolytic anemia, spinocerebellar ataxia and posterior column loss (like B12 deficiency, but without megaloblastic anemia and with normal methylmalonic acid); high doses raise bleeding risk on warfarin. Vitamin K: γ-carboxylation of factors II, VII, IX, X and proteins C and S — deficiency in newborns, with antibiotics or malabsorption → ↑PT/INR",
        "Newborns get IM vitamin K at birth to prevent vitamin K deficiency bleeding (sterile gut, poor placental transfer). Warfarin blocks vitamin K epoxide reductase (VKORC1). Fat-soluble vitamins are stored, so toxicity is possible (especially A and D)."
    ),
}

_BASIC_SCIENCE_ALIASES = {
    "adme": "pharmacokinetics", "bioavailability": "pharmacokinetics",
    "volume of distribution": "pharmacokinetics", "half-life": "pharmacokinetics",
    "half life": "pharmacokinetics", "drug half-life": "pharmacokinetics",
    "loading dose": "pharmacokinetics", "maintenance dose": "pharmacokinetics",
    "steady state": "pharmacokinetics", "first-pass metabolism": "pharmacokinetics",
    "first pass metabolism": "pharmacokinetics", "first-pass effect": "pharmacokinetics",
    "first-order kinetics": "zero-order kinetics", "first order kinetics": "zero-order kinetics",
    "zero order kinetics": "zero-order kinetics", "elimination kinetics": "zero-order kinetics",
    "michaelis-menten kinetics": "zero-order kinetics",
    "agonist": "pharmacodynamics", "antagonist": "pharmacodynamics",
    "partial agonist": "pharmacodynamics", "inverse agonist": "pharmacodynamics",
    "competitive antagonist": "pharmacodynamics", "noncompetitive antagonist": "pharmacodynamics",
    "potency": "pharmacodynamics", "therapeutic index": "pharmacodynamics",
    "therapeutic window": "pharmacodynamics", "dose-response curve": "pharmacodynamics",
    "ec50": "pharmacodynamics", "tachyphylaxis": "pharmacodynamics",
    "cyp450": "cyp450 interactions", "cytochrome p450": "cyp450 interactions",
    "p450": "cyp450 interactions", "cyp3a4": "cyp450 interactions",
    "cyp450 inducers": "cyp450 interactions", "cyp450 inhibitors": "cyp450 interactions",
    "cyp inducers": "cyp450 interactions", "cyp inhibitors": "cyp450 interactions",
    "enzyme inducers": "cyp450 interactions", "enzyme inhibitors": "cyp450 interactions",
    "drug interactions": "cyp450 interactions",
    "adrenergic receptors": "autonomic receptors", "alpha-1 receptor": "autonomic receptors",
    "alpha 1 receptor": "autonomic receptors", "beta-1 receptor": "autonomic receptors",
    "beta-2 receptor": "autonomic receptors", "beta receptors": "autonomic receptors",
    "alpha receptors": "autonomic receptors", "muscarinic receptors": "autonomic receptors",
    "nicotinic receptors": "autonomic receptors", "g protein-coupled receptors": "autonomic receptors",
    "gpcr": "autonomic receptors", "second messengers": "autonomic receptors",
    "toxidrome": "toxidromes", "anticholinergic toxidrome": "toxidromes",
    "cholinergic toxidrome": "toxidromes", "sympathomimetic toxidrome": "toxidromes",
    "opioid toxidrome": "toxidromes", "dumbels": "toxidromes",
    "anticholinergic syndrome": "toxidromes", "cholinergic crisis": "toxidromes",
    "organophosphate poisoning": "toxidromes",
    "antidote": "antidotes", "poisoning antidotes": "antidotes",
    "type i hypersensitivity": "hypersensitivity reactions",
    "type ii hypersensitivity": "hypersensitivity reactions",
    "type iii hypersensitivity": "hypersensitivity reactions",
    "type iv hypersensitivity": "hypersensitivity reactions",
    "type 1 hypersensitivity": "hypersensitivity reactions",
    "type 2 hypersensitivity": "hypersensitivity reactions",
    "type 3 hypersensitivity": "hypersensitivity reactions",
    "type 4 hypersensitivity": "hypersensitivity reactions",
    "hypersensitivity": "hypersensitivity reactions", "gell and coombs": "hypersensitivity reactions",
    "serum sickness": "hypersensitivity reactions", "arthus reaction": "hypersensitivity reactions",
    "delayed-type hypersensitivity": "hypersensitivity reactions",
    "immune complex disease": "hypersensitivity reactions",
    "igg": "immunoglobulins", "iga": "immunoglobulins", "igm": "immunoglobulins",
    "ige": "immunoglobulins", "igd": "immunoglobulins", "antibody classes": "immunoglobulins",
    "immunoglobulin": "immunoglobulins", "immunoglobulin classes": "immunoglobulins",
    "antibody structure": "immunoglobulins",
    "mhc class i": "mhc", "mhc class ii": "mhc", "mhc i": "mhc", "mhc ii": "mhc",
    "major histocompatibility complex": "mhc", "antigen presentation": "mhc",
    "hla class i": "mhc", "hla class ii": "mhc",
    "complement": "complement system", "complement cascade": "complement system",
    "membrane attack complex": "complement system", "classical pathway": "complement system",
    "alternative pathway": "complement system", "lectin pathway": "complement system",
    "c5a": "complement system", "c3b": "complement system",
    "hereditary angioedema": "complement system",
    "cytokine": "cytokines", "interleukins": "cytokines", "interleukin": "cytokines",
    "il-1": "cytokines", "il-2": "cytokines", "il-4": "cytokines", "il-6": "cytokines",
    "il-10": "cytokines", "il-12": "cytokines", "il-17": "cytokines",
    "tnf-alpha": "cytokines", "tnf alpha": "cytokines", "tnf-α": "cytokines",
    "interferon gamma": "cytokines", "ifn-gamma": "cytokines", "interferons": "cytokines",
    "t cell": "t cells", "t-cells": "t cells", "t lymphocytes": "t cells",
    "helper t cells": "t cells", "cd4": "t cells", "cd4 cells": "t cells",
    "cd4+ t cells": "t cells", "cd8": "t cells", "cytotoxic t cells": "t cells",
    "th1": "t cells", "th2": "t cells", "th17": "t cells", "regulatory t cells": "t cells",
    "treg": "t cells", "tregs": "t cells", "thymic selection": "t cells",
    "primary immunodeficiency": "primary immunodeficiencies",
    "immunodeficiency": "primary immunodeficiencies", "scid": "primary immunodeficiencies",
    "severe combined immunodeficiency": "primary immunodeficiencies",
    "cvid": "primary immunodeficiencies", "common variable immunodeficiency": "primary immunodeficiencies",
    "bruton agammaglobulinemia": "primary immunodeficiencies",
    "x-linked agammaglobulinemia": "primary immunodeficiencies",
    "chronic granulomatous disease": "primary immunodeficiencies",
    "cgd": "primary immunodeficiencies", "wiskott-aldrich syndrome": "primary immunodeficiencies",
    "ataxia-telangiectasia": "primary immunodeficiencies",
    "leukocyte adhesion deficiency": "primary immunodeficiencies",
    "chediak-higashi syndrome": "primary immunodeficiencies",
    "hyper-ige syndrome": "primary immunodeficiencies", "job syndrome": "primary immunodeficiencies",
    "iga deficiency": "primary immunodeficiencies", "selective iga deficiency": "primary immunodeficiencies",
    "hyper-igm syndrome": "primary immunodeficiencies",
    "graft rejection": "transplant rejection", "organ rejection": "transplant rejection",
    "hyperacute rejection": "transplant rejection", "acute rejection": "transplant rejection",
    "chronic rejection": "transplant rejection", "graft versus host disease": "transplant rejection",
    "graft-versus-host disease": "transplant rejection", "gvhd": "transplant rejection",
    "vaccine": "vaccine types", "vaccines": "vaccine types", "live vaccines": "vaccine types",
    "live attenuated vaccine": "vaccine types", "inactivated vaccine": "vaccine types",
    "toxoid": "vaccine types", "conjugate vaccine": "vaccine types",
    "glycolytic pathway": "glycolysis", "phosphofructokinase": "glycolysis",
    "pfk-1": "glycolysis", "pyruvate kinase": "glycolysis", "pyruvate dehydrogenase": "glycolysis",
    "pyruvate kinase deficiency": "glycolysis",
    "cori cycle": "gluconeogenesis", "fructose-1,6-bisphosphatase": "gluconeogenesis",
    "pyruvate carboxylase": "gluconeogenesis", "glucose-6-phosphatase": "gluconeogenesis",
    "pepck": "gluconeogenesis",
    "krebs cycle": "tca cycle", "citric acid cycle": "tca cycle",
    "tricarboxylic acid cycle": "tca cycle",
    "oxidative phosphorylation": "electron transport chain", "atp synthase": "electron transport chain",
    "cytochrome c oxidase": "electron transport chain", "uncouplers": "electron transport chain",
    "respiratory chain": "electron transport chain",
    "ornithine cycle": "urea cycle", "ornithine transcarbamylase deficiency": "urea cycle",
    "otc deficiency": "urea cycle", "hyperammonemia": "urea cycle",
    "beta-oxidation": "beta oxidation", "fatty acid oxidation": "beta oxidation",
    "ketone bodies": "beta oxidation", "ketogenesis": "beta oxidation",
    "carnitine shuttle": "beta oxidation", "mcad deficiency": "beta oxidation",
    "fatty acid synthesis": "beta oxidation",
    "hmp shunt": "pentose phosphate pathway", "hexose monophosphate shunt": "pentose phosphate pathway",
    "pentose phosphate shunt": "pentose phosphate pathway", "nadph": "pentose phosphate pathway",
    "glycogen storage disease": "glycogen storage diseases", "von gierke disease": "glycogen storage diseases",
    "pompe disease": "glycogen storage diseases", "cori disease": "glycogen storage diseases",
    "mcardle disease": "glycogen storage diseases",
    "lysosomal storage disease": "lysosomal storage diseases", "sphingolipidoses": "lysosomal storage diseases",
    "mucopolysaccharidoses": "lysosomal storage diseases", "fabry disease": "lysosomal storage diseases",
    "krabbe disease": "lysosomal storage diseases",
    "metachromatic leukodystrophy": "lysosomal storage diseases",
    "hurler syndrome": "lysosomal storage diseases", "hunter syndrome": "lysosomal storage diseases",
    "i-cell disease": "lysosomal storage diseases",
    "b vitamins": "water-soluble vitamins", "water soluble vitamins": "water-soluble vitamins",
    "vitamin b1": "water-soluble vitamins", "thiamine": "water-soluble vitamins",
    "vitamin b2": "water-soluble vitamins", "riboflavin": "water-soluble vitamins",
    "vitamin b3": "water-soluble vitamins", "niacin": "water-soluble vitamins",
    "vitamin b6": "water-soluble vitamins", "pyridoxine": "water-soluble vitamins",
    "biotin": "water-soluble vitamins", "vitamin c": "water-soluble vitamins",
    "ascorbic acid": "water-soluble vitamins", "beriberi": "water-soluble vitamins",
    "pellagra": "water-soluble vitamins", "scurvy": "water-soluble vitamins",
    "fat soluble vitamins": "fat-soluble vitamins", "vitamin a": "fat-soluble vitamins",
    "retinol": "fat-soluble vitamins", "vitamin e": "fat-soluble vitamins",
    "vitamin k": "fat-soluble vitamins", "vitamin k deficiency": "fat-soluble vitamins",
    "night blindness": "fat-soluble vitamins", "hypervitaminosis a": "fat-soluble vitamins",
}
