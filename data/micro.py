"""Microbiology organisms and disease names (tier 0.5d).

Edit freely — see data/__init__.py for how files are loaded."""
from ..formatters import _mo


_MICRO = {
    # ── Gram-positive cocci ───────────────────────────────────────────────
    "s aureus": _mo(
        "Gram+ cocci in clusters; β-hemolytic; catalase+ coagulase+",
        "Protein A (inhibits opsonization), TSST-1 (toxic shock — superantigen), exfoliatin (SSSS), Panton-Valentine leukocidin (PVL — necrotizing pneumonia/skin), coagulase (clots fibrin — abscess formation)",
        "Skin/soft tissue infections (furuncles, impetigo, cellulitis), bacteremia, endocarditis (IV drug users — tricuspid valve), osteomyelitis (most common cause), septic arthritis, pneumonia (post-influenza), food poisoning (preformed heat-stable toxin — rapid onset 1–6h, N/V), MRSA (healthcare and community)",
        "MSSA: nafcillin/oxacillin (penicillinase-resistant penicillins). MRSA: vancomycin (IV) or linezolid/daptomycin. Community MRSA skin: TMP-SMX or doxycycline. Decolonization: mupirocin nasal ointment + chlorhexidine baths",
        "S. aureus is catalase+ and coagulase+ (the main coagulase-positive human Staph). MRSA resistance: altered PBP2a (mecA gene) → β-lactams cannot bind. PVL toxin → necrotizing pneumonia in young healthy patients (post-influenza). SSSS (scalded skin syndrome): desquamation at desmoglein-1 cleavage site."
    ),
    "staphylococcus aureus": _mo(
        "Gram+ cocci in clusters; β-hemolytic; catalase+ coagulase+",
        "Protein A (Fc binding → immune evasion), TSST-1 (superantigen → cytokine storm), exfoliatin (SSSS), PVL (necrotizing infections), coagulase (abscess formation)",
        "Skin/soft tissue, bacteremia, endocarditis (IV drug use → tricuspid; prosthetic valve), osteomyelitis, septic arthritis, post-influenza pneumonia, food poisoning (1–6h), toxic shock syndrome, SSSS",
        "MSSA: anti-staphylococcal PCN (nafcillin/oxacillin). MRSA: vancomycin (IV), linezolid, daptomycin. Skin MRSA: TMP-SMX, doxycycline",
        "MCC of: osteomyelitis, septic arthritis, endocarditis (IV drug users), post-influenza pneumonia. Food poisoning: preformed toxin (heat-stable) → no fever, rapid onset 1–6h, vomiting-predominant."
    ),
    "mrsa": _mo(
        "Gram+ cocci in clusters; methicillin-resistant S. aureus — mecA gene → altered PBP2a → β-lactam resistance",
        "Same as S. aureus + mecA gene (PBP2a — low affinity for β-lactams). SCCmec (mobile genetic element carries mecA)",
        "Healthcare-MRSA (HA-MRSA): bacteremia, pneumonia (ventilator-associated), line infections, UTI. Community-MRSA (CA-MRSA): skin/soft tissue (boils, furuncles, abscesses — USA300 clone), necrotizing pneumonia (PVL+)",
        "IV/systemic: vancomycin (AUC-guided dosing 400–600 mg·h/L) or daptomycin (not pneumonia — inactivated by surfactant) or linezolid. Oral: TMP-SMX, doxycycline, clindamycin. Ceftaroline: 5th-gen cephalosporin active vs MRSA",
        "Decolonize MRSA carriers: mupirocin 2% nasal ointment × 5 days + chlorhexidine body wash. Failure of β-lactams in S. aureus: rule out MRSA. Vancomycin MIC creep → switch to daptomycin or ceftaroline for MIC ≥2."
    ),
    "strep pyogenes": _mo(
        "Gram+ cocci in chains; β-hemolytic (Group A Strep — GAS); catalase− bacitracin-sensitive",
        "M protein (anti-phagocytic — basis of type-specific immunity), hyaluronidase (spreading factor), streptokinase, streptolysin O/S (hemolysis — ASO titer), pyrogenic exotoxins A/B/C (superantigens → scarlet fever/TSS)",
        "Pharyngitis (strep throat — most common bacterial pharyngitis), impetigo (non-bullous), cellulitis/erysipelas, necrotizing fasciitis (type II — 'flesh-eating' — GAS), streptococcal TSS, rheumatic fever (→ rheumatic heart disease), post-strep glomerulonephritis (non-suppurative sequelae)",
        "PCN G or amoxicillin (first-line — 10 days; GAS NEVER develops PCN resistance). Penicillin allergy: cephalexin (non-anaphylactic allergy), clindamycin, azithromycin. Necrotizing fasciitis: IV PCN + clindamycin (inhibits toxin production) + surgical debridement",
        "Anti-streptolysin O (ASO) titer: ↑in pharyngitis (not impetigo — DNase B titer for skin). Rheumatic fever (Jones criteria): J♥NES — Joints (migratory polyarthritis), ♥ carditis (mitral regurgitation), Nodules (subcutaneous), Erythema marginatum, Sydenham chorea. Prevent with PCN prophylaxis."
    ),
    "group a strep": _mo(
        "Gram+ cocci in chains; β-hemolytic; catalase−; Lancefield Group A; bacitracin-sensitive",
        "M protein (anti-phagocytic), hyaluronidase, streptokinase, streptolysin O/S, pyrogenic exotoxins (scarlet fever/TSS)",
        "Strep pharyngitis, impetigo, erysipelas, cellulitis, necrotizing fasciitis (GAS), scarlet fever, streptococcal TSS, rheumatic fever, PSGN",
        "Amoxicillin or PCN V × 10 days (pharyngitis). Clindamycin + PCN (invasive GAS — clindamycin inhibits toxin production). Never penicillin-resistant",
        "GABHS never develops PCN resistance — always treat with PCN/amoxicillin. Treat pharyngitis to prevent rheumatic fever (ARF); PSGN is not prevented by antibiotics (throat or skin infection)."
    ),
    "strep pneumoniae": _mo(
        "Gram+ diplococci (lancet-shaped); α-hemolytic; catalase−; optochin-sensitive; bile-soluble; encapsulated",
        "Polysaccharide capsule (anti-phagocytic; 90+ serotypes), pneumolysin (cytotoxin), IgA protease, phospholipase C",
        "Pneumonia (CAP — lobar pneumonia, rust-colored sputum; most common bacterial CAP), meningitis (most common in adults), otitis media (most common in children), sinusitis, bacteremia, septic arthritis",
        "PCN (if susceptible), amoxicillin-clavulanate, ceftriaxone, fluoroquinolone (respiratory). Meningitis: vancomycin + ceftriaxone (empiric for PCN resistance) + dexamethasone (before/with antibiotics). Vaccine: PCV20 or PCV21 alone, or PCV15 followed by PPSV23",
        "Quellung reaction (capsule swells with anti-sera) — identifies capsular type. Optochin sensitivity distinguishes from viridans strep (optochin-resistant). PCN resistance via altered PBPs (not β-lactamase). Asplenic patients at highest risk → vaccinate."
    ),
    "n meningitidis": _mo(
        "Gram− diplococci (kidney bean-shaped); oxidase+; encapsulated (serogroups A,B,C,W,Y,X); ferments glucose AND maltose",
        "Polysaccharide capsule (anti-phagocytic), LOS (lipooligosaccharide — endotoxin), IgA protease, pili (adhesion)",
        "Meningococcal meningitis (young adults, college dormitories, asplenic patients), meningococcemia (petechial/purpuric rash — 'shotgun pellet' rash), Waterhouse-Friderichsen syndrome (bilateral adrenal hemorrhage → adrenal crisis), DIC",
        "Ceftriaxone (drug of choice). Prophylaxis for close contacts: ciprofloxacin (single dose, preferred) or rifampin × 2 days or ceftriaxone IM (single dose). Vaccine: MenACWY + MenB (serogroup B — Bexsero/Trumenba)",
        "Waterhouse-Friderichsen: fulminant meningococcemia → bilateral adrenal hemorrhage → acute adrenal insufficiency + shock + DIC + purpuric rash → rapidly fatal. Most rapid progression of any bacterial meningitis. Give antibiotics before LP if suspected."
    ),
    "n gonorrhoeae": _mo(
        "Gram− diplococci (intracellular in PMNs); oxidase+; does NOT ferment maltose (vs N. meningitidis which does); non-encapsulated; fastidious (Thayer-Martin medium)",
        "Pili (adhesion), opacity proteins (Opa — invasion), IgA protease, LOS (pro-inflammatory)",
        "Gonorrhea (urethritis — purulent discharge, dysuria; cervicitis; rectal; pharyngeal — often asymptomatic), PID (endometritis + salpingitis → ectopic pregnancy, infertility, Fitz-Hugh-Curtis — perihepatitis), DGI (disseminated gonococcal infection — triad: migratory polyarthritis + dermatitis + tenosynovitis)",
        "Ceftriaxone 500mg IM × 1 (uncomplicated) + doxycycline 100 mg BID × 7 days if chlamydia is not excluded (CDC 2020 — azithromycin no longer advised for co-treatment). DGI: ceftriaxone IV until improved → oral cefixime to complete 7–14 days. Report to public health",
        "Test of cure NOT routinely recommended for uncomplicated GC with ceftriaxone (if pharyngeal or treatment failure → repeat in 1–2 weeks). Partner treatment essential. PPNG (penicillinase-producing N. gonorrhoeae) → never use PCN. Screen all pregnant women, sexually active women <25yo."
    ),
    "e coli": _mo(
        "Gram− rod (bacillus); oxidase−; lactose-fermenter (pink on MacConkey); facultative anaerobe; motile; indole+",
        "Type 1 pili (uroepithelial adherence), P pili (pyelonephritis), heat-labile/heat-stable enterotoxins (ETEC), Shiga toxin (STEC/EHEC — O157:H7 — HUS), intimin (EPEC), bundle-forming pili",
        "UTI/pyelonephritis (most common cause of UTI), neonatal meningitis + sepsis (K1 capsule), ETEC (traveler's diarrhea — watery, no fever), EHEC O157:H7 (bloody diarrhea + HUS — TTP-like: ↓platelets + AKI + MAHA), EPEC (infant diarrhea)",
        "UTI: TMP-SMX or nitrofurantoin (uncomplicated cystitis); fluoroquinolone (complicated). Pyelonephritis: ceftriaxone or fluoroquinolone. ETEC: azithromycin or rifaximin (traveler's diarrhea). EHEC: supportive ONLY — NO antibiotics (↑HUS risk — antibiotics ↑Shiga toxin release)",
        "ETEC: heat-labile toxin (activates adenylyl cyclase → ↑cAMP → ↑Cl secretion); heat-stable toxin (activates guanylyl cyclase → ↑cGMP). EHEC O157:H7: bloody diarrhea, no fever, HUS (children most vulnerable) — DO NOT give antibiotics or antimotility agents."
    ),
    "pseudomonas": _mo(
        "Gram− rod; oxidase+; non-lactose fermenter (clear on MacConkey); obligate aerobe; motile; non-fermenter; produces pyocyanin (blue-green pigment) and pyoverdin (yellow-green fluorescent)",
        "Alginate (biofilm — CF mucoid strains), exotoxin A (ADP-ribosylation of EF-2 → ↓protein synthesis — same as diphtheria toxin), elastase/protease (tissue destruction), pili, LPS (endotoxin)",
        "Hospital-acquired infections: nosocomial pneumonia (VAP), UTI (catheter-associated), burn wound infections, bacteremia (immunocompromised). CF lungs (chronic mucoid infection — leading cause of CF mortality). Ecthyma gangrenosum (skin necrosis — blackened ulcers — in bacteremia). Malignant otitis externa (diabetics). Hot tub folliculitis",
        "Antipseudomonal β-lactams (pip-tazo, cefepime, meropenem/imipenem) ± aminoglycoside (tobramycin/gentamicin) for synergy. Ciprofloxacin (most potent oral agent). Inhaled tobramycin/aztreonam for CF. Colistin: last resort MDR Pseudomonas",
        "Intrinsic resistance: ampicillin, cephalosporins 1st–3rd gen (except ceftazidime; cefepime is 4th-gen), TMP-SMX. Acquired resistance: AmpC β-lactamase, efflux pumps, porin loss. CF: mucoid alginate strains → near-impossible to eradicate → suppress with inhaled antibiotics."
    ),
    "klebsiella": _mo(
        "Gram− rod; lactose-fermenter (pink on MacConkey); oxidase−; very mucoid colonies (string test +); polysaccharide capsule",
        "Polysaccharide capsule (anti-phagocytic), fimbriae, siderophores (iron acquisition), hypermucoviscous phenotype (hypervirulent K. pneumoniae — liver abscess)",
        "Pneumonia (alcoholics/diabetics — 'currant jelly' sputum — necrotizing lobar pneumonia), UTI (hospital-acquired — 2nd most common after E. coli), bacteremia, liver abscess (hypervirulent K. pneumoniae — K1/K2 — SE Asia), neonatal sepsis, meningitis. ESBL and KPC (carbapenem-resistant) strains major concern",
        "Sensitive: cephalosporins, fluoroquinolones, TMP-SMX. ESBL-producing: carbapenems (imipenem/meropenem). KPC (carbapenem-resistant): colistin, ceftazidime-avibactam, meropenem-vaborbactam, cefiderocol",
        "Currant jelly sputum: hemorrhagic mucoid sputum from necrotic lung tissue (Klebsiella pneumonia — bulging fissure sign on CXR). ESBL = extended-spectrum β-lactamase → resistance to penicillins, cephalosporins (including 3rd/4th-gen) and aztreonam → treat with carbapenem. KPC = Klebsiella pneumoniae carbapenemase → carbapenem resistance."
    ),
    "h influenzae": _mo(
        "Gram− coccobacillus (pleomorphic); encapsulated (type b — most virulent) or unencapsulated (NTHi — nontypeable); requires X (hemin) and V (NAD) factors (chocolate agar)",
        "Polysaccharide capsule (type b — PRP — polyribosylribitol phosphate), IgA protease, endotoxin (LOS)",
        "Before vaccine: Hib meningitis (children <5 — most common bacterial meningitis in pre-vaccine era), epiglottitis (thumbprint sign, drooling, tripod position). Post-vaccine era: NTHi causes otitis media, sinusitis, COPD exacerbations, conjunctivitis, bacteremia",
        "Ceftriaxone (meningitis/severe). Amoxicillin-clavulanate (otitis media/sinusitis — NTHi). Azithromycin (exacerbations). Prophylaxis after Hib exposure: rifampin × 4 days",
        "Hib vaccine (conjugated PRP-OMPC/PRP-T): transformed Hib meningitis from most common to rare. Epiglottitis (now mostly adults): 'thumb sign' on lateral neck X-ray; cherry-red swollen epiglottis on laryngoscopy — do NOT examine oropharynx without intubation team present."
    ),
    "listeria": _mo(
        "Gram+ rod; facultative intracellular; motile at room temperature (tumbling motility); grows at 4°C (cold enrichment); β-hemolytic; CAMP test positive (block-shaped enhancement with S. aureus — like Group B Strep)",
        "Actin-based motility (ActA — spreads cell-to-cell without leaving cells — avoids antibodies); listeriolysin O (LLO — pore-forming toxin — allows escape from phagosome)",
        "Meningitis/bacteremia in immunocompromised (HIV, transplant, steroids), elderly, pregnant women (bacteremia — ↑risk of preterm labor, stillbirth, neonatal sepsis/meningitis), neonates. Food-borne illness (ready-to-eat meats, soft cheeses, raw milk, deli foods — grow in refrigerator)",
        "Ampicillin (± gentamicin for synergy in meningitis). TMP-SMX (penicillin allergy). NOT cephalosporins (intrinsically resistant — add ampicillin to empiric meningitis regimen if >50yo/immunocompromised/pregnant)",
        "Empiric meningitis coverage: vancomycin + ceftriaxone = covers S. pneumoniae + N. meningitidis. Add AMPICILLIN if >50yo, immunocompromised, or pregnant (to cover Listeria — resistant to cephalosporins). Listeriolysin O allows escape from phagolysosome → survives inside macrophages."
    ),
    "c difficile": _mo(
        "Gram+ rod; anaerobe; spore-forming; cannot be killed by alcohol (spores — use soap/water or bleach). Toxin A (enterotoxin) + Toxin B (cytotoxin — more important for pathogenesis)",
        "Spores (environmental persistence — hospital surfaces), toxin A (↑fluid secretion, mucosal damage), toxin B (actin depolymerization → colonic cell death), CDT (binary toxin — hypervirulent NAP1/ribotype 027 strain)",
        "C. difficile infection (CDI): antibiotic-associated colitis/diarrhea (watery, ≥3 stools/24h + C. diff toxin in stool), pseudomembranous colitis (yellow plaques on colonoscopy — 'pseudomembranes'), fulminant colitis (toxic megacolon — surgery), recurrent CDI (10–35% after first episode)",
        "Initial episode (IDSA 2021): fidaxomicin 200 mg BID × 10 days (preferred) or oral vancomycin 125 mg QID × 10 days; metronidazole only if neither is available. Fulminant: oral (± rectal) vancomycin 500 mg QID + IV metronidazole. Recurrent: fidaxomicin (standard or extended-pulse) or vancomycin taper → fecal microbiota transplant (FMT). Contact precautions + soap/water handwashing (alcohol ineffective against spores)",
        "Hypervirulent strain (NAP1/BI/027): ↑toxin A+B production + CDT binary toxin + fluoroquinolone resistance → more severe disease. FMT: >90% effective for recurrent CDI. Risk factors: antibiotics (clindamycin, fluoroquinolones, cephalosporins most common), PPIs, hospitalization, advanced age, immunocompromise."
    ),
    "m tuberculosis": _mo(
        "Acid-fast bacillus (AFB); non-Gram staining; obligate aerobe; slow-growing (doubling time 15–20h); waxy mycolic acid cell wall → Ziehl-Neelsen stain (red) or auramine-rhodamine fluorescent stain",
        "Cord factor (trehalose dimycolate — inhibits PMN migration, induces granuloma), sulfatides (inhibit phagosome-lysosome fusion), LAM (lipoarabinomannan — inhibits macrophage activation), wax D (adjuvant for granuloma formation)",
        "Primary TB: usually asymptomatic (Ghon focus — subpleural, usually mid/lower lung zones; with the hilar node = Ghon complex). Reactivation TB: upper lobe cavitary disease, night sweats, weight loss, hemoptysis. Miliary TB (disseminated): millet seed opacities on CXR — immunocompromised. Extrapulmonary: Pott disease (vertebral osteomyelitis), TB meningitis, pleural effusion (lymphocytic, low glucose, high ADA), scrofula (cervical lymphadenopathy)",
        "Active TB (RIPE × 6 months): Rifampin + Isoniazid + Pyrazinamide + Ethambutol (2 months intensive) → Rifampin + Isoniazid (4 months continuation). Latent TB (CDC 2020): rifamycin-based regimens preferred — isoniazid + rifapentine weekly × 3 months (3HP), rifampin daily × 4 months (4R) or isoniazid + rifampin daily × 3 months (3HR); isoniazid alone for 6–9 months is an alternative. Screen all immigrants, HIV patients, healthcare workers with TST (PPD) or IGRA",
        "INH side effects: peripheral neuropathy (give B6/pyridoxine prophylaxis), hepatotoxicity, drug-induced lupus, sideroblastic anemia, CYP inhibition. EMB: optic neuritis (monthly visual acuity). PZA: hyperuricemia, hepatotoxicity. Screen for TB before all biologic therapy (anti-TNF)."
    ),
    "hiv": _mo(
        "RNA retrovirus (lentivirus); enveloped; ssRNA; reverse transcriptase (RNA→DNA). CD4 T-lymphocyte receptor + CCR5/CXCR4 co-receptor",
        "gp120/gp41 (CCR5/CXCR4 binding + fusion), reverse transcriptase (error-prone → rapid mutation → drug resistance), protease (viral maturation), integrase (DNA integration), Tat (transcription activation), Vif (degrades APOBEC3G)",
        "Acute HIV (2–4 weeks post-exposure): mono-like illness (fever, lymphadenopathy, pharyngitis, rash, headache). Asymptomatic (years). AIDS (CD4 <200 or AIDS-defining illness). Opportunistic infections by CD4 count: <500 (bacterial pneumonia, TB, HSV/VZV); <200 (PCP, toxoplasma, cryptococcus); <100 (MAC, CMV, CNS lymphoma)",
        "Initiate ART immediately (treat-all strategy — START trial). Preferred regimens: integrase inhibitor + 2 NRTIs (dolutegravir + TDF/FTC; bictegravir/TAF/FTC). Goal: viral load undetectable (<20–50 copies/mL) → ↓transmission (U=U: undetectable = untransmittable). PrEP: TDF/FTC or cabotegravir LAI",
        "CD4 <200: start PCP prophylaxis (TMP-SMX). CD4 <100: start toxoplasma prophylaxis (TMP-SMX DS covers both). CD4 <50: MAC prophylaxis (azithromycin weekly) only if ART is not started promptly (DHHS). Immune reconstitution inflammatory syndrome (IRIS): paradoxical worsening after ART initiation as immune system reconstitutes → treat underlying infection, continue ART."
    ),
    "hbv": _mo(
        "Partially dsDNA virus (hepadnavirus); enveloped; replicates via RNA intermediate (reverse transcriptase); 8 genotypes (A–H)",
        "HBsAg (surface antigen — first to appear), HBcAg (core — not detected in serum), HBeAg (e antigen — ↑replication), HBV DNA, HBx (transcription activator — promotes HCC), pre-core mutant (HBeAg-negative chronic HBV)",
        "Acute hepatitis B (jaundice, N/V, RUQ pain, malaise) → >95% of adults clear (<5% chronic) vs ~90% of infected neonates become chronic. Chronic HBV: cirrhosis + HCC risk (HBV integrates into genome). Serum sickness-like illness (prodrome: urticaria, arthralgias). Fulminant hepatitis (<1%)",
        "Acute: supportive (most clear spontaneously). Chronic with active replication: tenofovir (TDF or TAF, preferred) or entecavir (suppress HBV DNA). Treat if HBV DNA high + ↑ALT or cirrhosis or HCC risk. HBV vaccine (recombinant HBsAg): 3 doses (0,1,6 months) — 95% effective. HBIG for post-exposure prophylaxis",
        "Serology timeline: HBsAg (first to appear, persists in chronic) → anti-HBc IgM (acute infection marker) → HBeAg (↑replication, high infectivity) → window period (no HBsAg, no anti-HBs) → anti-HBs (immunity — recovery or vaccine). 'Dane particle' = complete infectious virion. HCC surveillance: US + AFP every 6 months in cirrhosis."
    ),
    "hcv": _mo(
        "ssRNA flavivirus; enveloped; 6 major genotypes (1–6); genotype 1 most common in US; high mutation rate (quasispecies)",
        "NS3/4A protease (cleaves viral polyprotein + interferes with innate immunity), NS5B RNA-dependent RNA polymerase (target of sofosbuvir), hypervariable region 1 (immune evasion — rapidly mutates)",
        "Acute HCV (usually asymptomatic — 75–85% become chronic); Chronic HCV: cirrhosis (20–30% after 20–30 years) + HCC (3–5%/year in cirrhosis). Cryoglobulinemia (type II — mixed) → vasculitis (palpable purpura, arthralgias, peripheral neuropathy, glomerulonephritis). Lichen planus, porphyria cutanea tarda",
        "Direct-acting antivirals (DAAs): pangenotypic regimens — sofosbuvir/velpatasvir × 12 weeks (most HCV) or glecaprevir/pibrentasvir × 8 weeks (non-cirrhotic). Cure rates >95%. No HCV vaccine. Screen all adults age 18–79 (USPSTF 2020), HIV+, PWID, needle-stick exposure",
        "HCV is the most common bloodborne pathogen in the US. Transmission: percutaneous (IVDU — 60%), sexual (low risk), vertical (perinatal). Cryoglobulinemia: HCV = most common cause of type II mixed cryoglobulinemia → treat with DAAs + sometimes rituximab for severe vasculitis."
    ),
    "hsv": _mo(
        "dsDNA herpesvirus (Herpesviridae); enveloped; HSV-1 (oral/facial) and HSV-2 (genital — most); both can cause either site. Establish lifelong latency in sensory ganglia (trigeminal → HSV-1; sacral → HSV-2)",
        "Glycoproteins (gB, gC, gD, gH/gL — envelope fusion, immune evasion), thymidine kinase (required for acyclovir activation — TK mutation → acyclovir resistance), ICP34.5 (neurovirulence — evades PKR antiviral response)",
        "Orolabial HSV-1: 'cold sores'/fever blisters (recur at same site triggered by UV, stress, fever). Genital HSV-2/1: painful vesicles → ulcers. Primary genital HSV: systemic sx (fever, myalgias, bilateral inguinal adenopathy). Neonatal HSV: from primary maternal genital HSV during delivery → encephalitis/disseminated disease. HSV encephalitis: temporal lobe (bizarre behavior, seizures, ↑CSF protein, ↑RBC — treat with acyclovir 10 mg/kg IV q8h × 14–21d)",
        "Acyclovir (nucleoside analogue — TK-dependent activation): primary genital HSV (400mg TID × 7–10d) or valacyclovir (1g BID × 7–10d). Suppressive therapy: acyclovir 400mg BID or valacyclovir 500mg QD (↓recurrences + asymptomatic shedding). Neonatal HSV/encephalitis: IV acyclovir (high dose). Acyclovir resistance (TK mutation): foscarnet",
        "Tzanck smear: multinucleated giant cells (not specific — also VZV). PCR of lesion swab: gold standard for diagnosis. HSV encephalitis: CSF PCR (HSV DNA) + MRI temporal lobe edema/hemorrhage. Acyclovir mechanism: requires viral TK for phosphorylation → selective for infected cells → low toxicity profile."
    ),
    "cmv": _mo(
        "dsDNA herpesvirus (β-herpesvirus); largest human herpesvirus; enveloped; latency in monocytes/myeloid progenitors; 'owl eye' intranuclear inclusions on biopsy",
        "US proteins (US2, US3, US6, US11 — downregulate MHC I → evade CTL), UL97 kinase (phosphorylates ganciclovir to active form), glycoproteins (complement evasion), pp65 (immunodominant tegument protein — CMV antigenemia test)",
        "Immunocompetent: CMV mononucleosis (heterophile Ab-negative mono — fever, atypical lymphocytes, hepatitis, ↑LFTs; unlike EBV: pharyngitis + splenomegaly less prominent). Immunocompromised (transplant/AIDS CD4 <50): CMV retinitis (pizza-pie fundus — hemorrhage + exudates), CMV pneumonitis, CMV colitis (bloody diarrhea, linear ulcers on colonoscopy), CMV esophagitis (large linear ulcers — vs HSV multiple small ulcers), CMV encephalitis",
        "Ganciclovir IV (transplant/CMV disease) or valganciclovir oral (bioavailability ~60%). Prophylaxis in transplant: valganciclovir × 3–6 months (letermovir in HSCT and kidney transplant). CMV retinitis: intravitreal ganciclovir/foscarnet injections (implant discontinued) + oral valganciclovir. Foscarnet (ganciclovir resistance — UL97 mutation). Cidofovir (salvage)",
        "CMV seroprevalence: 50–80% of adults (latent infection). CMV disease only in immunocompromised (solid organ transplant — highest risk donor+/recipient−, HSCT, HIV CD4 <50). Owl eye inclusions: large basophilic intranuclear inclusion surrounded by clear halo + small cytoplasmic inclusions. Monitor with CMV viral load (qPCR) or pp65 antigenemia."
    ),
    "candida": _mo(
        "Yeast (oval budding yeast in tissue/blood; pseudohyphae + hyphae = Candida albicans distinguishing feature — germ tube test + at 37°C). Dimorphic behavior. C. albicans most common species",
        "Adhesins (Als proteins — epithelial adhesion), hyphal switching (tissue invasion — hyphae more invasive than yeast), biofilm formation (catheter colonization → difficult to eradicate), secreted aspartyl proteases (tissue degradation)",
        "Mucocutaneous: oral thrush (white plaques that scrape off — 'cottage cheese' — unlike leukoplakia which doesn't scrape), esophageal candidiasis (AIDS-defining, dysphagia/odynophagia), vulvovaginal candidiasis (cottage cheese discharge, pH normal ≤4.5, pseudohyphae on KOH), diaper rash, onychomycosis. Invasive: candidemia (mortality ~40%), endophthalmitis, hepatosplenic candidiasis (leukemia recovery — multiple hepatic abscesses), chronic mucocutaneous candidiasis",
        "Mucocutaneous: fluconazole (azole — 1st line) or topical nystatin/clotrimazole. Invasive/candidemia: echinocandin (caspofungin/micafungin — 1st line) or fluconazole (if stable, susceptible). Remove all central lines in candidemia. Treat ≥14 days after first negative blood culture. Ophthalmic exam mandatory in candidemia (endophthalmitis)",
        "C. glabrata + C. krusei: intrinsically resistant to fluconazole → use echinocandin. C. auris: emerging, multidrug-resistant, nosocomial. Germ tube test: C. albicans + C. dubliniensis only produce germ tubes at 37°C (within 3h). Remove central venous catheter in candidemia — source of persistent infection."
    ),
    "aspergillus": _mo(
        "Filamentous mold (hyaline hyphae that branch at 45° angles — septate); NOT dimorphic. A. fumigatus most common pathogenic species. Ubiquitous in environment (soil, compost, HVAC systems)",
        "Galactomannan (cell wall polysaccharide — diagnostic antigen for serum/BAL testing), gliotoxin (↓phagocyte function), angioinvasion (vascular invasion — hemorrhagic infarcts), β-glucan (cell wall)",
        "Invasive aspergillosis (IA): neutropenic patients (AML, HSCT) + steroids + CGD. Halo sign on CT (early — ground-glass around nodule), Air crescent sign (late — neutrophil recovery). Allergic bronchopulmonary aspergillosis (ABPA): asthma + CF + eosinophilia + central bronchiectasis + ↑IgE + skin test positive. Aspergilloma (fungus ball in old TB/sarcoid cavity — hemoptysis). CPA (chronic pulmonary aspergillosis)",
        "Invasive: voriconazole (first-line — IDSA guideline). Isavuconazole or posaconazole (alternatives). Amphotericin B (salvage or vori failure). Surgical resection (hemoptysis from aspergilloma). ABPA: steroids + itraconazole. Prophylaxis in neutropenic/HSCT: posaconazole",
        "Galactomannan assay: serum (HSCT/hematological malignancy) or BAL (any patient). Sensitivity ↓ with antifungal prophylaxis. β-D-glucan: positive in Candida + Aspergillus + PCP (not Mucor — no glucan). Mucorales (Mucor/Rhizopus): ribbon-like, NON-septate hyphae branching at 90° — diabetes + DKA predispose. Treat with amphotericin B + surgery."
    ),
    "cryptococcus": _mo(
        "Encapsulated yeast; NOT dimorphic; large polysaccharide capsule (visualized with India ink — negative staining, 'halo' around yeast); urease+; melanin production (from catecholamines); C. neoformans (AIDS) and C. gattii (immunocompetent)",
        "Polysaccharide capsule (anti-phagocytic — complement evasion, ↓IL-12 → ↓T-cell activation), melanin (radical scavenger — antioxidant), urease, phospholipase",
        "Cryptococcal meningitis (CD4 <100 — most common in AIDS; insidious onset — weeks of HA, fever, ↓mental status; minimal CSF pleocytosis; ↑↑opening pressure; India ink +; cryptococcal antigen +). Cryptococcoma (mass lesion — 'soap bubble' lesions in basal ganglia on MRI). Pneumonia (often asymptomatic in immunocompetent)",
        "Induction: amphotericin B + flucytosine (5-FC) × 2 weeks (WHO 2022: single high-dose liposomal AmB + 14 days 5-FC + fluconazole) (most important phase — combination kills fungi synergistically). Consolidation: fluconazole 400mg/day × 8 weeks. Maintenance (suppressive): fluconazole 200mg/day (≥1 year, until CD4 ≥100 with suppressed viral load ≥3 months). Serial LPs (therapeutic): relieve ↑↑ICP (↓mortality); acetazolamide NOT useful for ICP in crypto",
        "Cryptococcal antigen (CrAg) serum lateral flow assay: extremely sensitive and specific — screen all HIV patients with CD4 <100 (pre-emptive fluconazole if CrAg+ without meningitis reduces mortality). Flucytosine: inhibits DNA/RNA synthesis — myelosuppression (monitor CBC). Never use fluconazole alone for induction (↑relapse)."
    ),
    "pneumocystis": _mo(
        "Atypical fungus (classified as fungus by rRNA; behaves like protozoan). Pneumocystis jirovecii (humans; NOT zoonotic — P. carinii = rats). NOT culturable in vitro; cysts (4–8 nuclei) + trophic forms",
        "β-glucan (cell wall — detectable in serum and BAL), dihydropteroate synthase (target of TMP-SMX), Msg (major surface glycoprotein — adhesion to alveolar epithelium, antigen variation → immune evasion)",
        "PCP (Pneumocystis jirovecii pneumonia): AIDS (CD4 <200 — most common AIDS-defining OI in US), transplant recipients, steroids, biologics, MTX. Dx: bilateral interstitial ('ground-glass') infiltrates + ↑LDH + subacute dyspnea + dry cough + hypoxia + BAL/sputum with GMS stain (silver stain shows cysts) or DFA",
        "TMP-SMX (first-line — 15–20 mg/kg/day TMP component × 21 days). Alternatives: pentamidine IV (toxicity: nephrotoxicity, hypoglycemia, QT prolongation), atovaquone, dapsone + TMP (mild-moderate). Adjunct prednisone (if PaO2 <70 or A-a gradient >35 → steroids ↓mortality). Prophylaxis: TMP-SMX DS QD (CD4 <200, post-transplant)",
        "GMS (Gomori methenamine silver) stain: 'gold standard' — cyst wall stains black, cysts have central dot. Giemsa: trophic forms (not cysts). β-D-glucan: ↑↑ in PCP (very high levels, >400 pg/mL). LDH: elevated in PCP (non-specific but sensitive). Room air A-a gradient: important for prognosis and steroid decision."
    ),
    "plasmodium": _mo(
        "Intracellular protozoan parasite; 5 species infecting humans: P. falciparum (most deadly), P. vivax (most common worldwide), P. ovale, P. malariae, P. knowlesi. Vector: female Anopheles mosquito",
        "Merozoite surface protein (RBC invasion), PfEMP1 (cytoadherence — sequestration in P. falciparum — binds endothelial receptors → organ damage), knobs (RBC membrane deformation), thickened RBC membrane (↓deformability), rosetting (RBC clumping)",
        "Malaria: cyclical fever (tertian every 48h — P. falciparum/vivax/ovale; quartan every 72h — P. malariae), chills, headache, myalgias, splenomegaly. Severe P. falciparum: cerebral malaria (seizures, coma), severe anemia (hemolysis), ARDS, AKI, hypoglycemia, hyperlactatemia, hyperparasitemia (>5%). P. vivax/ovale: hypnozoite dormant liver stage → relapse (months–years later)",
        "Uncomplicated P. falciparum (non-endemic areas): artemether-lumefantrine (Coartem) or atovaquone-proguanil (Malarone). Severe P. falciparum: IV artesunate (first-line — WHO) (IV artesunate is now FDA-approved; IV quinidine is no longer available in the US). P. vivax/ovale: chloroquine (if chloroquine-sensitive) + primaquine (eradicate hypnozoites — check G6PD first). Prophylaxis: atovaquone-proguanil, doxycycline, or mefloquine (depending on region resistance)",
        "P. falciparum: no hypnozoite (no relapse), multiple ring forms per RBC (distinctive), banana-shaped gametocytes, Maurer's clefts. P. vivax/ovale: enlarged RBC, Schüffner dots, hypnozoites (→ relapse → treat with primaquine after ruling out G6PD deficiency — hemolytic anemia). Sickle cell trait (HbAS): protective against P. falciparum malaria (RBC sickling prevents parasite growth). Duffy antigen absence (West Africans): protective against P. vivax."
    ),
    # ── Gram-positive cocci (additional) ─────────────────────────────────
    "strep agalactiae": _mo(
        "Gram+ cocci in chains; beta-hemolytic; Group B Strep (GBS); catalase−; CAMP test positive; hippurate hydrolysis positive; bacitracin-resistant",
        "Polysaccharide capsule (9 serotypes — Ia, Ib, II–VIII; Ia most common neonatal; III most common neonatal meningitis), CAMP factor (enhances staphylococcal beta-hemolysin → arrowhead hemolysis), sialic acid (immune evasion)",
        "Neonates: early-onset (birth–7 days — pneumonia, sepsis, meningitis from vaginal colonization); late-onset (7–90 days — bacteremia, meningitis — serotype III). Adults: bacteremia in elderly/immunocompromised, UTI in pregnant women, postpartum endometritis, wound infections",
        "Neonatal: ampicillin + gentamicin (synergy). Adults: penicillin G or ampicillin (always susceptible). Intrapartum prophylaxis for GBS-positive mothers: IV PCN G or ampicillin. PCN allergy: cefazolin (low-risk allergy), clindamycin (if susceptible) or vancomycin",
        "GBS universal screening at 36 0/7–37 6/7 weeks (ACOG 2020). CAMP test: GBS produces CAMP factor that synergizes with S. aureus beta-hemolysin → arrowhead-shaped enhanced hemolysis. Most common cause of neonatal sepsis and meningitis in developed countries."
    ),
    "group b strep": _mo(
        "Gram+ cocci in chains; beta-hemolytic; Lancefield Group B; catalase−; CAMP test positive",
        "Polysaccharide capsule, CAMP factor, sialic acid capsule (molecular mimicry — immune evasion)",
        "Neonatal sepsis/meningitis (most common cause 0–3 months), maternal chorioamnionitis, UTI in pregnancy, postpartum endometritis, invasive disease in elderly/diabetics",
        "Penicillin G first-line (always susceptible). Intrapartum prophylaxis: IV PCN or ampicillin. PCN allergy: cefazolin (low-risk allergy), clindamycin or vancomycin",
        "Most common cause of neonatal meningitis in developed countries. Screen all pregnant women at 36–37 weeks. Early-onset (<7 days) vs. late-onset (7–90 days) — distinct epidemiology."
    ),
    "s epidermidis": _mo(
        "Gram+ cocci in clusters; coagulase-NEGATIVE Staph (CoNS); catalase+; novobiocin-SENSITIVE (vs S. saprophyticus — novobiocin-resistant)",
        "Biofilm formation on prosthetic devices (slime/polysaccharide intercellular adhesin — PIA), immune evasion, intrinsic multidrug resistance",
        "Prosthetic device infections: PVE (early <60 days — most common CoNS), prosthetic joint infections, CSF shunt infections, CLABSI. Skin commensal — pathogen only with foreign body or immunocompromised",
        "Vancomycin (drug of choice for invasive). Rifampin added for biofilm penetration in prosthetic valve endocarditis. Device removal often required for cure",
        "Most common cause of healthcare-associated bacteremia (CLABSI). Biofilm prevents antibiotic killing and immune clearance. CoNS in blood culture: common contaminant — multiple positive bottles or device present = true pathogen."
    ),
    "enterococcus": _mo(
        "Gram+ cocci in pairs/chains; alpha or gamma (non)-hemolytic; catalase−; PYR+; bile-esculin+; grows in 6.5% NaCl; Group D. E. faecalis (80–90%, more susceptible) and E. faecium (more resistant, most VRE)",
        "Intrinsic resistance: cephalosporins, clindamycin, TMP-SMX (bacteriostasis only with beta-lactams). VRE: vanA gene (high-level resistance to vancomycin + teicoplanin). Virulence: cytolysin, aggregation substance",
        "UTI (2nd most common hospital-acquired UTI), bacteremia (line infections), endocarditis (subacute — aortic/mitral valve), biliary/intraabdominal infections (polymicrobial). VRE colonization/infection in ICU patients",
        "E. faecalis: ampicillin preferred. Endocarditis: ampicillin + gentamicin (synergy if no HLAR) or ampicillin + ceftriaxone (avoid aminoglycoside nephrotoxicity — ABCE trial). VRE: linezolid or daptomycin (high dose 8–12 mg/kg). VRE UTI: nitrofurantoin or fosfomycin",
        "Intrinsically resistant to cephalosporins (only bacteriostasis with penicillins alone — need aminoglycoside synergy for bactericidal killing in endocarditis). HLAR (high-level aminoglycoside resistance — MIC >2000): no synergy possible → use ampicillin + ceftriaxone double beta-lactam strategy."
    ),
    # ── Gram-positive rods ────────────────────────────────────────────────
    "c diphtheriae": _mo(
        "Gram+ rod; club-shaped (Chinese letter/palisade arrangement); non-motile; aerobe; Loeffler's serum medium + tellurite agar (black colonies); Elek test for toxin production",
        "Diphtheria toxin (phage-encoded — corynephage beta): ADP-ribosylation of EF-2 (elongation factor 2) → inhibits protein synthesis (same mechanism as Pseudomonas exotoxin A). Fragment B: cell entry. Fragment A: enzymatic toxin",
        "Respiratory diphtheria: pharyngitis + TOUGH gray pseudomembrane (bleeds on removal), adherent to posterior pharynx/tonsils, bull neck (massive cervical lymphadenopathy). Toxin spread: myocarditis (AV block, cardiomyopathy — 1–2 weeks), cranial nerve palsies (CN X palatal palsy), cutaneous diphtheria",
        "Diphtheria antitoxin IMMEDIATELY (neutralizes unbound toxin — give without waiting for culture). Antibiotics: erythromycin or PCN G × 14 days (eliminate organism). Airway management. Prevention: DTaP/Tdap vaccine (toxoid — immunizes against toxin)",
        "Non-toxigenic C. diphtheriae: no serious disease. Metachromatic granules (Babes-Ernst) on methylene blue stain. Tellurite reduces to telluride → black colonies. ADP-ribosylation of EF-2: same mechanism as P. aeruginosa exotoxin A. Schick test (historical): intradermal toxin → local inflammation means no antitoxin immunity."
    ),
    "c perfringens": _mo(
        "Gram+ rod; anaerobe; spore-forming; BOXCAR-shaped; double zone of hemolysis on blood agar; non-motile; lecithinase positive (Nagler reaction — egg yolk agar opacity)",
        "Alpha-toxin (lecithinase/phospholipase C — most important — destroys cell membranes), perfringolysin (theta-toxin, oxygen-labile hemolysin), enterotoxin (heat-labile — food poisoning, forms pores in colonocyte membranes)",
        "Gas gangrene (clostridial myonecrosis): rapidly spreading crepitant necrosis after trauma/surgery, severe pain out of proportion, bronze discoloration, crepitus, no fever initially. Food poisoning: spores germinate → heat-labile enterotoxin in GI → watery diarrhea + cramping (no vomiting) 8–24h after reheated meat/stew",
        "Gas gangrene: EMERGENT surgical debridement (wide excision/amputation) + IV PCN G + clindamycin (inhibits toxin production). Hyperbaric oxygen (adjunct). Food poisoning: supportive care only (self-limited 24h)",
        "CREPITUS (gas in tissue = CO2 from anaerobic metabolism) is hallmark of gas gangrene — X-ray/CT shows gas tracking. Do NOT wait for culture — clinical diagnosis + emergent surgery. Food poisoning: spores survive cooking → germinate on cooling → toxin produced in GI (different from S. aureus preformed toxin: S. aureus onset 1–6h + vomiting; C. perfringens onset 8–24h + diarrhea only)."
    ),
    "c botulinum": _mo(
        "Gram+ rod; anaerobe; spore-forming; 7 toxin types (A–G; A, B, E most common in humans). Spores heat-resistant (survive 100°C); toxin heat-labile (destroyed at 85°C for 5 min)",
        "Botulinum toxin (most potent biological toxin): cleaves SNARE proteins (synaptobrevin/SNAP-25/syntaxin) → prevents ACh vesicle fusion at NMJ → FLACCID paralysis (presynaptic, DESCENDING — opposite of tetanus which is spastic and ascending)",
        "Foodborne: preformed toxin in improperly canned food → descending flaccid paralysis (diplopia, dysarthria, dysphagia first → respiratory failure), no fever, normal mental status. Wound (IV drug users). Infant: spores in honey → floppy baby + constipation + weak cry + poor suck (do NOT give honey <12 months). Iatrogenic: botox",
        "Antitoxin (heptavalent HBAT — give ASAP, neutralizes unbound toxin). Supportive: mechanical ventilation. Infant botulism: human-derived BIG-IV (Baby BIG). Wound: debridement + PCN G. Food-borne: NO antibiotics (may ↑toxin release)",
        "Descending paralysis + 4 D's: Diplopia, Dysarthria, Dysphagia, Descending weakness. Symmetric, afebrile, with autonomic dysfunction (dry mouth, constipation, mydriasis, urinary retention). Distinguish from GBS (ascending, sensory, CSF protein ↑) and MG (fatigable, anti-AChR antibodies). Honey: spores cause infant botulism — NOT preformed toxin."
    ),
    "c tetani": _mo(
        "Gram+ rod; anaerobe; spore-forming; drumstick/tennis racket appearance (terminal spore); motile; ubiquitous in soil",
        "Tetanospasmin (tetanus toxin): retrograde axonal transport → cleaves synaptobrevin (VAMP) in inhibitory interneurons → BLOCKS GLYCINE + GABA → DISINHIBITION → SPASTIC paralysis (opposite of botulinum which is flaccid). Tetanolysin: cytotoxin",
        "Tetanus: trismus (lockjaw — masseter spasm, first symptom), risus sardonicus (spastic smile), opisthotonus (arched-back posturing — back muscle spasms), dysphagia, autonomic instability (labile HTN/hypotension, tachycardia/bradycardia). Neonatal tetanus: umbilical stump in unvaccinated mothers",
        "Wound debridement + Human Tetanus Immune Globulin (HTIG) 500 U IM (neutralizes unbound toxin) + metronidazole × 10–14 days + benzodiazepines (diazepam — muscle relaxation) + autonomic control (labetalol + magnesium sulfate) + ICU/ventilation + tetanus toxoid (opposite arm from HTIG)",
        "Tetanospasmin blocks inhibitory interneurons (glycinergic + GABAergic in spinal cord/brainstem) → spastic paralysis + autonomic storm. Botulinum blocks excitatory cholinergic NMJ → flaccid paralysis. Spores enter wounds (puncture, burns, IV drug use, umbilicus). Prophylaxis: Td/Tdap booster every 10 years; dirty wound → booster if last dose ≥5 years ago; add HTIG only if <3 lifetime doses or unknown history."
    ),
    # ── Gram-negative rods (additional) ──────────────────────────────────
    "salmonella": _mo(
        "Gram− rod; facultative anaerobe; motile (peritrichous flagella); non-lactose fermenter; H2S+; oxidase−. Typhoidal: S. typhi, S. paratyphi. Non-typhoidal (NTS): >2500 serotypes (S. typhimurium, S. enteritidis)",
        "Type III secretion system (invasion), Vi antigen capsule (S. typhi — anti-phagocytic), Salmonella pathogenicity islands (SPI-1/SPI-2 — intestinal invasion + intracellular survival)",
        "Typhoid fever (S. typhi): rose spots (salmon-colored blanching macules on trunk, day 7–10), relative bradycardia (Faget sign), stepwise fever, splenomegaly. NTS gastroenteritis: watery/bloody diarrhea 1–3 days after poultry/eggs/reptile exposure. Bacteremia in sickle cell/HIV. Osteomyelitis in sickle cell disease (most common cause)",
        "Typhoid: fluoroquinolone or azithromycin or ceftriaxone (↑quinolone resistance). NTS gastroenteritis: SUPPORTIVE ONLY — NO antibiotics (prolongs carrier state, no benefit unless bacteremia risk). Bacteremia: ceftriaxone or ciprofloxacin × 14 days",
        "Salmonella osteomyelitis in SCD: sickling → functional asplenia → bacteremia → bone seeding at vaso-occlusion sites. Rose spots in 30% of typhoid — culture skin lesion. Chronic typhoid carrier: gallbladder colonization (gallstones predispose). Reptile contact (turtles, iguanas): reservoir for NTS."
    ),
    "shigella": _mo(
        "Gram− rod; facultative anaerobe; NON-motile; non-lactose fermenter; NO H2S; very low infectious dose (10–200 organisms). Severity: S. dysenteriae (Shiga toxin, most severe) > S. flexneri > S. boydii > S. sonnei (mildest, most common in US)",
        "Type III secretion system (IpaA/B/C/D effectors → M-cell invasion), intracellular actin motility (IcsA — cell-to-cell spread), Shiga toxin (S. dysenteriae type 1 — inhibits ribosome → HUS)",
        "Bacillary dysentery: small-volume bloody diarrhea + mucus + TENESMUS (most distinguishing — painful urgency) + fever + fecal leukocytes. Complications: febrile seizures in children, HUS (S. dysenteriae type 1), reactive arthritis (Reiter — HLA-B27), toxic megacolon",
        "Antibiotics recommended for most cases (shorten illness and shedding — unlike NTS). Azithromycin (first-line). Ciprofloxacin (if susceptible). Avoid antimotility agents (↑complications)",
        "Shigella: person-to-person transmission (fecal-oral, low inoculum — 10–200 organisms). Non-motile, no H2S, human-only host, antibiotics usually given (unlike NTS). Reiter's syndrome after Shigella/Salmonella/Campylobacter/Chlamydia: HLA-B27 + urethritis + uveitis + arthritis."
    ),
    "campylobacter": _mo(
        "Gram− curved/spiral rod (seagull shape); oxidase+; microaerophilic (grows at 42°C, 5% O2, 10% CO2); motile (single polar flagellum — darting motility). C. jejuni most common",
        "Cytolethal distending toxin (CDT — G2/M cell cycle arrest), flagellum (motility + adhesion), outer membrane proteins, LOS (lipooligosaccharide — ganglioside molecular mimicry → GBS)",
        "Most common bacterial gastroenteritis in developed world. Zoonotic: poultry (most common), unpasteurized milk, puppies. Watery → bloody diarrhea + crampy pain + fever. Post-infectious: Guillain-Barré syndrome (most common identifiable antecedent — C. jejuni LOS mimics gangliosides), reactive arthritis, IBS",
        "Self-limited gastroenteritis: supportive. Antibiotics if severe/bloody/immunocompromised/bacteremia → azithromycin (DOC — ↑quinolone resistance from agricultural use). C. fetus bacteremia: ciprofloxacin or ampicillin",
        "GBS: anti-GQ1b/GM1/GD1a antibodies (molecular mimicry with C. jejuni LOS) — 25–40% of GBS cases preceded by Campylobacter. Grows at 42°C (birds' body temperature). Most common trigger of GBS. Urease-negative (unlike H. pylori)."
    ),
    "h pylori": _mo(
        "Gram− spiral rod; microaerophilic; urease+ (generates ammonia → buffers gastric acid → survival); oxidase+; catalase+; motile (multiple polar flagella). Class I carcinogen (WHO)",
        "Urease (acid neutralization), CagA (Type IV secretion → disrupts epithelial signaling, promotes malignancy), VacA (vacuolating cytotoxin, T-cell suppression), BabA (adherence to Lewis b blood group antigen)",
        "Peptic ulcer disease (70% gastric, 90% duodenal ulcers), gastric MALT lymphoma (eradication cures early-stage), gastric adenocarcinoma (6-fold ↑risk with CagA strains → intestinal metaplasia → dysplasia → cancer), functional dyspepsia, iron deficiency anemia",
        "Test-and-treat (uninvestigated dyspepsia, no alarm features). Diagnosis: urea breath test or stool antigen (active infection); endoscopic biopsy (CLO/urease test + histology + culture). Eradication (ACG 2024): bismuth quadruple therapy (PPI + bismuth + metronidazole + tetracycline × 14 days) first-line; rifabutin triple or vonoprazan + amoxicillin dual as alternatives; clarithromycin triple therapy only when the strain is known to be clarithromycin-susceptible. Confirm eradication 4+ weeks after treatment",
        "CagA: injected via Type IV secretion → activates RAS/ERK oncogenic pathways + disrupts cell polarity → carcinogenesis. Gastric MALT lymphoma: H. pylori-specific T-cells drive B-cell proliferation → 75–80% remission with eradication alone (stage I/II). Bismuth quadruple therapy: superior in areas with >15% clarithromycin resistance. NSAID + H. pylori = synergistic ulcer risk."
    ),
    "bacteroides fragilis": _mo(
        "Gram− rod; obligate anaerobe; pleomorphic; encapsulated (polysaccharide capsule — unique among gut anaerobes); bile-resistant; most clinically important colonic anaerobe (a minor fraction of gut Bacteroides)",
        "Polysaccharide complex (PSA — abscess induction, immunomodulation), BFT/fragilysin (metalloprotease — cleaves E-cadherin → disrupts epithelial barrier → diarrhea in ETBF), non-classical LPS (less immunostimulatory than E. coli)",
        "Intraabdominal abscesses (most common anaerobe — post-surgical, appendicitis, diverticulitis, peritonitis), pelvic inflammatory disease, aspiration pneumonia, bacteremia (polymicrobial), diabetic foot infections",
        "Metronidazole (mainstay). Beta-lactam/beta-lactamase inhibitors (pip-tazo, ampicillin-sulbactam, amoxicillin-clavulanate). Carbapenems (severe infections). NOT penicillin alone (beta-lactamase producing). Clindamycin: ↑resistance (~30%) — use with caution",
        "Most clinically important anaerobe despite low relative abundance (other Bacteroides species more numerous but less virulent). Polysaccharide capsule → T-cell-mediated abscess formation. BFT cleaves E-cadherin → ETBF diarrhea. Always cover anaerobes in intraabdominal infections (colon flora)."
    ),
    "vibrio cholerae": _mo(
        "Gram− curved rod (comma-shaped); oxidase+; motile (single polar flagellum); grows in alkaline media (TCBS agar — yellow colonies); non-invasive; O1 (El Tor/Classical — epidemic) and O139 serogroups cause outbreaks",
        "Cholera toxin (CT): ADP-ribosylation of Gs alpha → permanent adenylyl cyclase activation → ↑cAMP → ↑CFTR Cl− secretion → massive secretory diarrhea. TCP pilus (toxin-coregulated pilus — adhesion to small intestine; receptor for CTX phage carrying CT genes)",
        "Cholera: RICE-WATER diarrhea (massive, watery, no blood/pus — 10–20 L/day) + vomiting → severe dehydration → hypovolemic shock + metabolic acidosis + hypokalemia. Muscle cramps. 50% mortality untreated; <1% with adequate rehydration. 7th pandemic ongoing (El Tor biotype O1)",
        "ORAL REHYDRATION SOLUTION (ORS — cornerstone: Na-glucose co-transport intact). Severe: IV Ringer's lactate + ORS. Antibiotics (reduce duration + shedding): doxycycline (adults, single dose — DOC) or azithromycin (children, pregnancy). Zinc supplementation (children)",
        "ORS works because Na+/glucose co-transporter (SGLT1) is unaffected by CT (CT only activates CFTR secretion, does not block absorption). CT mechanism same as E. coli heat-labile toxin (LT) — both ADP-ribosylate Gs → ↑cAMP. V. vulnificus: wound infections in saltwater + septicemia from raw oysters in liver disease patients."
    ),
    "borrelia burgdorferi": _mo(
        "Gram− spirochete (too thin for Gram stain — visualized by silver stain/darkfield); microaerophilic; tick vector: Ixodes scapularis (Northeast/Midwest US). Reservoir: white-footed mouse",
        "Outer surface proteins (OspA — tick vaccine target; OspC — early infection; VlsE — antigenic variation → immune evasion). Lipoprotein VlsE → C6 peptide (ELISA target for serology). No LPS (unusual — uses cholesterol-rich lipoproteins instead)",
        "Lyme disease: Stage 1 (3–30 days): erythema migrans (bull's-eye rash >5 cm, central clearing — present 70–80%, pathognomonic) + flu-like illness. Stage 2 (weeks–months): disseminated — bilateral Bell's palsy (highly suggestive of Lyme in endemic areas), Lyme carditis (AV block — 1st to 3rd degree), meningitis, radiculopathy. Stage 3 (months–years): Lyme arthritis (knee most common — migratory oligoarthritis)",
        "Stage 1: doxycycline 100 mg BID × 10 days (preferred) or amoxicillin × 14 days. Stage 2 neurologic (facial palsy, meningitis, radiculopathy): oral doxycycline 14–21 days is as effective as IV ceftriaxone; carditis: IV ceftriaxone if hospitalized, then oral (14–21 days total). Lyme arthritis: doxycycline/amoxicillin × 28 days; if fails → IV ceftriaxone. Post-exposure prophylaxis: single doxycycline 200 mg within 72h (tick attached >36h, endemic area)",
        "Tick attachment >36h required for transmission. Two-tier serology: ELISA (screening) → Western blot (confirmation — IgM ≥2 of 3 bands, valid only in the first 30 days; IgG ≥5 of 10 bands; modified two-tier testing with two EIAs is now accepted). Empirical Lyme treatment for EM without serology (can be negative early). Post-Lyme disease syndrome: persistent symptoms after treatment — no proven benefit of prolonged antibiotics."
    ),
    "treponema pallidum": _mo(
        "Gram− spirochete (too thin — darkfield microscopy/silver stain); cannot be cultured in vitro; obligate human pathogen; sexual transmission + vertical (congenital). Always penicillin-sensitive (never develops resistance)",
        "Outer membrane proteins (OMPs — antigenically variable), penicillin-binding proteins (always sensitive), T. pallidum survives by antigen shedding and molecular mimicry. Cardiolipin (membrane component → non-treponemal antibody target)",
        "Syphilis: Primary (3 weeks): painless indurated chancre + regional lymphadenopathy. Secondary (6–8 weeks): maculopapular rash on PALMS + SOLES (pathognomonic), condyloma lata, mucous patches, systemic illness, alopecia. Latent: early (<1yr) or late (>1yr). Tertiary: gumma, cardiovascular (aortitis → aneurysm, AR — tree-bark), neurosyphilis (tabes dorsalis — posterior column loss; Argyll Robertson pupil — accommodates but doesn't react to light; general paresis). Congenital: saddle nose, Hutchinson teeth, saber shins, interstitial keratitis",
        "ALL stages: penicillin G (only proven therapy for all stages). Primary/secondary/early latent: benzathine PCN G 2.4M units IM × 1. Late latent/tertiary: benzathine PCN G 2.4M units IM × 3 (weekly). Neurosyphilis: aqueous crystalline PCN G 18–24M units/day IV × 10–14 days. PCN allergy (non-neurosyphilis/non-pregnant): doxycycline 14 days (early) or 28 days (late latent)",
        "Non-treponemal tests (screening, quantitative): RPR/VDRL — titers track treatment response (4-fold drop = adequate treatment). Treponemal tests (confirmatory): FTA-ABS, TPPA — remain positive lifelong. Jarisch-Herxheimer: fever + chills + hypotension within hours of first PCN dose (cytokine storm from spirochete lysis) — treat with antipyretics, do NOT stop PCN. Argyll Robertson pupil: bilateral, irregular, small pupils — accommodate but do not react to light ('prostitute's pupil — accommodates but doesn't react')."
    ),
    "rickettsia": _mo(
        "Gram− obligate intracellular coccobacillus; tick-borne (primarily); arthropod vector required. Spotted fever group (SFG — R. rickettsii: RMSF) vs. typhus group (R. prowazekii: louse-borne epidemic typhus; R. typhi: murine/flea-borne). Cannot survive outside host cells",
        "Obligate intracellular (infects vascular endothelial cells → vasculitis). Actin-based intracellular motility (like Listeria). OmpA/OmpB surface antigens. Endothelial invasion → capillary leak → hemorrhage + organ damage",
        "RMSF (R. rickettsii): fever + headache + PERIPHERAL rash (wrists/ankles/palms/soles → centripetal spread — trunk) appearing day 3–5. Thrombocytopenia, hyponatremia. If no rash: 'spotless fever' — worse prognosis. Epidemic typhus (R. prowazekii): centrifugal rash (trunk → periphery). Scrub typhus (Orientia tsutsugamushi): eschar (pathognomonic) + fever + rash + lymphadenopathy",
        "DOXYCYCLINE EMPIRICALLY — ALL rickettsia, ALL ages including children (benefit outweighs dental staining risk in life-threatening RMSF). Start WITHOUT waiting for confirmatory tests. Duration: 7–14 days (3 days after defervescence). Chloramphenicol only if true doxycycline allergy (inferior, more toxic)",
        "RMSF: most lethal tick-borne disease in US — delay in treatment significantly ↑mortality. Diagnosis: clinical (fever + rash + tick exposure) → empiric doxycycline. IFA serology (gold standard) — acute titers may be negative, requires convalescent. Doxycycline in children with RMSF: AAP and CDC endorse use (short course → minimal dental staining; delayed treatment → death). RMSF rash: peripheral → central (opposite of typhus: central → peripheral)."
    ),
    "chlamydia trachomatis": _mo(
        "Obligate intracellular; NO cell wall (no peptidoglycan → intrinsically resistant to beta-lactams); NOT visible on Gram stain. Biphasic lifecycle: elementary body (EB — infectious, small, enters cells) → reticulate body (RB — replicating inside inclusion → non-infectious). Serovars A–C (trachoma), D–K (STI), L1–L3 (LGV)",
        "MOMP/OmcB adhesins, molecular mimicry (HSP60 → autoimmune damage in PID), inclusions (prevent phagolysosome fusion), sequesters inside inclusion membrane avoiding immune killing",
        "Serovars D–K (most common bacterial STI in US): urethritis (males — often asymptomatic 50%), cervicitis (females — asymptomatic 75%), PID (scarring → infertility + ectopic pregnancy), epididymitis, reactive arthritis (Reiter). Neonatal: conjunctivitis (days 5–14) + afebrile pneumonia (1–3 months, staccato cough, eosinophilia). Trachoma (A–C): leading cause of preventable infectious blindness. LGV (L1–L3): painless ulcer → painful inguinal buboes + proctocolitis in MSM",
        "Doxycycline 100 mg BID × 7 days (preferred). Azithromycin 1g × 1 (alternative or pregnancy). LGV: doxycycline × 21 days. Neonatal: erythromycin PO × 14 days. Screen all sexually active women ≤25 + pregnant women + older women with risk factors",
        "NAAT (urine/swab): gold standard — most sensitive. Cannot synthesize ATP (energy parasite — depends on host cell). HSP60 molecular mimicry → Fallopian tube scarring (repeat infections) → ectopic pregnancy + infertility. Fitz-Hugh-Curtis syndrome (perihepatitis — violin-string adhesions): also from C. trachomatis + N. gonorrhoeae in PID."
    ),
    "mycoplasma pneumoniae": _mo(
        "NO CELL WALL — smallest free-living organism; intrinsically resistant to ALL beta-lactams and vancomycin; NOT visible on Gram stain; EATON AGENT; Eaton's/SP-4 special media; P1 adhesin protein; cold agglutinins (IgM anti-I antigen)",
        "P1 adhesin (attachment to respiratory cilia → ciliostasis), CARDS toxin (ADP-ribosyltransferase — vacuolating activity), hydrogen peroxide (oxidative damage), molecular mimicry (I antigen on RBCs → cold agglutinins)",
        "Walking pneumonia (atypical): gradual onset, dry hacking cough, low-grade fever, headache, malaise — patient ambulatory. Bilateral perihilar infiltrates (CXR worse than clinical appearance). Most common in school-age children + young adults. Extra-pulmonary: cold agglutinin hemolytic anemia, erythema multiforme, Stevens-Johnson syndrome, aseptic meningitis, encephalitis, Guillain-Barré, myocarditis/pericarditis",
        "Macrolides (azithromycin — first-line). Doxycycline (alternative). Fluoroquinolones (levofloxacin/moxifloxacin). NOT penicillin/cephalosporins (no cell wall to target). Most infections self-limited — antibiotics shorten duration",
        "Cold agglutinins: IgM auto-antibodies agglutinate RBCs at cold temperatures (cross-react with I antigen) → hemolytic anemia + Raynaud in severe infections (keep patient warm). CXR worse than clinical picture is hallmark of atypical pneumonia (vs. typical bacterial pneumonia = CXR matches severity). Negative Monospot (unlike EBV). Macrolide resistance ↑ (especially in Asia — use doxycycline or fluoroquinolone)."
    ),
    "bordetella pertussis": _mo(
        "Gram− coccobacillus; strict aerobe; slowly growing; fastidious (Bordet-Gengou agar — charcoal + blood); highly contagious (R0 = 12–17, one of highest of any pathogen); encapsulated; NON-motile",
        "Pertussis toxin (PT — ADP-ribosylates Gi alpha → ↑cAMP → lymphocytosis + ↑insulin secretion + histamine sensitization + ↑adherence), filamentous hemagglutinin (FHA — adhesin), pertactin, tracheal cytotoxin (mucociliary paralysis), adenylate cyclase toxin (enters phagocytes → ↑cAMP → ↓killing)",
        "Whooping cough: Catarrhal (1–2 weeks: URI symptoms, most infectious). Paroxysmal (2–6 weeks: severe paroxysmal coughing + inspiratory WHOOP + post-tussive vomiting + cyanosis; infants → apnea, no whoop). Convalescent (weeks–months). Lab: ↑↑lymphocytes (PT blocks lymphocyte homing from lymph nodes)",
        "Macrolides (azithromycin — preferred; erythromycin; clarithromycin). TMP-SMX (alternative). Treat within catarrhal phase → aborts illness. Post-exposure prophylaxis: azithromycin close contacts. Vaccination: DTaP (children, 5 doses) + Tdap (adults q10y + ALL pregnant women at 27–36 weeks gestation — protect newborn)",
        "Lymphocytosis: PT blocks CXCR4/CCR7 (lymphocyte homing receptors) → can't exit lymph nodes → ↑↑circulating lymphocytes (WBC 20,000–100,000+ cells/mcL — almost all lymphocytes). Infants <6 months: most severe disease (apnea, pulmonary HTN, death) — no whoop (too weak). Cocooning strategy: vaccinate all household contacts to protect newborns. NAAT (PCR of nasopharyngeal swab): most sensitive diagnostic test."
    ),
    # ── Viruses (additional) ──────────────────────────────────────────────
    "ebv": _mo(
        "dsDNA herpesvirus (gamma-herpesvirus); enveloped; infects B-lymphocytes via CD21 (CR2) and pharyngeal epithelium. Lifelong latency in memory B cells. >90% adults seropositive worldwide",
        "LMP1 (constitutively active CD40 signal → B-cell activation + immortalization + NF-kB), LMP2A (mimics BCR → survival signal), EBNAs (nuclear antigens — latency maintenance), EBERs (small RNAs — FISH target for EBV tumors), gp350 (B-cell receptor)",
        "Infectious mononucleosis: FEVER + exudative pharyngitis + POSTERIOR CERVICAL lymphadenopathy (bilateral posterior > anterior — characteristic) + splenomegaly. Atypical lymphocytes (reactive T-cells). Positive heterophile (Monospot). EBV malignancies: Burkitt lymphoma (t(8;14) myc/IgH, jaw mass, African endemic — EBV 95%), Hodgkin lymphoma (mixed cellularity), nasopharyngeal carcinoma (virtually 100% undifferentiated type — Southern China/SE Asia), primary CNS lymphoma (HIV), PTLD",
        "Infectious mono: supportive. Avoid contact sports × 3–4 weeks (splenic rupture risk). Corticosteroids if airway compromise/thrombocytopenia/hemolytic anemia. Antivirals NOT effective for EBV mono. AVOID ampicillin/amoxicillin (maculopapular rash common — not true allergy). EBV-PTLD: reduce immunosuppression + rituximab",
        "Monospot (heterophile Ab): IgM agglutinates horse/sheep/ox RBCs. Sensitivity 85%, specificity 94% in adults; false-negative in children <4y. EBV serology: VCA IgM (acute) → VCA IgG + EA-D IgG (active replication) → EBNA IgG (develops 2–4 months after acute — EBNA negative in acute mono). Spleen rupture risk: peak weeks 2–3 (can occur with minor trauma — key contraindication to contact sports)."
    ),
    "vzv": _mo(
        "dsDNA herpesvirus (alpha-herpesvirus); highly contagious (airborne + contact); same virus: chickenpox (primary) and shingles (reactivation from dorsal root/cranial nerve ganglia)",
        "Glycoproteins gB/gE/gC (envelope, cell-to-cell spread — gE essential), thymidine kinase (acyclovir activation), VZV kinases (immune evasion)",
        "Varicella (chickenpox): pruritic vesicular rash in crops — DIFFERENT STAGES simultaneously (macule → papule → vesicle → pustule → crust); begins face/trunk → centrifugal. Complications: bacterial superinfection (S. aureus/GAS), varicella pneumonitis (adults, severe in pregnancy), cerebellar ataxia, encephalitis. Herpes zoster (shingles): painful DERMATOMAL unilateral vesicular rash. Zoster ophthalmicus (CN V1 — Hutchinson sign: vesicle on nose tip → high risk of ocular involvement). Ramsay Hunt (geniculate ganglion CN VII): vesicles in ear + facial palsy + sensorineural hearing loss. Post-herpetic neuralgia (PHN): most common complication",
        "Varicella: acyclovir (within 24h of rash onset — adults/immunocompromised). Vaccine: live-attenuated Oka strain (2 doses). VZIG: post-exposure prophylaxis (immunocompromised/pregnant/neonates). Zoster: valacyclovir or famciclovir × 7 days (within 72h → faster healing, ↓acute pain; PHN benefit modest). Shingrix (recombinant zoster vaccine): 2 doses ≥50 years — >90% effective (Zostavax discontinued in the US in 2020)",
        "Ramsay Hunt syndrome: VZV in geniculate ganglion → FACIAL PALSY + ear vesicles (external auditory canal/concha) + hearing loss ± vertigo. Worse prognosis than Bell's palsy (HSV VII). Treat: acyclovir + prednisone. PHN: burning neuropathic pain >3 months after rash (elderly highest risk). Prevention: treat shingles within 72h + Shingrix vaccination."
    ),
    "influenza": _mo(
        "Negative-sense ssRNA (Orthomyxovirus); segmented genome (8 segments — reassortment enables pandemic). Influenza A (most virulent, humans + animals — H and N subtypes: H1N1, H3N2 most common) and B (humans primarily). Enveloped; infects via sialic acid receptors",
        "Hemagglutinin (HA — sialic acid binding + fusion; major vaccine antigen), neuraminidase (NA — cleaves sialic acid → virion release; oseltamivir/zanamivir target), M2 ion channel (amantadine target — influenza A only), NS1 (interferon antagonist — immune evasion)",
        "Abrupt onset FEVER + myalgias + HEADACHE + malaise + dry cough + rhinorrhea ('flu hits like a truck'). Complications: primary viral pneumonia, secondary bacterial pneumonia (S. aureus, S. pneumoniae, H. influenzae — most common cause of death), myositis, myocarditis, Reye syndrome (aspirin in children → hepatic failure + encephalopathy — AVOID aspirin in children with influenza)",
        "Oseltamivir (Tamiflu PO) or zanamivir (inhaled): start within 48h of symptom onset → ↓duration 1–2 days + ↓complications. High-risk: start even after 48h if severe/hospitalized. Baloxavir marboxil (single dose, PA endonuclease inhibitor). Annual influenza vaccine: IIV/RIV (inactivated) or LAIV (live attenuated — nasal spray, healthy non-pregnant 2–49yo)",
        "Antigenic DRIFT (minor, annual): point mutations in HA/NA → reason for annual vaccine reformulation. Antigenic SHIFT (major): reassortment of RNA segments between human + animal influenza A → pandemic (1918 H1N1: 50M deaths; 2009 H1N1 swine flu: pandemic). High-dose vaccine for ≥65yo (4× antigen). Reye syndrome: AVOID aspirin in children with influenza/varicella. Amantadine/rimantadine: only Influenza A, near-universal resistance in current strains — not used clinically."
    ),
    # ── Parasites (additional) ────────────────────────────────────────────
    "toxoplasma": _mo(
        "Obligate intracellular protozoan (apicomplexan); definitive host: cats (oocysts shed in feces). Humans: intermediate host (tachyzoites — acute, rapidly dividing; bradyzoites — tissue cysts in muscle/brain, chronic). T. gondii",
        "Rhoptries (apical invasion organelles), MIC proteins (adhesion), GRA proteins (modify parasitophorous vacuole — evade lysosome fusion), SAG1/p30 (surface antigen), bradyzoite → tachyzoite conversion (triggered by immunocompromise)",
        "Immunocompetent: asymptomatic (90%) or self-limited cervical lymphadenopathy (mono-like). AIDS (CD4 <100): CNS toxoplasmosis — MULTIPLE ring-enhancing brain lesions (basal ganglia predilection — CT/MRI) → seizures, focal deficits, fever. Ocular toxoplasmosis (most common infectious posterior uveitis — retinochoroiditis). Congenital: chorioretinitis + hydrocephalus + intracranial calcifications (diffuse/scattered parenchymal — vs. CMV: periventricular)",
        "CNS toxoplasmosis (AIDS): pyrimethamine + sulfadiazine + leucovorin × 6 weeks (acute) → chronic suppression until CD4 >200 for >6 months on ART. Alternative: pyrimethamine + clindamycin + leucovorin. TMP-SMX DS QD (prophylaxis if CD4 <100 — covers Toxo + PCP). Congenital: pyrimethamine + sulfadiazine + leucovorin × 12 months",
        "CNS Toxo vs. PCNSL (AIDS): Toxo → multiple lesions, positive IgG serology, RESPONDS to empiric treatment (50% size reduction at 2 weeks). PCNSL (EBV-driven) → solitary, CSF EBV PCR+, FDG-PET hypermetabolic. Treat empirically for Toxo first → biopsy if no response. Cats shed oocysts only 1–3 weeks during primary infection. Immunocompromised: avoid raw meat + cat litter boxes."
    ),
    "giardia": _mo(
        "Flagellated protozoan; two forms: trophozoite (pear-shaped, bilateral symmetry, 2 nuclei/'owl-eye', 4 pairs of flagella — adheres to small intestine) and cyst (infectious — survives environment, resistant to chlorine). G. intestinalis/lamblia/duodenalis",
        "Variant surface proteins (VSPs — antigenic variation), adhesive disc (sucking disc attaches to intestinal epithelium), brush border microvillus damage (↓disaccharidase/lactase → secondary lactose intolerance), bile salt disruption (fat malabsorption)",
        "Most common intestinal parasite in developed world. Foul-smelling watery diarrhea (NO blood/pus — small intestine infection) + bloating + flatulence + greasy stools + malabsorption (fat-soluble vitamins) + secondary lactose intolerance. Chronic: weight loss, failure to thrive (children). Sources: contaminated water ('beaver fever' — mountain streams), daycare centers, travel",
        "Metronidazole 250 mg TID × 5–7 days (first-line). Tinidazole 2g × 1 dose (easier adherence). Nitazoxanide (alternative). Paromomycin (pregnancy — non-absorbable). Test-of-cure stool Ag if persistent symptoms",
        "Diagnosis: stool Ag immunoassay (most sensitive/specific); stool O&P exam (3 specimens alternate days); PCR. IgA deficiency + common variable immunodeficiency → chronic severe giardiasis (absence of secretory IgA → failure to clear). Treatment failures: consider reinfection, compliance, IgA deficiency. Giardia does NOT cause bloody diarrhea (ameba = Entamoeba histolytica causes bloody diarrhea + liver abscess)."
    ),
    "histoplasma": _mo(
        "Dimorphic fungus: mold in environment (23°C → hyphae with macroconidia/microconidia — infectious) → YEAST in tissue at 37°C (small oval 2–4 μm, inside macrophages — 'fills histiocytes'). H. capsulatum (no actual capsule). Endemic: Ohio/Mississippi River valleys, Central/South America",
        "Macrophage parasitism (survives within phagolysosomes — inhibits acidification), alpha-1,3-glucan (outer wall — shields beta-glucan → ↓pattern recognition), calcium-binding protein (CaBP — ↓complement activation)",
        "Immunocompetent: asymptomatic or flu-like illness + hilar/mediastinal lymphadenopathy (calcifies → 'buckshot' calcifications on CXR). Chronic cavitary: COPD lungs, upper lobe cavitation (TB-mimic). Disseminated histoplasmosis (AIDS CD4 <150, transplant, anti-TNF therapy): fever, hepatosplenomegaly, pancytopenia, oral ulcers, adrenal insufficiency (most common infectious cause of Addison disease in endemic areas)",
        "Mild/moderate: itraconazole × 6–12 weeks (acute pulmonary) or × 12 months (chronic). Severe/disseminated: liposomal amphotericin B (induction 2 weeks) → itraconazole (12 months — secondary prophylaxis in AIDS until CD4 >150 on ART × 6 months)",
        "Histoplasma urine Ag: most sensitive for disseminated disease + acute pulmonary (>90%). Cross-reacts with Blastomyces/Coccidioides. Compare: Coccidioides (Southwest US — 'valley fever' — spherules with endospores), Blastomyces (broad-based budding yeast). All dimorphic: mold → yeast in body at 37°C (except Coccidioides: mold → spherules). Screen HIV+ in endemic areas; itraconazole prophylaxis if CD4 <150."
    ),
    "mucor": _mo(
        "Filamentous mold (Mucorales); ribbon-like, broad, NON-SEPTATE (aseptate) hyphae branching at 90° RIGHT angles (vs. Aspergillus: septate, 45° acute angles). Genera: Rhizopus (most common human pathogen), Mucor, Lichtheimia. Ubiquitous in environment (decaying matter, bread mold)",
        "Angioinvasion (vascular thrombosis → tissue ischemia → black necrotic eschar), spore germination in hyperglycemic/high-iron environments (iron essential for growth — acidosis releases iron from transferrin), hyphal invasion of vessel walls",
        "Rhinocerebral mucormycosis (most common form — DKA/uncontrolled DM): starts in sinuses → black necrotic eschar on palate → orbits (proptosis, CN palsies) → brain (cavernous sinus thrombosis). Pulmonary (immunocompromised — hematologic malignancy, HSCT): consolidation + reversed halo sign on CT. Cutaneous (burns, trauma). Disseminated (profound immunocompromise — high mortality). COVID-19 + steroids + DM → ↑mucormycosis (India 2021 outbreak)",
        "EMERGENT surgical debridement (aggressive, repeated — remove ALL necrotic tissue — TIME CRITICAL). Liposomal amphotericin B (DOC — high doses). Isavuconazole or posaconazole (alternative/step-down). Treat underlying DM/DKA. Reduce immunosuppression. Deferoxamine (iron chelator): CONTRAINDICATED (provides bioavailable iron for Mucor → ↑infection)",
        "Mucorales vs. Aspergillus: hyphae width + branching angle distinguish. Mucor: BROAD, ASEPTATE (folded/collapsed), 90° right angles. Aspergillus: narrow, septate, 45° acute angles. Both angioinvasive. CRITICAL DIFFERENCE: Mucorales produce NO beta-glucan (no glucan in cell wall) → beta-glucan assay NEGATIVE (Aspergillus/Candida/PCP = positive). Reversed halo sign (CT): ground-glass center + consolidation ring — highly specific for pulmonary mucormycosis."
    ),
    "hav": _mo(
        "Positive-sense ssRNA (Picornavirus/Hepatovirus); non-enveloped (naked — survives in environment, partially resistant to chlorine); single serotype; IgM anti-HAV confirms acute infection. No chronic infection, no HCC from HAV",
        "VP1/VP3 (capsid proteins — receptor binding to HAVCR1/TIM-1 on hepatocytes), 3C protease (cleaves host innate immune proteins), 2B viroporin (membrane permeability)",
        "Hepatitis A: fecal-oral transmission (contaminated food/water — shellfish filter feeders, raw produce, daycare, international travel). Incubation 15–50 days (avg 28 days). Prodrome: fever + malaise + nausea + RUQ pain → jaundice + dark urine + pale stools + pruritus. Self-limited (NO chronic hepatitis). Fulminant hepatic failure: <1% (↑risk with underlying liver disease). No chronic carrier state",
        "Supportive (no antiviral). Fulminant: liver transplant evaluation. Prevention: HAV vaccine (inactivated — Havrix/Vaqta, 2 doses) — all children 12–23 months + high-risk groups (MSM, IVDU, chronic liver disease, travel). Post-exposure prophylaxis within 2 weeks: HAV vaccine (preferred <40yo) or IGIM 0.1 mL/kg (>40yo, immunocompromised, infants)",
        "HAV serology: IgM anti-HAV = acute infection (diagnostic). IgG anti-HAV = past infection or vaccination = immunity. HAV vaccine (inactivated) safe in immunocompromised. No vertical transmission (unlike HBV). No genome integration → NO chronicity, NO HAV-related HCC. Shellfish (oysters, clams): bivalves filter large water volumes → concentrate HAV + Norovirus → uncooked shellfish major route. Norovirus: most common viral gastroenteritis outbreak pathogen in US."
    ),
    "hpv": _mo(
        "Circular dsDNA (Papillomavirus); non-enveloped; epitheliotropic (infects squamous epithelium). >200 types. High-risk (oncogenic): HPV 16+18 (70% cervical cancer), 31, 33, 45. Low-risk: HPV 6+11 (90% anogenital warts, recurrent respiratory papillomatosis)",
        "E6 protein (binds E6-AP ubiquitin ligase → p53 degradation → ↑S-phase entry, ↑genomic instability), E7 protein (binds hypophosphorylated pRb → releases E2F → uncontrolled cell cycle). E6 + E7 = primary oncoproteins. L1 major capsid protein (VLP vaccine antigen)",
        "Anogenital warts (condyloma acuminata — HPV 6/11): cauliflower-like, flesh-colored, painless genital/anal papules. Cervical cancer (HPV 16/18 — CIN → invasive). Oropharyngeal cancer (HPV 16 — ↑incidence, multiple oral-sex partners, better prognosis than tobacco-associated). Anal cancer (HPV 16 — ↑MSM, HIV). Recurrent respiratory papillomatosis (HPV 6/11 — laryngeal warts, hoarseness)",
        "HPV vaccines (VLP — non-infectious): Gardasil-9 (covers HPV 6,11,16,18,31,33,45,52,58). Routine vaccination: age 11–12 years (both sexes). 2-dose series (9–14yo); 3-dose series (15–26yo). Catch-up through age 26; shared decision 27–45yo. Condyloma: topical (imiquimod, podophyllin, TCA) or ablative (cryotherapy, laser). CIN2+ on colposcopy: LEEP or ablation",
        "E6 → p53 degradation: loss of G1/S checkpoint → unchecked cell proliferation + apoptosis suppression. E7 → pRb inactivation: E2F release → S-phase entry without growth signals. Cervical cancer screening (USPSTF): Pap q3y (21–29yo); 30–65yo: Pap q3y, hrHPV alone q5y, or co-test q5y. Gardasil-9: ~97% effective against covered genotype-specific infections. HPV = most common sexually transmitted infection in the US."
    ),

    # ── RNA Viruses ───────────────────────────────────────────────────────────
    "rsv": _mo(
        "RNA virus; paramyxovirus; non-segmented negative-sense ssRNA",
        "Leading cause of bronchiolitis and pneumonia in infants (<2yo); spreads via droplets + fomites; incubation 4-6d; symptoms: coryza → wheeze/crackles → respiratory distress (nasal flaring, retractions); syncytia formation (multinucleated giant cells); adults: mild URI; elderly/immunocompromised: severe pneumonia",
        "Bronchiolitis (infants), pneumonia (elderly/immunocompromised), mild URI (adults); Diagnosis: rapid antigen test (nasal swab), PCR",
        "Supportive (O2, hydration); high-flow nasal cannula if needed; palivizumab prophylaxis for high-risk infants (premature, CHD, CLD); nirsevimab or clesrovimab (single-dose mAbs); RSV vaccine (Abrysvo/Arexvy/mResvia) for adults ≥75yo and 50–74yo at increased risk; maternal Abrysvo at 32–36 weeks"
    ),
    "rotavirus": _mo(
        "dsRNA virus; Reoviridae; non-enveloped; 11 segments",
        "MCC of severe dehydrating gastroenteritis in children worldwide (<5yo); spreads fecal-oral; incubation 1-3d; symptoms: fever → vomiting → watery (non-bloody) diarrhea (3-8d); damages villous enterocytes → malabsorptive diarrhea",
        "Severe dehydrating gastroenteritis in children <5yo; Diagnosis: stool antigen ELISA or PCR",
        "Oral rehydration solution (ORS); zinc supplementation reduces severity; IV fluids if severe; rotavirus vaccine (RotaTeq 3-dose, Rotarix 2-dose): given at 2, 4, (6) months; contraindications: intussusception history, SCID"
    ),
    "parvovirus b19": _mo(
        "ssDNA virus; non-enveloped; smallest DNA virus; tropism for erythroid progenitors (erythroid progenitors express P antigen/globoside = receptor)",
        "Slapped-cheek disease (fifth disease, erythema infectiosum) in children: fever → facial rash → lacy reticular rash trunk/extremities; arthropathy in adults (symmetric small joints); aplastic crisis in sickle cell/hemolytic anemia (destroys RBC precursors); hydrops fetalis (fetal anemia/heart failure) if infected during pregnancy; pure red cell aplasia in immunocompromised",
        "Fifth disease, aplastic crisis, arthropathy, hydrops fetalis, pure red cell aplasia; Diagnosis: serology (IgM acute, IgG immune); PCR for immunocompromised",
        "Supportive; IVIG for immunocompromised; aplastic crisis: RBC transfusions; pregnancy exposure: serial ultrasound for fetal hydrops (q2-4 weeks ×10-12 weeks); no vaccine available"
    ),
    "measles": _mo(
        "RNA virus; paramyxovirus (Morbillivirus); negative-sense ssRNA; highly contagious (R₀ = 12-18)",
        "Prodrome: fever + 3Cs (Cough, Coryza, Conjunctivitis) + Koplik spots (white spots on buccal mucosa — pathognomonic, appear before rash); rash: morbilliform (maculopapular), begins head/neck → spreads cephalocaudal → lasts 5-6d; complications: pneumonia (MCC of death), encephalitis (1/1000), SSPE (subacute sclerosing panencephalitis — rare, years later, fatal), otitis media; vitamin A deficiency worsens severity",
        "Measles (rubeola), pneumonia (MCC of death), encephalitis (1/1000), SSPE, otitis media; Diagnosis: clinical; serology (IgM); PCR",
        "Supportive; vitamin A (50,000-200,000 IU for children — reduces mortality/morbidity); post-exposure: MMR within 72h OR IVIG within 6d; MMR vaccine (2 doses: 12-15 months + 4-6 years); airborne precautions"
    ),
    "mumps": _mo(
        "RNA virus; paramyxovirus (Rubulavirus); negative-sense ssRNA",
        "Parotitis (bilateral parotid swelling, painful, 'chipmunk' facies) — hallmark; prodrome: low-grade fever, malaise, headache; parotitis peaks day 3; complications: orchitis (20-30% post-pubertal males, but rarely causes infertility), oophoritis (5%), aseptic meningitis (15%), encephalitis (rare), sensorineural hearing loss (unilateral), pancreatitis",
        "Parotitis, orchitis (20-30% post-pubertal males), aseptic meningitis (15%), oophoritis, pancreatitis, SNHL; Diagnosis: clinical; serology (IgM); PCR; amylase elevated",
        "Supportive; analgesia; orchitis: scrotal support + ice packs; MMR vaccine (~88% effective against mumps after 2 doses — outbreaks still occur); droplet precautions ×5 days from parotitis onset"
    ),
    "rubella": _mo(
        "RNA togavirus; positive-sense ssRNA; teratogenic",
        "Mild disease in children/adults: low-grade fever, lymphadenopathy (post-auricular, suboccipital — hallmark), maculopapular rash (face → trunk → extremities, 3d duration); arthralgia (common in adult women); CONGENITAL RUBELLA SYNDROME (CRS): 1st trimester infection → deafness + cataracts + cardiac defects (PDA, pulmonary artery stenosis) + intellectual disability + blueberry muffin rash (dermal erythropoiesis); risk: 85% in first trimester, <1% after 20 weeks",
        "Rubella, congenital rubella syndrome (deafness, cataracts, PDA, ID); Diagnosis: serology (IgM acute, IgG immune); PCR; CRS: IgM in neonate, virus in urine/throat",
        "Supportive; NO antiviral; MMR vaccine (live attenuated — CONTRAINDICATED in pregnancy); rubella IgG screen all pregnant women; vaccinate non-immune women postpartum; droplet precautions; notifiable disease"
    ),
    "nocardia": _mo(
        "Gram+ filamentous branching rods; weakly acid-fast (modified AFB+); aerobic; soil organism",
        "Opportunistic infection primarily in immunocompromised (steroids, transplant, HIV, CGD); pulmonary nocardiosis: MCC of nocardia infection — cavitary pneumonia with upper lobe predilection; CNS involvement (brain abscess) in up to 40%; cutaneous nocardiosis: traumatic inoculation → mycetoma (painless swelling with draining sinuses); disseminated disease in severely immunocompromised; N. asteroides complex (pulmonary/CNS), N. brasiliensis (cutaneous)",
        "Pulmonary nocardiosis (cavitary, upper lobe), CNS (brain abscess up to 40%), cutaneous (mycetoma), disseminated; Diagnosis: Gram stain (branching filaments), modified AFB+, culture 1-2 weeks",
        "TMP-SMX (first-line, 6-12 months); imipenem + amikacin (severe/disseminated); amoxicillin-clavulanate alternative; CNS: TMP-SMX + imipenem"
    ),
    "actinomyces": _mo(
        "Gram+ filamentous branching rods; NOT acid-fast; anaerobic/microaerophilic; part of normal oral/GI/GU flora",
        "Causes chronic suppurative granulomatous infections with draining sinus tracts; 'sulfur granules' (yellow granules in discharge = colonies of Actinomyces) are pathognomonic; cervicofacial (MCC, 50%): jaw swelling + sinus tract, often after dental procedure or trauma (lumpy jaw); thoracic: pneumonia + empyema + rib/vertebral involvement; abdominal/pelvic: associated with IUD use (A. israelii); actinomycetoma: chronic foot infection",
        "Cervicofacial actinomycosis (lumpy jaw), thoracic, abdominal/pelvic (IUD-associated), actinomycetoma; Diagnosis: Gram stain (filamentous), anaerobic culture (sulfur granules), NOT acid-fast",
        "Prolonged penicillin G (IV 2-6 weeks) → amoxicillin (oral 6-12 months); doxycycline or clindamycin alternatives; surgical drainage of abscesses"
    ),
    "coccidioides": _mo(
        "Dimorphic fungus: mycelium (arthroconidia) in environment → spherule (endospores) in tissue; endemic Southwest US (San Joaquin Valley fever), Mexico, Central/South America",
        "Inhalation of arthroconidia; primary pulmonary coccidioidomycosis: 60% asymptomatic; 40%: fever, cough, pleuritic chest pain, arthralgia ('valley fever' or 'desert rheumatism'); eosinophilia characteristic; erythema nodosum or multiforme (hypersensitivity); CXR: pulmonary infiltrates, hilar adenopathy, cavities; disseminated (1-5%): skin (verrucous lesions), bone, meninges (most serious complication — chronic basilar meningitis with eosinophilic CSF)",
        "Valley fever (pulmonary), disseminated (skin, bone, meninges); Diagnosis: serology (IgM early, IgG late; CF titer correlates with severity); direct microscopy: spherule with endospores (pathognomonic); culture (BSL-3)",
        "Mild pulmonary: observation or fluconazole; severe/disseminated: fluconazole; amphotericin B for severely ill; lifelong fluconazole suppression for meningitis"
    ),
    "blastomyces": _mo(
        "Dimorphic fungus: mold (conidia) in environment → broad-based budding yeast in tissue; endemic: Ohio/Mississippi River valleys, Great Lakes, Central/Atlantic states; soil near decaying wood/water",
        "Inhalation of conidia; pulmonary blastomycosis: pneumonia (often mistaken for bacterial pneumonia or malignancy — chronic course distinguishes); skin (MCC extrapulmonary): verrucous/ulcerative lesions with microabscesses; bone (osteomyelitis, vertebrae); GU (prostatitis, epididymitis in men); CNS (rare, severe, meningitis); immunocompromised: severe disseminated ARDS-like picture",
        "Pulmonary blastomycosis, skin (verrucous), bone, GU (prostatitis/epididymitis), CNS; Diagnosis: broad-based budding yeast on microscopy; urine antigen (Mira Vista); culture",
        "Mild-moderate pulmonary: itraconazole; severe/CNS: amphotericin B → itraconazole step-down; pregnancy: amphotericin B (itraconazole teratogenic)"
    ),
    "sporothrix": _mo(
        "Dimorphic fungus: mold in environment → cigar-shaped yeast in tissue; Sporothrix schenckii; found in soil, sphagnum moss, rose thorns, hay, wood",
        "Sporotrichosis — 'rose gardener's disease': traumatic inoculation (thorn prick) → classic lymphocutaneous pattern: primary papule at inoculation site → ulcerates → ascending lymphangitis with nodules along lymphatic chain (sporotrichoid spread); fixed cutaneous: single lesion without lymphatic spread; disseminated (rare, immunocompromised): bone, joint, meninges, pulmonary; cat-associated outbreaks (bites/scratches)",
        "Sporotrichosis (lymphocutaneous, fixed cutaneous, disseminated, cat-associated); Diagnosis: culture (cigar-shaped yeast at 37°C); histology: asteroid bodies",
        "Lymphocutaneous: itraconazole 3-6 months; severe/disseminated/CNS: amphotericin B → itraconazole; SSKI alternative in resource-limited settings"
    ),
    "leishmania": _mo(
        "Intracellular protozoan; transmitted by sandfly (Phlebotomus/Lutzomyia); amastigote in macrophages (human tissue); promastigote in sandfly",
        "Three forms: (1) Cutaneous leishmaniasis: painless papule → ulcer with raised indurated border ('volcano crater' appearance); Old World (L. major, tropica) vs New World (L. braziliensis — risk of mucosal spread); (2) Mucocutaneous (espundia): L. braziliensis → destructive lesions of nose/mouth/pharynx; (3) Visceral (kala-azar, L. donovani, L. infantum): fever + massive splenomegaly + hepatomegaly + pancytopenia + hypergammaglobulinemia + darkening of skin; fatal if untreated",
        "Cutaneous ulcer (volcano crater), mucocutaneous destruction (espundia), visceral (kala-azar: splenomegaly, pancytopenia, fatal if untreated); Diagnosis: amastigotes in biopsy/bone marrow (Donovan bodies); rK39 antigen test; PCR",
        "Visceral: liposomal amphotericin B (first-line in immunocompromised/pregnant); miltefosine (oral); pentavalent antimonials; cutaneous: observation, topical paromomycin, fluconazole, or antimonials depending on species"
    ),
    "trypanosoma": _mo(
        "Flagellated protozoan; two major species with distinct vectors and disease patterns",
        "T. brucei (African sleeping sickness): vector = tsetse fly; two subspecies — T.b. gambiense (West Africa, 97% of cases, chronic) and T.b. rhodesiense (East Africa, acute, severe); Stage 1 (hemolymphatic): fever, lymphadenopathy (Winterbottom's sign — posterior cervical), chancre at bite site; Stage 2 (meningoencephalitic): CNS invasion → sleep cycle reversal, confusion, coma, death if untreated. T. cruzi (Chagas disease): vector = Reduviid bug (kissing bug, feces contaminate bite wound); acute: Romaña's sign (painless unilateral periorbital edema), myocarditis; chronic: dilated cardiomyopathy, heart block, sudden death, megaesophagus/megacolon",
        "African sleeping sickness (T. brucei: Stage 1 hemolymphatic, Stage 2 CNS), Chagas disease (T. cruzi: Romaña's sign, dilated cardiomyopathy, megacolon); Diagnosis: blood smear (trypomastigotes), CATT (T. brucei), 2 serologies (T. cruzi chronic), PCR",
        "T. b. gambiense: oral fexinidazole (stages 1–2, WHO-preferred) or pentamidine (stage 1) / nifurtimox-eflornithine (stage 2); T. b. rhodesiense: suramin (stage 1), melarsoprol (stage 2), fexinidazole now an option; T. cruzi: benznidazole or nifurtimox (most effective in acute phase)"
    ),
    "schistosoma": _mo(
        "Trematode (blood fluke); complex lifecycle: cercariae in fresh water penetrate skin → schistosomula → adult worms in portal/mesenteric veins; three main species",
        "Cercarial dermatitis ('swimmer's itch'): pruritic rash at skin penetration; Katayama fever (acute): 4-6 weeks after heavy exposure — fever, urticaria, eosinophilia, hepatosplenomegaly (serum sickness-like); Chronic disease by species: S. mansoni/japonicum: intestinal/hepatic — portal HTN, esophageal varices, 'pipe-stem' periportal fibrosis (Symmers fibrosis), hematemesis; S. haematobium: urogenital — hematuria, bladder fibrosis, obstructive uropathy, squamous cell carcinoma of bladder (not TCC!)",
        "Swimmer's itch, Katayama fever, portal HTN/pipe-stem fibrosis (mansoni/japonicum), bladder SCC (haematobium, not TCC); Diagnosis: stool/urine microscopy (egg spine pattern); serology; rectal biopsy",
        "Praziquantel (drug of choice, all species, single or two-dose regimen); prevention: avoid endemic fresh water; mass drug administration"
    ),
    "strongyloides": _mo(
        "Nematode (roundworm); unique: autoinfection cycle; can persist for decades; hyperinfection in immunosuppressed",
        "Penetration of intact skin by filariform larvae (from contaminated soil) → lung migration (Löffler-like) → swallowed → adult in proximal small bowel; chronic strongyloidiasis: urticarial rash (larva currens — linear, rapidly migrating, pathognomonic), mild GI symptoms; hyperinfection syndrome (immunosuppressed — corticosteroids, HTLV-1, transplant): massive larval invasion → gram-negative sepsis (larvae carry gut bacteria through bowel wall), meningitis, pneumonia, potentially fatal; eosinophilia (often absent in hyperinfection)",
        "Larva currens rash, chronic GI, hyperinfection syndrome (gram-negative sepsis, meningitis, pneumonia — in immunosuppressed); Diagnosis: stool O&P, Baermann technique, serology ELISA (high sensitivity)",
        "Ivermectin (drug of choice, superior to albendazole); hyperinfection: ivermectin until stool/sputum negative; SCREEN all patients before immunosuppression — treat if positive to prevent hyperinfection"
    ),
    "legionella": _mo(
        "Gram-negative rod that stains poorly (use silver stain); intracellular; grows on buffered charcoal yeast extract (BCYE) agar with cysteine and iron",
        "Survives and multiplies inside alveolar macrophages (blocks phagolysosome fusion); spread by aerosols from contaminated water (cooling towers, hot tubs, showers) — NOT person to person",
        "Legionnaires disease — severe atypical pneumonia with high fever, relative bradycardia, diarrhea, confusion, hyponatremia, ↑liver enzymes, ↑CK; Pontiac fever — mild, self-limited flu-like illness",
        "Azithromycin or a respiratory fluoroquinolone (levofloxacin) — β-lactams do not work (intracellular organism)",
        "Urinary antigen test detects serogroup 1 only — confirm with culture or PCR of sputum. Risks: smoking, older age, immunosuppression, chronic lung disease. Outbreaks are reported to public health."
    ),
    "sars-cov-2": _mo(
        "Enveloped positive-sense single-stranded RNA betacoronavirus",
        "Spike protein binds ACE2 (respiratory epithelium, type II pneumocytes, endothelium) after cleavage by TMPRSS2; spread by respiratory droplets and aerosols",
        "COVID-19 — fever, cough, loss of smell/taste, viral pneumonia with bilateral peripheral ground-glass opacities, ARDS, venous thromboembolism, myocarditis, MIS-C in children, post-COVID condition (long COVID)",
        "High-risk outpatients: nirmatrelvir-ritonavir (Paxlovid) within 5 days of symptoms, or 3 days of remdesivir; molnupiravir if neither is suitable. Hospitalized patients needing oxygen: dexamethasone (RECOVERY trial) ± remdesivir; tocilizumab or baricitinib for progressive disease; prophylactic anticoagulation. Vaccination (mRNA or protein subunit)",
        "Dexamethasone helps only patients who need oxygen. Ritonavir strongly inhibits CYP3A4 — check interactions (statins, DOACs, tacrolimus, amiodarone and many others)."
    ),
    "dermatophytes": _mo(
        "Filamentous fungi that infect keratin (skin, hair, nails) — Trichophyton (most common), Microsporum, Epidermophyton",
        "Keratinases; spread by direct contact, shared items and animals (Microsporum canis from cats and dogs)",
        "Tinea capitis (children — scaling, hair loss, kerion), corporis (ring-shaped plaque with central clearing — 'ringworm'), cruris (groin, spares the scrotum), pedis (athlete's foot), unguium (onychomycosis). Tinea versicolor is a different yeast (Malassezia — light or dark macules, 'spaghetti and meatballs' on KOH)",
        "Topical azoles or terbinafine for skin; ORAL therapy for tinea capitis (griseofulvin or terbinafine) and onychomycosis (terbinafine — check liver enzymes)",
        "Diagnose with a KOH prep (branching septate hyphae). Treating suspected tinea with a topical steroid alone causes tinea incognito. Under a Wood lamp, Microsporum fluoresces."
    ),
    "enterobius vermicularis": _mo(
        "Nematode (roundworm) — pinworm",
        "Fecal-oral spread of eggs (hands, bedding); female worms crawl out at night to lay eggs on perianal skin → self-reinfection by scratching",
        "Perianal itching (especially at night), poor sleep; rarely vulvovaginitis or appendicitis",
        "Albendazole (or mebendazole or pyrantel pamoate) single dose, repeated after 2 weeks; treat the whole household; wash bedding, keep nails short",
        "Diagnose with the tape test (adhesive tape on perianal skin first thing in the morning, eggs seen under the microscope); stool ova-and-parasite exams are usually negative. Most common worm infection in the US."
    ),
}

_MICRO_ALIASES = {
    "syphilis": "treponema pallidum", "treponema": "treponema pallidum",
    "lyme disease": "borrelia burgdorferi", "borrelia": "borrelia burgdorferi",
    "malaria": "plasmodium", "plasmodium falciparum": "plasmodium",
    "chlamydia": "chlamydia trachomatis", "gonorrhea": "n gonorrhoeae",
    "neisseria gonorrhoeae": "n gonorrhoeae", "neisseria meningitidis": "n meningitidis",
    "meningococcus": "n meningitidis",
    "clostridioides difficile": "c difficile", "clostridium difficile": "c difficile",
    "c diff": "c difficile",
    "tuberculosis": "m tuberculosis", "mycobacterium tuberculosis": "m tuberculosis",
    "streptococcus pyogenes": "strep pyogenes", "streptococcus pneumoniae": "strep pneumoniae",
    "pneumococcus": "strep pneumoniae", "streptococcus agalactiae": "strep agalactiae",
    "staph aureus": "s aureus", "staphylococcus epidermidis": "s epidermidis",
    "escherichia coli": "e coli", "pseudomonas aeruginosa": "pseudomonas",
    "klebsiella pneumoniae": "klebsiella", "haemophilus influenzae": "h influenzae",
    "listeria monocytogenes": "listeria", "helicobacter pylori": "h pylori",
    "enterococcus faecalis": "enterococcus", "campylobacter jejuni": "campylobacter",
    "bacteroides": "bacteroides fragilis",
    "clostridium perfringens": "c perfringens", "gas gangrene": "c perfringens",
    "tetanus": "c tetani", "botulism": "c botulinum", "diphtheria": "c diphtheriae",
    "cholera": "vibrio cholerae", "pertussis": "bordetella pertussis",
    "whooping cough": "bordetella pertussis",
    "rocky mountain spotted fever": "rickettsia", "rickettsia rickettsii": "rickettsia",
    "salmonellosis": "salmonella", "typhoid fever": "salmonella", "shigellosis": "shigella",
    "nocardiosis": "nocardia", "actinomycosis": "actinomyces",
    "hepatitis a": "hav", "hepatitis b": "hbv", "hepatitis c": "hcv",
    "herpes simplex": "hsv", "herpes simplex virus": "hsv",
    "cytomegalovirus": "cmv", "epstein-barr virus": "ebv", "epstein barr virus": "ebv",
    "mononucleosis": "ebv", "infectious mononucleosis": "ebv",
    "varicella": "vzv", "chickenpox": "vzv", "shingles": "vzv", "herpes zoster": "vzv",
    "varicella zoster virus": "vzv", "human papillomavirus": "hpv",
    "respiratory syncytial virus": "rsv", "parvovirus": "parvovirus b19",
    "fifth disease": "parvovirus b19",
    "candidiasis": "candida", "candida albicans": "candida",
    "pneumocystis jirovecii": "pneumocystis", "pneumocystis pneumonia": "pneumocystis",
    "aspergillosis": "aspergillus", "cryptococcosis": "cryptococcus",
    "cryptococcal meningitis": "cryptococcus", "histoplasmosis": "histoplasma",
    "coccidioidomycosis": "coccidioides", "valley fever": "coccidioides",
    "blastomycosis": "blastomyces", "sporotrichosis": "sporothrix", "mucormycosis": "mucor",
    "toxoplasmosis": "toxoplasma", "toxoplasma gondii": "toxoplasma",
    "giardiasis": "giardia", "giardia lamblia": "giardia",
    "leishmaniasis": "leishmania", "chagas disease": "trypanosoma",
    "schistosomiasis": "schistosoma", "strongyloidiasis": "strongyloides",
    "legionella pneumophila": "legionella", "legionnaires disease": "legionella",
    "legionnaires' disease": "legionella", "pontiac fever": "legionella",
    "covid-19": "sars-cov-2", "covid": "sars-cov-2", "coronavirus": "sars-cov-2",
    "tinea": "dermatophytes", "ringworm": "dermatophytes", "tinea corporis": "dermatophytes",
    "tinea capitis": "dermatophytes", "tinea pedis": "dermatophytes",
    "tinea cruris": "dermatophytes", "onychomycosis": "dermatophytes",
    "athlete's foot": "dermatophytes", "trichophyton": "dermatophytes",
    "pinworm": "enterobius vermicularis", "pinworms": "enterobius vermicularis",
    "enterobius": "enterobius vermicularis", "enterobiasis": "enterobius vermicularis",
    'hpv vaccine': 'hpv',
    'gardasil': 'hpv',
    'hpv vaccination': 'hpv',
    'h pylori stool antigen': 'h pylori',
    'urea breath test': 'h pylori',
    'stool antigen test': 'h pylori',
    'monospot': 'ebv',
    'heterophile antibody': 'ebv',
    'monospot test': 'ebv',
    'heterophile antibody test': 'ebv',
}
