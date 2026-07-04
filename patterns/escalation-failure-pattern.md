# PAT-02: Escalation Failure

**The OrdoAnimi Framework — Pattern & Playbook | Column 6**

| Field | Value |
|-------|-------|
| Pattern ID | PAT-02 |
| Name | Escalation Failure |
| Type | Pattern |
| Status | Active |
| Primary instruments | Escalation Protocol, CR-E2, CR-E3, CR-E4, Pulse System |
| Related patterns | PAT-01 (Stalled Decision), PAT-03 (Architecture Theatre Trap) |

---

## Problem

A decision was escalated from a Pulse session — but the escalation itself has now stalled. The higher-tier authority received the decision, acknowledged it, and produced no binding resolution. The decision has now passed through two Pulse cycles at the escalation tier without binding. The escalation has failed.

This is distinct from PAT-01 (Stalled Decision). In PAT-01, the decision never left the originating tier. In PAT-02, the escalation mechanism itself has broken down.

---

## Context

Escalation failure occurs in any of the following conditions:

- The escalated question was not sufficiently compressed before it arrived at the tier above (CR-E2 violation)
- No terminal condition was declared when the escalation was initiated (CR-E3 violation)
- The authority at the escalation tier does not accept ownership of the decision
- The decision was escalated but then diluted back into a committee with no single named owner (CR-O1 violation)
- The escalation tier's Pulse cadence is too infrequent to resolve the issue within the binding window

An escalation that fails is not neutral — it is a structural signal. The governance model is not functioning at the escalation tier, or the question was incorrectly scoped before it was escalated.

---

## Forces

**Why escalation failures are hard to recover from:**

1. Escalation carries an implicit promise of resolution. When it fails, confidence in the governance system erodes.
2. By the time an escalation fails, the original decision has usually aged well beyond 14 days. Secondary decisions have accumulated around the unresolved question.
3. The decision owner — already extended — must now navigate a governance failure, not just a decision delay.
4. Naming the escalation failure explicitly can feel like a political confrontation, which suppresses it being surfaced at all.

---

## Solution

### Step 1 — Diagnose the failure mode

| Failure mode | Indicator | Resolution |
|-------------|-----------|------------|
| Scope not compressed (CR-E2) | The escalation carried the same breadth as the original question | Reframe — isolate the single binary question the tier above must answer |
| No terminal condition (CR-E3) | The escalation had no defined binding point | Set one now — name the date and authority before re-escalating |
| No named owner (CR-O1) | The decision was absorbed by a committee | Name a single individual accountable for the resolution before the next session |
| Wrong tier | The authority to decide does not sit at the escalation tier | Escalate again — one tier higher |

### Step 2 — Declare the failure explicitly

The failure must be named in writing before the next Pulse. Not as accusation — as a structural observation documented in the ADL.

> "Decision [ID] was escalated to [Tier/role] on [date]. As of [date], no binding resolution has been produced. This constitutes an escalation failure under CR-E4. The decision now requires resolution at the tier above, or an explicit decision to accept the risk of continued ambiguity with a named owner and a defined review date."

### Step 3 — Escalate once more or invoke the boundary

If the governance structure has a higher tier, escalate — with a compressed scope, a named owner, and an explicit terminal condition (CR-E3). This is the final escalation before boundary.

If no higher tier exists, invoke the boundary statement: declare in writing what you can and cannot confirm, name the risk owner, and document the consequence of inaction. Then proceed within your confirmed scope.

The boundary statement is not a resignation. It is the practitioner exercising accountability in the absence of governance.

---

## Correspondence Rules Engaged

| Rule | Application |
|------|-------------|
| CR-E2 | Scope compression — the re-escalation must carry a narrower question than the failed escalation |
| CR-E3 | Terminal condition — every escalation must carry a defined binding point |
| CR-E4 | Two-cycle maximum — the failed escalation has consumed at least one cycle at the tier above |
| CR-O1 | Single named owner — no decision may sit in committee at any tier |
| CR-X1 | New expiry date assigned on re-escalation |

---

## Consequences

After this pattern is applied:

- The governance failure is documented as a structural event, not a personal failure
- The decision is either resolved at the next tier, or the risk is formally owned with a named individual
- The practitioner's professional position is protected by the boundary statement
- The escalation chain is closed — no decision loops indefinitely in the OrdoAnimi governance model

---

## Related Patterns

- **PAT-01 — Stalled Decision:** the precursor — escalation failure cannot occur without a stalled decision that was escalated
- **PAT-03 — Architecture Theatre Trap:** the risk when escalation fails repeatedly — governance becomes ceremony

---

*PAT-02: Escalation Failure — The OrdoAnimi Framework*
*© 2026 Phil Myint / OrdoAnimi | ISO/IEC/IEEE 42010:2022 Conformant*
