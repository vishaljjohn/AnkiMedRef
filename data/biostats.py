"""Biostatistics (tier 0.5g).

Edit freely — see data/__init__.py for how files are loaded."""
from ..formatters import _bs


_BIOSTATS = {
    "sensitivity": _bs(
        "TP / (TP + FN)",
        "Probability of a positive test GIVEN disease is present; ability to detect true disease; measures how well a test finds cases",
        "High sensitivity → few False Negatives → best for RULING OUT disease (SnNout); used for screening tests; if sensitivity is 100%, a negative result rules out disease completely",
        "Mnemonic: SnNout — high Sensitivity, Negative result rules OUT disease"
    ),
    "specificity": _bs(
        "TN / (TN + FP)",
        "Probability of a negative test GIVEN disease is absent; ability to correctly exclude non-diseased; measures how well a test avoids false positives",
        "High specificity → few False Positives → best for RULING IN disease (SpPin); used for confirmatory tests; if specificity is 100%, a positive result rules in disease completely",
        "Mnemonic: SpPin — high Specificity, Positive result rules IN disease"
    ),
    "ppv": _bs(
        "TP / (TP + FP)",
        "Probability of having the disease GIVEN a positive test result; depends heavily on disease prevalence — increases when prevalence increases",
        "PPV rises with higher prevalence; same test in a low-prevalence population has lower PPV (more false positives relative to true positives); PPV is NOT a fixed property of the test",
        "PPV and NPV are prevalence-dependent; sensitivity and specificity are prevalence-independent"
    ),
    "positive predictive value": _bs(
        "TP / (TP + FP)",
        "Probability of having the disease GIVEN a positive test result; depends heavily on disease prevalence — increases when prevalence increases",
        "PPV rises with higher prevalence; same test in a low-prevalence population has lower PPV (more false positives relative to true positives); PPV is NOT a fixed property of the test",
        "PPV and NPV are prevalence-dependent; sensitivity and specificity are prevalence-independent"
    ),
    "npv": _bs(
        "TN / (TN + FN)",
        "Probability of NOT having disease GIVEN a negative test result; increases when prevalence decreases (more true negatives in low-prevalence populations)",
        "NPV falls with higher disease prevalence (more false negatives relative to true negatives); high-prevalence populations → lower NPV from a negative test",
        "A highly sensitive test has high NPV — good for screening; low prevalence → high NPV even with mediocre test"
    ),
    "negative predictive value": _bs(
        "TN / (TN + FN)",
        "Probability of NOT having disease GIVEN a negative test result; increases when prevalence decreases (more true negatives in low-prevalence populations)",
        "NPV falls with higher disease prevalence (more false negatives relative to true negatives); high-prevalence populations → lower NPV from a negative test",
        "A highly sensitive test has high NPV — good for screening; low prevalence → high NPV even with mediocre test"
    ),
    "likelihood ratio": _bs(
        "LR+ = sensitivity / (1 − specificity) | LR− = (1 − sensitivity) / specificity",
        "LR+ = how much more likely a positive test occurs in disease vs. no disease; LR− = how much less likely a negative test occurs in disease vs. no disease; not affected by prevalence",
        "LR >10 or <0.1 = large, meaningful shift in post-test probability; LR 2-5 = small shift; LR ~1 = useless test; use Fagan nomogram or multiply pre-test odds × LR to get post-test odds",
        "LR is the most clinically useful test characteristic — directly updates pre-test to post-test probability independent of prevalence"
    ),
    "nnt": _bs(
        "1 / ARR (Absolute Risk Reduction)",
        "Number of patients who must be treated to prevent one additional bad outcome; lower NNT = more effective treatment; NNH = 1/ARI (absolute risk increase) for harms",
        "NNT of 1 = perfect (every treated patient benefits); NNT of ∞ = no benefit; NNT and NNH must be interpreted in context of disease severity and treatment side effects",
        "NNT = 1/ARR; ARR = control event rate − treatment event rate; RRR = ARR/control event rate; high-risk populations have lower NNT (higher ARR)"
    ),
    "number needed to treat": _bs(
        "1 / ARR (Absolute Risk Reduction)",
        "Number of patients who must be treated to prevent one additional bad outcome; lower NNT = more effective treatment; NNH = 1/ARI (absolute risk increase) for harms",
        "NNT of 1 = perfect (every treated patient benefits); NNT of ∞ = no benefit; NNT and NNH must be interpreted in context of disease severity and treatment side effects",
        "NNT = 1/ARR; ARR = control event rate − treatment event rate; RRR = ARR/control event rate; high-risk populations have lower NNT (higher ARR)"
    ),
    "absolute risk reduction": _bs(
        "ARR = Control Event Rate − Treatment Event Rate",
        "Absolute difference in event rates between control and treated groups; takes into account baseline risk; most clinically meaningful measure of treatment effect",
        "ARR is more informative than RRR alone — a 50% RRR means very different things if baseline risk is 0.2% (ARR=0.1%, NNT=1000) vs. 20% (ARR=10%, NNT=10)",
        "Drug companies prefer to report RRR (sounds more impressive); clinicians should ask for ARR and NNT to evaluate real-world benefit"
    ),
    "arr": _bs(
        "ARR = Control Event Rate − Treatment Event Rate",
        "Absolute difference in event rates between control and treated groups; takes into account baseline risk; most clinically meaningful measure of treatment effect",
        "ARR is more informative than RRR alone — a 50% RRR means very different things if baseline risk is 0.2% (ARR=0.1%, NNT=1000) vs. 20% (ARR=10%, NNT=10)",
        "Drug companies prefer to report RRR (sounds more impressive); clinicians should ask for ARR and NNT to evaluate real-world benefit"
    ),
    "relative risk reduction": _bs(
        "RRR = ARR / Control Event Rate  =  1 − Relative Risk",
        "Proportional reduction in event rate compared to control group; does not reflect absolute magnitude of benefit; same RRR can mean very different NNTs depending on baseline risk",
        "If control event rate = 4% and treatment rate = 2%: ARR = 2%, RRR = 50%, NNT = 50; RRR always looks better than ARR — beware marketing of relative risk reductions",
        "RRR = ARR / control rate; RRR alone without baseline risk is misleading; always pair with ARR or NNT"
    ),
    "rrr": _bs(
        "RRR = ARR / Control Event Rate  =  1 − Relative Risk",
        "Proportional reduction in event rate compared to control group; does not reflect absolute magnitude of benefit; same RRR can mean very different NNTs depending on baseline risk",
        "If control event rate = 4% and treatment rate = 2%: ARR = 2%, RRR = 50%, NNT = 50; RRR always looks better than ARR — beware marketing of relative risk reductions",
        "RRR = ARR / control rate; RRR alone without baseline risk is misleading; always pair with ARR or NNT"
    ),
    "relative risk": _bs(
        "RR = Incidence in Exposed / Incidence in Unexposed  (used in cohort studies)",
        "Ratio of event rates between exposed and unexposed groups; used in prospective/cohort studies; RR=1 means no association; RR>1 = increased risk; RR<1 = protective",
        "RR cannot be calculated from case-control studies (no incidence data) — use odds ratio instead; RR is directly interpretable: RR=3 means 3× more likely to develop outcome if exposed",
        "Study type determines valid measure: cohort/RCT → RR; case-control → OR; cross-sectional → prevalence ratio"
    ),
    "odds ratio": _bs(
        "OR = (Exposed cases / Unexposed cases) / (Exposed controls / Unexposed controls)  (used in case-control studies)",
        "Ratio of odds of exposure in cases vs. controls; used when incidence cannot be measured (case-control studies); approximates RR when disease prevalence is low (<10%)",
        "OR overestimates RR when disease prevalence is high (>10%); OR=1 means no association; OR>1 = increased odds of disease given exposure; always report 95% CI — if CI crosses 1, result is not statistically significant",
        "Case-control studies start with OUTCOME and look backward at exposure; cannot calculate incidence → cannot calculate RR directly; OR ≈ RR when prevalence is low"
    ),
    "attributable risk": _bs(
        "AR = Incidence in Exposed − Incidence in Unexposed  (same formula as ARR)",
        "Absolute excess risk due to a specific exposure; how many cases of disease are attributable to the exposure alone; public health measure of exposure impact",
        "Attributable risk percent (AR%) = AR / incidence in exposed × 100 = proportion of disease in exposed group attributable to the exposure; population attributable risk considers prevalence of exposure",
        "Useful for public health policy — how much disease would be prevented if exposure was eliminated; different from RR which is a ratio measure"
    ),
    "incidence": _bs(
        "New cases / Population at risk × Time period",
        "Rate of new disease onset in a population over a defined time period; measures disease occurrence; used in cohort and prospective studies",
        "Incidence rate (person-time denominator) vs. cumulative incidence (proportion); rising incidence can reflect true increase in disease OR improved detection; incidence ≠ prevalence",
        "Incidence = new cases (flow); Prevalence = existing cases (pool); Prevalence ≈ Incidence × Duration for stable diseases"
    ),
    "prevalence": _bs(
        "Existing cases / Total population at one point in time",
        "Proportion of a population with a condition at a specific point in time; measures disease burden; affected by incidence AND disease duration (recovery + death)",
        "Prevalence increases with: longer disease duration, decreased mortality (chronic diseases), in-migration of cases; decreases with: effective treatment, high case fatality, out-migration; point prevalence vs. period prevalence",
        "Prevalence ≈ Incidence × Duration; high prevalence despite low incidence = chronic disease (e.g., diabetes); low prevalence despite high incidence = short/fatal disease (e.g., Ebola)"
    ),
    "p-value": _bs(
        "Probability of observing results as extreme as those found (or more extreme) if the null hypothesis were true",
        "p < 0.05 = statistically significant (reject null hypothesis); p ≥ 0.05 = fail to reject null; does NOT measure effect size, clinical significance, or probability that null hypothesis is true",
        "p-value depends on sample size — large studies can make clinically meaningless differences statistically significant; small studies may miss clinically important differences (underpowered); always interpret p-value alongside effect size and confidence interval",
        "p-value ≠ probability null hypothesis is true; statistically significant ≠ clinically significant; convention of 0.05 is arbitrary (Fisher)"
    ),
    "confidence interval": _bs(
        "Range of values within which the true population parameter lies with a stated probability (typically 95%)",
        "95% CI: if the study were repeated 100 times, 95 of those intervals would contain the true value; narrower CI = more precise estimate (larger sample size); CI that crosses the null value (1 for ratios, 0 for differences) = not statistically significant",
        "95% CI roughly corresponds to p < 0.05 for statistical significance; CI provides more information than p-value alone (direction + magnitude + precision of effect); non-overlapping CIs = statistically significant difference",
        "Wider CI = less precise (small sample, high variance); CI crosses 1.0 for RR/OR or 0 for differences = p > 0.05; always report CI with effect estimates"
    ),
    "type i error": _bs(
        "Alpha (α) error — Rejecting a TRUE null hypothesis (false positive)",
        "Concluding there IS an effect when there actually is NOT; alpha is set by investigator (conventionally 0.05 = 5% chance of false positive); lowering alpha reduces type I error but increases type II error",
        "Multiple comparisons increase type I error risk — Bonferroni correction divides alpha by number of comparisons; p-value threshold of 0.05 means 1 in 20 significant results by chance alone when null is true",
        "Type I = False Positive; Type II = False Negative; Alpha = acceptable false positive rate; Beta = acceptable false negative rate; Power = 1 − Beta"
    ),
    "type ii error": _bs(
        "Beta (β) error — Failing to reject a FALSE null hypothesis (false negative)",
        "Concluding there is NO effect when there actually IS one; beta conventionally set at 0.20 (20% chance of false negative); power = 1 − beta = probability of detecting a true effect",
        "Underpowered studies (small sample size) → high type II error rate; increasing sample size, effect size, or alpha reduces type II error; type II error common in negative trials of beneficial treatments",
        "Power = 1 − β; power of 80% = 20% chance of missing a real effect; to reduce type II error: increase sample size, increase effect size, increase alpha, reduce variability"
    ),
    "power": _bs(
        "1 − β (Beta); Probability of detecting a TRUE effect when one exists",
        "Ability of a study to find a statistically significant result when the null hypothesis is actually false; conventional power = 80% (β = 0.2); power depends on sample size, effect size, alpha level, and variance",
        "Factors that increase power: larger sample size (most modifiable), larger true effect size, higher alpha (lower bar for significance), lower variance, one-tailed vs. two-tailed test; underpowered studies are major source of false-negative results",
        "A negative study result is only meaningful if the study had adequate power to detect a clinically relevant difference; always assess power/sample size calculation in study design"
    ),
    "lead-time bias": _bs(
        "Survival appears longer with screening but only because disease is detected earlier — not because patients actually live longer",
        "Classic bias in cancer screening studies; survival measured from diagnosis — earlier diagnosis adds time at the front end without extending life; makes screening appear effective when it may not be",
        "Example: lung cancer detected at stage I by screening appears to have 5-year survival of 80% vs. 15% for symptomatic detection; but if the patient dies at the same time regardless, screening only extended the period of 'having known cancer,' not actual lifespan",
        "Solution: measure mortality rates in population (not survival from diagnosis) to assess true screening benefit; all-cause mortality or disease-specific mortality endpoints are unaffected by lead-time bias"
    ),
    "length-time bias": _bs(
        "Screening preferentially detects slow-growing (indolent) tumors — making screened cancers appear less lethal than unscreened cancers",
        "Tumors with longer preclinical phase (slow-growing) spend more time in the window where screening can detect them; aggressive fast-growing tumors progress quickly from preclinical to symptomatic phase — often missed by periodic screening",
        "Example: screen-detected breast cancers appear to have better prognosis than interval cancers — partly because screening catches the slow indolent tumors more often; gives false impression of screening efficacy",
        "Both lead-time AND length-time biases cause overestimation of screening benefits; need RCT with mortality endpoint to prove screening truly saves lives"
    ),
    "recall bias": _bs(
        "Cases more likely to remember/report past exposures than controls — systematic over-reporting of exposure in case group",
        "Common in retrospective case-control studies; cases (who have disease) may search their memory harder for possible causes; mothers of children with birth defects more likely to recall medication exposures than mothers of healthy children",
        "Solution: use objective records instead of self-report (medical records, biological samples); use prospective cohort designs; verify exposure history with medical records",
        "Recall bias → overestimation of OR in case-control studies; opposite can also occur (differential under-reporting in controls); systematic, not random error → cannot be corrected by increasing sample size"
    ),
    "selection bias": _bs(
        "Systematic error in how study participants are selected — exposed and unexposed groups differ in ways other than the exposure of interest",
        "Leads to a study sample that is not representative of the target population; types include: healthy worker effect, Berkson's bias (hospital-based case-control studies), non-response bias, volunteer bias, attrition/loss to follow-up bias",
        "Berkson's bias: hospitalized patients have different disease spectrum than community — hospital-based case-control studies may show spurious associations; healthy worker effect: employed workers healthier than general population → underestimates occupational hazards",
        "Solution: random sampling from well-defined population; minimize loss to follow-up (<20% rule of thumb); intention-to-treat analysis for RCTs; cannot be corrected statistically after the fact"
    ),
    "confounding": _bs(
        "A third variable associated with BOTH the exposure AND the outcome — creates a spurious or masked association between exposure and outcome",
        "Confounder must be: associated with exposure, independently associated with outcome, not on causal pathway between exposure and outcome; example: smoking is a confounder in coffee-heart disease studies (smokers drink more coffee AND have more heart disease)",
        "Prevention: randomization (RCTs eliminate confounding), restriction, matching, stratification; Analysis: multivariate regression, propensity score matching, Mantel-Haenszel method; cannot be fully controlled in observational studies — only RCTs eliminate unknown confounders",
        "Confounding ≠ effect modification (interaction); effect modification = exposure has different effect in different subgroups (biological phenomenon, not a bias); confounding = statistical distortion to be controlled"
    ),
    "intention to treat": _bs(
        "Analyze all participants as randomized, regardless of protocol adherence, treatment received, or dropout status",
        "Preserves the benefits of randomization (maintains comparability of groups); prevents bias from selective dropout or non-adherence; reflects real-world effectiveness (not just efficacy under ideal conditions); reduces type I error",
        "Conservative approach — tends to underestimate true treatment effect (diluted by non-adherent participants); per-protocol analysis (only analyzes adherent participants) gives efficacy estimate but is vulnerable to selection bias; both should be reported",
        "ITT = all randomized patients analyzed in original group; per-protocol = only adherent patients; as-treated = analyzed by treatment actually received; ITT is gold standard for primary analysis in RCTs"
    ),
    "number needed to harm": _bs(
        "NNH = 1 / ARI (Absolute Risk Increase)",
        "Number of patients who must be treated (or exposed) before one additional harmful outcome occurs; higher NNH = safer treatment; must weigh NNT vs. NNH to assess risk-benefit ratio",
        "If NNT = 20 (one benefit per 20 treated) and NNH = 200 (one harm per 200 treated), benefit clearly outweighs harm for most patients; if NNH approaches NNT, risk-benefit assessment becomes critical",
        "NNH = 1/ARI; ARI = treatment event rate − control event rate (for adverse outcomes); clinical decision-making requires both NNT and NNH in same units and timeframe"
    ),
    "kappa statistic": _bs(
        "κ = (Observed agreement − Expected agreement) / (1 − Expected agreement)",
        "Measures inter-rater reliability accounting for chance agreement; κ = 1.0 perfect agreement; κ = 0 agreement no better than chance; κ < 0 agreement worse than chance",
        "Interpretation: κ < 0.20 slight; 0.21-0.40 fair; 0.41-0.60 moderate; 0.61-0.80 substantial; 0.81-1.0 almost perfect agreement; used for categorical outcomes (vs. Pearson's r for continuous)",
        "Useful in assessing diagnostic reliability (e.g., pathologist agreement on biopsy reading); does not account for degree of disagreement — weighted kappa used for ordinal data"
    ),
    "hawthorne effect": _bs(
        "Participants change their behavior because they know they are being observed or studied",
        "Leads to overestimation of treatment effects in unblinded studies; subjects in clinical trials may adhere better, exercise more, or eat better simply because they are being monitored",
        "Solution: blinding (single, double, triple); placebo controls; minimizing contact between investigators and participants; Hawthorne effect affects both treatment and control groups but may be differential",
        "Named after Western Electric Hawthorne Works studies; leads to performance bias — differential behavior change between groups based on awareness of group assignment"
    ),
    "placebo effect": _bs(
        "Perceived or actual improvement in symptoms from an inert treatment believed to be active",
        "Real, measurable physiological and psychological responses to placebo; magnitude varies by condition (largest in pain, depression, nausea; smaller in objective outcomes like tumor shrinkage); related to patient expectation, provider enthusiasm, treatment ritual",
        "Nocebo effect = placebo's opposite — harm from inert treatment believed to be harmful (side effects from placebo in clinical trials); placebo effect strongest when: condition is subjective, provider is enthusiastic, treatment is elaborate",
        "Reason RCTs require placebo-controlled design — active treatment effect = total effect − placebo effect; open-label studies overestimate treatment benefits"
    ),


    "rct": _bs(
        "Randomized Controlled Trial",
        "Gold standard for establishing causation; participants randomly assigned to intervention or control; minimizes confounding (known + unknown); blinding (single/double/triple) reduces bias; limitations: expensive, time-consuming, ethical constraints, Hawthorne effect, may not generalize (external validity)",
        "Hierarchy of evidence: RCT > cohort > case-control > cross-sectional > case series > expert opinion. ITT analysis: analyzes all randomized participants in assigned group regardless of adherence — preserves randomization, more conservative. Per-protocol: only analyzes adherent participants — overestimates efficacy"
    ),
    "cohort study": _bs(
        "Prospective (or retrospective) observational study following exposed vs unexposed groups over time",
        "Prospective: follow forward from exposure to outcome; good for rare exposures; can calculate incidence and relative risk (RR); multiple outcomes per study. Retrospective: uses existing records; faster, cheaper but relies on data quality. Limitations: selection bias, loss to follow-up, expensive for rare outcomes",
        "Calculates RR (not OR). Best for: rare exposures, multiple outcomes, establishing temporality. Cannot prove causation (no randomization). Example: Framingham Heart Study"
    ),
    "case-control study": _bs(
        "Retrospective observational study: cases (disease) vs controls (no disease), comparing prior exposure",
        "Select cases and controls, then look BACK at exposure history; efficient for rare diseases or long latency periods; calculates odds ratio (OR) — approximates RR when disease is rare (rare disease assumption); limitations: recall bias (cases remember exposures better), selection of appropriate controls (critical), cannot calculate incidence",
        "Key concept: OR = (a×d)/(b×c) in 2×2 table. Recall bias is the biggest threat. Matching controls to cases controls confounding. Best study design for rare diseases (e.g., studying angiosarcoma + vinyl chloride)"
    ),
    "cross-sectional study": _bs(
        "Snapshot study: exposure and outcome measured simultaneously in a population at one point in time",
        "Prevalence study — describes disease frequency and associations; calculates prevalence ratio or prevalence OR; fast, cheap, good for hypothesis generation; cannot establish temporality (cannot determine if exposure preceded disease); limitations: prevalence-incidence bias (surviving cases only), not good for rare diseases or diseases with short duration",
        "Calculates prevalence (not incidence or RR). 'Chicken and egg problem' — cannot establish causation. Good for: planning health services, screening program design, hypothesis generation"
    ),
    "hazard ratio": _bs(
        "HR = instantaneous rate of events in exposed / rate in unexposed",
        "Time-to-event (survival analysis) analog of relative risk; estimated by Cox proportional hazards regression; HR = 1 (no difference), <1 (protective), >1 (harmful); proportional hazards assumption: HR constant over time; interpretation: 'at any given time, the hazard of the event is X times higher in the exposed group'",
        "Unlike RR (cumulative), HR is an instantaneous rate ratio. Kaplan-Meier curves visualize survival data; log-rank test compares survival curves. Censoring: patients who don't experience event by study end are 'censored' — still contribute data up to that point"
    ),
    "meta-analysis": _bs(
        "Quantitative pooling of results from multiple studies to produce a single summary estimate",
        "Steps: PICO question → systematic search → study selection (inclusion/exclusion) → data extraction → assess heterogeneity (I² statistic: <25% low, 25-75% moderate, >75% high) → fixed-effects (assumes one true effect) or random-effects (allows effect size to vary) model → forest plot; funnel plot for publication bias (Egger's test)",
        "Systematic review without pooling = qualitative synthesis. Publication bias (positive results more likely published) inflates effect sizes. GRADE framework rates quality of evidence. Forest plot: each study = horizontal line (95% CI) + box (weight); diamond = pooled effect. I² >50% → substantial heterogeneity → interpret pooled estimate cautiously"
    ),
    "bradford hill criteria": _bs(
        "9 criteria for assessing causality in epidemiological associations (not all required)",
        "1. Strength of association (large OR/RR more likely causal); 2. Consistency (replicated in different settings); 3. Specificity (one cause → one disease); 4. Temporality (exposure precedes disease — ONLY essential criterion); 5. Biological gradient (dose-response); 6. Plausibility (biological mechanism); 7. Coherence (consistent with known facts); 8. Experiment (reversible with removal of exposure); 9. Analogy (similar cause-effect relationships exist)",
        "Temporality is the ONLY required criterion. Classic application: smoking and lung cancer (1964 Surgeon General's report). Does NOT prove causation but strengthens causal inference. Specificity is the weakest criterion (many causes → one disease is common)"
    ),
    "kaplan-meier": _bs(
        "Non-parametric method for estimating survival function over time",
        "Plots probability of surviving beyond time t; step-function that drops at each event; censored observations (+) shown on curve but don't count as events; each step = event occurrence; allows comparison of survival between groups; analyzed by log-rank test (tests if curves are statistically different overall)",
        "Median survival: time at which 50% of subjects have experienced event. Assumptions: censoring random (non-informative), survival probabilities apply to all enrolled at that time, no time trend in enrollment. Limitations: no covariate adjustment (use Cox regression for that)"
    ),
    "ecological study": _bs(
        "Observational study where unit of analysis is a group (population), not an individual",
        "Compares disease rates across populations with different exposures (e.g., countries with different salt intake and CVD mortality); fast, cheap, uses existing aggregate data; generates hypotheses; cannot control individual-level confounders",
        "Ecological fallacy (ecological correlation ≠ individual-level association): assuming group-level relationship applies to individuals. Example: countries with more TVs per capita have lower cancer rates — confounded by wealth. Cannot establish individual causation"
    ),
    "nnh": _bs(
        "NNH = 1 / Absolute Risk Increase (ARI)",
        "Number of patients who must receive an intervention for ONE additional patient to be harmed; inverse of absolute risk increase (ARI = risk in exposed − risk in unexposed); higher NNH = safer intervention; compare NNT vs NNH to assess benefit-harm balance",
        "If ARI = 0.02 (2% excess risk), NNH = 50. Decision: if NNT &lt; NNH → likely net benefit. ARR = risk_control − risk_treatment; ARI = risk_treatment − risk_control. Both NNT and NNH depend on baseline risk → change in different populations"
    ),
    'standard deviation': _bs(
        'SD = √[Σ(x − mean)² / (n − 1)]',
        'Spread of individual values around the mean',
        'Normal distribution: ±1 SD contains 68%, ±2 SD 95%, ±3 SD 99.7% of values; reported with the mean to describe a sample',
        'SD describes the spread of the data; SEM (SD/√n) describes how precisely the mean is estimated and is always smaller',
    ),
    'standard error of the mean': _bs(
        'SEM = SD / √n',
        'How far the sample mean is likely to be from the true population mean',
        'Shrinks as the sample grows; used to build confidence intervals: 95% CI ≈ mean ± 1.96 × SEM',
        'Larger n → smaller SEM → narrower CI → more precise estimate (SD does not shrink with n)',
    ),
    'normal distribution': _bs(
        'Mean = median = mode',
        'Symmetric, bell-shaped (Gaussian) distribution',
        "68-95-99.7 rule for ±1, 2 and 3 SD; many lab reference ranges are set at mean ± 2 SD, so 5% of healthy people fall outside the 'normal' range",
        'Bimodal distribution (two peaks) suggests two populations, e.g. fast vs slow acetylators',
    ),
    'positive skew': _bs(
        'Mean > median > mode',
        'Asymmetric distribution with a long tail to the right (high values)',
        'Common for income, hospital length of stay and many lab values; the mean is pulled toward the tail, so the median is the better summary',
        'Skew is named for the tail: positive = tail to the right; negative = tail to the left (mean &lt; median &lt; mode)',
    ),
    'negative skew': _bs(
        'Mean &lt; median &lt; mode',
        'Asymmetric distribution with a long tail to the left (low values)',
        'Examples: age at death in high-income countries, scores on an easy exam',
        'The mode sits at the peak and the mean is dragged into the tail',
    ),
    't-test': _bs(
        't = (mean₁ − mean₂) / SE of the difference',
        'Compares the MEANS of two groups (continuous outcome)',
        'Unpaired t-test: two separate groups; paired t-test: the same subjects before vs after; assumes roughly normal data — non-parametric alternatives: Mann-Whitney U (unpaired), Wilcoxon signed-rank (paired)',
        '2 groups → t-test; ≥3 groups → ANOVA; categorical outcomes → chi-square',
    ),
    'anova': _bs(
        'F = variance between groups / variance within groups',
        'Analysis of variance — compares the MEANS of three or more groups',
        'A significant F means at least one mean differs; post-hoc tests (Tukey, Bonferroni) find which; running many t-tests instead inflates the type I error rate',
        'ANOVA = 3+ groups with a continuous outcome',
    ),
    'chi-square test': _bs(
        'χ² = Σ (observed − expected)² / expected',
        'Compares PROPORTIONS of a categorical variable between two or more groups (contingency table)',
        "Needs expected counts ≥5 per cell — use Fisher's exact test for small samples; tests association, not its strength or direction",
        'Chi-square = categories (e.g. % smokers with vs without lung cancer); t-test/ANOVA = means',
    ),
    'correlation coefficient': _bs(
        'Pearson r ranges from −1 to +1',
        'Strength and direction of a LINEAR relationship between two continuous variables',
        "+1 perfect positive, −1 perfect negative, 0 no linear relationship; r² (coefficient of determination) = proportion of variance explained; Spearman's rho for ranked or non-normal data",
        'Correlation does not prove causation — confounding and reverse causality remain possible',
    ),
    'pre-test probability': _bs(
        'Pre-test odds = probability / (1 − probability)',
        'Probability that the patient has the disease BEFORE the test result is known (prevalence + clinical findings)',
        'Post-test odds = pre-test odds × likelihood ratio; post-test probability = odds / (1 + odds); the Fagan nomogram does this graphically',
        'The same result means different things in different patients — a positive test with low pre-test probability may still be a false positive',
    ),
    'post-test probability': _bs(
        'Post-test odds = pre-test odds × LR; probability = odds / (1 + odds)',
        'Probability of disease AFTER the test result is known',
        'Positive result: use LR+ = sensitivity / (1 − specificity); negative result: LR− = (1 − sensitivity) / specificity; after a positive result the post-test probability equals the PPV',
        'LR+ >10 or LR− <0.1 cause large, often conclusive shifts in probability',
    ),
    'roc curve': _bs(
        'Sensitivity (true-positive rate) plotted against 1 − specificity (false-positive rate) across all cut-offs',
        'Receiver operating characteristic curve — the trade-off between sensitivity and specificity of a test',
        'Area under the curve (AUC): 0.5 = chance, 1.0 = perfect; the best cut-off lies closest to the upper-left corner',
        'Lowering the cut-off for a positive test → ↑sensitivity, ↓specificity, more false positives',
    ),
    'publication bias': _bs(
        '—',
        'Studies with positive or significant results are more likely to be published than null studies',
        'Distorts meta-analyses toward exaggerated effects; detected with funnel plots (asymmetry); reduced by mandatory trial registration',
        'Funnel-plot asymmetry is the classic sign of publication bias',
    ),
    'observer bias': _bs(
        '—',
        'Measurement bias when the person assessing outcomes knows the exposure or treatment group',
        'Prevented by blinding outcome assessors (double-blind design) and using objective outcome measures',
        "Pygmalion effect: the researcher's belief in a treatment influences the result; Hawthorne effect: subjects change behavior because they are watched",
    ),
    'attrition bias': _bs(
        '—',
        'Systematic differences between groups in who drops out or is lost to follow-up',
        'Common in long cohort studies and RCTs; limited by intention-to-treat analysis and maximizing follow-up; >20% loss to follow-up threatens validity',
        'If dropouts differ in prognosis from those who stay, results are biased even with randomization',
    ),
    'crossover study': _bs(
        '—',
        'Each participant receives both treatments in sequence (randomized order) with a washout period between',
        'Subjects act as their own controls, so fewer are needed; unsuitable for curable conditions or treatments with lasting effects; carry-over is the main threat',
        "The washout period must be long enough for the first treatment's effect to disappear",
    ),
    'non-inferiority trial': _bs(
        'Upper bound of the CI for the difference must stay within a pre-set margin (Δ)',
        'Trial designed to show a new treatment is NOT unacceptably worse than an existing one',
        'Used when the new treatment has other advantages (oral vs IV, fewer side effects, cost); per-protocol results are also checked because ITT can bias toward non-inferiority',
        'Example: DOAC trials vs warfarin (ROCKET-AF, ARISTOTLE) tested non-inferiority first, then superiority',
    ),
    'clinical trial phases': _bs(
        'Phase 0 → I → II → III → IV',
        'Stages of drug testing in humans',
        'Phase I: small number of healthy volunteers (or patients) — safety, dosing, pharmacokinetics; Phase II: patients — efficacy and side effects, dose-finding; Phase III: large RCT vs standard care/placebo → approval; Phase IV: post-marketing surveillance for rare/long-term adverse effects',
        'Phase I: is it safe? Phase II: does it work? Phase III: is it better? Phase IV: does it stay safe?',
    ),
    'case fatality rate': _bs(
        'Deaths from the disease / people with the disease (× 100)',
        'Proportion of people diagnosed with a disease who die from it within a set period',
        'Measures severity; differs from mortality rate (deaths / whole population) — a rare but deadly disease has a high case fatality rate and a low mortality rate',
        'Early in outbreaks the case fatality rate is often overestimated because mild cases are missed',
    ),
    'mortality rate': _bs(
        'Deaths in a period / population at risk (often per 1000 or 100,000 per year)',
        'Frequency of death in a defined population over a set time',
        'Crude vs age-adjusted rates (standardization allows comparison of populations with different age structures); infant mortality = infant deaths / 1000 live births; maternal mortality = per 100,000 live births',
        'Mortality rate ≠ case fatality rate (whole population vs only those with the disease)',
    ),
}
