# Pulse System

**Velocity™ VP5 — Rhythm Viewpoint | Operating Layer**

> The Pulse is the Velocity™ operating heartbeat.  
> It is a structured cadence of review, decision, and escalation events.  
> Governance that does not operate at a defined frequency is not governance — it is event-driven reaction.

---

## Pulse Configuration

| Field | Value |
|-------|-------|
| **Programme / Engagement** | |
| **Pulse Tier** | Tier 1 (Weekly) \| Tier 2 (Fortnightly) \| Tier 3 (Monthly) |
| **Pulse Owner** | Single named facilitator and decision authority |
| **Participants** | Named roles — not open invitation |
| **Session Duration** | [e.g. 60 minutes — no extensions] |
| **Effective From** | YYYY-MM-DD |

---

## Pulse Tiers

| Tier | Frequency | Scope | Decision authority |
|------|-----------|-------|-------------------|
| Tier 1 | Weekly | Active delivery decisions (VP2, VP3) | Solution Architect / Delivery Lead |
| Tier 2 | Fortnightly | Programme and cross-team decisions | Enterprise Architect / Programme Director |
| Tier 3 | Monthly | Strategic direction, canvas review | CIO / Architecture Review Board |

Escalation moves upward: Tier 1 → Tier 2 → Tier 3. Maximum two cycles at any tier before mandatory binding at the tier above.

---

## Pulse Briefing Template

*Distributed 48 hours before the session. No surprises in the room.*

---

**PULSE BRIEFING**  
Programme: [Name] | Date: YYYY-MM-DD | Tier: [1/2/3]

---

### Decisions Requiring Binding This Session

| ID | Decision | Age (days) | Owner | Recommendation |
|----|----------|------------|-------|---------------|
| TOM-YYYYMMDD-XXX | | | | Decide / Escalate / Defer with new expiry |

### Open Questions Approaching Expiry

| Question | Raised | Expiry | Age | Risk if not closed |
|----------|--------|--------|-----|-------------------|
| | YYYY-MM-DD | YYYY-MM-DD | | |

### Escalations from Previous Session

| Escalation | Source | Escalated By | Required outcome |
|------------|--------|-------------|-----------------|
| | | | Bind / Further escalation |

### Fitness Function Failures Requiring Response

| Function | Failure description | Upstream assumption at risk |
|----------|--------------------|-----------------------------|
| | | |

### New Questions Raised Since Last Pulse

| Question | Raised by | Proposed expiry | Proposed owner |
|----------|-----------|----------------|---------------|
| | | YYYY-MM-DD | |

---

## Pulse Board (Live During Session)

*The Pulse Board is the live tracking surface. Update in real time.*

---

**PULSE BOARD**  
Session: [Programme] | Date: YYYY-MM-DD | Facilitator: [Name]

---

| # | Item | Type | Decision / Outcome | Owner | Due |
|---|------|------|-------------------|-------|-----|
| 1 | | Aging decision | | | |
| 2 | | New decision | | | |
| 3 | | Escalation | | | |
| 4 | | Fitness function | | | |
| 5 | | New question | | | |

**Session test:** Did this session produce at least one binding decision?  
☐ Yes — governance functioning  
☐ No — identify what prevented closure and name it in the Pulse Report

---

## Pulse Report Template

*Distributed within 24 hours. The binding record of the session.*

---

**PULSE REPORT**  
Programme: [Name] | Date: YYYY-MM-DD | Tier: [1/2/3]  
Facilitator: [Name] | Present: [Names / roles]

---

### Decisions Made This Session

| ID | Decision | Owner | Date | Status |
|----|----------|-------|------|--------|
| TOM-YYYYMMDD-XXX | [One sentence] | [Name] | YYYY-MM-DD | Decided |

### Escalations Triggered

| Question / Decision | Escalated to | Tier | Required by | Terminal condition |
|--------------------|-------------|------|-------------|-------------------|
| | | Tier [X] | YYYY-MM-DD | |

### Questions Deferred

| Question | New expiry date | Owner | Reason for deferral |
|----------|----------------|-------|---------------------|
| | YYYY-MM-DD | | |

### Actions Outstanding

| Action | Owner | Due date |
|--------|-------|----------|
| | | |

### Session Health

| Metric | This session |
|--------|-------------|
| Decisions made | |
| Escalations triggered | |
| Questions resolved | |
| Questions deferred | |
| Session produced binding decision? | Yes / No |

---

## Escalation Protocol

When a decision is escalated from this session:

1. **Scope compresses** — the question arriving at the tier above must be narrower (CR-E2)
2. **Ownership intensifies** — fewer people carry it upward, not more (CR-E2)
3. **Terminal condition is declared** — the escalation carries a defined binding point (CR-E3)
4. **Maximum two cycles** — no decision passes through more than two Pulse cycles without binding (CR-E4)

**Escalation is not a holding pattern. It is a narrowing function.**

---

## Pulse Anti-Patterns

These patterns indicate the Pulse has become ceremony rather than governance:

| Anti-pattern | Signal | Response |
|-------------|--------|----------|
| **The Status Update Pulse** | Every agenda item is informational; nothing requires a decision | Redesign the agenda — if there is nothing to decide, cancel the session |
| **The Endless Alignment Loop** | The same question appears in three consecutive sessions | Invoke CR-E4: force escalation or bind with the information available |
| **The Growing Invite List** | Each session has more attendees than the last | Invoke CR-E2: scope compression required; reduce not expand |
| **The Offline Decision** | Binding decisions are made outside the Pulse without recording | All binding decisions enter the ADL within 24 hours |
| **The Caveat Decision** | Decision is "agreed in principle" with unresolved conditions | Not a decision; return to Pulse with conditions resolved or explicitly dropped |

---

*Pulse System — Velocity™ VP5 | Velocity Architecture Framework™*  
*© 2026 Phil Myint / ZenCloud Global Consultants | ISO/IEC/IEEE 42010:2022 Conformant*
