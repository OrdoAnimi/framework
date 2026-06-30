# Correspondence Rules Register

**Velocity™ — All Viewpoints | ISO/IEC/IEEE 42010:2022 Conformant**

> Correspondence rules govern the relationships between viewpoints, artefacts, and decisions.  
> They enforce consistency, traceability, and obligation across architecture descriptions.  
> All rules are mandatory unless marked Conditional.

---

## CR-T — Traceability Rules

### CR-T1: Trade-off Matrix → Guardrail Canvas
Every Trade-off Matrix decision must reference at least one Guardrail Canvas constraint it operates within, or explicitly state which constraint it overrides and why.

- **Enforced by:** Fitness function `test_traceability_tom_to_canvas()`
- **Applies to:** All VP2 artefacts
- **Status:** Mandatory

---

### CR-T2: ADR → Trade-off Matrix
Every ADR that implements a solution-level decision must reference the governing Trade-off Matrix record.

- **Applies to:** All VP3 ADRs
- **Status:** Mandatory

---

### CR-T3: Supersession traceability
Any ADR or Trade-off Matrix that supersedes a prior record must explicitly reference the superseded record by ID. Superseded records are retained in the ADL — never deleted.

- **Applies to:** All VP2, VP3 artefacts
- **Status:** Mandatory

---

### CR-T4: Fitness Function → Architectural intent
Every fitness function must carry a comment reference to at least one ADR, Trade-off Matrix, or Correspondence Rule that states the intent it enforces.

- **Format:** `# [ADR-NNN | TOM-YYYYMMDD-NNN | CR-XX] — description`
- **Applies to:** All VP3 fitness functions
- **Status:** Mandatory

---

## CR-E — Escalation Rules

### CR-E1: 14-Day Decision Aging Rule
Any significant architectural decision open for more than 14 calendar days without binding resolution triggers a mandatory escalation event.

- **Enforced by:** Velocity Dashboard aging monitor + fitness function `test_decision_aging()`
- **Applies to:** All open VP2 and VP3 decisions
- **Status:** Hard rule

---

### CR-E2: Scope compression on escalation
When a decision is escalated, the scope presented to higher authority must be narrower than the scope that triggered escalation. An escalation that expands the audience or the problem scope is a process violation.

- **Applies to:** All escalations from VP5 Pulse sessions
- **Status:** Mandatory

---

### CR-E3: Escalation terminal condition
Every escalation must carry a declared terminal condition — a defined point at which the decision binds and does not re-enter circulation unless explicit revisitation criteria (as per CR-X2) are met.

- **Applies to:** All escalations
- **Status:** Mandatory

---

### CR-E4: Pulse escalation window
Decisions not resolved within a Pulse window escalate at the start of the next Pulse event. No decision may pass through more than two Pulse cycles without binding resolution at the appropriate authority level.

- **Applies to:** VP5 Pulse governance cycle
- **Status:** Mandatory

---

## CR-O — Ownership Rules

### CR-O1: Single named owner
Every Trade-off Matrix, ADR, and open question must carry a single named individual as owner. Committee ownership is not permitted. If no individual can be named, this is an escalation trigger.

- **Applies to:** All VP2, VP3, VP4 artefacts
- **Status:** Mandatory

---

### CR-O2: Ownership Map currency
The Ownership Map (RACI) in the Velocity Dashboard must be updated within 5 business days of any ownership transfer.

- **Applies to:** VP4 Velocity Dashboard
- **Status:** Mandatory

---

### CR-O3: Practitioner scope declaration
The practitioner (architect or equivalent) maintains a current written scope declaration defining what they are and are not accountable for within their engagement.

- **Applies to:** VP6 Practitioner artefacts
- **Status:** Conditional (recommended for all engagements exceeding 3 months)

---

## CR-L — Layer Separation Rules

### CR-L1: Enterprise layer constraint
Enterprise architecture artefacts (Guardrail Canvas) must not prescribe solution patterns, mandate specific technologies, or describe system structure. If a canvas contains technology mandates, it has overreached.

- **Enforced by:** Fitness function `test_guardrail_canvas_scope()`
- **Applies to:** All VP1 artefacts
- **Status:** Mandatory

---

### CR-L2: Solution layer decisiveness
Solution architecture artefacts (Trade-off Matrix) must produce a commitment sufficient for delivery to begin without further interpretation. A Trade-off Matrix that ends in further analysis, deferred options, or qualified recommendations has not produced a decision.

- **Test:** Could a delivery team begin work the same day this was agreed?
- **Applies to:** All VP2 artefacts
- **Status:** Mandatory

---

### CR-L3: Technical layer feedback obligation
Technical architecture findings (VP3) that invalidate solution-layer or enterprise-layer assumptions must be surfaced via escalation within one Pulse window. Silent divergence is a process violation.

- **Applies to:** All VP3 fitness function failures and significant technical discoveries
- **Status:** Mandatory

---

### CR-L4: No layer substitution
No layer may substitute for another:
- Enterprise artefacts may not resolve delivery problems
- Solution artefacts may not restate enterprise principles already in a canvas
- Technical teams may not redefine organisational intent without escalation

- **Enforced by:** Fitness function `test_no_layer_bypass()`
- **Applies to:** All viewpoints
- **Status:** Mandatory

---

## CR-X — Expiry Rules

### CR-X1: Ambiguity lifespan
Every significant unresolved architectural question must be assigned an expiry date at the point it is raised. Questions without expiry dates are treated as CR-E1 violations.

- **Applies to:** All open questions in the ADL
- **Status:** Mandatory

---

### CR-X2: Revisitation criteria
A decision may be revisited only when one of the following conditions is met:
1. New material evidence not available at time of decision
2. A threshold breach defined in the original record
3. A material context shift approved by the named owner

Absence of these conditions does not prevent a decision from being reconsidered, but the reconsideration must be documented as a new artefact (not a modification of the original).

- **Applies to:** All VP2 and VP3 decisions
- **Status:** Mandatory

---

### CR-X3: Guardrail Canvas review date enforcement
Every Guardrail Canvas carries a mandatory Review Date field. On that date, the canvas must be either reaffirmed (with a new Review Date) or superseded. A canvas with an expired Review Date is considered inactive and does not provide valid constraints for downstream decisions.

- **Enforced by:** VP4 Velocity Dashboard aging monitor
- **Applies to:** All VP1 artefacts
- **Status:** Mandatory

---

## Rule Summary

| ID | Category | Status | Artefacts |
|----|----------|--------|-----------|
| CR-T1 | Traceability | Mandatory | VP2 → VP1 |
| CR-T2 | Traceability | Mandatory | VP3 → VP2 |
| CR-T3 | Traceability | Mandatory | VP2, VP3 |
| CR-T4 | Traceability | Mandatory | VP3 fitness functions |
| CR-E1 | Escalation | Hard rule | All open decisions |
| CR-E2 | Escalation | Mandatory | Escalations |
| CR-E3 | Escalation | Mandatory | Escalations |
| CR-E4 | Escalation | Mandatory | VP5 |
| CR-O1 | Ownership | Mandatory | VP2, VP3, VP4 |
| CR-O2 | Ownership | Mandatory | VP4 |
| CR-O3 | Ownership | Conditional | VP6 |
| CR-L1 | Layer | Mandatory | VP1 |
| CR-L2 | Layer | Mandatory | VP2 |
| CR-L3 | Layer | Mandatory | VP3 |
| CR-L4 | Layer | Mandatory | All |
| CR-X1 | Expiry | Mandatory | ADL |
| CR-X2 | Expiry | Mandatory | VP2, VP3 |
| CR-X3 | Expiry | Mandatory | VP1 |

---

*Correspondence Rules Register — Velocity Architecture Framework™*  
*© 2026 Phil Myint / ZenCloud Global Consultants | ISO/IEC/IEEE 42010:2022 Conformant*
