"""Individual drugs and brand names (tier 0.5).

Edit freely — see data/__init__.py for how files are loaded."""
from ..formatters import _dr


_DRUGS = {
    # ── Beta-blockers ─────────────────────────────────────────────────────
    "metoprolol": _dr(
        "Selective beta-1 blocker (cardioselective at low-moderate doses; loses selectivity at high doses). Reduces HR, contractility, and renin release via beta-1 blockade.",
        "HTN, angina, ACS, HFrEF (metoprolol SUCCINATE — MERIT-HF: 34% mortality reduction), rate control in AF/flutter, migraine prophylaxis, essential tremor, thyrotoxicosis (symptom control).",
        "Bradycardia, AV block, fatigue, erectile dysfunction, bronchospasm at high doses (beta-2 spillover — use with caution in asthma/COPD), hypoglycemia masking (blunts tachycardia but NOT diaphoresis — cholinergic). Abrupt withdrawal → rebound HTN + angina.",
        "Metoprolol TARTRATE (immediate release — BID dosing) vs. SUCCINATE (extended release — once daily — the one with mortality benefit in HFrEF — MERIT-HF trial). Three BBs with HFrEF mortality benefit: Carvedilol, Metoprolol succinate, Bisoprolol (CoMeB). Cardioselective BBs: Metoprolol, Atenolol, Bisoprolol, Esmolol (MABE). BB must be started low and titrated slowly in HFrEF (initially may worsen HF)."
    ),
    "carvedilol": _dr(
        "Non-selective beta-1 + beta-2 blocker + alpha-1 blocker (beta:alpha-1 blockade ratio ~10:1 — labetalol is the one with 3:1 oral / 7:1 IV). Alpha-1 blockade adds peripheral vasodilation reducing afterload.",
        "HFrEF (US Carvedilol HF program, COPERNICUS — mortality benefit), post-MI LV dysfunction, HTN (with concurrent tachycardia or high-output state).",
        "Hypotension (alpha-1 blockade — orthostatic), bradycardia, dizziness, weight gain, worsening glycemic control (especially in T2DM — masks hypoglycemia symptoms), bronchospasm.",
        "One of 3 BBs with proven HFrEF mortality benefit (Carvedilol, Metoprolol succinate, Bisoprolol). Unlike selective BBs, carvedilol's alpha-1 blockade provides additional afterload reduction — preferred in HFrEF with HTN. Non-selective BBs contraindicated in asthma — carvedilol should be avoided in reactive airway disease. BBs + CCBs (diltiazem/verapamil): AVOID combination — additive AV block and negative inotropy."
    ),
    "propranolol": _dr(
        "Non-selective beta-1 + beta-2 blocker. Also inhibits peripheral T4→T3 conversion (deiodinase inhibition) and decreases renin. Highly lipid-soluble (crosses BBB — CNS effects).",
        "HTN, angina, migraine prophylaxis, essential tremor, performance anxiety (situational — stage fright), thyrotoxicosis + thyroid storm (blocks sympathomimetic effects + T4→T3 conversion), portal HTN variceal prophylaxis (non-selective BBs reduce portal pressure), pheochromocytoma (ONLY AFTER alpha-blockade established).",
        "Bronchospasm (CONTRAINDICATED in asthma/COPD — beta-2 blockade), bradycardia, AV block, peripheral vasoconstriction, hypoglycemia masking, fatigue, vivid dreams/nightmares (CNS penetration), impotence, hypertriglyceridemia.",
        "NEVER give beta-blocker before alpha-blocker in pheochromocytoma — unopposed alpha-1 stimulation causes hypertensive crisis. Propranolol unique: inhibits peripheral T4→T3 conversion (useful in thyroid storm alongside PTU). Portal HTN: non-selective BBs (propranolol, nadolol, carvedilol) reduce portal pressure by ↓CO (beta-1) + splanchnic vasoconstriction (beta-2 blockade → unchecked alpha-1 → ↓splanchnic blood flow). Rebound angina/HTN: must taper over 1-2 weeks."
    ),
    "labetalol": _dr(
        "Combined alpha-1 blocker + non-selective beta-1+2 blocker (ratio 1:3 alpha:beta oral; 1:7 IV). Results in vasodilation (alpha-1) + reduced HR/contractility (beta) without reflex tachycardia.",
        "Hypertensive emergency (IV — drug of choice in pregnancy-related HTN urgency/emergency), HTN in pregnancy (safe — one of preferred agents with hydralazine and nifedipine), aortic dissection (combined HR + BP reduction without reflex tachycardia).",
        "Orthostatic hypotension, paradoxical pressor response (rare), hepatotoxicity (chronic oral — rare), bronchospasm (non-selective beta component — avoid in asthma), scalp tingling/burning (common, benign), neonatal bradycardia if given close to delivery.",
        "Key advantage over pure vasodilators in aortic dissection: reduces both rate of pressure rise (dp/dt) and mean pressure simultaneously without reflex tachycardia. SAFE in pregnancy (unlike most antihypertensives — ACEi/ARBs teratogenic). IV labetalol: onset 5 min, peak 10 min, duration 3-6h. Maternal beta-blockade can cause neonatal bradycardia, hypoglycemia — monitor newborn."
    ),
    "esmolol": _dr(
        "Cardioselective (beta-1) ultra-short-acting IV beta-blocker. Hydrolyzed by red blood cell esterases → half-life ~9 min. Must be given as IV infusion (bolus + maintenance).",
        "Acute rate control in SVT/AF/flutter, perioperative HTN and tachycardia, aortic dissection (rate control as bridge to BP control), thyroid storm, acute MI with tachycardia.",
        "Hypotension, bradycardia, AV block, bronchospasm (less than non-selective BBs at standard doses), injection-site phlebitis (concentrated solution — use central line if possible).",
        "Half-life ~9 min makes esmolol ideal when rapid titration or reversal needed (hemodynamic instability — if bradycardia/hypotension develops, stopping infusion reverses effect rapidly). Aortic dissection protocol: esmolol infusion to target HR <60 bpm BEFORE adding nitroprusside (prevent reflex tachycardia from nitroprusside which ↑dp/dt — dangerous in dissection). Dosing: 500 mcg/kg loading bolus over 1 min → 50-200 mcg/kg/min infusion."
    ),
    # ── ACE Inhibitors ────────────────────────────────────────────────────
    "lisinopril": _dr(
        "ACE inhibitor — blocks conversion of Angiotensin I → Angiotensin II by ACE. Also prevents bradykinin degradation (↑bradykinin levels → vasodilation + cough + angioedema). Reduces efferent arteriolar tone → ↓intraglomerular pressure → nephroprotective.",
        "HTN (first-line), HFrEF (mortality benefit — CONSENSUS/SOLVD trials), post-MI LV dysfunction (start within 24h if no CI), CKD with proteinuria (reduces progression), diabetic nephropathy (ACEi/ARB preferred regardless of BP to reduce proteinuria).",
        "Dry cough (10-15% — bradykinin accumulation; switch to ARB), angioedema (rare 0.1-0.5% — bradykinin-mediated; life-threatening; CONTRAINDICATED thereafter — switching to an ARB carries a small (<10%) risk of recurrent angioedema), hyperkalemia (↓aldosterone → K+ retention), AKI (especially bilateral renal artery stenosis — ↓efferent tone → ↓GFR → acute Cr rise). CONTRAINDICATED: pregnancy (fetal renal agenesis, oligohydramnios, skull hypoplasia — FDA boxed warning for fetal toxicity), prior ACEi angioedema, hyperkalemia, bilateral RAS.",
        "ACEi cough: affects 10-15% of patients (higher in Asian populations — up to 30-40%). Mechanism: ↑bradykinin + substance P in airways → sensory nerve stimulation → dry, tickling cough. SWITCH TO ARB (no cough — bradykinin not affected). Acceptable Cr rise after starting ACEi: up to 30% above baseline (expected — ↓efferent tone → ↓GFR). STOP if Cr rises >50% or K+ >5.5. ACEi + ARB combination: NOT recommended (ONTARGET trial — no added benefit + ↑AKI + ↑hyperkalemia)."
    ),
    "captopril": _dr(
        "ACE inhibitor (sulfhydryl-containing — unique among ACEi — responsible for some unique adverse effects). Short half-life requires 2-3x daily dosing.",
        "HTN, HFrEF, post-MI, scleroderma renal crisis (DRUG OF CHOICE — ACEi rapidly lower BP and improve renal function in scleroderma crisis — even with Cr elevation), CKD with proteinuria.",
        "Dry cough (same as all ACEi — bradykinin), angioedema, hyperkalemia, AKI. UNIQUE TO CAPTOPRIL (sulfhydryl group): taste disturbance (dysgeusia — metallic taste), proteinuria/membranous nephropathy at high doses, leukopenia/neutropenia (rare), rash.",
        "Scleroderma renal crisis: captopril is DRUG OF CHOICE (dramatically reversed historical 1-year mortality from >85% to ~25%). ACEi should be continued even if Cr worsens in scleroderma renal crisis (unlike standard renal failure where ACEi held — in scleroderma, ACEi are therapeutic). Short half-life is a disadvantage vs. longer-acting ACEi (lisinopril, ramipril, enalapril) for chronic HTN and HFrEF."
    ),
    # ── ARBs ──────────────────────────────────────────────────────────────
    "losartan": _dr(
        "ARB — directly blocks AT1 receptor (angiotensin II type 1) → prevents all Ang II effects (vasoconstriction, aldosterone release, remodeling). Does NOT affect bradykinin degradation (ACE still active) → no cough, very rare angioedema. UNIQUE: also has uricosuric effect (blocks URAT1 tubular urate transporter → ↑uric acid excretion).",
        "HTN (especially if ACEi intolerance — cough), HFrEF (CHARM trial — if ACEi intolerant), diabetic nephropathy in T2DM (RENAAL trial — ↓renal progression), stroke prevention in HTN + LVH (LIFE trial), gout + HTN (uricosuric — ↓serum urate).",
        "Hyperkalemia (↓aldosterone), AKI (same mechanism as ACEi — ↓efferent tone), hypotension. CONTRAINDICATED: pregnancy (same as ACEi — fetal renal toxicity), hyperkalemia, bilateral RAS. Angioedema: very rare (but ~10% of ACEi angioedema patients cross-react — use with caution).",
        "LIFE trial: losartan vs. atenolol in HTN + LVH → losartan superior (↓stroke, ↓new-onset DM). RENAAL trial: losartan vs. placebo in T2DM + nephropathy → losartan ↓ESRD + ↓doubling of Cr. Losartan ONLY uricosuric ARB — useful in gout + HTN combination. ARBs end in '-sartan' (losartan, valsartan, irbesartan, olmesartan, candesartan, telmisartan). ACEi vs ARB: identical indications/CI except ACEi causes cough/angioedema (bradykinin), ARB does not."
    ),
    # ── Calcium Channel Blockers ──────────────────────────────────────────
    "amlodipine": _dr(
        "Dihydropyridine (DHP) CCB — selectively blocks L-type Ca2+ channels in vascular smooth muscle >> cardiac muscle → arterial vasodilation → ↓SVR → ↓afterload. Long half-life (30-50h) allows once-daily dosing and gradual onset (low rate of reflex tachycardia vs. short-acting nifedipine).",
        "HTN (first-line — especially African Americans and elderly; ALLHAT: CCB non-inferior to thiazide for most outcomes; ACCOMPLISH: amlodipine + ACEi superior to HCTZ + ACEi for CV events), stable angina (↓afterload + ↑coronary blood flow via vasodilation), vasospastic/Prinzmetal angina, Raynaud phenomenon.",
        "Peripheral ankle edema (dose-dependent — arteriolar dilation + capillary hydrostatic pressure increase; NOT fluid retention — diuretics unhelpful; adding ACEi reduces edema), flushing, headache, gingival hyperplasia, reflex tachycardia (less than nifedipine — long half-life). NOT negatively inotropic — SAFE in HFrEF.",
        "ACCOMPLISH trial: amlodipine + benazepril (ACEi) > HCTZ + benazepril for CV events in high-risk HTN. DHP CCBs safe in HFrEF (no negative inotropy) unlike non-DHP CCBs (diltiazem, verapamil — CONTRAINDICATED in HFrEF). Short-acting nifedipine: avoid in HTN (reflex tachycardia, ↑MI risk). AVOID ALL CCBs in pre-excited AF (WPW) — slows AV node → forces conduction via accessory pathway → VF."
    ),
    "diltiazem": _dr(
        "Non-DHP CCB (benzothiazepine) — blocks L-type Ca2+ channels in cardiac conduction system AND vascular smooth muscle → slows SA node + AV node conduction + ↓contractility + vasodilation. Rate-lowering effect comparable to beta-blockers.",
        "AF/flutter rate control (IV: 0.25 mg/kg bolus then infusion — preferred when beta-blockers contraindicated, e.g., COPD/asthma), stable angina, vasospastic angina, PSVT termination (IV), HTN. SAFE in most COPD/asthma patients (unlike beta-blockers).",
        "Bradycardia, AV block (1st-3rd degree), hypotension, constipation, peripheral edema (less than DHP CCBs), negative inotrope — CONTRAINDICATED in HFrEF (EF <40%), CONTRAINDICATED in pre-excited AF/flutter (WPW) — may accelerate ventricular rate via accessory pathway → VF.",
        "AVOID diltiazem (and verapamil) + beta-blockers simultaneously — additive AV block → complete heart block risk. CONTRAINDICATED in HFrEF (↓contractility worsens pump function — use amlodipine instead). Diltiazem + digoxin: additive bradycardia, ↑digoxin levels (CYP3A4 inhibition). Vasospastic angina + cocaine use: CCBs are preferred (cocaine → coronary vasospasm; beta-blockers → unopposed alpha → ↑vasospasm)."
    ),
    "verapamil": _dr(
        "Non-DHP CCB (phenylalkylamine) — most potent AV nodal blocking of all CCBs. Blocks Ca2+ channels in heart >> vessels → ↓SA automaticity, ↓AV conduction velocity, ↓contractility, some coronary vasodilation.",
        "AF/flutter rate control, PSVT termination (IV), SVT prophylaxis, stable + vasospastic angina, hypertrophic obstructive cardiomyopathy (HOCM — ↓outflow obstruction by ↓contractility + HR), cluster headache prophylaxis, migraine prevention, idiopathic left ventricular VT (Belhassen VT — verapamil-sensitive).",
        "Constipation (MOST COMMON adverse effect — Ca2+ required for GI smooth muscle; more constipating than diltiazem), bradycardia, AV block, hypotension, edema, negative inotrope — CONTRAINDICATED in HFrEF, CONTRAINDICATED in WPW + AF (same reason as diltiazem — → VF).",
        "Verapamil most constipating CCB (Ca2+ critical for intestinal peristalsis). Verapamil-sensitive VT: fascicular VT (left posterior fascicle origin — RBBB + left axis deviation morphology) — rare, responds dramatically to verapamil (vs. most VT which needs amiodarone/procainamide). Verapamil + digoxin: ↑digoxin toxicity (↓digoxin clearance + additive AV block). Idiopathic HOCM: verapamil (or beta-blocker) — reduce outflow gradient."
    ),
    # ── Diuretics ─────────────────────────────────────────────────────────
    "furosemide": _dr(
        "Loop diuretic — inhibits NKCC2 (Na+/K+/2Cl- cotransporter) in thick ascending limb of loop of Henle → ↑excretion of Na+, K+, Cl-, Ca2+, Mg2+. Disrupts medullary concentration gradient → impairs ADH-mediated water reabsorption. Highest diuretic ceiling of any class.",
        "Acute decompensated HF (pulmonary edema — IV push), chronic HF edema, cirrhotic ascites (with spironolactone 5:2 ratio — spiro 100:furo 40), nephrotic syndrome edema, resistant HTN (when eGFR <30 — thiazides lose efficacy), hypercalcemia (IV furosemide + aggressive NS hydration → ↑urinary Ca2+ excretion).",
        "Hypokalemia (MOST COMMON — ↑distal K+ delivery → ↑aldosterone-driven K+ secretion), hypomagnesemia, hypocalcemia (urinary Ca2+ wasting — opposite of thiazides), hyponatremia, hypochloremic metabolic alkalosis (contraction alkalosis), hyperuricemia (gout), OTOTOXICITY (high-dose IV or rapid infusion — especially combined with aminoglycosides — sensorineural hearing loss), prerenal azotemia, sulfonamide allergy (cross-reactivity).",
        "Loops LOSE Ca2+; Thiazides RETAIN Ca2+. Furosemide resistance in severe HF: poor oral bioavailability (GI edema), ↑tubular secretion competition (↑organic acid in uremia competes for transport). Solutions: IV furosemide, higher doses, or add metolazone (blocks NCC in DCT — sequential nephron blockade — synergistic diuresis). Ototoxicity: rate-dependent with IV furosemide (use infusion <4 mg/min; avoid in patients on cisplatin or aminoglycosides). Torsemide + bumetanide: better oral bioavailability in HF."
    ),
    "hydrochlorothiazide": _dr(
        "Thiazide diuretic — inhibits Na+/Cl- cotransporter (NCC) in distal convoluted tubule → ↑Na+ and Cl- excretion. Unique: ↑Ca2+ reabsorption (activates apical Ca2+ channels + basolateral NCX). Paradoxical ↓urine output in nephrogenic DI (volume depletion → ↑proximal reabsorption → ↓collecting duct delivery).",
        "HTN (first-line — ALLHAT trial; most effective in African Americans + elderly; combined with ACEi/ARB or CCB), nephrolithiasis due to hypercalciuria (↑tubular Ca2+ reabsorption → ↓urinary Ca2+), osteoporosis (↑Ca2+ retention), nephrogenic DI (reduces urine output paradoxically — volume contraction ↑proximal reabsorption).",
        "Hypokalemia (↑distal K+ secretion), hyperuricemia (↓urate excretion → gout), hyperglycemia (↓insulin secretion — impairs K+-dependent glucose-stimulated insulin release), hyperlipidemia (↑LDL, TG), hyponatremia (MOST DANGEROUS — dilutional; thiazides cause more hyponatremia than loop diuretics — collect duct still responds to ADH), hypercalcemia (↑Ca2+ reabsorption), photosensitivity, sulfonamide allergy cross-reactivity.",
        "5 H's of thiazide toxicity: Hypokalemia, Hyperglycemia, Hyperlipidemia, Hyperuricemia, Hypercalcemia. Chlorthalidone preferred over HCTZ (longer t1/2 24-72h vs. 6-12h — greater BP reduction — ALLHAT used chlorthalidone). HCTZ ineffective when eGFR <30 (inadequate delivery to NCC). Thiazide + loop diuretic = synergistic sequential nephron blockade (add thiazide/metolazone to loop for refractory edema). Thiazide ONLY diuretic that causes hypercalcemia (all others cause hypocalcemia or no effect)."
    ),
    "spironolactone": _dr(
        "Aldosterone receptor antagonist (MRA) — competitive antagonist at mineralocorticoid receptor in cortical collecting duct → ↓ENaC and Na+/K+-ATPase expression → Na+ excretion + K+ retention. Also weak androgen receptor antagonist (anti-androgenic effects at high doses).",
        "HFrEF (RALES trial — 30% ↓mortality in NYHA class III-IV HFrEF with EF <35%), cirrhotic ascites (FIRST-LINE for ascites management — 100 mg:40 mg spiro:furosemide 5:2 ratio), primary hyperaldosteronism (BAH/bilateral hyperplasia — medical management), resistant HTN (PATHWAY-2 trial — most effective 4th drug after ACEi/ARB + CCB + thiazide), hirsutism/PCOS (anti-androgenic).",
        "Hyperkalemia (MOST SERIOUS — K+-sparing; CONTRAINDICATED if K+ >5.0 or eGFR <30), gynecomastia + sexual dysfunction in men (anti-androgenic: blocks AR + has estrogenic activity), menstrual irregularities, metabolic acidosis (type IV RTA in some), breast tenderness.",
        "RALES trial: spironolactone 25mg/day in NYHA III-IV HFrEF → 30% ↓mortality. EMPHASIS-HF: eplerenone in mild HFrEF. Eplerenone: selective MRA (binds only mineralocorticoid receptor — no anti-androgenic effects → no gynecomastia) — EPHESUS trial (post-MI HFrEF). Spiro 'K+-sparing' but achieves this by blocking aldosterone (diuresis via Na+ excretion + K+ retention). Amiloride/triamterene: K+-sparing diuretics by directly blocking ENaC (not aldosterone-mediated)."
    ),
    # ── Antiarrhythmics ───────────────────────────────────────────────────
    "amiodarone": _dr(
        "Class III antiarrhythmic (K+ channel blocker — ↑action potential duration + QT interval) with additional Class I (Na+ channel), Class II (non-competitive beta-blockade), and Class IV (Ca2+ channel) properties. Contains 37% iodine by weight → thyroid effects. Half-life 40-55 days (longest of any commonly used drug).",
        "Ventricular tachycardia/VF (first-line IV for hemodynamically stable VT; second-line for VF post-defibrillation in ACLS), AF/flutter (rate + rhythm control), SVT; safe in HFrEF (no negative inotropy — dofetilide is the other main option).",
        "PULMONARY TOXICITY (most serious — interstitial pneumonitis → fibrosis; monitor with baseline + annual PFTs/CXR; new dyspnea + a fall in DLCO (>15-20%) suggests early toxicity), THYROID (hypothyroidism most common — iodine load → Wolff-Chaikoff effect; hyperthyroidism — Jod-Basedow; check TFTs q6 months), HEPATOTOXICITY (check LFTs q6 months), CORNEAL MICRODEPOSITS (nearly 100% of patients — usually benign; halos around lights; rarely requires stopping), PHOTOSENSITIVITY + gray-blue slate skin discoloration (chronic), NEUROTOXICITY (peripheral neuropathy, ataxia, tremor, cognitive slowing), QT PROLONGATION (paradoxically less TdP than other Class III agents).",
        "Amiodarone drug interactions: CYP2D6 + CYP3A4 inhibitor → ↑warfarin (reduce dose 30-50%, recheck INR), ↑digoxin (reduce digoxin dose 50%), ↑statins (↑myopathy risk — avoid simvastatin >20mg), ↑cyclosporine. Monitor: baseline TFTs, LFTs, CXR, PFTs, eye exam; then TFTs + LFTs q6 months, CXR annually. ACLS: amiodarone 300 mg IV push for shockable rhythm VF/pulseless VT after 3rd defibrillation, then 150 mg, then 1mg/min infusion. Only antiarrhythmic safe in HFrEF."
    ),
    "digoxin": _dr(
        "Cardiac glycoside — inhibits Na+/K+-ATPase → ↑intracellular Na+ → activates Na+/Ca2+ exchanger (NCX) → ↑intracellular Ca2+ → ↑myocardial contractility (positive inotrope). Vagomimetic: ↑vagal tone → ↓SA node rate + ↓AV conduction (negative chronotrope + dromotrope).",
        "Chronic HFrEF (reduces hospitalizations + improves symptoms — DIG trial — NO mortality benefit; goal serum level 0.5-0.9 ng/mL in HF), rate control in AF/flutter especially with concurrent HFrEF (unique advantage: both inotropic + rate-controlling).",
        "NARROW THERAPEUTIC INDEX (0.5-0.9 ng/mL for HF; >2.0 ng/mL = toxic). Early toxicity: GI symptoms (nausea, vomiting, anorexia — EARLIEST sign), visual disturbances (xanthopsia — yellow-green halos, chromatopsia). Cardiac toxicity: ANY arrhythmia (premature beats most common), bidirectional VT (pathognomonic of toxicity), regularized AF (junctional tachycardia — AV block + junctional rhythm superficially resembles regular AF), complete AV block. Hypokalemia POTENTIATES toxicity (K+ competes with digoxin at Na+/K+-ATPase binding site).",
        "Digoxin toxicity triggers: hypokalemia (MOST COMMON — thiazides/loop diuretics, vomiting, diarrhea), hypomagnesemia, hypothyroidism (↓renal clearance), renal failure (digoxin renally cleared — ↑levels), quinidine + amiodarone + verapamil (↑digoxin levels by 50-100% — reduce digoxin dose). Antidote: Digibind/DigiFab (anti-digoxin Fab fragments) — rapidly reverses all toxicity. Xanthopsia (yellow vision): reportedly caused Van Gogh's 'yellow period' (treated with digitalis-containing foxglove). Rule: if AF suddenly becomes regular on digoxin → suspect toxicity (junctional rhythm)."
    ),
    "lidocaine": _dr(
        "Class Ib antiarrhythmic (Na+ channel blocker) — binds rapidly to activated/inactivated Na+ channels → slows conduction in depolarized/ischemic tissue. Shortens action potential duration (unique among Class I). Fast on/off kinetics. Also: local anesthetic (blocks Na+ channels in peripheral nerves — mechanism of local anesthesia).",
        "Ventricular arrhythmias — acute VT/VF in setting of MI or ischemia (IV — second line after amiodarone in ACLS), ventricular arrhythmia suppression peri-cardiac surgery. Local anesthesia (topical, infiltration, nerve block, epidural — ALL forms of local anesthesia). Neuropathic pain (lidocaine patch — 5% — postherpetic neuralgia, local neuropathy).",
        "CNS toxicity (first at low levels): lightheadedness, tinnitus, circumoral numbness, slurred speech, confusion, seizures. Cardiovascular (at higher levels): myocardial depression, bradycardia, hypotension, cardiac arrest. Local anesthetic systemic toxicity (LAST): IV lipid emulsion (20% intralipid) is antidote. CONTRAINDICATED in: Wolff-Parkinson-White, second- or third-degree AV block without pacemaker, severe SA node disease.",
        "Class Ib agents: Lidocaine, Mexiletine, Tocainide — shorten action potential duration (unlike Ia and Ic). Lidocaine works preferentially in ischemic tissue (rapid on/off — binds more frequently to rapidly firing depolarized cells). Lidocaine 1% vs. 2% (epinephrine): epi causes vasoconstriction → ↑duration of anesthesia + ↓systemic absorption. NEVER use epi-containing lidocaine in digits, penis, ear lobe, nose tip — ischemic necrosis. Local anesthetic toxicity order: CNS first (low threshold) → cardiovascular (high threshold — serious overdose)."
    ),
    "adenosine": _dr(
        "Endogenous purine nucleoside — binds A1 adenosine receptors → activates IK(Ado) K+ channels → hyperpolarizes SA and AV nodes → transiently blocks AV conduction (2-15 seconds). Half-life: 10 seconds (eliminated by erythrocyte adenosine deaminase and cellular uptake).",
        "PSVT termination — DRUG OF CHOICE (terminates AV nodal re-entry tachycardia and AV re-entry via accessory pathway; uncovers atrial flutter waves if mechanism is flutter not SVT), diagnostic tool for wide-complex tachycardia (VT: adenosine usually ineffective; SVT with aberrancy: terminates).",
        "Brief asystole/pause (expected — diagnostic; lasts seconds), chest pain/pressure (40% of patients — transient, caused by coronary vasodilation), dyspnea, flushing, bronchospasm (CONTRAINDICATED in asthma — A1 receptor in bronchial smooth muscle), headache. All effects last <30 seconds (ultra-short half-life).",
        "CRITICAL: NEVER give adenosine in WPW + AF/flutter — blocks AV node → forces all conduction via accessory pathway → rapid ventricular response (300 bpm) → VF. Doses: 6 mg IV rapid peripheral push with flush → if no response 12 mg × 2 doses. Central line: use lower dose (delivered directly to heart). Caffeine/theophylline: adenosine receptor antagonists → BLOCK effects (may need higher dose or use alternative). Dipyridamole (adenosine reuptake inhibitor) → POTENTIATES adenosine (↑risk of prolonged asystole — reduce to 1 mg if patient on dipyridamole)."
    ),
    # ── Anticoagulants ────────────────────────────────────────────────────
    "warfarin": _dr(
        "Vitamin K antagonist (VKA) — inhibits vitamin K epoxide reductase (VKOR) → blocks regeneration of active vitamin K (KH2) → ↓hepatic synthesis of vitamin K-dependent factors: II, VII, IX, X and proteins C and S. Factor VII (half-life 6h) depletes first → PT/INR rises first. Full anticoagulation requires 5-7 days (to deplete all factors). Monitored by PT/INR (therapeutic 2-3 for most indications; 2.5-3.5 for mechanical valves).",
        "AF (especially valvular AF — moderate/severe mitral stenosis — DOACs INADEQUATE, warfarin REQUIRED; mechanical heart valves — only anticoagulant proven safe), DVT/PE (if DOAC unavailable or inappropriate), antiphospholipid syndrome (high-titer antibodies), thrombophilia with recurrent clots.",
        "Bleeding (GI, intracranial), SKIN NECROSIS (3-5 days after starting — protein C and S have shorter half-lives → early warfarin depletes them first → transient hypercoagulability → skin microthrombi; risk ↑in hereditary protein C/S deficiency — BRIDGE WITH HEPARIN until fully anticoagulated), teratogenic (fetal warfarin embryopathy — nasal hypoplasia, stippled epiphyses, CNS malformations — most dangerous 6-9 weeks gestation; avoid in pregnancy → use UFH/LMWH), purple toe syndrome (cholesterol embolization — rare), alopecia.",
        "Interactions: ↑INR — antibiotics (kill gut flora producing vitamin K2 + some inhibit CYP2C9: metronidazole, fluconazole, TMP-SMX, erythromycin), amiodarone (strong CYP2C9 inhibitor — ↑warfarin 30-50%), NSAIDs (↑bleeding, displace protein binding), aspirin. ↓INR — rifampin (strongest CYP inducer — warfarin doses must ↑3-5x), carbamazepine, phenytoin, barbiturates, St John's Wort, ↑vitamin K foods (spinach, kale, broccoli). Reversal: Vit K (phytonadione — slow onset 6-12h) + 4-factor PCC (Kcentra — immediate, preferred over FFP in life-threatening bleeding) ± FFP."
    ),
    "heparin": _dr(
        "Unfractionated heparin (UFH) — binds antithrombin III (ATIII) → conformational change → 1000-fold ↑ATIII inhibition of thrombin (IIa) + Factor Xa (+ IXa, XIa, XIIa). To inactivate thrombin: heparin chain must simultaneously bind ATIII + thrombin (requires ≥18 saccharides). To inactivate Xa: only ATIII binding needed (shorter chains effective). Monitored by aPTT (therapeutic 60-100 sec or 1.5-2.5x control) or anti-Xa level.",
        "DVT/PE treatment + prevention (perioperative, medical inpatients), ACS/pre-PCI anticoagulation (UFH preferred over LMWH for PCI due to titratability), cardiac/vascular surgery (CPB — high dose), bridging anticoagulation (for warfarin interruption in high-risk patients), pregnancy anticoagulation (does NOT cross placenta — SAFE in pregnancy).",
        "Bleeding (major risk), HIT TYPE II (immune — IgG against PF4/heparin complex → platelet activation → THROMBOCYTOPENIA + PARADOXICAL THROMBOSIS; 1-5% of patients, onset day 5-10; STOP ALL HEPARIN IMMEDIATELY including flushes; switch to non-heparin anticoagulant: argatroban, bivalirudin, fondaparinux), HIT Type I (non-immune, mild, benign — no action needed), osteoporosis (long-term use > 3 months), hypoaldosteronism (hyperkalemia).",
        "HIT II: THROMBOTIC complication despite thrombocytopenia (paradox). 4Ts score: Thrombocytopenia >50% fall, Timing 5-10 days, Thrombosis (new), oTher causes unlikely. If HIT suspected: STOP heparin (including LMWH — cross-reactive), transition to argatroban (direct thrombin inhibitor — hepatic clearance; preferred if renal failure) or bivalirudin or fondaparinux. Do NOT give warfarin until platelets recover >150k (protein C depletion risk → limb gangrene). Protamine sulfate: reverses UFH 1:1 (1mg per 100 units UFH given in last 2-4h); partially reverses LMWH."
    ),
    "enoxaparin": _dr(
        "LMWH (low molecular weight heparin) — derived from UFH depolymerization. Mean MW ~4500 Da. Preferentially inhibits Factor Xa (via ATIII) >> thrombin (too short to bridge ATIII-thrombin). More predictable pharmacokinetics than UFH → fixed weight-based SQ dosing (no routine monitoring). Eliminated renally.",
        "DVT/PE prophylaxis (surgical patients — orthopedic, abdominal, gynecologic; medical inpatients) and treatment (preferred over UFH for uncomplicated DVT/PE), NSTEMI/UA (ESSENCE/TIMI 11B: superior to UFH), bridging anticoagulation, cancer-associated thrombosis (historically LMWH; now DOACs preferred per CARAVAGGIO for most cancers).",
        "Bleeding, injection site bruising/hematoma, HIT (MUCH lower risk than UFH — ~0.1% vs. 1-5% — but HIT antibodies can cross-react → switch to non-heparin if HIT diagnosed), osteoporosis (less than UFH), elevated LFTs (transient, benign), ACCUMULATES IN RENAL FAILURE — DOSE REDUCE OR SWITCH TO UFH if CrCl <30.",
        "Monitoring: anti-Xa level needed only in: renal failure, extreme obesity, pregnancy, children. Anti-Xa peak drawn 4h post-SQ dose (therapeutic 0.6-1.0 IU/mL BID dosing; 1.0-2.0 IU/mL for once-daily). Enoxaparin 1mg/kg SQ BID (or 1.5mg/kg once daily) for DVT/PE treatment; 40mg SQ daily (medical prophylaxis) or 30mg BID (orthopedic). Cannot use standard aPTT to monitor (insufficient thrombin inhibition to affect aPTT). Protamine partially reverses LMWH (~60% anti-Xa activity)."
    ),
    "apixaban": _dr(
        "Direct Factor Xa inhibitor (DOAC) — directly and reversibly binds active site of Factor Xa → prevents conversion of prothrombin → thrombin → ↓thrombus formation. Does NOT require ATIII cofactor. Predictable PK: ~27% renal excretion (most renal-safe DOAC), dual hepatic/renal elimination. No routine monitoring needed.",
        "AF stroke prevention (ARISTOTLE trial — superior to warfarin: ↓stroke/SE by 21% + ↓major bleeding by 31% + ↓mortality by 11%), DVT/PE treatment (AMPLIFY — non-inferior efficacy + ↓major bleeding vs. LMWH/warfarin), DVT/PE extended secondary prevention (AMPLIFY-EXT), orthopedic surgery prophylaxis. PREFERRED in elderly + CKD due to lowest renal excretion.",
        "Bleeding (lower rate of major bleeding and ICH vs. warfarin — key advantage over warfarin), no specific antidote initially (andexanet alfa approved 2018 for life-threatening bleeding — expensive, limited availability). No GI symptoms (unlike dabigatran).",
        "ARISTOTLE: apixaban vs. warfarin in AF → superior (↓stroke + ↓bleeding + ↓mortality) — only DOAC to show mortality benefit. Apixaban most preferred in elderly/CKD (27% renal excretion vs. dabigatran 80%). DOAC reversal: andexanet alfa (Xa inhibitors — apixaban, rivaroxaban) or 4-factor PCC empirically. DOACs NEVER in: mechanical heart valves, moderate-severe mitral stenosis (valvular AF) — must use warfarin. DOACs preferred over warfarin in non-valvular AF and most VTE (simpler, no monitoring, ↓ICH). Drug interactions: P-gp + CYP3A4 inhibitors/inducers affect DOACs."
    ),
    "dabigatran": _dr(
        "Direct thrombin inhibitor (DTI, DOAC) — prodrug (dabigatran etexilate) converted by serum esterases to active dabigatran → directly + reversibly binds both free thrombin AND fibrin-bound thrombin. NOT affected by ATIII. ~80% RENAL EXCRETION — major limitation. No CYP metabolism.",
        "AF stroke prevention (RE-LY: 150 mg BID superior to warfarin in stroke prevention; 110 mg BID non-inferior with ↓major bleeding), DVT/PE treatment/prevention (RE-COVER trial), reduced dose (75 mg BID) for AF with CrCl 15-30 (use with extreme caution; CONTRAINDICATED CrCl <15).",
        "GI adverse effects — dyspepsia, abdominal discomfort, GI bleeding ↑ vs warfarin (tartaric acid formulation — take WITH food; consider switching to apixaban/rivaroxaban if GI intolerance), GI bleeding: higher than warfarin (especially 150 mg) though ICH lower than warfarin, ACCUMULATES in renal failure (80% renal clearance — dose adjust or avoid with poor renal function).",
        "UNIQUE specific antidote: IDARUCIZUMAB (Praxbind) — humanized anti-dabigatran monoclonal Ab fragment; reverses dabigatran in minutes (RE-VERSE AD trial). Only DOAC with initial specific reversal agent. Drug interactions: P-gp inhibitors ↑dabigatran (amiodarone, dronedarone, verapamil — use with caution; reduce dose if CrCl 30-50). P-gp inducers ↓dabigatran (rifampin — avoid). RE-ALIGN trial (dabigatran in mechanical heart valves): FAILED — more strokes + bleeds vs. warfarin → DOACs NEVER in mechanical valves."
    ),
    # ── Antiplatelet ──────────────────────────────────────────────────────
    "clopidogrel": _dr(
        "P2Y12 ADP receptor antagonist (antiplatelet) — PRODRUG requiring hepatic CYP2C19 conversion to active thiol metabolite → IRREVERSIBLY alkylates P2Y12 receptor → ↓ADP-stimulated platelet aggregation. Effect persists for platelet lifetime (7-10 days). Hold 5-7 days before elective surgery.",
        "ACS (DAPT with aspirin × 12 months post-ACS and/or stent), secondary stroke/TIA prevention (CAPRIE: clopidogrel alone > aspirin), PAD, elective PCI. Still used when ticagrelor/prasugrel contraindicated (prior stroke/TIA — contraindication for prasugrel; bleeding risk; cost).",
        "Bleeding, TTP (rare 0.02% — STOP immediately; treat with plasmapheresis — similar mechanism to ticlopidine), rash, GI upset. RESISTANCE: CYP2C19 loss-of-function polymorphism (25-30% of patients — especially East Asians) → poor metabolizers → ↓platelet inhibition → ↑stent thrombosis/MACE.",
        "Omeprazole (PPI) + clopidogrel: CYP2C19 competition → ↓clopidogrel activation (FDA warning). Use pantoprazole (less CYP2C19 inhibition) if PPI needed. CYP2C19 genotyping available to identify poor metabolizers → switch to ticagrelor (not affected by CYP2C19). TRITON-TIMI 38: prasugrel > clopidogrel in ACS (↓stent thrombosis/MI) but ↑major bleeding. PLATO: ticagrelor > clopidogrel in ACS (↓CV death/MI/stroke, similar major bleeding). Clopidogrel preferred if: prior stroke/TIA (contraindication to prasugrel), prior intracranial hemorrhage (contraindication to ticagrelor), high bleeding risk, or triple therapy with an anticoagulant. Before CABG hold clopidogrel 5 days, ticagrelor 3-5 days, prasugrel 7 days."
    ),
    "aspirin": _dr(
        "Irreversible COX-1 (and COX-2) inhibitor — acetylates serine residue at COX active site → ↓PGG2/PGH2 → ↓TXA2 (platelet aggregation + vasoconstriction) permanently in platelets (anucleate — cannot synthesize new COX). Antiplatelet effect: low dose 81 mg. Anti-inflammatory/antipyretic/analgesic: higher doses 325-650 mg (COX-2 inhibition → ↓PGE2).",
        "Antiplatelet: ACS (325 mg loading then 81 mg maintenance), secondary prevention of MI/stroke (81 mg), DAPT with P2Y12 inhibitor post-PCI × 12 months. Anti-inflammatory: RA, pericarditis (+ colchicine), Kawasaki disease (high dose: 80-100 mg/kg/day during febrile phase), gout (full anti-inflammatory doses). Antipyretic/analgesic (not first choice — use acetaminophen). Preeclampsia prevention (low dose 81 mg starting 12-16 weeks — ASPRE trial).",
        "GI ulcers/bleeding (inhibits PGE2-mediated gastric mucosal protection — use PPI prophylaxis if high GI risk), Reye syndrome (CHILDREN with viral infections — influenza/VZV → hepatic failure + encephalopathy — CONTRAINDICATED in <16 years with viral illness), aspirin-exacerbated respiratory disease (AERD/Samter triad — asthma + nasal polyps + aspirin sensitivity — COX-1 → ↓PGE2 → ↑leukotrienes → bronchoconstriction), salicylate toxicity (tinnitus, hyperventilation → mixed respiratory alkalosis + metabolic acidosis).",
        "Salicylate poisoning: early = respiratory alkalosis (direct stimulation of medullary respiratory center → hyperventilation → ↓CO2). Late = metabolic acidosis (uncouples oxidative phosphorylation → lactic acid + accumulation of salicylate anion). Treatment: urinary alkalinization with NaHCO3 (pKa 3 → ionizes salicylate in urine → ion trapping prevents tubular reabsorption → ↑excretion) + hemodialysis if severe. Low-dose aspirin RAISES uric acid (inhibits tubular urate secretion — AVOID in gout). When DAPT ends, one antiplatelet (usually aspirin) is continued lifelong."
    ),
    "ticagrelor": _dr(
        "Direct, REVERSIBLE P2Y12 ADP receptor antagonist (cyclopentyl-triazolopyrimidine — not a thienopyridine) — NOT a prodrug (no CYP2C19 conversion needed → effective regardless of CYP2C19 genotype). Faster onset and greater platelet inhibition than clopidogrel. Platelets recover 3-5 days after stopping (shorter surgical hold time). Also inhibits adenosine reuptake (unique — explains some AEs).",
        "ACS (PLATO trial: ticagrelor > clopidogrel — ↓CV death + MI + stroke with similar major bleeding — now preferred in ACS), DAPT with aspirin × 12 months post-ACS/stent. Also: secondary prevention in high-risk stable CAD (lower dose 60 mg BID — PEGASUS-TIMI 54).",
        "Dyspnea (10-15% — transient, mechanism: adenosine reuptake inhibition → ↑adenosine → bronchial constriction + ↑ventilatory drive — usually resolves without stopping drug), bleeding (similar major bleeding to clopidogrel in PLATO), ventricular pauses/bradycardia (first weeks — adenosine-mediated — usually brief, self-limited; monitor first week in bradycardia-prone patients), GI upset.",
        "PLATO trial: ticagrelor vs. clopidogrel in ACS → 9.8% vs. 11.7% CV events (p<0.001) — 16% relative risk reduction in primary endpoint. KEY finding: ticagrelor benefit diminished in patients on aspirin >100 mg (higher aspirin doses interfere — maintain aspirin at 81 mg with ticagrelor). Dyspnea: reassure patients (usually benign, transient). Dyspnea is more troublesome in COPD/asthma, but these are not contraindications. CONTRAINDICATED with prior intracranial hemorrhage. Prasugrel: faster/more potent; preferred in STEMI + PCI; CONTRAINDICATED in prior stroke/TIA (↑ICH risk — TRITON-TIMI 38)."
    ),
    "alteplase": _dr(
        "Recombinant tissue plasminogen activator (tPA) — binds fibrin in thrombus → converts plasminogen to plasmin at clot surface → fibrinolysis (fibrin-specific clot dissolution). More fibrin-specific than streptokinase (preferentially activates clot-bound plasminogen). t1/2 ~4-5 min (cleared by liver).",
        "Acute ischemic stroke (0.9 mg/kg IV, max 90 mg — 10% as bolus, 90% over 60 min — within 4.5h of symptom onset if no CI), STEMI (if primary PCI not available within 120 min), massive PE (hemodynamic instability — 100 mg over 2h), catheter-directed thrombolysis (selected DVT/PE cases), occluded catheters (low-dose alteplase).",
        "ICH (2-7% in stroke treatment — most feared — perform CT to EXCLUDE hemorrhage before giving), systemic bleeding, angioedema (rare), reperfusion arrhythmias (after thrombolysis for MI).",
        "Absolute CI to tPA in acute ischemic stroke: hemorrhage on CT, SBP >185/110 (treat first to <185/110), prior ICH ever, recent ischemic stroke (<3 months), active internal bleeding, platelet <100k, INR >1.7 or heparin in last 48h with aPTT elevated, known intracranial tumor/AVM/aneurysm. Relative CI: minor/rapidly improving stroke, surgery <14 days, recent MI. After giving tPA for stroke: NO heparin/antiplatelet for 24h (recheck CT at 24h). Mechanical thrombectomy (LVO): extends window to 6-24h (DAWN/DEFUSE-3 trials — penumbra imaging selects candidates). Tenecteplase (TNK): single weight-based IV bolus — increasingly used instead of alteplase."
    ),
    # ── Statins / Lipid ───────────────────────────────────────────────────
    "atorvastatin": _dr(
        "HMG-CoA reductase inhibitor (statin) — competitively and reversibly inhibits rate-limiting step of hepatic cholesterol synthesis (HMG-CoA → mevalonate) → ↓intracellular cholesterol → ↑LDL receptor expression (SREBP2-mediated) → ↑LDL clearance. Also pleiotropic: ↓CRP (anti-inflammatory), plaque stabilization, endothelial NO ↑. Metabolized by CYP3A4. Highest-intensity statin at 40-80 mg.",
        "Primary + secondary prevention of ASCVD (MI, stroke, PAD) — statin indicated in: any ASCVD, LDL ≥190, DM age 40-75, 10-year ASCVD risk ≥7.5%. High-intensity: atorvastatin 40-80 mg or rosuvastatin 20-40 mg (target ≥50% LDL reduction). Heterozygous and homozygous FH (familial hypercholesterolemia — add ezetimibe or PCSK9 inhibitor for inadequate response).",
        "MYOPATHY (myalgias most common — 5-10%; myositis — ↑CK + sx; rhabdomyolysis — rare but life-threatening — ↑↑↑CK + AKI + tea-colored urine + myoglobinuria → STOP STATIN), new-onset DM (modest risk with high-intensity statins — overall CV benefit >> DM risk), hepatotoxicity (rare — routine LFT monitoring no longer recommended; check if symptomatic), teratogenic (CONTRAINDICATED in pregnancy + breastfeeding — cholesterol needed for fetal development).",
        "Statin-induced myopathy risk ↑ with: CYP3A4 inhibitors (amiodarone, diltiazem, verapamil, azole antifungals, macrolides, grapefruit juice → ↑atorvastatin levels), fibrates (especially gemfibrozil — avoid combination; use fenofibrate if needed — less CYP2C8 interaction), hypothyroidism (↑myopathy risk), renal failure, Asian descent (↑rosuvastatin levels). Rosuvastatin/pravastatin: NOT CYP3A4 metabolized → safer with CYP3A4 inhibitors. Rhabdomyolysis treatment: aggressive IV hydration to prevent myoglobin-induced AKI. PCSK9 inhibitors (evolocumab, alirocumab): for statin-intolerant or inadequate response to max statin — ↓LDL 50-60% additional."
    ),
    "nitroglycerin": _dr(
        "Organic nitrate → metabolized to NO (nitric oxide) → activates soluble guanylyl cyclase → ↑cGMP → PKG activation → myosin light chain phosphatase activation + ↓Ca2+ → smooth muscle relaxation. VENODILATION (↓preload, ↓LVEDP) predominates at low doses. Arteriolar dilation (↓afterload) at high IV doses. Coronary vasodilation (especially vasospasm relief). Does NOT cause coronary steal (unlike dipyridamole).",
        "Acute angina (sublingual 0.4 mg q5min × 3 — if no relief after 3 doses, call 911 → possible MI), stable + vasospastic angina (prophylaxis with long-acting nitrates — isosorbide mononitrate), acute MI (IV — especially with pulmonary edema or ongoing ischemia + HTN), hypertensive emergency with ACS or pulmonary edema, esophageal spasm, anal fissure (topical glyceryl trinitrate), cocaine-induced coronary vasospasm.",
        "Headache (MOST COMMON — meningeal vasodilation), orthostatic hypotension (preload reduction), reflex tachycardia, nitrate tolerance (with continuous 24h use — require 10-12h nitrate-free interval daily), methemoglobinemia (high-dose IV prolonged use — treat with methylene blue), hypotension. CONTRAINDICATED with PDE5 inhibitors (sildenafil, tadalafil, vardenafil — additive cGMP accumulation → severe hypotension → potentially fatal — ASK ABOUT PDE5 INHIBITOR USE BEFORE GIVING NTG).",
        "PDE5 inhibitors (Viagra/sildenafil, Cialis/tadalafil): ABSOLUTE CONTRAINDICATION with nitrates — both ↑cGMP (sildenafil inhibits PDE5 which breaks down cGMP; NTG produces cGMP) → profound hypotension + reflex tachycardia. AVOID nitroglycerin in: RV infarct (RV preload-dependent — nitrates → ↓preload → cardiovascular collapse — treat inferior STEMI + hypotension + JVD + clear lungs with IV FLUIDS not nitrates), HOCM (↓preload → ↑outflow obstruction), severe AS (↓preload → ↓CO across fixed orifice → shock). Nitrate tolerance: prevention requires 10-12h nitrate-free period (e.g., isosorbide mononitrate once daily in morning or eccentric BID — 8am and 2pm — NOT TID)."
    ),

    "penicillin g": _dr(
        "Inhibits bacterial cell wall synthesis by binding PBPs, blocking peptidoglycan cross-linking; bactericidal",
        "Strep pharyngitis, syphilis (T. pallidum), neurosyphilis, rheumatic fever prophylaxis, Clostridial infections",
        "Hypersensitivity (anaphylaxis <0.05%); Jarisch-Herxheimer reaction with spirochete treatment",
        "Drug of choice for syphilis at all stages; penicillin allergy — use ceftriaxone for syphilis if allergy not anaphylactic; desensitize if pregnant"
    ),
    "amoxicillin": _dr(
        "Aminopenicillin; inhibits cell wall synthesis (PBP binding); broader gram-negative coverage than PCN G/V",
        "Strep pharyngitis, otitis media, sinusitis, H. pylori (clarithromycin triple, rifabutin triple or vonoprazan dual regimens), Lyme disease (early), dental prophylaxis",
        "Rash (especially in EBV mononucleosis — 'ampicillin rash'); diarrhea; hypersensitivity",
        "Maculopapular rash with amoxicillin + mono is NOT a true penicillin allergy — caused by immune complexes, not IgE"
    ),
    "ampicillin-sulbactam": _dr(
        "Ampicillin + beta-lactamase inhibitor; covers gram-positives, many gram-negatives, anaerobes",
        "Polymicrobial infections, aspiration pneumonia, diabetic foot infections, intra-abdominal infections",
        "Rash, diarrhea, C. diff; maculopapular rash in EBV",
        "Sulbactam has intrinsic activity against Acinetobacter — useful for MDR Acinetobacter infections"
    ),
    "nafcillin": _dr(
        "Antistaphylococcal penicillin; penicillinase-resistant; binds PBPs; bactericidal against MSSA",
        "MSSA bacteremia, endocarditis, osteomyelitis, septic arthritis, skin/soft tissue infections",
        "Interstitial nephritis, neutropenia (prolonged use), hepatotoxicity; extravasation causes tissue necrosis — give IV only",
        "Preferred over vancomycin for MSSA — better outcomes in MSSA bacteremia; MRSA requires vancomycin or daptomycin"
    ),
    "piperacillin-tazobactam": _dr(
        "Extended-spectrum antipseudomonal penicillin + beta-lactamase inhibitor; broad spectrum including Pseudomonas, anaerobes",
        "HAP/VAP, complicated intra-abdominal, febrile neutropenia empiric, polymicrobial infections",
        "Hypokalemia, neurotoxicity (high doses), acute kidney injury (esp. with vancomycin — VANC-PTZ nephrotoxicity)",
        "VANC + pip-tazo combination significantly increases AKI risk vs. VANC + cefepime — prefer cefepime when possible"
    ),
    "cefazolin": _dr(
        "First-generation cephalosporin; excellent gram-positive (MSSA, Strep) coverage; limited gram-negative",
        "Surgical prophylaxis (most procedures), MSSA infections, UTI (E. coli/Klebsiella), skin/soft tissue",
        "Hypersensitivity (cross-reactivity with PCN <2%), diarrhea; Coombs-positive hemolytic anemia (rare)",
        "First-line for MSSA in penicillin-allergic patients without anaphylaxis history; preferred surgical prophylaxis agent"
    ),
    "ceftriaxone": _dr(
        "Third-generation cephalosporin; excellent gram-negative (including Enterobacteriaceae), good Strep coverage; CSF penetration",
        "Community-acquired pneumonia, meningitis, gonorrhea, Lyme disease, pyelonephritis, SSTI, spontaneous bacterial peritonitis",
        "Biliary sludge/pseudolithiasis (especially in neonates/elderly), ceftriaxone-calcium precipitation (avoid in neonates with Ca-containing IV), diarrhea",
        "Never mix with calcium-containing solutions — forms precipitate; biliary sludge is reversible on discontinuation"
    ),
    "cefepime": _dr(
        "Fourth-generation cephalosporin; extended gram-negative spectrum including Pseudomonas; good gram-positive; CNS penetration",
        "Febrile neutropenia, HAP/VAP, pseudomonal infections, meningitis (gram-negative), complicated UTI",
        "Neurotoxicity (encephalopathy, myoclonus, non-convulsive status epilepticus — especially in renal failure), hypersensitivity",
        "Cefepime neurotoxicity underrecognized — check renal function and dose-adjust; AMS in ICU patient on cefepime → consider drug effect"
    ),
    "ceftaroline": _dr(
        "Fifth-generation cephalosporin; one of only two beta-lactams with MRSA activity (with ceftobiprole); binds PBP2a; gram-negative coverage similar to ceftriaxone",
        "MRSA skin/soft tissue infections, MRSA bacteremia (salvage), community-acquired pneumonia",
        "Hypersensitivity, positive direct Coombs test (no hemolysis typically), neutropenia (prolonged use)",
        "Anti-MRSA beta-lactam (ceftobiprole also FDA-approved in 2024) — useful for patients who cannot tolerate vancomycin; does NOT cover Pseudomonas"
    ),
    "imipenem-cilastatin": _dr(
        "Carbapenem; broadest beta-lactam spectrum (gram-positive, gram-negative, anaerobes, ESBL-producers); cilastatin prevents renal inactivation",
        "Severe/life-threatening infections, ESBL-producers, Acinetobacter, febrile neutropenia (resistant organisms)",
        "Seizures (lowest seizure threshold among carbapenems — dose-adjust in renal failure), nausea/vomiting, hypersensitivity",
        "Highest seizure risk among carbapenems; avoid in CNS infections — use meropenem instead; does NOT cover MRSA or VRE"
    ),
    "meropenem": _dr(
        "Carbapenem; broad spectrum similar to imipenem; better CNS penetration, lower seizure risk; stable to renal dipeptidase (no cilastatin needed)",
        "Bacterial meningitis (gram-negative), severe intra-abdominal, febrile neutropenia, ESBL/AmpC infections",
        "Nausea, diarrhea, hypersensitivity, thrombocytopenia; less seizure risk than imipenem",
        "Preferred carbapenem for CNS infections; KPC-producing Klebsiella may require combination therapy or ceftazidime-avibactam"
    ),
    "aztreonam": _dr(
        "Monobactam; inhibits cell wall synthesis by binding PBP3; ONLY gram-negative aerobic coverage (Pseudomonas, Enterobacteriaceae); no gram-positive/anaerobe activity",
        "Gram-negative infections in PCN/cephalosporin-allergic patients (minimal cross-reactivity); UTI, pneumonia, sepsis",
        "Minimal toxicity profile; hypersensitivity (rare, lower cross-reactivity with PCN); hepatotoxicity (rare)",
        "Safe in PCN-allergic patients except those allergic to ceftazidime (shared side chain); must combine with agent for gram-positive coverage"
    ),
    "vancomycin": _dr(
        "Glycopeptide; inhibits cell wall synthesis by binding D-Ala-D-Ala terminus of peptidoglycan precursors; bactericidal against most gram-positives",
        "MRSA infections, C. diff colitis (oral for C. diff only — not absorbed), PCN-allergic gram-positive infections, febrile neutropenia (gram-positive coverage)",
        "Nephrotoxicity (AUC/MIC-guided dosing to minimize), ototoxicity, vancomycin infusion reaction (formerly 'red man syndrome'; not allergy — rate-related histamine release — slow infusion), thrombophlebitis",
        "Vancomycin infusion reaction: flushing/rash/hypotension from rapid infusion — slow rate + diphenhydramine; NOT an allergy; oral vancomycin stays in GI tract (not systemic)"
    ),
    "gentamicin": _dr(
        "Aminoglycoside; irreversibly binds 30S ribosomal subunit; disrupts protein synthesis and membrane; concentration-dependent bactericidal activity",
        "Gram-negative infections (Pseudomonas, Enterobacteriaceae), synergy with beta-lactams for enterococcal/streptococcal endocarditis",
        "Nephrotoxicity (proximal tubular damage — nonoliguric AKI), ototoxicity (vestibular > cochlear — irreversible), neuromuscular blockade",
        "Once-daily dosing (extended-interval) preferred over q8h — same efficacy, less nephrotoxicity; monitor troughs; avoid in myasthenia gravis"
    ),
    "azithromycin": _dr(
        "Macrolide; binds 50S ribosomal subunit (23S rRNA); inhibits translocation; bacteriostatic; long tissue half-life (68h)",
        "Community-acquired pneumonia (atypicals — Mycoplasma, Chlamydophila, Legionella), Chlamydia trachomatis, MAC prophylaxis/treatment (with ethambutol), pertussis",
        "GI upset, QTc prolongation (risk with other QT-prolonging drugs), hepatotoxicity (rare), cardiovascular mortality concern",
        "Z-pak popularized azithromycin for sinusitis/bronchitis — largely inappropriate (viral); QTc check important; excellent intracellular penetration for atypicals"
    ),
    "ciprofloxacin": _dr(
        "Fluoroquinolone; inhibits DNA gyrase (gram-negatives) and topoisomerase IV (gram-positives); concentration-dependent bactericidal",
        "UTI/pyelonephritis, anthrax (prophylaxis/treatment), Pseudomonas infections, traveler's diarrhea, prostatitis, bone/joint infections",
        "Tendinopathy/tendon rupture (Achilles — black box warning especially >60yo, steroids, renal failure), QTc prolongation, CNS effects (seizures, confusion), phototoxicity, C. diff",
        "Avoid in children (cartilage damage) and pregnancy; chelated by divalent cations (Ca, Mg, Al, Fe) — take 2h before or 6h after; fluoroquinolone-resistant UTI rising"
    ),
    "levofloxacin": _dr(
        "Respiratory fluoroquinolone; enhanced gram-positive coverage (S. pneumoniae) vs. ciprofloxacin; inhibits DNA gyrase and topoisomerase IV",
        "Community-acquired pneumonia (respiratory quinolone), atypical pneumonia, Legionella, sinusitis, pyelonephritis, TB (second-line)",
        "QTc prolongation, tendinopathy/rupture, peripheral neuropathy, C. diff, hypoglycemia (especially with sulfonylureas), CNS effects",
        "Preferred over ciprofloxacin for respiratory infections (better pneumococcal coverage); avoid use for simple UTI — reserve to prevent resistance"
    ),
    "doxycycline": _dr(
        "Tetracycline; binds 30S ribosomal subunit; inhibits aminoacyl-tRNA binding; bacteriostatic; excellent intracellular penetration",
        "Atypical pneumonia (Mycoplasma, Chlamydophila, Legionella), Lyme disease, RMSF (Rickettsia), Chlamydia, syphilis (PCN allergy), malaria prophylaxis, acne, anthrax",
        "GI upset (take with food), photosensitivity, esophageal ulceration (take with full glass of water upright), tooth discoloration/enamel hypoplasia (<8yo), hepatotoxicity",
        "Drug of choice for RMSF — do NOT delay for confirmation (fatal if treated late); only tetracycline acceptable in children for RMSF given risk of death"
    ),
    "tmp-smx": _dr(
        "Trimethoprim-sulfamethoxazole; TMP inhibits dihydrofolate reductase; SMX inhibits dihydropteroate synthase; sequential folate pathway blockade — synergistic bactericidal",
        "UTI (E. coli), Pneumocystis jirovecii pneumonia (treatment and prophylaxis), Toxoplasma prophylaxis, MRSA SSTI (community-acquired), Nocardia",
        "Sulfonamide allergy (rash, Stevens-Johnson), bone marrow suppression (megaloblastic anemia, leukopenia), hyperkalemia (TMP blocks K+ secretion in distal nephron), nephrotoxicity, crystalluria",
        "PCP prophylaxis if CD4 <200; TMP raises serum creatinine (blocks tubular secretion — not true GFR decline); hyperkalemia mechanism similar to amiloride"
    ),
    "metronidazole": _dr(
        "Nitroimidazole; undergoes reduction to toxic free radicals that damage DNA; active only against anaerobes and certain protozoa",
        "C. diff (only if fidaxomicin or oral vancomycin is unavailable; IV add-on in fulminant disease), Trichomonas, bacterial vaginosis, Giardia, amebiasis, H. pylori (bismuth quadruple therapy), intra-abdominal anaerobes",
        "Metallic taste, nausea, disulfiram-like reaction with alcohol (avoid alcohol), peripheral neuropathy (prolonged use), CNS toxicity (high doses/prolonged)",
        "Disulfiram-like reaction: acetaldehyde accumulates when alcohol + metronidazole — flushing, tachycardia, vomiting; oral metronidazole is now a last-resort option for C. diff; IV metronidazole is only an add-on in fulminant disease"
    ),
    "clindamycin": _dr(
        "Lincosamide; binds 50S ribosomal subunit (23S rRNA) — same site as macrolides/chloramphenicol; inhibits translocation; bacteriostatic",
        "Anaerobic infections above the diaphragm (aspiration pneumonia, lung abscess), MRSA SSTI (CA-MRSA), group A Strep (PCN allergy), Toxoplasma (with pyrimethamine), Babesia",
        "C. diff colitis (historically highest risk antibiotic for C. diff), diarrhea, pseudomembranous colitis, hepatotoxicity",
        "Highest historically-associated risk for C. diff; good for SSTI (CA-MRSA often sensitive); check inducible clindamycin resistance (D-zone test) before using for MRSA"
    ),
    "linezolid": _dr(
        "Oxazolidinone; inhibits protein synthesis by binding 23S rRNA of 50S subunit — unique mechanism prevents formation of 70S initiation complex; bacteriostatic against most organisms",
        "MRSA infections (pneumonia, bacteremia, SSTI), VRE, drug-resistant gram-positive infections (alternatives when vancomycin fails)",
        "Thrombocytopenia, anemia (prolonged use — reversible), serotonin syndrome (MAOI properties — avoid SSRIs, SNRIs, TCAs), peripheral neuropathy, optic neuropathy (prolonged use)",
        "Weak MAOI — serious serotonin syndrome with serotonergic drugs; no dosing adjustment for renal/hepatic failure; oral bioavailability ~100% (equivalent to IV)"
    ),
    "daptomycin": _dr(
        "Lipopeptide; inserts into gram-positive cell membrane in calcium-dependent manner; causes rapid depolarization and cell death; bactericidal",
        "MRSA bacteremia and endocarditis (right-sided), VRE, MRSA SSTI (complicated), enterococcal infections",
        "Myopathy/rhabdomyolysis (monitor CK weekly), eosinophilic pneumonia (rare but serious — stop if respiratory symptoms), peripheral neuropathy",
        "CANNOT use for pulmonary infections — inactivated by surfactant; right-sided IE with MRSA: daptomycin effective; must monitor CK regularly for myopathy"
    ),
    "nitrofurantoin": _dr(
        "Nitrofuran; reduced by bacterial nitrofuran reductase to reactive intermediates that damage DNA, proteins, and ribosomes; bactericidal in urine",
        "Uncomplicated UTI (E. coli, Enterococcus, Staphylococcus saprophyticus); UTI prophylaxis; NOT for pyelonephritis",
        "GI upset (take with food), pulmonary toxicity (acute: hypersensitivity pneumonitis; chronic: pulmonary fibrosis), hemolytic anemia (G6PD deficiency), hepatotoxicity",
        "Avoid if CrCl <30 (inadequate urinary concentration and increased toxicity); contraindicated at term pregnancy (hemolytic anemia in neonate); first-line for uncomplicated cystitis"
    ),
    "rifampin": _dr(
        "Rifamycin; inhibits prokaryotic DNA-dependent RNA polymerase (beta-subunit); bactericidal; excellent intracellular penetration",
        "TB (combination regimen — never monotherapy due to rapid resistance), leprosy, N. meningitidis prophylaxis, H. influenzae type b prophylaxis, prosthetic valve endocarditis (adjunct), Legionella (adjunct)",
        "Orange-red discoloration of body fluids (urine, tears, sweat — warn patients), potent CYP450 inducer (reduces levels of OCP, warfarin, HIV meds, many others), hepatotoxicity, flu-like syndrome (intermittent dosing)",
        "Never use alone — rapid resistance develops; powerful inducer of CYP3A4, CYP2C9, P-gp — numerous drug interactions; orange tears can stain contact lenses"
    ),
    "isoniazid": _dr(
        "Inhibits mycolic acid synthesis (InhA enzyme) in M. tuberculosis; prodrug activated by KatG catalase-peroxidase; bactericidal against actively replicating TB",
        "TB treatment (cornerstone of RIPE regimen) and latent TB infection (LTBI) prophylaxis (3 months with rifapentine [3HP] or rifampin [3HR] preferred; isoniazid alone 6–9 months as an alternative)",
        "Peripheral neuropathy (pyridoxine/B6 deficiency — supplement B6), hepatotoxicity (age-dependent risk; elevated LFTs common, clinical hepatitis ~1%), lupus-like syndrome, CNS toxicity (seizures in overdose — treat with pyridoxine)",
        "RIPE: Rifampin + Isoniazid + Pyrazinamide + Ethambutol; slow and fast acetylators (NAT2 polymorphism) affect drug levels; pyridoxine supplementation mandatory"
    ),
    "pyrazinamide": _dr(
        "Nicotinamide analog; converted to pyrazinoic acid in acidic environment of macrophage phagolysosomes; mechanism not fully elucidated; kills semi-dormant bacilli in macrophages",
        "TB treatment (first 2 months of RIPE regimen — sterilizing agent for intracellular bacilli)",
        "Hyperuricemia (gout — blocks uric acid excretion), hepatotoxicity (dose-dependent), arthralgias, nausea",
        "Used only first 2 months of 6-month regimen — sterilizes macrophage reservoir; causes hyperuricemia but clinical gout uncommon — hold if symptomatic gout"
    ),
    "ethambutol": _dr(
        "Inhibits arabinosyl transferase — blocks arabinogalactan synthesis in M. tuberculosis cell wall; bacteriostatic",
        "TB treatment (part of RIPE — prevents emergence of resistance to other agents), MAC treatment (with azithromycin and rifampin)",
        "Optic neuritis (dose-dependent — visual acuity, red-green color discrimination changes; usually reversible); hyperuricemia",
        "Obtain baseline visual acuity and color vision; monitor monthly; drug discontinued if visual changes; avoid in young children who cannot report visual symptoms"
    ),
    "fluconazole": _dr(
        "Triazole antifungal; inhibits 14-alpha-demethylase (CYP51A1) — blocks ergosterol synthesis; fungistatic against Candida (fungicidal for some)",
        "Candida (mucocutaneous, esophageal, candidemia, UTI), Cryptococcal meningitis (consolidation therapy), Coccidioidomycosis, dermatophytes",
        "Nausea, hepatotoxicity, QTc prolongation, CYP2C9 inhibitor (warfarin, phenytoin levels increase), teratogenic",
        "Candida krusei intrinsically resistant; Candida glabrata often resistant; first-line for non-neutropenic candidemia is echinocandin (anidulafungin/caspofungin) not fluconazole"
    ),
    "voriconazole": _dr(
        "Second-generation triazole; inhibits 14-alpha-demethylase; broader spectrum than fluconazole; covers Aspergillus and many molds",
        "Invasive aspergillosis (drug of choice), Fusarium, Scedosporium, candidemia (including azole-resistant), endemic fungi",
        "Visual disturbances (transient photopsia — 30%; harmless), hepatotoxicity, QTc prolongation, photosensitivity (squamous cell carcinoma risk long-term), hallucinations, phototoxicity",
        "Drug of choice for invasive aspergillosis; CYP2C19 polymorphisms cause highly variable levels — therapeutic drug monitoring (TDM) recommended; avoid with rifampin (induces metabolism)"
    ),
    "amphotericin b": _dr(
        "Polyene; binds ergosterol in fungal cell membrane, forming pores — cell leakage and death; fungicidal; broadest antifungal spectrum",
        "Life-threatening fungal infections (Cryptococcus, Aspergillus, Mucor/Rhizopus, Candida), empiric in febrile neutropenia, Leishmaniasis",
        "Nephrotoxicity (infusion-related, cumulative — monitor creatinine, K+, Mg2+), infusion reactions (rigors, fever, chills — premedicate with acetaminophen/diphenhydramine), hypokalemia, hypomagnesemia, anemia",
        "Amphotericin B deoxycholate (conventional) most nephrotoxic; lipid formulations (liposomal AmB) less nephrotoxic — preferred; prehydration with NS reduces nephrotoxicity; 'shake and bake' = rigors/fever from infusion"
    ),
    "caspofungin": _dr(
        "Echinocandin; inhibits beta-1,3-glucan synthase — disrupts fungal cell wall synthesis (no human equivalent → selective toxicity); fungicidal against Candida",
        "Invasive candidiasis (first-line for candidemia in most patients), esophageal candidiasis, empiric therapy in febrile neutropenia, Aspergillus (salvage)",
        "Hepatotoxicity (transaminase elevation — monitor LFTs), infusion site reactions, histamine-mediated reactions (rare), drug interactions (cyclosporine increases levels)",
        "Echinocandins preferred over fluconazole for invasive candidiasis/candidemia; minimal renal toxicity (no dose adjustment for renal failure); poor CNS, eye, urine penetration"
    ),
    "acyclovir": _dr(
        "Nucleoside analog; phosphorylated by viral thymidine kinase (TK) → triphosphate inhibits viral DNA polymerase; incorporated into viral DNA causing chain termination; selective for infected cells",
        "HSV-1/2 (genital herpes, cold sores, encephalitis), VZV (chickenpox, zoster), HSV prophylaxis in immunocompromised",
        "Nephrotoxicity (crystalluria — adequate hydration essential), neurotoxicity (high doses/renal failure — tremors, confusion), phlebitis (IV), nausea",
        "Requires viral TK for activation — acyclovir-resistant HSV has TK mutations; HSV encephalitis requires IV acyclovir immediately — do not delay for PCR results; valacyclovir = prodrug with better oral bioavailability"
    ),
    "ganciclovir": _dr(
        "Nucleoside analog; phosphorylated by CMV UL97 kinase (and cellular kinases) → triphosphate inhibits CMV DNA polymerase; incorporated into viral DNA",
        "CMV retinitis, CMV colitis/esophagitis, CMV pneumonitis (especially post-transplant), CMV prophylaxis (immunocompromised)",
        "Bone marrow suppression (neutropenia, thrombocytopenia — dose-limiting), nephrotoxicity, teratogenic/embryotoxic, CNS effects",
        "Valganciclovir = oral prodrug of ganciclovir with good bioavailability; CMV resistance via UL97 (low-level) or UL54 (high-level) mutations; foscarnet if ganciclovir-resistant"
    ),
    "oseltamivir": _dr(
        "Neuraminidase inhibitor; prevents release of new viral particles from infected cells and reduces viral spread; active against influenza A and B",
        "Influenza A and B treatment (within 48h of symptom onset — reduces duration by ~1 day) and prophylaxis (post-exposure, high-risk patients)",
        "Nausea/vomiting (take with food), headache; neuropsychiatric events (rare — mainly in children, particularly Japan)",
        "Most benefit if started within 48h; still consider if >48h in hospitalized, high-risk, or severe disease; treat confirmed influenza in pregnancy regardless of timing"
    ),

    "phenytoin": _dr(
        "Blocks voltage-gated Na+ channels in a use-dependent (frequency-dependent) manner — stabilizes neuronal membranes; slows action potential propagation",
        "Focal and generalized tonic-clonic seizures, status epilepticus (IV fosphenytoin preferred), trigeminal neuralgia",
        "Gingival hyperplasia, hirsutism, coarsening of facial features, peripheral neuropathy (chronic), cerebellar atrophy, nystagmus/ataxia/diplopia (dose-related), zero-order kinetics (small dose increases cause large level increases), teratogenic (fetal hydantoin syndrome), hepatotoxicity",
        "Zero-order (saturation) kinetics at therapeutic levels — small dose changes cause large swings; narrow therapeutic index (10-20 mcg/mL); induces CYP enzymes; Stevens-Johnson rare but serious"
    ),
    "levetiracetam": _dr(
        "Binds synaptic vesicle protein SV2A — modulates neurotransmitter release; unique mechanism distinct from all other AEDs",
        "Focal and generalized epilepsy, status epilepticus (IV), myoclonic seizures (juvenile myoclonic epilepsy — first-line)",
        "Behavioral/psychiatric side effects (irritability, aggression, depression — 'Keppra rage'), somnolence, headache; minimal drug interactions",
        "No hepatic metabolism, no drug interactions — ideal for patients on multiple medications or with liver disease; needs dose adjustment for renal impairment; pyridoxine (B6) for behavioral effects has only limited, low-quality evidence"
    ),
    "valproate": _dr(
        "Multiple mechanisms: blocks Na+ channels, increases GABA (inhibits GABA transaminase), blocks T-type Ca2+ channels; broad-spectrum AED",
        "Generalized epilepsy (all types — tonic-clonic, absence, myoclonic), focal seizures, bipolar disorder (mood stabilizer), migraine prophylaxis",
        "Hepatotoxicity (fatal — especially <2yo, polytherapy; check LFTs), neural tube defects (spina bifida — major teratogen — avoid in pregnancy), thrombocytopenia, pancreatitis, weight gain, tremor, alopecia, hyperammonemia (with or without hepatotoxicity)",
        "Absolute contraindication in pregnancy (highest teratogen risk among AEDs — 10x risk of spina bifida); causes hyperammonemia via carnitine depletion — can give L-carnitine; inhibits CYP enzymes"
    ),
    "carbamazepine": _dr(
        "Blocks voltage-gated Na+ channels (use-dependent); similar to phenytoin but different structure; also has antidepressant, antimanic properties",
        "Focal seizures (first-line), trigeminal neuralgia (drug of choice), bipolar disorder, glossopharyngeal neuralgia",
        "SJS/TEN (HLA-B*1502 in Asian patients — screen before use), SIADH/hyponatremia, aplastic anemia/agranulocytosis, diplopia/ataxia (dose-related), CYP3A4 inducer (auto-induces own metabolism), teratogenic (neural tube defects)",
        "HLA-B*1502 testing in Han Chinese and SE Asian patients before starting — SJS risk is 10x higher; autoinduction requires dose increases over first months; leukopenia common — monitor CBC"
    ),
    "lamotrigine": _dr(
        "Blocks voltage-gated Na+ channels and inhibits glutamate release; broad-spectrum; preferred in pregnancy among AEDs",
        "Focal and generalized seizures, absence seizures, bipolar disorder (maintenance — prevents depressive episodes), Lennox-Gastaut syndrome",
        "SJS/TEN (especially if titrated too fast or combined with valproate — valproate doubles lamotrigine levels via UGT inhibition), dizziness, diplopia, headache, rash",
        "Must titrate slowly (especially with valproate) to minimize SJS risk; safest AED in pregnancy (still some risk); preferred for women of childbearing potential; levels drop significantly during pregnancy — monitor and adjust"
    ),
    "phenobarbital": _dr(
        "Enhances GABA-A receptor activity (increases duration of Cl- channel opening — different from benzodiazepines which increase frequency); also inhibits glutamate",
        "Seizures (neonatal seizures — drug of choice), status epilepticus (if benzo + phenytoin fail), focal/generalized epilepsy, alcohol withdrawal",
        "CNS depression (sedation, cognitive impairment), respiratory depression (high doses), physical dependence/withdrawal, CYP450 inducer (major — reduces many drug levels), osteomalacia (chronic — CYP induction of vitamin D metabolism)",
        "Drug of choice for neonatal seizures (IV phenobarbital); potent inducer reduces levels of warfarin, OCP, many other drugs; requires slow taper to discontinue (withdrawal seizures)"
    ),
    "ethosuximide": _dr(
        "Blocks T-type (low-voltage) calcium channels in thalamic neurons — interrupts 3Hz spike-wave discharges of absence seizures; ONLY effective for absence seizures",
        "Childhood absence epilepsy (drug of choice — preferred over valproate in children due to better cognitive and behavioral tolerability)",
        "GI upset (nausea, vomiting — take with food), headache, drowsiness, SLE-like syndrome, aplastic anemia (rare), behavioral changes",
        "First-line for pure absence epilepsy; does NOT work for other seizure types — if patient also has tonic-clonic seizures, use valproate instead; does not affect other Na+ channels"
    ),
    "haloperidol": _dr(
        "Typical (first-generation) antipsychotic; potent D2 receptor antagonist in mesolimbic pathway; also blocks D1, alpha-1, H1, muscarinic receptors",
        "Schizophrenia (positive symptoms), acute agitation (IV/IM), Tourette syndrome, delirium, Huntington's chorea, antiemetic (low doses)",
        "EPS: akathisia (restlessness), parkinsonism, acute dystonia (torticollis — treat with benztropine/diphenhydramine), tardive dyskinesia (long-term — irreversible); NMS (fever, rigidity, autonomic instability, elevated CK — life-threatening); QTc prolongation; hyperprolactinemia",
        "High potency = more EPS, less sedation/hypotension; NMS treatment: stop drug, dantrolene, bromocriptine; haloperidol decanoate = long-acting injectable (IM monthly); least sedating typical antipsychotic"
    ),
    "clozapine": _dr(
        "Atypical antipsychotic; D4 > D2 antagonism; also 5-HT2A, H1, muscarinic, alpha-1 antagonist; broad receptor blockade; no significant D2 blockade in nigrostriatal pathway",
        "Treatment-resistant schizophrenia (failed 2 antipsychotics), suicidality reduction in schizophrenia/schizoaffective disorder (only antipsychotic FDA-approved for this)",
        "Agranulocytosis (1-2% — mandatory ANC monitoring; REMS program), weight gain (most among antipsychotics), metabolic syndrome, myocarditis (rare — early), seizures (dose-dependent), hypersalivation, sedation, orthostatic hypotension, constipation (fatal ileus possible)",
        "Required ANC monitoring per REMS: weekly x6mo, biweekly x6mo, monthly thereafter; stop if ANC <1000; never restart after agranulocytosis; most effective antipsychotic overall — use for treatment-resistant cases"
    ),
    "risperidone": _dr(
        "Atypical antipsychotic; D2 and 5-HT2A antagonist; higher D2 affinity than other atypicals — intermediate EPS risk",
        "Schizophrenia, bipolar disorder (acute mania), irritability in autism spectrum disorder, pediatric schizophrenia",
        "EPS (dose-dependent — more than other atypicals), hyperprolactinemia (most among atypicals — galactorrhea, amenorrhea, sexual dysfunction), weight gain, metabolic syndrome, orthostatic hypotension, QTc prolongation",
        "Highest prolactin elevation among atypicals — ask about sexual dysfunction, menstrual irregularities; paliperidone = active metabolite; risperidone long-acting injectable (Risperdal Consta) available"
    ),
    "olanzapine": _dr(
        "Atypical antipsychotic; D2, 5-HT2A, H1, muscarinic, alpha-1 antagonist; broad receptor blockade",
        "Schizophrenia, bipolar mania, acute agitation (IM), treatment-resistant depression (with fluoxetine — Symbyax), anorexia nervosa",
        "Weight gain (greatest metabolic liability — average 10+ lbs), metabolic syndrome, diabetes, dyslipidemia, sedation (H1 blockade), constipation, orthostatic hypotension",
        "Most metabolically problematic atypical — monitor glucose, lipids, weight; olanzapine + lorazepam IM combination causes respiratory depression and death — avoid concurrent use; IM available for acute agitation"
    ),
    "quetiapine": _dr(
        "Atypical antipsychotic; D2, 5-HT2A, H1, alpha-1 antagonist; relatively low D2 affinity (short receptor occupancy)",
        "Schizophrenia, bipolar disorder (mania and depression — FDA-approved), adjunctive treatment-resistant depression, insomnia (off-label — low dose via H1 blockade)",
        "Sedation (H1 blockade — most sedating atypical), orthostatic hypotension, weight gain, metabolic syndrome, cataracts (baseline and annual slit-lamp exams recommended), QTc prolongation",
        "Most sedating atypical — commonly abused for sleep; very low EPS risk (low D2 affinity); frequently used off-label for insomnia/anxiety — suboptimal evidence; cataracts found in animal studies — monitoring recommended"
    ),
    "aripiprazole": _dr(
        "Atypical antipsychotic; partial D2/D3 agonist + 5-HT1A partial agonist + 5-HT2A antagonist; 'dopamine system stabilizer' — acts as antagonist when DA high, agonist when DA low",
        "Schizophrenia, bipolar mania, MDD adjunct, irritability in autism, Tourette syndrome, agitation (IM)",
        "Akathisia (most common adverse effect — dose-related), insomnia/restlessness/anxiety, nausea, weight gain (least metabolic liability among atypicals), impulse control disorders (gambling, hypersexuality)",
        "Best metabolic profile among atypicals — preferred for metabolically vulnerable patients; partial agonism can worsen positive symptoms in high-dopamine states; akathisia responds to propranolol or dose reduction"
    ),
    "fluoxetine": _dr(
        "SSRI; selectively inhibits serotonin reuptake transporter (SERT) — increases synaptic serotonin; delayed therapeutic effect (2-6 weeks)",
        "MDD, OCD, bulimia nervosa, panic disorder, PMDD, bipolar depression (with olanzapine), social anxiety disorder",
        "Sexual dysfunction (decreased libido, anorgasmia — most common reason for discontinuation), GI upset, insomnia/activation, headache, weight changes; serotonin syndrome (with MAOIs, tramadol); QTc prolongation (at high doses)",
        "Longest half-life SSRI (1-6 days + active metabolite norfluoxetine 4-16 days) — fewest withdrawal symptoms; LEAST likely to cause discontinuation syndrome; potent CYP2D6 inhibitor — drug interactions; wait 5 weeks after stopping fluoxetine before starting an MAOI (2 weeks for other SSRIs)"
    ),
    "sertraline": _dr(
        "SSRI; inhibits SERT with high selectivity; minimal inhibition of NE or DA reuptake",
        "MDD, PTSD (first-line), OCD, social anxiety disorder, panic disorder, PMDD",
        "GI side effects (most GI-prone SSRI — take with food), sexual dysfunction, insomnia, weight gain, headache, serotonin syndrome (with MAOIs), discontinuation syndrome (shorter half-life than fluoxetine)",
        "Most studied SSRI in pregnancy (safest evidence profile — though not zero risk); first-line for PTSD; moderate CYP2D6 inhibitor; discontinuation syndrome if stopped abruptly — taper slowly"
    ),
    "venlafaxine": _dr(
        "SNRI; inhibits both SERT (primary, low doses) and NET (at higher doses) — dual mechanism increases serotonin and norepinephrine",
        "MDD (efficacy advantage over SSRIs in severe depression), generalized anxiety disorder, social anxiety disorder, panic disorder, fibromyalgia, neuropathic pain",
        "Hypertension (NE effect — dose-dependent; monitor BP), sexual dysfunction, GI upset, insomnia, discontinuation syndrome (severe — must taper), diaphoresis, serotonin syndrome",
        "Severe discontinuation syndrome — taper very slowly (switch to fluoxetine for tapering in severe cases); dose-dependent increase in NE effects (low dose = mostly serotonergic); more effective than SSRIs for severe/melancholic depression"
    ),
    "duloxetine": _dr(
        "SNRI; balanced inhibition of SERT and NET at all doses (unlike venlafaxine); also mild inhibition of dopamine reuptake",
        "MDD, generalized anxiety disorder, diabetic peripheral neuropathy, fibromyalgia, chronic musculoskeletal pain, stress urinary incontinence",
        "Nausea (most common — take with food), dry mouth, constipation, insomnia, hypertension, hepatotoxicity (avoid in liver disease/heavy alcohol use), discontinuation syndrome",
        "FDA-approved for multiple pain syndromes — useful in patients with comorbid depression + chronic pain; avoid in hepatic impairment; CYP1A2 and CYP2D6 inhibitor"
    ),
    "bupropion": _dr(
        "NDRI (norepinephrine-dopamine reuptake inhibitor); weak NE and DA reuptake inhibitor; no serotonergic activity; also nicotinic acetylcholine receptor antagonist",
        "MDD (especially atypical depression, anhedonia), smoking cessation (Zyban), ADHD (off-label), sexual dysfunction caused by SSRIs (off-label adjunct), seasonal affective disorder",
        "Seizures (dose-dependent — lowers seizure threshold; contraindicated in eating disorders/seizure history), insomnia, anxiety/activation, dry mouth, hypertension; NO sexual dysfunction (unique advantage); NO weight gain",
        "Only antidepressant that promotes weight loss; avoids sexual dysfunction — useful as adjunct or monotherapy when sexual side effects are concern; absolute contraindication in anorexia/bulimia (increased seizure risk)"
    ),
    "amitriptyline": _dr(
        "TCA (tricyclic antidepressant); blocks SERT and NET; also blocks H1, muscarinic, alpha-1 receptors; blocks Na+ and K+ channels (cardiac effects)",
        "Depression (less used now due to side effects), neuropathic pain (first-line), migraine prophylaxis, insomnia, fibromyalgia, IBS",
        "Anticholinergic: dry mouth, constipation, urinary retention, blurry vision, confusion (especially elderly); antihistamine: sedation, weight gain; alpha-1 blockade: orthostatic hypotension; cardiac: QTc prolongation, arrhythmias; lethal in overdose (wide QRS, arrhythmias, seizures)",
        "Highly lethal in overdose — QRS widening, refractory VT; treat overdose with sodium bicarbonate (Na loading narrows QRS); antihistaminergic sedation makes it useful for insomnia/neuropathic pain at low doses"
    ),
    "phenelzine": _dr(
        "MAOI (irreversible, non-selective); inhibits MAO-A and MAO-B — increases synaptic monoamines (NE, DA, 5-HT); irreversible (requires new enzyme synthesis — 2 weeks washout)",
        "Atypical depression (MOA most effective — hypersomnia, reactive mood, rejection sensitivity, leaden paralysis), treatment-resistant depression, social phobia",
        "Hypertensive crisis with tyramine (aged cheese, cured meats, tap beer — 'cheese reaction' via MAO-A in gut), serotonin syndrome (with SSRIs, SNRIs, TCAs, tramadol, meperidine, dextromethorphan), orthostatic hypotension, weight gain, insomnia, sexual dysfunction",
        "Must maintain tyramine-restricted diet; 2-week washout before/after switching to serotonergic drugs; meperidine + MAOI = potentially fatal (serotonin syndrome); selegiline at low doses = selective MAO-B inhibitor (no dietary restriction)"
    ),
    "lithium": _dr(
        "Mechanism incompletely understood; inhibits inositol monophosphatase and glycogen synthase kinase-3 (GSK-3); modulates second messenger systems; stabilizes mood",
        "Bipolar disorder (gold standard — acute mania and maintenance; reduces suicide risk), schizoaffective disorder, augmentation of antidepressants, cluster headache prophylaxis",
        "Narrow therapeutic index (0.6-1.2 mEq/L maintenance; toxicity >1.5 mEq/L); toxicity: tremor, polyuria/polydipsia (nephrogenic DI), hypothyroidism, cardiac (T-wave flattening, Ebstein-like changes), renal insufficiency (chronic), teratogenic (Ebstein anomaly), neurotoxicity (>2 mEq/L: ataxia, confusion, seizures)",
        "NSAIDs, ACEi, thiazides all increase lithium levels (decreased renal excretion) — dangerous interactions; dehydration raises levels; toxicity treated with hemodialysis if severe; monitor levels, TSH, creatinine regularly"
    ),
    "diazepam": _dr(
        "Benzodiazepine; positive allosteric modulator of GABA-A receptor — increases frequency of Cl- channel opening (requires GABA present); CNS depressant",
        "Anxiety (acute), status epilepticus (IV — first-line), alcohol withdrawal (CIWA protocol), muscle spasm, procedural sedation, pre-anesthesia, acute panic",
        "CNS depression (sedation, ataxia), respiratory depression (especially with opioids or alcohol — avoid combination), physical dependence/tolerance, withdrawal (seizures, autonomic instability), anterograde amnesia",
        "Benzodiazepines work ONLY in presence of GABA (unlike barbiturates); rebound anxiety and withdrawal seizures on abrupt discontinuation; treat overdose with flumazenil (reversal agent — but short-acting; avoid in polydrug OD with TCAs — lowers seizure threshold)"
    ),
    "lorazepam": _dr(
        "Benzodiazepine (intermediate-acting); GABA-A positive allosteric modulator; no active metabolites — preferred in hepatic impairment",
        "Status epilepticus (IV/IM — first-line in hospital), acute agitation, procedural anxiolysis, alcohol withdrawal, ICU sedation",
        "Respiratory depression, CNS depression, propylene glycol toxicity (prolonged IV infusion — high-dose), physical dependence, anterograde amnesia",
        "No active metabolites — preferred in elderly and hepatic failure (LOT: Lorazepam, Oxazepam, Temazepam — all no active metabolites); propylene glycol accumulation with high-dose prolonged IV infusion"
    ),
    "midazolam": _dr(
        "Short-acting benzodiazepine; water-soluble at low pH, lipophilic at physiologic pH; rapid onset; potent amnestic properties; GABA-A modulator",
        "Procedural sedation, anesthesia induction, ICU sedation, status epilepticus (IM midazolam — as effective as IV lorazepam), intubation premedication",
        "Respiratory depression (significant — especially with opioids; have resuscitation ready), hypotension, retrograde/anterograde amnesia, paradoxical agitation (children)",
        "IM midazolam now preferred initial treatment for status epilepticus in pre-hospital setting (RAMPART trial — faster to administer than establishing IV); very short acting — infusion needed for sustained sedation"
    ),
    "levodopa": _dr(
        "Dopamine precursor; crosses BBB (dopamine cannot); converted to dopamine by DOPA decarboxylase in CNS; given with carbidopa (peripheral DOPA decarboxylase inhibitor) to reduce peripheral conversion and allow lower doses",
        "Parkinson's disease (most effective symptomatic treatment — gold standard), dopamine-responsive dystonia",
        "Motor fluctuations (wearing off, on-off phenomenon — dyskinesias with long-term use), nausea/vomiting (without carbidopa), orthostatic hypotension, hallucinations/psychosis (dopaminergic), dyskinesias (peak-dose), impulse control disorders",
        "Carbidopa prevents peripheral conversion — reduces nausea and allows lower L-dopa dose; dyskinesias and motor fluctuations worsen over years; dopamine agonists (pramipexole, ropinirole) preferred in younger patients to delay L-dopa"
    ),
    "donepezil": _dr(
        "Reversible acetylcholinesterase inhibitor (AChEI); inhibits breakdown of ACh in synaptic cleft — increases cholinergic transmission in cortex and hippocampus",
        "Alzheimer's disease (mild to severe — all stages), dementia with Lewy bodies, vascular dementia (off-label)",
        "Cholinergic side effects: nausea, vomiting, diarrhea (GI most common — dose-limiting), bradycardia (vagotonic), syncope, nightmares/vivid dreams (REM-related), muscle cramps, urinary incontinence",
        "Modest benefit — slows cognitive decline but does not halt disease; start at 5mg QHS (minimize GI effects); 23mg dose approved for moderate-severe but GI side effects more common; nightmares from cholinergic REM augmentation — switch to AM dosing"
    ),
    "memantine": _dr(
        "NMDA (glutamate) receptor antagonist — non-competitive, voltage-dependent; blocks pathological glutamate excitotoxicity while allowing physiologic NMDA activity",
        "Moderate-to-severe Alzheimer's disease (alone or with AChEI); combination with donepezil superior to either alone",
        "Generally well-tolerated; dizziness, headache, constipation, confusion (rare); excreted unchanged in urine — dose adjust for renal impairment",
        "Different mechanism from AChEIs — used in combination for moderate-severe AD; does not slow progression; excreted renally (unlike donepezil — hepatic); no significant drug interactions"
    ),
    "morphine": _dr(
        "Opioid agonist; binds mu (primary), kappa, delta receptors; activates descending pain inhibition, opens K+ channels, closes Ca2+ channels — hyperpolarizes neurons",
        "Severe pain (post-op, cancer, acute MI pain, sickle cell crisis), dyspnea in palliative care, acute pulmonary edema (preload reduction + anxiolysis)",
        "Respiratory depression (dose-dependent — most feared), constipation (no tolerance develops — always give stool softener), nausea/vomiting, pruritus (histamine release — not allergy), miosis (pinpoint pupils), urinary retention, physical dependence, hypotension, SIADH",
        "Constipation persists throughout therapy — methylnaltrexone or lubiprostone for opioid-induced constipation; active metabolite morphine-6-glucuronide accumulates in renal failure — prolonged effect; treat overdose with naloxone"
    ),
    "naloxone": _dr(
        "Opioid antagonist; competitive antagonist at mu, kappa, delta receptors; reverses all opioid effects; short half-life (30-90 min)",
        "Opioid overdose reversal (emergency), postoperative opioid reversal, diagnosis of opioid dependence, opioid-induced pruritus",
        "Precipitates acute opioid withdrawal in dependent patients (agitation, tachycardia, vomiting, diaphoresis), pulmonary edema (rare), resedation (opioid outlasts naloxone)",
        "Half-life shorter than most opioids — resedation occurs; may need repeated doses or infusion; naltrexone = long-acting oral opioid antagonist (monthly injectable formulation for AUD/OUD); Narcan available OTC"
    ),
    "buprenorphine": _dr(
        "Partial mu-opioid agonist (high receptor affinity, low intrinsic activity) + kappa antagonist; long half-life; ceiling effect on respiratory depression",
        "Opioid use disorder (OUD) treatment (Suboxone = buprenorphine + naloxone), moderate-to-severe pain (Belbuca, Butrans patch), neonatal opioid withdrawal syndrome",
        "Withdrawal precipitation if given to opioid-dependent patient too soon (must wait for COWS score ≥8), nausea, headache, constipation, diaphoresis, dental caries (sublingual formulation — saliva pH changes)",
        "Ceiling effect on respiratory depression makes it safer than full agonists; naloxone added to Suboxone to deter IV abuse (naloxone poorly absorbed SL but active if injected); high receptor affinity — can displace other opioids"
    ),
    "methylphenidate": _dr(
        "Blocks reuptake of dopamine and norepinephrine (DAT and NET inhibitor); increases synaptic concentrations of DA and NE in prefrontal cortex",
        "ADHD (first-line pharmacotherapy for children and adults), narcolepsy",
        "Decreased appetite/weight loss (growth suppression in children — monitor height/weight), insomnia (give early in day), increased HR and BP, headache, GI upset, tics (relative contraindication with Tourette), substance abuse potential (Schedule II), psychosis (rare)",
        "Must hold in patients with structural cardiac abnormalities or uncontrolled hypertension; drug holiday in summer can allow growth recovery; amphetamines (Adderall) also first-line — similar mechanism but release DA from vesicles also"
    ),
    "sumatriptan": _dr(
        "Triptan; selective 5-HT1B/1D agonist; vasoconstricts dilated intracranial vessels, inhibits trigeminal nociceptive neurotransmitter release",
        "Acute migraine treatment (abortive — acute attack), cluster headache (SC injection only)",
        "Chest/jaw tightness (vasospasm — rule out cardiac), dizziness, paresthesias, flushing, rebound headache (medication overuse headache if used >10 days/month), serotonin syndrome (with MAOIs — avoid combination)",
        "Contraindicated in uncontrolled hypertension, coronary artery disease, basilar/hemiplegic migraine, within 24h of ergotamine; most effective when taken early in migraine attack; SC formulation fastest onset for cluster headache"
    ),

    "metformin": _dr(
        "Biguanide; activates AMPK — decreases hepatic gluconeogenesis (primary), improves peripheral insulin sensitivity, slows intestinal glucose absorption; does NOT cause hypoglycemia",
        "Type 2 diabetes (first-line monotherapy), PCOS (off-label — reduces insulin resistance), pre-diabetes, weight management adjunct",
        "GI side effects (nausea, diarrhea, metallic taste — start low and titrate; ER formulation better tolerated), lactic acidosis (rare — contraindicated if eGFR <30; hold before contrast if eGFR 30-60), B12 deficiency (long-term — monitor annually)",
        "Hold metformin before IV contrast if eGFR <60 (restart 48h after if no AKI); does not cause hypoglycemia; lactic acidosis risk elevated with tissue hypoxia (shock, CHF, liver failure) — contraindicated in these; check eGFR regularly"
    ),
    "glipizide": _dr(
        "Second-generation sulfonylurea; closes ATP-sensitive K+ channels on pancreatic beta cells — depolarization → Ca2+ influx → insulin secretion; insulin secretagogue",
        "Type 2 diabetes (monotherapy or add-on); effective only if residual beta-cell function present",
        "Hypoglycemia (most common — avoid in elderly, irregular eaters, CKD; do not skip meals), weight gain, rash, photosensitivity, SIADH (rare)",
        "Most common side effect = hypoglycemia; contraindicated in T1DM (no beta cells); glyburide has longer duration and active metabolites — avoid in elderly/CKD; glipizide preferred (shorter acting, no active metabolites)"
    ),
    "sitagliptin": _dr(
        "DPP-4 inhibitor; inhibits dipeptidyl peptidase-4 which degrades incretins (GLP-1, GIP) — increases active GLP-1 → glucose-dependent insulin secretion, suppresses glucagon",
        "Type 2 diabetes (monotherapy or combination); renal dosing adjustment required; weight neutral",
        "Nasopharyngitis, URI, pancreatitis (rare — monitor for abdominal pain), joint pain (arthralgia — can be severe), heart failure (saxagliptin associated — class concern for some members)",
        "Glucose-dependent mechanism — low hypoglycemia risk when used alone; weight neutral advantage; pancreatitis risk — hold if acute abdominal pain develops; saxagliptin increased HF hospitalizations — avoid in HF"
    ),
    "semaglutide": _dr(
        "GLP-1 receptor agonist (long-acting — once weekly SC or daily oral); mimics GLP-1: glucose-dependent insulin secretion, suppresses glucagon, slows gastric emptying, increases satiety via CNS",
        "Type 2 diabetes (SC weekly Ozempic; oral Rybelsus), obesity/overweight treatment (SC weekly Wegovy — higher dose), cardiovascular risk reduction (T2DM with CVD)",
        "GI side effects (nausea, vomiting, diarrhea — most common; dose-limiting; improve with time), thyroid C-cell tumors (black box — contraindicated in MEN2/medullary thyroid cancer history), pancreatitis (rare), gallbladder disease",
        "SUSTAIN-6 (and SELECT, in obesity without diabetes): cardiovascular benefit; FLOW: kidney benefit in T2DM with CKD; weight loss effect (15-17% body weight) makes Wegovy first-in-class obesity medication; contraindicated in personal/family history of MTC or MEN2; gastroparesis worsened — avoid"
    ),
    "empagliflozin": _dr(
        "SGLT-2 inhibitor; blocks sodium-glucose cotransporter-2 in proximal convoluted tubule — increases glucosuria (~60-80 g/day), reduces renal glucose reabsorption; osmotic diuresis, natriuresis",
        "Type 2 diabetes with cardiovascular disease (reduces MACE), heart failure with reduced ejection fraction (HFrEF — reduces hospitalization and mortality), CKD (slows progression), weight reduction",
        "Genitourinary infections (UTI, mycotic/yeast infections — especially women), DKA (euglycemic — glucose may be normal), Fournier's gangrene (necrotizing fasciitis of perineum — rare), polyuria, dehydration, hypotension, amputation risk (canagliflozin most — monitor feet)",
        "Euglycemic DKA: patient appears relatively well, glucose may be only mildly elevated — check ketones; hold SGLT-2 before surgery/fasting (DKA risk); mechanism in HF/CKD independent of glucose-lowering — benefits even in non-diabetics"
    ),
    "insulin glargine": _dr(
        "Long-acting insulin analog; forms microprecipitate at neutral pH after injection — slow, steady absorption; peakless (flat profile); ~24h duration",
        "Type 1 diabetes (basal insulin — requires meal-time bolus), Type 2 diabetes (basal insulin for inadequate oral control)",
        "Hypoglycemia (less than NPH due to peakless profile), weight gain, lipodystrophy at injection site, hypokalemia",
        "Do NOT mix with other insulins (different pH — precipitates); once daily injection (can be given any time — consistency important); hypoglycemia less common than NPH; U-300 (Toujeo) is concentrated formulation — longer duration"
    ),
    "insulin lispro": _dr(
        "Rapid-acting insulin analog; reversal of amino acids at B28-B29 positions — prevents self-association; onset 15min, peak 60-90min, duration 3-4h",
        "Mealtime (prandial) insulin in T1DM and T2DM, mild-moderate DKA (SC protocols); IV regular insulin is used for hyperkalemia and severe DKA",
        "Hypoglycemia (if meal delayed or insufficient carbs consumed — inject within 15min of meal), weight gain, lipodystrophy",
        "Inject right before meals (or immediately after in uncertain eaters); faster onset than regular insulin (which needs 30min before meal); aspart and glulisine are similar rapid-acting analogs; rapid-acting analogs: lispro, aspart, glulisine"
    ),
    "levothyroxine": _dr(
        "Synthetic T4; converted to active T3 by deiodinases in peripheral tissues; activates nuclear thyroid hormone receptors; increases basal metabolic rate, cardiac output, heat production",
        "Hypothyroidism (drug of choice for all causes), myxedema coma (IV), thyroid cancer (suppressive therapy — supratherapeutic dosing to suppress TSH)",
        "Iatrogenic hyperthyroidism (if over-replaced — palpitations, weight loss, atrial fibrillation, bone loss), minimal when properly dosed; absorption reduced by calcium, iron, antacids (take 30-60min before breakfast)",
        "Take on empty stomach 30-60min before food (or at bedtime 4h after last meal — equally effective); calcium, iron, PPIs reduce absorption; TSH monitoring: check 6-8 weeks after dose change; myxedema coma: IV T4 + IV hydrocortisone (adrenal insufficiency often coexists)"
    ),
    "methimazole": _dr(
        "Thioamide; inhibits thyroid peroxidase (TPO) — blocks iodine oxidation and organification; also blocks iodotyrosine coupling; preferred thioamide (once daily dosing, more potent)",
        "Hyperthyroidism (Graves disease, toxic nodular goiter), pre-operative preparation before thyroidectomy, thyroid storm adjunct",
        "Agranulocytosis (0.5% — check WBC for sore throat/fever; warn patients), rash/pruritus, hepatotoxicity, teratogenic (aplasia cutis, choanal atresia — avoid in 1st trimester)",
        "Preferred over PTU except in 1st trimester pregnancy (where PTU preferred — methimazole causes aplasia cutis); agranulocytosis: stop drug immediately if ANC <1000 (check CBC with differential for any fever/sore throat); does NOT reduce T4 already synthesized — takes weeks to work"
    ),
    "propylthiouracil": _dr(
        "Thioamide; inhibits TPO (same as methimazole) PLUS blocks peripheral conversion of T4 to active T3 (inhibits 5'-deiodinase) — additional advantage in thyroid storm",
        "Hyperthyroidism during first trimester of pregnancy (preferred over methimazole), thyroid storm (high-dose PTU blocks peripheral T4→T3 conversion)",
        "Agranulocytosis (0.5%), severe hepatotoxicity (fulminant hepatic failure — risk higher than methimazole; black box warning), vasculitis (ANCA-positive), rash",
        "PTU preferred only in: 1st trimester pregnancy and thyroid storm; methimazole preferred all other times due to hepatotoxicity risk; PTU requires multiple daily dosing vs. once-daily methimazole"
    ),
    "prednisone": _dr(
        "Synthetic glucocorticoid (prodrug → active prednisolone by 11-beta-HSD); binds glucocorticoid receptor — modulates gene transcription; anti-inflammatory, immunosuppressive, metabolic effects",
        "Inflammatory conditions (asthma exacerbation, COPD exacerbation, IBD, RA, SLE, vasculitis), allergic reactions (anaphylaxis adjunct), nephrotic syndrome, adrenal insufficiency, autoimmune diseases, transplant rejection prevention",
        "Short-term: hyperglycemia, fluid retention, hypertension, insomnia, mood changes, psychosis. Long-term: osteoporosis (supplement Ca + vitamin D), adrenal suppression (HPA axis), Cushing's features (moon face, buffalo hump, striae, central obesity), cataracts, glaucoma, avascular necrosis, muscle wasting, poor wound healing, infection susceptibility, peptic ulcers",
        "HPA suppression: >20mg/day for >3 weeks can suppress HPA axis — taper (do not stop abruptly); stress dosing needed for surgery/illness; give with food to reduce GI effects; use lowest effective dose for shortest duration"
    ),
    "dexamethasone": _dr(
        "Potent synthetic glucocorticoid; minimal mineralocorticoid activity; ~7x potency of prednisone; long half-life; crosses blood-brain barrier well",
        "Cerebral edema (tumors, meningitis), croup (airway edema), COVID-19 (mechanically ventilated/O2-dependent), altitude sickness, Cushing syndrome workup (dexamethasone suppression test), suspected adrenal crisis before an ACTH stimulation test (does not cross-react with cortisol assays), preterm fetal lung maturation (betamethasone preferred), antiemesis (with chemotherapy)",
        "Similar to other glucocorticoids but more potent — hyperglycemia, immunosuppression, adrenal suppression; minimal Na+ retention (no mineralocorticoid activity)",
        "Drug of choice for cerebral edema; no mineralocorticoid effect — preferred when edema is concern; dexamethasone suppression test: normal = cortisol suppressed (hypothalamus/pituitary shut down); Cushing's = cortisol NOT suppressed"
    ),
    "fludrocortisone": _dr(
        "Synthetic mineralocorticoid; acts on aldosterone receptors — promotes Na+ reabsorption and K+/H+ excretion in collecting duct; retains water; has modest glucocorticoid activity",
        "Adrenal insufficiency (primary — Addison's disease; with hydrocortisone), congenital adrenal hyperplasia (CAH — with hydrocortisone), orthostatic hypotension (neurogenic), POTS",
        "Hypertension, edema, hypokalemia (overdosage), headache; mineralocorticoid excess symptoms at high doses",
        "Used ONLY for mineralocorticoid replacement in Addison's disease (hydrocortisone alone insufficient for mineralocorticoid needs); monitor BP and electrolytes; doses in mcg range (0.05-0.2mg) — small changes have large effects"
    ),
    "colchicine": _dr(
        "Binds tubulin — prevents polymerization into microtubules; inhibits neutrophil migration and phagocytosis; prevents urate crystal ingestion by neutrophils",
        "Acute gout attack (most effective if given early — within 12-24h of onset), gout flare prophylaxis during urate-lowering initiation, familial Mediterranean fever (FMF), pericarditis (first-line, with NSAIDs)",
        "GI toxicity (nausea, vomiting, diarrhea — dose-limiting; hallmark of toxicity), myopathy/neuropathy (prolonged use or in renal failure), bone marrow suppression, rhabdomyolysis (with statins)",
        "P-glycoprotein substrate — clarithromycin, cyclosporine, ketoconazole increase levels dramatically (reduce dose); does NOT lower uric acid; GI toxicity is earliest toxicity sign; for a flare, low-dose colchicine (1.2 mg then 0.6 mg 1h later) is as effective as high-dose with far less GI toxicity (AGREE trial)"
    ),
    "allopurinol": _dr(
        "Xanthine oxidase inhibitor; blocks conversion of hypoxanthine → xanthine → uric acid; decreases uric acid production; active metabolite oxypurinol also inhibits XO",
        "Chronic gout (urate-lowering therapy — prevent recurrent attacks, tophi, uric acid nephropathy), tumor lysis syndrome prophylaxis, uric acid nephrolithiasis",
        "Allopurinol hypersensitivity syndrome (AHS) — rash → SJS/TEN, hepatitis, renal failure (HLA-B*5801 in Han Chinese/Korean — screen); acute gout flare (when initiating — start low, titrate slowly, give colchicine prophylaxis); GI upset, rash",
        "Can be started during a flare with anti-inflammatory cover (ACR 2020) — never stop it during a flare; give colchicine prophylaxis for 3-6 months when starting; titrate to uric acid goal <6 mg/dL (or <5 for tophi); HLA-B*5801 testing in high-risk populations; febuxostat = alternative XO inhibitor (non-purine structure)"
    ),
    "febuxostat": _dr(
        "Non-purine selective xanthine oxidase inhibitor; different chemical structure from allopurinol; fully inhibits XO (both oxidized and reduced forms); hepatically metabolized (safe in mild-moderate renal impairment)",
        "Chronic gout (urate-lowering therapy — for patients intolerant or unresponsive to allopurinol), uric acid lowering",
        "Cardiovascular risk (black box: increased CV mortality vs. allopurinol — CARES trial; FDA requires CV safety evaluation; avoid in patients with established CVD if allopurinol is appropriate), gout flare on initiation, nausea, liver function abnormalities",
        "Second-line after allopurinol; avoid in patients with MI or stroke history if allopurinol can be tolerated; safer than allopurinol in HLA-B*5801 carriers (different structure — no AHS risk); expensive vs. allopurinol"
    ),
    "alendronate": _dr(
        "Nitrogen-containing bisphosphonate; binds hydroxyapatite in bone; taken up by osteoclasts — inhibits farnesyl pyrophosphate synthase (FPP synthase) in mevalonate pathway → osteoclast apoptosis; reduces bone resorption",
        "Osteoporosis treatment and prevention (post-menopausal, glucocorticoid-induced), Paget's disease of bone, hypercalcemia of malignancy (IV pamidronate/zoledronic acid)",
        "Esophageal irritation/ulceration (MUST take with full 8oz water, remain upright 30-60min after — contraindicated in esophageal disease), atypical femoral fractures (prolonged use >5yr — 'chalk stick' fractures), osteonecrosis of the jaw (ONJ — rare; especially with dental procedures/IV bisphosphonates), hypocalcemia (correct calcium deficiency first)",
        "Drug holiday after 5 years for low-risk osteoporosis (bisphosphonate incorporated into bone — residual effect); hold before major dental procedures if on IV bisphosphonate; supplement Ca + vitamin D with therapy; once-weekly dosing improves adherence"
    ),
    "omeprazole": _dr(
        "PPI (proton pump inhibitor); prodrug — activated in acidic parietal cell canaliculus; irreversibly binds and inhibits H+/K+-ATPase (proton pump); blocks up to 95% of acid secretion",
        "GERD, peptic ulcer disease (gastric/duodenal — H. pylori eradication regimens, NSAID-induced), Zollinger-Ellison syndrome, prevention of GI bleeding (stress ulcer prophylaxis in ICU), Barrett's esophagus",
        "Hypomagnesemia (long-term — monitor Mg2+ if >1yr use), B12 deficiency (reduced absorption), C. diff (increased risk), osteoporosis/hip fracture (long-term), drug interactions (clopidogrel — omeprazole inhibits CYP2C19 reducing activation; use pantoprazole instead), rebound acid hypersecretion on discontinuation",
        "Use for shortest duration at lowest dose; if needed long-term, reassess periodically; use pantoprazole instead of omeprazole in patients on clopidogrel (less CYP2C19 inhibition); wean gradually to prevent rebound hypersecretion"
    ),
    "ondansetron": _dr(
        "5-HT3 receptor antagonist; blocks serotonin at vagal afferents in GI tract and in chemoreceptor trigger zone (CTZ) of area postrema — anti-emetic",
        "Chemotherapy-induced nausea/vomiting (CINV — gold standard), post-operative nausea/vomiting (PONV), pregnancy nausea/vomiting (hyperemesis gravidarum)",
        "QTc prolongation (dose-dependent — avoid high IV doses; ECG monitoring if cardiac risk factors), headache, constipation, dizziness, serotonin syndrome (rare, with other serotonergic drugs), masking of ileostomy output change",
        "Preferred antiemetic for CINV and PONV; single IV dose max 16 mg (the 32 mg dose was withdrawn for QT prolongation); 5-HT3 antagonists work best for acute CINV (first 24h); add dexamethasone and NK1 antagonist (aprepitant) for highly emetogenic chemotherapy"
    ),
    "metoclopramide": _dr(
        "D2 antagonist (pro-motility) + 5-HT3 antagonist + 5-HT4 agonist; blocks CTZ and peripheral D2 receptors; increases lower esophageal sphincter tone, promotes gastric emptying",
        "Gastroparesis (diabetic and idiopathic), GERD (adjunct), chemotherapy-induced nausea, migraines (IV — with diphenhydramine to prevent EPS), hiccups (intractable)",
        "EPS: acute dystonia, akathisia, drug-induced parkinsonism, tardive dyskinesia (black box warning — avoid >12 weeks); drowsiness, galactorrhea (hyperprolactinemia), QTc prolongation",
        "Black box warning: use >12 weeks associated with irreversible tardive dyskinesia; give with diphenhydramine prophylactically when used for migraines (prevents acute dystonia); avoid in Parkinson's disease (worsens); erythromycin also prokinetic"
    ),
    "lactulose": _dr(
        "Synthetic non-absorbable disaccharide; cleaved by colonic bacteria to organic acids — acidifies colon (traps NH4+), osmotic laxative effect; decreases intestinal ammonia absorption",
        "Hepatic encephalopathy (reduces ammonia by acidifying colon and trapping NH4+, promoting bowel movements — primary treatment), constipation (osmotic laxative)",
        "Diarrhea (dose-limiting — titrate to 2-4 soft stools/day), flatulence, bloating, nausea, abdominal cramping, hypernatremia (if dehydrated from excessive diarrhea)",
        "Goal is 2-4 soft bowel movements per day for hepatic encephalopathy; can be given as retention enema if patient cannot take PO; rifaximin (non-absorbable antibiotic) is add-on or alternative to reduce ammonia-producing bacteria"
    ),
    "rifaximin": _dr(
        "Non-absorbable rifamycin antibiotic; inhibits bacterial RNA synthesis (DNA-dependent RNA polymerase); minimal systemic absorption — acts locally in GI tract",
        "Hepatic encephalopathy (prevention of recurrent episodes — add-on to lactulose), traveler's diarrhea (non-invasive E. coli), IBS-D (irritable bowel syndrome with diarrhea), small intestinal bacterial overgrowth (SIBO)",
        "Well tolerated (systemic absorption <1%); nausea, flatulence, abdominal pain (mild); C. diff (rare given poor systemic bioavailability); peripheral edema in liver disease patients",
        "Unlike most antibiotics, rifaximin stays in GI tract — minimal systemic effects and drug interactions; second-line or adjunct to lactulose in hepatic encephalopathy; used long-term for prevention (6 months of data)"
    ),
    "acetaminophen": _dr(
        "Exact mechanism uncertain; inhibits prostaglandin synthesis centrally (weak COX-1/2 inhibition) + central endocannabinoid system modulation; analgesic and antipyretic but NOT anti-inflammatory",
        "Mild-to-moderate pain (headache, osteoarthritis, post-op pain), fever reduction; preferred analgesic in pregnancy, children, elderly, patients with GI or renal disease, anticoagulated patients",
        "Hepatotoxicity (dose-dependent — toxic metabolite NAPQI accumulates if glutathione depleted; liver necrosis; main cause of acute liver failure in US), nephrotoxicity (chronic high-dose), rash (rare)",
        "Antidote: N-acetylcysteine (NAC) — replenishes glutathione; Rumack-Matthew nomogram guides treatment decisions; max dose 4g/day (3g/day in liver disease/heavy alcohol users); acetaminophen toxicity #1 cause of ALF in US; toxic dose in adults ~7.5-10g"
    ),
    "ibuprofen": _dr(
        "Non-selective NSAID; reversibly inhibits COX-1 and COX-2 — blocks prostaglandin and thromboxane synthesis; anti-inflammatory, analgesic, antipyretic, antiplatelet (reversible)",
        "Pain (mild-moderate — musculoskeletal, dental, headache, dysmenorrhea), fever, inflammatory conditions (arthritis, pericarditis), patent ductus arteriosus closure (indomethacin/ibuprofen in neonates)",
        "GI toxicity (ulcers, bleeding — COX-1 inhibition reduces mucosal protection; give PPI if prolonged use or risk factors), cardiovascular risk (increased MACE — avoid in cardiac patients; naproxen safest NSAID cardiovascular profile), nephrotoxicity (prostaglandin-dependent renal blood flow — avoid in CKD, dehydration, elderly), platelet dysfunction (reversible, unlike aspirin), hypertension, fluid retention",
        "Avoid from 20 weeks of pregnancy (fetal renal dysfunction/oligohydramnios — FDA 2020) and especially in the third trimester (premature ductus closure), post-CABG, severe renal/hepatic failure; combine with PPI if GI risk; celecoxib = selective COX-2 inhibitor (less GI toxicity, same CV risk)"
    ),
    "ketorolac": _dr(
        "Potent NSAID (non-selective COX inhibitor); one of few NSAIDs given IM/IV (others: IV ibuprofen, IV meloxicam, IV indomethacin in neonates); avoids opioid adverse effects; analgesic potency similar to low-dose morphine",
        "Moderate-to-severe acute pain (post-op, renal colic, trauma — opioid-sparing), migraine (IV/IM)",
        "GI bleeding/ulcers (high risk with systemic use), renal toxicity (especially in hypovolemic or elderly patients), platelet dysfunction, cardiovascular risk; avoid >5 days (increased toxicity with prolonged use)",
        "Maximum 5 days total therapy (oral + parenteral combined); higher GI and renal risk than oral NSAIDs (systemic exposure); useful opioid-sparing agent; 30 mg ketorolac IM is roughly equianalgesic to 10 mg morphine IM"
    ),

    "cyclosporine": _dr(
        "Calcineurin inhibitor; binds cyclophilin → complex inhibits calcineurin phosphatase → prevents NFAT dephosphorylation → blocks IL-2 transcription → inhibits T-cell activation and proliferation",
        "Solid organ transplant rejection prophylaxis, bone marrow transplant, psoriasis, rheumatoid arthritis, nephrotic syndrome (steroid-resistant)",
        "Nephrotoxicity (dose-dependent afferent arteriole vasoconstriction — most dose-limiting; monitor creatinine and levels), hypertension, neurotoxicity (tremor, headache, seizures), gingival hyperplasia, hirsutism, hyperlipidemia, hyperkalemia, hypomagnesemia, hyperuricemia/gout",
        "Narrow therapeutic index — TDM essential (trough levels); CYP3A4 substrate — many interactions (azole antifungals, macrolides increase levels; rifampin decreases); grapefruit juice increases levels; nephrotoxicity additive with aminoglycosides, NSAIDs"
    ),
    "tacrolimus": _dr(
        "Calcineurin inhibitor; binds FKBP12 → complex inhibits calcineurin → blocks NFAT → suppresses IL-2 transcription; 100x more potent than cyclosporine",
        "Solid organ transplant (kidney, liver, heart — most commonly used in US), GVHD prevention, atopic dermatitis (topical), autoimmune hepatitis",
        "Nephrotoxicity (similar to cyclosporine), neurotoxicity (tremor, headache, seizures — more than cyclosporine), diabetogenic (impairs insulin secretion — new-onset diabetes after transplant NODAT), hypertension, hyperkalemia, alopecia (unlike cyclosporine — no gingival hyperplasia/hirsutism)",
        "More diabetogenic and more neurotoxic than cyclosporine; less gingival hyperplasia and hirsutism — better cosmetic profile; CYP3A4 substrate (same interactions as cyclosporine); topical tacrolimus for atopic dermatitis — black box (malignancy concern)"
    ),
    "mycophenolate": _dr(
        "Inhibits inosine monophosphate dehydrogenase (IMPDH) — blocks de novo purine synthesis; T and B lymphocytes rely on de novo pathway (lack salvage pathway) → selective lymphocyte suppression",
        "Solid organ transplant (usually combined with calcineurin inhibitor + steroids), lupus nephritis (first-line), IgA nephropathy, ANCA vasculitis",
        "GI toxicity (nausea, vomiting, diarrhea — most common; take with food; EC-MPS formulation better tolerated), leukopenia, anemia, thrombocytopenia, teratogenic (absolute contraindication in pregnancy — symmetrical limb defects, orofacial clefts)",
        "Selective for lymphocytes (lack salvage purine pathway) — less bone marrow toxicity than azathioprine; teratogenic — REMS program, negative pregnancy test required; levels affected by proton pump inhibitors (reduce absorption)"
    ),
    "azathioprine": _dr(
        "Prodrug → 6-mercaptopurine (6-MP; non-enzymatic, glutathione-mediated) → 6-thioguanine nucleotides (6-TGN, active); xanthine oxidase and TPMT inactivate 6-MP → inhibits de novo purine synthesis; incorporated into DNA causing strand breaks; antiproliferative",
        "Autoimmune diseases (Crohn's disease, ulcerative colitis, rheumatoid arthritis, SLE, autoimmune hepatitis, myasthenia gravis), transplant rejection prevention, dermatomyositis",
        "Bone marrow suppression (neutropenia, thrombocytopenia, anemia), GI toxicity (nausea, hepatotoxicity, pancreatitis), malignancy risk (non-melanoma skin cancer, lymphoma), teratogenicity",
        "Allopurinol inhibits xanthine oxidase — markedly increases 6-MP/azathioprine toxicity (can be fatal); MUST reduce azathioprine dose by 75% if using with allopurinol; TPMT genotyping guides dosing (poor metabolizers accumulate 6-TGN)"
    ),
    "sirolimus": _dr(
        "mTOR inhibitor; binds FKBP12 → complex inhibits mTOR kinase → blocks cell cycle progression (G1→S) in response to IL-2; both B and T cell inhibition; antiproliferative",
        "Renal transplant rejection prevention (usually avoiding calcineurin inhibitors to spare kidneys), LAM (lymphangioleiomyomatosis), certain cancers (mTOR pathway tumors), stents (eluting from drug-eluting coronary stents)",
        "Impaired wound healing (delaying introduction after transplant), hyperlipidemia (LDL and triglyceride elevation — most pronounced), thrombocytopenia, pulmonary toxicity (interstitial pneumonitis), oral ulcers, proteinuria, edema",
        "NOT nephrotoxic (unlike calcineurin inhibitors) — but impairs wound healing; delay 2-6 weeks post-transplant before starting; drug-eluting stent coatings (sirolimus, everolimus, paclitaxel) prevent in-stent restenosis; everolimus = structural analog"
    ),
    "methotrexate": _dr(
        "Folate antagonist; inhibits dihydrofolate reductase (DHFR) — blocks purine and pyrimidine synthesis; also increases adenosine release (anti-inflammatory); at high doses: direct cytotoxic; at low doses (weekly): anti-inflammatory",
        "Rheumatoid arthritis (first-line DMARD — weekly low dose), psoriasis, psoriatic arthritis, IBD (Crohn's), DMARD in SLE, chemotherapy (leukemia ALL — high dose, ectopic pregnancy, gestational trophoblastic disease, lymphoma)",
        "Hepatotoxicity/fibrosis (cumulative dose — monitor LFTs, liver biopsy after cumulative dose thresholds), pulmonary toxicity (hypersensitivity pneumonitis — dyspnea/cough), bone marrow suppression (megaloblastic anemia), mucositis/stomatitis, teratogenic (absolute contraindication — neural tube defects), nephrotoxicity (high dose — alkalinize urine and leucovorin rescue)",
        "ECTOPIC PREGNANCY: 50 mg/m² IM single dose; hCG on days 4 and 7 must fall ≥15% (else repeat dose); hold folic acid, NSAIDs and alcohol; contraindicated with rupture/instability, IUP, breastfeeding, abnormal CBC/LFTs/creatinine. Leucovorin rescue: folinic acid bypasses DHFR block — given 24h after high-dose MTX to rescue normal cells; supplemental folic acid given weekly with RA dosing to reduce side effects (does NOT reduce efficacy); renally cleared — toxic with renal failure; NSAIDs reduce renal clearance — dangerous interaction"
    ),
    "cyclophosphamide": _dr(
        "Alkylating agent; prodrug activated by CYP450 to acrolein + phosphoramide mustard; phosphoramide mustard cross-links DNA strands preventing replication; cell-cycle non-specific",
        "Lymphomas, leukemias, multiple myeloma, solid tumors (breast, ovarian), severe autoimmune diseases (lupus nephritis, ANCA vasculitis including GPA), nephrotic syndrome (steroid-resistant)",
        "Hemorrhagic cystitis (acrolein damages bladder epithelium — MUST prehydrate + mesna to bind acrolein; give with aggressive IV fluids), bone marrow suppression, alopecia, nausea/vomiting, SIADH (impairs water excretion at high doses), gonadotoxicity (premature ovarian failure, infertility — counsel and consider fertility preservation), bladder cancer (long-term), secondary malignancies",
        "Mesna is urotoxicity prophylaxis — binds acrolein in urine; adequate hydration essential; high-dose cyclophosphamide can cause SIADH — the large-volume hydration given to prevent cystitis can then cause hyponatremia (use isotonic fluids, monitor Na+); bladder cancer risk persists for years (investigate any hematuria)"
    ),
    "cisplatin": _dr(
        "Platinum coordination compound; enters cells and undergoes aquation → forms intrastrand and interstrand DNA crosslinks (platinum-GG adducts) → inhibits DNA replication; cell-cycle non-specific",
        "Testicular cancer (curative — BEP regimen), ovarian cancer, bladder cancer, head and neck cancers, lung cancer, cervical cancer",
        "Nephrotoxicity (dose-limiting — proximal tubular damage; prehydrate aggressively with IV NS + amifostine; Mg wasting), ototoxicity (sensorineural hearing loss — irreversible; high-frequency first; check audiogram), peripheral neuropathy (dose-cumulative, irreversible), severe nausea/vomiting (most emetogenic chemotherapy — requires ondansetron + NK1 antagonist + dexamethasone), hypomagnesemia, myelosuppression (less than other alkylators)",
        "3 classic toxicities: nephro + oto + peripheral neuropathy; aggressive pre/post hydration (2-3L NS) mandatory; carboplatin = less nephro/neuro/oto toxic but more myelosuppressive — used when renal function compromised; testicular germ cell tumors highly cisplatin-sensitive"
    ),
    "doxorubicin": _dr(
        "Anthracycline; intercalates DNA; inhibits topoisomerase II (prevents re-ligation of DNA strand breaks); generates free radicals (cardiac toxicity); most active in S phase (largely cell-cycle non-specific)",
        "Breast cancer, lymphomas (CHOP; ABVD for Hodgkin), leukemias, sarcomas, ovarian cancer",
        "Cardiotoxicity (cumulative dose-dependent cardiomyopathy — dilated CM; lifetime cumulative dose limit ~550 mg/m2; monitor ECHO/MUGA before and during; dexrazoxane for iron chelation/cardioprotection), myelosuppression (dose-limiting), alopecia, severe nausea, mucositis, red urine (warn patients — not hematuria), vesicant (extravasation causes severe tissue necrosis)",
        "Cumulative cardiotoxicity — keep lifetime dose under limits; dexrazoxane cardioprotective for patients exceeding threshold; liposomal doxorubicin (Doxil) less cardiotoxic; extravasation: stop infusion, aspirate, cold compress, dexrazoxane antidote"
    ),
    "bleomycin": _dr(
        "Glycopeptide antibiotic; binds DNA + Fe2+ → generates free radicals → DNA strand breaks; minimal myelosuppression (unique among chemotherapy)",
        "Testicular cancer (BEP — bleomycin/etoposide/cisplatin), Hodgkin lymphoma (ABVD), sclerotherapy (pleural effusions), warts",
        "Pulmonary toxicity (most serious — pulmonary fibrosis; dose-cumulative; worsened by high FiO2 — avoid supplemental O2 unless SpO2 <88%; chest CT + PFTs baseline and during treatment), Raynaud's phenomenon, skin changes (hyperpigmentation, flagellate dermatitis), fever/chills (test dose in lymphoma patients due to anaphylaxis risk — though no longer recommended universally), mucositis",
        "MINIMAL bone marrow suppression — unique advantage; bleomycin + high FiO2 during anesthesia = ARDS risk — alert anesthesiologist; Raynaud's can persist for years after treatment; bleomycin hydrolase absent in skin and lungs — explains organ-specific toxicity"
    ),
    "vincristine": _dr(
        "Vinca alkaloid; binds beta-tubulin — prevents polymerization into mitotic spindle (M-phase specific); cell death by mitotic arrest",
        "Leukemia (ALL — mainstay), lymphoma (CHOP), Wilms tumor, neuroblastoma, Ewing sarcoma, multiple myeloma",
        "Peripheral neuropathy (dose-limiting — sensorimotor neuropathy; dose-dependent; may be irreversible with high cumulative dose), constipation (autonomic neuropathy — prophylax with stool softeners/laxatives), SIADH, jaw pain (first cycle), alopecia; MINIMAL myelosuppression",
        "If vincristine ever accidentally given intrathecally — FATAL; must be dispensed in minibag (not syringe) to prevent IT administration; peripheral neuropathy most dose-limiting; constipation from autonomic neuropathy — must give stool softeners prophylactically"
    ),
    "paclitaxel": _dr(
        "Taxane; binds beta-tubulin and STABILIZES polymerized microtubules — prevents depolymerization; microtubule hyperstabilization arrests mitosis (M-phase specific); different mechanism from vinca alkaloids",
        "Breast cancer (adjuvant and metastatic), ovarian cancer (first-line with carboplatin), lung cancer, Kaposi sarcoma, pancreatic cancer (nab-paclitaxel), cervical cancer",
        "Peripheral neuropathy (dose-limiting — sensorimotor; often persistent post-treatment), hypersensitivity reactions (Cremophor EL vehicle — premedicate with dexamethasone + diphenhydramine + H2 blocker; nab-paclitaxel albumin-bound formulation reduces HSR), myelosuppression (neutropenia), alopecia, bradycardia (asymptomatic — infusion-related), arthralgias/myalgias (2-3 days after each cycle)",
        "Premedicate before every infusion (hypersensitivity to Cremophor); nab-paclitaxel (Abraxane) = albumin-bound formulation — no Cremophor, less hypersensitivity, higher tissue concentration; alopecia typically complete; neutrophil nadir day 8-11"
    ),
    "5-fluorouracil": _dr(
        "Pyrimidine antimetabolite; converted to FdUMP — inhibits thymidylate synthase (TS) → blocks dTMP synthesis → impaired DNA synthesis; also incorporated into RNA as FUTP → RNA dysfunction; S-phase specific",
        "Colorectal cancer (adjuvant and metastatic — FOLFOX/FOLFIRI regimens), breast cancer, head and neck cancers, pancreatic cancer, anal cancer, topical (actinic keratosis, basal cell carcinoma)",
        "Myelosuppression, mucositis/stomatitis (dose-limiting with bolus dosing), hand-foot syndrome (palmar-plantar erythrodysesthesia — with continuous infusion), diarrhea, cardiotoxicity (coronary artery vasospasm — ischemia/MI in ~1%; particularly with cisplatin), neurotoxicity (cerebellar ataxia — rare)",
        "Leucovorin (folinic acid) potentiates 5-FU by stabilizing FdUMP-TS complex — co-administered in colorectal regimens; DPD deficiency (dihydropyrimidine dehydrogenase — enzyme that catabolizes 5-FU): life-threatening toxicity; cardiotoxicity rare but potentially fatal — screen for symptoms"
    ),
    "hydroxyurea": _dr(
        "Ribonucleotide reductase inhibitor — blocks conversion of ribonucleotides to deoxyribonucleotides; depletes dNTP pool → S-phase arrest; increases HbF production in sickle cell disease (mechanism incompletely understood — myelosuppression and increased erythropoiesis drive HbF induction)",
        "Sickle cell disease (reduces painful crises by 50%, acute chest syndrome, need for transfusion; increases HbF), CML (chronic phase), essential thrombocythemia, polycythemia vera, cervical cancer (with radiation)",
        "Bone marrow suppression (neutropenia, thrombocytopenia, anemia — monitor CBC regularly), leg ulcers (long-term use), teratogenic (avoid in pregnancy), skin changes, mucositis, secondary leukemia (rare, long-term)",
        "First disease-modifying therapy for sickle cell disease; typically see HbF rise in 2-3 months; hydration and leg care to prevent/treat leg ulcers; check CBC every 4-8 weeks — hold if significant cytopenias; contraception essential during use"
    ),
    "rituximab": _dr(
        "Chimeric monoclonal antibody targeting CD20 on B cells; binds CD20 → antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity, direct apoptosis → B-cell depletion",
        "B-cell non-Hodgkin lymphoma (CD20+), CLL, rheumatoid arthritis (anti-TNF failure), ANCA vasculitis (GPA, MPA), immune thrombocytopenia (ITP), TTP (refractory), MS (off-label), pemphigus vulgaris",
        "Infusion reactions (fever, chills, hypotension — most common first infusion; premedicate with acetaminophen/diphenhydramine/steroids), severe mucocutaneous reactions (SJS), hepatitis B reactivation (screen all patients for HBsAg/HBcAb before — give prophylaxis), progressive multifocal leukoencephalopathy (PML — JC virus), hypogammaglobulinemia (prolonged B-cell depletion), cytopenias",
        "Screen ALL patients for hepatitis B before administration — reactivation can be fatal; PML risk (JC virus) — lower than natalizumab but monitor for neurological changes; immunoglobulins recover slowly after B-cell depletion — increased infection risk months post-treatment"
    ),
    "imatinib": _dr(
        "BCR-ABL tyrosine kinase inhibitor (TKI); occupies ATP-binding site of BCR-ABL kinase → blocks phosphorylation of downstream substrates; also inhibits PDGFR and c-KIT",
        "CML (chronic myeloid leukemia — BCR-ABL+; first-line for chronic phase), GIST (gastrointestinal stromal tumor — c-KIT+), Ph+ ALL",
        "Edema/fluid retention (periorbital, pleural effusion, ascites — especially in elderly), nausea (take with food), muscle cramps, myelosuppression, hepatotoxicity, QTc prolongation, rash",
        "First small-molecule tyrosine kinase inhibitor (2001); BCR-ABL mutation T315I ('gatekeeper mutation') confers resistance to imatinib and 2nd-gen TKIs — requires ponatinib; second-generation TKIs (dasatinib, nilotinib) more potent for imatinib-resistant CML; imatinib + GIST: 80% response rate in c-KIT+ tumors"
    ),
    "trastuzumab": _dr(
        "Humanized monoclonal antibody targeting HER2 (ErbB2) extracellular domain; blocks HER2 signaling, antibody-dependent cellular cytotoxicity (ADCC), prevents HER2 cleavage",
        "HER2-positive breast cancer (early-stage adjuvant — dramatically reduces recurrence; metastatic — combined with chemotherapy), HER2-positive gastric/gastroesophageal junction adenocarcinoma",
        "Cardiotoxicity (cardiomyopathy, LV dysfunction — NOT cumulative dose-dependent unlike anthracyclines; reversible on stopping; monitor ECHO every 3 months), infusion reactions (usually mild), pulmonary toxicity (rare), diarrhea",
        "HER2 testing required before prescribing (IHC 3+ or FISH amplified); cardiotoxicity additive with anthracyclines — avoid concurrent use (give sequentially in adjuvant); reversible cardiomyopathy (unlike doxorubicin); pertuzumab added for metastatic disease (dual HER2 blockade)"
    ),
    "bevacizumab": _dr(
        "Humanized monoclonal antibody against VEGF (vascular endothelial growth factor); blocks VEGF from binding VEGFR — inhibits angiogenesis, normalizes tumor vasculature",
        "Metastatic colorectal cancer, NSCLC (non-squamous), renal cell carcinoma, glioblastoma, cervical cancer, ovarian cancer",
        "Hypertension (most common — treat with antihypertensives; dose-reduce if severe), thromboembolism (VTE and arterial — increases clotting risk), bleeding/hemorrhage (hemoptysis — contraindicated in squamous NSCLC due to fatal hemoptysis), poor wound healing/wound dehiscence (stop ≥28 days before elective surgery; restart ≥28 days after, once the wound has healed), GI perforation (rare but serious), proteinuria, posterior reversible encephalopathy syndrome (PRES)",
        "Hold ≥4 weeks (28 days) before and after elective surgery (impaired wound healing); do NOT use in squamous cell lung cancer (fatal pulmonary hemorrhage); hypertension usually manageable but requires monitoring; anti-VEGF mechanism normalizes leaky tumor vasculature — improves chemotherapy delivery"
    ),
    "hydroxychloroquine": _dr(
        "Aminoquinoline antimalarial; accumulates in lysosomes — increases lysosomal pH (alkalinizes acidic compartments); disrupts antigen processing and presentation; reduces inflammatory cytokines (TNF, IL-1); also inhibits TLR signaling",
        "Systemic lupus erythematosus (cornerstone of therapy — reduces flares, organ damage, mortality, thrombosis; continue throughout pregnancy), rheumatoid arthritis (DMARD), discoid lupus, Sjogren's syndrome, malaria prophylaxis and treatment",
        "Retinal toxicity (chloroquine retinopathy — 'bull's eye' maculopathy; dose-dependent and cumulative; annual ophthalmology exams after 5yr; irreversible — screening aims to catch it early), GI upset (nausea, take with food), QTc prolongation, skin hyperpigmentation, myopathy/cardiomyopathy (rare, long-term)",
        "Annual ophthalmology exam after 5 years of use (or earlier if high risk); keep dose ≤5 mg/kg/day of actual body weight to reduce retinal risk (AAO 2016); one of safest long-term immunosuppressants in pregnancy; reduces mortality and cardiovascular events in SLE independent of disease control"
    ),

    # ── Anticoagulant reversal agents ──────────────────────────────────────
    "protamine sulfate": _dr(
        "Strongly cationic protein (from salmon sperm) that forms stable complex with heparin (strongly anionic) → ionic binding inactivates heparin anticoagulant activity; partially reverses LMWH (enoxaparin) — reverses anti-IIa activity but not anti-Xa activity",
        "Heparin overdose/reversal (complete), LMWH reversal (partial — reverses ~60%), post-cardiopulmonary bypass heparin reversal",
        "Hypotension, bradycardia, pulmonary hypertension (give slowly IV), anaphylaxis/anaphylactoid reactions (higher risk in fish allergy, prior protamine exposure, vasectomized men — anti-protamine antibodies), anticoagulant rebound (protamine-heparin complex dissociates)",
        "1mg protamine neutralizes ~100 units of heparin (or 1mg enoxaparin); give slowly over 10 minutes; anaphylaxis risk elevated in fish/salmon allergy and prior NPH insulin use (NPH contains protamine); anticoagulant rebound 30-90 minutes post-administration — monitor"
    ),
    "idarucizumab": _dr(
        "Humanized monoclonal antibody fragment (Fab) with 350× higher affinity for dabigatran than thrombin; binds both free and thrombin-bound dabigatran → rapid reversal within minutes",
        "Dabigatran (direct thrombin inhibitor) reversal in life-threatening bleeding or emergency surgery; brand name Praxbind",
        "Hypersensitivity reactions (rare), thromboembolic events (after reversal — underlying thrombotic risk reasserts); headache; generally very well tolerated",
        "Specific antidote for dabigatran ONLY — does not reverse factor Xa inhibitors (apixaban, rivaroxaban); 5g IV in two 2.5g doses given consecutively; resume anticoagulation as soon as medically appropriate; RE-VERSE AD trial: >98% reversal within minutes"
    ),
    "andexanet alfa": _dr(
        "Recombinant modified factor Xa decoy protein with no catalytic activity; binds and sequesters factor Xa inhibitors (apixaban, rivaroxaban) with high affinity → reduces anti-Xa activity",
        "Reversal of apixaban and rivaroxaban in life-threatening or uncontrolled bleeding; brand name Andexxa",
        "Thromboembolic events (MI, stroke, DVT, PE — significantly elevated risk ~18% in 30 days; weigh carefully), infusion reactions (flushing, urticaria, feeling hot), very expensive",
        "Specific antidote for factor Xa inhibitors — not for dabigatran; high cost ($25,000+ per dose); significant thromboembolism risk post-reversal — restart anticoagulation as soon as possible; 4-factor PCC is alternative for factor Xa reversal when andexanet unavailable"
    ),
    "4-factor pcc": _dr(
        "Prothrombin Complex Concentrate containing factors II, VII, IX, X (all vitamin K-dependent factors) + Protein C and S; rapidly restores vitamin K-dependent factor levels",
        "Warfarin reversal (urgent/emergent — faster than vitamin K alone; gives immediate factor replacement), factor Xa inhibitor reversal (off-label when andexanet unavailable), factor II or X deficiency",
        "Thromboembolic events (DIC, MI, PE, DVT — contains procoagulant factors), hypersensitivity reactions (heparin-containing products — HIT risk), volume overload (much less than FFP)",
        "For warfarin reversal: 4-factor PCC + vitamin K together — PCC gives immediate reversal, vitamin K prevents recurrence; faster and smaller volume than FFP; Kcentra is FDA-approved brand in US; dosing based on INR and weight"
    ),
    "vitamin k": _dr(
        "Fat-soluble vitamin; cofactor for gamma-carboxylation of glutamate residues on coagulation factors II, VII, IX, X, Protein C, Protein S — necessary for functional coagulation factor synthesis",
        "Warfarin reversal (non-urgent — takes 12-24h for oral, 6-12h for IV; restores factor synthesis), vitamin K deficiency (malabsorption, prolonged antibiotics, newborn prophylaxis), reversal of supratherapeutic INR",
        "Anaphylaxis (IV phytonadione — rare but serious; give slowly diluted; oral preferred when possible), warfarin resistance (can make re-anticoagulation difficult for 1-2 weeks after large doses of vitamin K)",
        "IV vitamin K effect begins in 6-12h but takes 24-48h for full effect — use PCC/FFP for emergent reversal; phytonadione (K1) is the form used therapeutically; warfarin works by antagonizing vitamin K; newborn prophylaxis prevents hemorrhagic disease of the newborn"
    ),
    # ── Biologics / DMARDs ─────────────────────────────────────────────────
    "adalimumab": _dr(
        "Fully human monoclonal IgG1 antibody against TNF-alpha; neutralizes both soluble and membrane-bound TNF; prevents TNF from binding its receptors → blocks downstream inflammatory cascade",
        "Rheumatoid arthritis (first biologic after methotrexate failure), ankylosing spondylitis, psoriatic arthritis, Crohn's disease, ulcerative colitis, plaque psoriasis, uveitis; brand name Humira (one of the top-selling drugs ever)",
        "Reactivation of latent TB (screen with TST/IGRA before starting), serious infections (bacterial, fungal, viral), demyelinating disease (worsens MS — avoid), CHF worsening (avoid in moderate-severe CHF), lupus-like syndrome, injection site reactions, malignancy risk (lymphoma)",
        "Screen for LTBI (latent TB) with TST or IGRA before ALL anti-TNF biologics; treat LTBI before starting; hepatitis B reactivation — screen HBsAg/HBcAb; live vaccines contraindicated during therapy; many biosimilars now available (Hadlima, Hyrimoz, Cyltezo)"
    ),
    "infliximab": _dr(
        "Chimeric (human/mouse) IgG1 monoclonal antibody against TNF-alpha; binds both soluble and membrane-bound TNF; given IV infusion only (unlike adalimumab which is SC)",
        "RA (with methotrexate), Crohn's disease (including fistulizing — first biologic approved for Crohn's), ulcerative colitis, ankylosing spondylitis, psoriatic arthritis, plaque psoriasis; brand name Remicade",
        "Infusion reactions (fever, chills, urticaria, hypotension — during infusion; premedicate with acetaminophen/antihistamine/steroids), same black box as adalimumab (TB reactivation, serious infections, malignancy), immunogenicity (anti-drug antibodies → loss of response — concomitant immunosuppressant reduces antibody formation), CHF worsening",
        "Chimeric structure → higher immunogenicity than fully human adalimumab; concurrent MTX reduces antibody formation and improves durability; drug level monitoring and anti-drug antibody testing guide dosing adjustments; TB screening mandatory before starting"
    ),
    "etanercept": _dr(
        "Fusion protein: two p75 TNF receptor domains fused to Fc portion of human IgG1; decoy receptor that binds and neutralizes TNF-alpha and lymphotoxin-alpha (TNF-beta); does NOT bind to membrane-bound TNF",
        "RA, psoriatic arthritis, ankylosing spondylitis, plaque psoriasis, juvenile idiopathic arthritis; brand name Enbrel",
        "Same anti-TNF class effects: serious infections, TB reactivation (lower risk than infliximab — does not bind membrane TNF), demyelination risk, CHF worsening, injection site reactions, malignancy",
        "Lower TB reactivation risk compared to monoclonal anti-TNF antibodies (does not lyse TNF-producing granuloma cells); still requires LTBI screening before starting; NOT effective for IBD (unlike infliximab/adalimumab) — does not bind membrane-bound TNF"
    ),
    "tocilizumab": _dr(
        "Humanized monoclonal antibody against IL-6 receptor (IL-6R); blocks IL-6 signaling — reduces acute phase reactants, inflammation, and fever; IL-6 drives CRS and cytokine storm",
        "RA (after anti-TNF failure), giant cell arteritis (first biologic approved for GCA), systemic juvenile idiopathic arthritis, cytokine release syndrome (CRS from CAR-T therapy — drug of choice), COVID-19 (mechanically ventilated patients — reduces mortality)",
        "Serious infections (IL-6 suppression masks fever — infections may present without fever), hepatotoxicity (LFT elevation), neutropenia, thrombocytopenia, hyperlipidemia, GI perforation (especially in diverticulitis), no fever as infection signal — watch other signs",
        "IL-6 mediates fever response — tocilizumab masks fever as an infection sign; particularly useful in CRS from immunotherapy; COVID-19 trials (RECOVERY, REMAP-CAP) demonstrated mortality benefit in severe disease; IGRA/TST screening before starting (TB risk)"
    ),
    "abatacept": _dr(
        "Fusion protein: CTLA-4 extracellular domain + IgG1 Fc; binds CD80/CD86 on APCs → blocks CD28 co-stimulation → T-cell anergy/non-activation; selective T-cell co-stimulation modulator",
        "RA (after methotrexate failure — alternative to anti-TNF; preferred in patients with high infection risk or history of TB), psoriatic arthritis, juvenile idiopathic arthritis; brand name Orencia",
        "Serious infections (lower risk than anti-TNF agents), headache, nausea, infusion reactions (IV formulation), COPD exacerbations (increased risk in COPD patients — avoid), malignancy risk",
        "Preferred over anti-TNF in patients at high infection risk (elderly, COPD, prior TB) — generally safer infection profile; TB screening still recommended before starting (lower reactivation risk than anti-TNF); avoid live vaccines"
    ),
    "ustekinumab": _dr(
        "Human monoclonal antibody against p40 subunit shared by IL-12 and IL-23; blocks Th1 (via IL-12) and Th17 (via IL-23) pathways — key in psoriasis and IBD pathogenesis",
        "Moderate-severe plaque psoriasis, psoriatic arthritis, Crohn's disease (moderate-severe — after failure of conventional therapy or anti-TNF), ulcerative colitis; brand name Stelara",
        "Upper respiratory infections, headache, fatigue, injection site reactions; generally well tolerated — favorable safety profile vs. anti-TNF; serious infections (rare), malignancy risk (theoretical), reversible posterior leukoencephalopathy (RPLS, very rare)",
        "Favorable safety profile — TB screening recommended before starting; effective for both skin and gut manifestations; given as IV induction then SC maintenance; does not increase risk of opportunistic infections as much as anti-TNF; no CHF worsening concerns"
    ),
    "secukinumab": _dr(
        "Human monoclonal antibody targeting IL-17A; blocks IL-17A from binding its receptor → reduces neutrophil recruitment and keratinocyte activation; IL-17A is a key driver of psoriasis and spondyloarthritis",
        "Moderate-severe plaque psoriasis (excellent efficacy — superior to anti-TNF for skin), psoriatic arthritis, ankylosing spondylitis (highly effective); brand name Cosentyx",
        "Nasopharyngitis, upper respiratory infections, Candida infections (IL-17A is critical for mucosal Candida defense — monitor for oral/vaginal candidiasis), IBD exacerbation or new onset (avoid in IBD — can worsen Crohn's and UC), injection site reactions",
        "Do NOT use in IBD — IL-17 blockade worsens inflammatory bowel disease; excellent efficacy for axial spondyloarthritis and psoriasis; Candida infections manageable with antifungals; low TB reactivation risk (still screen before starting); ixekizumab and bimekizumab = related IL-17 inhibitors"
    ),
    # ── HIV antiretrovirals ────────────────────────────────────────────────
    "tenofovir": _dr(
        "Nucleotide reverse transcriptase inhibitor (NtRTI); tenofovir alafenamide (TAF) or tenofovir disoproxil fumarate (TDF); phosphorylated to tenofovir diphosphate → inhibits HIV and HBV reverse transcriptase by chain termination",
        "HIV treatment (component of first-line regimens — Truvada: TDF+FTC; Descovy: TAF+FTC), PrEP (HIV pre-exposure prophylaxis), chronic hepatitis B treatment",
        "TDF: nephrotoxicity (Fanconi syndrome — proximal tubular injury; monitor creatinine, phosphate, urine protein), bone density loss (decreased BMD — monitor with DEXA); TAF: significantly less nephrotoxicity and bone toxicity than TDF (preferred in renal/bone risk); both: hepatitis B flare if stopped abruptly in HBV co-infected patients",
        "TAF preferred over TDF in patients with renal disease or osteoporosis; do NOT stop abruptly in HBV/HIV co-infection — severe hepatitis flare; PrEP with TDF+FTC: >99% effective if taken daily; emtricitabine (FTC) almost always paired with tenofovir"
    ),
    "emtricitabine": _dr(
        "Nucleoside reverse transcriptase inhibitor (NRTI); cytidine analog; phosphorylated to FTC triphosphate → competitive inhibitor of HIV reverse transcriptase with chain termination; also active against HBV",
        "HIV treatment (paired with tenofovir in nearly all first-line regimens — Truvada, Descovy, Biktarvy, Genvoya), PrEP, hepatitis B (second-line)",
        "Minimal adverse effects — generally well tolerated; skin hyperpigmentation (palms/soles — more common in darker-skinned individuals), headache, nausea; HBV flare if stopped in co-infected patients; resistance mutation M184V",
        "M184V resistance mutation — reduces FTC efficacy but also reduces viral fitness and improves susceptibility to tenofovir; HBV co-infection: stopping FTC can cause severe hepatitis flare; nearly always used in combination (never monotherapy)"
    ),
    "efavirenz": _dr(
        "Non-nucleoside reverse transcriptase inhibitor (NNRTI); non-competitive inhibitor of HIV-1 reverse transcriptase; binds allosteric hydrophobic pocket — does not require phosphorylation",
        "HIV treatment (component of Atripla: EFV+TDF+FTC — once-daily single tablet regimen); historically first-line but now largely replaced by integrase inhibitors (better tolerated)",
        "CNS effects (most common — vivid dreams, nightmares, insomnia, dizziness, depression, hallucinations — occur in ~50%; worst in first 2-4 weeks, usually improve; take at bedtime); rash (SJS rarely), hepatotoxicity, hyperlipidemia, QTc prolongation, teratogenic (neural tube defects in animals — avoid in 1st trimester/pregnancy)",
        "Take at bedtime to minimize CNS effects (sleep through peak levels); CYP3A4 inducer AND substrate — many drug interactions; K103N mutation = resistance (single mutation causes high-level resistance); replaced by dolutegravir/bictegravir in most guidelines — better CNS tolerability"
    ),
    "dolutegravir": _dr(
        "Integrase strand transfer inhibitor (INSTI); binds integrase active site → prevents insertion of HIV DNA into host genome; second-generation INSTI (more potent, higher genetic barrier to resistance vs. raltegravir)",
        "HIV treatment (preferred first-line — current WHO and DHHS guidelines; component of Triumeq: DTG+ABC+3TC; Dovato: DTG+3TC); components of Biktarvy: BIC+TAF+FTC (bictegravir = similar INSTI)",
        "Weight gain (class effect for INSTIs — metabolic implications), neuropsychiatric effects (insomnia, depression, anxiety — less than efavirenz but real), hypersensitivity reactions with abacavir (HLA-B*5701 testing before abacavir — NOT dolutegravir itself), potential neural tube defects (periconceptional — counseling required)",
        "High genetic barrier to resistance — very few resistance mutations; generally better tolerated than efavirenz; early neural-tube-defect signal (Tsepamo study, Botswana) fell to ~0.1% with more data — dolutegravir is now preferred in pregnancy; take 2h before or 6h after antacids, iron or calcium (chelation)"
    ),
    "ritonavir": _dr(
        "HIV protease inhibitor (PI); inhibits HIV protease → prevents cleavage of viral polyproteins → immature non-infectious virions; at low doses: potent CYP3A4 inhibitor (pharmacokinetic booster — increases levels of co-administered PIs)",
        "HIV treatment — primarily used as pharmacokinetic booster (low-dose 100-200mg) to increase levels of other PIs (lopinavir/r, darunavir/r, atazanavir/r), not as sole antiretroviral at full dose; nirmatrelvir/ritonavir (Paxlovid) = COVID-19 treatment",
        "GI toxicity (diarrhea, nausea, vomiting — dose-related; dose-dependent), hepatotoxicity, hyperlipidemia (marked elevation in triglycerides and LDL), hyperglycemia, lipodystrophy (fat redistribution — buffalo hump, truncal obesity, facial wasting), drug interactions (potent CYP3A4 inhibitor — contraindicated with many drugs)",
        "Ritonavir at therapeutic doses is poorly tolerated; used exclusively as booster in HIV; Paxlovid (nirmatrelvir/ritonavir) for COVID-19: ritonavir boosts nirmatrelvir levels; check drug interactions carefully — ritonavir inhibits CYP3A4 and P-gp dramatically (statins, immunosuppressants, many others)"
    ),
    "darunavir": _dr(
        "Second-generation HIV protease inhibitor; binds HIV protease active site with high affinity; must be boosted with cobicistat or ritonavir (CYP3A4 inhibitor) to achieve adequate levels; high genetic barrier to resistance",
        "HIV treatment (preferred PI in first-line or treatment-experienced regimens; preferred PI in pregnancy); Prezcobix = darunavir/cobicistat; Symtuza = DRV/c/TAF/FTC",
        "GI effects (nausea, diarrhea — milder than older PIs), rash (sulfonamide moiety — caution in sulfa allergy), hepatotoxicity (monitor LFTs), metabolic effects (hyperlipidemia, hyperglycemia, lipodystrophy — less than older PIs), drug interactions (CYP3A4 substrate — ritonavir/cobicistat boosts levels)",
        "Preferred PI in pregnancy (robust safety data); high genetic barrier to resistance — requires multiple mutations; cobicistat vs. ritonavir as booster: equivalent pharmacokinetic effect, cobicistat has no antiretroviral activity; must be taken with food"
    ),
    "raltegravir": _dr(
        "First-generation HIV integrase strand transfer inhibitor (INSTI); competitively inhibits strand transfer step of integration of viral DNA into host chromosome; twice-daily dosing (once-daily 1200 mg option)",
        "HIV treatment (alternative first-line; preferred in pregnancy — long safety data; preferred when avoiding drug interactions important); Isentress",
        "Nausea, headache, diarrhea, insomnia (generally well tolerated), rhabdomyolysis (rare), psychiatric symptoms, immune reconstitution inflammatory syndrome (IRIS); lower genetic barrier to resistance than dolutegravir (Q148 + secondary mutations)",
        "Lower genetic barrier to resistance vs. dolutegravir — once-daily DTG generally preferred unless drug interactions or pregnancy (where raltegravir has more data); IRIS: paradoxical worsening when immune system reconstitutes — not drug failure; safe in renal and hepatic impairment"
    ),
    "maraviroc": _dr(
        "CCR5 antagonist/entry inhibitor; binds CCR5 co-receptor on CD4+ T cells → conformational change prevents gp120 from binding → blocks HIV-1 entry; ONLY active against CCR5-tropic HIV-1 (R5 virus)",
        "HIV treatment — treatment-experienced patients with documented CCR5-tropic virus (requires tropism testing before use); Selzentry/Celsentri; useful when resistance to other classes",
        "Hepatotoxicity (may be preceded by allergic reaction), orthostatic hypotension (CYP3A4 substrate — ritonavir doubles levels), upper respiratory infections, cough, dizziness, abdominal pain; immune reconstitution inflammatory syndrome",
        "REQUIRES tropism assay (Trofile) before use — will not work against CXCR4-tropic or dual-tropic HIV; if CXCR4-tropic virus present, viral variants may emerge on maraviroc; unique mechanism — blocks entry rather than replication"
    ),
    # ── Checkpoint inhibitors ─────────────────────────────────────────────
    "pembrolizumab": _dr(
        "Humanized IgG4 monoclonal antibody against PD-1 (programmed death-1) receptor; blocks PD-1/PD-L1 interaction → restores anti-tumor T-cell activity; T-cell checkpoint inhibitor",
        "Multiple cancers: melanoma (adjuvant and metastatic), NSCLC (high PD-L1 expression, first-line; combination with chemotherapy), head and neck SCC, urothelial carcinoma, MSI-H/dMMR tumors (any solid tumor — tumor-agnostic approval), cervical, gastric, TMB-high tumors; brand name Keytruda",
        "Immune-related adverse events (irAEs) — can affect any organ: pneumonitis (cough, dyspnea — most common lethal irAE), colitis/diarrhea, hepatitis (elevated LFTs), endocrinopathies (thyroiditis, adrenal insufficiency, hypophysitis, T1DM), dermatitis (rash, vitiligo), nephritis, neurotoxicity; irAEs treated with corticosteroids",
        "MSI-H/dMMR tumor-agnostic approval (2017) = first ever histology-agnostic cancer approval; all irAEs treated with steroids (prednisone 1-2 mg/kg); most irAEs reversible except endocrinopathies (often permanent — lifetime hormone replacement needed); PD-L1 expression predicts but doesn't guarantee response"
    ),
    "nivolumab": _dr(
        "Fully human IgG4 monoclonal antibody against PD-1; same checkpoint target as pembrolizumab (different antibody); restores T-cell anti-tumor immunity by blocking PD-1/PD-L1 and PD-1/PD-L2",
        "Melanoma (among the first PD-1 inhibitors approved, 2014; first-line metastatic), NSCLC, renal cell carcinoma, Hodgkin lymphoma (relapsed/refractory), urothelial carcinoma, head and neck SCC, colorectal cancer (MSI-H), gastric cancer; brand name Opdivo",
        "Same irAE profile as pembrolizumab: pneumonitis, colitis, hepatitis, endocrinopathies, nephritis, dermatitis, neurotoxicity; CheckMate trials established efficacy; combination with ipilimumab (dual checkpoint blockade) increases efficacy but significantly increases irAE frequency and severity",
        "Ipilimumab + nivolumab combination has highest response rates in melanoma and RCC but ~50-60% grade 3-4 irAEs; Opdualag = nivolumab + relatlimab (LAG-3 inhibitor) approved for melanoma; irAE management identical to pembrolizumab"
    ),
    "ipilimumab": _dr(
        "Human IgG1 monoclonal antibody against CTLA-4 (cytotoxic T-lymphocyte antigen-4); blocks CTLA-4/B7 interaction → prevents T-cell inhibition in lymph nodes → enhances T-cell priming and activation; different mechanism from PD-1 inhibitors",
        "Melanoma (first checkpoint inhibitor approved — 2011; adjuvant and metastatic, often combined with nivolumab), RCC (with nivolumab), colorectal cancer MSI-H (with nivolumab), NSCLC (with nivolumab + chemotherapy); brand name Yervoy",
        "irAEs more frequent and severe than PD-1 inhibitors (especially colitis — dose-dependent; serious colitis in ~30% at higher doses); colitis, hepatitis, hypophysitis (anterior pituitary insufficiency — headache, fatigue, hypopituitarism), dermatitis, uveitis; combined with nivolumab: dramatically increased irAE rate",
        "First checkpoint inhibitor approved — landmark survival benefit in metastatic melanoma; hypophysitis: permanent pituitary damage → lifetime corticosteroid + thyroid replacement; dose-dependent irAE frequency (10 mg/kg more toxic than 3 mg/kg)"
    ),
    "atezolizumab": _dr(
        "Humanized IgG1 monoclonal antibody against PD-L1 (not PD-1); blocks PD-L1/PD-1 AND PD-L1/CD80 interactions; preserves PD-L2/PD-1 signaling (theoretical benefit for reduced irAE — not clearly demonstrated); IgG1 Fc modified to prevent antibody-dependent cytotoxicity",
        "NSCLC (with or without chemotherapy), triple-negative breast cancer (US indication withdrawn 2021), urothelial carcinoma, small cell lung cancer (with chemotherapy), hepatocellular carcinoma (with bevacizumab); brand name Tecentriq",
        "Similar irAE profile to PD-1 inhibitors: pneumonitis, colitis, hepatitis, endocrinopathies, dermatitis; infusion reactions",
        "PD-L1 vs. PD-1 inhibitor — targeting PD-L1 on tumor vs. PD-1 on T cells; durvalumab and avelumab are other PD-L1 inhibitors; combination with bevacizumab for HCC: atezo+bev improved OS vs. sorafenib (IMbrave150 trial); PD-L1 testing (22C3, SP142 assays — antibody/assay pair matters)"
    ),
    # ── Misc high-yield additions ─────────────────────────────────────────
    "n-acetylcysteine": _dr(
        "Replenishes glutathione by providing cysteine precursor; glutathione conjugates and detoxifies NAPQI (toxic acetaminophen metabolite) produced by CYP2E1/CYP3A4; also direct antioxidant and vasodilator",
        "Acetaminophen overdose (antidote — must give within 8-10h for maximal benefit; still give even if late), contrast-induced nephropathy prevention (controversial — minimal evidence), COPD exacerbations (mucolytic), meconium ileus equivalent (GI use)",
        "Nausea/vomiting (oral formulation — acetylcysteine has sulfur odor), anaphylactoid reactions (IV — especially first infusion; flushing, urticaria, bronchospasm; treat with antihistamine and slow infusion), hepatotoxicity (rare)",
        "Antidote for acetaminophen toxicity — most effective if given within 8-10h of ingestion; use Rumack-Matthew nomogram to determine need for treatment; can still benefit even >24h post-ingestion if evidence of liver injury; IV preferred for serious toxicity; 21-hour IV protocol or 72-hour oral protocol"
    ),
    "mesalamine": _dr(
        "5-aminosalicylic acid (5-ASA); topically active anti-inflammatory in GI mucosa; inhibits COX and LOX pathways → reduces prostaglandins and leukotrienes; inhibits TNF and NF-κB; acts locally on colonic mucosa",
        "Ulcerative colitis (first-line — induction and maintenance of remission for mild-moderate disease; oral ± rectal formulations), microscopic colitis, Crohn's colitis (limited evidence)",
        "Generally well tolerated; nephrotic syndrome/interstitial nephritis (rare but serious — monitor renal function), paradoxical worsening of colitis (rare), headache, nausea, pancreatitis (rare), pericarditis/myocarditis (rare)",
        "Multiple formulations target different colonic regions (Asacol — ileum/colon; Rowasa enema — rectosigmoid; Canasa suppository — rectum); different from sulfasalazine (5-ASA + sulfapyridine carrier) — mesalamine avoids sulfonamide side effects; monitor creatinine annually; Crohn's: less effective than UC"
    ),
    "albuterol": _dr(
        "Short-acting beta-2 adrenergic agonist (SABA); activates beta-2 receptors in bronchial smooth muscle → Gs → adenylyl cyclase → cAMP → PKA activation → smooth muscle relaxation and bronchodilation; rapid onset (5-15 min), duration 4-6h",
        "Acute bronchospasm (asthma attack, COPD exacerbation — rescue inhaler), exercise-induced bronchospasm (pretreatment), hyperkalemia (shifts K+ intracellularly — temporizing measure), anaphylaxis (bronchospasm component)",
        "Tachycardia, palpitations, tremor, hypokalemia (K+ shifts intracellularly — monitor with IV albuterol), paradoxical bronchospasm (rare — especially with first use of new canister), lactic acidosis (high-dose continuous nebulization in severe asthma — metabolic effect)",
        "Rescue inhaler — use for acute symptoms; overuse (>2 days/week) indicates need for step-up therapy (add ICS); correct MDI technique critical; levalbuterol = R-enantiomer only (theoretically less cardiac side effects, more expensive); nebulization for severe attacks"
    ),
    "tiotropium": _dr(
        "Long-acting muscarinic antagonist (LAMA); anticholinergic; blocks M3 muscarinic receptors in airway smooth muscle → prevents bronchoconstriction and reduces mucus secretion; once-daily inhaled; duration >24h",
        "COPD (maintenance therapy — reduces exacerbations, improves lung function and quality of life; first-line for symptomatic COPD); asthma (add-on therapy in uncontrolled asthma)",
        "Dry mouth (most common — muscarinic blockade), urinary retention (avoid in BPH — blocks M3 in bladder), constipation, narrow-angle glaucoma exacerbation (avoid — ocular anticholinergic effect), tachycardia (rare), paradoxical bronchospasm",
        "Do NOT use as rescue inhaler (long-acting — not for acute bronchospasm); rinse mouth after use; avoid in angle-closure glaucoma (use mouthpiece carefully — avoid aerosol in eyes); UPLIFT trial: reduced exacerbation rate and hospitalization in COPD; aclidinium and umeclidinium = alternative LAMAs"
    ),
    "montelukast": _dr(
        "Leukotriene receptor antagonist (LTRA); blocks cysteinyl leukotriene receptor 1 (CysLT1) — prevents leukotrienes (LTC4, LTD4, LTE4) from causing bronchoconstriction, mucus secretion, and eosinophil recruitment; oral, once daily",
        "Asthma (add-on therapy — step 2 alternative to low-dose ICS; less effective than ICS as monotherapy), allergic rhinitis, exercise-induced bronchoconstriction, aspirin-exacerbated respiratory disease (AERD/Samter's triad)",
        "Neuropsychiatric effects (black box warning — depression, suicidal ideation, sleep disturbances, hallucinations, aggression, anxiety; FDA 2020 boxed warning; reserve for patients not adequately controlled on other options), churg-strauss vasculitis (eosinophilic — when oral steroids tapered), headache, GI upset",
        "Black box neuropsychiatric warning (2020) — counsel patients and families; Samter's triad: asthma + nasal polyps + aspirin sensitivity (NSAID-exacerbated respiratory disease) — LTRAs useful; zafirlukast = alternative LTRA (requires LFT monitoring); zileuton = 5-lipoxygenase inhibitor (different target)"
    ),
    "salmeterol": _dr(
        "Long-acting beta-2 adrenergic agonist (LABA); selective beta-2 agonist with prolonged receptor binding via lipophilic side chain; onset 30 min (NOT for acute bronchospasm); duration 12h; MUST be used with ICS in asthma",
        "Asthma (add-on to ICS — NEVER as monotherapy in asthma; fixed-dose combination with fluticasone — Advair), COPD maintenance (with or without ICS), exercise-induced bronchospasm prevention",
        "Tachycardia, tremor, hypokalemia; black box warning (LABA monotherapy in asthma without ICS increases asthma-related deaths — SMART trial); paradoxical bronchospasm; not for acute rescue",
        "SABA for rescue; LABA for maintenance (always with ICS in asthma); SABA + LABA = complementary bronchodilators; SMART trial: salmeterol alone (without ICS) increased asthma mortality → LABAs must ALWAYS be combined with ICS in asthma; formoterol = faster-onset LABA (can be used as rescue in SMART approach — MART)"
    ),
    "fluticasone": _dr(
        "Inhaled corticosteroid (ICS); high-potency synthetic glucocorticoid; binds glucocorticoid receptor → suppresses inflammatory gene transcription → reduces airway inflammation, eosinophilia, mucus secretion, bronchial hyperresponsiveness",
        "Asthma controller therapy (first-line maintenance — reduces exacerbations and improves symptom control; used at lowest effective dose), COPD (with LABA — reduces exacerbations in frequent exacerbators), allergic rhinitis (nasal spray — Flonase)",
        "Oropharyngeal candidiasis (local immunosuppression — RINSE MOUTH after each use), dysphonia (hoarseness — vocal cord myopathy), adrenal suppression (high doses — especially in children; monitor growth), decreased bone density (high doses, long-term), cataracts/glaucoma (long-term high-dose)",
        "Always rinse mouth and gargle after inhaled steroids — prevents oral candidiasis; spacer/valved holding chamber increases lung deposition and reduces oropharyngeal deposition; most potent ICS per microgram (fluticasone furoate, mometasone also high-potency); STEP DOWN to lowest effective ICS dose once controlled"
    ),

    # ── Cardiovascular — ARNi / HFrEF ────────────────────────────────────
    "sacubitril-valsartan": _dr(
        "Angiotensin receptor-neprilysin inhibitor (ARNi). Valsartan blocks AT1 receptor; sacubitril (prodrug → LBQ657) inhibits neprilysin, the enzyme that degrades natriuretic peptides (BNP, ANP, bradykinin) → ↑natriuretic peptides → vasodilation, natriuresis, anti-remodeling.",
        "HFrEF (EF ≤40%) in stable outpatients (NYHA II-III) who tolerate RAAS blockade — replaces ACEi/ARB in chronic HFrEF; reduces CV death + HF hospitalization by 20% vs. enalapril (PARADIGM-HF trial). Post-MI LV dysfunction: PARADISE-MI did not significantly beat ramipril.",
        "Hypotension (very common — titrate slowly), hyperkalemia, AKI, angioedema (bradykinin accumulation — risk ↑ if switched from ACEi — MUST wait ≥36 h washout before starting). CONTRAINDICATED: pregnancy, prior ACEi/ARNi angioedema, concurrent ACEi use.",
        "PARADIGM-HF: sacubitril-valsartan reduced CV death + HF hospitalization 20% vs. enalapril (stopped early for benefit). 36-hour washout from ACEi mandatory before starting (overlapping ACE inhibition + neprilysin inhibition → ↑↑bradykinin → angioedema risk). Guideline-directed medical therapy (GDMT) in HFrEF: ACEi/ARB/ARNi + beta-blocker + MRA + SGLT2i = 'the four pillars'."
    ),
    "bisoprolol": _dr(
        "Highly selective beta-1 blocker (most cardioselective commercially available — minimal beta-2 effect even at higher doses). Reduces HR, myocardial O2 demand, renin release, and neurohormonal activation in HF.",
        "HFrEF (CIBIS-II trial — 34% reduction in all-cause mortality; one of 3 BBs with proven HFrEF mortality benefit), HTN, angina, rate control in AF.",
        "Bradycardia, AV block, fatigue, cold extremities. HIGH selectivity means safer in mild-moderate asthma/COPD vs. non-selective BBs — but still use with caution. Abrupt withdrawal → rebound angina/HTN.",
        "Only 3 beta-blockers have proven HFrEF mortality benefit (remember CoMeB): Carvedilol (COPERNICUS), Metoprolol succinate (MERIT-HF), Bisoprolol (CIBIS-II). Bisoprolol most selective — preferred when beta-2 side effects (bronchospasm, peripheral vasoconstriction) are a concern. Start low, titrate slowly in HFrEF — acutely may worsen compensation."
    ),
    "ivabradine": _dr(
        "Selective funny current (If) inhibitor — blocks HCN channels in sinoatrial node → slows spontaneous depolarization → reduces heart rate WITHOUT affecting contractility, conduction velocity, or blood pressure.",
        "HFrEF (EF ≤35%) in sinus rhythm with resting HR ≥70 bpm despite maximally tolerated beta-blocker (or beta-blocker intolerance) — SHIFT trial: reduced CV death + HF hospitalization. Stable angina (rate reduction → ↓O2 demand).",
        "Bradycardia (dose-limiting), phosphenes (transient visual brightness — If channels in retina), AF (slight ↑risk — contraindicated in AF/flutter — only works in sinus rhythm), headache, hypertension. CONTRAINDICATED: AF, HR <60, severe hepatic impairment, concurrent strong CYP3A4 inhibitors.",
        "SHIFT trial: ivabradine added to beta-blocker reduced composite HF endpoint. Pure rate reducer — no negative inotropy (unlike beta-blockers). Only effective in sinus rhythm (If channel is pacemaker current of SA node). Phosphenes (visual brightening with light changes) are pathognomonic, benign, reversible."
    ),
    "eplerenone": _dr(
        "Selective mineralocorticoid receptor antagonist (MRA). Blocks aldosterone at mineralocorticoid receptor → natriuresis, ↓K+ excretion, ↓cardiac fibrosis/remodeling. MORE SELECTIVE than spironolactone (avoids progesterone/androgen receptor binding).",
        "Post-MI with LV dysfunction (EF ≤40%) and HF or diabetes — EPHESUS trial (15% mortality reduction started within 3-14 days of MI). HFrEF (EF ≤35%, NYHA II-IV) — EMPHASIS-HF trial (mortality benefit). HTN (resistant HTN — add-on).",
        "Hyperkalemia (monitor K+ closely — CONTRAINDICATED if K+ >5.5 at start or CrCl ≤30), gynecomastia/sexual dysfunction much less than spironolactone (no anti-androgen/progestogenic effects).",
        "Eplerenone vs. spironolactone: both MRAs with similar efficacy — eplerenone preferred in men who develop gynecomastia/sexual dysfunction on spironolactone. EPHESUS: post-MI HFrEF — started 3-14 days post-MI reduced all-cause mortality. Use with caution with ACEi/ARB (↑↑hyperkalemia risk). MRA + SGLT2i combination: SGLT2i partially offsets hyperkalemia risk of MRA."
    ),
    "ramipril": _dr(
        "Long-acting ACE inhibitor (prodrug → ramiprilat, t½ ~13-17h, once-daily dosing). Inhibits ACE → ↓Ang II → vasodilation, ↓aldosterone, ↓cardiac remodeling. Anti-proteinuric via ↓intraglomerular pressure.",
        "HTN, HFrEF, post-MI LV dysfunction, high cardiovascular risk (HOPE trial — 22% ↓ in composite CV death/MI/stroke in high-risk patients WITHOUT HF), diabetic and non-diabetic nephropathy.",
        "Dry cough (bradykinin), angioedema (CONTRAINDICATED thereafter), hyperkalemia, AKI (bilateral RAS). CONTRAINDICATED: pregnancy, bilateral RAS, prior ACEi angioedema.",
        "HOPE trial: ramipril 10 mg daily reduced CV death/MI/stroke 22% in high-risk patients (DM/vascular disease — NOT necessarily HF or HTN). Landmark trial that extended ACEi indication to primary/secondary CV prevention. Among most prescribed ACEi globally with strong trial evidence. Prodrug requiring hepatic conversion — reduced efficacy in liver failure."
    ),
    "nifedipine": _dr(
        "Dihydropyridine (DHP) calcium channel blocker — blocks L-type Ca²⁺ channels in vascular smooth muscle predominantly (minimal cardiac conduction effect). Potent peripheral vasodilation → ↓afterload → reflex tachycardia (especially with IR formulation).",
        "HTN (XL/extended-release — once daily; IR AVOID for chronic HTN due to reflex tachycardia + ↑CV events in meta-analyses), hypertensive emergency in pregnancy (oral — safe in pregnancy, unlike ACEi/ARBs), Raynaud phenomenon (vasospasm relief), vasospastic (Prinzmetal) angina, tocolysis (preterm labor — relaxes uterine smooth muscle).",
        "Reflex tachycardia (IR > XL — due to rapid vasodilation + baroreceptor activation), peripheral edema (ankle dependent — vasodilation), headache, flushing, gingival hyperplasia (classic with nifedipine). IR nifedipine AVOID in ACS and chronic HTN — associated with ↑MI risk.",
        "IR nifedipine sublingual was previously used for hypertensive emergency but is now CONTRAINDICATED — unpredictable absorption, excessive hypotension, coronary steal. Use XL formulation for chronic HTN. Safe in pregnancy (unlike ACEi/ARBs — teratogenic). Grapefruit inhibits CYP3A4 (CCB metabolism) → ↑drug levels — advise patients to avoid."
    ),
    "hydralazine": _dr(
        "Direct arteriolar vasodilator — activates guanylate cyclase → ↑cGMP → vascular smooth muscle relaxation (mechanism not fully elucidated; possibly NO-mediated). Reduces afterload without venodilatation → reflex tachycardia and fluid retention.",
        "Hypertensive emergency in pregnancy (IV — alongside labetalol and nifedipine as first-line options), HTN in pregnancy (chronic — second-line after methyldopa and labetalol), HFrEF in Black patients unable to tolerate ACEi/ARBs (A-HeFT trial: hydralazine + isosorbide dinitrate reduced all-cause mortality 43% in self-identified Black patients with HFrEF).",
        "Reflex tachycardia (baroreceptor activation — add beta-blocker for chronic use), fluid retention (add diuretic), lupus-like syndrome (drug-induced lupus — slow acetylators at higher risk; anti-histone antibodies; stop drug → resolves), peripheral neuropathy (pyridoxine deficiency).",
        "A-HeFT trial: fixed-dose hydralazine/isosorbide dinitrate (BiDil) reduced all-cause mortality 43% and HF hospitalization 33% in Black patients with HFrEF — first trial in a specific racial/ethnic group. Mechanism of racial difference: Black patients have lower nitric oxide bioavailability — NO-based therapy more effective. Drug-induced lupus: NAT2 slow acetylators (accumulate toxic metabolites) — dose-dependent — more common in women."
    ),
    "isosorbide mononitrate": _dr(
        "Organic nitrate — bioconverted to nitric oxide (NO) → activates guanylate cyclase → ↑cGMP → vascular smooth muscle relaxation. Predominant effect on veins (↓preload/LVEDP) > arteries (↓afterload). No hepatic first-pass metabolism (unlike dinitrate) — ~100% bioavailability, once-daily dosing.",
        "Stable angina prophylaxis (first-line oral nitrate — eccentric dosing to prevent tolerance), HFrEF with hydralazine (A-HeFT used isosorbide DINITRATE), esophageal spasm.",
        "Headache (vasodilation — very common; tolerance develops), hypotension/syncope (especially with PDE5 inhibitors — CONTRAINDICATED: sildenafil/tadalafil/vardenafil within 24-48h — risk of profound hypotension), reflex tachycardia, tolerance (tachyphylaxis with continuous exposure — require nitrate-free interval ≥8-12h/day).",
        "Nitrate tolerance: continuous exposure desensitizes guanylate cyclase. Eccentric dosing (e.g., 8AM and 2PM — NOT at night) maintains a nitrate-free interval to prevent tolerance. ABSOLUTE CONTRAINDICATION with PDE5 inhibitors (Viagra/Cialis/Levitra) — both ↑cGMP → severe refractory hypotension. Nitroglycerin for acute angina; isosorbide mononitrate for prophylaxis."
    ),
    "sotalol": _dr(
        "Class III antiarrhythmic (Vaughan Williams) — prolongs action potential duration and refractory period via K⁺ channel (IKr) blockade (Class III effect) PLUS non-selective beta-blocking activity (Class II effect). Prolongs QT interval.",
        "Ventricular arrhythmias (sustained VT/VF — refractory or high-risk), AF/flutter maintenance of sinus rhythm (especially with structural heart disease — but inferior to amiodarone for efficacy; preferred when amiodarone toxicity is unacceptable).",
        "QT prolongation → Torsades de Pointes (most dangerous — risk ↑ with hypokalemia, hypomagnesemia, bradycardia, renal failure — sotalol is renally cleared). Bradycardia, AV block, fatigue, bronchospasm (beta-2 blockade — avoid in asthma). CONTRAINDICATED: QTc >450 ms, CrCl <40 mL/min, hypokalemia.",
        "Sotalol MUST be initiated in hospital setting with continuous QT monitoring for at least 3 days (dose-related QTc prolongation + Torsades risk). Renally cleared (dose reduce or avoid with eGFR <40). Corrected QT must be checked before each dose increase. Unlike amiodarone — no thyroid/pulmonary/hepatic toxicity. Remember: Class II + III properties = beta-blocker + K-channel blocker."
    ),
    "procainamide": _dr(
        "Class Ia antiarrhythmic — blocks fast Na⁺ channels (slows phase 0 depolarization → ↓conduction velocity) AND K⁺ channels (prolongs repolarization → ↑ERP). Also blocks ganglionic nicotinic receptors → hypotension with IV administration.",
        "Acute termination of WPW-associated AF/flutter with wide-complex tachycardia (DRUG OF CHOICE — unlike adenosine/digoxin/verapamil which can accelerate ventricular rate via accessory pathway — procainamide slows bypass tract conduction), stable monomorphic VT, AF conversion.",
        "Hypotension (IV — vasodilation + negative inotropy), QT prolongation → Torsades de Pointes, widened QRS (Na+ channel blockade). Drug-induced lupus-like syndrome (highest-risk drug for drug-induced lupus — anti-histone antibodies; anti-dsDNA usually NEGATIVE, as with hydralazine). DILS affects up to 30% on chronic therapy.",
        "WPW + AF = PROCAINAMIDE (not adenosine, not verapamil, not diltiazem — these block AV node but the accessory pathway (Bundle of Kent) conducts faster → unopposed rapid ventricular response → VF). Procainamide active metabolite = NAPA (N-acetylprocainamide) — accumulates in renal failure; predominantly Class III activity. Drug-induced lupus: procainamide most common cause (30% on chronic Rx), anti-histone Abs in >95%, anti-dsDNA rare (unlike idiopathic SLE)."
    ),
    "dronedarone": _dr(
        "Class III antiarrhythmic — multi-channel blocker (K⁺, Na⁺, Ca²⁺ channels) + anti-adrenergic effects. Structurally similar to amiodarone (without iodine moiety) — fewer thyroid/pulmonary toxicities BUT less efficacious and shorter half-life.",
        "Paroxysmal or persistent AF/flutter — maintenance of sinus rhythm in patients with risk factors who are in sinus rhythm at time of prescription. Reduces CV hospitalizations (ATHENA trial).",
        "Hepatotoxicity (rare but severe — monitor LFTs; report new symptoms), bradycardia, QT prolongation (less than amiodarone), GI upset (nausea, diarrhea). CONTRAINDICATED: permanent AF (PALLAS trial — ↑CV death in permanent AF), NYHA III-IV or recent decompensated HF, severe hepatic impairment, concurrent QT-prolonging drugs.",
        "PALLAS trial: dronedarone significantly INCREASED mortality in permanent AF with risk factors → now CONTRAINDICATED in permanent AF. Only for paroxysmal/persistent AF patients who are in sinus rhythm. Does NOT contain iodine (unlike amiodarone) → no thyroid toxicity; shorter t½ (~13-19h vs. amiodarone 40-55 days) → easier to stop if problems arise. Less effective than amiodarone for AF maintenance but much safer side effect profile."
    ),
    # ── Emergency / ICU ───────────────────────────────────────────────────
    "magnesium sulfate": _dr(
        "Magnesium competes with calcium at voltage-gated Ca²⁺ channels, inhibits NMDA receptors, and stabilizes cell membranes. In eclampsia: raises seizure threshold by reducing CNS neuronal excitability. In arrhythmias: stabilizes cardiac membranes and restores normal ionic gradients.",
        "Eclampsia/pre-eclampsia (DRUG OF CHOICE for seizure prophylaxis and treatment — Magpie trial: ~58% reduction in eclampsia vs. placebo), torsades de pointes (direct treatment — 2g IV bolus), preterm labor tocolysis (delays delivery 48h to allow corticosteroids — NOT for long-term tocolysis), severe asthma (IV adjunct in refractory exacerbation), hypomagnesemia, refractory ventricular arrhythmias.",
        "Toxicity (dose-dependent — monitor levels, reflexes, RR): loss of DTRs (first sign, ~7-10 mEq/L), respiratory depression (~10-13 mEq/L), cardiac arrest (>15-25 mEq/L); therapeutic 4-7 mEq/L. Hypotension, flushing, nausea. Antidote: CALCIUM GLUCONATE (10 mL of 10% IV over 10 min).",
        "Eclampsia: magnesium superior to phenytoin and diazepam (Collaborative Eclampsia Trial, 1995). Monitor toxicity with: patellar reflex (abolition = first sign → reduce infusion), RR >12, urine output >25 mL/h. Renally cleared — reduce dose in renal failure. Antidote calcium gluconate should be at bedside during infusion. Magnesium for Torsades: works regardless of Mg level — suppresses early afterdepolarizations (Ca2+ channel block)."
    ),
    "calcium gluconate": _dr(
        "Provides extracellular Ca²⁺ ions — directly antagonizes the cardiac effects of hyperkalemia by stabilizing the cardiac membrane (raises threshold potential → reduces automaticity and conduction velocity changes without altering K⁺ levels). Also replenishes calcium in hypocalcemia.",
        "Hyperkalemia (cardiac membrane stabilization — FIRST-LINE when ECG changes present: peaked T-waves, widened QRS, sine wave pattern; acts in 1-3 min, lasts 30-60 min — temporizing while K+ lowering measures take effect), hypocalcemia (tetany, seizures), hypermagnesemia (antidote), calcium channel blocker overdose (high-dose — reverses negative inotropy), hydrofluoric acid burns (topical/IV).",
        "Hypercalcemia (if over-administered), bradycardia/asystole if given too rapidly, tissue necrosis with extravasation (vesicant — use central line or calcium chloride peripherally), nausea. Caution with digoxin toxicity (hypercalcemia potentiates digoxin).",
        "Calcium gluconate vs. calcium chloride: both ionize immediately (gluconate does NOT need hepatic activation); chloride has ~3x more elemental Ca²⁺ per ampule (10 mL of 10%: ~270 mg vs ~93 mg), gluconate is less irritating peripherally (preferred in cardiac arrest or severe hemodynamic compromise — but more caustic extravasation risk). In hyperkalemia: calcium does NOT lower serum K⁺ — it ONLY protects the heart. Must follow with K⁺-lowering (insulin/dextrose, kayexalate, dialysis). Onset 1-3 min; duration ~30-60 min."
    ),
    "sodium bicarbonate": _dr(
        "Alkalinizing agent — provides HCO₃⁻ to buffer excess H⁺ → ↑serum pH. In TCA overdose: alkalinization narrows QRS (Na⁺ channel blockade reversed by alkaline pH). In hyperkalemia: shifts K⁺ intracellularly via H⁺/K⁺ exchange (limited efficacy in chronic ESRD). In rhabdomyolysis: alkalinizes urine → reduces myoglobin precipitation.",
        "Severe metabolic acidosis (pH <7.1 — especially if ↓HCO₃⁻ is primary; NOT for lactic acidosis from tissue hypoperfusion where underlying cause must be treated), TCA overdose (DRUG OF CHOICE — QRS >100ms, ventricular arrhythmia, hypotension — target pH 7.45-7.55), hyperkalemia (temporizing — limited in ESRD), rhabdomyolysis (urine alkalinization to prevent renal tubular cast precipitation), salicylate toxicity (alkalinizes urine → ion trapping → ↑renal elimination).",
        "Metabolic alkalosis (overcorrection), hypernatremia (sodium load), hypocalcemia (alkalosis → ↑protein binding of Ca²⁺ → ↓ionized Ca²⁺ → tetany), hypokalemia (K⁺ shifts into cells), paradoxical intracellular acidosis (CO₂ crosses membranes but HCO₃⁻ does not — relevant in cardiac arrest).",
        "TCA overdose pearl: sodium bicarb works by 2 mechanisms — (1) alkalinization reverses Na+ channel blockade (TCAs bind more when non-ionized at acidic pH); (2) sodium loading overcomes competitive Na+ channel block. Target arterial pH 7.45-7.55. QRS >100ms = indication for bicarb. Bicarb in cardiac arrest controversial (ACLS does not recommend routinely — use only for specific indications: TCA OD, hyperkalemia, pre-existing metabolic acidosis)."
    ),
    "dextrose 50%": _dr(
        "Hypertonic glucose solution (50g dextrose/100 mL = 25g per standard 50 mL amp). Rapidly raises blood glucose; also used with insulin to shift K⁺ intracellularly (insulin requires glucose to prevent hypoglycemia). In hyperkalemia: drives K⁺ into cells via Na⁺/K⁺ ATPase stimulation (insulin-mediated).",
        "Hypoglycemia emergency (IV — unconscious patient, unable to take oral glucose), hyperkalemia (D50 + regular insulin — lowers serum K+ by 0.5-1.5 mEq/L over 30-60 min — temporizing), acute alcohol intoxication with suspected Wernicke's (give THIAMINE FIRST before dextrose — prevents precipitating Wernicke's encephalopathy).",
        "Hyperglycemia (especially in non-diabetics or if overdosed), phlebitis/tissue necrosis (hypertonic — use central line ideally or well-functioning peripheral IV), hyperosmolarity, rebound hypoglycemia after insulin.",
        "THIAMINE before dextrose in alcoholics (or any malnourished patient): glucose metabolism requires thiamine (cofactor for pyruvate dehydrogenase, α-ketoglutarate dehydrogenase) — giving dextrose to thiamine-depleted patient precipitates Wernicke's encephalopathy (confusion, ophthalmoplegia, ataxia — Wernicke's triad). Insulin + D50 for hyperkalemia: regular insulin 10 units IV + D50 50 mL. Monitor glucose q30 min — hypoglycemia occurs 1-4 hours later. K⁺ falls 0.5-1.5 mEq/L (temporary — 2-4h)."
    ),
    "glucagon": _dr(
        "Polypeptide hormone — activates Gs-coupled glucagon receptor → ↑cAMP → activates PKA → (1) hepatic glycogenolysis + gluconeogenesis → ↑blood glucose; (2) positive inotropic + chronotropic effects independent of beta-adrenergic receptors (bypasses receptor blockade).",
        "Hypoglycemia (when IV access unavailable — IM/SC/intranasal — raises glucose via hepatic glycogenolysis; requires adequate hepatic glycogen stores — ineffective in alcoholics/malnourished/fasted), beta-blocker overdose (high-dose — bypasses blocked beta-receptors to restore inotropy/chronotropy), calcium channel blocker overdose (positive inotrope), esophageal food impaction (smooth muscle relaxation — facilitates passage), anaphylaxis in beta-blocker patients (refractory to epinephrine — glucagon restores HR/BP).",
        "Nausea and vomiting (common — give slowly), hyperglycemia, tachycardia. Ineffective in hepatic glycogen-depleted states (alcoholism, prolonged fasting, adrenal insufficiency). Hypersensitivity (rare).",
        "Beta-blocker OD: glucagon is antidote — bypasses blocked beta-receptors via its own Gs receptor → ↑cAMP → ↑inotropy/chronotropy. Dose: 3-10 mg IV bolus, then infusion. Also useful in CCB OD (multi-modal approach: calcium, high-dose insulin, glucagon, lipid emulsion). Nasal glucagon (Baqsimi): FDA-approved for severe hypoglycemia — effective even in unconscious patients, no IV needed."
    ),
    "atropine": _dr(
        "Competitive antagonist at muscarinic (M1-M5) receptors — blocks parasympathetic (cholinergic) effects. ↑HR (blocks vagal tone on SA/AV nodes), bronchodilation (↓secretions), ↓GI motility, mydriasis, cycloplegia, ↓glandular secretions (dry mouth, dry eyes, urinary retention).",
        "Symptomatic bradycardia (ACLS first-line: 1 mg IV q3-5 min, max 3 mg — sinus bradycardia, high-degree AV block as temporizing measure), organophosphate/nerve agent poisoning (ANTIDOTE — blocks muscarinic overstimulation: SLUDGE symptoms; titrate to drying secretions — no upper dose limit in OD), pre-anesthetic (↓oral secretions), eye drops (mydriasis for exam, amblyopia treatment), antidote for cholinergic drug toxicity (neostigmine reversal).",
        "Anticholinergic toxidrome (tachycardia, dry mouth, urinary retention, constipation, hyperthermia, confusion, flushing, mydriasis — 'hot as a hare, dry as a bone, red as a beet, blind as a bat, mad as a hatter'). AVOID in acute angle-closure glaucoma (↑IOP), urinary obstruction (BPH), tachycardia.",
        "Organophosphate poisoning (pesticides, nerve agents — sarin, VX): mechanism = irreversible AChE inhibition → acetylcholine accumulation → SLUDGE (Salivation, Lacrimation, Urination, Defecation, GI cramps, Emesis) + DUMBELS + nicotinic effects (muscle weakness, paralysis). Atropine: titrate to DRY SECRETIONS (NOT to HR). Can require massive doses (hundreds of mg in severe poisoning). Pralidoxime (2-PAM) reactivates AChE if given before 'aging' (covalent bond becomes irreversible — minutes for soman, hours for most others)."
    ),
    "succinylcholine": _dr(
        "Depolarizing neuromuscular blocker (NMB) — binds nicotinic ACh receptors at NMJ and depolarizes the motor end plate. Fasciculations followed by flaccid paralysis (sustained depolarization prevents repolarization/subsequent contraction). Metabolized by plasma pseudocholinesterase (butyrylcholinesterase) → ultra-short acting (~10-12 min).",
        "Rapid sequence intubation (RSI) — gold standard for emergent intubation when full-stomach/aspiration risk (fastest onset: 30-60 sec, intubating conditions in 60-90 sec), electroconvulsive therapy (muscle relaxation), laryngospasm treatment.",
        "Hyperkalemia (depolarization releases K⁺ from muscle cells — ~0.5 mEq/L normally; DANGEROUS hyperkalemia in: burns (after 24h), crush injury, prolonged immobilization, denervation (stroke, SCI), myopathies — can cause fatal cardiac arrest). Malignant hyperthermia (triggering agent — in susceptible individuals — treat with dantrolene), bradycardia (muscarinic effect — more in children, repeat doses), increased IOP/ICP/intragastric pressure, prolonged paralysis with pseudocholinesterase deficiency.",
        "AVOID succinylcholine in (SCI/stroke/burns/crush/prolonged immobility — HIGH K⁺ RISK): instead use rocuronium 1.2 mg/kg (equally fast at high dose). Malignant hyperthermia: triggered by succinylcholine + volatile anesthetics → uncontrolled Ca²⁺ release from SR → hyperthermia, rigidity, metabolic acidosis, hyperkalemia. ANTIDOTE: DANTROLENE (inhibits RyR1 receptor → ↓SR Ca²⁺ release). Pseudocholinesterase deficiency: succinylcholine cannot be metabolized → prolonged paralysis (hours) — check personal/family history of 'anesthesia problems'."
    ),
    "rocuronium": _dr(
        "Non-depolarizing aminosteroid neuromuscular blocker — competitive antagonist at nicotinic ACh receptors at NMJ → flaccid paralysis without fasciculations. At high dose (1.2 mg/kg) onset rivals succinylcholine (60-90 sec) — viable RSI alternative. Duration: 30-60 min (standard dose), 60-90 min (high dose).",
        "Rapid sequence intubation (RSI) — preferred over succinylcholine when succinylcholine CONTRAINDICATED (hyperkalemia risk: burns, crush, SCI, denervation injury; malignant hyperthermia susceptibility; pseudocholinesterase deficiency). General anesthesia induction, mechanical ventilation facilitation.",
        "Residual neuromuscular blockade (must confirm reversal before extubation), anaphylaxis (most common cause of anaphylaxis during anesthesia — IgE mediated; cross-reactive with other aminosteroids), tachycardia (vagolytic — mild), pain on injection (common).",
        "RSI dose: 1.2 mg/kg (twice the ED95) — same onset as succinylcholine (60-90 sec). Standard intubating dose: 0.6 mg/kg (onset 90-120 sec). REVERSAL: sugammadex (cyclodextrin — encapsulates and inactivates rocuronium/vecuronium — specific and complete reversal even at deep block; 16 mg/kg for immediate reversal) or neostigmine (acetylcholinesterase inhibitor — only at moderate block). Rocuronium preferred choice in burns, SCI, hyperkalemia, MH susceptible patients — avoids succinylcholine hyperkalemia risk."
    ),
    "ketamine": _dr(
        "Dissociative anesthetic — NMDA receptor antagonist → blocks glutamate-mediated excitatory neurotransmission → dissociative anesthesia (analgesia + amnesia + sedation while maintaining airway reflexes and respiratory drive). Also has analgesic properties at sub-anesthetic doses (spinal NMDA receptors), sympathomimetic effects (↑catecholamine release), and bronchodilation.",
        "Rapid sequence intubation (hemodynamically unstable patients — catecholamine release maintains BP), procedural sedation/analgesia (emergency/pediatric — 'dissociative sedation'), severe acute pain (low-dose — opioid-sparing), severe refractory asthma (bronchodilation), refractory depression (IV subanesthetic doses — rapid antidepressant effect within hours), trauma (maintains hemodynamics).",
        "Emergence reactions (vivid dreams, hallucinations, delirium — ↓with benzodiazepine co-administration), ↑ICP and IOP (traditionally avoided in TBI — more recent evidence less clear), ↑BP and HR (sympathomimetic — ADVANTAGE in hypotensive patients but AVOID if hypertensive emergency or CAD), hypersalivation (antisialagogue pre-treatment with glycopyrrolate), laryngospasm (rare).",
        "Unique among anesthetics: MAINTAINS airway reflexes and respiratory drive (unlike propofol/barbiturates) → preferred for procedural sedation when airway management is a concern. Bronchodilation (mechanism: catecholamine release + direct smooth muscle effect) → useful in status asthmaticus. Hemodynamic stability: ketamine increases catecholamines → preferred induction agent in trauma/hypovolemic shock. Contraindicated (relative): uncontrolled HTN, active psychosis, conditions where ↑ICP is harmful."
    ),
    "propofol": _dr(
        "IV anesthetic — potentiates GABA-A receptor-mediated Cl⁻ influx → CNS depression. Rapid onset (30-60 sec), short duration (5-10 min) due to rapid redistribution. Contains intralipid emulsion (soybean oil, egg lecithin) — caloric load (1.1 kcal/mL).",
        "Induction and maintenance of general anesthesia, procedural sedation, ICU sedation (short-term — preferred for mechanically ventilated patients due to titrability), refractory status epilepticus (high-dose — suppresses burst activity), refractory PONV.",
        "Propofol infusion syndrome (PRIS — rare but life-threatening with high doses >5 mg/kg/h or prolonged infusion >48h: metabolic acidosis, cardiac failure, rhabdomyolysis, renal failure, hypertriglyceridemia — monitor TG, lactate), hypotension (vasodilation + negative inotropy — common with induction), apnea (have airway equipment ready), pain on injection (use large vein or lidocaine pretreatment), propofol-related infections (excellent growth medium — strict aseptic technique, discard after 12h).",
        "Propofol for RSI: 1.5-2.5 mg/kg IV — rapid, smooth induction but causes significant hypotension (avoid in hemodynamic instability — use ketamine or etomidate instead). PRIS monitoring in ICU: check TG, CK, pH q24-48h if infusion >48h or >5 mg/kg/h. No analgesic properties — must combine with opioids. Unique: gives urine a green tint (phenol metabolites) — benign. Egg/soy allergy: propofol historically avoided (now generally considered safe — egg allergy to egg WHITE proteins, not lecithin)."
    ),
    "fentanyl": _dr(
        "Synthetic opioid — highly selective mu-opioid receptor agonist. 100x more potent than morphine. Rapid onset (IV: 1-2 min) and short duration (30-60 min) due to high lipophilicity → rapid CNS penetration and redistribution. Minimal histamine release (unlike morphine). Significant first-pass metabolism — transdermal and buccal/nasal formulations bypass this.",
        "Acute pain (IV — procedure, trauma, post-op — preferred over morphine in renal failure as metabolites not renally cleared), anesthesia induction/maintenance (as part of balanced anesthesia), chronic cancer pain (transdermal patch — 72h duration — significant opioid-tolerant patients only), procedural sedation/analgesia (IV/intranasal — pediatric and adult), CBRN mass casualty (carfentanil is analog — weaponized).",
        "Respiratory depression (dose-limiting — naloxone reversal), sedation, constipation, nausea. CHEST WALL RIGIDITY (wooden chest syndrome — rapid high-dose IV bolus → severe rigidity of chest wall and vocal cords → cannot ventilate — treat with NMB + naloxone). Less histamine than morphine (safer in hemodynamic instability). Serotonin syndrome risk with MAOIs.",
        "Preferred over morphine in renal failure: morphine-6-glucuronide (active metabolite) accumulates in CKD → prolonged sedation/respiratory depression. Fentanyl metabolites are inactive. Transdermal patch: onset 12-24h (steady state ~3 days); levels fall by half ~17h after removal — NOT for acute pain. Never use transdermal in opioid-naïve patients (fatal respiratory depression). Carfentanil (veterinary opioid, 100x fentanyl potency) used in illicit drug supply — naloxone doses may need to be repeated."
    ),
    # ── Endocrine — Diabetes ──────────────────────────────────────────────
    "pioglitazone": _dr(
        "Thiazolidinedione (TZD) — activates PPARγ (peroxisome proliferator-activated receptor gamma) nuclear receptor → promotes adipocyte differentiation, ↑adiponectin, ↑GLUT4 expression → insulin sensitization in peripheral tissues (adipose > muscle). Also improves hepatic insulin sensitivity → reduces hepatic glucose output. Reduces hepatic fat (useful in NAFLD/NASH).",
        "Type 2 diabetes (insulin sensitizer — monotherapy or add-on; most effective when insulin resistance is predominant), NAFLD/NASH (off-label — reduces liver inflammation and fibrosis in NASH — PIVENS trial: ↑histological improvement), prevention of T2DM in pre-diabetes (ACT NOW trial).",
        "Weight gain (fluid retention + adipogenesis — 2-5 kg average), edema (peripheral — ↑sodium/water retention — worsens HF), heart failure exacerbation (CONTRAINDICATED in NYHA III-IV HF), bone fractures (↑fracture risk in distal extremities — especially women — ↓osteoblast differentiation via PPARγ), bladder cancer (possible association — FDA warning; avoid in active/prior bladder cancer), hepatotoxicity (rare — monitor LFTs; older troglitazone was withdrawn for this).",
        "Troglitazone (first TZD) withdrawn for hepatotoxicity — pioglitazone and rosiglitazone much safer. Rosiglitazone associated with ↑MI risk (2007 Nissen meta-analysis; RECORD trial later reassuring) — pioglitazone NOT (actually may be cardioprotective — PROactive trial). TZDs: slowest onset of glucose-lowering of all agents (takes 2-4 weeks for full effect). Contraindicated in HF (fluid retention worsens HF) and bladder cancer."
    ),
    "liraglutide": _dr(
        "GLP-1 receptor agonist — mimics glucagon-like peptide-1 → stimulates glucose-dependent insulin secretion (only when glucose elevated — low hypoglycemia risk), suppresses glucagon, slows gastric emptying, and increases satiety via central appetite suppression. T½ ~13h (once-daily SC injection).",
        "Type 2 diabetes (add-on — effective A1c reduction, weight loss, cardiovascular benefit), obesity/overweight (Saxenda — FDA-approved for weight management at higher dose 3mg; reduces body weight 5-8%), cardiovascular risk reduction in T2DM with established CVD or high risk (LEADER trial — 13% ↓ MACE: CV death/MI/stroke).",
        "Nausea and vomiting (most common — GI, dose-dependent, usually improves with dose titration), diarrhea, injection-site reactions. Rare: pancreatitis (FDA warning — use caution in prior pancreatitis history), thyroid C-cell tumors (rodents only — FDA black box warning; avoid in personal/family history of MTC or MEN2). Does NOT cause hypoglycemia as monotherapy (glucose-dependent insulin secretion).",
        "LEADER trial: liraglutide reduced MACE (CV death/non-fatal MI/stroke) by 13% vs. placebo in T2DM patients with high CV risk — first GLP-1 agonist with CV benefit. Weight loss mechanism: delays gastric emptying + hypothalamic satiety signaling (reduces food intake). Once-daily injection (vs. semaglutide: once-weekly). Semaglutide (Ozempic) has even greater CV benefit (SUSTAIN-6) and greater weight loss — now preferred. GLP-1 agonists also reduce NAFLD activity."
    ),
    "dapagliflozin": _dr(
        "SGLT2 inhibitor — blocks sodium-glucose cotransporter 2 in proximal renal tubule → ↓glucose reabsorption → glycosuria (loses ~70-80g glucose/day) → ↓plasma glucose + weight loss + osmotic diuresis (↓BP). Additional effects: ↓preload/afterload (diuresis), ↓uric acid, ↓inflammation, improved cardiac energetics (ketone utilization).",
        "Type 2 diabetes (glucose lowering + weight loss + CV/renal benefit), HFrEF (DAPA-HF trial — ↓CV death + worsening HF regardless of T2DM status — first SGLT2i approved for HF in non-diabetics), HFpEF (DELIVER trial — benefit in EF >40%), CKD (DAPA-CKD — slows eGFR decline regardless of DM).",
        "UTI and genital mycotic infections (glycosuria creates urinary glucose → fungal/bacterial growth — especially women; candida vulvovaginitis most common), polyuria (osmotic diuresis), volume depletion/hypotension (watch with diuretics), DKA (euglycemic DKA — glucose may be normal/near-normal — insidious presentation; risk ↑ with low carb diet, fasting, surgery, illness — hold before surgery), Fournier's gangrene (rare, necrotizing fasciitis of genitalia — FDA warning), limb amputation risk (canagliflozin > dapagliflozin/empagliflozin — CANVAS trial).",
        "Euglycemic DKA: SGLT2i promotes ketogenesis (↑glucagon:insulin ratio, fatty acid oxidation) while lowering glucose — DKA can develop with 'normal' glucose (normoglycemic DKA). Check β-hydroxybutyrate if DKA suspected in SGLT2i user. Unique among antidiabetics: direct HF benefit independent of glucose (DAPA-HF: ↓mortality in HFrEF regardless of DM). 4 pillars of HFrEF: ACEi/ARB/ARNi + BB + MRA + SGLT2i."
    ),
    "octreotide": _dr(
        "Synthetic somatostatin analog (t½ ~1.5-2h vs 2-3 min for endogenous somatostatin) — activates somatostatin receptors (SSTR2/5) → inhibits release of GH, IGF-1, TSH, insulin, glucagon, gastrin, secretin, VIP, motilin → reduces splanchnic blood flow and portal pressure.",
        "Variceal bleeding (IV infusion — reduces splanchnic blood flow + portal pressure → ↓variceal pressure; combined with endoscopy/banding), acromegaly (GH hypersecretion — medical management or post-surgery residual disease), carcinoid syndrome (flushing, diarrhea from serotonin/VIP hypersecretion — also delays carcinoid tumor progression — PROMID/CLARINET trials), VIPoma and glucagonoma, sulfonylurea-induced hypoglycemia (inhibits insulin release), refractory diarrhea (chemotherapy-induced, secretory).",
        "GI: nausea, cramping, fat malabsorption (↓CCK → ↓pancreatic enzymes → steatorrhea), cholelithiasis (↓gallbladder contractility → bile stasis → stones — common with chronic use). Bradycardia. Hyperglycemia or hypoglycemia (complex effects on insulin/glucagon). Injection-site pain.",
        "Variceal bleed protocol: octreotide 50 mcg IV bolus → 50 mcg/h infusion for 3-5 days (alongside endoscopic banding/sclerotherapy and prophylactic antibiotics — SBP prevention). Acromegaly: primary treatment is surgery (trans-sphenoidal); octreotide LAR (long-acting release — monthly IM) for residual disease or surgical failure. Carcinoid: peptide receptor radionuclide therapy (177Lu-DOTATATE) for progressive disease."
    ),
    "desmopressin": _dr(
        "Synthetic ADH analog (V2 receptor agonist > V1) — V2 receptor activation in renal collecting duct → ↑aquaporin-2 (AQP2) insertion → ↑water reabsorption → concentrated urine + ↓serum osmolality. Also promotes vWF and Factor VIII release from endothelial Weibel-Palade bodies (hemostatic effect).",
        "Central (neurogenic) diabetes insipidus (↓ADH secretion — traumatic, surgical, idiopathic — desmopressin replaces ADH; does NOT work in nephrogenic DI — kidneys unresponsive to ADH), enuresis (primary nocturnal — intranasal/oral), von Willebrand disease type 1 (↑vWF release — effective in mild/moderate), hemophilia A (mild-moderate — ↑Factor VIII release — avoids plasma-derived products), uremic bleeding (↑platelet adhesion via ↑vWF).",
        "Hyponatremia (excessive water retention — most dangerous adverse effect; especially with high fluid intake or in patients prone to SIADH), headache, nausea, facial flushing. Tachyphylaxis with repeated doses in hemostasis indications (vWF/FVIII stores depleted — space doses ≥24-48h). Thrombosis risk (rare, especially in elderly with CV disease).",
        "Central vs. nephrogenic DI differentiation: water deprivation test → then desmopressin challenge → if urine concentrates → central DI (responds to ADH analog); if no response → nephrogenic DI. Desmopressin in neurosurgery: skull base surgery, transphenoidal pituitary surgery often causes transient central DI — desmopressin treats. Hemostasis: DDAVP works only if endothelial vWF stores are intact — ineffective in Type 2B vWD (contraindicated — causes thrombocytopenia) and Type 3 vWD (absent vWF)."
    ),
    # ── Neurology / Pain ─────────────────────────────────────────────────
    "gabapentin": _dr(
        "Binds alpha-2-delta (α₂δ) subunit of voltage-gated Ca²⁺ channels in CNS → reduces Ca²⁺ influx at presynaptic terminals → ↓release of excitatory neurotransmitters (glutamate, substance P, norepinephrine). NOT a GABA analog despite name (does NOT bind GABA receptors or GABAergic mechanisms).",
        "Neuropathic pain (first-line: diabetic peripheral neuropathy, postherpetic neuralgia, central sensitization, fibromyalgia), epilepsy (focal/partial seizures — adjunct), restless legs syndrome, alcohol withdrawal (off-label — reduces craving + withdrawal symptoms), anxiety disorders (off-label), perioperative pain (opioid-sparing effect).",
        "Sedation and dizziness (most common — dose-limiting; ↑fall risk in elderly), ataxia, peripheral edema, weight gain, cognitive impairment. Respiratory depression with opioids/CNS depressants (↑risk — increasingly recognized; FDA warning). Non-linear absorption (saturable intestinal transporter — dose-dependent bioavailability, 60% at 300mg → 35% at 1600mg per dose — multiple daily dosing required).",
        "Pregabalin vs. gabapentin: pregabalin has LINEAR absorption (predictable PK), higher potency, fewer daily doses, approved for fibromyalgia (and GAD in the EU; gabapentin for neither). Non-linear gabapentin absorption means bioavailability varies — avoid large single doses. Drug abuse potential increasing (↑controlled substance classification in many states). Opioid combination: synergistic analgesia but also synergistic respiratory depression — use caution (FDA warning 2019)."
    ),
    "pregabalin": _dr(
        "Binds alpha-2-delta (α₂δ) subunit of voltage-gated Ca²⁺ channels (same mechanism as gabapentin) → ↓excitatory neurotransmitter release. LINEAR pharmacokinetics (unlike gabapentin) — predictable dose-response, higher bioavailability (~90%), twice-daily dosing.",
        "Neuropathic pain (first-line: diabetic peripheral neuropathy, postherpetic neuralgia, central post-stroke pain, spinal cord injury pain), fibromyalgia (FDA-approved), generalized anxiety disorder (approved in the EU, not by FDA), partial seizures (adjunctive), social anxiety (off-label).",
        "Sedation and dizziness (most common — especially at initiation; worse with dose escalation), weight gain, peripheral edema, ataxia, blurred vision, euphoria (↑abuse potential — Schedule V controlled substance), respiratory depression (with opioids/CNS depressants — FDA warning 2019). Withdrawal syndrome with abrupt discontinuation (anxiety, insomnia, nausea — taper when stopping).",
        "Advantages over gabapentin: linear absorption → predictable dosing, fewer doses/day (BID vs. TID-QID), approved for fibromyalgia and (in the EU) GAD — gabapentin is not. However, abuse potential more recognized (Schedule V in US; controlled in the UK). Both gabapentinoids implicated in opioid overdose deaths — up to 25% of fatal opioid ODs have gabapentinoid co-ingestion. Start low, titrate slowly — tolerance to CNS side effects develops."
    ),
    "topiramate": _dr(
        "Broad-spectrum antiepileptic — multiple mechanisms: (1) blocks voltage-gated Na⁺ channels; (2) potentiates GABA-A receptors; (3) antagonizes AMPA/kainate (glutamate) receptors; (4) inhibits carbonic anhydrase (CA II, IV — weak diuretic + metabolic acidosis). Weight loss mechanism via hypothalamic appetite suppression.",
        "Epilepsy (focal and generalized — broad spectrum; also Lennox-Gastaut syndrome), migraine prophylaxis (FDA-approved — effective, especially with obesity), obesity (Qsymia = topiramate + phentermine — FDA-approved), alcohol use disorder (off-label — reduces craving + heavy drinking days), binge eating disorder (off-label).",
        "Cognitive impairment ('Dopamax' — word-finding difficulty, slowed thinking — most problematic adverse effect; dose-dependent), paresthesias (CA inhibition → altered ion transport), weight loss (often 2-8 kg — useful in obesity), kidney stones (CA inhibition → ↑urine pH → calcium phosphate/oxalate stones — stay hydrated), metabolic acidosis (CA inhibition), acute angle-closure glaucoma (rare but acute — stop immediately), oligohidrosis + hyperthermia (↓sweating — especially children). TERATOGENIC (oral clefts — avoid in pregnancy).",
        "'Dopamax': word-finding problems are most patient-complained side effect — distinguishes from other AEDs. Unique: weight loss (unlike valproate — weight gain, carbamazepine — mild gain). Migraine prophylaxis dose: 50-100 mg/day (lower than epilepsy doses — fewer CNS side effects). Teratogenicity: oral clefts 11x higher than baseline — STRONGLY avoid in women of childbearing potential (use contraception). Alcohol use disorder: one of few medications with good evidence."
    ),
    "pramipexole": _dr(
        "Non-ergot dopamine receptor agonist — preferentially binds D3 > D2 > D4 receptors. Directly stimulates dopamine receptors in striatum and limbic system WITHOUT requiring conversion to dopamine (unlike levodopa — works even with neurodegeneration progression).",
        "Parkinson's disease (early and advanced — monotherapy in early PD to delay dyskinesia; adjunct to levodopa in advanced PD), restless legs syndrome (RLS — FDA-approved; first-line — reduces urge to move legs at rest and improves sleep), early-stage PD in younger patients (preferred over levodopa to delay motor fluctuations and dyskinesias).",
        "Impulse control disorders (ICDs — pathological gambling, hypersexuality, compulsive shopping, binge eating — class effect of dopamine agonists, especially at high doses; D3 receptor agonism → mesolimbic reward pathway activation), excessive daytime somnolence (sudden 'sleep attacks' while driving — warn patients), orthostatic hypotension, hallucinations (especially in elderly), nausea, edema. AUGMENTATION in RLS (worsening of RLS symptoms with dose escalation — switch to gabapentin/pregabalin).",
        "Impulse control disorders: MUST counsel all patients before initiating — impulse control disorders in ~14-17% on dopamine agonists (DOMINION study); screen regularly. If ICD develops, taper and switch to different class (levodopa, MAO-B inhibitor). In early PD: dopamine agonists preferred in young patients (<60-65) — delay levodopa to preserve its honeymoon period and delay motor complications (dyskinesias, on-off fluctuations). Motor complications from levodopa occur earlier with longer treatment duration."
    ),
    "amantadine": _dr(
        "Multiple mechanisms: (1) NMDA receptor antagonist → reduced glutamatergic excitotoxicity; (2) releases dopamine from presynaptic neurons + blocks dopamine reuptake; (3) anticholinergic properties. In Parkinson's: the dopaminergic + anti-glutamatergic effects reduce dyskinesias. Antiviral: blocks M2 ion channel (influenza A only) → prevents viral uncoating.",
        "Parkinson's disease (adjunct — reduces levodopa-induced dyskinesias; modest anti-Parkinson effect; useful for drug-induced parkinsonism), multiple sclerosis fatigue (off-label — first-line for MS-related fatigue), influenza A prophylaxis/treatment (largely obsolete — widespread resistance; now replaced by oseltamivir), traumatic brain injury (emerging evidence for promoting arousal/recovery).",
        "Anticholinergic effects (dry mouth, constipation, urinary retention), livedo reticularis (mottled purplish skin discoloration — benign, reversible), ankle edema, hallucinations/confusion (especially elderly, high dose), NMS-like syndrome on abrupt withdrawal (do NOT stop suddenly in Parkinson's patients). Renally cleared — dose reduce in CKD.",
        "Livedo reticularis: classic amantadine adverse effect — purplish mottled skin of the legs — benign, cosmetic, reversible on discontinuation. Most useful Parkinson's role: reducing levodopa-induced dyskinesias (peak-dose dyskinesias — jerky involuntary movements) — NMDA antagonism dampens the glutamatergic hyperstimulation that underlies dyskinesias. Influenza: nearly all circulating influenza A strains are resistant — oseltamivir preferred."
    ),
    # ── Oncology ─────────────────────────────────────────────────────────
    "bortezomib": _dr(
        "Proteasome inhibitor — reversibly inhibits the 26S proteasome (specifically 20S catalytic core chymotrypsin-like activity) → accumulation of misfolded proteins → ER stress → unfolded protein response → apoptosis. Plasma cells (multiple myeloma) are particularly dependent on high protein secretion → proteasome → uniquely sensitive to proteasome inhibition.",
        "Multiple myeloma (first-line and relapsed/refractory — VRd: bortezomib + lenalidomide + dexamethasone; VCD: bortezomib + cyclophosphamide + dex), mantle cell lymphoma (relapsed/refractory), AL amyloidosis.",
        "Peripheral neuropathy (most significant — dose-limiting; predominantly sensory; SC administration ↓risk vs. IV; dose reduction or switch to carfilzomib if severe), thrombocytopenia (nadir day 11, recovery day 21 — cyclical), fatigue, GI (nausea, diarrhea, constipation), herpes zoster reactivation (VZV prophylaxis mandatory — acyclovir/valacyclovir throughout therapy), hypotension.",
        "Peripheral neuropathy: SC injection significantly reduces neuropathy vs. IV (same efficacy) — now preferred route. If PN develops: reduce dose, switch to weekly dosing, or switch to carfilzomib (irreversible next-gen proteasome inhibitor — less neurotoxicity). VZV prophylaxis: ALL patients on bortezomib receive acyclovir 400mg BID (or valacyclovir) — VZV reactivation occurs in 10-15% without prophylaxis. Response marker: serum free light chains + M-protein electrophoresis."
    ),
    "lenalidomide": _dr(
        "Immunomodulatory drug (IMiD) — analog of thalidomide. Mechanism: binds cereblon (CRBN, part of E3 ubiquitin ligase complex) → promotes ubiquitination and degradation of transcription factors Ikaros (IKZF1) and Aiolos (IKZF3) → cytotoxic to myeloma/lymphoma cells + T-cell and NK-cell activation + anti-angiogenesis + anti-proliferative effects.",
        "Multiple myeloma (mainstay — induction VRd/Rd, maintenance after transplant — continuous until progression), myelodysplastic syndrome with del(5q) (DRUG OF CHOICE — induces cytogenetic remission; transfusion independence), mantle cell lymphoma, follicular lymphoma.",
        "Thrombosis (DVT/PE — IMiD class effect — prophylactic anticoagulation MANDATORY: aspirin for low-risk, LMWH/DOAC for high-risk), myelosuppression (neutropenia — dose-limiting; thrombocytopenia), teratogenicity (SEVERE — thalidomide analog; absolute CONTRAINDICATION in pregnancy — REMS program required: RevAssist/REMS — monthly pregnancy testing in women of childbearing potential), fatigue, rash, peripheral neuropathy (less than thalidomide), second primary malignancies (AML — especially after transplant).",
        "Thalidomide history: thalidomide caused 10,000+ cases of phocomelia (limb defects) in 1950-60s → withdrawn → reintroduced for multiple myeloma (with REMS) → lenalidomide developed as safer analog (less neuropathy, less VTE — though still significant). REMS program (RevAssist): prescribers, pharmacists, patients must all be enrolled; pregnancy test required monthly; only 28-day supply dispensed. Lenalidomide is highly teratogenic — single dose in first trimester can cause severe birth defects."
    ),
    "tamoxifen": _dr(
        "Selective estrogen receptor modulator (SERM) — tissue-specific ER activity: ANTAGONIST in breast (blocks ER → anti-proliferative), AGONIST in uterus (→ endometrial proliferation → endometrial cancer risk), AGONIST in bone (→ ↑BMD — osteoprotective), AGONIST in liver (→ ↑LDL receptor → ↓LDL, ↑TG). Active metabolite endoxifen formed by CYP2D6.",
        "Hormone receptor (HR)-positive breast cancer (adjuvant treatment — premenopausal women: 5-10 years → ~40-50% fewer recurrences and ~30% lower breast-cancer mortality; high-risk women without breast cancer — chemoprevention), metastatic HR+ breast cancer.",
        "Endometrial cancer (ER agonist in uterus → endometrial hyperplasia → increased risk; monitor for abnormal uterine bleeding), VTE (DVT/PE — 2-3x ↑risk — similar to oral contraceptives), menopausal symptoms (hot flashes, vaginal dryness), cataracts, mood changes. Teratogenic — contraception required. AVOID strong CYP2D6 inhibitors (fluoxetine, paroxetine) → ↓endoxifen → ↓efficacy.",
        "CYP2D6 interaction critical: tamoxifen → CYP2D6 → endoxifen (active metabolite, 30-100x more potent at ER). Strong CYP2D6 inhibitors (fluoxetine, paroxetine — antidepressants!) significantly ↓endoxifen → ↓efficacy → ↑recurrence risk. Prefer sertraline (weak CYP2D6 inhibitor) or venlafaxine for hot flashes in tamoxifen patients. Aromatase inhibitors (anastrozole, letrozole) preferred in postmenopausal women (more effective than tamoxifen) — tamoxifen preferred in premenopausal women."
    ),
    "anastrozole": _dr(
        "Non-steroidal aromatase inhibitor (AI) — reversibly inhibits aromatase (CYP19A1) → blocks conversion of androgens (androstenedione, testosterone) to estrogens (estrone, estradiol) in peripheral tissues (adipose, adrenal, muscle) → profound estrogen suppression in postmenopausal women (where ovaries are not the primary estrogen source).",
        "HR-positive breast cancer in postmenopausal women (adjuvant therapy — superior to tamoxifen in postmenopausal women: ATAC trial — ↓recurrence, ↓contralateral BC, better tolerability), metastatic HR+ breast cancer (first-line), breast cancer prevention (high-risk postmenopausal women), gynecomastia (off-label — reduces estrogen in males).",
        "Musculoskeletal symptoms (arthralgia, myalgia — most common complaint, affects 50% — joint stiffness and pain, worse in morning; ↓with exercise and vitamin D), osteoporosis (estrogen suppression → ↑bone resorption → ↓BMD — monitor with DEXA, supplement calcium + vitamin D, consider bisphosphonate), menopausal symptoms (hot flashes — less than tamoxifen, vaginal dryness, dyspareunia), lipid effects (↑LDL — unlike tamoxifen which ↓LDL), NO endometrial cancer risk (unlike tamoxifen), NO VTE risk increase (unlike tamoxifen).",
        "AIs only work in postmenopausal women (ovaries are the main estrogen source premenopausally — aromatase inhibition only reduces peripheral estrogen, not ovarian production). Aromatase inhibitors preferred over tamoxifen in postmenopausal women: ATAC trial and multiple meta-analyses show superior efficacy. AI + ovarian suppression increasingly used in premenopausal women (TEXT/SOFT trials). DEXA scan baseline and annually — AI-induced bone loss is significant and progressive."
    ),
    "filgrastim": _dr(
        "Recombinant human granulocyte colony-stimulating factor (G-CSF) — binds G-CSF receptor on myeloid progenitors and mature neutrophils → stimulates neutrophil proliferation, differentiation, survival, and functional activation. ↑Neutrophil production from bone marrow + mobilizes stem cells into peripheral blood.",
        "Chemotherapy-induced neutropenia (↓febrile neutropenia risk and duration — given 24-72h after chemotherapy completion, NOT on day of chemo), severe chronic neutropenia (congenital — Kostmann syndrome, idiopathic, cyclic), HIV-associated neutropenia, stem cell mobilization before autologous/allogeneic transplant (high-dose → mobilizes CD34+ progenitors into blood for apheresis collection), after bone marrow transplant (↑engraftment speed).",
        "Bone pain (most common — medullary expansion in long bones; ↓with NSAIDs/antihistamines), splenomegaly (↑splenic work — rare splenic rupture, especially in healthy donors), capillary leak syndrome (rare), exacerbation of sickle cell disease (do NOT use in SCD — G-CSF can trigger vaso-occlusive crisis and ARDS — FDA warning; severe/fatal crises reported), Sweet's syndrome (rare — neutrophilic dermatosis).",
        "Timing with chemotherapy critical: give G-CSF 24-72h AFTER last dose of chemotherapy — giving on same day as or before chemotherapy creates a wave of rapidly dividing myeloid cells that are MORE sensitive to cytotoxic agents → paradoxically worsens myelosuppression. Long-acting pegfilgrastim (Neulasta) — single injection per cycle (PEGylated → ↑t½ → once/cycle vs. daily filgrastim). G-CSF before stem cell harvest (PBSC mobilization): single doses or combined with plerixafor (CXCR4 antagonist) for enhanced mobilization."
    ),
    "olaparib": _dr(
        "PARP inhibitor (PARPi) — inhibits poly(ADP-ribose) polymerase 1/2 → prevents PARP-mediated base excision repair of single-strand DNA breaks → SSBs persist → collapse into DSBs during replication. In BRCA1/2-mutant cells (homologous recombination deficient — HRD), DSBs cannot be repaired by HR → synthetic lethality (PARP inhibition + HR deficiency → cell death). Normal cells with intact HR repair DSBs and survive.",
        "BRCA1/2-mutated ovarian cancer (maintenance after platinum-chemotherapy — SOLO1: 3-year PFS 60% vs. 27%; first-line maintenance after complete/partial response), BRCA1/2-mutated breast cancer (metastatic — OlympiAD: improved PFS vs. chemotherapy), BRCA1/2-mutated metastatic castration-resistant prostate cancer (PROfound trial), BRCA1/2-mutated pancreatic cancer (maintenance).",
        "Myelosuppression (anemia most common — check CBC monthly; thrombocytopenia, neutropenia), nausea and vomiting (take with food), fatigue, MDS/AML (rare but serious — especially with prior platinum exposure; monitor CBC), pneumonitis (rare). No significant CYP interactions with olaparib itself but drug is CYP3A4 substrate — avoid strong inhibitors.",
        "Synthetic lethality concept: BRCA1/2-mutant tumors rely on PARP-mediated BER (only intact DNA repair pathway) — olaparib eliminates this → tumor-specific killing. Normal cells survive (BRCA intact → HR can fix DSBs). BRCA testing now standard before prescribing. Companion diagnostics: germline and somatic BRCA testing. Biomarker expansion: HRD-positive tumors (beyond BRCA) also respond — broader testing with genomic instability scores now used."
    ),
    # ── Psychiatry ────────────────────────────────────────────────────────
    "mirtazapine": _dr(
        "Noradrenergic and specific serotonergic antidepressant (NaSSA) — blocks presynaptic alpha-2 adrenergic autoreceptors/heteroreceptors → ↑NE and 5-HT release. Also blocks H1 histamine receptors (sedation, appetite ↑), 5-HT2A (anxiolytic, improved sleep architecture) and 5-HT3 (antiemetic) receptors. No serotonin reuptake inhibition.",
        "Major depressive disorder (especially with insomnia, anxiety, anorexia, weight loss, or chemotherapy-induced nausea — beneficial side effect profile), PTSD (sleep disturbance), cancer-related anorexia/cachexia (↑appetite, weight gain — beneficial in this context), refractory nausea/vomiting (5-HT3 blockade), MDD in elderly (well-tolerated, sedating, ↑appetite).",
        "Sedation (most common — H1 blockade; useful for insomnia; paradoxically LESS sedating at higher doses as NE-enhancing effects increase), weight gain and increased appetite (H1 blockade — clinically significant, limits use in overweight patients), dry mouth, constipation, agranulocytosis (rare, 1/1000 — monitor CBC if fever/sore throat), hyperlipidemia.",
        "Paradoxical dose effect: 7.5-15 mg MORE sedating than 30-45 mg. At low doses: H1 blockade predominates → sedation. At higher doses: ↑NE release counteracts sedation. This means if sedation is problematic, INCREASE dose rather than decrease. No sexual dysfunction (no serotonin reuptake → no SSRI-related sexual SE). Few drug interactions (metabolized by CYP1A2/2D6/3A4 but inhibits none significantly). Weight gain: mirtazapine and paroxetine cause most weight gain among antidepressants."
    ),
    "trazodone": _dr(
        "Serotonin antagonist and reuptake inhibitor (SARI) — inhibits serotonin transporter (SERT) at higher doses (antidepressant) AND blocks 5-HT2A receptors (anxiolytic, improved slow-wave sleep) AND blocks H1 + alpha-1 receptors (sedation, orthostatic hypotension). At low doses (25-100 mg): primarily H1 + 5-HT2A blockade → sleep promotion with minimal antidepressant effect.",
        "Insomnia (most common use in US — low-dose 25-100 mg QHS; non-habit-forming, non-controlled substance — widely used, though AASM guidelines do not recommend it for chronic insomnia (CBT-I first-line)), major depression (antidepressant doses 150-400 mg/day — second-line; often combined with SSRIs for sleep), depression-associated anxiety, PTSD nightmares.",
        "Sedation (desired at low doses, problematic at antidepressant doses — daytime drowsiness), orthostatic hypotension (alpha-1 blockade — fall risk in elderly), priapism (prolonged painful erection — rare 1/6000 — occurs in first 28 days; UROLOGICAL EMERGENCY if >4h — cavernous fibrosis and impotence if untreated; penile aspiration + phenylephrine). Nausea, dizziness. Relatively safe in overdose — far less cardiotoxic than TCAs (QT prolongation possible).",
        "Priapism is the classic trazodone side effect — most common drug-associated priapism. Mechanism: alpha-1 blockade → vasodilation of cavernosal arteries → engorgement without detumescence. Treatment: intracavernosal phenylephrine injection (sympathomimetic → vasoconstriction) — surgical shunt if refractory. Warn male patients. At LOW doses (≤150 mg): primarily acts as sleep aid (5-HT2A blockade → ↑slow-wave sleep). No significant abuse potential — unlike benzodiazepines → commonly chosen off-label for insomnia."
    ),
    "escitalopram": _dr(
        "SSRI — selective serotonin reuptake inhibitor; S-enantiomer of citalopram (active enantiomer; R-citalopram is inactive and may inhibit S-citalopram's binding). Highest selectivity for SERT among SSRIs → fewest off-target effects → best tolerability profile. Minimal CYP interactions.",
        "Major depressive disorder (FDA-approved; first-line; STAR*D used citalopram, its racemate), generalized anxiety disorder (FDA-approved), panic disorder (off-label — effective), social anxiety disorder (off-label), OCD (off-label), PTSD (off-label).",
        "Sexual dysfunction (most common bothersome SE — delayed ejaculation, ↓libido, anorgasmia — affects 30-40%; switch to bupropion or mirtazapine if problematic), nausea and GI upset (early — takes 2-4 weeks to resolve; take with food), insomnia or somnolence, headache, QTc prolongation (citalopram/escitalopram have dose-dependent QTc prolongation — FDA limits citalopram to 40 mg/day; 20 mg/day in >60yo — less concern with escitalopram at standard doses). SIADH (rare — syndrome of inappropriate ADH — especially elderly), discontinuation syndrome (taper — brain zaps, flu-like symptoms, irritability).",
        "Escitalopram vs. citalopram: escitalopram is the pure S-enantiomer (active) → same efficacy at HALF the dose with fewer QTc concerns and better tolerability. Considered most tolerable SSRI along with sertraline — preferred first-line for most patients. CYP interactions: escitalopram minimally inhibits CYP enzymes (unlike fluoxetine — strong 2D6 inhibitor; fluvoxamine — strong 1A2/3A4 inhibitor) → safer with other medications. Full antidepressant effect takes 4-8 weeks — set expectations early."
    ),
    "buspirone": _dr(
        "Partial agonist at serotonin 5-HT1A receptors (presynaptic autoreceptors → ↓5-HT firing; postsynaptic → direct anxiolytic effect) + weak dopamine D2/D3 partial agonist. No action at GABA-A receptors (unlike benzodiazepines — mechanism entirely different). Non-sedating, non-habit-forming, no withdrawal syndrome.",
        "Generalized anxiety disorder (first-line alongside SSRIs/SNRIs — especially if substance abuse history makes benzodiazepines contraindicated; most effective for chronic persistent anxiety, less for acute situational anxiety), augmentation of antidepressants in MDD (STAR*D — buspirone augmentation), anxiety in elderly (preferred over benzodiazepines — no cognitive impairment, falls risk).",
        "Dizziness, headache, nausea, nervousness (initial activation — takes days-weeks to resolve), restlessness. NO sedation, NO cognitive impairment, NO addiction/dependence, NO withdrawal syndrome. Delayed onset: 2-4 weeks to therapeutic effect (unlike benzodiazepines which are immediate — major limitation). Drug interactions: strong CYP3A4 inhibitors ↑buspirone levels (reduce dose); avoid MAOIs (serotonin syndrome).",
        "Key advantage over benzodiazepines: no addiction, dependence, tolerance, or withdrawal — ideal for patients with substance use disorder or elderly. Major drawback: delayed onset (2-4 weeks) — benzodiazepines work immediately. DOES NOT work for PRN ('as needed') use (no acute anxiolytic effect). Patients previously on benzodiazepines often rate buspirone as ineffective — benzodiazepines suppress symptoms immediately; buspirone requires regular daily dosing. Discontinuation symptom-free (can stop abruptly)."
    ),
    # ── GI ───────────────────────────────────────────────────────────────
    "misoprostol": _dr(
        "Synthetic prostaglandin E1 (PGE1) analog — binds EP2/EP3 receptors in gastric mucosa → ↑mucus and bicarbonate secretion + ↑mucosal blood flow (cytoprotective) + ↓gastric acid secretion. In uterus: EP2/EP3 agonism → myometrial contractions (uterotonic) + cervical softening/dilation (ripening).",
        "NSAID-induced gastric ulcer prevention (FDA-approved — Cytotec; given concurrently with NSAIDs, especially in high-risk patients: elderly, prior PUD, anticoagulant use), cervical ripening and labor induction (vaginal or buccal — low-dose), postpartum hemorrhage (PPH) prevention and treatment (IM/rectal/sublingual — especially in resource-limited settings), medication abortion (mifepristone + misoprostol — up to 10 weeks gestation; misoprostol alone — 85% efficacy), incomplete/inevitable abortion management (softens cervix for D&C).",
        "GI: diarrhea and cramping (most common with oral — dose-related; less with vaginal route), nausea. Uterine: hyperstimulation (uterine tachysystole — prolonged/frequent contractions → fetal distress), uterine rupture (with prior uterine surgery — CS scar — AVOID high-dose vaginal misoprostol in VBAC candidates — risk of rupture). Fever (direct PG effect — especially with rectal/buccal route for PPH).",
        "VBAC safety: misoprostol is CONTRAINDICATED for labor induction in women with prior uterine surgery (cesarean scar) due to uterine rupture risk — use Foley balloon or low-dose oxytocin instead. PPH protocol: oxytocin first-line; misoprostol 800-1000 mcg rectally/sublingually if oxytocin unavailable (WHO recommendation for resource-limited settings). Mifepristone + misoprostol (medication abortion): mifepristone (progesterone receptor antagonist) 200 mg PO → 24-48h → misoprostol 800 mcg buccal/vaginal → 95-98% efficacy ≤10 weeks. Doses to know: labor induction/cervical ripening 25 mcg vaginally every 3–6 h (or 25–50 mcg orally every 2–4 h); early pregnancy loss 800 mcg vaginally (after mifepristone 200 mg); PPH 600–1000 mcg (oral/sublingual/rectal)."
    ),
    "sucralfate": _dr(
        "Aluminum-containing polysaccharide — in acidic environment (pH <4), undergoes polymerization and forms a viscous paste that selectively adheres to ulcer base and injured mucosa (positively charged sucralfate binds negatively charged proteins in ulcer crater) → physical protective barrier against acid, pepsin, and bile. Also stimulates mucus production, bicarbonate secretion, and PGE synthesis. Does NOT neutralize acid or inhibit proton pump.",
        "Active duodenal ulcers (FDA-approved — effective as antacids/H2 blockers but less convenient — QID dosing), stress ulcer prophylaxis in ICU (oral/NG — particularly patients on mechanical ventilation without high-risk bleeding factors; possible advantages: does not raise gastric pH, lower Clostridioides difficile risk — but less effective than PPIs/H2RAs at preventing bleeding), GERD (maintenance — limited evidence), oral mucositis (off-label — rinse/swish-spit).",
        "Constipation (aluminum — most common), aluminum toxicity in renal failure (systemic absorption of aluminum → encephalopathy, osteomalacia in severe CKD/dialysis patients — AVOID or use with caution), drug interactions (reduces absorption of fluoroquinolones, phenytoin, warfarin, digoxin, levothyroxine — space by 2h), bezoar formation (rarely).",
        "Cook 1998 (NEJM): ranitidine reduced clinically important GI bleeding vs. sucralfate with similar VAP rates; sucralfate does not raise gastric pH (theoretically less gastric colonization). PEPTIC compared PPIs with H2RAs, not sucralfate. Administer on EMPTY STOMACH (30-60 min before meals) — acid environment required for activation. Space other medications ≥2h (forms chelates)."
    ),
    "ursodiol": _dr(
        "Ursodeoxycholic acid (UDCA) — hydrophilic bile acid that when enriched in bile pool: (1) displaces hydrophobic, hepatotoxic bile acids; (2) stabilizes hepatocyte and cholangiocyte membranes (directly cytoprotective); (3) stimulates hepatocellular secretion; (4) reduces cholesterol saturation of bile (promotes cholesterol gallstone dissolution); (5) immunomodulatory (↓MHC class I expression on hepatocytes).",
        "Primary biliary cholangitis (PBC) — DRUG OF CHOICE (13-15 mg/kg/day): slows disease progression, improves LFTs, delays liver transplant; primary sclerosing cholangitis (PSC — disappointing efficacy, not standard of care), cholesterol gallstones (dissolution — non-surgical candidates: 6-24 months, ≥50% dissolution if small radiolucent stones), intrahepatic cholestasis of pregnancy (ICP — modest pruritus relief; PITCHES trial showed no reduction in stillbirth or preterm birth), NASH/NAFLD (limited evidence — not standard of care).",
        "Generally well-tolerated. Diarrhea (most common — especially at high doses), nausea, pruritus (rare). At very high doses (>28-30 mg/kg/day) in PSC: associated with INCREASED risk of colorectal neoplasia and cirrhosis complications.",
        "PBC: UDCA is standard first-line therapy — responsive patients (>40% ↓ALP at 1 year) have near-normal prognosis. Non-responders: add a PPAR agonist (elafibranor, seladelpar — approved 2024) or a fibrate; obeticholic acid (FXR agonist) is now restricted. Gallstone dissolution: only effective for cholesterol stones (not pigment stones — dark/black in hemolysis/cirrhosis), small (<1 cm), functioning gallbladder. Stones recur in 50% after stopping — not curative. ICP (obstetric cholestasis): UDCA 10-15 mg/kg/day → reduces pruritus and bile acid levels → delivery timing guided by bile-acid level (36-39 weeks)."
    ),
    # ── Respiratory ───────────────────────────────────────────────────────
    "ipratropium": _dr(
        "Short-acting muscarinic antagonist (SAMA) — quaternary ammonium compound (does NOT cross BBB → minimal CNS effects, does not cross into systemic circulation significantly — minimal systemic anticholinergic effects). Blocks M1/M3 muscarinic receptors in airways → bronchodilation + ↓mucus secretion (M3 → Gq → ↑secretions). Peak effect 30-90 min (slower than albuterol); duration 4-6h.",
        "COPD (first-line bronchodilator for COPD — preferred over SABA as monotherapy; synergistic with albuterol — Combivent/DuoNeb: ipratropium + albuterol combination for acute and maintenance), acute severe asthma exacerbation (adjunct to SABA in ED/hospital — ↓hospitalization rate), acute COPD exacerbation (ipratropium + albuterol first-line), rhinorrhea (nasal spray — allergic and non-allergic rhinitis).",
        "Dry mouth (most common — anticholinergic but minimal because quaternary structure → ↓systemic absorption), urinary retention (caution in BPH — rare at inhaled doses), constipation, tachycardia (rare), paradoxical bronchospasm (rare, stop immediately), narrow-angle glaucoma (if mist contacts eyes — use mouthpiece carefully, avoid nebulizer mist in eyes).",
        "COPD vs. asthma: anticholinergics are FIRST-LINE in COPD (M3 cholinergic tone drives bronchoconstriction in COPD → anticholinergics particularly effective); in asthma — SABA is first-line, ipratropium is adjunct only in acute exacerbations. COPD order: SAMA or LAMA first → add LABA → add ICS if high exacerbation risk. Tiotropium (LAMA) replaced ipratropium for COPD maintenance — once-daily dosing with greater efficacy. Ipratropium still primary for acute exacerbations and combination (Combivent)."
    ),
    "roflumilast": _dr(
        "Selective phosphodiesterase-4 (PDE4) inhibitor — PDE4 is the dominant PDE in inflammatory cells (neutrophils, eosinophils, T-cells, macrophages). PDE4 inhibition → ↑intracellular cAMP → suppresses inflammatory cell activation → ↓neutrophilic airway inflammation (key in COPD). Also has small bronchodilator effect (cAMP → smooth muscle relaxation). Oral — systemic anti-inflammatory (unlike inhaled therapies).",
        "Severe COPD with chronic bronchitis and frequent exacerbations (FEV1 <50% predicted, ≥2 exacerbations/year, chronic productive cough) — adjunct to LAMA + LABA (reduces exacerbation frequency ~13-17% vs. placebo — M2-124/125 and REACT trials). NOT a bronchodilator — does NOT replace inhaled therapy. NOT for asthma (not FDA-approved).",
        "GI (most common and dose-limiting — nausea, diarrhea, abdominal pain — occurs early, may resolve with time or dose reduction, take with food), weight loss (average 2-3 kg — clinically significant at times; monitor BMI), psychiatric effects (depression, suicidal ideation — label warning; screen for depression/anxiety before and during treatment), headache, insomnia. AVOID in moderate-severe hepatic impairment (hepatic metabolism).",
        "Patient selection is KEY: COPD with chronic bronchitis phenotype (chronic cough + sputum production → suggests neutrophilic inflammation → PDE4 inhibition particularly effective). Eosinophil count >150 cells/μL predicts better response. Does not cause bronchoconstriction (unlike beta-blockers). Psychiatric warning: assess baseline mental health; avoid in suicidal ideation or severe depression. Start 250 mcg daily for 4 weeks before 500 mcg to reduce GI effects and discontinuation."
    ),
    "theophylline": _dr(
        "Methylxanthine — non-selective phosphodiesterase inhibitor (↑cAMP and cGMP → bronchodilation + anti-inflammatory) + adenosine receptor antagonist (A1, A2 — contributes to bronchodilation, CNS stimulation, cardiac effects) + histone deacetylase (HDAC) activation at low doses (anti-inflammatory, ↑corticosteroid sensitivity in COPD). Narrow therapeutic index (therapeutic range 5-15 mcg/mL; toxic >20 mcg/mL).",
        "COPD (adjunct — low-dose for steroid-sensitizing effect; rarely used due to toxicity risk vs. modern inhalers), severe refractory asthma (add-on — largely supplanted by biologics), apnea of prematurity (caffeine preferred now — safer), formerly first-line for asthma (historical — now last-line due to narrow TI and drug interactions).",
        "Narrow therapeutic index — toxicity at >20 mcg/mL: GI (nausea, vomiting, diarrhea — early), CNS (anxiety, insomnia, headache → seizures — serious), cardiovascular (tachycardia, arrhythmias — atrial/ventricular → VT/VF). Drug interactions (CYP1A2 substrate): cigarette smoking INDUCES CYP1A2 → ↓levels (smokers need higher doses; levels ↑when quitting — watch for toxicity). Erythromycin, ciprofloxacin, cimetidine INHIBIT CYP1A2 → ↑toxicity. Caffeine (shared methylxanthine effects) → additive toxicity.",
        "Clinical use now very limited — replaced by safer alternatives (LABAs, tiotropium, biologics). Low-dose theophylline (5-10 mcg/mL) restores corticosteroid sensitivity in COPD (HDAC activation) — potential role in severe refractory patients. Monitor drug levels regularly and with ANY medication change (extensive CYP1A2 interactions). Toxicity antidote: activated charcoal (for ingestion), beta-blockers (for arrhythmias — despite bronchospasm risk in severe toxicity), benzodiazepines for seizures, hemodialysis for severe toxicity."
    ),


    # ── Vasopressors / Inotropes ──────────────────────────────────────────────
    "norepinephrine": _dr(
        "α1 > α2 >> β1 agonist; potent vasoconstriction + mild inotropy; ↑SVR + ↑MAP; minimal β2 (no bronchodilation)",
        "First-line vasopressor in septic shock; cardiogenic shock (with dobutamine); distributive shock; central line preferred (short-term peripheral use acceptable)",
        "Hypertension, reflex bradycardia, limb ischemia/necrosis (extravasation — phentolamine antidote), mesenteric/renal ischemia at high doses",
        "Preferred vasopressor in septic shock over dopamine (SOAP-II trial: ↓arrhythmias). Phenylephrine: pure α1 agonist — use in hypotension + tachycardia (e.g., AF with RVR + shock) to avoid reflex tachycardia worsening"
    ),
    "dopamine": _dr(
        "Dose-dependent receptor agonism: low (1-5 mcg/kg/min) = D1 → renal/mesenteric vasodilation (↑GFR); intermediate (5-10) = β1 → ↑HR + ↑contractility; high (>10) = α1 → vasoconstriction",
        "Vasopressor (second-line after norepinephrine); bradycardia with hemodynamic compromise; historically used for 'renal-protective' doses (not supported by evidence)",
        "Tachyarrhythmias (more than norepinephrine — SOAP-II: ↑AF); nausea/vomiting; extravasation causes necrosis; ↑PCWP in HF",
        "SOAP-II trial: dopamine vs norepinephrine in shock — dopamine had more arrhythmias, higher mortality in cardiogenic shock subgroup. 'Renal dose' dopamine does NOT prevent AKI — abandoned. Contraindicated in pheochromocytoma, sulfite allergy (most formulations)"
    ),
    "dobutamine": _dr(
        "Synthetic catecholamine; β1 > β2 agonist; ↑contractility (inotropy) + ↑HR; mild ↓SVR (β2); net: ↑CO + ↓filling pressures; weak α1",
        "Cardiogenic shock (with vasopressor); acute decompensated HF with low CO; stress testing (dobutamine echo — detects wall motion abnormalities)",
        "Tachyarrhythmias, ↑myocardial oxygen demand, hypotension (↓SVR), tolerance with prolonged use, ↑mortality with chronic/intermittent outpatient use (avoid long-term except palliation or bridging)",
        "Unlike dopamine, primarily inotropic not vasopressor. In cardiogenic shock: dobutamine + norepinephrine (inotropy + vasoconstriction). Milrinone preferred in patients on chronic beta-blockers (bypasses β1 receptor). Levosimendan: calcium sensitizer, improves inotropy without ↑O2 demand — not approved in US"
    ),
    "vasopressin": _dr(
        "V1 receptor agonist → smooth muscle vasoconstriction (splanchnic, skin, muscle); V2 receptor → renal collecting duct water reabsorption (via AQP2); no adrenergic effect",
        "Second-line vasopressor in septic shock (adjunct to norepinephrine — spares catecholamine dose); variceal bleeding (splanchnic vasoconstriction); central DI (desmopressin preferred); hemorrhagic shock; cardiac arrest (historical — removed from ACLS 2015)",
        "Hyponatremia (V2 effect — use with caution), mesenteric ischemia, digital ischemia, coronary vasospasm; not dose-titrated in septic shock (fixed 0.03 units/min)",
        "Fixed dose 0.03 units/min in septic shock — do NOT titrate. VANISH trial: vasopressin first → less renal replacement therapy but no mortality benefit. Terlipressin (V1-selective): preferred for variceal bleeding + hepatorenal syndrome in many countries (FDA-approved 2022 for HRS-AKI)"
    ),
    "epinephrine": _dr(
        "α1, α2, β1, β2 agonist (balanced); β1 = ↑HR + ↑contractility; α1 = vasoconstriction; β2 = bronchodilation; ↑glycogenolysis; ↑glucagon",
        "Cardiac arrest (1mg IV q3-5min — ACLS); anaphylaxis (0.3-0.5mg IM thigh — first-line); severe bronchospasm; refractory septic shock; croup (racemic nebulized); local anesthetic adjunct (↑duration, ↓bleeding)",
        "Hypertension, tachyarrhythmias, myocardial ischemia, pulmonary edema (↑PCWP), hypokalemia (β2), hyperglycemia; IV extravasation → necrosis",
        "Anaphylaxis: IM in anterolateral thigh (faster absorption than deltoid; NOT IV unless cardiac arrest or refractory). Cardiac arrest: 1mg IV/IO q3-5min — PARAMEDIC2 (out-of-hospital arrest): ↑30-day survival (3.2% vs 2.4%) but no significant gain in good neurologic outcome. Wears off quickly — repeat dosing essential in anaphylaxis"
    ),
    "phenylephrine": _dr(
        "Pure α1 agonist; ↑SVR → ↑MAP; reflex bradycardia (↑BP → baroreceptor → ↓HR); NO β effects — no ↑HR or ↑contractility",
        "Hypotension with tachycardia (e.g., SVT with hypotension, spinal anesthesia hypotension); vasoplegia; nasal decongestant (topical); mydriatic (eye drops)",
        "Reflex bradycardia, hypertension, peripheral vasoconstriction, mesenteric ischemia; avoid in cardiogenic shock (↑afterload worsens CO); no inotropy",
        "Useful when tachycardia is present or must be avoided. In neurogenic shock: phenylephrine restores SVR without ↑HR. Useful in HOCM with hypotension (↑afterload reduces LVOT obstruction) and severe AS under anesthesia (maintains coronary perfusion); avoid when LV function is poor. Spinal hypotension in obstetrics: phenylephrine preferred over ephedrine (less fetal acidosis)"
    ),
    "milrinone": _dr(
        "Phosphodiesterase-3 (PDE3) inhibitor → ↑cAMP → ↑contractility + vasodilation (arterial + venous); inodilator — ↑CO + ↓SVR + ↓PCWP; bypasses β receptor",
        "Acute decompensated HF with low CO (especially on chronic beta-blockers where dobutamine is less effective); bridge to transplant or LVAD; RV failure after cardiac surgery",
        "Hypotension (vasodilation — may need vasopressor coadministration), tachyarrhythmias, thrombocytopenia; renally cleared — dose-reduce in AKI; ↑mortality in chronic oral use (PROMISE trial — not for chronic therapy)",
        "Advantage over dobutamine in beta-blocker patients (bypasses β1 receptor). OPTIME-CHF trial: milrinone in acute HF → ↑hypotension + ↑arrhythmias, no mortality benefit, worse outcomes in ischemic etiology. Use with vasopressor if hypotensive"
    ),
    # ── Analgesics / Opioids ──────────────────────────────────────────────────
    "oxycodone": _dr(
        "Semisynthetic opioid; μ-opioid receptor agonist; hepatic CYP3A4 + CYP2D6 metabolism; active metabolite oxymorphone (CYP2D6); oral bioavailability ~60-87% (higher than morphine)",
        "Moderate-to-severe acute pain; chronic pain (ER formulation); cancer pain; OxyContin (ER); Percocet (oxycodone + acetaminophen); Percodan (+ aspirin)",
        "Constipation (treat prophylactically), respiratory depression, sedation, nausea/vomiting, physical dependence, addiction; avoid in severe hepatic impairment",
        "High abuse potential — Schedule II. CYP2D6 poor metabolizers: ↓analgesic effect. CYP3A4 inhibitors (azole antifungals, macrolides): ↑oxycodone levels → toxicity. OxyContin abuse led to opioid crisis; ER formulation now tamper-resistant. Naloxone reversal dose may need to be repeated (oxycodone half-life longer than naloxone)"
    ),
    "hydromorphone": _dr(
        "Semisynthetic opioid; μ-opioid agonist; 5-10× more potent than morphine; faster onset; hepatic glucuronidation → hydromorphone-3-glucuronide (neuroexcitatory metabolite — accumulates in renal failure → myoclonus, seizures)",
        "Severe acute pain (post-op, cancer); opioid-tolerant patients; IV/SC/IM/oral; PCA use; often used when morphine causes excessive histamine release",
        "Respiratory depression, sedation, nausea, constipation, urinary retention; neuroexcitatory metabolite in renal failure (H3G → myoclonus, seizures, cognitive impairment); physical dependence",
        "Preferred over morphine in renal failure (morphine-6-glucuronide accumulates more); 5-10× more potent (dosing error risk — HIGH-ALERT medication). PO to IV conversion: 7.5mg PO ≈ 1.5mg IV. Dilaudid is brand name. Schedule II"
    ),
    "tramadol": _dr(
        "Weak μ-opioid agonist + SNRI (inhibits serotonin + norepinephrine reuptake); prodrug activated by CYP2D6 (to O-desmethyltramadol — active opioid component)",
        "Moderate pain; neuropathic pain (SNRI component); sometimes used in fibromyalgia",
        "Seizures (↓seizure threshold — avoid in seizure disorders), serotonin syndrome (with SSRIs/SNRIs/MAOIs), nausea/vomiting, constipation, dizziness; less respiratory depression than traditional opioids but still present; physical dependence",
        "CYP2D6 ultra-rapid metabolizers: rapid conversion → opioid toxicity (↑respiratory depression). CYP2D6 poor metabolizers: ↓efficacy. Contraindicated with MAOIs (serotonin syndrome). Avoid in epilepsy, suicidal ideation. Schedule IV. NOT safer than other opioids in terms of abuse/dependence despite lower DEA schedule"
    ),
    "naltrexone": _dr(
        "Pure opioid antagonist (μ > δ > κ); orally bioavailable; blocks opioid receptors competitively; hepatic metabolism; half-life 4h (nalmefene longer-acting); extended-release IM (Vivitrol) monthly",
        "Opioid use disorder (OUD) maintenance treatment — prevents euphoria from opioids; alcohol use disorder (AUD) — reduces craving and reward; extended-release IM preferred for adherence",
        "Hepatotoxicity at very high doses (liver function monitoring); opioid withdrawal precipitation if opioids present (must be opioid-free 7-10 days before starting); nausea, fatigue, myalgia; avoid in acute hepatitis/liver failure",
        "Distinct from naloxone (naltrexone = long-acting oral/IM; naloxone = short-acting IV/IN for overdose reversal). Patient must be opioid-free ≥7-10 days to avoid precipitated withdrawal. MOUD options: buprenorphine (partial agonist), methadone (full agonist, highly regulated), naltrexone (antagonist — no abuse potential)"
    ),
    "codeine": _dr(
        "Prodrug — converted to morphine by CYP2D6 (~10% of dose); weak μ-opioid agonist; antitussive at subanalgetic doses; phosphate salt",
        "Mild-to-moderate pain (often combined with acetaminophen); antitussive (cough suppression); antidiarrheal",
        "Respiratory depression (esp. CYP2D6 ultra-rapid metabolizers — life-threatening in children); constipation, nausea, sedation; abuse potential; physical dependence",
        "FDA BLACK BOX: contraindicated in children <12yo for pain; <18yo post-tonsillectomy/adenoidectomy; breastfeeding mothers (infant deaths reported). Ultra-rapid metabolizers convert to high morphine levels → respiratory arrest. Poor metabolizers get no analgesia. Being phased out in pediatrics. Schedule II-V depending on formulation"
    ),
    "celecoxib": _dr(
        "Selective COX-2 inhibitor (spares COX-1); ↓prostaglandin synthesis → anti-inflammatory, analgesic, antipyretic; GI mucosa protection maintained (COX-1 activity preserved) → ↓GI ulcers vs non-selective NSAIDs",
        "Osteoarthritis, rheumatoid arthritis, acute pain, dysmenorrhea, ankylosing spondylitis; familial adenomatous polyposis (FDA indication withdrawn 2011)",
        "Cardiovascular risk (↑MI, stroke — class effect for COX-2 selective agents; rofecoxib withdrawn 2004); renal insufficiency, hypertension, edema; sulfonamide allergy cross-reactivity (contains sulfonamide moiety — use caution); minimal GI ulceration",
        "PRECISION trial: celecoxib non-inferior to ibuprofen and naproxen for CV events in arthritis patients. Still carries CV warning but lower absolute risk than early data suggested. Preferred NSAID in high GI-risk patients. Avoid in severe renal impairment, last trimester of pregnancy (premature ductus closure)"
    ),
    "naproxen": _dr(
        "Non-selective COX-1 + COX-2 inhibitor; NSAID; long half-life (12-17h) allows twice-daily dosing; inhibits thromboxane A2 (platelet aggregation) and prostaglandins",
        "Osteoarthritis, RA, acute pain, dysmenorrhea, gout attacks, migraine, fever; OTC (Aleve) and prescription formulations",
        "GI ulceration/bleeding (add PPI in high-risk patients), renal insufficiency (↓renal prostaglandins → ↓GFR), hypertension, edema, cardiovascular events (lower CV risk than ibuprofen per meta-analyses), platelet dysfunction",
        "Among NSAIDs, naproxen appears to have the most favorable cardiovascular profile (least ↑CV risk). Avoid in CKD (eGFR <30), severe HF, third trimester pregnancy. Analgesic ceiling effect — higher doses → more toxicity without more analgesia. Take with food. Avoid in aspirin-sensitive asthma"
    ),
    "indomethacin": _dr(
        "Non-selective COX-1 + COX-2 inhibitor; one of the most potent NSAIDs; also used to close patent ductus arteriosus (↓prostaglandin E2 keeps PDA open)",
        "Gout (acute attack — very effective), ankylosing spondylitis, pericarditis (with colchicine), heterotopic ossification prophylaxis, PDA closure in neonates (IV formulation)",
        "High GI toxicity (ulcers, bleeding), headache/dizziness (CNS effects more prominent than other NSAIDs), renal insufficiency, hypertension, platelet dysfunction; contraindicated in neonates with renal impairment/NEC/bleeding",
        "Drug of choice for acute gout if colchicine contraindicated. For PDA: indomethacin 0.2mg/kg IV q12h × 3 doses; ibuprofen or acetaminophen IV are alternatives. Notably effective for pericarditis pain. One of oldest/most studied NSAIDs. Complete response defines paroxysmal hemicrania and hemicrania continua. High CNS side effects limit use"
    ),
    # ── Antibiotics — Missing ─────────────────────────────────────────────────
    "cephalexin": _dr(
        "1st-generation cephalosporin; β-lactam; oral bioavailability ~90%; inhibits cell wall synthesis (PBP binding → bactericidal); covers gram+ (staph, strep) > gram- (limited)",
        "Uncomplicated skin/soft tissue infections (non-purulent cellulitis, impetigo — MSSA); strep pharyngitis (penicillin alternative); UTI (uncomplicated); (IV cefazolin is the 1st-gen agent used for surgical prophylaxis)",
        "GI upset (most common), allergic reactions (cross-reactivity with penicillin ~1-2% in true penicillin allergy), C. difficile (low risk)",
        "Non-purulent cellulitis (strep/MSSA): cephalexin 500mg QID × 5d. No MRSA coverage. 'Keflex' brand name. Better oral option than amoxicillin for skin infections. Penicillin allergy: if non-anaphylactic, cephalexin safe to use (low cross-reactivity). Dose-adjust in renal impairment"
    ),
    "clarithromycin": _dr(
        "Macrolide antibiotic; inhibits 50S ribosomal subunit (23S rRNA) → ↓protein synthesis; bacteriostatic; potent CYP3A4 inhibitor (major drug interactions); hepatic metabolism",
        "Community-acquired pneumonia (atypical organisms — Mycoplasma, Chlamydophila, Legionella); H. pylori (PPI + clarithromycin + amoxicillin — now only when clarithromycin susceptibility is known); MAC prophylaxis/treatment (HIV); sinusitis, pharyngitis",
        "GI upset (metallic taste), QT prolongation (torsades risk), hepatotoxicity; MAJOR CYP3A4 inhibitor — ↑levels of statins (myopathy), warfarin, digoxin, colchicine, many immunosuppressants; hypotension/AKI with calcium channel blockers (CYP3A4)",
        "H. pylori eradication: clarithromycin-based triple therapy — BUT ↑clarithromycin resistance (>15% in US) → bismuth quadruple therapy preferred empirically. MAC in HIV: azithromycin preferred (weekly, better tolerated, fewer drug interactions). QTc prolongation: use with caution in cardiac patients"
    ),
    "ampicillin": _dr(
        "Aminopenicillin; β-lactam; inhibits cell wall PBP; broader gram- coverage than natural penicillins; acid-stable (oral); IV formulation; NOT β-lactamase stable",
        "Listeria monocytogenes (meningitis/bacteremia — drug of choice); enterococcal infections (UTI, endocarditis — with gentamicin for SBE); group B strep prophylaxis in labor; biliary infections; meningitis empiric (with ceftriaxone in neonates/elderly)",
        "Rash (maculopapular — NOT allergy, common with EBV/mono — classically 70-100% of ampicillin-treated mono; ~30% in recent studies); GI upset; C. difficile; allergy (anaphylaxis); ↑resistance from β-lactamase",
        "Ampicillin + rash: Epstein-Barr virus mononucleosis → frequent maculopapular rash (not IgE-mediated, not true allergy — patient can receive penicillin again). Ampicillin-sulbactam (Unasyn) adds β-lactamase inhibitor. Listeria: cephalosporins have NO activity — ampicillin or TMP-SMX required"
    ),
    "ertapenem": _dr(
        "Carbapenem β-lactam; inhibits cell wall PBPs; broad spectrum: covers gram+, gram-, anaerobes; unlike other carbapenems, no Pseudomonas/Acinetobacter/Enterococcus coverage; once-daily dosing (t½ 4h)",
        "Community-acquired intraabdominal infections; complicated UTI/pyelonephritis; diabetic foot infections; ESBL-producing enterobacteriaceae; aspiration pneumonia; outpatient IV therapy (once-daily convenient)",
        "GI upset, diarrhea, C. difficile, seizures (lower risk than imipenem), hypersensitivity (cross-reactivity with penicillin <1%); not for Pseudomonas/Acinetobacter/MRSA",
        "Key advantage over meropenem/imipenem: once-daily dosing allows outpatient IV. Key disadvantage: NO Pseudomonas coverage — do not use if Pseudomonas suspected (hospital-acquired, immunocompromised, structural lung disease). Does cover ESBL Enterobacteriaceae. Imipenem has highest seizure risk of carbapenems (do not use in CNS infections)"
    ),
    "tigecycline": _dr(
        "Glycylcycline antibiotic; binds the 30S ribosomal subunit (blocks aminoacyl-tRNA entry → ↓protein synthesis); overcomes tetracycline resistance (tet pump/ribosomal protection); bacteriostatic; broad spectrum",
        "Complicated skin/soft tissue infections (MRSA, VRE, anaerobes); complicated intraabdominal infections; community-acquired pneumonia; covers MRSA, VRE, ESBL, Acinetobacter, Stenotrophomonas; NOT for Pseudomonas",
        "Nausea/vomiting (↑ vs other antibiotics — dose-limiting), photosensitivity, tooth discoloration (avoid in children <8yo, pregnancy — class D), hepatotoxicity; BLACK BOX: ↑all-cause mortality vs other antibiotics in clinical trials",
        "FDA black box warning: tigecycline associated with ↑mortality in clinical trials (mechanism unclear — possibly subtherapeutic levels from rapid distribution into tissue). Use only when alternatives not suitable. NOT for bacteremic patients or hospital-acquired pneumonia. Covers most resistant organisms but poor pharmacodynamics in bloodstream"
    ),
    "fosfomycin": _dr(
        "Phosphonic acid antibiotic; inhibits MurA (first step in peptidoglycan synthesis — blocks UDP-GlcNAc → fosfomycin binds active site covalently); bactericidal; single-dose oral (trometamol salt) achieves high urine concentrations",
        "Uncomplicated lower UTI in women (single 3g oral dose); ESBL-producing E. coli UTI; MRSA UTI; Enterococcus faecalis UTI; Vancomycin-resistant Enterococcus UTI (IV formulation in some countries)",
        "GI upset (diarrhea, nausea — most common), headache; generally well tolerated with single dose; rare: hypokalemia; avoid in severe renal impairment (eGFR <30 — reduced urinary concentration)",
        "Single-dose convenience — excellent adherence. Active against most common UTI pathogens including ESBL and MRSA. Resistance rates low (unique mechanism — few bacteria have MurA mutations). Not effective for upper UTI/pyelonephritis (insufficient tissue levels with oral formulation). IV formulation used for systemic MRSA in Europe — not available in US"
    ),
    "colistin": _dr(
        "Polymyxin antibiotic; disrupts gram-negative outer membrane (binds lipopolysaccharide LPS → detergent effect → membrane permeabilization → cell death); bactericidal; last-resort antibiotic; colistimethate sodium (CMS) = prodrug",
        "Last-resort treatment for carbapenem-resistant gram-negative infections (Pseudomonas aeruginosa, Acinetobacter baumannii, Klebsiella pneumoniae — CRE); used when no other options available",
        "Nephrotoxicity (↑SCr in 30-50% — monitor closely); neurotoxicity (paresthesias, dizziness, neuromuscular blockade, apnea); dose-adjust in renal impairment; inhaled colistin for respiratory infections (less systemic toxicity)",
        "CMS (colistimethate sodium) is the prodrug → converted to colistin in vivo; optimal dosing complex — use PK/PD models + clinical pharmacist. Often combined with rifampin, meropenem, or fosfomycin for synergy against XDR organisms. Polymyxin B: similar mechanism, used as active drug (not prodrug); different PK — prefer for systemic infections"
    ),
    "cefdinir": _dr(
        "3rd-generation oral cephalosporin; β-lactam; broad-spectrum gram+ and gram- coverage; oral formulation (bioavailability ~25%); not active against Pseudomonas or MRSA",
        "Community-acquired pneumonia; acute bacterial exacerbation of chronic bronchitis; sinusitis; otitis media (children — common use); skin/soft tissue infections (non-MRSA); pharyngitis",
        "GI upset (red/orange stools if taken with iron supplements — benign but alarming to patients), allergic reactions, C. difficile, false-positive urine glucose (Clinitest)",
        "Red stools from iron-cefdinir complex — educate patients taking iron. Very commonly prescribed for pediatric otitis media (Omnicef brand). No activity vs MRSA, Pseudomonas, or atypical organisms. Advantage: once-daily dosing for some indications. Lower bioavailability means higher doses needed"
    ),
    # ── Antivirals ────────────────────────────────────────────────────────────
    "valacyclovir": _dr(
        "Prodrug of acyclovir; L-valyl ester → converted by intestinal/hepatic valacyclovirase to acyclovir; oral bioavailability 54% (vs 15-30% acyclovir → higher tissue levels achievable orally); same mechanism as acyclovir (thymidine kinase-dependent activation → chain termination)",
        "HSV-1/HSV-2: oral herpes (cold sores), genital herpes (episodic + suppressive therapy); herpes zoster (shingles — 1g TID × 7d); VZV; CMV prophylaxis (in transplant — 2g QID); Bell's palsy (controversial but commonly used)",
        "Same as acyclovir: headache, nausea, renal insufficiency (adequate hydration required); TTP/HUS at high doses (2g QID in immunocompromised — associated with TMA); CNS toxicity in renal failure",
        "Preferred over acyclovir orally due to higher bioavailability → simpler dosing, higher plasma levels. Herpes zoster: initiate within 72h of rash onset (or if new lesions still appearing). Suppressive therapy for genital herpes: 500mg-1g daily → ↓transmission by ~50%. Famciclovir (prodrug of penciclovir): similar indications, alternative choice"
    ),
    "remdesivir": _dr(
        "Adenosine nucleoside prodrug; phosphoramidate prodrug → active triphosphate → incorporates into viral RNA → causes premature chain termination; broad antiviral spectrum (RNA viruses); targets RNA-dependent RNA polymerase (RdRp)",
        "COVID-19 (hospitalized patients requiring supplemental O2 — 5-day course; reduced time to recovery in ACTT-1 trial); also has activity against Ebola (used in DRC outbreak), Marburg, RSV, hepatitis C; IV only (poor oral bioavailability)",
        "Bradycardia (transient — infusion-related), nausea, elevated LFTs, infusion-related hypersensitivity; IV formulation (no oral); no renal dose adjustment (FDA removed the eGFR restriction in 2023)",
        "ACTT-1 trial: remdesivir ↓time to recovery (10 vs 15 days) in hospitalized COVID-19 patients on O2; no mortality benefit shown. WHO Solidarity trial: no mortality benefit. Best benefit in patients on low-flow O2. Not recommended for patients not on O2 or requiring mechanical ventilation. FDA-approved for COVID-19 (Veklury). Activity against many RNA viruses makes it a broad-spectrum candidate"
    ),
    "nirmatrelvir-ritonavir": _dr(
        "Nirmatrelvir: oral SARS-CoV-2 protease inhibitor (3CLpro/Mpro — blocks viral polyprotein cleavage → prevents replication); Ritonavir: CYP3A4 inhibitor (pharmacokinetic booster — ↑nirmatrelvir levels by inhibiting its metabolism); co-packaged as Paxlovid",
        "COVID-19 in high-risk adults with mild-to-moderate disease (symptom onset ≤5 days; ↓hospitalizations/death by ~89% in unvaccinated high-risk adults — EPIC-HR trial); prescribed under EUA/full approval",
        "Dysgeusia (metallic taste — very common, 5%), diarrhea, hypertension, myalgia; MAJOR drug interactions via ritonavir CYP3A4 inhibition (↑levels of: statins → myopathy, tacrolimus/cyclosporine → toxicity, anticoagulants, antiarrhythmics, sedatives — CONTRAINDICATED with many drugs); 'COVID rebound' (symptom recurrence after completing course)",
        "Ritonavir is a potent CYP3A4 inhibitor — must HOLD statins, many other medications during 5-day course (drug-drug interactions are the primary barrier to prescribing). COVID rebound: ~5-7% of patients develop symptom recurrence at day 7-10 (unclear mechanism; extended course controversial). Nirmatrelvir resistance emerging. Alternatives: molnupiravir (lower efficacy), remdesivir (IV)"
    ),
    "valganciclovir": _dr(
        "Oral prodrug of ganciclovir; L-valyl ester → intestinal/hepatic hydrolysis → ganciclovir; bioavailability ~60% (vs oral ganciclovir 6%); ganciclovir: nucleoside analogue → phosphorylated by viral UL97 kinase → inhibits CMV DNA polymerase",
        "CMV retinitis (AIDS — oral equivalent to IV ganciclovir); CMV prophylaxis in solid organ transplant recipients (900mg QD); CMV disease treatment (induction: 900mg BID × 21d); prevention of CMV in high-risk transplant (D+/R-)",
        "Myelosuppression (neutropenia — dose-limiting, monitor CBC weekly; ↑with mycophenolate coadministration), anemia, thrombocytopenia; carcinogenic + teratogenic (animal data) — use contraception during and 90d after; potential carcinogen",
        "Neutropenia is the main limiting toxicity — often requires G-CSF (filgrastim) support. Resistance via UL97 kinase mutations (ganciclovir-resistant CMV) → switch to foscarnet or cidofovir. Foscarnet: pyrophosphate analogue, nephrotoxic but no cross-resistance with ganciclovir. Letermovir: CMV-specific terminase inhibitor for prophylaxis (less myelotoxic)"
    ),
    # ── Antifungals ───────────────────────────────────────────────────────────
    "itraconazole": _dr(
        "Triazole antifungal; inhibits fungal CYP51 (lanosterol 14α-demethylase) → ↓ergosterol synthesis → disrupts cell membrane; broader spectrum than fluconazole (dermatophytes, dimorphic fungi); solution has higher bioavailability than capsule",
        "Histoplasmosis (mild-moderate; step-down from amphotericin B); blastomycosis (mild-moderate); sporotrichosis (lymphocutaneous); onychomycosis (nail fungus); dermatophytosis; aspergillosis (alternative to voriconazole); coccidioidomycosis",
        "GI intolerance (nausea, diarrhea — especially oral solution), negative inotrope effect → contraindicated in HF; potent CYP3A4 inhibitor (major drug interactions — similar to ritonavir); hepatotoxicity; hypokalemia; alopecia; hypersensitivity",
        "Negative inotrope: contraindicated in CHF/LV dysfunction. Cyclodextrin vehicle in oral solution — laxative effect, but better absorbed. Take capsule with acidic food/cola (acid-dependent absorption); solution taken on empty stomach. TDM: trough levels 0.5-1 mg/L (prophylaxis), >1 mg/L (treatment). Voriconazole has largely replaced it for Aspergillus"
    ),
    "posaconazole": _dr(
        "Extended-spectrum triazole; inhibits fungal CYP51 → ↓ergosterol; broadest spectrum azole (covers Aspergillus, Mucor/Rhizopus — rare among azoles); oral delayed-release tablet (better bioavailability than suspension) or IV",
        "Prophylaxis in high-risk immunocompromised patients (AML induction chemotherapy, GVHD on steroids — Cornely and Ullmann 2007 trials: ↓invasive fungal infections; ↓mortality in AML); salvage for refractory aspergillosis; mucormycosis (after/with amphotericin B); fluconazole-resistant Candida",
        "QT prolongation, hepatotoxicity, nausea/vomiting; potent CYP3A4 inhibitor (major drug interactions — ↑tacrolimus, cyclosporine, midazolam, statins); hypokalemia/hypomagnesemia",
        "One of only two azoles active against Mucorales (with isavuconazole) — used as step-down after amphotericin B for mucormycosis. Tablet formulation significantly better than suspension. TDM: trough >0.7 mg/L (prophylaxis), >1 mg/L (treatment). Isavuconazole (Cresemba): newer broad-spectrum azole, better tolerated, fewer drug interactions — alternative to posaconazole"
    ),
    "micafungin": _dr(
        "Echinocandin antifungal; inhibits β-(1,3)-glucan synthase → ↓cell wall glucan synthesis (essential for Candida/Aspergillus, absent in mammals) → fungicidal against Candida, fungistatic against Aspergillus; IV only",
        "Invasive candidiasis including candidemia (first-line); esophageal candidiasis; Candida prophylaxis in HSCT recipients; aspergillosis (salvage); active against azole-resistant Candida (C. glabrata, C. krusei, C. auris)",
        "Hepatotoxicity (monitor LFTs), infusion-related reactions (rare); generally very well tolerated; minimal drug interactions (not a CYP450 substrate or inhibitor); no dose adjustment for renal/mild hepatic impairment",
        "Echinocandins (caspofungin, micafungin, anidulafungin) are preferred first-line for invasive candidiasis (IDSA guidelines). Less active against non-Candida/Aspergillus fungi (Cryptococcus, dimorphic fungi — intrinsically resistant). Candida auris: echinocandin first-line but resistance emerging. No oral formulation (any echinocandin). Kuse 2007 trial: micafungin non-inferior to liposomal amphotericin B for candidemia"
    ),
    # ── GI Drugs ─────────────────────────────────────────────────────────────
    "pantoprazole": _dr(
        "Proton pump inhibitor (PPI); irreversibly inhibits H+/K+-ATPase (proton pump) on gastric parietal cell secretory canaliculus; prodrug activated at pH <4; suppresses acid secretion >90%; available IV (advantage over omeprazole in inpatients)",
        "GERD, peptic ulcer disease (H. pylori — part of eradication regimens), stress ulcer prophylaxis (ICU patients), upper GI bleed (IV — post-endoscopic therapy), Zollinger-Ellison syndrome, NSAID-induced ulcers",
        "C. difficile infection (↑risk — alteration of gut microbiome), pneumonia (↑risk in hospitalized patients — aspiration of colonized oral bacteria), hypomagnesemia (chronic use), vitamin B12 deficiency (chronic), fractures (chronic — ↓Ca absorption), drug interactions (↓clopidogrel activation via CYP2C19 — omeprazole worse than pantoprazole)",
        "IV pantoprazole preferred in inpatients (omeprazole no IV formulation in US). PPI overuse: ~50% of hospitalized patients on PPIs don't have clear indication — associated with C. diff, pneumonia, hypomagnesemia. H. pylori: bismuth quadruple therapy (PPI + bismuth + metronidazole + tetracycline × 14 days) is first-line (ACG 2024). Stress ulcer prophylaxis: patients on mechanical ventilation + coagulopathy (otherwise minimal evidence)"
    ),
    "famotidine": _dr(
        "H2-receptor antagonist (H2RA); competitively blocks histamine H2 receptors on gastric parietal cells → ↓cAMP → ↓H+/K+-ATPase activity → ↓acid secretion; less complete acid suppression than PPIs; more rapid onset",
        "GERD (mild-moderate), peptic ulcer disease, Zollinger-Ellison, stress ulcer prophylaxis (when PPI not needed), heartburn (OTC), IV formulation for NPO patients",
        "Headache, dizziness; rare: thrombocytopenia, confusion in elderly/renal impairment (cimetidine, not famotidine, raises creatinine by blocking tubular secretion); dose-reduce in renal impairment (renally cleared); less effective than PPIs for acid suppression",
        "Ranitidine (Zantac) withdrawn 2020 due to NDMA contamination → famotidine now the preferred H2RA. H2RAs do not require acid for activation (unlike PPIs) → faster onset and effective when PPIs have not yet taken effect. Tachyphylaxis: H2RAs lose efficacy with continuous use (receptor upregulation). Often used in combination with PPI for nocturnal acid breakthrough"
    ),
    "prochlorperazine": _dr(
        "Phenothiazine antipsychotic/antiemetic; D2 receptor antagonist in chemoreceptor trigger zone (CTZ) + vomiting center; also has antihistamine, anticholinergic, α1-blocking properties",
        "Nausea/vomiting (post-operative, chemotherapy, migraine, ER setting — IV/IM); vertigo; acute agitation (IM — less used); migraine headache (IV/IM — often with diphenhydramine to prevent akathisia)",
        "Extrapyramidal symptoms (EPS: akathisia, dystonia, drug-induced Parkinsonism — pretreat with diphenhydramine or benztropine), sedation, hypotension (α1 blockade), QT prolongation; neuroleptic malignant syndrome (rare but potentially fatal); tardive dyskinesia (chronic use)",
        "IV in ED for migraine: prochlorperazine 10mg IV + diphenhydramine 25mg IV (prevents akathisia — very effective 'migraine cocktail'); ketorolac often added. Akathisia (restlessness, compulsion to move) is common and distressing — always premedicate. Avoid in Parkinson's disease (worsens symptoms)"
    ),
    # ── Psychiatric / Neuro ───────────────────────────────────────────────────
    "paroxetine": _dr(
        "SSRI + significant muscarinic (anticholinergic) + histamine H1 antagonism; potent CYP2D6 inhibitor; strong serotonin reuptake inhibition; short half-life (~21h — ↑discontinuation syndrome risk) with NO active metabolite",
        "Major depression, panic disorder, social anxiety disorder, GAD, PTSD, OCD, premenstrual dysphoric disorder (PMDD), menopausal hot flashes (non-hormonal)",
        "Anticholinergic effects (dry mouth, constipation, urinary retention, blurred vision — more than other SSRIs), weight gain, sexual dysfunction, sedation; SEVERE discontinuation syndrome (taper slowly); QT prolongation (less than TCAs); teratogenicity (Pregnancy category D — cardiac defects, persistent pulmonary HTN of newborn)",
        "Highest anticholinergic burden of SSRIs — avoid in elderly (Beers criteria). Worst discontinuation syndrome of SSRIs (short half-life, no active metabolite) — 'brain zaps', flu-like symptoms. Potent CYP2D6 inhibitor — ↓conversion of tamoxifen to its active metabolite (endoxifen) → ↓efficacy of tamoxifen in breast cancer. Contraindicated with MAOIs (serotonin syndrome)"
    ),
    "nortriptyline": _dr(
        "Tricyclic antidepressant (TCA); secondary amine (metabolite of amitriptyline); blocks norepinephrine + serotonin reuptake; also blocks muscarinic, α1-adrenergic, H1-histamine receptors; less anticholinergic than amitriptyline",
        "Depression (particularly melancholic); neuropathic pain (diabetic neuropathy, post-herpetic neuralgia); migraine prophylaxis; chronic pain syndromes; smoking cessation (off-label); enuresis (in children)",
        "Anticholinergic (less than amitriptyline): dry mouth, constipation, urinary retention; sedation, weight gain, orthostatic hypotension, QTc prolongation, tachycardia; LETHAL in overdose (wide QRS → ventricular arrhythmias — sodium bicarbonate treatment); sexual dysfunction",
        "Among TCAs, nortriptyline + desipramine have lowest anticholinergic burden → preferred in elderly (but still use caution — Beers criteria). Therapeutic drug monitoring: nortriptyline 50-150 ng/mL. TCA overdose: sodium bicarb (narrows QRS), physostigmine CONTRAINDICATED (asystole, seizures), magnesium (TdP). CYP2D6 metabolizes TCAs — paroxetine inhibition → ↑TCA levels → toxicity"
    ),
    "ziprasidone": _dr(
        "Atypical antipsychotic (SGA); D2 + D3 + 5-HT2A antagonist; also 5-HT1A partial agonist + SNRI properties; minimal H1 and muscarinic blockade; highest QT prolongation among atypicals",
        "Schizophrenia, bipolar mania and maintenance, acute agitation (IM formulation); acute psychosis; schizoaffective disorder",
        "QTc prolongation (most among atypicals — baseline ECG required; avoid with other QT-prolonging drugs or hypokalemia/hypomagnesemia); orthostatic hypotension, sedation; EPS (less than FGAs); minimal weight gain/metabolic effects (advantage vs olanzapine/quetiapine); must take with food (↑bioavailability by 2×)",
        "Metabolic advantages: minimal weight gain, minimal glucose/lipid effects (vs olanzapine, quetiapine). QT prolongation is the main concern — screen ECG before starting, check electrolytes. MUST take with food (≥500 cal meal doubles absorption). IM ziprasidone for acute agitation — onset 15-20 min. Caution with concurrent QT-prolonging drugs (macrolides, fluoroquinolones, antiarrhythmics)"
    ),
    "lurasidone": _dr(
        "Atypical antipsychotic (SGA); D2 + D3 antagonist, 5-HT2A antagonist, 5-HT7 antagonist, partial 5-HT1A agonist, α2C antagonist; minimal H1 + muscarinic blockade → favorable metabolic profile",
        "Schizophrenia; bipolar I depression (FDA-approved — one of few antipsychotics approved for bipolar depression); adult/pediatric schizophrenia; adjunctive/monotherapy bipolar depression",
        "Akathisia (most common — prominent), somnolence, EPS, nausea; minimal weight gain; minimal metabolic effects; QT prolongation minimal; MUST take with food (≥350 cal)",
        "One of the few agents FDA-approved for bipolar depression (along with quetiapine, olanzapine-fluoxetine, cariprazine and lumateperone). Metabolic profile similar to aripiprazole — minimal weight gain/metabolic effects. 5-HT7 antagonism may contribute to antidepressant effect and cognitive improvement. CYP3A4 substrate — avoid strong CYP3A4 inhibitors/inducers (ketoconazole, rifampin). Must take with food — 2-3x ↑AUC"
    ),
    "rivastigmine": _dr(
        "Reversible acetylcholinesterase inhibitor + butyrylcholinesterase inhibitor (dual inhibitor — distinguishes from donepezil/galantamine); pseudo-irreversible binding (carbamylation); available as oral, transdermal patch; brain-selective",
        "Alzheimer's disease (mild-to-moderate); Parkinson's disease dementia (only cholinesterase inhibitor FDA-approved for PD dementia); Lewy body dementia; transdermal patch reduces GI side effects",
        "GI (nausea, vomiting, diarrhea — dose-limiting, reduced with titration and patch formulation), weight loss, dizziness, headache; cholinergic effects (bradycardia, syncope); patch: skin irritation, avoid heat exposure (↑absorption)",
        "Transdermal patch: comparable efficacy to oral, significantly less GI side effects — preferred for patients who develop GI intolerance. EXELON patch. Only cholinesterase inhibitor approved for PD dementia — important clinical point. Start at low dose, titrate monthly. Does NOT slow disease progression — symptomatic benefit only. Patch: rotate sites daily"
    ),
    "modafinil": _dr(
        "Wakefulness-promoting agent; exact mechanism unclear — inhibits dopamine reuptake (DAT inhibitor) → ↑dopamine + norepinephrine; also ↑histamine, serotonin, glutamate, ↓GABA in wake-promoting regions; does NOT cause sensitization/euphoria like amphetamines at therapeutic doses",
        "Narcolepsy (with/without cataplexy — FDA-approved); shift work sleep disorder; obstructive sleep apnea (adjunct to CPAP); off-label: ADHD, fatigue in multiple sclerosis, cancer-related fatigue, cognitive enhancement",
        "Headache (most common), nausea, nervousness, insomnia; Stevens-Johnson syndrome/TEN (rare but serious — discontinue at first sign of rash); CYP3A4 inducer (↓levels of: hormonal contraceptives — ADVISE additional contraception; cyclosporine, warfarin, many drugs); schedule IV",
        "Armodafinil (R-enantiomer): longer half-life, once-daily dosing, used for same indications. Modafinil is NOT a first-line stimulant for ADHD (better evidence for methylphenidate, amphetamines). CYP3A4 induction: backup contraception required. Lower abuse potential than traditional stimulants (amphetamines). Schedule IV (lower than amphetamines Schedule II)"
    ),
    # ── Cardiovascular ────────────────────────────────────────────────────────
    "atenolol": _dr(
        "Cardioselective β1-blocker (β1 >> β2 at therapeutic doses); hydrophilic (renal elimination, no CNS penetration, less vivid dreams/nightmares than propranolol); no ISA, no membrane stabilization; half-life 6-9h",
        "Hypertension, angina, post-MI (↓mortality), rate control in AF/flutter; migraine prophylaxis (off-label); essential tremor; anxiety (situational)",
        "Bradycardia, AV block, fatigue, cold extremities; ↑triglycerides, ↓HDL; less bronchospasm than non-selective BBs (but still avoid in severe asthma); worsens Raynaud's; rebound HTN if abruptly stopped; ↓hypoglycemia awareness in diabetics",
        "Renal clearance: ↓dose in CKD (eGFR <35). Less lipophilic than metoprolol/propranolol → less CNS effects (fewer nightmares, depression, sexual dysfunction — questionable evidence). Hydrophilicity: atenolol > bisoprolol > metoprolol > propranolol (lipophilic). LIFE and ASCOT: atenolol-based therapy was inferior to losartan- or amlodipine-based therapy for stroke/CV events — not first-line for uncomplicated HTN"
    ),
    "nitroprusside": _dr(
        "Venous + arterial vasodilator; nitric oxide donor → ↑cGMP → smooth muscle relaxation; reduces both preload (venous dilation) and afterload (arterial dilation) → ↓↓ SVR + ↓PCWP; ultrashort half-life (seconds)",
        "Hypertensive emergencies (most potent); acute HF with very high SVR (not hypotensive shock); severe HF with high filling pressures; aortic dissection (with esmolol/BB); flash pulmonary edema",
        "CYANIDE TOXICITY (thiocyanate accumulation — hepatic conversion of CN to thiocyanate, renal elimination — risk with high doses/prolonged use/renal failure): metabolic acidosis + lactic acidosis + altered mental status + skin color change; hypotension; reflex tachycardia (sympathetic activation); ↑ICP; 'coronary steal' in MI; thiocyanate toxicity (hypothyroidism, ataxia, psychosis)",
        "Must be wrapped in foil (light-sensitive). Cyanide toxicity prevention: limit dose (<2 mcg/kg/min) and duration (<48-72h), add sodium thiosulfate or hydroxocobalamin (binds CN); avoid in renal failure. Monitor: lactic acidosis (early sign of CN toxicity), thiocyanate levels (>100 mcg/mL = toxic). Preferred in aortic dissection: BB first → reduce dP/dt → then nitroprusside (prevents reflex tachycardia)"
    ),
    "candesartan": _dr(
        "Angiotensin II receptor blocker (ARB); selectively blocks AT1 receptor → ↓vasoconstriction + ↓aldosterone release + ↓sympathetic activity; no ACE inhibition → no bradykinin accumulation → no cough or angioedema (minimal risk vs ACEi)",
        "Hypertension, heart failure (reduced EF — CHARM trial: ↓hospitalizations + mortality); chronic kidney disease with proteinuria; diabetic nephropathy; alternative to ACEi in ACEi-intolerant patients (cough/angioedema)",
        "Hyperkalemia, hypotension, renal insufficiency (AKI in renal artery stenosis — similar to ACEi), angioedema (rare, lower risk than ACEi); teratogenicity (contraindicated in pregnancy)",
        "CHARM trial: candesartan ↓CV death/HF hospitalizations in HFrEF patients not tolerating ACEi. ARBs vs ACEi: similar efficacy, ↓cough, ↓angioedema risk (but angioedema still possible, can cross-react). ONTARGET: ACEi + ARB combination → ↑adverse effects without additional benefit — avoid combination. Sacubitril/valsartan (ARNi) superior to ACEi in HFrEF — transition point"
    ),
    # ── Diabetes ─────────────────────────────────────────────────────────────
    "glimepiride": _dr(
        "Sulfonylurea (3rd generation); closes ATP-sensitive K+ channels on pancreatic β cells → membrane depolarization → Ca2+ influx → insulin secretion; insulin secretagogue — mechanism independent of blood glucose level",
        "Type 2 diabetes mellitus (monotherapy or combination); preferred sulfonylurea for elderly (less hypoglycemia than glyburide); once-daily dosing",
        "HYPOGLYCEMIA (principal adverse effect — can be prolonged and severe; risk ↑with missed meals, alcohol, renal impairment); weight gain (3-5 lbs); rare: hemolytic anemia in G6PD deficiency",
        "Compared to glyburide: less hypoglycemia (no long-acting active metabolites) → preferred in elderly. Compared to glipizide: both acceptable; glimepiride is once daily (glipizide IR often BID, XL once daily). Avoid in renal impairment (eGFR <30) — ↑risk hypoglycemia. Sulfonylureas fell out of favor due to hypoglycemia risk and weight gain vs newer agents (GLP-1, SGLT2i) — however remain widely used, inexpensive, generic"
    ),
    "canagliflozin": _dr(
        "SGLT2 inhibitor (sodium-glucose cotransporter-2 inhibitor); blocks glucose + sodium reabsorption in proximal tubule → glucosuria + natriuresis → ↓blood glucose + ↓BP + ↓weight; also SGLT1 inhibition in gut (↓GI glucose absorption)",
        "Type 2 diabetes; established CV disease (CANVAS trial: ↓MACE); ↓HF hospitalization (CANVAS); diabetic kidney disease (CREDENCE: ↓ESKD and renal progression)",
        "Genital mycotic infections (most common — candidal vulvovaginitis, balanitis), UTI, DKA (euglycemic DKA — normal glucose, don't miss); ↓bone density + ↑fracture risk (unique to canagliflozin vs other SGLT2i); amputations (CANVAS: ↑lower limb amputation risk — below-knee; boxed warning removed 2020 — monitor feet); hypotension, volume depletion, hyperkalemia",
        "Unique risks vs other SGLT2i: ↑amputation risk (below-knee) and ↑fracture risk — not clearly seen with empagliflozin/dapagliflozin. Euglycemic DKA: glucose often 200-250 (not markedly elevated) but anion gap metabolic acidosis — hold SGLT2i before procedures/fasting. Do not start if eGFR <30, but it can be continued until dialysis for kidney protection (little glucose lowering at low eGFR). CREDENCE: first trial showing renal protection in DM + CKD"
    ),
    "dulaglutide": _dr(
        "GLP-1 receptor agonist (long-acting, once-weekly SC injection); mimics glucagon-like peptide-1 → ↑glucose-dependent insulin secretion, ↓glucagon, ↓gastric emptying, ↑satiety; Fc fusion protein (extends half-life to 5 days)",
        "Type 2 diabetes (AWARD trials); CV risk reduction in established CVD or high risk (REWIND trial — ↓MACE regardless of prior CVD — broadest CV benefit data); weight loss; HbA1c reduction",
        "GI (nausea, vomiting, diarrhea — dose-limiting, especially on initiation — improve over time), injection site reactions; tachycardia; hypoglycemia (rare when monotherapy); pancreatitis (rare); thyroid C-cell tumors (rodent data — FDA black box; contraindicated in MEN2/medullary thyroid cancer history)",
        "REWIND: ↓MACE in T2DM with high CV risk regardless of established CVD — broader indication than semaglutide (SUSTAIN-6)/liraglutide (LEADER) which required established CVD. Once-weekly auto-injector (Trulicity) — convenient. GI side effects: start low dose, titrate after 4 weeks, take with largest meal, avoid high-fat meals initially. Modest weight loss (~2-4 kg — less than semaglutide/tirzepatide)"
    ),
    # ── Anxiolytics / Benzodiazepines ────────────────────────────────────────
    "alprazolam": _dr(
        "Benzodiazepine; positive allosteric modulator of GABA-A receptor → ↑frequency of Cl⁻ channel opening → CNS depression; rapid onset (30–60 min), intermediate duration (t½ 6–27h)",
        "Panic disorder (high-potency BZD — SSRIs/CBT are first-line; BZDs short-term), generalized anxiety disorder (short-term), agoraphobia; short-term relief of acute anxiety and anxiety associated with depression",
        "Sedation, cognitive impairment, anterograde amnesia, psychomotor slowing, ataxia; respiratory depression (additive with opioids/alcohol — DANGEROUS); physical dependence and withdrawal (rebound anxiety, insomnia, seizures — taper slowly); abuse potential (Schedule IV); paradoxical agitation (rare)",
        "High-potency BZD — preferred for panic disorder over diazepam (lower potency). Abrupt discontinuation after prolonged use → severe withdrawal seizures (life-threatening) — taper over weeks to months; equivalent diazepam dose used for structured taper. Avoid in elderly (Beers criteria — ↑fall risk, delirium). Avoid with opioids (Black Box Warning: respiratory depression/death). Short-acting BZDs (alprazolam, lorazepam) have higher abuse potential than long-acting (diazepam, clonazepam)."
    ),
    "clonazepam": _dr(
        "Benzodiazepine; positive allosteric modulator of GABA-A receptor → ↑frequency of Cl⁻ channel opening → CNS depression; long-acting (t½ 20–50h), slow onset relative to alprazolam",
        "Panic disorder (longer duration → fewer interdose rebound symptoms than alprazolam), generalized anxiety disorder; seizure disorders (absence seizures, Lennox-Gastaut, myoclonic, akinetic); akathisia (antipsychotic-induced); restless legs syndrome; essential tremor",
        "Sedation, cognitive impairment, ataxia, anterograde amnesia; respiratory depression (additive with CNS depressants/opioids); tolerance and physical dependence (slower to develop than short-acting BZDs due to longer t½); withdrawal: anxiety, insomnia, tremor, seizures; paradoxical agitation/aggression",
        "Longer t½ than alprazolam → smoother blood levels, fewer rebound symptoms — preferred for maintenance anxiety treatment if BZD required. Lower abuse potential than short-acting BZDs. Anti-seizure: preferred for myoclonic + atonic seizures; adjunct in Lennox-Gastaut. Taper slowly to prevent seizure-withdrawal (reduce dose 5–10% per week). Beers criteria: avoid in elderly. Unlike alprazolam, long half-life means missed doses less critical — but also slower offset if toxicity occurs."
    ),
    # ── ADHD / CNS Stimulants ────────────────────────────────────────────────
    "amphetamine": _dr(
        "Mixed amphetamine salts (75% d-amphetamine, 25% l-amphetamine); reverses monoamine transporter function → effluxes dopamine + norepinephrine (and serotonin) from presynaptic terminals; also inhibits MAO; net effect: ↑synaptic DA + NE in prefrontal cortex → ↑executive function",
        "ADHD (children ≥3y and adults — Schedule II); narcolepsy; short-term obesity treatment (rarely used)",
        "Decreased appetite, weight loss, insomnia, tachycardia, hypertension, headache; growth suppression in children (drug holidays considered); tics (may worsen in predisposed); anxiety/irritability; abuse/dependence potential (Schedule II); cardiovascular events at high doses (MI, stroke — rare); psychosis at high doses or in predisposed",
        "Adderall = d,l-amphetamine mixed salts; Adderall XR = extended-release. DA efflux mechanism differs from methylphenidate (reuptake inhibitor) — hence different abuse profile. Cardiovascular screening: EKG not routinely required but assess for structural heart disease. ADHD treatment: start low, titrate; if inadequate response/side effects → switch formulation or drug class. Drug holidays: summer breaks in children to assess continued need and allow catch-up growth. Abuse potential: highest of all ADHD agents — diversion concern in adolescents."
    ),
    "lisdexamfetamine": _dr(
        "Prodrug of d-amphetamine; cleaved by red blood cell hydrolases (rate-limiting step) after absorption → releases active d-amphetamine; slower conversion → prolonged, smooth effect; mechanism same as amphetamine (DA/NE efflux)",
        "ADHD (children ≥6y and adults — first ADHD agent FDA-approved for binge eating disorder [BED]); moderate-to-severe binge eating disorder in adults",
        "Same class effects as amphetamine: decreased appetite, insomnia, dry mouth, headache, increased HR/BP; growth suppression in children; cardiovascular risk; psychiatric symptoms; potential for abuse (Schedule II — though lower due to prodrug mechanism: oral prodrug converts slowly vs insufflation/injection has less abuse potential)",
        "Vyvanse = lisdexamfetamine. Prodrug design: once-daily dosing (12–14h coverage); abuse-deterrent by design (lysine conjugation prevents rapid effect if injected/insufflated — lysis only occurs in RBCs). Approved for BED in adults: reduces binge days/week. Among the longest-acting amphetamine formulations. Cardiovascular: baseline HR/BP, reassess periodically. Compare to Adderall XR: both effective for ADHD; Vyvanse smoother curve, lower abuse potential."
    ),
    "armodafinil": _dr(
        "R-enantiomer of modafinil; exact mechanism unclear — inhibits dopamine reuptake (DAT); may also involve NE, histamine, orexin pathways; similar t½ to modafinil (~15h) but higher plasma levels later in the day → sustained wakefulness throughout day; low abuse potential (Schedule IV)",
        "Narcolepsy; shift work sleep disorder; obstructive sleep apnea (adjunct to CPAP for residual sleepiness); off-label: fatigue in cancer/MS, depression adjunct",
        "Headache (most common), nausea, dizziness, dry mouth, insomnia; severe skin reactions (Stevens-Johnson syndrome — rare; label warning); hypersensitivity reactions; psychiatric symptoms (anxiety, agitation, hallucinations — rare); contraindicated in hypersensitivity to modafinil/armodafinil; CYP3A4 inducer → reduces OCP efficacy (use backup contraception)",
        "Nuvigil = armodafinil; Provigil = modafinil (racemic mix). R-enantiomer: once-daily dosing achieves more sustained plasma levels vs modafinil (take in morning). Not a substitute for sleep — does not address sleep debt. Lower abuse potential than amphetamines (Schedule IV vs II). CYP interactions: induces CYP3A4 (↓hormonal contraceptives, cyclosporine) and inhibits CYP2C19 (↑omeprazole, diazepam levels). Reassess every 6 months."
    ),
    "atomoxetine": _dr(
        "Selective norepinephrine reuptake inhibitor (SNRI — pure NRI, not serotonergic); blocks NE transporter (NET) → ↑synaptic NE in prefrontal cortex; no direct dopamine transporter activity; not a stimulant → NOT a controlled substance",
        "ADHD in children ≥6y, adolescents, and adults (non-stimulant first-line option — preferred when: stimulant intolerance, comorbid anxiety/tics, history of substance abuse, or parental preference for non-controlled medication); off-label: anxiety, enuresis",
        "Decreased appetite, nausea/vomiting (common initially), insomnia or somnolence, dry mouth, constipation, urinary hesitancy/retention; modest increase in HR + BP (less than stimulants); sexual dysfunction in adults; RARE: suicidal ideation (Black Box Warning in pediatric patients — monitor closely first 4 weeks); hepatotoxicity (rare, stop if jaundice/dark urine); priapism (very rare)",
        "Strattera = atomoxetine. Key advantage: not a controlled substance — no abuse potential, no DEA prescribing restrictions, easier refills. Delayed onset: 2–6 weeks for full effect (unlike stimulants: hours). CYP2D6 metabolized: poor metabolizers (10% of population) → 5× higher plasma levels → ↑adverse effects; strong CYP2D6 inhibitors (fluoxetine, paroxetine) raise atomoxetine levels. 24h coverage without drug holidays — beneficial for continuous symptom control. Black Box Warning: suicidal ideation — counsel families; do NOT use in bipolar without mood stabilizer."
    ),
    # ── Antihistamines ───────────────────────────────────────────────────────
    "cetirizine": _dr(
        "Second-generation H1 antihistamine; selective peripheral H1 receptor antagonist; metabolite of hydroxyzine; low CNS penetration due to P-glycoprotein efflux and zwitterionic character → minimal sedation; does not cross blood-brain barrier significantly",
        "Allergic rhinitis (seasonal + perennial); chronic urticaria; allergic conjunctivitis; pruritus; angioedema (mild); food allergy symptom relief (adjunct)",
        "Low-grade sedation (more sedating than loratadine/fexofenadine — ~10–15% of patients report drowsiness), dry mouth, headache, fatigue; minimal anticholinergic effects; generally well tolerated; dose-reduce in renal impairment (renally excreted — eGFR <30 halve dose)",
        "Zyrtec = cetirizine; active metabolite levocetirizine (Xyzal) — slightly less sedating. Compared to 1st gen (diphenhydramine, hydroxyzine): minimal CNS depression, no anticholinergic effects. Compared to loratadine: faster onset (1h vs 1–3h), slightly more effective for urticaria, slightly more sedating. Compared to fexofenadine: more sedating but equal efficacy. Renal dosing: eGFR <11 avoid or halve dose. Effective for chronic idiopathic urticaria — may require higher doses (up to 4× standard). Onset 1 hour, once daily, duration 24h."
    ),
    "loratadine": _dr(
        "Second-generation H1 antihistamine; selective peripheral H1 receptor antagonist; P-glycoprotein substrate → does not cross blood-brain barrier → non-sedating at standard doses; hepatic metabolism to active metabolite desloratadine",
        "Allergic rhinitis (seasonal + perennial); chronic urticaria; allergic skin conditions; OTC allergy relief (non-sedating — safe for daytime use in pilots, operators of heavy machinery)",
        "Headache, dry mouth, somnolence at high doses (non-sedating at standard 10 mg); generally excellent tolerability; minimal anticholinergic effects; rare: hepatotoxicity (very rare); QTc prolongation at very high doses (negligible at therapeutic doses)",
        "Claritin = loratadine; Clarinex = desloratadine (active metabolite, slightly more potent). Non-sedating: FAA-approved for pilots at standard dosing. Metabolized by CYP3A4 and CYP2D6 → interactions with inhibitors raise plasma levels (ketoconazole, erythromycin) — but clinical significance low. Hepatic impairment: dose every other day. Compare to fexofenadine: both non-sedating, both effective; fexofenadine better studied for robust non-sedation. Desloratadine (Clarinex): active metabolite, some evidence of potency advantage. Once daily, onset 1–3 hours, 24h duration."
    ),
    "diphenhydramine": _dr(
        "First-generation H1 antihistamine; also blocks muscarinic (anticholinergic), alpha-adrenergic, and serotonin receptors; highly lipophilic → penetrates CNS readily → significant sedation; blocks H1 receptors and has sodium channel blocking activity",
        "Allergic reactions (urticaria, angioedema, anaphylaxis adjunct — IV); motion sickness; nausea/vomiting; insomnia (OTC sleep aid); parkinsonism/EPS (drug-induced); cough suppression; pruritus; mild dystonic reactions",
        "Sedation (profound — CNS depression), anticholinergic effects (dry mouth, urinary retention, constipation, blurred vision, tachycardia, confusion — esp. elderly), paradoxical excitation (children + elderly), cognitive impairment; overdose: anticholinergic toxidrome (hot as hare, dry as bone, red as beet, mad as hatter, blind as bat); chronic use → dementia risk (Beers criteria); QTc prolongation at high doses",
        "Benadryl = diphenhydramine. AVOID in elderly (Beers criteria: ↑delirium, falls, cognitive impairment, urinary retention). For anaphylaxis: adjunct only — epinephrine is first-line (diphenhydramine does NOT reverse anaphylaxis quickly enough to prevent cardiovascular collapse). Drug-induced EPS/acute dystonia: IV/IM diphenhydramine 25–50 mg → rapid relief. Half-life ~4–9h; 25–50 mg PO/IV/IM. Tolerance to sedation develops (not to antihistamine effect). Anticholinergic toxidrome reversal: physostigmine (cholinesterase inhibitor) — use only if life-threatening."
    ),
    # ── Laxatives / GI ──────────────────────────────────────────────────────
    "bisacodyl": _dr(
        "Stimulant laxative; direct action on colonic mucosa → stimulates enteric nervous system → increases peristalsis; also inhibits electrolyte/water absorption in the colon → net luminal water accumulation; onset: oral 6–12h, rectal (suppository) 15–60 min",
        "Constipation (short-term); bowel preparation (colonoscopy — used with PEG or alone for low-volume prep); opioid-induced constipation (stimulant laxative class preferred); post-surgical ileus prevention",
        "Abdominal cramping (common), hypokalemia with prolonged/excessive use, fluid and electrolyte imbalance, melanosis coli (brown-black discoloration of colonic mucosa — benign, reversible, from prolonged use); cathartic colon (chronic abuse — atonic colon); do not crush enteric-coated tablets; suppository may cause rectal irritation",
        "Dulcolax = bisacodyl. Mechanism distinguishes stimulant laxatives (bisacodyl, senna) from osmotic (lactulose, PEG, magnesium salts) from stool softeners (docusate) from lubricants (mineral oil). Preferred for opioid-induced constipation (stimulant works despite gut dysmotility from opioids; osmotic agents less effective alone). Enteric-coated tablets: do not take within 1h of antacids/milk (coating dissolves → gastric irritation). Rectal route fastest. Not recommended for long-term use (melanosis coli, dependency). Bowel prep: 4 bisacodyl 5-mg tablets + magnesium citrate or split-dose PEG."
    ),
    "docusate": _dr(
        "Stool softener (emollient/surfactant laxative); anionic surfactant → lowers surface tension of stool → allows water and fat penetration into stool → softening without stimulation of peristalsis; weak laxative effect; onset 12–72h",
        "Prevention of constipation (especially postoperative, post-MI — minimize straining); softening hard stools in patients who should avoid straining (anorectal surgery, hemorrhoids, cardiac/vascular conditions); routine constipation prophylaxis in hospitalized patients on opioids or bed rest",
        "Generally very well tolerated; mild abdominal cramping; diarrhea with excessive use; theoretical concern: enhances absorption of other drugs (surfactant effect — clinically minimal); rectal form may cause rectal irritation",
        "Colace = docusate sodium; also available as docusate calcium. Weakest laxative class — used for prevention, not treatment of constipation. Often combined with stimulant laxative (Peri-Colace = docusate + senna). Controversial efficacy evidence — some studies show minimal benefit over placebo for treatment of established constipation. For opioid-induced constipation: stimulant laxatives (senna, bisacodyl) preferred over docusate alone. Post-MI straining avoidance: docusate + senna. Standard hospital constipation prophylaxis: senna ± docusate rather than docusate alone."
    ),
    "polyethylene glycol": _dr(
        "Osmotic laxative (isosmotic polyethylene glycol 3350); non-absorbable, non-metabolized polymer → retains water in colon by osmosis → softens stool, increases stool volume, stimulates colonic peristalsis; does not disturb electrolyte balance (isosmotic — no electrolyte shift unlike lactulose/magnesium)",
        "Occasional constipation (OTC: MiraLax 17g daily); chronic constipation (long-term safe); fecal disimpaction; bowel preparation for colonoscopy (high-volume PEG 4L — GoLYTELY/CoLyte; low-volume PEG 2L — MoviPrep; non-PEG low-volume preps: SUPREP (sulfate), Prepopik (picosulfate)); constipation in children",
        "Bloating, flatulence, cramping, nausea (especially with colonoscopy prep volumes); diarrhea with excessive doses; rare electrolyte disturbances at high volumes (PEG 3350 standard dose — no significant electrolyte issues); well tolerated for long-term use",
        "MiraLax = PEG 3350 (OTC). GoLYTELY/NuLYTELY/CoLyte = PEG + electrolytes (4L for colonoscopy prep — gold standard). Low-volume preps (MoviPrep 2L, SUPREP, Prepopik) equally efficacious with better compliance. Advantages over lactulose: no fermentation, no gas/flatulence, no electrolyte disturbance, palatable. No dependency, safe for long-term use. Children: FDA-approved for short-term constipation but commonly used long-term for functional constipation (AGA supports prolonged use). Onset: 12–72h for standard dosing. Fecal disimpaction: 1–1.5g/kg/day × 3–6 days."
    ),
    # ── ACE Inhibitors ───────────────────────────────────────────────────────
    "enalapril": _dr(
        "ACE inhibitor (prodrug — enalaprilat is active form after hepatic de-esterification); inhibits angiotensin-converting enzyme → ↓angiotensin II → vasodilation + ↓aldosterone → ↓BP + ↓sodium retention; ↑bradykinin (kinin accumulation → ACEi cough); also available as IV enalaprilat for hypertensive urgency",
        "Hypertension; heart failure with reduced EF (HFrEF — reduces mortality, CONSENSUS trial — 40% mortality reduction in severe HF); post-MI LV dysfunction (SOLVD trial); diabetic nephropathy; CKD with proteinuria; prevention of LV remodeling post-MI",
        "Dry cough (10–15% — bradykinin accumulation → switch to ARB), angioedema (rare, life-threatening — ↑risk in Black patients, hereditary angioedema patients, patients on DPP-4 inhibitors or mTOR inhibitors), hyperkalemia, hypotension (first dose — especially volume-depleted), acute kidney injury (bilateral renal artery stenosis — GFR depends on angiotensin II efferent tone), teratogenicity (contraindicated in pregnancy)",
        "CONSENSUS trial: enalapril ↓mortality 40% in severe HFrEF. SOLVD trial: enalapril ↓mortality + HF hospitalizations in HFrEF. ACEi vs ARB: ACEi has more side effects (cough, angioedema) but more outcome data; ARBs equally effective, fewer side effects — use ARB if ACEi intolerant. ACEi + ARB combination: ONTARGET showed no benefit + ↑adverse effects — avoid combination. Transition to sacubitril/valsartan (ARNi) in stable HFrEF improves outcomes vs ACEi alone (PARADIGM-HF). Monitor K+/Cr 1–2 weeks after initiation or dose change. Rise in Cr <30% acceptable — beyond that, investigate renal artery stenosis."
    ),
    # ── ARBs ────────────────────────────────────────────────────────────────
    "valsartan": _dr(
        "Angiotensin II receptor blocker (ARB); selectively blocks AT1 receptor → ↓vasoconstriction, ↓aldosterone release, ↓sympathetic tone; no ACE inhibition → no bradykinin accumulation → no cough (or angioedema risk negligible); also component of sacubitril/valsartan (Entresto) — ARNi",
        "Hypertension; HFrEF (Val-HeFT: ↓hospitalizations; VALHEFT in ACEi-intolerant patients); post-MI LV dysfunction with HF or LVH (VALIANT trial — equivalent to captopril post-MI); diabetic nephropathy; alternative to ACEi in intolerant patients",
        "Hyperkalemia, hypotension, renal insufficiency (AKI in bilateral renal artery stenosis), angioedema (rare — but lower risk than ACEi); teratogenicity (contraindicated in pregnancy); no cough (key advantage over ACEi)",
        "Diovan = valsartan (single agent); Entresto = sacubitril/valsartan (ARNi — PARADIGM-HF: superior to enalapril in HFrEF — ↓CV death + HF hospitalizations 20%). VALIANT: valsartan non-inferior to captopril post-MI with LV dysfunction. Val-HeFT: valsartan added to ACEi — no additional mortality benefit (avoid ACEi + ARB combination per ONTARGET). Washout period: if transitioning from ACEi to Entresto, 36h washout required (prevent angioedema risk — both raise bradykinin). ARBs similar efficacy to ACEi for hypertension, HF, proteinuria — preferred when ACEi causes cough."
    ),
    "irbesartan": _dr(
        "Angiotensin II receptor blocker (ARB); selective AT1 receptor antagonist → ↓vasoconstriction + ↓aldosterone; no ACEi-associated cough; moderate potency ARB; primarily hepatic elimination (no dose adjust for renal impairment unlike some ARBs)",
        "Hypertension; diabetic nephropathy in type 2 diabetes with hypertension + microalbuminuria or overt nephropathy (IDNT trial — slowed CKD progression vs amlodipine or placebo); alternative to ACEi in cough/angioedema-intolerant patients",
        "Hyperkalemia, hypotension, renal impairment; angioedema (rare, lower than ACEi); teratogenicity (contraindicated in pregnancy); no dose adjustment needed in renal impairment (hepatic elimination — advantage over renally-cleared ARBs)",
        "Avapro = irbesartan. IDNT trial (irbesartan diabetic nephropathy trial): irbesartan reduced doubling of serum creatinine and ESRD vs amlodipine and placebo in T2DM + nephropathy; BP-independent renoprotective effect. IRMA-2: irbesartan ↓progression to overt proteinuria in T2DM with microalbuminuria. Hepatic metabolism (CYP2C9): no dose reduction in CKD (unlike ARBs with renal excretion). ONTARGET: ARB equivalent to ACEi for CV outcomes in high-risk patients. No-cough advantage — key differentiator from the ACEi class."
    ),
    "olmesartan": _dr(
        "Angiotensin II receptor blocker (ARB); selective AT1 receptor antagonist → ↓vasoconstriction + ↓aldosterone release; long t½ (13h) → once-daily dosing; potent ARB; primarily biliary/fecal excretion (~40% renal — no dose adjustment required in renal impairment)",
        "Hypertension (monotherapy or combination); CKD with proteinuria; alternative to ACEi for hypertension in patients with ACEi intolerance; combination products available (Benicar HCT — olmesartan + HCTZ; Azor — olmesartan + amlodipine; Tribenzor — triple combination)",
        "Hyperkalemia, hypotension, renal insufficiency; angioedema (rare, lower than ACEi); sprue-like enteropathy (RARE but important: severe chronic diarrhea, weight loss, villous atrophy — mimics celiac disease — FDA label warning 2013 — occurs months to years after starting; resolves on discontinuation); teratogenicity (contraindicated in pregnancy)",
        "Benicar = olmesartan. Unique adverse effect: olmesartan-induced enteropathy — sprue-like with villous atrophy on biopsy, celiac antibodies NEGATIVE, resolves when olmesartan stopped (FDA warning 2013). Consider in any patient on olmesartan presenting with chronic diarrhea + weight loss. ARB class: no outcome superiority over ACEi (ONTARGET); avoid ACEi + ARB combination. Potent ARB — ROADMAP trial: delayed onset of microalbuminuria in T2DM. Combination Azor (olmesartan + amlodipine): synergistic BP reduction."
    ),
    "telmisartan": _dr(
        "Angiotensin II receptor blocker (ARB); selective AT1 receptor antagonist; also partial PPARγ agonist (insulin-sensitizing effect — potential metabolic benefit); longest t½ of ARBs (~24h) → smooth 24h coverage; exclusively biliary/fecal excretion (no dose adjustment in renal impairment even with dialysis)",
        "Hypertension; CV risk reduction in high-risk patients who cannot tolerate ACEi (ONTARGET: non-inferior to ramipril for CV outcomes with fewer side effects; TRANSCEND: ↓CV events vs placebo in ACEi-intolerant patients); CKD with proteinuria; metabolic syndrome (off-label — PPARγ partial agonism may improve insulin sensitivity)",
        "Hyperkalemia, hypotension, renal insufficiency; angioedema (rare); teratogenicity (contraindicated in pregnancy); no dose adjustment in renal impairment or ESRD (biliary excretion — unique among ARBs); elevates LFTs (rare hepatotoxicity — monitor)",
        "Micardis = telmisartan. Longest t½ of ARBs (24h) → most consistent 24h BP control — particularly good for morning BP surge (peak cardiovascular event risk). Unique PPARγ partial agonism → metabolic benefits: ↑insulin sensitivity, ↑HDL, ↓triglycerides — potential advantage in metabolic syndrome. Exclusively fecal excretion — safe in any degree of renal failure without dose adjustment. ONTARGET: telmisartan non-inferior to ramipril (ACEi) for CV outcomes in high-risk patients. TRANSCEND: telmisartan ↓CV events in ACEi-intolerant high-risk patients."
    ),
    # ── Beta-Blockers ────────────────────────────────────────────────────────
    "nebivolol": _dr(
        "Highly selective β1 adrenergic receptor blocker (most β1-selective of all beta-blockers at low doses); also stimulates β3 receptors → eNOS activation → ↑nitric oxide (NO) production → vasodilation (unique mechanism among beta-blockers); at high doses loses β1 selectivity",
        "Hypertension; heart failure with reduced EF (adjunct — class evidence supports all evidence-based beta-blockers [carvedilol, metoprolol succinate, bisoprolol] but nebivolol included in some HF guidelines for elderly — SENIORS trial); angina (off-label)",
        "Bradycardia, hypotension, fatigue, dizziness; less bronchospasm than non-selective (high β1 selectivity); sexual dysfunction; peripheral vasoconstriction (less than non-selective due to NO release); exercise intolerance; masking of hypoglycemia (less than propranolol); cold extremities (mild — counteracted by vasodilation)",
        "Bystolic = nebivolol. Dual mechanism: β1 blockade + NO-mediated vasodilation → unique hemodynamic profile; potentially better tolerability (less fatigue, erectile dysfunction) than other beta-blockers. SENIORS trial: nebivolol ↓composite of death/CV hospitalization in elderly HF patients (>70y) — broad EF inclusion (EF >35% included). Most β1-selective at doses ≤10 mg/day — selectivity is lost at higher doses and in CYP2D6 poor metabolizers. Vasodilatory beta-blocker: similar to carvedilol but via NO (carvedilol = α1 + β1/β2 blockade)."
    ),
    # ── PPIs ─────────────────────────────────────────────────────────────────
    "esomeprazole": _dr(
        "S-enantiomer of omeprazole; proton pump inhibitor (PPI); prodrug activated by acidic environment of parietal cell canaliculus → active sulfenamide binds irreversibly to H+/K+-ATPase (proton pump) → profound acid suppression; higher bioavailability than omeprazole → more consistent acid suppression",
        "GERD (erosive esophagitis — healing + maintenance); Zollinger-Ellison syndrome; H. pylori eradication (combination regimen); peptic ulcer disease (PUD) treatment + prevention (NSAID-induced); stress ulcer prophylaxis (ICU); Barrett's esophagus surveillance adjunct; upper GI bleed (IV high-dose infusion post-endoscopy)",
        "Generally well tolerated short-term; long-term: hypomagnesemia (↓Mg2+ absorption — monitor with prolonged use), vitamin B12 deficiency, iron deficiency, osteoporosis/fractures, Clostridioides difficile infection (↑risk — alkaline gut pH promotes spore germination), community-acquired pneumonia (↑risk, small), interstitial nephritis (rare); CYP2C19 metabolism — drug interactions (clopidogrel — ↓activation; atazanavir — ↓levels)",
        "Nexium = esomeprazole. S-isomer of omeprazole (Prilosec) — modest clinical advantage (more consistent acid suppression across CYP2C19 metabolizer phenotypes). PPIs preferred over H2 blockers for erosive esophagitis. IV esomeprazole post-endoscopy for high-risk peptic ulcer bleed: 80 mg bolus → 8 mg/h infusion × 72h → ↓rebleeding + surgery. De-prescribing: reassess indication; wean/stop when no longer needed. Rebound acid hypersecretion: taper rather than abruptly stopping after prolonged use. Clopidogrel interaction: esomeprazole (and omeprazole) inhibit CYP2C19 → ↓clopidogrel activation — use pantoprazole or rabeprazole instead."
    ),
    # ── Inhaled Corticosteroids / Pulmonary ──────────────────────────────────
    "budesonide": _dr(
        "Inhaled corticosteroid (ICS) — glucocorticoid receptor agonist; local anti-inflammatory effects in airways; ↓eosinophil infiltration, ↓cytokine release, ↓airway edema, ↓mucus secretion; high first-pass hepatic metabolism → minimal systemic bioavailability when inhaled (reduces systemic adverse effects); also available oral (Entocort/Uceris for IBD)",
        "Asthma (maintenance — controller therapy, Step 2+); COPD (component of ICS/LABA combos — Symbicort/Breztri); croup (nebulized budesonide — alternative to oral dexamethasone for mild-moderate croup); Crohn's disease (oral Entocort — ileal/right-colonic Crohn's in remission induction); ulcerative colitis (Uceris — rectal foam for distal disease)",
        "Local: oral candidiasis (thrush — rinse mouth/gargle after use), dysphonia (hoarseness), pharyngeal irritation; systemic (dose-dependent, high-dose prolonged use): adrenal suppression, growth retardation in children (small, often catch-up), osteoporosis, skin thinning, HPA axis suppression (rare at standard doses); no bronchodilation (use with LABA for COPD/moderate asthma)",
        "Pulmicort = budesonide inhaled (flexhaler, respules for nebulization). Preferred ICS in pregnancy (most safety data). Rinse and spit after use to prevent oral candidiasis + reduce pharyngeal deposition. Pulmicort Respules (nebulized): used in young children (<4y) with recurrent wheezing/asthma. Oral budesonide (Entocort EC): targets ileum/right colon — ↓systemic effects vs prednisone for ileal Crohn's (ECCO guidelines). Croup: nebulized budesonide 2 mg — equivalent to oral dexamethasone, but single IV/oral dexamethasone preferred (cheaper, faster, single dose)."
    ),
    "budesonide-formoterol": _dr(
        "Fixed-dose inhaler combining budesonide (ICS — anti-inflammatory glucocorticoid) + formoterol (long-acting β2 agonist [LABA] — bronchodilator); formoterol: fast onset (2–3 min) + long duration (12h) → unique among LABAs — can be used for both maintenance AND rescue (SMART therapy in asthma)",
        "Asthma (maintenance + SMART rescue therapy — single inhaler maintenance and reliever therapy — reduces exacerbations vs SABA-based rescue; endorsed by GINA and NAEPP 2020 — reliever use is off-label in the US); COPD (Symbicort — maintenance therapy for moderate-severe COPD — reduces exacerbations + improves FEV1)",
        "ICS effects (local): oral candidiasis (rinse mouth after), dysphonia; formoterol/LABA effects: tachycardia, tremor, hypokalemia, headache; LABA monotherapy in asthma ↑asthma-related death (never use LABA without ICS — FDA removed the boxed warning from ICS/LABA combinations in 2017); systemic steroid effects (rare at standard doses); adrenal suppression with high doses",
        "Symbicort = budesonide/formoterol. SMART therapy: formoterol's rapid onset allows same inhaler for maintenance + rescue in asthma — SYGMA trials showed significant reduction in exacerbations vs SABA-based rescue. GINA has preferred ICS-formoterol as the reliever since 2019. COPD: Symbicort reduces exacerbations, improves quality of life. LABA safety: LABA monotherapy in asthma → ↑severe exacerbations/death — always combine with ICS. Compare to fluticasone-salmeterol (Advair): salmeterol slower onset (10–20 min) → NOT suitable for rescue; formoterol faster → suitable. Breztri = budesonide/glycopyrrolate/formoterol (triple therapy for COPD)."
    ),
    "fluticasone-salmeterol": _dr(
        "Fixed-dose inhaler combining fluticasone propionate (ICS — potent glucocorticoid receptor agonist with high topical anti-inflammatory potency) + salmeterol (LABA — long-acting β2 agonist with slow onset [10–20 min], 12h duration); salmeterol is lipophilic → stays in airway lipid bilayer (lipid anchor mechanism) → prolonged receptor activation",
        "Asthma (maintenance — Step 3–5 therapy for uncontrolled asthma on ICS alone; NOT for rescue — salmeterol onset too slow); COPD (Advair 250/50 or 500/50 — reduces exacerbations, improves FEV1 + quality of life)",
        "ICS effects (fluticasone): local oral candidiasis, dysphonia; systemic with high-dose: HPA suppression (fluticasone has lowest systemic bioavailability of ICS — preferred in patients at risk); LABA effects (salmeterol): tachycardia, tremor, hypokalemia; ↑asthma-related death with LABA monotherapy (not seen with ICS combination — boxed warning removed 2017); COPD: ↑pneumonia risk (ICS + LABA in COPD — TORCH trial finding — particularly fluticasone)",
        "Advair = fluticasone/salmeterol (Diskus DPI or HFA MDI). Pivotal TORCH trial (COPD): fluticasone/salmeterol ↓exacerbations + improved quality of life, but ↑pneumonia risk vs salmeterol alone or placebo. Asthma: salmeterol's slow onset (10–20 min) precludes rescue use — always pair with separate SABA (albuterol) for rescue. Fluticasone is most potent ICS by microgram weight, highest topical:systemic ratio. SMART therapy: NOT possible with Advair (salmeterol not fast enough) — use Symbicort instead. FDA removed the boxed warning from ICS/LABA inhalers in 2017 after safety trials (including AUSTRI) showed no ↑serious asthma events. Anoro = umeclidinium/vilanterol (LAMA+LABA) — different from Advair."
    ),
    # ── Anticoagulants ───────────────────────────────────────────────────────
    "rivaroxaban": _dr(
        "Direct oral anticoagulant (DOAC); direct factor Xa inhibitor → ↓thrombin generation → ↓fibrin clot formation; competitive, reversible, dose-dependent inhibition of free + prothrombinase-bound + clot-bound factor Xa; no antithrombin III required (direct inhibition — unlike heparin); predictable pharmacokinetics → no routine monitoring",
        "Nonvalvular atrial fibrillation — stroke/systemic embolism prevention (ROCKET-AF); DVT/PE treatment (once-daily at higher dose after 3 weeks of twice-daily loading); DVT/PE prophylaxis post-surgery (hip/knee replacement); extended secondary VTE prevention (Xarelto 10 mg daily — EINSTEIN CHOICE); stable CAD/PAD risk reduction (2.5 mg BID + aspirin — COMPASS trial); thrombosis prophylaxis in medically ill patients",
        "Bleeding (major risk — GI bleeding risk higher than warfarin/apixaban; intracranial bleed lower than warfarin); no routine monitoring (advantage but no easy dosing adjustment); renal clearance (33% renal — reduce dose in CKD; avoid if CrCl <15–30 depending on indication); drug interactions (P-gp + CYP3A4 substrate — avoid strong dual inhibitors/inducers — azole antifungals, rifampin, carbamazepine); reversal: andexanet alfa (factor Xa decoy — FDA approved); activated charcoal if recent ingestion",
        "Xarelto = rivaroxaban. ROCKET-AF: non-inferior to warfarin for stroke prevention in AF; once-daily dosing (convenience) but BID for VTE treatment initially. GI bleeding: higher than apixaban — ARISTOTLE (apixaban) showed lower GI bleed; prefer apixaban if GI risk high. Reversal: andexanet alfa (Andexxa) — FDA-approved but expensive; 4-factor PCC alternative if unavailable. Take with evening meal (largest meal) — ↑absorption by 39%. Valvular AF exclusion: RE-LY/ROCKET/ARISTOTLE excluded mechanical valves + moderate-severe rheumatic MS → warfarin required in these. CrCl thresholds: AF <15 avoid; VTE treatment <30 avoid."
    ),
    "fondaparinux": _dr(
        "Synthetic pentasaccharide; selective indirect factor Xa inhibitor — binds antithrombin III → 300-fold ↑AT III affinity for factor Xa → inhibits factor Xa only (unlike UFH/LMWH which also inhibit thrombin/IIa); subcutaneous injection; predictable pharmacokinetics (weight-based dosing, no monitoring); renal elimination (t½ 17–21h)",
        "Prophylaxis of DVT/PE post-orthopedic surgery (hip/knee replacement, hip fracture — PENTHIFRA and related trials); acute DVT/PE treatment (MATISSE trials — non-inferior to LMWH/UFH; bridge to warfarin); ACS (OASIS-5/6: unstable angina/NSTEMI — non-inferior to enoxaparin with ↓major bleeding; STEMI — adjunct, do not use alone for PCI due to catheter thrombosis risk)",
        "Bleeding (major bleeding risk); thrombocytopenia (does NOT cause HIT — no platelet factor 4 cross-reactivity → key advantage over heparin/LMWH in HIT patients); renal clearance (avoid in CrCl <30 mL/min — significant accumulation → ↑bleeding); no reversal agent (protamine ineffective — unlike UFH; andexanet alfa has some activity; 4F-PCC/rFVIIa as alternatives); injection site bruising",
        "Arixtra = fondaparinux. DOES NOT CAUSE HIT — preferred anticoagulant when HIT is confirmed or strongly suspected (HIT or HITT — fondaparinux binds AT-III, not PF4 — no cross-reactivity). ACS nuance: preferred over enoxaparin in NSTEMI (OASIS-5: non-inferior efficacy, ↓bleeding); in STEMI/PCI add UFH bolus during catheterization (fondaparinux alone → ↑catheter thrombosis). No monitoring required (predictable, weight-independent after weight-based selection). Only 1 daily SC injection. No reversal: clinical challenge if bleeding — protamine does NOT work. Renal dosing critical: CrCl <30 → use UFH or LMWH instead."
    ),
    "prasugrel": _dr(
        "Thienopyridine prodrug P2Y12 ADP receptor antagonist; irreversibly inhibits P2Y12 receptor on platelets → ↓ADP-mediated platelet aggregation; FASTER + MORE POTENT platelet inhibition than clopidogrel (more complete conversion to active metabolite — single CYP step vs clopidogrel's two-step CYP2C19-dependent conversion); irreversible → effect lasts platelet lifetime (~7–10 days)",
        "Acute coronary syndrome (ACS) managed with PCI — STEMI and NSTEMI/UA undergoing PCI (TRITON-TIMI 38 trial: prasugrel vs clopidogrel — ↓CV death/MI/stroke but ↑bleeding); dual antiplatelet therapy (DAPT) with aspirin; not for medical management without PCI",
        "Bleeding (primary — ↑vs clopidogrel due to more potent platelet inhibition); CONTRAINDICATED in: prior stroke/TIA (↑net harm — intracranial hemorrhage risk exceeds benefit), age ≥75 years (net harm — use only if high-risk DM or prior MI), weight <60 kg (↑bleeding, consider dose reduction); no significant drug interactions via CYP (unlike clopidogrel); discontinue 7 days before elective surgery",
        "Effient = prasugrel. TRITON-TIMI 38: prasugrel vs clopidogrel in ACS + PCI — ↓MI by 24%, ↓stent thrombosis, but ↑life-threatening + fatal bleeding (↑ICH — especially prior stroke/TIA cohort). FDA Black Box: contraindicated in prior stroke/TIA; not recommended ≥75y or <60 kg. Advantages over clopidogrel: more consistent platelet inhibition (no CYP2C19 variability), faster onset, less clopidogrel non-responder issue. Ticagrelor (Brilinta): reversible P2Y12 inhibitor — alternative in ACS (PLATO trial); dyspnea side effect. For stable CAD, clopidogrel remains standard (less bleeding). Duration DAPT: ACS = typically 12 months (shorter if high bleeding risk); high-risk = longer per risk-benefit."
    ),
    # ── Class III Antiarrhythmics ─────────────────────────────────────────────
    "dofetilide": _dr(
        "Class III antiarrhythmic; selectively blocks rapid delayed rectifier potassium current (IKr) → prolongs action potential duration + effective refractory period in atrial tissue → terminates and prevents reentrant arrhythmias; dose-dependent QTc prolongation",
        "Maintenance of normal sinus rhythm in atrial fibrillation and atrial flutter (DIAMOND trials — maintained SR in ~58% at 1 year); chemical cardioversion of AF/AFL to sinus rhythm (effective in 30–70% within 24–36h)",
        "QTc PROLONGATION → TORSADES DE POINTES (TdP) — life-threatening polymorphic VT; renal clearance (dose MUST be adjusted for CrCl — avoid if CrCl <20); contraindicated with drugs that ↑QTc or inhibit renal tubular secretion (cimetidine, verapamil, ketoconazole, trimethoprim — ↑dofetilide levels → ↑TdP risk); baseline QTc >440ms (or >500ms with bundle branch) → contraindicated",
        "Tikosyn = dofetilide. REMS program: Tikosyn prescribing requires special certification (REMS — Risk Evaluation and Mitigation Strategy) — must be initiated in-hospital (minimum 3 days) with continuous cardiac monitoring (ECG QTc monitoring every 2–3h for 3 doses) due to TdP risk. QTc monitoring: if QTc increases >15% or >500ms → reduce dose or discontinue. Drug interactions critical: cimetidine, verapamil, ketoconazole, prochlorperazine, megestrol — contraindicated (↑dofetilide plasma levels). DIAMOND-CHF: dofetilide safe in HF (no ↑mortality unlike class I/IC). Renal dosing: CrCl >60 → 500 mcg BID; 40–60 → 250 mcg BID; 20–40 → 125 mcg BID; <20 → contraindicated."
    ),
    # ── Dopamine Agonists ─────────────────────────────────────────────────────
    "ropinirole": _dr(
        "Non-ergot dopamine agonist; selectively stimulates D2 and D3 receptors in the striatum and limbic system → activates dopaminergic pathways (bypasses degenerating nigrostriatal neurons in Parkinson's); does not require enzymatic conversion to active form (unlike levodopa); crosses blood-brain barrier",
        "Parkinson's disease (early monotherapy — delays motor complications vs levodopa; adjunct to levodopa in advanced disease); restless legs syndrome (RLS) — FDA approved for moderate-to-severe RLS (immediate-release form)",
        "Nausea, vomiting (initiation — ↓with titration and food), somnolence (sudden-onset 'sleep attacks' — warn patients about driving), dizziness/orthostatic hypotension, hallucinations/psychosis (esp. elderly), impulse control disorders (ICDs: pathological gambling, hypersexuality, binge eating, compulsive shopping — up to 17% of patients — dose-dependent), leg edema, dyskinesias (less than levodopa in early PD), augmentation in RLS (paradoxical worsening with dose escalation)",
        "Requip = ropinirole. Sleep attacks: abrupt onset of sleep without warning (even mid-conversation) — must warn all patients, avoid driving until tolerance established. Impulse control disorders (ICDs): important and underrecognized — screen at each visit; dose reduction or switch medication if develops. Augmentation in RLS: symptoms occur earlier in day, spread to arms — most common long-term RLS complication of dopamine agonists — switch to alpha-2-delta ligand (gabapentin, pregabalin) or iron supplementation if ferritin <75. Early PD: dopamine agonists preferred in younger patients (<60y) to delay dyskinesias. Ergot vs non-ergot: ropinirole is non-ergot → no cardiac fibrosis risk (pramipexole also non-ergot; cabergoline = ergot — ↑fibrosis)."
    ),
    # ── Statins ───────────────────────────────────────────────────────────────
    "rosuvastatin": _dr(
        "Synthetic HMG-CoA reductase inhibitor (statin); inhibits rate-limiting step of cholesterol biosynthesis → ↓intrahepatic cholesterol → ↑LDL receptor expression → ↑LDL clearance from plasma; most potent LDL reduction among statins (58–65% LDL reduction at maximum dose); water-soluble (unlike simvastatin/lovastatin — ↓myopathy risk); minimal CYP450 metabolism",
        "Primary hypercholesterolemia and mixed dyslipidemia; ASCVD risk reduction (ACC/AHA guidelines — high-intensity statin: rosuvastatin 20–40 mg); LDL goals in high-risk patients (FH, established ASCVD, DM, CKD); primary prevention in intermediate risk (JUPITER trial — rosuvastatin ↓MACE 44% in normal LDL + elevated hsCRP); slowing progression of atherosclerosis",
        "Myalgia/myopathy (class effect — muscle pain + CK elevation), rhabdomyolysis (rare — <0.1% but more common with high dose or drug interactions), hepatotoxicity (transaminase elevation — class effect, rare clinical hepatitis), new-onset diabetes (class effect — 10–20% ↑risk, more with high-intensity statins), headache, nausea; no CYP3A4 metabolism → FEWER drug interactions than simvastatin/lovastatin/atorvastatin",
        "Crestor = rosuvastatin. Most potent statin — high-intensity: rosuvastatin 20–40 mg or atorvastatin 40–80 mg (ACC/AHA). JUPITER trial: rosuvastatin 20 mg ↓MI, stroke, CV death by 44% in patients with normal LDL (<130) but elevated hsCRP (>2 mg/L) — expanded primary prevention. Not metabolized by CYP3A4 → no interactions with azole antifungals, macrolides, grapefruit — advantage over other statins. Water-soluble → ↓intramuscular penetration → lower myopathy risk. Asian patients: use lower doses (10–20 mg) — higher plasma levels for given dose. Drug interactions: cyclosporine, gemfibrozil (↑rosuvastatin levels via OATP1B1) — dose cap 5–10 mg."
    ),
    # ── Insulins ────────────────────────────────────────────────────────────
    "insulin aspart": _dr(
        "Rapid-acting insulin analog; substitution of proline-28 with aspartic acid in B-chain → ↓self-aggregation → more rapid absorption from SC injection; onset 10–20 min, peak 1–3h, duration 3–5h; binds insulin receptor → promotes glucose uptake (GLUT4 translocation), glycogen synthesis, lipogenesis; ↓hepatic gluconeogenesis, ↓lipolysis",
        "Mealtime insulin (prandial coverage) in type 1 and type 2 diabetes; insulin pumps (continuous SC insulin infusion — CSII); correction boluses for hyperglycemia; intraoperative glucose management; hyperkalemia (insulin-glucose treatment — can use rapid-acting); DKA treatment (IV regular insulin preferred but aspart/lispro can be used SC in mild-moderate DKA)",
        "HYPOGLYCEMIA (primary — onset within 10–20 min of injection, peaks at meal; must eat immediately after injection or at injection time); weight gain; injection site reactions (lipohypertrophy with rotation failure, lipoatrophy); hypokalemia with IV use; hypersensitivity (rare); local allergic reactions",
        "NovoLog (US) / NovoRapid (international) = insulin aspart. Rapid-acting analogs: aspart (NovoLog), lispro (Humalog), glulisine (Apidra) — interchangeable for prandial coverage. Faster than regular insulin: inject 0–15 min before meal (regular requires 30 min pre-meal). Ultra-rapid formulations: faster aspart (Fiasp — onset 2.5 min with nicotinamide addition) for even tighter postprandial control. Pump use: aspart and lispro most commonly used in CSII. Mixing: do NOT mix with glargine (binds, delays/unpredictable absorption). Regular insulin: still preferred for IV drips in ICU/DKA protocol (more studied IV, cost). Fiasp is a faster-acting reformulation, not a biosimilar; biosimilar aspart: Merilog (US, 2025), Trurapi (EU)."
    ),
    # ── Corticosteroids ──────────────────────────────────────────────────────
    "methylprednisolone": _dr(
        "Synthetic glucocorticoid (intermediate-acting); 5× potency of hydrocortisone (anti-inflammatory), minimal mineralocorticoid activity; binds glucocorticoid receptor → ↓phospholipase A2 (via lipocortin) → ↓arachidonic acid → ↓prostaglandins + leukotrienes; ↓NF-κB transcription → ↓pro-inflammatory cytokines; available IV (Solu-Medrol), oral (Medrol dose pack), and IM",
        "Asthma exacerbations (IV/oral Solu-Medrol for acute severe asthma); COPD exacerbations (IV/oral); anaphylaxis (adjunct after epinephrine); organ transplant immunosuppression; multiple sclerosis relapses (high-dose IV 1g/day × 3–5 days — Optic Neuritis Treatment Trial); SCI (historic NASCIS use — AANS/CNS 2013 guidelines recommend against); inflammatory conditions (RA, IBD flares, vasculitis, SLE); giant cell arteritis; dermatomyositis/polymyositis",
        "Short-term: hyperglycemia (all glucocorticoids — monitor blood glucose), hypertension, fluid retention (mild — less mineralocorticoid than hydrocortisone), psychiatric effects (euphoria, psychosis — 'steroid psychosis' especially at high doses), insomnia, increased appetite; long-term: HPA axis suppression, Cushing's syndrome, osteoporosis, avascular necrosis (femoral head — classic), immunosuppression (↑infection risk), myopathy (proximal), skin thinning, adrenal insufficiency on abrupt withdrawal",
        "Medrol = methylprednisolone oral; Solu-Medrol = IV methylprednisolone succinate. Dose pack (4 mg Medrol): 6-day taper (24 mg day 1 → taper to 0) — commonly prescribed for allergic reactions, musculoskeletal conditions. Potency: hydrocortisone 1 → prednisolone 4 → methylprednisolone 5 → dexamethasone 25 (anti-inflammatory). MS relapse: high-dose IV methylprednisolone 1g/day × 3–5 days — speeds recovery, does NOT change long-term disability. Avascular necrosis: cumulative dose + systemic lupus most strongly associated. Adrenal suppression: prednisone ≥20 mg/day (or equivalent) for ≥3 weeks → assume HPA suppression and taper; abrupt discontinuation → adrenal crisis. Surgical stress dosing: stress-dose steroids for adrenal-suppressed patients perioperatively."
    ),
    # ── Antibiotics ──────────────────────────────────────────────────────────
    "amoxicillin-clavulanate": _dr(
        "Combination of amoxicillin (aminopenicillin — acylates penicillin-binding proteins [PBPs] → inhibits peptidoglycan cross-linking → cell wall lysis) + clavulanate (β-lactamase inhibitor — irreversible suicide inhibitor of β-lactamases → protects amoxicillin from enzymatic degradation); extends amoxicillin coverage to β-lactamase-producing organisms",
        "Upper respiratory infections (sinusitis, otitis media, community-acquired pneumonia — β-lactamase producing H. influenzae, M. catarrhalis); skin/soft tissue infections (animal bites — dog/cat — coverage for Pasteurella, Capnocytophaga); diabetic foot infections (mild-moderate); UTI (complicated); intra-abdominal infections (mild); dental/odontogenic infections; prophylaxis for bite wounds",
        "Diarrhea/GI upset (most common — clavulanate-related; amoxicillin-clavulanate has highest GI side effect rate among oral penicillins — take with food); hepatotoxicity (rare — cholestatic hepatitis, usually weeks after completing course — more common with clavulanate component; risk ↑ in elderly + prolonged use); allergy (penicillin allergy — cross-reactivity with cephalosporins ~1–2%); Clostridioides difficile diarrhea (broad-spectrum); rash (ampicillin/amoxicillin class — maculopapular rash in EBV mononucleosis — NOT true allergy)",
        "Augmentin = amoxicillin-clavulanate. Formulations: 875/125 mg BID (standard adult), 500/125 mg TID, XR 2000/125 mg BID (for drug-resistant S. pneumoniae sinusitis). Animal bites: Augmentin is first-line for prophylaxis and empirical treatment (covers Pasteurella multocida, Capnocytophaga canimorsus, oral anaerobes). Do NOT use for sore throat/pharyngitis (Strep A → plain amoxicillin; mononucleosis → ampicillin/amoxicillin class → maculopapular rash common). GI side effects: take with food ↓GI upset; diarrhea from clavulanate-induced gut microbiome disruption. Hepatotoxicity: delayed (1–6 weeks post-course) — cholestatic jaundice, usually self-limited. Penicillin allergy: if mild (rash), cross-reactivity ~1–2% with cephalosporins; if severe (anaphylaxis) — avoid all beta-lactams or skin test."
    ),
    # ── SSRIs ────────────────────────────────────────────────────────────────
    "citalopram": _dr(
        "Selective serotonin reuptake inhibitor (SSRI); most selective SSRI for serotonin transporter (SERT) inhibition with minimal off-target receptor activity (no significant H1, muscarinic, or alpha-1 blockade) → favorable tolerability profile; S-enantiomer (escitalopram) is the active component; hepatic metabolism (CYP2C19, CYP2D6, CYP3A4)",
        "Major depressive disorder (FDA-approved); generalized anxiety disorder; panic disorder (off-label); OCD (off-label); PTSD (off-label); social anxiety disorder (off-label); premenstrual dysphoric disorder (off-label); depression in elderly (often preferred due to clean pharmacology)",
        "GI effects (nausea, diarrhea — common on initiation, improve over 1–2 weeks), sexual dysfunction (delayed orgasm, decreased libido — class effect — affects 30–40%), insomnia or somnolence, headache, dry mouth, sweating; serotonin syndrome (with MAOIs, linezolid, triptans, tramadol — rare but serious); QTc prolongation (dose-dependent — FDA 2012 safety communication: max 40 mg/day in adults, 20 mg/day if >60y or hepatic impairment or CYP2C19 inhibitor use — due to dose-dependent QT prolongation); hyponatremia (SIADH — especially elderly + diuretics); discontinuation syndrome (abrupt stop → 'FINISH' symptoms — flu-like, insomnia, nausea, imbalance, sensory disturbances, hyperarousal — taper gradually); activation syndrome in children/adolescents (agitation, suicidality — Black Box Warning)",
        "Celexa = citalopram; Lexapro = escitalopram (S-enantiomer — more potent, fewer drug interactions, same mechanism). SSRI selection: citalopram/escitalopram favored for minimal drug interactions and clean receptor profile. QTc concern: FDA 2012 limited max dose to 40 mg/day (20 mg for elderly/hepatic impairment) — dose-dependent QTc prolongation unique among SSRIs. Escitalopram generally preferred over citalopram now (same efficacy, half the dose, fewer QTc concerns at therapeutic doses). Black Box Warning: antidepressants increase suicidal thinking/behavior in children, adolescents, young adults — monitor closely first 1–2 months. Full antidepressant effect: 4–6 weeks. Discontinuation: taper over weeks to avoid withdrawal. SIADH: especially in elderly — check Na+ if confusion develops."
    ),
    # ── Electrolyte / GI ─────────────────────────────────────────────────────
    "sodium polystyrene sulfonate": _dr(
        "Cation exchange resin; exchanges sodium ions for potassium ions in the GI tract (primarily large intestine) → binds K+ in colon lumen → excreted in feces; each gram of resin exchanges ~0.5–1 mEq of K+; slow onset (6–24h); available as powder for suspension (oral or retention enema)",
        "Hyperkalemia treatment (chronic hyperkalemia in CKD/ESRD — removes total body potassium; also used for acute hyperkalemia, though onset too slow for emergent membrane stabilization); hyperkalemia in patients on ACEi/ARB/potassium-sparing diuretics; ESRD patients unable to dialyze or between sessions",
        "GI adverse effects: constipation, nausea, vomiting, anorexia; INTESTINAL NECROSIS (serious — rare but life-threatening, especially when given with sorbitol [sorbitol coadministration associated with colonic necrosis] or in postoperative ileus/bowel obstruction); hypokalemia with overuse; hypomagnesemia, hypocalcemia (also exchanges Mg2+, Ca2+); sodium load (each gram provides ~100 mg Na → caution in fluid-overloaded patients, heart failure, hypertension); aspiration risk with oral suspension",
        "Kayexalate = sodium polystyrene sulfonate. Newer agents preferred when available: patiromer (Veltassa — GI exchange resin, better tolerated, no necrosis risk, onset ~7h) and sodium zirconium cyclosilicate (SZC — Lokelma, selective K+ trap, onset 1–2h, very effective, FDA-approved for hyperkalemia). Sorbitol danger: historical formulation mixed SPS with 70% sorbitol (as vehicle) → colonic necrosis reports — FDA recommends avoiding sorbitol with SPS. Onset too slow for emergency use: for acute hyperkalemia with ECG changes → calcium gluconate (immediate) + insulin/glucose + albuterol first, then resin or dialysis for K+ removal. ESRD: dialysis most effective for definitive K+ removal. Despite limitations, SPS widely used due to cost and availability."
    ),
    # ── Phenothiazines / Antiemetics ─────────────────────────────────────────
    "promethazine": _dr(
        "Phenothiazine first-generation H1 antihistamine; also blocks dopamine D2 receptors (antiemetic effect via CTZ + area postrema), muscarinic receptors (anticholinergic), and alpha-1 adrenergic receptors; highly sedating due to broad receptor antagonism; crosses BBB readily",
        "Nausea/vomiting (chemotherapy-induced, postoperative, motion sickness, morning sickness of pregnancy [controversial — pregnancy category C, FDA caution in first trimester]); allergic conditions (urticaria, rhinitis); preoperative sedation; adjunct to opioid analgesia (potentiates); motion sickness prevention; insomnia (sedation)",
        "SEVERE: fatal respiratory depression in children <2 years (BLACK BOX WARNING — CONTRAINDICATED in children <2y; extreme caution 2–12y); IV administration risks: tissue necrosis/gangrene (inadvertent intra-arterial injection) + phlebitis → preferred routes are oral, IM deep, rectal suppository; AVOID IV push; anticholinergic effects (dry mouth, urinary retention, constipation, blurred vision, confusion); EPS/tardive dyskinesia (D2 blockade — phenothiazine class); QTc prolongation; sedation; neuroleptic malignant syndrome (rare); lower seizure threshold",
        "Phenergan = promethazine. BLACK BOX WARNING: contraindicated in children <2y (fatal respiratory depression — dose-dependent CNS depression). IV promethazine controversy: IV use risks severe tissue injury with extravasation or intra-arterial injection → necrosis, gangrene, amputation — Black Box Warning; use only if no alternative, give via running IV, avoid dorsum of hand/wrist (prefer large antecubital vein). IM or PO route preferred. Compared to ondansetron: ondansetron safer (no D2, no anticholinergic, no respiratory depression), preferred in most settings. Promethazine useful in opioid-sparing regimens (potentiates analgesia). Phenothiazine EPS: akathisia, acute dystonia, tardive dyskinesia with chronic use. QTc: additive with other QTc-prolonging agents."
    ),
    # ── OB/GYN drugs ──
    'oxytocin': _dr(
        'Synthetic oxytocin; binds Gq-coupled oxytocin receptors on myometrium (receptor density rises sharply near term) → ↑intracellular Ca2+ → rhythmic uterine contractions; also milk let-down (myoepithelial cells). Structurally similar to ADH',
        'Induction and augmentation of labor (IV infusion, titrated); FIRST-LINE prevention and treatment of postpartum hemorrhage (10 units IM or IV infusion after delivery of the anterior shoulder/placenta — active management of the third stage); after miscarriage or uterine evacuation',
        'Uterine TACHYSYSTOLE (>5 contractions in 10 min averaged over 30 min) → fetal hypoxia/late decelerations; uterine rupture (especially with a scar); WATER INTOXICATION/hyponatremia with prolonged high-dose infusion (ADH-like effect — seizures); hypotension with rapid IV bolus',
        'Tachysystole with an abnormal tracing → STOP oxytocin first, reposition, IV fluid, consider terbutaline. Oxytocin is the uterotonic of choice for PPH because it has no major contraindications.',
    ),
    'methylergonovine': _dr(
        'Ergot alkaloid; partial agonist at α-adrenergic, serotonin (5-HT2A) and dopamine receptors → sustained (tetanic) uterine contraction and vasoconstriction',
        'Postpartum hemorrhage from uterine atony (second-line after oxytocin): 0.2 mg IM every 2–4 h; subinvolution of the uterus',
        'HYPERTENSION (can be severe), coronary vasospasm, nausea/vomiting, headache; serotonin syndrome or ergotism with strong CYP3A4 inhibitors (protease inhibitors, macrolides, azoles)',
        'CONTRAINDICATED in hypertension/preeclampsia, cardiovascular disease and Raynaud. Never give IV push (stroke). Brand: Methergine.',
    ),
    'carboprost': _dr(
        'Synthetic 15-methyl prostaglandin F2α analog → strong myometrial contraction; also smooth muscle contraction of bronchi and GI tract',
        'Postpartum hemorrhage from uterine atony refractory to oxytocin: 0.25 mg IM (or intramyometrial) every 15–90 min, max 8 doses (2 mg); second-trimester pregnancy termination (historical)',
        'BRONCHOSPASM, diarrhea (very common), vomiting, fever/chills, flushing, hypertension, desaturation',
        'CONTRAINDICATED in ASTHMA. Methylergonovine → avoid in HTN; carboprost → avoid in asthma; misoprostol → no major contraindication (fever, shivering). Brand: Hemabate.',
    ),
    'dinoprostone': _dr(
        'Prostaglandin E2 → cervical ripening (collagen breakdown, ↑water content) and uterine contractions',
        'Cervical ripening for labor induction with an unfavorable cervix (Bishop score ≤6): vaginal insert (Cervidil — removable) or gel (Prepidil)',
        'Uterine tachysystole with fetal heart rate changes (remove the insert), fever, nausea, vomiting, diarrhea',
        'Avoid prostaglandins (dinoprostone, misoprostol) in women with a prior cesarean or uterine scar (rupture risk) — use a Foley balloon or oxytocin instead. Wait 30 min after removing the insert before starting oxytocin.',
    ),
    'tranexamic acid': _dr(
        'Synthetic lysine analog; blocks lysine-binding sites on plasminogen → prevents conversion to plasmin and fibrin breakdown (antifibrinolytic)',
        'POSTPARTUM HEMORRHAGE: 1 g IV over 10 min within 3 h of birth, repeat once after 30 min if bleeding continues (WOMAN trial: ↓death from bleeding); heavy menstrual bleeding (oral 1.3 g TID ×5 days); trauma hemorrhage (CRASH-2, within 3 h); surgery/dental bleeding in hemophilia',
        'Thromboembolism (theoretical — not increased in PPH/trauma trials), seizures at high doses, nausea, visual disturbance; dose-adjust in renal impairment',
        'Benefit is time-dependent — given after 3 h it may be harmful. Oral TXA for heavy periods is a non-hormonal option when contraception is not wanted.',
    ),
    'betamethasone': _dr(
        'Potent fluorinated glucocorticoid that crosses the placenta; induces fetal type II pneumocytes to produce SURFACTANT and accelerates maturation of lungs, brain vasculature and gut',
        'Antenatal corticosteroids: 12 mg IM ×2 doses 24 h apart (alternative: dexamethasone 6 mg IM q12h ×4) when delivery is likely within 7 days at 24 0/7–33 6/7 weeks (consider from 22–23 weeks); late-preterm course at 34 0/7–36 6/7 if no prior course and no pregestational diabetes (ALPS trial); topical for dermatoses',
        "Maternal hyperglycemia for ~3–5 days (monitor/adjust insulin in diabetics), leukocytosis (WBC rise — don't mistake for infection); neonatal hypoglycemia after late-preterm courses",
        'Benefits: ↓neonatal death, RDS, intraventricular hemorrhage and necrotizing enterocolitis; maximal benefit 24 h–7 days after the first dose. One rescue course allowed if ≥7–14 days since the first and delivery <34 weeks.',
    ),
    'rho(d) immune globulin': _dr(
        'Pooled IgG anti-D antibody; binds and clears fetal Rh(D)-positive red cells from the maternal circulation before the mother can mount her own immune response (prevents sensitization)',
        'Rh(D)-negative, antibody-NEGATIVE women: 300 mcg IM at 28 weeks; within 72 h of delivering an Rh(D)+ infant; after any sensitizing event — abortion, ectopic, miscarriage (ACOG 2024: may be omitted before 12 weeks), molar evacuation, amniocentesis/CVS, abdominal trauma, external cephalic version, antepartum bleeding; ITP in Rh+ patients (IV)',
        'Injection-site pain, fever; transient positive antibody screen (passive anti-D); rare hemolysis/allergic reactions; blood-product origin',
        'One 300 mcg vial covers 30 mL of fetal whole blood (15 mL fetal RBCs); Kleihauer-Betke or flow cytometry quantifies larger hemorrhages → give extra vials. Useless once the mother is already sensitized. Brand: RhoGAM.',
    ),
    'terbutaline': _dr(
        'Selective β2-adrenergic agonist → ↑cAMP → myometrial (and bronchial) smooth muscle relaxation',
        'Acute uterine TACHYSYSTOLE with an abnormal fetal heart tracing (0.25 mg SC once); short-term tocolysis (≤48–72 h) in some settings; facilitates external cephalic version; asthma (historical)',
        'Maternal tachycardia, palpitations, tremor, hyperglycemia, hypokalemia, pulmonary edema, arrhythmias, myocardial ischemia; fetal tachycardia',
        'FDA boxed warning: do NOT use injectable terbutaline for prolonged tocolysis (>48–72 h) or oral terbutaline for preterm labor prevention (maternal cardiac deaths). Avoid in cardiac disease and poorly controlled diabetes or hyperthyroidism.',
    ),
    'clomiphene': _dr(
        'Selective estrogen receptor modulator (SERM); blocks hypothalamic estrogen receptors → removes negative feedback → ↑GnRH pulses → ↑FSH and LH → follicle development and ovulation',
        'Ovulation induction for anovulatory infertility (PCOS — now second-line to letrozole; unexplained infertility with IUI); male hypogonadism (off-label)',
        'Multiple gestation (~7–10%, mostly twins), hot flashes, visual disturbances (scotomata — stop the drug), mood changes, ovarian enlargement/cysts, OHSS (rare), thin endometrium and hostile cervical mucus (antiestrogen effects)',
        'PCOS ovulation induction: LETROZOLE has a higher live-birth rate than clomiphene (PPCOS II trial). Limit to ~6 ovulatory cycles.',
    ),
    'letrozole': _dr(
        'Non-steroidal aromatase inhibitor → ↓conversion of androgens to estrogens → (premenopausal) ↓estrogen feedback → ↑FSH → ovulation; (postmenopausal) profound estrogen suppression',
        'FIRST-LINE ovulation induction in PCOS (off-label) and unexplained infertility; hormone receptor-positive breast cancer in postmenopausal women (adjuvant, metastatic); endometriosis and fibroids (off-label)',
        'Hot flashes, arthralgia/myalgia, fatigue; long-term (cancer use): bone loss/osteoporosis, ↑cholesterol; fewer multiple pregnancies and less endometrial thinning than clomiphene',
        'Taken for 5 days early in the cycle (days 3–7); short half-life means no estrogen deprivation at implantation. Breast cancer use: DEXA monitoring + calcium/vitamin D.',
    ),
    'mifepristone': _dr(
        'Progesterone receptor antagonist (also glucocorticoid receptor antagonist at higher doses) → decidual breakdown, cervical softening and ↑myometrial sensitivity to prostaglandins',
        'Medication abortion up to 70–77 days (200 mg PO, then misoprostol 800 mcg buccal 24–48 h later — ~95–98% effective); management of early pregnancy loss (200 mg PO before misoprostol — more effective than misoprostol alone, PreFaR trial); Cushing syndrome hyperglycemia (Korlym, high dose)',
        'Cramping and bleeding (expected), nausea, prolonged/heavy bleeding requiring aspiration (rare), infection (rare — Clostridium sordellii)',
        'Exclude ectopic pregnancy first (mifepristone does not treat it). Contraindications: ectopic, IUD in place (remove), chronic adrenal failure, long-term steroids, bleeding disorder/anticoagulation, porphyria. Rh-negative ≥12 weeks: RhIG.',
    ),
    'medroxyprogesterone': _dr(
        'Progestin; suppresses LH surge (ovulation), thickens cervical mucus, thins/decidualizes the endometrium',
        'Contraception: DMPA 150 mg IM (or 104 mg SC) every 13 weeks (typical-use failure ~4%); abnormal uterine bleeding (oral cyclic or taper), endometrial hyperplasia without atypia, endometrial protection with estrogen HRT, secondary amenorrhea (progestin challenge), endometriosis pain',
        'Irregular bleeding then amenorrhea, WEIGHT GAIN, reversible BONE MINERAL DENSITY LOSS (boxed warning — recovers after stopping), DELAYED return of fertility (up to 10–18 months), mood changes, headache',
        'Good choice when estrogen is contraindicated (VTE, smokers >35, migraine with aura) and for sickle cell disease (↓crises) and seizure disorders. Do not use if the patient wants pregnancy soon after stopping. Brand: Depo-Provera.',
    ),
    'levonorgestrel': _dr(
        'Progestin. EMERGENCY contraception (1.5 mg PO once): delays/prevents the LH surge and ovulation — NOT an abortifacient (no effect after implantation). IUD (52 mg — Mirena, Liletta; lower doses — Kyleena, Skyla): thickens cervical mucus, endometrial suppression, sperm inhibition',
        'Emergency contraception within 72 h (some effect to 120 h; OTC, no age restriction); long-acting reversible contraception — 52 mg LNG-IUD effective up to 8 years; heavy menstrual bleeding (most effective medical therapy), endometrial hyperplasia without atypia, endometrial protection with HRT, dysmenorrhea/adenomyosis',
        'EC: nausea, irregular next period. IUD: irregular spotting first 3–6 months then light periods/amenorrhea, expulsion (~3–6%), uterine perforation at insertion (rare), PID only in the first 3 weeks after insertion, ovarian cysts; if pregnancy occurs it is more likely ectopic',
        'Oral LNG EC is less effective with BMI >30 → prefer ulipristal or a copper IUD (most effective EC). Pregnancy with an IUD in place → exclude ectopic, then remove the IUD if strings visible.',
    ),
    'etonogestrel implant': _dr(
        'Single subdermal rod (68 mg etonogestrel — Nexplanon) in the inner upper arm; suppresses ovulation and thickens cervical mucus',
        'Long-acting reversible contraception — MOST EFFECTIVE reversible method (failure <0.1%), FDA-labeled 3 years (effective ~5); safe postpartum, while breastfeeding, and when estrogen is contraindicated',
        'UNPREDICTABLE bleeding (most common reason for removal), headache, acne, weight change, mood changes; insertion/removal complications (deep or non-palpable rod)',
        "Efficacy reduced by enzyme-inducing drugs (rifampin, carbamazepine, phenytoin, efavirenz, St John's wort) — add or switch method.",
    ),
    'progesterone': _dr(
        'Natural progesterone (vaginal gel/insert, IM in oil, oral micronized); maintains the decidua and myometrial quiescence; opposes estrogen-driven endometrial proliferation',
        'Prevention of preterm birth in a singleton pregnancy with a SHORT CERVIX (≤20 mm before 24 weeks): vaginal progesterone; luteal phase support in IVF; endometrial protection with estrogen HRT (micronized progesterone — may carry lower breast cancer and VTE risk than synthetic progestins); secondary amenorrhea',
        'Drowsiness (oral — take at bedtime), vaginal irritation/discharge, breast tenderness, bloating, mood changes',
        '17-α-hydroxyprogesterone caproate (Makena) IM injections for prior preterm birth were WITHDRAWN by the FDA in 2023 (PROLONG trial — no benefit).',
    ),
    'doxylamine-pyridoxine': _dr(
        'Combination H1-antihistamine (doxylamine, also anticholinergic and sedating) + vitamin B6 (pyridoxine); mechanism of B6 in nausea unclear',
        'FIRST-LINE pharmacologic therapy for nausea and vomiting of pregnancy (Diclegis/Bonjesta; or OTC doxylamine 12.5 mg + pyridoxine 25 mg); pyridoxine alone for mild symptoms',
        'Drowsiness (most common — take at bedtime), dizziness, dry mouth, constipation',
        'Extensive safety data — not teratogenic. Step-up if needed: add an antidopaminergic (metoclopramide, prochlorperazine, promethazine) or ondansetron; IV fluids with thiamine if dehydrated.',
    ),
    'methyldopa': _dr(
        'Prodrug converted to α-methylnorepinephrine → central α2-adrenergic agonist → ↓sympathetic outflow → ↓peripheral resistance',
        'Chronic hypertension in pregnancy (long safety record; now usually third-line after labetalol and nifedipine because of weaker efficacy and side effects)',
        'Sedation, fatigue, depression (often intolerable), dry mouth, orthostatic hypotension; POSITIVE direct Coombs test (10–20%) with rare autoimmune HEMOLYTIC anemia; hepatitis; drug fever; rebound hypertension if stopped abruptly',
        'Not for acute severe hypertension (slow onset) — use IV labetalol, IV hydralazine or immediate-release oral nifedipine for BP ≥160/110. Avoid postpartum (worsens postpartum depression).',
    ),
    'leuprolide': _dr(
        'GnRH AGONIST; continuous (non-pulsatile) receptor stimulation → initial flare of LH/FSH, then pituitary DOWN-REGULATION → ↓LH/FSH → medical castration (↓estrogen/testosterone) within ~2–4 weeks',
        'Endometriosis, uterine fibroids (preoperative shrinkage and anemia correction — 3 months), central precocious puberty, prostate cancer (with antiandrogen to block flare), IVF protocols/trigger, gender-affirming care',
        'Hypoestrogenic effects: hot flashes, vaginal dryness, BONE LOSS (limit to 6 months without add-back therapy), mood changes; initial flare (prostate cancer: bone pain, urinary obstruction)',
        'Add-back therapy (norethindrone ± low-dose estrogen) allows longer use. GnRH ANTAGONISTS (elagolix, relugolix — oral; degarelix) cause immediate suppression with NO flare.',
    ),
    'relugolix': _dr(
        'Oral GnRH ANTAGONIST → immediate dose-dependent ↓LH/FSH and estradiol (no flare); combination product includes estradiol 1 mg + norethindrone acetate 0.5 mg add-back (Myfembree)',
        'Heavy menstrual bleeding from uterine FIBROIDS and moderate-severe ENDOMETRIOSIS pain (relugolix combination, up to 24 months); advanced prostate cancer (relugolix alone — Orgovyx)',
        'Hot flashes, bone mineral density loss (less with add-back), headache, mood changes/depression, ↑liver enzymes; combination product carries estrogen class risks (boxed warning: thromboembolism)',
        'Elagolix (Orilissa; Oriahnn with add-back) is the related oral GnRH antagonist. Estrogen-containing combinations are contraindicated in high VTE risk, smokers >35, and migraine with aura.',
    ),
    'raloxifene': _dr(
        'SERM: estrogen AGONIST in bone and liver (↓LDL); ANTAGONIST in breast and uterus (no endometrial proliferation, unlike tamoxifen)',
        'Postmenopausal osteoporosis (↓vertebral fractures — not hip); reduction of invasive breast cancer risk in high-risk postmenopausal women',
        '↑VTE risk (boxed warning — stop 72 h before immobilization), hot flashes, leg cramps, peripheral edema; ↑fatal stroke risk in women with CAD',
        'Tamoxifen vs raloxifene: both ↑VTE; only tamoxifen ↑endometrial cancer (agonist in uterus). Raloxifene does not treat hot flashes (it causes them).',
    ),
    'conjugated estrogens': _dr(
        'Mixture of estrogens (e.g. Premarin) binding nuclear estrogen receptors; in AUB, IV estrogen promotes rapid endometrial regrowth over denuded areas and ↑clotting factors',
        'Menopausal vasomotor symptoms and genitourinary syndrome (oral, transdermal estradiol, vaginal cream); ACUTE heavy uterine bleeding (25 mg IV every 4–6 h up to 24 h, then switch to oral COC/progestin); prevention of postmenopausal osteoporosis; hypogonadism/POI',
        'Unopposed estrogen → ENDOMETRIAL HYPERPLASIA/CANCER (add a progestogen if uterus present), VTE and stroke (lower with transdermal), breast cancer (with combined therapy, WHI), gallbladder disease, nausea, breast tenderness',
        'Bazedoxifene + conjugated estrogens (Duavee) protects the endometrium without a progestin. Transdermal estradiol preferred when VTE risk or hypertriglyceridemia.',
    ),
    'fezolinetant': _dr(
        'Neurokinin-3 (NK3) receptor antagonist; blocks neurokinin B signaling on hypothalamic KNDy neurons in the thermoregulatory center (overactive after estrogen loss)',
        'Moderate-severe vasomotor symptoms (hot flashes) of menopause — NON-HORMONAL option (Veozah, 2023); elinzanetant (NK1/NK3 antagonist) is a related agent',
        'Abdominal pain, diarrhea, insomnia, back pain; HEPATOTOXICITY (boxed warning added 2024 — check LFTs at baseline and monthly for the first 3 months, then at 6 and 9 months)',
        'Useful for women with breast cancer history or other contraindications to estrogen. Contraindicated with strong CYP1A2 inhibitors and cirrhosis.',
    ),
    'cabergoline': _dr(
        'Long-acting ergot-derived dopamine D2 receptor AGONIST → inhibits prolactin secretion from lactotrophs; shrinks prolactinomas',
        'Hyperprolactinemia and PROLACTINOMA (first-line; better tolerated and more effective than bromocriptine); lactation suppression (rarely); acromegaly (adjunct); OHSS prevention in IVF',
        'Nausea, headache, dizziness, orthostatic hypotension; impulse control disorders; cardiac VALVULOPATHY at high (Parkinson) doses — echo if long-term high dose; psychosis',
        'Pregnancy: bromocriptine has more safety data — stop dopamine agonists once pregnant for most microadenomas; macroadenomas need visual-field monitoring (tumor growth).',
    ),
    'bromocriptine': _dr(
        'Ergot-derived dopamine D2 receptor agonist → ↓prolactin; also used in Parkinson disease; quick-release form resets hypothalamic dopaminergic tone (diabetes)',
        'Hyperprolactinemia/prolactinoma (preferred when pregnancy is planned — most safety data), acromegaly, Parkinson disease (rarely now), type 2 diabetes (Cycloset), peripartum cardiomyopathy (investigational in some centers), neuroleptic malignant syndrome',
        'Nausea/vomiting (take with food at bedtime), orthostatic hypotension, headache, nasal congestion; psychosis; postpartum use linked to stroke, MI and seizures — no longer used to suppress lactation in the US',
        'Cabergoline (twice weekly) is preferred for prolactinoma outside pregnancy planning.',
    ),
    'zuranolone': _dr(
        'Oral neuroactive steroid; positive allosteric modulator of synaptic and extrasynaptic GABA-A receptors (synthetic analog of allopregnanolone, which falls abruptly after delivery)',
        'POSTPARTUM DEPRESSION (moderate-severe) — 50 mg once daily in the evening with fat-containing food for 14 days (Zurzuvae, FDA 2023); rapid onset (days). IV brexanolone is the related 60-hour infusion',
        'Somnolence, dizziness, sedation (boxed warning: no driving for 12 h after each dose), fatigue, UTI, suicidal thoughts (as with antidepressants); CNS depression with alcohol/opioids/benzodiazepines',
        'SSRIs (sertraline) remain standard for PPD and are breastfeeding-compatible; zuranolone offers a fast 2-week course; limited breastfeeding data.',
    ),
    'folic acid': _dr(
        'Synthetic folate; converted to tetrahydrofolate — cofactor for purine and thymidylate synthesis (DNA synthesis) and methylation (homocysteine → methionine)',
        'Prevention of NEURAL TUBE DEFECTS: 0.4 mg (400 mcg) daily for all women capable of pregnancy, from ≥1 month before conception through the first 2–3 months; 4 mg daily if prior NTD-affected pregnancy; folate-deficiency megaloblastic anemia; with methotrexate (RA) to reduce toxicity; hemolytic anemias (sickle cell)',
        'Well tolerated; high doses can MASK B12 deficiency (corrects the anemia while neurologic damage progresses)',
        'Neural tube closes by day 28 after conception — before most women know they are pregnant, so supplementation must start before conception. Leucovorin (folinic acid) — not folic acid — rescues methotrexate toxicity.',
    ),
    # ── Primary care / family medicine drugs ──
    'varenicline': _dr(
        'Partial AGONIST at α4β2 nicotinic acetylcholine receptors → modest dopamine release (↓craving/withdrawal) while BLOCKING nicotine binding (↓reward from smoking)',
        'Smoking cessation — most effective single agent; start 1 week before the quit date (or flexible quit within 1–3 months), 12 weeks (+12 more if successful); can combine with NRT',
        'NAUSEA (most common — take with food and water), insomnia, abnormal/vivid dreams, headache; neuropsychiatric effects (boxed warning REMOVED 2016 after EAGLES — safe in stable psychiatric illness; monitor); dose-reduce if CrCl <30',
        'First-line for tobacco cessation alongside combination NRT; renally cleared, no drug interactions to speak of. Brand: Chantix.',
    ),
    'nicotine replacement therapy': _dr(
        'Delivers nicotine without combustion toxins; long-acting PATCH (steady level) relieves withdrawal; short-acting forms (gum, lozenge, inhaler, nasal spray) treat cravings',
        'Smoking cessation — COMBINATION NRT (patch + short-acting) is as effective as varenicline and better than single NRT; start on the quit date; 8–12+ weeks; OTC (patch, gum, lozenge)',
        "Patch: skin irritation, vivid dreams/insomnia (remove at bedtime); gum: jaw soreness, hiccups, dyspepsia ('chew and park'); nasal spray: nasal irritation; overdose symptoms with continued smoking (nausea, dizziness)",
        'Safe in stable cardiovascular disease; can be considered in pregnancy if counseling fails (lower risk than smoking).',
    ),
    'finasteride': _dr(
        '5α-reductase (type 2) inhibitor → ↓conversion of testosterone to DIHYDROTESTOSTERONE (DHT) → prostate shrinkage (~20–30% over 6–12 months); dutasteride inhibits types 1 and 2',
        'BPH with enlarged prostate (with or without α-blocker — combination ↓acute urinary retention and surgery, MTOPS); male-pattern androgenic alopecia (1 mg); hirsutism (off-label)',
        'Decreased libido, erectile/ejaculatory dysfunction, gynecomastia; HALVES the PSA (multiply PSA by 2 for interpretation after 6 months); ↑high-grade prostate cancer detection (PCPT); TERATOGENIC — pregnant women should not handle crushed tablets (feminization of a male fetus)',
        'Takes 6–12 months to work — α-blockers (tamsulosin) give faster symptom relief.',
    ),
    'tamsulosin': _dr(
        'Selective α1A-adrenergic antagonist (uroselective) → relaxes smooth muscle of the prostate and bladder neck → ↑urine flow',
        'BPH lower urinary tract symptoms (first-line drug; works in days); medical expulsive therapy for distal ureteral stones 5–10 mm; urinary retention (trial without catheter); prostatitis/CPPS',
        'Orthostatic hypotension/dizziness (less than nonselective α-blockers — terazosin, doxazosin), retrograde/abnormal ejaculation, nasal congestion; INTRAOPERATIVE FLOPPY IRIS SYNDROME during cataract surgery (tell the ophthalmologist)',
        'Nonselective α-blockers (doxazosin, terazosin) also lower BP but are not preferred antihypertensives (ALLHAT — ↑HF).',
    ),
    'sildenafil': _dr(
        'Phosphodiesterase-5 inhibitor → ↑cGMP in corpus cavernosum and pulmonary vasculature smooth muscle → vasodilation (requires sexual stimulation/nitric oxide release)',
        'Erectile dysfunction (on demand ~1 h before, effect 4–6 h); pulmonary arterial hypertension (Revatio); tadalafil (36 h; daily option) also treats BPH symptoms',
        'Headache, flushing, dyspepsia, nasal congestion, back pain/myalgia (tadalafil), blue-tinged vision (PDE6 — sildenafil), hypotension; NAION (sudden vision loss — stop), sudden hearing loss, PRIAPISM >4 h (emergency)',
        'CONTRAINDICATED with nitrates (any form) or riociguat — profound hypotension; separate from α-blockers. Wait 24 h (sildenafil) / 48 h (tadalafil) before nitroglycerin.',
    ),
    'oxybutynin': _dr(
        'Antimuscarinic (M3 > M1) → relaxes detrusor, ↓involuntary contractions; tertiary amine — crosses the blood-brain barrier',
        'Overactive bladder/urge incontinence, neurogenic bladder, bladder spasms (catheter/stent), hyperhidrosis',
        'Anticholinergic effects: dry mouth (most common), constipation, blurred vision, urinary retention, tachycardia, heat intolerance; CONFUSION/cognitive impairment and ↑dementia risk in older adults (Beers — avoid); contraindicated in narrow-angle glaucoma, urinary retention, gastric retention',
        'Older adults with urge incontinence → prefer a β3-agonist (mirabegron, vibegron) or trospium (quaternary — less CNS penetration).',
    ),
    'mirabegron': _dr(
        'β3-adrenergic receptor agonist → detrusor relaxation during filling → ↑bladder capacity',
        'Overactive bladder/urge incontinence — preferred over antimuscarinics in OLDER adults (no anticholinergic cognitive burden); vibegron is a related agent (no BP effect, no CYP2D6 inhibition)',
        'Hypertension (mild ↑BP — monitor; avoid if severe uncontrolled HTN), headache, nasopharyngitis, UTI, urinary retention (with outlet obstruction); moderate CYP2D6 inhibitor (↑metoprolol, desipramine levels)',
        'Behavioral therapy (bladder training, pelvic floor exercises) comes before any OAB medication.',
    ),
    'denosumab': _dr(
        'Monoclonal antibody against RANKL → blocks osteoclast formation, function and survival → ↓bone resorption',
        'Osteoporosis (high fracture risk, CKD where bisphosphonates are limited, bisphosphonate intolerance) — 60 mg SC every 6 months; bone metastases/hypercalcemia of malignancy, giant cell tumor (Xgeva 120 mg monthly)',
        'HYPOCALCEMIA (especially CKD — check Ca and vitamin D first), infections (cellulitis, UTI), eczema, osteonecrosis of the jaw and atypical femoral fractures (rare); REBOUND VERTEBRAL FRACTURES if stopped or delayed — must transition to a bisphosphonate',
        'Never simply stop denosumab — rapid bone loss and multiple vertebral fractures; follow with zoledronic acid or alendronate.',
    ),
    'terbinafine': _dr(
        'Allylamine antifungal; inhibits SQUALENE EPOXIDASE → ↓ergosterol + toxic squalene accumulation → fungicidal against dermatophytes',
        'ONYCHOMYCOSIS (oral 250 mg daily — 6 weeks fingernails, 12 weeks toenails; most effective oral agent — confirm with KOH/culture/PCR first), tinea capitis (Trichophyton — terbinafine or griseofulvin), tinea pedis/corporis/cruris (topical 1–2 weeks)',
        'HEPATOTOXICITY (rare liver failure — baseline LFTs; avoid in liver disease), taste/smell disturbance (can be prolonged), GI upset, rash/SJS, depression, drug-induced lupus; CYP2D6 inhibitor (↑TCAs, β-blockers, SSRIs)',
        'Confirm onychomycosis before 12 weeks of oral therapy — half of dystrophic nails are not fungal (psoriasis, trauma).',
    ),
    'permethrin': _dr(
        'Pyrethroid; blocks sodium channel repolarization in arthropod nerve membranes → paralysis and death of mites/lice',
        'SCABIES (5% cream neck-down, leave 8–14 h, repeat in 1 week; first-line, safe in pregnancy, breastfeeding and infants ≥2 months); HEAD LICE (1% lotion/creme rinse OTC; repeat day 9–10); treated clothing/nets for tick and mosquito prevention',
        'Burning, stinging, itching, erythema; post-scabetic itch persists 2–4 weeks (not failure); rare allergic reactions (chrysanthemum)',
        'Treat all close contacts at the same time and launder bedding — otherwise reinfestation.',
    ),
    'mupirocin': _dr(
        'Topical antibiotic; binds bacterial ISOLEUCYL-tRNA synthetase → ↓protein synthesis (unique mechanism, no cross-resistance)',
        'Localized IMPETIGO (2% ointment TID ×5 days), secondary infected minor wounds; nasal decolonization of S. aureus/MRSA (intranasal BID ×5 days, with chlorhexidine body washes) for recurrent infections or preoperative',
        'Local burning, itching; resistance with widespread prolonged use',
        'Extensive impetigo, many lesions or systemic signs → oral cephalexin (MRSA: clindamycin/TMP-SMX/doxycycline).',
    ),
    'cyclobenzaprine': _dr(
        'Centrally acting skeletal muscle relaxant structurally related to TCAs (5-HT2 antagonism in the brainstem → ↓tonic somatic motor activity)',
        'Acute musculoskeletal low back/neck pain and spasm (short-term ≤2–3 weeks, adjunct to NSAIDs); fibromyalgia sleep (low dose, off-label)',
        'SEDATION, dizziness, dry mouth and other ANTICHOLINERGIC effects, confusion; serotonin syndrome with serotonergic drugs/MAOIs; arrhythmias in overdose (TCA-like); contraindicated post-MI, arrhythmias, heart block, hyperthyroidism',
        'Beers criteria: avoid muscle relaxants in older adults (sedation, falls, anticholinergic effects).',
    ),
    'meclizine': _dr(
        'First-generation H1 antihistamine with anticholinergic properties → ↓vestibular stimulation and labyrinth excitability',
        'Motion sickness (take 1 h before travel), short-term symptomatic relief of acute peripheral vertigo (vestibular neuritis, Ménière attacks)',
        'Drowsiness, dry mouth, blurred vision, urinary retention, confusion (elderly); vestibular suppressants delay central compensation if used long-term',
        'Not recommended for BPPV (use the Epley maneuver); avoid in older adults (Beers).',
    ),
    'zolpidem': _dr(
        "Non-benzodiazepine 'Z-drug' hypnotic; positive allosteric modulator selective for GABA-A receptors containing the α1 subunit (sedative, less anxiolytic/muscle relaxant)",
        'Short-term treatment of insomnia (sleep-onset; ER for maintenance; sublingual low-dose for middle-of-the-night awakening)',
        'Next-morning impairment (FDA lowered dose for WOMEN — 5 mg IR — slower clearance), COMPLEX SLEEP BEHAVIORS (sleepwalking, sleep-driving, eating — boxed warning; stop if occurs), amnesia, falls and fractures in elderly, dependence/withdrawal, respiratory depression with opioids/alcohol',
        'CBT-I is first-line for chronic insomnia; avoid Z-drugs in older adults (Beers). Take only when 7–8 h of sleep is available.',
    ),
    'melatonin': _dr(
        'Endogenous pineal hormone (synthetic OTC supplement); MT1/MT2 receptor agonist → shifts circadian phase and modestly promotes sleep onset (ramelteon is the FDA-approved MT1/MT2 agonist)',
        'Jet lag, delayed sleep-phase disorder, shift work, insomnia in children with ADHD/autism (with behavioral strategies), sleep-onset insomnia in older adults (modest)',
        'Generally well tolerated: headache, daytime drowsiness, vivid dreams; supplement content is unregulated and variable (gummies — pediatric ingestions rising)',
        "AASM suggests not using melatonin for chronic insomnia in adults (weak evidence) — it's a timing (chronobiotic) agent more than a hypnotic.",
    ),
    'tirzepatide': _dr(
        'Dual GIP and GLP-1 receptor agonist (once weekly SC) → glucose-dependent insulin secretion, ↓glucagon, slowed gastric emptying, ↓appetite',
        'Type 2 diabetes (Mounjaro — greatest HbA1c and weight reduction of the incretins, SURPASS); chronic weight management (Zepbound — ~20% weight loss, SURMOUNT); obstructive sleep apnea with obesity (FDA 2024)',
        'Nausea, vomiting, diarrhea, constipation (dose-escalate slowly), decreased appetite; gallbladder disease, pancreatitis; thyroid C-cell tumor boxed warning (contraindicated with MTC/MEN2); hypoglycemia with insulin/sulfonylureas; ↓absorption of ORAL CONTRACEPTIVES after start and dose increases (use non-oral/backup contraception for 4 weeks); aspiration risk under anesthesia',
        'Stop ≥2 months before a planned pregnancy; weight is regained after stopping.',
    ),
    'ezetimibe': _dr(
        'Inhibits the NPC1L1 cholesterol transporter at the intestinal brush border → ↓dietary and biliary cholesterol absorption → ↑hepatic LDL receptors → ↓LDL ~20–25%',
        'Add-on to maximally tolerated statin when LDL remains above goal (IMPROVE-IT: ↓CV events post-ACS), statin intolerance, homozygous FH, sitosterolemia',
        'Well tolerated: diarrhea, myalgias (rare), ↑transaminases with statins (rare)',
        'Typical escalation for ASCVD: high-intensity statin → add ezetimibe → add PCSK9 inhibitor (or bempedoic acid/inclisiran).',
    ),
    'evolocumab': _dr(
        "Monoclonal antibody against PCSK9 (alirocumab similar; inclisiran is an siRNA given twice yearly) → PCSK9 can't degrade LDL receptors → ↑LDL receptor recycling → ↓LDL ~50–60%",
        'Clinical ASCVD or familial hypercholesterolemia with LDL above goal despite maximally tolerated statin + ezetimibe (FOURIER — ↓MI, stroke); statin intolerance',
        'Injection-site reactions, nasopharyngitis, flu-like symptoms; very low LDL appears safe; SC every 2 weeks or monthly; cost',
        'PCSK9 gain-of-function mutations cause FH; loss-of-function lowers LDL and CAD risk — the genetic basis for the drug.',
    ),
    'chlorthalidone': _dr(
        'Thiazide-like diuretic; inhibits the Na+/Cl− cotransporter in the distal convoluted tubule; longer half-life and more potent than hydrochlorothiazide',
        'Hypertension (preferred thiazide — outcome data from ALLHAT and SHEP; first-line, especially Black patients and those without CKD indications for ACEi), edema, calcium nephrolithiasis prevention (hypercalciuria), nephrogenic DI',
        "HYPOKALEMIA, hyponatremia (elderly women), hypomagnesemia, HYPERCALCEMIA (can unmask hyperparathyroidism), HYPERURICEMIA/gout, hyperglycemia, hyperlipidemia, metabolic alkalosis, photosensitivity, sulfonamide allergy (rare cross-reactivity); diuretic Thiazides 'hyperGLUC': hyperGlycemia, hyperLipidemia, hyperUricemia, hyperCalcemia",
        "Also effective in advanced CKD (CLICK trial, eGFR 15–30) — the old 'thiazides don't work in CKD' teaching is outdated.",
    ),
    'ferrous sulfate': _dr(
        'Oral iron salt (325 mg = 65 mg elemental iron); absorbed in the duodenum via DMT1, regulated by hepcidin (↑hepcidin after each dose — alternate-day dosing ↑fractional absorption)',
        'Iron-deficiency anemia (once daily or every other day; continue ~3 months after Hb normalizes to replete stores); prophylaxis in pregnancy, infants (formula/supplement from 4 months if exclusively breastfed), CKD',
        'GI upset, constipation, nausea, dark/black stools (not melena — guaiac can be positive), metallic taste; absorption ↓ by calcium, antacids, PPIs, tea/coffee, tetracyclines/fluoroquinolones (chelation), ↑ by vitamin C; iron OVERDOSE in children — leading cause of pediatric poisoning deaths (GI bleeding, shock, acidosis, liver failure; deferoxamine)',
        'Reticulocytes rise within ~7–10 days and Hb by ~1 g/dL in 2–3 weeks — no response → nonadherence, ongoing bleeding, malabsorption (celiac, H. pylori), or wrong diagnosis.',
    ),
    'cyanocobalamin': _dr(
        'Vitamin B12 — cofactor for methionine synthase (homocysteine → methionine; folate recycling) and methylmalonyl-CoA mutase',
        'B12 deficiency: pernicious anemia (anti-intrinsic factor/parietal cell antibodies, atrophic gastritis), bariatric surgery/ileal resection, Crohn, metformin, PPIs/H2 blockers, vegan diet, elderly, Diphyllobothrium; neurologic involvement (subacute combined degeneration — dorsal columns + corticospinal tracts, peripheral neuropathy, dementia)',
        'Very safe; hypokalemia early in treatment of severe megaloblastic anemia (cells regenerate), acne, injection pain',
        'High-dose ORAL B12 (1000–2000 μg daily) works even in pernicious anemia (passive diffusion ~1%); IM for severe neurologic disease. Check methylmalonic acid when B12 is borderline.',
    ),
    'cholecalciferol': _dr(
        'Vitamin D3; hydroxylated in the liver (25-OH D) then kidney (1,25-(OH)2 D, calcitriol, via 1α-hydroxylase stimulated by PTH) → ↑intestinal calcium/phosphate absorption, bone mineralization',
        'Vitamin D deficiency/insufficiency, osteoporosis (with calcium), infants (400 IU daily if breastfed), malabsorption, osteomalacia/rickets; calcitriol (active form) for CKD, hypoparathyroidism',
        'Toxicity (rare, very high doses — usually >10,000 IU/day chronically): HYPERCALCEMIA, hypercalciuria, kidney stones, nausea, confusion; granulomatous disease (sarcoidosis) ↑sensitivity',
        'Routine supplementation for fall or fracture prevention in community-dwelling older adults without deficiency is NOT recommended (USPSTF); ensure adequacy in osteoporosis treatment.',
    ),
    'benzonatate': _dr(
        'Peripherally acting antitussive related to tetracaine (local anesthetic) → anesthetizes pulmonary stretch receptors',
        'Symptomatic relief of cough (acute bronchitis, URIs) in adults and children ≥10',
        'Sedation, dizziness, headache, GI upset; swallow capsules whole (chewing → oral anesthesia, choking, laryngospasm); OVERDOSE in young children (seizures, arrhythmias, death) — keep away from children',
        'Honey (children >1 year) and dextromethorphan are other cough options; avoid codeine in children (<12 contraindicated).',
    ),
    'ulipristal': _dr(
        'Selective progesterone receptor modulator → delays or inhibits ovulation even after the LH surge has begun (more effective than levonorgestrel late in the follicular phase)',
        'EMERGENCY CONTRACEPTION up to 120 h (5 days) after unprotected intercourse (30 mg single dose, prescription — ella); preferred over levonorgestrel for BMI >30 and later presentations',
        'Headache, nausea, abdominal pain, delayed/irregular next menses; may ↓efficacy of progestin-containing contraception if started within 5 days (wait 5 days before starting hormonal contraception, use backup); breastfeeding pause per label; CYP3A4 inducers ↓efficacy',
        'Most effective EC is the copper IUD (also provides ongoing contraception); then ulipristal; then levonorgestrel (OTC).',
    ),
    'danazol': _dr(
        'Synthetic androgen (17α-ethinyl testosterone derivative) — suppresses the midcycle LH/FSH surge (anovulation, hypoestrogenic state) and has direct androgenic/antiestrogenic effects on endometrium',
        'Endometriosis (older second-line), hereditary angioedema prophylaxis (↑C1 esterase inhibitor), ITP/aplastic anemia (rare), fibrocystic breast pain',
        'Androgenic: acne, hirsutism, oily skin, weight gain, deepening voice (may be irreversible), clitoromegaly; ↓HDL/↑LDL, hepatotoxicity (cholestasis, peliosis hepatis, adenoma), pseudotumor cerebri. Teratogenic — female fetal virilization (contraindicated in pregnancy)',
        'Largely replaced by progestins, GnRH agonists/antagonists (elagolix) for endometriosis because of androgenic side effects. Irreversible voice change is the classic counseling point.',
    ),
    'ospemifene': _dr(
        'Oral selective estrogen receptor modulator (SERM) — estrogen agonist on vaginal epithelium, antagonist/neutral on breast',
        'Moderate–severe dyspareunia and vaginal dryness from genitourinary syndrome of menopause in women who cannot or prefer not to use vaginal estrogen',
        'Hot flashes (worsens vasomotor symptoms), muscle spasm, ↑VTE and stroke risk (boxed warning), possible endometrial stimulation',
        'First-line for GSM remains vaginal moisturizers/lubricants → low-dose vaginal estrogen. Ospemifene and vaginal DHEA (prasterone) are alternatives.',
    ),
    'disulfiram': _dr(
        'Irreversibly inhibits ALDEHYDE DEHYDROGENASE → acetaldehyde accumulates when alcohol is consumed → aversive reaction (flushing, throbbing headache, nausea/vomiting, sweating, tachycardia, hypotension, dyspnea) — deterrent, not anti-craving',
        'Alcohol use disorder in highly motivated patients who want ABSTINENCE, ideally with SUPERVISED administration (spouse, clinic) — adherence determines efficacy. Start only ≥12 hours after last drink (BAC zero); reaction possible up to ~ 2 weeks after last dose',
        'Hepatotoxicity (check LFTs baseline and periodically; avoid in significant liver disease), peripheral/optic neuropathy, psychosis, metallic taste, drowsiness; severe disulfiram-ethanol reaction (arrhythmias, MI, death). Avoid hidden alcohol (mouthwash, cough syrups, sauces, hand sanitizer, aftershave). Contraindicated: severe cardiac disease, psychosis, pregnancy. Inhibits CYP2C9 (↑warfarin, phenytoin)',
        'Disulfiram-like reactions with alcohol also occur with METRONIDAZOLE, tinidazole, some cephalosporins (cefotetan, cefoperazone — MTT side chain), sulfonylureas (chlorpropamide), griseofulvin, procarbazine, ketoconazole. First-line AUD drugs are naltrexone and acamprosate; disulfiram for supervised, motivated patients.',
    ),
    'acamprosate': _dr(
        'Glutamate (NMDA) modulator/GABA analog — restores balance between excitatory and inhibitory neurotransmission disrupted by chronic alcohol; reduces protracted withdrawal symptoms/craving',
        'Maintenance of ABSTINENCE in alcohol use disorder after detoxification (start once abstinent; continue even if relapse). First-line alongside naltrexone. PREFERRED in LIVER DISEASE (not hepatically metabolized) and in patients needing OPIOIDS (naltrexone would block/precipitate withdrawal)',
        'Diarrhea (most common), nausea, anxiety, insomnia, depression/suicidality (rare). RENALLY excreted unchanged — reduce dose if CrCl 30–50; CONTRAINDICATED if CrCl ≤30. TID dosing (adherence issue). Safe with alcohol (no reaction)',
        'AUD + cirrhosis → acamprosate (renal clearance). AUD + CKD → naltrexone (avoid acamprosate). AUD + chronic opioid therapy → acamprosate (not naltrexone). Other options: gabapentin, topiramate (off-label), baclofen (liver disease).',
    ),
    'esketamine': _dr(
        'S-enantiomer of ketamine; NMDA receptor ANTAGONIST → glutamate surge, AMPA activation, BDNF/synaptogenesis — RAPID antidepressant effect (hours–days)',
        'TREATMENT-RESISTANT DEPRESSION (failed ≥2 antidepressants) and MDD with acute SUICIDAL ideation/behavior — INTRANASAL, given in a certified healthcare setting (REMS) with ≥2 h post-dose observation, in conjunction with an oral antidepressant (or as monotherapy for TRD per newer labeling)',
        'Dissociation, sedation, dizziness, nausea, ↑BLOOD PRESSURE (transient — check before/after), abuse/misuse potential (Schedule III), cognitive effects; cannot drive until next day after restful sleep. Contraindicated: aneurysmal vascular disease, AVM, intracerebral hemorrhage history. IV racemic ketamine used off-label',
        'Treatment-resistant depression after 2 failed SSRIs → esketamine nasal spray (in clinic, 2-hour monitoring, BP checks) — or ECT. Rapid onset distinguishes it from conventional antidepressants (weeks).',
    ),
    'argatroban': _dr(
        'Direct thrombin inhibitor (IV; reversible, binds active site of thrombin — free and clot-bound); hepatically cleared',
        'HEPARIN-INDUCED THROMBOCYTOPENIA (treatment and prophylaxis) — preferred in RENAL failure (hepatic clearance); anticoagulation during PCI in HIT. Alternatives for HIT: bivalirudin (renal/enzymatic), fondaparinux, DOACs (stable patients)',
        'Bleeding; prolongs aPTT (monitor target 1.5–3× baseline) and falsely ↑INR (complicates warfarin transition — overlap until INR >4 on combined therapy); reduce dose in hepatic impairment; no reversal agent',
        'HIT: stop ALL heparin (including flushes, LMWH) → start a non-heparin anticoagulant (argatroban if renal failure; bivalirudin if hepatic failure) → warfarin only after platelets recover (>150k), overlapping ≥5 days. Never give platelets routinely or start warfarin alone (venous limb gangrene — protein C depletion).',
    ),
    'teriparatide': _dr(
        'Recombinant PTH(1–34) analog given INTERMITTENTLY (daily SQ) → ANABOLIC: stimulates osteoblasts > osteoclasts → ↑bone formation and density (continuous PTH is catabolic). Abaloparatide = PTHrP analog (similar)',
        'Severe OSTEOPOROSIS at very high fracture risk (T-score ≤−3.0, multiple/vertebral fractures, fractures on bisphosphonates), glucocorticoid-induced osteoporosis; max ~ 2 years lifetime then FOLLOW with an antiresorptive (bisphosphonate/denosumab) to maintain gains; hypoparathyroidism (PTH 1–84)',
        'Transient HYPERCALCEMIA, orthostatic hypotension/dizziness, nausea, leg cramps, ↑uric acid; OSTEOSARCOMA in rats (former boxed warning) → avoid with Paget disease of bone, unexplained ↑ALP, open epiphyses (children), prior skeletal radiation, bone metastases/skeletal malignancy',
        'Anabolic first then antiresorptive gives the greatest BMD gains in very-high-risk patients. Romosozumab (sclerostin antibody) is the other anabolic option (12 months; avoid with recent MI/stroke).',
    ),
    'omalizumab': _dr(
        'Recombinant humanized monoclonal ANTI-IgE antibody: binds free IgE (Cε3 domain) → prevents IgE binding to FcεRI on mast cells/basophils → ↓receptor expression and mediator release',
        'Moderate–severe persistent ALLERGIC ASTHMA (positive skin/specific IgE to perennial aeroallergen + elevated total IgE; uncontrolled on ICS/LABA), chronic spontaneous URTICARIA refractory to high-dose antihistamines, nasal polyps (CRSwNP), IgE-mediated FOOD ALLERGY (reduces reactions to accidental exposure). SQ every 2–4 weeks (dose by IgE and weight)',
        'ANAPHYLAXIS (~ 0.1–0.2%; can be delayed — observe after first doses, prescribe epinephrine autoinjector), injection-site reactions, possible ↑helminth infections, arthralgias; not for acute bronchospasm',
        'Asthma biologics by phenotype: allergic/high IgE → omalizumab; eosinophilic → mepolizumab, reslizumab, benralizumab (anti-IL-5/IL-5R); type 2 high (eos or FeNO) → dupilumab (anti-IL-4Rα); any severe → tezepelumab (anti-TSLP).',
    ),
    'dupilumab': _dr(
        'Monoclonal antibody against IL-4 RECEPTOR α subunit → blocks IL-4 and IL-13 signaling (type 2 inflammation)',
        'Moderate–severe ATOPIC DERMATITIS (≥6 months of age), moderate–severe eosinophilic/type 2 ASTHMA or oral steroid-dependent asthma, chronic rhinosinusitis with nasal polyps, EOSINOPHILIC ESOPHAGITIS, prurigo nodularis, COPD with eosinophilia, chronic spontaneous urticaria',
        'CONJUNCTIVITIS/keratitis (most common in atopic dermatitis), injection-site reactions, transient eosinophilia, oral herpes, facial erythema; avoid live vaccines; treat pre-existing helminth infections',
        'Moderate–severe eczema not controlled with topical steroids/calcineurin inhibitors → dupilumab (or JAK inhibitors — upadacitinib/abrocitinib, boxed warnings) rather than long-term systemic steroids.',
    ),
    'nirsevimab': _dr(
        'Long-acting monoclonal antibody against the RSV F (fusion) protein (prefusion site Ø) — passive immunization lasting ≥5 months (single dose)',
        'RSV PREVENTION in ALL infants <8 months born during or entering their first RSV season (one IM dose, ideally at birth or before season) unless the mother received RSV vaccine (Abrysvo, 32–36 weeks) ≥14 days before delivery; children 8–19 months at increased risk (chronic lung disease of prematurity, severe immunocompromise, cystic fibrosis, American Indian/Alaska Native) for their second season',
        'Rare hypersensitivity, rash, injection-site reaction; does not interfere with routine vaccines',
        'Replaces PALIVIZUMAB (monthly injections, high-risk only) for most infants. Clesrovimab is a newer alternative. RSV bronchiolitis treatment remains supportive (no bronchodilators/steroids routinely).',
    ),
    'palivizumab': _dr(
        'Humanized monoclonal antibody against RSV F protein — passive immunoprophylaxis, given MONTHLY IM during RSV season (up to 5 doses)',
        'RSV prophylaxis in HIGH-RISK infants: prematurity <29 weeks (first year), chronic lung disease of prematurity, hemodynamically significant congenital heart disease, neuromuscular disease/airway abnormalities, immunocompromised — now largely used only when nirsevimab is unavailable',
        'Injection-site reactions, fever, rare anaphylaxis; not a treatment for active RSV infection',
        'Most infants now receive single-dose nirsevimab (or are protected by maternal RSV vaccine at 32–36 weeks) instead of monthly palivizumab.',
    ),
    'surfactant': _dr(
        'Exogenous pulmonary surfactant (poractant alfa, beractant, calfactant — animal-derived phospholipids [dipalmitoylphosphatidylcholine] + surfactant proteins B/C) → ↓alveolar surface tension, prevents alveolar collapse at end-expiration, ↑compliance',
        'NEONATAL RESPIRATORY DISTRESS SYNDROME (surfactant deficiency of prematurity) — given intratracheally (via ETT or less-invasive surfactant administration [LISA/MIST] thin catheter while on CPAP) for preterm infants with RDS requiring FiO2 >0.30–0.40 on CPAP; also meconium aspiration (selected), congenital pneumonia',
        'Transient bradycardia/desaturation and airway obstruction during dosing, rapid improvement in compliance → risk of PNEUMOTHORAX/hyperoxia if ventilator settings not weaned, pulmonary hemorrhage',
        'Prevention of RDS: antenatal corticosteroids (↑surfactant production — lamellar bodies; L/S ratio >2 = lung maturity) + early CPAP; rescue surfactant when needed. Surfactant production begins ~ 24–28 weeks, adequate ~ 35 weeks.',
    ),
    'deferasirox': _dr(
        'Oral iron CHELATOR (tridentate; binds Fe³⁺ → fecal excretion)',
        'Chronic transfusional IRON OVERLOAD (sickle cell disease, thalassemia major, MDS, Diamond-Blackfan) — start when ferritin >1,000 ng/mL or after ~ 20 units transfused; non-transfusion-dependent thalassemia. Alternatives: deferoxamine (SQ/IV infusion — also acute iron poisoning), deferiprone (oral — AGRANULOCYTOSIS, weekly ANC)',
        'Renal toxicity (↑creatinine, Fanconi syndrome — monitor), hepatotoxicity, GI hemorrhage/ulcers, rash, auditory/ocular toxicity (annual exams); monitor creatinine, LFTs, ferritin monthly',
        'Transfusion-dependent thalassemia with ferritin 2,500 → chelation (deferasirox) + cardiac T2* MRI (iron cardiomyopathy is the leading cause of death). Hereditary hemochromatosis is treated with phlebotomy, not chelation.',
    ),
    'intravenous immunoglobulin': _dr(
        'Pooled polyclonal IgG from thousands of donors: replacement of antibodies (immunodeficiency) and IMMUNOMODULATION (Fc receptor blockade, neutralization of autoantibodies, complement inhibition, FcRn saturation → ↑catabolism of pathogenic IgG)',
        'Primary humoral immunodeficiency (CVID, X-linked agammaglobulinemia — replacement); KAWASAKI DISEASE (2 g/kg + aspirin within 10 days — ↓coronary aneurysms); ITP (rapid platelet ↑ — bleeding, pre-procedure, pregnancy); GUILLAIN-BARRÉ (equal to plasmapheresis); MYASTHENIC CRISIS; CIDP, multifocal motor neuropathy; dermatomyositis; MIS-C; fetal/neonatal alloimmune thrombocytopenia; severe neonatal hemolytic disease (selected); toxic shock syndrome (adjunct); post-exposure (measles, varicella — VariZIG preferred, hepatitis A)',
        'Infusion reactions (headache, fever, chills — slow rate, premedicate), ASEPTIC MENINGITIS, THROMBOSIS (MI, stroke, VTE — hyperviscosity), AKI (sucrose-containing products — osmotic nephrosis), hemolysis (anti-A/B), TRALI, volume overload; ANAPHYLAXIS in IgA-DEFICIENT patients with anti-IgA antibodies (use IgA-depleted product); interferes with serologies and live vaccines (delay MMR/varicella ~ 8–11 months after high-dose IVIG)',
        'Kawasaki disease → IVIG 2 g/kg + high-dose aspirin. GBS → IVIG or PLEX (not steroids). Patient with selective IgA deficiency who needs IVIG → IgA-depleted product (anaphylaxis risk).',
    ),
    'acetazolamide': _dr(
        'Carbonic anhydrase inhibitor (proximal tubule) → ↓HCO3⁻ reabsorption → bicarbonate diuresis (NaHCO3 loss) → NON-ANION GAP (hyperchloremic) METABOLIC ACIDOSIS; ↓aqueous humor and CSF production',
        'IDIOPATHIC INTRACRANIAL HYPERTENSION (first-line with weight loss), GLAUCOMA (acute angle-closure — IV/PO; also topical CAIs dorzolamide), ACUTE MOUNTAIN SICKNESS prophylaxis/treatment (respiratory stimulation via metabolic acidosis), metabolic ALKALOSIS (e.g., contraction alkalosis with volume overload in HF/COPD), periodic paralysis, urinary alkalinization (uric acid/cystine — limited), epilepsy (adjunct), central sleep apnea',
        'Paresthesias (fingers, perioral), METALLIC/altered taste (carbonated drinks), fatigue, nausea, polyuria, HYPOKALEMIA, NAGMA, calcium phosphate KIDNEY STONES (↑urine pH, ↓citrate), SULFONAMIDE (cross-reactivity concern — SJS rare), aplastic anemia rare; worsens hepatic encephalopathy (↑ammonia reabsorption — alkaline urine) — avoid in cirrhosis; caution in COPD with severe hypercapnia',
        'Obese woman with IIH → acetazolamide + weight loss. Trekker planning to climb to 4,000 m → acetazolamide prophylaxis (gradual ascent best). Causes NAGMA (type 2 RTA-like).',
    ),
    'nimodipine': _dr(
        'Dihydropyridine CALCIUM CHANNEL BLOCKER with relative cerebral vascular selectivity (lipophilic, crosses BBB) — neuroprotective effect',
        'ANEURYSMAL SUBARACHNOID HEMORRHAGE: 60 mg PO/NG every 4 h × 21 days started within 96 h — ↓delayed cerebral ischemia and improves neurologic outcome (not by preventing angiographic vasospasm)',
        'HYPOTENSION (reduce dose/split to 30 mg q2h — avoid cerebral hypoperfusion), headache, flushing, edema; NEVER give the capsule contents IV (cardiac arrest/death); CYP3A4 interactions',
        'Every aneurysmal SAH patient gets oral nimodipine for 21 days, plus early aneurysm securing (coiling/clipping), BP control before securing (SBP <160), euvolemia, and monitoring for vasospasm (days 3–14), hydrocephalus, hyponatremia (cerebral salt wasting/SIADH) and seizures.',
    ),
    'fomepizole': _dr(
        'Competitive inhibitor of ALCOHOL DEHYDROGENASE → blocks conversion of methanol → formic acid and ethylene glycol → glycolic/oxalic acids (toxic metabolites)',
        'METHANOL and ETHYLENE GLYCOL poisoning (also diethylene glycol): give on suspicion (history, unexplained ↑osmolal gap and/or AGMA, visual symptoms, calcium oxalate crystals/AKI) before levels return; loading 15 mg/kg IV then 10 mg/kg q12h (↑frequency during hemodialysis); disulfiram-ethanol reaction (blocks acetaldehyde formation)',
        'Headache, nausea, dizziness, bradycardia (rare), mild ↑LFTs; safer and easier dosing than ethanol (alternative ADH inhibitor — intoxication, hypoglycemia)',
        'Toxic alcohol ingestion → fomepizole + HEMODIALYSIS (for severe acidosis pH <7.25–7.3, visual changes (methanol), AKI, high levels, deteriorating vitals) + cofactors: folic/folinic acid (methanol → formate clearance), thiamine + pyridoxine (ethylene glycol), sodium bicarbonate for acidosis.',
    ),
    'dimercaprol': _dr(
        'BAL (British anti-Lewisite) — dithiol chelator given deep IM (in peanut oil); forms stable complexes with heavy metals → renal/biliary excretion',
        'Severe LEAD POISONING (lead encephalopathy or blood lead ≥70 μg/dL in children — give BAL FIRST, then CaNa2-EDTA 4 hours later to avoid redistribution of lead into the brain), ARSENIC, MERCURY (inorganic), gold poisoning; Wilson disease (historical)',
        'Painful IM injections, hypertension, tachycardia, fever, nausea, headache, hemolysis in G6PD deficiency; contraindicated in PEANUT ALLERGY (formulated in peanut oil); avoid with iron (toxic complex)',
        'Lead levels in children: ≥3.5 μg/dL → environmental investigation; ≥45 μg/dL → SUCCIMER (oral DMSA) chelation; ≥70 or encephalopathy → hospitalize, dimercaprol + CaNa2-EDTA.',
    ),
    'succimer': _dr(
        'DMSA (meso-2,3-dimercaptosuccinic acid) — ORAL water-soluble dithiol chelator for heavy metals',
        'LEAD POISONING in children with blood lead ≥45 μg/dL WITHOUT encephalopathy (19-day course; outpatient once removed from exposure) — first-line oral chelator; also arsenic and mercury poisoning',
        'GI upset, rash, transient ↑LFTs, neutropenia (monitor CBC), sulfur odor; ensure the child is removed from the lead source before chelation',
        'Child with blood lead 52 μg/dL and no neurologic symptoms → remove from source + oral succimer; recheck levels (rebound common). Basophilic stippling + microcytic anemia + abdominal pain/constipation → lead.',
    ),
    'pralidoxime': _dr(
        "2-PAM — oxime that REACTIVATES acetylcholinesterase by removing the phosphoryl group from organophosphate-bound enzyme — effective only before 'AGING' (irreversible binding)",
        'ORGANOPHOSPHATE poisoning (insecticides — malathion, parathion; nerve agents — sarin, VX) with nicotinic signs (muscle fasciculations, WEAKNESS, respiratory muscle paralysis); given WITH ATROPINE (which treats muscarinic effects — DUMBELS: Diarrhea, Urination, Miosis, Bronchorrhea/Bronchospasm/Bradycardia, Emesis, Lacrimation, Salivation/Sweating — titrate atropine to drying of bronchial secretions); not needed for carbamates (reversible)',
        'Transient diplopia, blurred vision, dizziness, headache, tachycardia, hypertension, laryngospasm/muscle rigidity with rapid infusion',
        'Farmer with miosis, salivation, bronchorrhea, bradycardia and fasciculations after spraying crops → organophosphate → decontaminate (remove clothes, protect staff), ATROPINE (large repeated doses until secretions dry) + PRALIDOXIME early; benzodiazepines for seizures.',
    ),
    'terlipressin': _dr(
        'Synthetic VASOPRESSIN ANALOG (V1 receptor agonist, prodrug of lysine-vasopressin) → SPLANCHNIC VASOCONSTRICTION → ↓portal pressure and redirects blood to systemic circulation → ↑renal perfusion',
        'HEPATORENAL SYNDROME-AKI (FDA-approved 2022) with IV ALBUMIN; also variceal bleeding (outside US); alternatives for HRS in US: norepinephrine + albumin (ICU) or midodrine + octreotide + albumin',
        'Ischemic events (myocardial, mesenteric, digital/skin necrosis), RESPIRATORY FAILURE (fluid overload with albumin — avoid if SpO2 <90% or volume overload; boxed warning), hyponatremia, abdominal pain, diarrhea, bradycardia; avoid with serum Cr ≥5 mg/dL or ACLF grade 3 (less benefit, more harm)',
        'Cirrhotic with ascites and rising creatinine not improving after stopping diuretics and 2 days of albumin, bland urine → HRS-AKI → terlipressin + albumin; liver transplant is definitive.',
    ),
    'nicardipine': _dr(
        'IV dihydropyridine CALCIUM CHANNEL BLOCKER — arteriolar vasodilator, titratable infusion (onset 5–15 min); no significant negative inotropy or AV nodal effect',
        'HYPERTENSIVE EMERGENCY (aortic dissection with β-blocker first, ACUTE ISCHEMIC STROKE BP control before/after thrombolysis, intracerebral hemorrhage — SBP target ~140, subarachnoid hemorrhage, preeclampsia/eclampsia, postoperative HTN, sympathomimetic crisis); alternatives: clevidipine, labetalol, esmolol',
        'Reflex TACHYCARDIA, headache, flushing, hypotension, phlebitis (peripheral IV — change site every 12 h), nausea; caution in aortic stenosis and acute HF (no inotropic support)',
        'Hypertensive emergency: lower MAP by no more than ~ 25% in the first hour (except aortic dissection — SBP <120 in 20 min with β-blocker first; acute ischemic stroke — only if >220/120 or <185/110 for tPA; ICH — SBP 140–160).',
    ),
    'potassium chloride': _dr(
        'Potassium replacement (oral or IV); chloride corrects associated hypochloremic metabolic alkalosis',
        'HYPOKALEMIA (and prevention with diuretics), DKA (add 20–40 mEq/L to fluids when K 3.5–5.3 and urine output adequate; if K <3.5 → replace BEFORE insulin), metabolic alkalosis (saline-responsive — vomiting/NG suction), digoxin toxicity with hypokalemia',
        'HYPERKALEMIA (arrhythmias — especially renal failure, ACEi/ARB, K-sparing diuretics, trimethoprim, NSAIDs), PHLEBITIS/pain with peripheral IV (max ~ 10 mEq/h peripheral, ≤20–40 mEq/h central with cardiac monitoring — NEVER IV push → cardiac arrest), GI irritation/ulceration and pill esophagitis (oral — take with water/food, upright)',
        'Each 10 mEq raises serum K ~ 0.1 mEq/L (more when K is very low). Replace MAGNESIUM concurrently (refractory hypokalemia). Oral route preferred when possible. Avoid dextrose-containing carrier fluids in severe hypokalemia (insulin shift).',
    ),
    'hypertonic saline': _dr(
        '3% NaCl (513 mEq/L) or 23.4% (central line only) — raises serum sodium and plasma osmolality → osmotic water shift out of cells (↓cerebral edema)',
        'SEVERE SYMPTOMATIC HYPONATREMIA (seizures, coma, severe confusion, vomiting): 3% NaCl 100–150 mL bolus over 10–20 min, repeat up to 2–3 times until symptoms improve (goal ↑Na 4–6 mEq/L in first hours), then limit correction to ≤8 mEq/L/24 h in high-risk; ↑INTRACRANIAL PRESSURE/cerebral edema (TBI, herniation — alternative to mannitol, preferred if hypotensive); hyponatremia from exercise-associated causes',
        'OSMOTIC DEMYELINATION SYNDROME with overcorrection of CHRONIC hyponatremia (>48 h) — especially alcohol use disorder, malnutrition, hypokalemia, liver disease, Na <105 (correct ≤8 mEq/L/24 h; if overcorrected, re-lower with D5W ± desmopressin), volume overload/pulmonary edema, hyperchloremic acidosis, phlebitis (3% may be given peripherally with caution)',
        'Seizing patient with Na 112 → 3% saline bolus now (acute symptoms trump correction-rate concerns), then slow. Asymptomatic chronic hyponatremia (SIADH) → fluid restriction, not hypertonic saline. Normal saline can WORSEN hyponatremia in SIADH.',
    ),
    'hydroxyzine': _dr(
        'First-generation (sedating) H1 ANTIHISTAMINE with anticholinergic and anxiolytic properties (metabolized to cetirizine)',
        'PRURITUS (urticaria, atopic dermatitis, pruritus of allergic origin), ANXIETY (non-addictive alternative to benzodiazepines for short-term/as-needed use), preoperative sedation, nausea',
        'SEDATION, anticholinergic effects (dry mouth, urinary retention, confusion — avoid in elderly: BEERS list), QT PROLONGATION (avoid with other QT drugs), tremor/seizures at high doses; avoid in early pregnancy',
        'As-needed anxiolytic without abuse potential (unlike benzodiazepines) — useful in substance use disorders; first-line chronic anxiety treatment remains SSRIs/SNRIs + CBT.',
    ),
    'cyproheptadine': _dr(
        'First-generation H1 antihistamine with potent SEROTONIN (5-HT2A) ANTAGONIST and anticholinergic activity',
        'SEROTONIN SYNDROME (moderate–severe — 12 mg PO/NG load, then 2 mg q2h; oral only) as an adjunct to stopping serotonergic drugs, benzodiazepines and cooling; allergic rhinitis/urticaria; appetite stimulation (off-label); SSRI-induced sexual dysfunction (off-label); cyclic vomiting/migraine prophylaxis in children',
        'Sedation, anticholinergic effects (urinary retention, dry mouth), ↑appetite/weight gain',
        'Serotonin syndrome (clonus, hyperreflexia, agitation, diaphoresis, diarrhea, hyperthermia after a new serotonergic drug) → stop drugs + benzodiazepines + cyproheptadine; NMS instead → dantrolene/bromocriptine.',
    ),
    'dantrolene': _dr(
        'Ryanodine receptor (RYR1) ANTAGONIST → blocks calcium release from the SARCOPLASMIC RETICULUM of skeletal muscle → muscle relaxation (direct-acting; not at NMJ)',
        'MALIGNANT HYPERTHERMIA (2.5 mg/kg IV rapid push, repeat up to 10 mg/kg — must be available wherever volatile anesthetics/succinylcholine are used); NEUROLEPTIC MALIGNANT SYNDROME (severe, with bromocriptine); chronic SPASTICITY (spinal cord injury, MS, cerebral palsy, stroke — oral)',
        'Muscle weakness, HEPATOTOXICITY (chronic oral use — monitor LFTs, boxed warning), sedation, phlebitis; dantrolene + verapamil → hyperkalemia/cardiovascular collapse (avoid CCBs)',
        'Rising end-tidal CO2, tachycardia, masseter rigidity and hyperthermia during anesthesia with sevoflurane/succinylcholine → malignant hyperthermia → stop trigger, 100% O2 hyperventilation, IV dantrolene, cool, treat hyperkalemia.',
    ),
    'vedolizumab': _dr(
        'Humanized monoclonal antibody against α4β7 INTEGRIN → blocks lymphocyte binding to MAdCAM-1 on GUT endothelium → GUT-SELECTIVE inhibition of leukocyte trafficking',
        'Moderate–severe ULCERATIVE COLITIS and CROHN DISEASE (induction and maintenance), including patients failing anti-TNF or wishing to avoid systemic immunosuppression (elderly, infection risk); pouchitis',
        'Nasopharyngitis, headache, arthralgia, infusion reactions; low systemic infection risk; PML risk theoretical (no confirmed cases — unlike NATALIZUMAB, which blocks α4 integrin systemically including the brain → PML from JC virus)',
        'IBD biologic options: anti-TNF (infliximab, adalimumab — screen TB/HBV; perianal fistulizing Crohn), vedolizumab (gut-selective, safest infection profile), ustekinumab/IL-23 inhibitors (risankizumab, mirikizumab, guselkumab), JAK inhibitors (tofacitinib, upadacitinib), S1P modulators (ozanimod, etrasimod) for UC.',
    ),
    'loperamide': _dr(
        'Peripherally acting μ-OPIOID receptor agonist (minimal CNS penetration — P-glycoprotein efflux at therapeutic doses) → ↓intestinal motility/secretion, ↑anal sphincter tone',
        "Symptomatic treatment of acute NON-BLOODY diarrhea (travelers' diarrhea ± single-dose antibiotic), chronic diarrhea (IBS-D, microscopic colitis, short bowel, bile acid diarrhea adjunct), fecal incontinence, high-output ostomy",
        "Constipation, abdominal cramps, ileus; AVOID with BLOODY diarrhea/fever (invasive pathogens — Shigella, EHEC, C. difficile → toxic megacolon/HUS risk), in children <2 years; MEGADOSES (abuse — 'poor man's methadone' for opioid withdrawal) → QT prolongation, torsades de pointes, ventricular arrhythmias, cardiac arrest",
        "Watery travelers' diarrhea → loperamide + azithromycin single dose if moderate–severe; bloody diarrhea with fever → antibiotics without loperamide. Massive loperamide ingestion with wide QRS/QT → opioid withdrawal self-treatment → cardiac monitoring.",
    ),
    'senna': _dr(
        'STIMULANT LAXATIVE (anthraquinone glycosides — sennosides) → activated by colonic bacteria → stimulates myenteric plexus/colonic motility and secretion; onset 6–12 h',
        "CONSTIPATION (occasional; OPIOID-INDUCED CONSTIPATION prophylaxis with every scheduled opioid — 'opioid + bowel regimen'), bowel preparation adjunct; often combined with docusate (stool softener — limited evidence) or osmotic laxatives (polyethylene glycol)",
        'Abdominal cramping, diarrhea, electrolyte disturbances (hypokalemia) with overuse, MELANOSIS COLI (benign brown-black pigmentation of colonic mucosa with chronic anthraquinone use — lipofuscin in macrophages), urine discoloration; avoid in bowel obstruction',
        'Stepwise constipation: fiber/fluids → osmotic (PEG — first-line, also for children) → stimulant (senna, bisacodyl) → secretagogues (lubiprostone, linaclotide, plecanatide, prucalopride); opioid-induced refractory → PAMORAs (methylnaltrexone, naloxegol). Brown pigmentation on colonoscopy in a chronic laxative user → melanosis coli.',
    ),
    'iron sucrose': _dr(
        'Intravenous IRON preparation (iron–sucrose complex; also ferric carboxymaltose, ferumoxytol, iron dextran, ferric derisomaltose) — bypasses GI absorption, rapid repletion of iron stores',
        'Iron deficiency anemia when oral iron is ineffective/not tolerated or absorption impaired: CKD (especially dialysis — with ESAs), IBD, celiac, post-bariatric surgery, ongoing blood loss, PREGNANCY (2nd/3rd trimester when oral fails or rapid repletion needed before delivery), heart failure with iron deficiency (↓hospitalization — ferritin <100 or 100–299 with TSAT <20%), chemotherapy-induced anemia with ESA',
        'Hypotension, infusion reactions (rare anaphylaxis — highest with older high-molecular-weight iron dextran; test dose), nausea, metallic taste, HYPOPHOSPHATEMIA (especially ferric carboxymaltose — FGF23; can cause osteomalacia with repeated doses), iron overload with excessive dosing; avoid during active bacteremia',
        'Oral iron is first-line (every-other-day dosing improves absorption; take with vitamin C, avoid with antacids/calcium/tea). Reticulocytes rise in ~ 7–10 days; hemoglobin ↑ ~ 1 g/dL per 2–3 weeks; continue 3 months after Hb normalizes to replete stores.',
    ),
    'epoetin alfa': _dr(
        'Recombinant human ERYTHROPOIETIN (erythropoiesis-stimulating agent — ESA; darbepoetin = longer-acting) → stimulates erythroid progenitor proliferation/differentiation in bone marrow',
        'ANEMIA of CKD (Hgb <10 g/dL; dialysis and non-dialysis) — target Hgb ~ 10–11.5 (NOT normal — higher targets ↑stroke, MI, death); chemotherapy-induced anemia (non-curative intent, Hb <10), zidovudine-induced anemia in HIV, reduction of transfusions in elective noncardiac surgery, lower-risk MDS with low EPO level',
        'HYPERTENSION (most common; can cause hypertensive encephalopathy/seizures), THROMBOSIS (VTE, stroke, MI, dialysis access thrombosis), ↑mortality/tumor progression in some cancers (boxed warning — use lowest dose to avoid transfusion), pure red cell aplasia (anti-EPO antibodies), headache, flu-like symptoms',
        'Before starting/during ESA therapy, ensure IRON REPLETE (ferritin >100–200 ng/mL, TSAT >20%; give IV iron in CKD) — iron deficiency is the most common cause of ESA hyporesponsiveness. EPO is also abused by endurance athletes (polycythemia, ↑Hct, thrombosis).',
    ),
    'prothrombin complex concentrate': _dr(
        'Plasma-derived concentrate of vitamin K–dependent clotting factors: 4-factor PCC (Kcentra — factors II, VII, IX, X + proteins C and S) — rapid, small-volume correction of factor deficiencies',
        'URGENT REVERSAL of WARFARIN (vitamin K antagonist) in major/life-threatening bleeding (intracranial hemorrhage, GI bleed with shock) or emergency surgery — ALWAYS with IV VITAMIN K 5–10 mg (PCC effect wanes in ~ 6–8 h); off-label reversal of factor Xa inhibitors (apixaban, rivaroxaban, edoxaban) when andexanet unavailable',
        'THROMBOEMBOLIC events (stroke, MI, DVT/PE — especially in patients anticoagulated for a thrombotic indication), DIC, allergic reactions, contains heparin (contraindicated in HIT); dosing by INR and weight',
        'Warfarin-associated ICH (INR 3.5) → 4F-PCC + IV vitamin K immediately (faster, less volume than FFP — which needs thawing, ABO typing, large volumes → TACO). Supratherapeutic INR without bleeding → hold warfarin ± oral vitamin K (INR >10).',
    ),
    'tolvaptan': _dr(
        "Selective VASOPRESSIN V2 RECEPTOR ANTAGONIST ('vaptan') at the collecting duct → ↓aquaporin-2 insertion → AQUARESIS (free-water excretion without sodium loss) → ↑serum sodium",
        'Euvolemic or hypervolemic HYPONATREMIA (SIADH, heart failure) — clinically significant (Na <125 or symptomatic despite fluid restriction), initiated in HOSPITAL with frequent Na monitoring; rapidly progressive AUTOSOMAL DOMINANT POLYCYSTIC KIDNEY DISEASE (slows cyst growth/eGFR decline — different dosing, REMS)',
        "OVERLY RAPID CORRECTION of sodium → osmotic demyelination (don't combine with hypertonic saline; avoid fluid restriction in first 24 h; monitor Na q6–8h), thirst, polyuria/pollakiuria, dry mouth, HEPATOTOXICITY (boxed — limit to 30 days for hyponatremia; avoid in liver disease/cirrhosis), hypovolemia; CYP3A4 substrate (avoid strong inhibitors); NOT for hypovolemic hyponatremia",
        'SIADH hyponatremia treatment ladder: fluid restriction (<800–1,000 mL/day) → salt tablets ± loop diuretic, oral urea → tolvaptan (hospital initiation, short-term); severe symptoms → hypertonic saline. Demeclocycline (nephrogenic DI-inducing) older option.',
    ),
}

_DRUG_BRAND_ALIASES = {
    "abilify": "aripiprazole",
    "acetadote": "n-acetylcysteine",
    "actigall": "ursodiol",
    "actos": "pioglitazone",
    "adderall": "amphetamine",
    "advair": "fluticasone-salmeterol",
    "advil": "ibuprofen",
    "aldactone": "spironolactone",
    "aleve": "naproxen",
    "altace": "ramipril",
    "amaryl": "glimepiride",
    "ancef": "cefazolin",
    "apresoline": "hydralazine",
    "aricept": "donepezil",
    "arixtra": "fondaparinux",
    "aspirin ec": "aspirin",
    "atacand": "candesartan",
    "ativan": "lorazepam",
    "augmentin": "amoxicillin-clavulanate",
    "avapro": "irbesartan",
    "avastin": "bevacizumab",
    "bactrim": "tmp-smx",
    "basaglar": "insulin glargine",
    "benadryl": "diphenhydramine",
    "benicar": "olmesartan",
    "biaxin": "clarithromycin",
    "brilinta": "ticagrelor",
    "bystolic": "nebivolol",
    "cancidas": "caspofungin",
    "cardizem": "diltiazem",
    "celebrex": "celecoxib",
    "celexa": "citalopram",
    "cellcept": "mycophenolate",
    "cipro": "ciprofloxacin",
    "claritin": "loratadine",
    "clozaril": "clozapine",
    "colace": "docusate",
    "colcrys": "colchicine",
    "compazine": "prochlorperazine",
    "concerta": "methylphenidate",
    "cordarone": "amiodarone",
    "coreg": "carvedilol",
    "corlanor": "ivabradine",
    "coumadin": "warfarin",
    "cozaar": "losartan",
    "crestor": "rosuvastatin",
    "cubicin": "daptomycin",
    "cymbalta": "duloxetine",
    "cytoxan": "cyclophosphamide",
    "ddavp": "desmopressin",
    "decadron": "dexamethasone",
    "depakote": "valproate",
    "diflucan": "fluconazole",
    "digox": "digoxin",
    "dilantin": "phenytoin",
    "dilaudid": "hydromorphone",
    "diovan": "valsartan",
    "dobutrex": "dobutamine",
    "dopamine hcl": "dopamine",
    "dulcolax": "bisacodyl",
    "duragesic": "fentanyl",
    "effexor": "venlafaxine",
    "effient": "prasugrel",
    "elavil": "amitriptyline",
    "eliquis": "apixaban",
    "enbrel": "etanercept",
    "entresto": "sacubitril-valsartan",
    "exelon": "rivastigmine",
    "farxiga": "dapagliflozin",
    "flagyl": "metronidazole",
    "flonase": "fluticasone",
    "florinef": "fludrocortisone",
    "fosamax": "alendronate",
    "geodon": "ziprasidone",
    "gleevec": "imatinib",
    "glucagon hcl": "glucagon",
    "glucophage": "metformin",
    "glucotrol": "glipizide",
    "haldol": "haloperidol",
    "herceptin": "trastuzumab",
    "humalog": "insulin lispro",
    "humira": "adalimumab",
    "imitrex": "sumatriptan",
    "imuran": "azathioprine",
    "inderal": "propranolol",
    "indocin": "indomethacin",
    "inspra": "eplerenone",
    "intropin": "dopamine",
    "invanz": "ertapenem",
    "invokana": "canagliflozin",
    "isordil": "isosorbide mononitrate",
    "januvia": "sitagliptin",
    "jardiance": "empagliflozin",
    "kayexalate": "sodium polystyrene sulfonate",
    "keflex": "cephalexin",
    "keppra": "levetiracetam",
    "keytruda": "pembrolizumab",
    "klonopin": "clonazepam",
    "lactulose": "lactulose",
    "lanoxin": "digoxin",
    "lantus": "insulin glargine",
    "lasix": "furosemide",
    "latuda": "lurasidone",
    "levaquin": "levofloxacin",
    "levophed": "norepinephrine",
    "lexapro": "escitalopram",
    "lipitor": "atorvastatin",
    "lopressor": "metoprolol",
    "lovenox": "enoxaparin",
    "lyrica": "pregabalin",
    "maxipime": "cefepime",
    "medrol": "methylprednisolone",
    "merrem": "meropenem",
    "micardis": "telmisartan",
    "milrinone lactate": "milrinone",
    "miralax": "polyethylene glycol",
    "mirapex": "pramipexole",
    "motrin": "ibuprofen",
    "ms contin": "morphine",
    "mucomyst": "n-acetylcysteine",
    "multaq": "dronedarone",
    "mycamine": "micafungin",
    "narcan": "naloxone",
    "neoral": "cyclosporine",
    "neosynephrine": "phenylephrine",
    "neupogen": "filgrastim",
    "neurontin": "gabapentin",
    "nexium": "esomeprazole",
    "nifedipine xl": "nifedipine",
    "nipride": "nitroprusside",
    "nitro-bid": "nitroglycerin",
    "nitroglycerin sl": "nitroglycerin",
    "norvasc": "amlodipine",
    "novolog": "insulin aspart",
    "nuvigil": "armodafinil",
    "opdivo": "nivolumab",
    "oxycontin": "oxycodone",
    "ozempic": "semaglutide",
    "pamelor": "nortriptyline",
    "paracetamol": "acetaminophen",
    "paxil": "paroxetine",
    "paxlovid": "nirmatrelvir-ritonavir",
    "penicillin vk": "penicillin g",
    "pepcid": "famotidine",
    "percocet": "oxycodone",
    "phenergan": "promethazine",
    "plaquenil": "hydroxychloroquine",
    "plavix": "clopidogrel",
    "pradaxa": "dabigatran",
    "prilosec": "omeprazole",
    "primaxin": "imipenem-cilastatin",
    "prinivil": "lisinopril",
    "prograf": "tacrolimus",
    "protonix": "pantoprazole",
    "provigil": "modafinil",
    "prozac": "fluoxetine",
    "ptu": "propylthiouracil",
    "pulmicort": "budesonide",
    "rapamune": "sirolimus",
    "reglan": "metoclopramide",
    "remeron": "mirtazapine",
    "remicade": "infliximab",
    "requip": "ropinirole",
    "risperdal": "risperidone",
    "ritalin": "methylphenidate",
    "rituxan": "rituximab",
    "rocephin": "ceftriaxone",
    "septra": "tmp-smx",
    "seroquel": "quetiapine",
    "sinemet": "levodopa",
    "singulair": "montelukast",
    "spiriva": "tiotropium",
    "sporanox": "itraconazole",
    "strattera": "atomoxetine",
    "suboxone": "buprenorphine",
    "sumatriptan": "sumatriptan",
    "symbicort": "budesonide-formoterol",
    "synthroid": "levothyroxine",
    "tamiflu": "oseltamivir",
    "tapazole": "methimazole",
    "tegretol": "carbamazepine",
    "tenormin": "atenolol",
    "tikosyn": "dofetilide",
    "toprol": "metoprolol",
    "toradol": "ketorolac",
    "toujeo": "insulin glargine",
    "trulicity": "dulaglutide",
    "tylenol": "acetaminophen",
    "tylenol #3": "codeine",
    "uloric": "febuxostat",
    "ultram": "tramadol",
    "unasyn": "ampicillin-sulbactam",
    "ursodiol": "ursodiol",
    "valium": "diazepam",
    "valtrex": "valacyclovir",
    "vancocin": "vancomycin",
    "vasotec": "enalapril",
    "veklury": "remdesivir",
    "verapamil sr": "verapamil",
    "versed": "midazolam",
    "vfend": "voriconazole",
    "vibramycin": "doxycycline",
    "victoza": "liraglutide",
    "vivitrol": "naltrexone",
    "vyvanse": "lisdexamfetamine",
    "wellbutrin": "bupropion",
    "xanax": "alprazolam",
    "xarelto": "rivaroxaban",
    "yervoy": "ipilimumab",
    "z-pack": "azithromycin",
    "zestril": "lisinopril",
    "zithromax": "azithromycin",
    "zofran": "ondansetron",
    "zoloft": "sertraline",
    "zosyn": "piperacillin-tazobactam",
    "zovirax": "acyclovir",
    "zpack": "azithromycin",
    "zyban": "bupropion",
    "zyloprim": "allopurinol",
    "zyprexa": "olanzapine",
    "zyrtec": "cetirizine",
    "zyvox": "linezolid",
    'pitocin': 'oxytocin',
    'methergine': 'methylergonovine',
    'hemabate': 'carboprost',
    'cervidil': 'dinoprostone',
    'prepidil': 'dinoprostone',
    'prostaglandin e2': 'dinoprostone',
    'pge2': 'dinoprostone',
    'cyklokapron': 'tranexamic acid',
    'lysteda': 'tranexamic acid',
    'txa': 'tranexamic acid',
    'celestone': 'betamethasone',
    'rhogam': 'rho(d) immune globulin',
    'rhig': 'rho(d) immune globulin',
    'anti-d': 'rho(d) immune globulin',
    'anti-d immunoglobulin': 'rho(d) immune globulin',
    'rh immune globulin': 'rho(d) immune globulin',
    'rho d immune globulin': 'rho(d) immune globulin',
    'winrho': 'rho(d) immune globulin',
    'brethine': 'terbutaline',
    'clomid': 'clomiphene',
    'clomiphene citrate': 'clomiphene',
    'femara': 'letrozole',
    'mifeprex': 'mifepristone',
    'korlym': 'mifepristone',
    'ru-486': 'mifepristone',
    'depo-provera': 'medroxyprogesterone',
    'dmpa': 'medroxyprogesterone',
    'provera': 'medroxyprogesterone',
    'depo provera': 'medroxyprogesterone',
    'medroxyprogesterone acetate': 'medroxyprogesterone',
    'plan b': 'levonorgestrel',
    'mirena': 'levonorgestrel',
    'liletta': 'levonorgestrel',
    'kyleena': 'levonorgestrel',
    'skyla': 'levonorgestrel',
    'lng-iud': 'levonorgestrel',
    'levonorgestrel iud': 'levonorgestrel',
    'hormonal iud': 'levonorgestrel',
    'nexplanon': 'etonogestrel implant',
    'implanon': 'etonogestrel implant',
    'contraceptive implant': 'etonogestrel implant',
    'etonogestrel': 'etonogestrel implant',
    'prometrium': 'progesterone',
    'makena': 'progesterone',
    '17-ohp caproate': 'progesterone',
    'hydroxyprogesterone caproate': 'progesterone',
    'vaginal progesterone': 'progesterone',
    'diclegis': 'doxylamine-pyridoxine',
    'bonjesta': 'doxylamine-pyridoxine',
    'doxylamine': 'doxylamine-pyridoxine',
    'pyridoxine': 'doxylamine-pyridoxine',
    'aldomet': 'methyldopa',
    'lupron': 'leuprolide',
    'leuprolide acetate': 'leuprolide',
    'myfembree': 'relugolix',
    'orgovyx': 'relugolix',
    'elagolix': 'relugolix',
    'orilissa': 'relugolix',
    'oriahnn': 'relugolix',
    'evista': 'raloxifene',
    'premarin': 'conjugated estrogens',
    'estradiol patch': 'conjugated estrogens',
    'estrogen therapy': 'conjugated estrogens',
    'veozah': 'fezolinetant',
    'elinzanetant': 'fezolinetant',
    'dostinex': 'cabergoline',
    'parlodel': 'bromocriptine',
    'cycloset': 'bromocriptine',
    'zurzuvae': 'zuranolone',
    'brexanolone': 'zuranolone',
    'zulresso': 'zuranolone',
    'prenatal vitamins': 'folic acid',
    'cytotec': 'misoprostol',
    'chantix': 'varenicline',
    'champix': 'varenicline',
    'nrt': 'nicotine replacement therapy',
    'nicotine patch': 'nicotine replacement therapy',
    'nicotine gum': 'nicotine replacement therapy',
    'nicotine lozenge': 'nicotine replacement therapy',
    'nicoderm': 'nicotine replacement therapy',
    'proscar': 'finasteride',
    'propecia': 'finasteride',
    'dutasteride': 'finasteride',
    'avodart': 'finasteride',
    'flomax': 'tamsulosin',
    'alpha blocker for bph': 'tamsulosin',
    'viagra': 'sildenafil',
    'revatio': 'sildenafil',
    'cialis': 'sildenafil',
    'tadalafil': 'sildenafil',
    'vardenafil': 'sildenafil',
    'ditropan': 'oxybutynin',
    'tolterodine': 'oxybutynin',
    'solifenacin': 'oxybutynin',
    'vesicare': 'oxybutynin',
    'trospium': 'oxybutynin',
    'myrbetriq': 'mirabegron',
    'vibegron': 'mirabegron',
    'gemtesa': 'mirabegron',
    'prolia': 'denosumab',
    'xgeva': 'denosumab',
    'lamisil': 'terbinafine',
    'elimite': 'permethrin',
    'bactroban': 'mupirocin',
    'flexeril': 'cyclobenzaprine',
    'antivert': 'meclizine',
    'ambien': 'zolpidem',
    'eszopiclone': 'zolpidem',
    'lunesta': 'zolpidem',
    'z-drugs': 'zolpidem',
    'ramelteon': 'melatonin',
    'rozerem': 'melatonin',
    'mounjaro': 'tirzepatide',
    'zepbound': 'tirzepatide',
    'zetia': 'ezetimibe',
    'repatha': 'evolocumab',
    'alirocumab': 'evolocumab',
    'praluent': 'evolocumab',
    'pcsk9 inhibitor': 'evolocumab',
    'inclisiran': 'evolocumab',
    'thalitone': 'chlorthalidone',
    'iron sulfate': 'ferrous sulfate',
    'oral iron': 'ferrous sulfate',
    'vitamin b12': 'cyanocobalamin',
    'b12 injection': 'cyanocobalamin',
    'vitamin d3': 'cholecalciferol',
    'tessalon': 'benzonatate',
    'tessalon perles': 'benzonatate',
    'ulipristal acetate': 'ulipristal',
    'gnrh agonist': 'leuprolide',
    'gnrh agonists': 'leuprolide',
    'aromatase inhibitor': 'letrozole',
    'aromatase inhibitors': 'letrozole',
    'osphena': 'ospemifene',
    'antabuse': 'disulfiram',
    'disulfiram reaction': 'disulfiram',
    'disulfiram-like reaction': 'disulfiram',
    'campral': 'acamprosate',
    'spravato': 'esketamine',
    'stimulants': 'methylphenidate',
    'stimulant': 'methylphenidate',
    'stimulant medication': 'methylphenidate',
    'acova': 'argatroban',
    'forteo': 'teriparatide',
    'abaloparatide': 'teriparatide',
    'tymlos': 'teriparatide',
    'pth analog': 'teriparatide',
    'xolair': 'omalizumab',
    'anti-ige': 'omalizumab',
    'dupixent': 'dupilumab',
    'beyfortus': 'nirsevimab',
    'synagis': 'palivizumab',
    'rsv monoclonal antibody': 'nirsevimab',
    'rsv immunoprophylaxis': 'nirsevimab',
    'exogenous surfactant': 'surfactant',
    'poractant alfa': 'surfactant',
    'beractant': 'surfactant',
    'curosurf': 'surfactant',
    'exjade': 'deferasirox',
    'jadenu': 'deferasirox',
    'iron chelation': 'deferasirox',
    'deferiprone': 'deferasirox',
    'ivig': 'intravenous immunoglobulin',
    'immune globulin': 'intravenous immunoglobulin',
    'iv immunoglobulin': 'intravenous immunoglobulin',
    'intravenous immune globulin': 'intravenous immunoglobulin',
    'diamox': 'acetazolamide',
    'carbonic anhydrase inhibitor': 'acetazolamide',
    'nimotop': 'nimodipine',
    'antizol': 'fomepizole',
    '4-methylpyrazole': 'fomepizole',
    'british anti-lewisite': 'dimercaprol',
    'dmsa': 'succimer',
    'chemet': 'succimer',
    '2-pam': 'pralidoxime',
    'protopam': 'pralidoxime',
    'terlivaz': 'terlipressin',
    'cardene': 'nicardipine',
    'clevidipine': 'nicardipine',
    'kcl': 'potassium chloride',
    'potassium replacement': 'potassium chloride',
    'k-dur': 'potassium chloride',
    '3% saline': 'hypertonic saline',
    '3% sodium chloride': 'hypertonic saline',
    '23.4% saline': 'hypertonic saline',
    'vistaril': 'hydroxyzine',
    'atarax': 'hydroxyzine',
    'periactin': 'cyproheptadine',
    'dantrium': 'dantrolene',
    'ryanodex': 'dantrolene',
    'entyvio': 'vedolizumab',
    'imodium': 'loperamide',
    'sennosides': 'senna',
    'senokot': 'senna',
    'melanosis coli': 'senna',
    'venofer': 'iron sucrose',
    'iv iron': 'iron sucrose',
    'intravenous iron': 'iron sucrose',
    'ferric carboxymaltose': 'iron sucrose',
    'injectafer': 'iron sucrose',
    'ferumoxytol': 'iron sucrose',
    'iron dextran': 'iron sucrose',
    'epo': 'epoetin alfa',
    'erythropoietin': 'epoetin alfa',
    'epogen': 'epoetin alfa',
    'procrit': 'epoetin alfa',
    'darbepoetin': 'epoetin alfa',
    'aranesp': 'epoetin alfa',
    'esa': 'epoetin alfa',
    'erythropoiesis-stimulating agent': 'epoetin alfa',
    'protamine': 'protamine sulfate',
    'pcc': 'prothrombin complex concentrate',
    '4f-pcc': 'prothrombin complex concentrate',
    'kcentra': 'prothrombin complex concentrate',
    'four-factor pcc': 'prothrombin complex concentrate',
    '4-factor prothrombin complex concentrate': 'prothrombin complex concentrate',
    'samsca': 'tolvaptan',
    'jynarque': 'tolvaptan',
    'vaptans': 'tolvaptan',
    'conivaptan': 'tolvaptan',
    'neo-synephrine': 'phenylephrine',
    'trimethoprim-sulfamethoxazole': 'tmp-smx',
    'trimethoprim/sulfamethoxazole': 'tmp-smx',
    'co-trimoxazole': 'tmp-smx',
    'phytonadione': 'vitamin k',
    'vitamin k1': 'vitamin k',
}
