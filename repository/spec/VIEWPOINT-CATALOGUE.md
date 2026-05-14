# ZAF Viewpoint Catalogue
## ISO/IEC/IEEE 42010:2022 — Formal Viewpoint Definitions

**Framework:** ZenCloud Architecture Framework™ (ZAF)  
**Author:** Phil Myint / ZenCloud Global Consultants  
**Date:** May 2026

---

## Purpose

This catalogue formally defines each of the six ZAF viewpoints in accordance with ISO/IEC/IEEE 42010:2022 Section 7 requirements. Each viewpoint definition includes: stakeholders, concerns, model kinds, conventions, and rationale.

---

## VP1 — Direction Viewpoint

**Instrument:** Guardrail Canvas  
**Layer:** Enterprise  
**Location:** `/viewpoints/vp1-direction/`

### Stakeholders
Executive leadership (C-suite, board), enterprise architects, business unit leaders, investment decision-makers.

### Concerns
- What is the strategic direction the organisation is committed to?
- Where is investment misaligned with strategic priority?
- What capabilities are unowned or in dispute?
- What decision is required before this direction can move to funded delivery?
- What assumptions does this direction depend on?

### Model kind
The Guardrail Canvas — a structured one-page commitment record capturing: direction committed to, decision owner, date, live assumptions, first invalidation trigger, what was not decided, hidden veto holders, and next decision required.

### Conventions
- Direction stated in one sentence. Multi-sentence directions are not yet commitments.
- Assumptions must be specific and named. Vague assumptions are not recorded.
- Invalidation trigger named by the decision owner — not inferred by the architect.
- The artefact is produced after the executive conversation, not before it.

### Rationale for inclusion
The Direction viewpoint exists because organisations commit resources without committing to direction. The Guardrail Canvas makes the commitment concrete, dated, and revisable when conditions change. Without this viewpoint, investment decisions are made against an assumed but unstated direction — the primary source of strategic misalignment.

---

## VP2 — Decision Viewpoint

**Instrument:** Trade-off Matrix  
**Layer:** Solution  
**Location:** `/viewpoints/vp2-decision/`

### Stakeholders
Solution architects, enterprise architects, project leads, technical decision-makers, governance bodies.

### Concerns
- What solution was chosen and why?
- What options were evaluated and rejected?
- What assumptions does this decision depend on?
- What constraints have been accepted?
- What would invalidate this decision?
- Who made this decision and when?

### Model kind
The Trade-off Matrix — a structured decision record capturing: decision made, options rejected with rejection rationale, assumptions, constraints accepted, principles compliance or exception, invalidation triggers, and named decision owner with date.

### Conventions
- Rejected options section is mandatory. A decision record without rejected options has no forensic value.
- Decision owner is one named individual — not a team or committee.
- Written on the day the decision is made — not retrospectively.
- Assumptions and constraints are explicitly separated.

### Rationale for inclusion
The Decision viewpoint exists because architectural decisions are routinely made without recording the context, the alternatives considered, or the conditions that would change them. The Trade-off Matrix provides the forensic record that allows future practitioners to know whether a decision is still valid.

---

## VP3 — Truth Viewpoint

**Instruments:** Architecture Decision Records (ADRs) + Fitness Functions  
**Layer:** Technical  
**Location:** `/viewpoints/vp3-truth/`

### Stakeholders
Technical architects, delivery teams, operations teams, incident response teams, auditors.

### Concerns
- What was decided, what was rejected, and what would change this decision?
- Does the current system state conform to architectural intent?
- Where has the as-built state diverged from the as-designed state?
- What are the integration dependencies that would block planned changes?
- Is the infrastructure documentation accurate enough to support incident response?

### Model kinds
Two model kinds:

**ADR (Architecture Decision Record)** — five fields: decision, what was rejected, what would change this decision, decision owner, date. Written the same day. No template beyond these five fields.

**Fitness Function** — a quantifiable test that confirms an architectural characteristic is maintained over time. Defined at artefact level, executed continuously or at defined cadence.

### Conventions
- ADRs are immutable once written. New circumstances produce a new ADR referencing the original — the original is never modified.
- Fitness functions must be executable — aspirational fitness functions that cannot be measured are not fitness functions.
- Ground truth artefacts (as-is models, integration maps, infrastructure diagrams) are maintained by operators — not reviewed annually by the architecture team.

### Rationale for inclusion
The Truth viewpoint exists because organisations lose the context of past decisions (ADRs) and lose currency of the actual state (fitness functions and ground truth artefacts). Both failures produce the same outcome: decisions made on false assumptions. The Truth viewpoint is the accuracy layer.

---

## VP4 — Velocity Viewpoint

**Instruments:** Velocity Dashboard + Architectural Decision Log (ADL)  
**Layer:** Control  
**Location:** `/viewpoints/vp4-velocity/`

### Stakeholders
Enterprise architects, architecture governance bodies, CTO/CIO, portfolio managers.

### Concerns
- How fast are architectural decisions being made?
- Where is decision latency creating organisational risk?
- What is the current state of architectural debt?
- What decisions are overdue or stalled?
- Is the architecture portfolio moving toward or away from the target state?

### Model kinds
**Velocity Dashboard** — a control instrument showing: decision latency by domain, architectural debt indicators, overdue decisions, and portfolio trajectory. Updated at the cadence defined by the Pulse System (VP5).

**Architectural Decision Log (ADL)** — a time-ordered register of all significant architecture decisions across the portfolio. Links to individual ADRs (VP3). Enables pattern analysis and debt identification at the portfolio level.

### Conventions
- Decision latency is measured from the point a decision is identified as required to the point it is made and recorded.
- Architectural debt items are quantified where possible — qualitative-only debt entries are flagged as requiring quantification.
- The ADL is the source of truth for governance reporting — not meeting minutes or email threads.

### Rationale for inclusion
The Velocity viewpoint exists because architecture governance without measurement is opinion. The dashboard and log instruments provide the control data that allows the architecture practice to demonstrate value and identify where it is adding friction rather than reducing it.

---

## VP5 — Rhythm Viewpoint

**Instrument:** Pulse System  
**Layer:** Operating  
**Location:** `/viewpoints/vp5-rhythm/`

### Stakeholders
Enterprise architects, delivery leads, architecture review boards, governance bodies, executive sponsors.

### Concerns
- What is the operating cadence for architectural governance?
- When are architecture reviews conducted and by whom?
- How are architectural issues escalated?
- What is the exception approval process for deviations from standards and principles?
- How is architectural health communicated to executives?

### Model kind
**Pulse System** — a cadence definition instrument specifying: review frequency by artefact type, escalation paths, exception approval mechanism, and executive reporting format. Not a meeting schedule — a governance operating model.

### Conventions
- Exception processes must be achievable within 48 hours or they will be bypassed.
- Pulse reports to executives use business language — no artefact terminology.
- The rhythm is triggered by conditions (decision required, artefact overdue, exception raised) — not only by calendar dates.

### Rationale for inclusion
The Rhythm viewpoint exists because architecture governance without a defined operating cadence either over-governs (blocking delivery) or under-governs (becoming irrelevant). The Pulse System defines the minimum governance rhythm required to maintain architectural integrity without becoming overhead.

---

## VP6 — Practitioner Viewpoint

**Instrument:** Integrity Arc (Auctor Custos role)  
**Layer:** Human  
**Location:** `/viewpoints/vp6-practitioner/`

### Stakeholders
Enterprise architects, solution architects, architecture practice leads, organisation leadership.

### Concerns
- Who is responsible for the integrity of the architecture practice?
- What are the operating obligations of the practitioner role?
- How does the practitioner maintain objectivity under delivery pressure?
- What is the escalation obligation when architectural integrity is being compromised?
- How is practitioner performance assessed?

### Model kind
**Integrity Arc** — a practitioner operating model defining: the Auctor Custos role obligations, the escalation obligation triggers, the integrity assessment criteria, and the practitioner development arc from entry to senior practice.

The Auctor Custos (author-guardian) is the named practitioner accountable for the integrity of the architecture description. Every architecture description has one named Auctor Custos.

### Conventions
- The Auctor Custos obligation is to the architecture's integrity — not to the delivery timeline or the stakeholder's preference.
- Escalation is an obligation, not an option, when architectural integrity is being materially compromised.
- Practitioner performance is assessed against the integrity arc criteria — not against delivery velocity alone.

### Rationale for inclusion
The Practitioner viewpoint exists because architecture quality ultimately depends on practitioner behaviour under pressure. Frameworks that specify artefacts and viewpoints without specifying the practitioner obligation model produce correct-looking documents produced by practitioners who have been pressured into ratifying bad decisions. VP6 closes that gap.

---

*ZenCloud Global Consultants · ZenCloud Architecture Framework™ · May 2026*
