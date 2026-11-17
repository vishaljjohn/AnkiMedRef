"""HTML formatters for the offline dictionaries in data/.

Each takes the fields of one entry and returns the tooltip HTML."""

_LAB_LBL = ('<span style="color:var(--mqr-lbl);font-size:11px;font-weight:600;'
            'text-transform:uppercase;letter-spacing:0.5px">')


def _dc(moa, members, uses, ci_adr, pearl=None):
    """Format a drug-class tooltip HTML block."""
    LBL = ('<span style="color:var(--mqr-lbl);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    def pill(m):
        return (f'<span style="display:inline-block;background:var(--mqr-pill-bg);'
                f'border:1px solid var(--mqr-border);border-radius:5px;padding:1px 7px;'
                f'margin:2px 2px 0 0;font-size:11px;color:var(--mqr-pill-fg)">{m}</span>')
    pills = "".join(pill(m) for m in members)
    rows = [
        f'{LBL}MOA</span> {moa}',
        f'{LBL}Members</span><br>{pills}',
        f'{LBL}Uses</span> {uses}',
        f'{LBL}CI / ADR</span> {ci_adr}',
    ]
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-pearl-bg);'
            f'border-left:3px solid var(--mqr-pearl-border);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-pearl-fg)"><b>Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _lr(ref_range, critical, high_means, low_means, units="", pearl=None):
    """Format a lab reference range tooltip HTML block."""
    LBL = _LAB_LBL
    CRIT = ('<span style="background:var(--mqr-crit-bg);color:var(--mqr-crit-fg);padding:1px 6px;'
            'border-radius:4px;font-size:11px;font-weight:600">')
    # Most ranges already end with their units ("3.5–5.0 mEq/L") — don't repeat them
    if units and units not in ref_range:
        ref_range = f"{ref_range} {units}"
    rows = [f'{LBL}Normal</span> {ref_range}']
    if critical:
        rows.append(f'{LBL}Critical</span> {CRIT}{critical}</span>')
    rows += [
        f'{LBL}↑ High</span> {high_means}',
        f'{LBL}↓ Low</span> {low_means}',
    ]
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-pearl-bg);'
            f'border-left:3px solid var(--mqr-pearl-border);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-pearl-fg)"><b>Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _bs(formula, definition, detail, pearl=None):
    """Format a biostatistics/epidemiology tooltip HTML block (teal scheme)."""
    LBL = ('<span style="color:var(--mqr-lbl-teal);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    rows = [
        f'{LBL}Formula</span> {formula}',
        f'{LBL}Definition</span> {definition}',
        f'{LBL}Detail</span> {detail}',
    ]
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-teal-bg);'
            f'border-left:3px solid var(--mqr-lbl-teal);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-teal-fg)"><b>Key Point:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _dr(moa, uses, adverse, pearl=None):
    """Format an individual drug tooltip HTML block (purple scheme)."""
    LBL = ('<span style="color:var(--mqr-lbl-purple);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    rows = [
        f'{LBL}MOA</span> {moa}',
        f'{LBL}Uses</span> {uses}',
        f'{LBL}Adverse</span> {adverse}',
    ]
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-purple-bg);'
            f'border-left:3px solid var(--mqr-lbl-purple);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-mn-fg)"><b>Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _dd(criteria, features, treatment, pearl=None):
    """Format a disease/condition tooltip HTML block."""
    LBL = ('<span style="color:var(--mqr-lbl);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    rows = [
        f'{LBL}Criteria / Dx</span> {criteria}',
        f'{LBL}Key Features</span> {features}',
        f'{LBL}Treatment</span> {treatment}',
    ]
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-pearl-bg);'
            f'border-left:3px solid var(--mqr-pearl-border);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-pearl-fg)"><b>Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _mo(gram_morph, virulence, diseases, treatment, pearl=None):
    """Format a microbiology organism tooltip HTML block."""
    LBL = ('<span style="color:var(--mqr-lbl);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    def tag(color, text):
        return (f'<span style="background:{color};border-radius:4px;padding:1px 6px;'
                f'font-size:11px;font-weight:600;margin-right:4px">{text}</span>')
    rows = [
        f'{LBL}Gram/Morph</span> {gram_morph}',
        f'{LBL}Virulence</span> {virulence}',
        f'{LBL}Diseases</span> {diseases}',
        f'{LBL}Treatment</span> {treatment}',
    ]
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-pearl-bg);'
            f'border-left:3px solid var(--mqr-pearl-border);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-pearl-fg)"><b>Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _ss(purpose, criteria, scoring, pearl=None):
    """Format a clinical scoring system tooltip HTML block."""
    LBL = ('<span style="color:var(--mqr-lbl);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    rows = [
        f'{LBL}Purpose</span> {purpose}',
        f'{LBL}Criteria</span> {criteria}',
        f'{LBL}Score</span> {scoring}',
    ]
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-pearl-bg);'
            f'border-left:3px solid var(--mqr-pearl-border);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-pearl-fg)"><b>Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _af(category, key_points, clinical_pearl):
    """Format an anatomy/physiology tooltip HTML block."""
    LBL = ('<span style="color:var(--mqr-lbl-amber);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    rows = [
        f'{LBL}Category</span> {category}',
        f'{LBL}Key Points</span> {key_points}',
    ]
    if clinical_pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-amber-bg);'
            f'border-left:3px solid var(--mqr-lbl-amber);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-amber-fg)"><b>Clinical Pearl:</b> {clinical_pearl}</div>'
        )
    return "<br>".join(rows)


def _sg(finding, indicates, pearl=None):
    """Format a clinical sign tooltip HTML block (rose scheme)."""
    LBL = ('<span style="color:var(--mqr-lbl-rose);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    rows = [
        f'{LBL}Finding</span> {finding}',
        f'{LBL}Indicates</span> {indicates}',
    ]
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-rose-bg);'
            f'border-left:3px solid var(--mqr-lbl-rose);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-rose-fg)"><b>Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _ob(topic, key_points, management, pearl=None):
    """Format an OB/GYN topic tooltip HTML block (rose scheme)."""
    LBL = ('<span style="color:var(--mqr-lbl-rose);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    rows = [
        f'{LBL}Topic</span> {topic}',
        f'{LBL}Key Points</span> {key_points}',
    ]
    if management:
        rows.append(f'{LBL}Management</span> {management}')
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-rose-bg);'
            f'border-left:3px solid var(--mqr-lbl-rose);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-rose-fg)"><b>Shelf Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)


def _pc(topic, key_points, management, pearl=None):
    """Format a primary-care topic tooltip HTML block (teal scheme)."""
    LBL = ('<span style="color:var(--mqr-lbl-teal);font-size:11px;font-weight:600;'
           'text-transform:uppercase;letter-spacing:0.5px">')
    rows = [f'{LBL}Topic</span> {topic}', f'{LBL}Key Points</span> {key_points}']
    if management:
        rows.append(f'{LBL}Management</span> {management}')
    if pearl:
        rows.append(
            f'<div style="margin-top:5px;padding:3px 7px;background:var(--mqr-teal-bg);'
            f'border-left:3px solid var(--mqr-lbl-teal);border-radius:3px;font-size:11px;'
            f'color:var(--mqr-teal-fg)"><b>Shelf Pearl:</b> {pearl}</div>'
        )
    return "<br>".join(rows)
