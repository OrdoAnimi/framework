# ZAF Correspondence Matrix
## ISO/IEC/IEEE 42010:2022 — Inter-View Relationships and Consistency Rules

**Framework:** ZenCloud Architecture Framework™ (ZAF)  
**Author:** Phil Myint / ZenCloud Global Consultants  
**Date:** May 2026

---

## Purpose

This matrix defines how the six ZAF viewpoints relate to each other and the consistency rules that govern those relationships. It supplements the 17 correspondence rules in `/correspondence-rules/RULES.md` with a visual mapping of inter-view dependencies and a summary consistency checking procedure.

---

## Viewpoint relationship map

```
VP1 Direction ──────────────────────────────────────────────────────┐
     │                                                               │
     │ constrains            informs                                 │
     ▼                       ▼                                       │
VP2 Decision ─────── VP3 Truth ─────── VP4 Velocity                 │
     │                       │                │                     │
     │ feeds                 │ validates      │ reports to          │
     ▼                       ▼                ▼                     │
VP5 Rhythm ◄──────── VP3 Truth          VP5 Rhythm ◄────────────────┘
     │
     │ governs
     ▼
VP6 Practitioner
```

**Reading the map:**
- VP1 constrains VP2 — decisions must comply with declared direction and principles
- VP2 feeds VP3 — decision records are the primary input to the truth layer
- VP3 validates VP2 — fitness functions test whether solution decisions hold over time
- VP4 reports to VP5 — velocity metrics feed the governance rhythm
- VP5 governs VP6 — the operating cadence defines practitioner obligations
- VP1 informs VP4 — strategic direction sets the target against which velocity is measured

---

## Correspondence matrix

Each row defines a consistency requirement between two viewpoints. The check column states how the consistency is verified.

| Rule | From | To | Consistency requirement | Check |
|---|---|---|---|---|
| CR-01 | VP1 Direction | VP2 Decision | Every significant solution decision must reference the strategic direction it serves. If no direction can be named, the decision is not aligned. | Every Trade-off Matrix (VP2) has a named VP1 direction reference. |
| CR-02 | VP1 Direction | VP4 Velocity | The portfolio trajectory in the Velocity Dashboard must move toward the declared direction. Divergence is an escalation trigger. | VP4 dashboard shows directional alignment indicator against VP1 commitments. |
| CR-03 | VP2 Decision | VP3 Truth | Every significant decision recorded in a Trade-off Matrix (VP2) must produce an ADR in VP3 on the same day. | Every VP2 entry has a corresponding VP3 ADR reference. No ADR = decision not complete. |
| CR-04 | VP2 Decision | VP5 Rhythm | Decisions that violate architecture principles must be routed through the VP5 exception process before being recorded as approved in VP2. | Every VP2 entry with a principle non-compliance note has a VP5 exception approval reference. |
| CR-05 | VP3 Truth | VP2 Decision | When a fitness function (VP3) fails, the associated VP2 decision must be reviewed and either reaffirmed or superseded by a new decision. | VP3 fitness function failures trigger a VP2 review within 30 days. |
| CR-06 | VP3 Truth | VP4 Velocity | Ground truth artefact accuracy dates (VP3) feed the architectural debt indicators in VP4. Artefacts not updated within their defined maintenance window are recorded as debt items. | VP4 debt register includes all VP3 artefacts past their accuracy date. |
| CR-07 | VP4 Velocity | VP5 Rhythm | Decision latency metrics from VP4 feed the VP5 pulse reporting cycle. Latency above defined thresholds triggers escalation via the VP5 process. | VP5 pulse reports include VP4 latency data. Threshold breaches are named. |
| CR-08 | VP5 Rhythm | VP6 Practitioner | The Auctor Custos (VP6) is responsible for ensuring VP5 cadence is maintained. Missed review cycles are an Auctor Custos obligation breach. | VP6 practitioner assessment includes VP5 cadence compliance. |
| CR-09 | VP1 Direction | VP6 Practitioner | The Auctor Custos (VP6) has an escalation obligation when delivery pressure is causing VP1 direction commitments to be violated without a recorded direction change. | VP6 escalation log references VP1 commitments being overridden without a new VP1 record. |
| CR-10 | VP3 Truth | VP6 Practitioner | The Auctor Custos (VP6) is accountable for the accuracy of ground truth artefacts (VP3). Drift from accuracy is an Auctor Custos obligation — not a documentation team obligation. | VP3 artefact accuracy dates have named Auctor Custos on each entry. |
| CR-11 | VP2 Decision | VP4 Velocity | Decisions recorded in VP2 are logged in the VP4 ADL. The ADL is the portfolio-level decision register. Decisions not in the ADL are not visible to governance. | VP4 ADL contains all VP2 decisions above the significance threshold. |
| CR-12 | VP4 Velocity | VP1 Direction | When the VP4 dashboard identifies a funded initiative that cannot be traced to a VP1 direction commitment, it is flagged as an unaligned investment. | VP4 portfolio items each reference a VP1 direction commitment. Untraced items flagged. |
| CR-13 | VP3 Truth | VP1 Direction | When an ADR records a decision that contradicts a VP1 direction commitment, a VP1 direction review is triggered. Contradictions are not resolved silently in VP3. | VP3 ADRs with direction conflict notes trigger VP1 review within 14 days. |
| CR-14 | VP5 Rhythm | VP2 Decision | The VP5 architecture compliance review is a required gate before VP2 decisions that affect principles compliance are finalised. Advisory findings do not block. Blocking findings require resolution or exception. | VP2 decisions affecting principle compliance have a VP5 review reference. |
| CR-15 | VP6 Practitioner | VP3 Truth | The Auctor Custos (VP6) is the named authority for VP3 ADR records in their domain. ADRs without a named Auctor Custos are incomplete. | All VP3 ADRs have a named VP6 Auctor Custos. |
| CR-16 | VP1 Direction | VP3 Truth | When VP1 direction assumptions change (invalidation trigger fires), all VP3 ADRs that reference those assumptions must be reviewed and either reaffirmed or superseded. | VP1 assumption changes trigger a VP3 review queue within 30 days. |
| CR-17 | VP4 Velocity | VP6 Practitioner | Persistent decision latency (VP4) in a domain is surfaced to the Auctor Custos (VP6) as a performance indicator. Latency that exceeds defined thresholds for more than two consecutive reporting cycles is an escalation obligation trigger. | VP6 practitioner assessment includes VP4 latency indicators for their domain. |

---

## Consistency checking procedure

The following procedure is used to check consistency across views at the cadence defined by VP5:

**Step 1 — Direction integrity check (VP1 → VP2, VP4)**
Confirm all active VP2 decisions and VP4 portfolio items reference a current VP1 direction commitment. Flag any that do not.

**Step 2 — Decision completeness check (VP2 → VP3)**
Confirm every VP2 Trade-off Matrix entry has a corresponding VP3 ADR. Flag decisions without ADRs.

**Step 3 — Truth accuracy check (VP3 → VP4)**
Confirm all VP3 ground truth artefacts are within their defined maintenance window. Log overdue artefacts in VP4 as debt items.

**Step 4 — Velocity threshold check (VP4 → VP5)**
Check VP4 latency metrics against defined thresholds. Trigger VP5 escalation for breaches.

**Step 5 — Practitioner obligation check (VP6)**
Confirm Auctor Custos assignments are current for all VP3 ADRs. Confirm VP5 cadence has been maintained. Review VP6 escalation log for unresolved items.

**Frequency:** Full consistency check at VP5 pulse cadence. Partial checks (Steps 1 and 2) at every architecture review session.

---

## Relationship to correspondence rules

The 17 correspondence rules in `/correspondence-rules/RULES.md` provide the detailed natural-language specification for each constraint. This matrix provides the summary view and the consistency checking procedure. Both documents must be read together for a complete picture of ZAF inter-view governance.

---

*ZenCloud Global Consultants · ZenCloud Architecture Framework™ · May 2026*
