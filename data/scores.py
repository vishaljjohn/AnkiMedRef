"""Clinical scores and alternate names (tier 0.5e).

Edit freely — see data/__init__.py for how files are loaded."""
from ..formatters import _ss


_SCORES = {
    # ── Pulmonary / PE / DVT ──────────────────────────────────────────────────
    "wells pe": _ss(
        "Estimate pre-test probability of pulmonary embolism",
        "Clinical DVT signs/sx +3 · PE #1 diagnosis +3 · HR >100 +1.5 · Immobilization/surgery ≤4 wks +1.5 · Prior DVT/PE +1.5 · Hemoptysis +1 · Malignancy +1",
        "≤4 = PE unlikely (use D-dimer) · >4 = PE likely (proceed to CT-PA). Simplified: ≤1 low, 2–6 moderate, >6 high",
        "If Wells ≤4 and D-dimer negative → PE ruled out, no imaging needed. Wells >4 → skip D-dimer, go straight to CT-PA."
    ),
    "wells dvt": _ss(
        "Estimate pre-test probability of deep vein thrombosis",
        "Active cancer +1 · Paralysis/cast +1 · Bedridden >3d or surgery <12wks +1 · Tenderness along deep veins +1 · Entire leg swollen +1 · Calf swelling >3cm vs other leg +1 · Pitting edema (symptomatic leg) +1 · Collateral superficial veins +1 · Alternative diagnosis as/more likely −2",
        "Score ≤0: low probability · 1–2: moderate · ≥3: high. Low + neg D-dimer = DVT excluded",
        "Alternative diagnosis point is critical — always consider cellulitis, Baker cyst, muscle tear."
    ),
    "curb-65": _ss(
        "Severity score for community-acquired pneumonia (CAP) — guides admission decision",
        "C: Confusion (new) +1 · U: Urea >7 mmol/L (BUN >19 mg/dL) +1 · R: RR ≥30/min +1 · B: BP <90 systolic or ≤60 diastolic +1 · 65: Age ≥65 +1",
        "0–1: outpatient (mortality <1%) · 2: inpatient ward (mortality ~9%) · ≥3: consider ICU (mortality ~22%) · 4–5: severe (mortality >40%)",
        "PSI/PORT score is more accurate but complex. CURB-65 is the quick bedside tool. Score 2 = short admission or close outpatient follow-up."
    ),
    "curb65": _ss(
        "Severity score for community-acquired pneumonia (CAP)",
        "Confusion + Urea >7 mmol/L + RR ≥30 + BP <90/60 + Age ≥65 (1 point each)",
        "0–1: outpatient · 2: inpatient · ≥3: ICU consideration · ≥4: severe"
    ),
    # ── Cardiac ───────────────────────────────────────────────────────────────
    "chads2-vasc": _ss(
        "Stroke risk in non-valvular atrial fibrillation — guides anticoagulation",
        "CHF +1 · Hypertension +1 · Age ≥75 +2 · Diabetes +1 · Stroke/TIA history +2 · Vascular disease (MI, PAD, aortic plaque) +1 · Age 65–74 +1 · Sex (female) +1",
        "0 (men) or 1 (women): no anticoagulation · 1 (men) or 2 (women): consider · ≥2 (men) or ≥3 (women): anticoagulate, DOAC preferred (ACC/AHA 2023)",
        "Female sex is a risk modifier, not a standalone indication."
    ),
    "cha2ds2-vasc": _ss(
        "Stroke risk score in atrial fibrillation",
        "CHF +1 · HTN +1 · Age ≥75 +2 · DM +1 · Stroke/TIA +2 · Vascular disease +1 · Age 65–74 +1 · Female sex +1",
        "Score ≥2 (men) or ≥3 (women): anticoagulate. Score 0 (men) or 1 (women): no anticoagulation needed",
        "DOACs preferred over warfarin for non-valvular AF (except mechanical valves or moderate-severe mitral stenosis)."
    ),
    "has-bled": _ss(
        "Bleeding risk in patients with AF on anticoagulation — NOT a reason to withhold anticoagulation",
        "Hypertension (uncontrolled SBP >160) +1 · Abnormal renal function (dialysis, Cr >2.3, transplant) +1 · Abnormal liver function (cirrhosis, bili >2×, ALT >3×) +1 · Stroke history +1 · Bleeding history or predisposition +1 · Labile INR (TTR <60%) +1 · Elderly (age >65) +1 · Drugs (antiplatelets/NSAIDs) +1 · Alcohol (≥8 drinks/week) +1",
        "0–2: low-moderate risk · ≥3: high bleeding risk (1 per 100 patient-years). Max score 9",
        "High HAS-BLED score = identify and correct modifiable risk factors (BP control, stop NSAIDs), NOT a reason to stop anticoagulation. Stroke risk from AF almost always exceeds bleeding risk."
    ),
    "heart score": _ss(
        "Risk stratification for chest pain — predicts major adverse cardiac events (MACE) at 30 days",
        "H-istory: highly suspicious +2, moderately suspicious +1, slightly suspicious +0 · E-CG: significant ST deviation +2, non-specific repolarization +1, normal +0 · A-ge: ≥65 +2, 45–64 +1, <45 +0 · R-isk factors: known atherosclerosis or ≥3 risk factors +2, 1–2 risk factors +1, none +0 · T-roponin: >3× ULN +2, 1–3× ULN +1, ≤ULN +0",
        "0–3: low (1.7% MACE — safe for early discharge) · 4–6: moderate (12% MACE — observe/stress test) · 7–10: high (65% MACE — cardiology consult, likely admission)",
        "HEART score 0–3 with negative serial troponins → safe discharge. Better than TIMI for undifferentiated ED chest pain."
    ),
    "timi": _ss(
        "Risk score for NSTEMI/Unstable Angina — predicts 14-day mortality/MI/revascularization",
        "Age ≥65 +1 · ≥3 CAD risk factors (HTN, DM, hyperlipidemia, family hx, smoking) +1 · Known CAD (stenosis ≥50%) +1 · ST deviation on ECG +1 · ≥2 anginal events in 24h +1 · Aspirin use in prior 7 days +1 · Elevated cardiac markers +1",
        "0–2: low risk (4.7%) · 3–4: moderate (13.2%) · 5–7: high (26.2%). Score ≥3 → early invasive strategy",
        "TIMI was derived for NSTEMI — not as useful for undifferentiated chest pain. HEART score performs better in ED."
    ),
    "grace score": _ss(
        "Predicts in-hospital and 6-month mortality in ACS",
        "Variables: age, heart rate, SBP, creatinine, Killip class, ST-segment deviation, cardiac arrest at presentation, elevated cardiac biomarkers (each contributes weighted points — use online calculator)",
        "Low <108: <1% in-hospital mortality · Intermediate 109–140: 1–3% · High >140: >3%. 6-month mortality: low <88, intermediate 88–118, high >118",
        "GRACE is more accurate than TIMI for ACS risk but requires a calculator. Drives decision for early invasive strategy in NSTEMI."
    ),
    # ── Sepsis / ICU ──────────────────────────────────────────────────────────
    "qsofa": _ss(
        "Bedside screening tool to identify sepsis in non-ICU patients",
        "Altered mental status (any GCS reduction) +1 · Respiratory rate ≥22/min +1 · Systolic BP ≤100 mmHg +1",
        "Score ≥2: high likelihood of sepsis, poor prognosis — initiate sepsis workup and management",
        "qSOFA predicts mortality but does not define sepsis (Sepsis-3 uses SOFA ≥2). SSC 2021 recommends against qSOFA alone as a screening tool (less sensitive than SIRS, NEWS or MEWS)."
    ),
    "sofa": _ss(
        "Sequential Organ Failure Assessment — defines sepsis (SOFA ≥2 from baseline) and tracks ICU progression",
        "Respiratory (PaO2/FiO2): <400=1, <300=2, <200+vent=3, <100+vent=4 · Coagulation (Plt): <150=1, <100=2, <50=3, <20=4 · Liver (Bili mg/dL): 1.2–1.9=1, 2–5.9=2, 6–11.9=3, ≥12=4 · Cardiovascular (MAP/vasopressors): MAP<70=1, dopamine≤5=2, NE≤0.1=3, NE>0.1=4 · CNS (GCS): 13–14=1, 10–12=2, 6–9=3, <6=4 · Renal (Cr mg/dL): 1.2–1.9=1, 2–3.4=2, 3.5–4.9=3, >5=4",
        "Score ≥2 from baseline = organ dysfunction = sepsis (Sepsis-3 definition). Max 24 points. Rising SOFA = worsening. Septic shock: SOFA ≥2 + vasopressors to maintain MAP ≥65 + lactate >2 mmol/L",
        "Each 1-point increase in SOFA = ~10% increase in ICU mortality. Use Sepsis-3 SOFA for diagnosis, not Sequential Organ Failure (older)."
    ),
    # ── GI / Liver ────────────────────────────────────────────────────────────
    "child-pugh": _ss(
        "Severity of liver cirrhosis — predicts surgical risk and survival",
        "Bilirubin (mg/dL): <2=1, 2–3=2, >3=3 · Albumin (g/dL): >3.5=1, 2.8–3.5=2, <2.8=3 · INR: <1.7=1, 1.7–2.3=2, >2.3=3 · Ascites: none=1, mild=2, moderate-severe=3 · Encephalopathy: none=1, grade 1–2=2, grade 3–4=3",
        "Class A (5–6): 1-yr survival 100%, 2-yr 85% — good candidate for surgery · Class B (7–9): 1-yr 80%, 2-yr 60% · Class C (10–15): 1-yr 45%, 2-yr 35% — avoid elective surgery",
        "Child-Pugh used clinically; MELD (now MELD 3.0) used for transplant allocation. Class C = high perioperative mortality."
    ),
    "meld": _ss(
        "Model for End-Stage Liver Disease — predicts 90-day mortality, used for transplant organ allocation",
        "MELD = 3.78×ln(bilirubin mg/dL) + 11.2×ln(INR) + 9.57×ln(creatinine mg/dL) + 6.43. MELD-Na adds serum Na: MELD + 1.32×(137–Na) − 0.24×MELD×(137–Na)",
        "<10: <2% 90-day mortality · 10–19: 6% · 20–29: 20% · 30–39: 52% · ≥40: 71%. MELD ≥15: transplant benefit outweighs risk",
        "US allocation used MELD-Na from 2016 and MELD 3.0 (adds sex and albumin) since July 2023 — serum Na strongly predicts outcomes in cirrhosis."
    ),
    "bisap": _ss(
        "Bedside Index of Severity in Acute Pancreatitis — early mortality prediction",
        "BUN >25 mg/dL +1 · Impaired mental status (GCS <15 or disorientation) +1 · SIRS (≥2 of: temp >38 or <36°C, HR >90, RR >20 or pCO2 <32, WBC >12k or <4k or >10% bands) +1 · Age >60 +1 · Pleural effusion on imaging +1",
        "0: <1% mortality · 1: 1.9% · 2: 3.6% · 3: 5.3% · 4–5: 22% mortality. Score ≥3 = severe pancreatitis",
        "BISAP is simpler than Ranson criteria (scored at 0h vs Ranson at 0h+48h). Equivalent predictive accuracy."
    ),
    "ranson": _ss(
        "Ranson criteria — predicts severity of acute pancreatitis (scored at admission and 48h)",
        "At admission: Age >55 · WBC >16,000 · Glucose >200 mg/dL · LDH >350 IU/L · AST >250 IU/L. At 48h: Hct drop >10% · BUN rise >5 mg/dL · Ca <8 mg/dL · PaO2 <60 mmHg · Base deficit >4 mEq/L · Fluid sequestration >6L",
        "<3 criteria: mild (mortality <1%) · 3–4: 15% · 5–6: 40% · ≥7: nearly 100% mortality",
        "Cannot be fully calculated until 48h — this is a limitation vs BISAP (instant). Each criterion = 1 point."
    ),
    # ── Neurology / Stroke ────────────────────────────────────────────────────
    "gcs": _ss(
        "Glasgow Coma Scale — quantifies level of consciousness, guides airway management",
        "Eyes: Spontaneous=4, To voice=3, To pain=2, None=1 · Verbal: Oriented=5, Confused=4, Words=3, Sounds=2, None=1 · Motor: Obeys=6, Localizes=5, Withdraws=4, Flexion=3, Extension=2, None=1",
        "Min 3 (deepest coma) to max 15 (normal). ≤8 = severe brain injury → intubate. 9–12 = moderate. 13–15 = mild. GCS ≤8: 'Intubate'",
        "GCS Motor score alone is the strongest predictor of outcome. GCS 3T = intubated patient (T for tube)."
    ),
    "glasgow coma scale": _ss(
        "Quantifies level of consciousness",
        "Eyes (1–4) + Verbal (1–5) + Motor (1–6). Eyes: spontaneous=4, voice=3, pain=2, none=1. Verbal: oriented=5, confused=4, words=3, sounds=2, none=1. Motor: obeys=6, localizes=5, withdraws=4, flexion=3, extension=2, none=1",
        "Total 3–15. ≤8 = severe (intubate) · 9–12 = moderate · 13–15 = mild TBI"
    ),
    "abcd2": _ss(
        "Predicts 2-day stroke risk after TIA — guides admission vs outpatient workup",
        "Age ≥60 +1 · BP ≥140/90 at presentation +1 · Clinical features: unilateral weakness +2, speech disturbance only +1, other +0 · Duration: ≥60 min +2, 10–59 min +1, <10 min +0 · Diabetes +1",
        "0–3: low (2-day stroke risk 1%) · 4–5: moderate (4%) · 6–7: high (8%). Score ≥4 → admit for expedited workup",
        "ABCD2 has limited discrimination — most guidelines now recommend rapid outpatient workup for all TIAs regardless of score."
    ),
    # ── Renal / General ───────────────────────────────────────────────────────
    "apache ii": _ss(
        "ICU severity of illness score — predicts hospital mortality",
        "12 acute physiology variables (each 0–4 pts): temp, MAP, HR, RR, oxygenation, pH, Na, K, Cr, Hct, WBC, GCS. Plus: Age points (0–6) + Chronic health points (2–5 if chronic organ failure/immunocompromise)",
        "Score range 0–71. Each 5-point increase ≈ doubles predicted mortality. Score >25 = predicted mortality >50%. Used for ICU triage and research stratification",
        "APACHE II requires 24h of data — not bedside in real time. SOFA preferred for sepsis. APACHE II used in ICU admission decisions and research."
    ),
    # ── Aliases ───────────────────────────────────────────────────────────────
    "wells score": _ss(
        "See Wells PE or Wells DVT score",
        "Wells PE: Clinical DVT signs +3 · PE #1 diagnosis +3 · HR >100 +1.5 · Immobilization +1.5 · Prior DVT/PE +1.5 · Hemoptysis +1 · Malignancy +1. Wells DVT: 9 criteria, alternative diagnosis −2",
        "PE: ≤4 = unlikely, >4 = likely. DVT: ≤0 = low, 1–2 = moderate, ≥3 = high"
    ),

    # ── Neurological ─────────────────────────────────────────────────────────
    "nihss": _ss(
        "NIH Stroke Scale — quantify stroke severity and guide treatment decisions",
        "11 items: LOC (0–3), LOC questions (0–2), LOC commands (0–2), gaze (0–2), visual fields (0–3), facial palsy (0–3), motor arm L/R (0–4 each), motor leg L/R (0–4 each), limb ataxia (0–2), sensory (0–2), language/aphasia (0–3), dysarthria (0–2), extinction/neglect (0–2). Max = 42",
        "0 = no stroke · 1–4 = minor · 5–15 = moderate · 16–20 = moderate-severe · ≥21 = severe. NIHSS ≥6 + LVO on imaging → thrombectomy candidate (up to 24h with appropriate penumbra imaging)",
        "NIHSS ≥4–5: threshold for IV tPA in many protocols (clinical judgment). Posterior circulation strokes often underscored by NIHSS (measures anterior circulation deficits better). Serial NIHSS: ↑≥4 points = clinical deterioration."
    ),
    # ── Hepatic ───────────────────────────────────────────────────────────────
    # ── Critical Care ─────────────────────────────────────────────────────────
    "news": _ss(
        "National Early Warning Score — detect clinical deterioration in ward patients and trigger escalation",
        "6 physiological parameters (scored 0–3 each): RR · SpO2 · Supplemental O2 (any = +2) · Temperature · SBP · HR. Plus: Consciousness (AVPU: Alert=0, Voice/Pain/Unresponsive=3). NEWS2 adds confusion to AVPU (ACVPU)",
        "0: low risk (routine monitoring) · 1–4: low-medium (↑frequency, consider review) · 5–6 or any single parameter score 3: medium (urgent review) · ≥7: high (emergency team, consider ICU)",
        "NEWS2 replaces original NEWS — specifically adds ACVPU (new confusion = 3 points regardless of other parameters). Shown to outperform modified early warning score (MEWS) for predicting cardiac arrest, ICU admission, and unexpected death at 24h. Limitations: not validated in obstetrics, COPD (SpO2 targets differ), or burns. NHS mandated NEWS2 as standard in UK hospitals."
    ),
    # ── Surgical / Procedural Risk ────────────────────────────────────────────
    "rcri": _ss(
        "Revised Cardiac Risk Index — predict major adverse cardiac events (MACE) in non-cardiac surgery",
        "6 independent predictors (1 point each): High-risk surgery (intraperitoneal, intrathoracic, suprainguinal vascular) · Ischemic heart disease (prior MI, positive stress test, angina, nitrate use, ECG with Q waves) · Congestive heart failure · Cerebrovascular disease (prior stroke/TIA) · Insulin-dependent diabetes · Preoperative creatinine >2 mg/dL",
        "0 factors: MACE risk 0.4% · 1: 1% · 2: 2.4–6.6% · ≥3: 5.4–11%. Low risk (<1%) → proceed without further testing",
        "High-risk surgery (RCRI): abdominal aortic aneurysm, aortoiliac, intraperitoneal, intrathoracic. Low-risk: superficial, endoscopy, cataract, breast. Cardiac biomarkers (troponin): recommended preoperatively in high-risk patients — perioperative MI common and often silent. BNP/NT-proBNP: elevated preop → ↑risk of 30-day MACE. Functional capacity ≥4 METs (climbing stairs, brisk walk) → proceed without further cardiac testing."
    ),
    "alvarado": _ss(
        "Alvarado score (MANTRELS) — diagnose acute appendicitis",
        "Migration of pain to RLQ +1 · Anorexia +1 · Nausea/Vomiting +1 · Tenderness in RLQ +2 · Rebound tenderness +1 · Elevated temperature (>37.3°C) +1 · Leukocytosis (>10K) +2 · Shift to left (neutrophilia) +1. Maximum = 10",
        "0–4: low probability (appendicitis unlikely — discharge with instructions) · 5–6: compatible (consider CT or observation) · 7–8: probable · 9–10: definite appendicitis → surgical consult",
        "AIR score (Appendicitis Inflammatory Response) — more recent alternative with better discrimination. CT abdomen/pelvis (with IV contrast): gold standard, sensitivity 94%, specificity 95%. US: preferred in children and pregnant women (avoids radiation). Pediatric Appendicitis Score (PAS): validated for children. Perforation risk ↑significantly with symptom duration >36–48h."
    ),
    "glasgow-blatchford": _ss(
        "Glasgow-Blatchford Score — predict need for clinical intervention in upper GI bleed",
        "Blood urea (mmol/L): 6.5–7.9=2, 8–9.9=3, 10–24.9=4, ≥25=6 · Hemoglobin men (g/dL): 12–12.9=1, 10–11.9=3, <10=6 · Hemoglobin women: 10–11.9=1, <10=6 · SBP (mmHg): 100–109=1, 90–99=2, <90=3 · Pulse ≥100=1 · Melena=1 · Syncope=2 · Hepatic disease=2 · Cardiac failure=2",
        "0: very low risk — outpatient management safe (97–99% NPV for needing intervention) · ≥1: admit and endoscopy · ≥6: high risk — ICU consideration",
        "GBS score 0: no intervention needed in 99% — can be discharged and scheduled for outpatient endoscopy. Performs better than Rockall pre-endoscopy (Rockall requires endoscopic findings). Complete Rockall score (post-endoscopy): adds endoscopic findings + diagnosis — predicts re-bleed and mortality. Pre-endoscopy Rockall: clinical variables only."
    ),
    # ── Liver / GI ────────────────────────────────────────────────────────────
    "rockall": _ss(
        "Rockall score — predict re-bleeding and mortality after upper GI bleed",
        "Pre-endoscopy: Age (<60=0, 60–79=1, ≥80=2) + Shock (no shock=0, tachycardia=1, hypotension=2) + Comorbidity (none=0, CHF/IHD/major=2, renal/hepatic/metastatic cancer=3). Post-endoscopy adds: Diagnosis (Mallory-Weiss=0, all other=1, GI malignancy=2) + Major stigmata of bleeding (none/flat spot=0, clot/visible vessel/spurting=2)",
        "0–2: low risk (re-bleed ~5%, mortality ~0%) · 3–4: moderate · ≥5: high risk (re-bleed 30–40%, mortality 10–40%)",
        "Pre-endoscopy Rockall: predict mortality before scope. Full post-endoscopy: guides re-endoscopy timing. Forrest classification for peptic ulcer: Ia (spurting = highest risk 55% re-bleed) → Ib (oozing) → IIa (visible vessel — 43%) → IIb (adherent clot — 22%) → IIc (flat spot) → III (clean base — 5%). High-risk Forrest (Ia, Ib, IIa): endoscopic hemostasis + 72h PPI infusion."
    ),
    # ── Obstetrics ────────────────────────────────────────────────────────────
    "apgar": _ss(
        "Assess newborn's condition at birth and need for resuscitation",
        "A-ppearance (color): blue/pale=0, blue extremities=1, pink all over=2 · P-ulse (HR): absent=0, <100=1, ≥100=2 · G-rimace (reflex irritability): none=0, grimace=1, cry/cough=2 · A-ctivity (muscle tone): limp=0, some flexion=1, active motion=2 · R-espiration: absent=0, weak/irregular=1, strong cry=2",
        "7–10: normal (routine care) · 4–6: moderate depression (stimulate, supplemental O2) · 0–3: severe depression (immediate resuscitation — bag-mask ventilation, CPR if HR <60). Assessed at 1 and 5 minutes",
        "1-min Apgar: reflects intrauterine conditions. 5-min Apgar: response to resuscitation — better predictor of neonatal outcome. Score ≤3 at 5 min and remains low at 10, 15, 20 min → ↑risk of cerebral palsy. APGAR mnemonic attributed to Virginia Apgar (1952). Apgar not intended to predict individual neurological outcome — population-level statistic. Neonatal resuscitation starts before Apgar if clearly depressed."
    ),
    "bishop": _ss(
        "Bishop score — assess cervical favorability for labor induction",
        "5 parameters: Dilation (cm): 0=0, 1–2=1, 3–4=2, ≥5=3 · Effacement (%): 0–30=0, 40–50=1, 60–70=2, ≥80=3 · Station (−3 to +3): −3=0, −2=1, −1/0=2, +1/+2=3 · Consistency: firm=0, medium=1, soft=2 · Position: posterior=0, mid=1, anterior=2",
        "≤5: unfavorable cervix → cervical ripening before induction (misoprostol, dinoprostone, Foley balloon, mechanical methods) · 6–8: intermediate · ≥9: favorable → oxytocin induction appropriate",
        "Modified Bishop score: simplified (dilation, effacement, station, consistency — excludes position). Cervical ripening agents: prostaglandins (misoprostol [Cytotec], dinoprostone [Cervidil]) — caution with prior uterine scar (↑uterine rupture risk with misoprostol). Mechanical: Foley catheter balloon (safe in prior CS). Successful induction: Bishop ≥9 → induction success rate approaching spontaneous labor."
    ),
    # ── Pediatric ─────────────────────────────────────────────────────────────
    "pecarn": _ss(
        "Pediatric Emergency Care Applied Research Network — identify children at very low risk for clinically important TBI (ciTBI) after head trauma",
        "Age <2: normal mental status + no scalp hematoma (except frontal) + no LOC ≥5s + no severe mechanism + no palpable skull fracture + acting normally per parent → ciTBI risk <0.02% (CT not recommended). Age ≥2: normal mental status + no LOC + no vomiting + no severe mechanism + no severe HA + no signs basilar skull fracture → ciTBI risk <0.05%",
        "Very low risk: observation only, no CT. Intermediate risk: physician decision based on other factors (parental preference, observation availability). High risk (any PECARN positive factor): CT head recommended",
        "Severe mechanisms: MVC with ejection/rollover/death of another, pedestrian/cyclist without helmet struck by motorized vehicle, fall >1.5m (age ≥2) or >0.9m (<2), head struck by high-impact object. PECARN validated in multicenter prospective study — sensitivity >99% for ciTBI. ciTBI = death, neurosurgical intervention, intubation >24h, or hospital admission ≥2 nights for head trauma."
    ),
    # ── Cardiology (additional) ───────────────────────────────────────────────
    "nyha": _ss(
        "New York Heart Association functional classification — severity of heart failure symptoms",
        "Class I: no limitation of physical activity (ordinary activity does not cause symptoms) · Class II: slight limitation (comfortable at rest, ordinary activity → symptoms) · Class III: marked limitation (comfortable at rest, less than ordinary activity → symptoms) · Class IV: symptoms at rest, unable to carry on any physical activity without discomfort",
        "Class III–IV: indicate advanced HF. Class I–II: appropriate for most guideline-directed therapies",
        "NYHA class guides therapy escalation, eligibility for CRT (Class III–IV + LBBB + EF ≤35%), ICD (Class I–III + EF ≤35%), and transplant listing (Class III–IV refractory). NYHA is subjective and may not correlate with objective EF. 6-minute walk test, VO2 max: objective functional assessments. ACC/AHA stages A–D: complementary staging system (A = risk factors only; B = structural disease, no symptoms; C = structural disease + symptoms [NYHA I–IV]; D = refractory)."
    ),
    "killip": _ss(
        "Killip classification — risk stratify acute MI patients by heart failure severity",
        "Class I: no HF signs (no rales, no S3) · Class II: rales in lower half lung fields or S3 gallop · Class III: pulmonary edema (rales >lower half) · Class IV: cardiogenic shock (SBP <90 + hypoperfusion)",
        "I: 30-day mortality ~6% · II: ~17% · III: ~38% · IV: ~67–81%",
        "Killip class at presentation is a strong independent predictor of mortality in STEMI and NSTEMI. Cardiogenic shock (Killip IV): intra-aortic balloon pump (IABP) does NOT improve mortality (IABP-SHOCK II trial); consider Impella or VA-ECMO as hemodynamic support. Primary PCI is treatment of choice even in cardiogenic shock."
    ),
    # ── Psychiatric / Substance ────────────────────────────────────────────────
    "cage": _ss(
        "CAGE questionnaire — screen for alcohol use disorder (AUD)",
        "C: Have you felt you should Cut down on drinking? · A: Have people Annoyed you by criticizing your drinking? · G: Have you ever felt Guilty about drinking? · E: Have you ever had a drink first thing in the morning as an Eye-opener?",
        "0: very low risk · 1: possible AUD (further evaluation) · ≥2: likely AUD (sensitivity 71%, specificity 90%)",
        "AUDIT (Alcohol Use Disorders Identification Test): 10-item questionnaire — more sensitive than CAGE, especially for hazardous drinking. AUDIT-C: abbreviated 3-item version. CAGE limitations: does not capture recent drinking (AUDIT-C better for screening). CIWA-Ar: assesses alcohol withdrawal severity (>8 = pharmacological treatment with benzodiazepines). ETOH withdrawal timeline: tremor/agitation (6–24h) → seizures (24–48h) → delirium tremens (48–72h)."
    ),
    "phq-9": _ss(
        "Patient Health Questionnaire-9 — screen and monitor depression severity",
        "9 items (DSM-5 criteria for MDD), each 0–3 (not at all / several days / more than half / nearly every day): depressed mood · anhedonia · sleep changes · fatigue · appetite changes · worthlessness/guilt · concentration · psychomotor changes · suicidal ideation. Score 0–27",
        "0–4: none · 5–9: mild (watchful waiting) · 10–14: moderate (treatment plan) · 15–19: moderately severe (active treatment) · 20–27: severe (immediate treatment, consider MH referral). PHQ-2: items 1+2 only — score ≥3 positive screen",
        "PHQ-9 item 9 (suicidal ideation): always address directly regardless of total score. MDD diagnosis: PHQ-9 score ≥10 + ≥5 of 9 symptoms for ≥2 weeks (at least one = depressed mood or anhedonia). Validated in primary care, numerous languages. GAD-7: analogous 7-item tool for generalized anxiety disorder (score ≥10 = moderate-severe anxiety)."
    ),
    # ── Infectious Disease ─────────────────────────────────────────────────────
    "mascc": _ss(
        "Multinational Association for Supportive Care in Cancer — identify low-risk febrile neutropenia patients for outpatient oral antibiotics",
        "Burden of febrile neutropenia symptoms: mild=5, moderate=3, severe/moribund=0 · No hypotension (SBP >90) +5 · No COPD +4 · Solid tumor or no previous fungal infection +4 · No dehydration +3 · Outpatient status at onset +3 · Age <60 +2",
        "Score ≥21: low risk (3% serious complication) — outpatient oral ciprofloxacin + amoxicillin-clavulanate appropriate · Score <21: high risk → hospital admission + IV broad-spectrum antibiotics (piperacillin-tazobactam, cefepime, or carbapenem)",
        "Febrile neutropenia: fever ≥38.3°C or sustained ≥38°C × 1h + ANC <500 or <1000 and expected to fall to <500. Blood cultures × 2 sets before antibiotics. ANC <100 → very high risk regardless of MASCC. G-CSF (filgrastim): primary prophylaxis if expected neutropenia >7 days (solid tumors); reduces duration but not mortality in established FN. High-risk features override MASCC: leukemia, stem cell transplant, poor performance status."
    ),
    # ── Trauma ────────────────────────────────────────────────────────────────
    "ottawa knee": _ss(
        "Ottawa Knee Rules — determine when knee X-ray is needed after acute injury",
        "X-ray required if ANY: Age ≥55 · Isolated patella tenderness (no other bony tenderness) · Fibular head tenderness · Unable to flex knee to 90° · Unable to bear weight for 4 steps both immediately and in ED",
        "All criteria absent: knee fracture excluded (sensitivity ~99%) → no X-ray needed → save time, cost, radiation",
        "Ottawa Rules (knee + ankle) reduce unnecessary X-rays by 30–40%. Ottawa Ankle Rules: malleolar zone tenderness + unable to bear weight → X-ray malleolus; midfoot tenderness + unable to bear weight → foot X-ray. Cannot apply if: altered consciousness, intoxicated, distracting painful injury, age <18 (knee — ankle rules validated to age 2). Pittsburgh Knee Rules: alternative (age <12 or ≥50 + mechanism + inability to walk → X-ray)."
    ),
    "ottawa ankle": _ss(
        "Ottawa Ankle Rules — determine when ankle/foot X-ray needed after acute injury",
        "Ankle X-ray if: pain in malleolar zone AND (tenderness over posterior 6 cm or tip of lateral malleolus OR posterior 6 cm or tip of medial malleolus OR unable to bear weight 4 steps). Foot X-ray if: pain in midfoot zone AND (tenderness at base of 5th metatarsal OR navicular OR unable to bear weight)",
        "Sensitivity ~98–100% for significant fractures — if Ottawa negative, no X-ray needed",
        "Validated in adults and children ≥2 years (Bachmann modified). Reduces ankle X-rays by ~30%. Apply only in acute injury (<10 days). Proximal fibular fracture (Maisonneuve): high ankle sprain → X-ray entire fibula if high suspicion. Ottawa Rules not validated for: suspected lisfranc injury, stress fractures, or pathological fractures."
    ),
    # ── Dermatology / Oncology ────────────────────────────────────────────────
    "breslow": _ss(
        "Breslow thickness — primary prognostic factor for cutaneous melanoma",
        "Measured in mm from granular layer of epidermis to deepest tumor cell on vertical section. T staging: T1a ≤0.8mm (no ulceration) · T1b ≤0.8mm with ulceration or 0.8–1.0mm any · T2 1.01–2.0mm · T3 2.01–4.0mm · T4 >4.0mm",
        "≤1.0mm: 5-year survival >90% · 1.01–2.0mm: ~80% · 2.01–4.0mm: ~70% · >4.0mm: ~50%. Ulceration upstages prognosis",
        "Breslow thickness + ulceration = T stage in AJCC 8th edition. Clark level (invasion depth by anatomical layer): largely replaced by Breslow. Sentinel lymph node biopsy (SLNB): indicated for Breslow ≥0.8mm (T1b+) — if positive → nodal ultrasound surveillance (completion dissection no longer routine — MSLT-II) and adjuvant immunotherapy or targeted therapy. BRAF V600E mutation (50% of melanomas): vemurafenib + cobimetinib (BRAF/MEK inhibitors); immunotherapy (nivolumab, pembrolizumab, ipilimumab + nivolumab) — first-line for unresectable/metastatic."
    ),
    "gleason": _ss(
        "Gleason score — grade prostate cancer based on glandular architecture",
        "Grade 1–5 assigned to two most common patterns (primary + secondary). Gleason score = primary grade + secondary grade (range 2–10). Grade Groups: 1 = Gleason ≤6 · 2 = Gleason 3+4=7 · 3 = Gleason 4+3=7 · 4 = Gleason 4+4 or 3+5 or 5+3=8 · 5 = Gleason 9–10",
        "Grade Group 1 (Gleason ≤6): favorable, often active surveillance · Grade Group 2–3 (Gleason 7): intermediate risk · Grade Group 4–5 (Gleason 8–10): high risk → definitive treatment",
        "Grade Group replaces Gleason score for clinical communication (clearer risk stratification). PSA + Grade Group + T stage = D'Amico classification (low/intermediate/high risk). Active surveillance: Grade Group 1 + PSA <10 + cT1–2a. Multiparametric MRI (mpMRI): pre-biopsy — PI-RADS score 1–5 (≥3 warrants biopsy). PSMA PET-CT: superior staging vs. conventional imaging for biochemical recurrence."
    ),
    "centor": _ss(
        "Centor / McIsaac score — probability of group A streptococcal pharyngitis",
        "Tonsillar exudate or swelling +1 · Tender, swollen anterior cervical nodes +1 · Fever >38°C +1 · Absence of cough +1 · McIsaac age modifier: 3–14 y +1, 15–44 y 0, ≥45 y −1",
        "0–1: no testing or antibiotics · 2–3: rapid antigen test — treat if positive · ≥4: test (some guidelines allow empiric treatment). Children with a negative rapid test → throat culture",
        "Confirmed strep: penicillin V or amoxicillin for 10 days (cephalexin or azithromycin if allergic) — prevents rheumatic fever, not post-streptococcal glomerulonephritis. Cough, runny nose, conjunctivitis or mouth ulcers point to a virus."
    ),
    "perc": _ss(
        "Pulmonary Embolism Rule-out Criteria — exclude PE without any testing in LOW pretest-probability patients",
        "Age <50 · HR <100 · SaO2 ≥95% on room air · No hemoptysis · No estrogen use · No previous DVT/PE · No one-sided leg swelling · No surgery or trauma needing hospitalization in the past 4 weeks",
        "All 8 met + clinician gestalt of low probability (<15%) → PE ruled out, no D-dimer needed · Any criterion positive → D-dimer (or a Wells-based pathway)",
        "Use PERC only when pretest probability is already low; not validated for high-risk or hospitalized patients. An age-adjusted D-dimer cut-off (age × 10 µg/L) after age 50 reduces unnecessary CT scans."
    ),
    "ciwa-ar": _ss(
        "Clinical Institute Withdrawal Assessment for Alcohol, revised — severity of alcohol withdrawal",
        "10 items: nausea/vomiting, tremor, sweating, anxiety, agitation, tactile, auditory and visual disturbances, headache (0–7 each), orientation/clouded sensorium (0–4); maximum 67",
        "<8–10: minimal (usually no medication) · 8/10–15: moderate · >15–20: severe — risk of seizures and delirium tremens; guides symptom-triggered benzodiazepine dosing",
        "Needs a patient who can communicate (not for intubated or delirious patients). Timeline: tremor and anxiety 6–24 h, seizures and hallucinosis 12–48 h, delirium tremens 48–96 h. Give thiamine before glucose; benzodiazepines are first line (lorazepam or oxazepam in liver disease); phenobarbital for refractory withdrawal."
    ),
    "canadian ct head rule": _ss(
        "Canadian CT Head Rule — who needs CT after minor head injury (GCS 13–15 with witnessed loss of consciousness, amnesia or disorientation)",
        "High risk (need for neurosurgery): GCS <15 at 2 h · suspected open or depressed skull fracture · any sign of basal skull fracture (hemotympanum, raccoon eyes, Battle sign, CSF leak from ear or nose) · ≥2 episodes of vomiting · age ≥65. Medium risk (brain injury on CT): amnesia for ≥30 min before impact · dangerous mechanism (pedestrian struck, ejection, fall from >3 ft or 5 stairs)",
        "Any high- or medium-risk factor → CT head · None → CT not needed (sensitivity ~100% for lesions needing neurosurgery)",
        "Does not apply to anticoagulated patients, seizures after injury, age <16 or GCS <13 — they need CT. Use PECARN rules for children."
    ),
    "nexus": _ss(
        "NEXUS criteria — whether to image the cervical spine after blunt trauma",
        "Imaging NOT needed only if ALL are present: no posterior midline cervical tenderness · no focal neurologic deficit · normal alertness · no intoxication · no painful distracting injury",
        "All 5 met → no imaging · Any one absent → CT cervical spine (preferred over X-ray in adults)",
        "The Canadian C-spine rule is more specific (high-risk factors: age ≥65, dangerous mechanism, limb paresthesias; then can the patient rotate the neck 45° each way?). Keep spinal motion restriction until the spine is cleared."
    ),
    # ── OB/GYN & breast ──
    'edinburgh postnatal depression scale': _ss(
        'Screen for perinatal (postpartum and antenatal) depression',
        '10 self-report items on the past 7 days (mood, anhedonia, self-blame, anxiety, panic, coping, sleep, sadness, crying, SELF-HARM — item 10), each scored 0–3',
        'Total 0–30 · ≥10 possible depression · ≥13 probable major depression (common cutoff) · ANY positive answer to item 10 → same-day safety assessment',
        'Screen at least once in pregnancy and postpartum (ACOG), and at well-baby visits at 1, 2, 4 and 6 months (AAP). A screen is not a diagnosis — confirm with a clinical interview.',
    ),
    'biophysical profile': _ss(
        'Assess fetal well-being (antepartum testing) in high-risk pregnancies',
        '5 components, 2 points each (0 if absent) within 30 min: NST reactive · fetal BREATHING (≥1 episode ≥30 s) · gross body MOVEMENT (≥3) · fetal TONE (≥1 extension-flexion) · AMNIOTIC FLUID (deepest pocket >2 cm)',
        '8–10 normal (repeat per indication) · 6 equivocal (deliver if ≥37 weeks; repeat in 24 h if preterm) · ≤4 abnormal → usually deliver · oligohydramnios alone warrants evaluation regardless of score',
        'MODIFIED BPP = NST + amniotic fluid index (most commonly used). Acute markers (NST, breathing, movement, tone) reflect current CNS oxygenation; amniotic fluid reflects chronic placental function.',
    ),
    'amsel criteria': _ss(
        'Clinical diagnosis of bacterial vaginosis',
        '1) Thin, homogeneous, gray-white discharge · 2) Vaginal pH >4.5 · 3) Positive whiff (amine) test with 10% KOH · 4) Clue cells >20% of epithelial cells on saline wet mount',
        '≥3 of 4 = bacterial vaginosis',
        'Gram stain Nugent score (7–10 = BV) is the laboratory gold standard; NAAT panels are increasingly used.',
    ),
    'ferriman-gallwey score': _ss(
        'Quantify hirsutism (terminal hair growth in androgen-dependent areas)',
        '9 body areas (upper lip, chin, chest, upper and lower abdomen, upper and lower back, arm, thigh), each scored 0 (none) to 4 (frank virilization)',
        'Total ≥4–6 (population dependent; ≥8 classic) = hirsutism',
        'Hirsutism + irregular menses → PCOS most likely, but check total testosterone, 17-OHP, TSH and prolactin; rapid progression → tumor workup.',
    ),
    'bi-rads': _ss(
        'Standardized reporting category for breast imaging (mammogram, ultrasound, MRI)',
        '0 incomplete — needs more imaging · 1 negative · 2 benign · 3 probably benign (≤2% malignant) · 4 suspicious (4A/4B/4C: 2–95%) · 5 highly suggestive of malignancy (≥95%) · 6 biopsy-proven cancer',
        '0 → additional views/ultrasound · 1–2 → routine screening · 3 → short-interval follow-up imaging at 6 months · 4–5 → biopsy (core needle) · 6 → treatment',
        'A palpable mass with a BI-RADS 1–2 mammogram still needs ultrasound ± biopsy — imaging does not override a suspicious exam.',
    ),
    'gail model': _ss(
        "Estimate a woman's 5-year and lifetime risk of invasive breast cancer (NCI Breast Cancer Risk Assessment Tool)",
        'Age, age at menarche, age at first live birth, number of first-degree relatives with breast cancer, number of prior breast biopsies and atypical hyperplasia, race/ethnicity',
        '5-year risk ≥1.67% (or ≥3% per USPSTF threshold for benefit) → discuss risk-reducing medication (tamoxifen, raloxifene, aromatase inhibitors)',
        'Not for women with BRCA mutations, prior breast cancer, LCIS or chest radiation — use genetic models (Tyrer-Cuzick/IBIS) for strong family histories.',
    ),
    'pop-q': _ss(
        'Pelvic Organ Prolapse Quantification system — standardized staging of prolapse',
        'Measures 6 vaginal points (Aa, Ba, C, D, Ap, Bp) relative to the HYMEN during maximal Valsalva, plus genital hiatus, perineal body and total vaginal length',
        'Stage 0 none · I most distal point >1 cm above hymen · II within 1 cm above/below hymen · III >1 cm beyond hymen but not complete · IV complete eversion (procidentia)',
        'Symptoms (not stage) drive treatment — asymptomatic stage II needs no intervention.',
    ),
    # ── Primary care screening ──
    'audit-c': _ss(
        'Screen for unhealthy alcohol use (USPSTF — screen all adults)',
        "3 questions (0–4 each): How often do you have a drink containing alcohol? How many drinks on a typical day when drinking? How often do you have ≥6 drinks (men) / ≥4 (women and older adults) on one occasion? Single-question screen: 'How many times in the past year have you had ≥5 (men) / ≥4 (women) drinks in a day?' (≥1 = positive)",
        'Total 0–12 · positive ≥4 in men, ≥3 in women (higher scores = greater risk) → brief intervention (FRAMES), assess for alcohol use disorder (DSM-5), offer treatment (naltrexone, acamprosate, topiramate, gabapentin)',
        'Low-risk drinking limits: ≤2 drinks/day men, ≤1/day women; no alcohol in pregnancy. CAGE is less sensitive for at-risk (non-dependent) drinking.',
    ),
    'gad-7': _ss(
        'Screen for and grade severity of generalized anxiety disorder (also panic, social anxiety, PTSD)',
        "7 items over the past 2 weeks (0 not at all – 3 nearly every day): nervous/anxious, can't stop worrying, worrying too much, trouble relaxing, restless, irritable, afraid something awful might happen",
        '0–4 minimal · 5–9 mild · 10–14 moderate · 15–21 severe; ≥10 positive screen → clinical evaluation',
        'USPSTF recommends anxiety screening in adults <65 (including pregnant/postpartum) and children 8–18.',
    ),
    'epworth sleepiness scale': _ss(
        'Quantify daytime sleepiness (OSA, narcolepsy, insufficient sleep)',
        'Chance of dozing (0–3) in 8 situations: reading, watching TV, sitting inactive in public, passenger in a car for 1 h, lying down in the afternoon, sitting and talking, sitting quietly after lunch without alcohol, in a car stopped in traffic',
        '0–10 normal · 11–12 mild · 13–15 moderate · 16–24 severe excessive daytime sleepiness',
        'Sleepiness ≠ fatigue; high scores in a driver warrant counseling about drowsy driving.',
    ),
    'stop-bang': _ss(
        'Screen for obstructive sleep apnea (often preoperatively)',
        'Snoring loudly · Tired/sleepy during day · Observed apneas · high blood Pressure · BMI >35 · Age >50 · Neck circumference >40 cm (16 in) · male Gender — 1 point each',
        '0–2 low risk · 3–4 intermediate · 5–8 high risk of moderate-severe OSA → polysomnography (or home sleep test)',
        'High-risk OSA patients need perioperative precautions (opioid-sparing analgesia, CPAP, monitoring).',
    ),
    'frax': _ss(
        'Estimate 10-year probability of hip fracture and major osteoporotic fracture',
        'Age, sex, BMI, prior fragility fracture, parental hip fracture, current smoking, glucocorticoids (≥3 months ≥5 mg prednisone), rheumatoid arthritis, secondary osteoporosis, alcohol ≥3 units/day ± femoral neck BMD',
        'Treat (US NOF/BHOF thresholds) if osteopenia (T-score −1 to −2.5) with 10-year risk of HIP fracture ≥3% or MAJOR osteoporotic fracture ≥20%; also treat T-score ≤−2.5 or any hip/vertebral fragility fracture regardless of FRAX',
        'DEXA screening: all women ≥65 and younger postmenopausal women at increased risk (FRAX or OST); men insufficient evidence (USPSTF).',
    ),
    'mini-cog': _ss(
        'Brief screen for cognitive impairment (~3 min)',
        '3-word registration and recall (1 point per word) + CLOCK DRAWING (normal = 2 points: all numbers in correct position and hands pointing to the requested time)',
        'Total 0–5 · 0–2 positive screen (possible dementia) → further evaluation (MoCA/MMSE, labs — B12, TSH; imaging) · 3–5 negative (some use <4)',
        'MoCA (<26 abnormal) is more sensitive than MMSE for mild cognitive impairment; adjust for education.',
    ),
    'ascvd risk calculator': _ss(
        'Estimate 10-year risk of atherosclerotic cardiovascular disease (Pooled Cohort Equations; AHA PREVENT 2023 is the newer race-free equation including CKD and adds heart failure risk)',
        'Age 40–79, sex, race (PCE), total cholesterol, HDL, systolic BP, treated hypertension, diabetes, smoking (PREVENT adds eGFR, BMI, statin use, ± HbA1c, UACR, social deprivation)',
        '<5% low · 5–7.4% borderline · 7.5–19.9% intermediate (statin with shared decision; risk enhancers/coronary calcium score help) · ≥20% high (high-intensity statin). Not for patients with clinical ASCVD, LDL ≥190, or diabetes 40–75 (they already qualify)',
        'Coronary artery calcium score of 0 (non-smoker, intermediate risk) favors deferring statin; CAC ≥100 favors treatment.',
    ),
    'phq-2': _ss(
        'Two-question screen for depression',
        'Over the past 2 weeks, how often bothered by: (1) little interest or pleasure in doing things; (2) feeling down, depressed or hopeless — each 0–3',
        "Score ≥3 (or any 'yes' on the yes/no version) → full PHQ-9 and clinical interview",
        'USPSTF: screen all adults (and adolescents 12–18) for depression with adequate follow-up systems.',
    ),
}

_SCORE_ALIASES = {
    "abcd2 score": "abcd2",
    "alvarado score": "alvarado",
    "apache 2": "apache ii",
    "apache2": "apache ii",
    "apgar score": "apgar",
    "bisap score": "bisap",
    "bishop score": "bishop",
    "breslow thickness": "breslow",
    "cage questionnaire": "cage",
    "cha2ds2vasc": "cha2ds2-vasc",
    "chads2": "cha2ds2-vasc",
    "child pugh": "child-pugh",
    "child-pugh score": "child-pugh",
    "gleason score": "gleason",
    "grace": "grace score",
    "has bled": "has-bled",
    "hasbled": "has-bled",
    "heart": "heart score",
    "killip class": "killip",
    "mascc score": "mascc",
    "meld score": "meld",
    "news score": "news",
    "nih stroke scale": "nihss",
    "nih stroke score": "nihss",
    "nyha class": "nyha",
    "pecarn rule": "pecarn",
    "phq 9": "phq-9",
    "phq9": "phq-9",
    "qsofa score": "qsofa",
    "quick sofa": "qsofa",
    "ranson criteria": "ranson",
    "rcri score": "rcri",
    "rockall score": "rockall",
    "sofa score": "sofa",
    "timi score": "timi",
    "wells": "wells score",
    "centor score": "centor", "centor criteria": "centor", "mcisaac score": "centor",
    "modified centor": "centor", "modified centor score": "centor",
    "perc rule": "perc", "perc criteria": "perc",
    "ciwa": "ciwa-ar", "ciwa score": "ciwa-ar", "ciwa protocol": "ciwa-ar",
    "canadian head ct rule": "canadian ct head rule", "ct head rule": "canadian ct head rule",
    "nexus criteria": "nexus", "canadian c-spine rule": "nexus", "canadian c spine rule": "nexus",
    'epds': 'edinburgh postnatal depression scale',
    'edinburgh depression scale': 'edinburgh postnatal depression scale',
    'edinburgh postpartum depression scale': 'edinburgh postnatal depression scale',
    'bpp': 'biophysical profile',
    'modified biophysical profile': 'biophysical profile',
    'modified bpp': 'biophysical profile',
    "amsel's criteria": 'amsel criteria',
    'ferriman gallwey': 'ferriman-gallwey score',
    'ferriman-gallwey': 'ferriman-gallwey score',
    'birads': 'bi-rads',
    'bi rads': 'bi-rads',
    'gail score': 'gail model',
    'pop q': 'pop-q',
    'popq': 'pop-q',
    'audit c': 'audit-c',
    'alcohol screening': 'audit-c',
    'alcohol use screening': 'audit-c',
    'gad7': 'gad-7',
    'gad 7': 'gad-7',
    'ess': 'epworth sleepiness scale',
    'epworth': 'epworth sleepiness scale',
    'stop bang': 'stop-bang',
    'stopbang': 'stop-bang',
    'frax score': 'frax',
    'frax tool': 'frax',
    'minicog': 'mini-cog',
    'mini cog': 'mini-cog',
    'pooled cohort equations': 'ascvd risk calculator',
    'ascvd risk score': 'ascvd risk calculator',
    'prevent equations': 'ascvd risk calculator',
    '10-year ascvd risk': 'ascvd risk calculator',
    'phq2': 'phq-2',
    'phq 2': 'phq-2',
}
