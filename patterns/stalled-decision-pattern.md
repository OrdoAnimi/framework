# PAT-01: Stalled Decision

**The OrdoAnimi Framework — Pattern & Playbook | Column 6**

| Field | Value |
|-------|-------|
| Pattern ID | PAT-01 |
| Name | Stalled Decision |
| Type | Pattern |
| Status | Active |
| Primary instruments | Trade-off Matrix, ADL, CR-E1, Pulse System |
| Related patterns | PAT-02 (Escalation Failure) |

---

## Problem

A significant architectural decision has been open for more than 14 days. It is listed in the ADL, assigned to an owner, and has appeared in at least one Pulse session — but no binding resolution has been produced. The decision keeps returning to the agenda without closing.

---

## Context

This pattern appears in any of the following conditions:

- The decision requires input from a stakeholder who has not engaged
- The options are politically sensitive and no one wants to own the outcome
- The decision scope is too broad — it keeps expanding to include adjacent concerns
- The owner lacks the authority to decide and has not escalated
- The available evidence is insufficient and the owner is waiting for certainty that will not arrive

Stalled decisions are the primary driver of Decision Latency — one of the eight coined concepts in the framework. They are also the trigger condition for CR-E1.

---

## Forces

**Why this is hard to resolve without a framework response:**

1. The decision feels like it is in progress — there is activity, discussion, and apparent movement — but no binding output.
2. Stakeholders often prefer ambiguity over a decision they might disagree with.
3. The owner may not have been told that 14 days is the outer limit.
4. Pulse sessions treat it as an update item rather than a decision item, which reinforces stalling.
5. The longer a decision is open, the more secondary decisions accumulate around it, increasing the cost of resolving it.

---

## Solution

Apply in sequence. Do not skip steps.

### Step 1 — Activate CR-E1
At day 14, the decision formally enters escalation. This is not a discretionary call — CR-E1 is mandatory. The ADL entry is updated to reflect escalation status with the date and the escalation destination.

The owner is notified that the decision is now an escalation item, not an open question. The framing changes: the question is no longer "what should we decide?" but "who is accountable for the decision not being made?"

### Step 2 — Diagnose the stall type
Before escalating, identify which of the five stall conditions applies (see Context above). The diagnosis determines which instrument resolves it.

| Stall type | Resolution instrument |
|------------|----------------------|
| Missing stakeholder | Force attendance at next Pulse or separate closed session |
| Political sensitivity | Reduce scope; isolate the specific question that must bind |
| Scope too broad | Decompose into sub-decisions; bind each separately |
| Owner lacks authority | Escalate — invoke CR-E2 (scope compression) and CR-E3 (terminal condition) |
| Waiting for certainty | Apply Velocity of Truth principle: decide with what is known; document the uncertainty as a fitness function |

### Step 3 — Reframe in the next Pulse session
The stalled decision is placed first on the Pulse agenda — not as an update but as the binding item. The session has one required output: a decision. If the session ends without one, CR-E4 fires — the next Pulse must be at the tier above.

The Pulse facilitator names the stall condition explicitly at the start of the item:

> "This decision has been open for [N] days. Today it binds or it escalates. There is no third option."

### Step 4 — Bind with the available evidence
If the stall is caused by waiting for information that is unlikely to arrive in the required timeframe, the decision is made with the evidence that exists. The uncertainty is documented in the ADR as a fitness function that will either confirm or invalidate the assumption.

This is the application of the Velocity of Truth: the rate at which ambiguity expires is not determined by the arrival of certainty. It is determined by the cost of continued ambiguity.

---

## Correspondence Rules Engaged

| Rule  | Application |
|-------|-------------|
| CR-E1 | Triggers at day 14 — non-negotiable |
| CR-E2 | Scope of the escalated question must be narrower than the original |
| CR-E3 | Escalation carries a defined terminal condition before it leaves the Pulse |
| CR-E4 | Maximum two Pulse cycles before binding or tier escalation |
| CR-O1 | Single named owner throughout — the stall does not permit committee deferral |
| CR-X1 | Every re-opened question arising from the stall carries a new expiry date |

---

## Consequences

After this pattern is applied:

- The decision binds or is escalated to a tier with explicit authority to bind it
- The stall condition is documented in the ADL as a governance event
- Subsequent decisions that were waiting on this one are unblocked
- The owner's accountability for the stall is preserved in the record (not for blame — for pattern recognition)

**What does not change:** the decision itself. The pattern resolves the stall; it does not make the decision easier or guarantee the right answer. The right answer requires evidence, which the pattern forces into the open.

---

## Related Patterns

- **PAT-02 — Escalation Failure:** what happens when the escalation from a stalled decision also fails to bind
- **PAT-03 — Architecture Theatre Trap:** when stalled decisions are resolved by producing artefacts that document the stall rather than resolving it

---

*PAT-01: Stalled Decision — The OrdoAnimi Framework*
*© 2026 Phil Myint / OrdoAnimi | ISO/IEC/IEEE 42010:2022 Conformant*
