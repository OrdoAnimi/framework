# PBK-01: Onboarding a New Engagement

**The OrdoAnimi Framework — Pattern & Playbook | Column 6**

| Field | Value |
|-------|-------|
| Playbook ID | PBK-01 |
| Name | Onboarding a New Engagement |
| Type | Playbook |
| Status | Active |
| Scope | The first 21 days of any new architecture engagement |
| Primary instruments | Guardrail Canvas (VP1), Trade-off Matrix (VP2), ADL (VP4), Pulse System (VP5), Integrity Arc (VP6) |
| Correspondence rules | CR-O1, CR-O3, CR-X1, CR-T1, CR-L1 |

---

## Purpose

This playbook defines the mandatory sequence for establishing a OrdoAnimi governance structure at the start of a new engagement. It applies to any engagement where the OrdoAnimi framework is the governing method — regardless of scale.

The purpose of onboarding is not to produce artefacts. It is to establish the conditions under which decisions can be made. The first 21 days either produce those conditions or they produce documents that document the absence of conditions.

---

## Before You Begin — Scope Declaration (CR-O3)

For any engagement longer than 3 months, a written scope declaration is required before any work begins. The scope declaration states:

- What the practitioner is responsible for deciding
- What the practitioner is responsible for advising on
- What sits outside the practitioner's scope
- Who holds authority for each category of decision

This is not a contract addendum. It is the practitioner's statement of their Integrity Arc (VP6) — the line between adviser and decision-maker.

**If scope is not declared in writing, all subsequent artefacts carry ambiguous accountability. The scope declaration is the first act of governance.**

---

## The 21-Day Sequence

### Days 1–5: Establish Direction (VP1)

**Objective:** Produce the first Guardrail Canvas.

| Move | Action | Output |
|------|--------|--------|
| 1.1 | Identify the single most consequential architectural question facing the engagement | Named question in writing |
| 1.2 | Identify all stakeholders for that question (S1–S10 register) | Populated stakeholder map |
| 1.3 | Confirm the authority who can bind decisions at enterprise level (S5 or S6) | Named binding authority |
| 1.4 | Elicit enterprise constraints — what cannot change regardless of the solution chosen | Constraint register |
| 1.5 | Draft Guardrail Canvas GC-[YYYYMMDD]-001 — constraints, not solutions (CR-L1) | Canvas document |
| 1.6 | Confirm Canvas with binding authority — must be signed or explicitly confirmed in writing | Confirmed Canvas |

**Do not produce a Trade-off Matrix until the Canvas is confirmed.** A solution explored without an enterprise constraint set will require rework.

---

### Days 6–10: Open the ADL (VP4)

**Objective:** Establish the decision log and activate the operating rhythm.

| Move | Action | Output |
|------|--------|--------|
| 2.1 | Create ADL/INDEX.md — first entry references the confirmed Canvas | ADL opened |
| 2.2 | List every known open architectural question from the engagement brief | Decision register (preliminary) |
| 2.3 | Assign a single named owner and an expiry date (CR-O1, CR-X1) to every open question | Populated decision register |
| 2.4 | Flag any question older than 14 days — it is already in CR-E1 territory | Escalation list (if any) |
| 2.5 | Identify the highest-priority open question for the first Trade-off Matrix | Prioritised question |

---

### Days 11–15: First Trade-off Matrix (VP2)

**Objective:** Produce the first binding architectural decision under the governing Canvas.

| Move | Action | Output |
|------|--------|--------|
| 3.1 | Draft TOM-[YYYYMMDD]-001 — must reference confirmed Canvas (CR-T1) | Trade-off Matrix draft |
| 3.2 | Identify the 2–4 viable options for the priority question | Options defined |
| 3.3 | Define the evaluation criteria against the Canvas constraints | Criteria set |
| 3.4 | Score each option against each criterion — with evidence for each score | Scored matrix |
| 3.5 | Present to decision-maker (not a committee — a named individual, CR-O1) | Decision session |
| 3.6 | Bind the decision: one option selected, rationale documented, ADR opened if required | Binding decision |
| 3.7 | Update ADL entry — status: Decided | ADL updated |

---

### Days 16–21: First Pulse (VP5)

**Objective:** Establish the operating rhythm and baseline the engagement health.

| Move | Action | Output |
|------|--------|--------|
| 4.1 | Schedule the Tier 1 Pulse (weekly) — same time, same participants, standing agenda | Calendar commitment |
| 4.2 | Prepare the first Pulse Briefing — using the confirmed template (templates/pulse-briefing.md) | Pulse Briefing document |
| 4.3 | Conduct the first Pulse session — present: one open decision, one confirmed decision, risk register, next actions | Session record |
| 4.4 | Any decisions open >14 days at this point — activate CR-E1 in the session | Escalation actions |
| 4.5 | Produce the Pulse Report — brief summary of the session for the owning authority | Pulse Report |
| 4.6 | Update the Velocity Dashboard — first baseline | Dashboard update |

---

## What You Must Have Produced by Day 21

At the close of the onboarding period, the following must exist. If any item is absent, name the absence and the reason in writing before continuing.

| Artefact | ID | Required by |
|----------|-----|------------|
| Scope declaration | — | CR-O3 |
| Guardrail Canvas (confirmed) | GC-[date]-001 | CR-T1 |
| ADL opened with populated register | ADL/INDEX.md | CR-O1, CR-X1 |
| One confirmed binding decision | TOM-[date]-001 | CR-L2 |
| Pulse rhythm established | Calendar + first session record | VP5 |

---

## Failure Modes — What to Watch For

| Failure mode | Early indicator | Response |
|-------------|----------------|----------|
| Canvas produced without binding authority | "We'll get the CIO to sign off later" | Stop. Bind the Canvas first. |
| TOM produced without Canvas | Options being explored without constraints | Produce Canvas before next session |
| Decision register owned by "the team" | No single name against any item | Apply CR-O1 — name one owner per item now |
| Pulse rhythm not established by Day 21 | "We'll start that next month" | Book the standing session before the week ends |
| Scope never declared | Practitioner is doing things not agreed | Produce scope declaration immediately, even if late |

---

## Related Patterns

- **PAT-01 — Stalled Decision:** the most likely failure in Days 6–15 if the decision register is not managed actively
- **PAT-03 — Architecture Theatre Trap:** the risk if artefacts are produced but no decision binds in the first 21 days

---

## Related Examples

- `examples/adl-example.md` — shows a populated ADL at end of onboarding period
- `examples/pulse-briefing-example.md` — shows a first Pulse Briefing using the Cloud Platform Modernisation scenario
- `examples/pulse-report-example.md` — shows a Pulse Report following the first session

---

*PBK-01: Onboarding a New Engagement — The OrdoAnimi Framework*
*© 2026 Phil Myint / OrdoAnimi | ISO/IEC/IEEE 42010:2022 Conformant*
