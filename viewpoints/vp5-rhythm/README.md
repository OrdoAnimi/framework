# VP5 — Rhythm Viewpoint

**Instrument:** Pulse System  
**Layer:** Operating rhythm  
**ISO/IEC/IEEE 42010 conformant viewpoint**

---

## Purpose

The Rhythm Viewpoint enforces architectural cadence. Governance that does not operate at a defined frequency is not governance — it is event-driven reaction.

The Pulse is the Velocity™ operating heartbeat. It is a structured cadence of review, decision, and escalation events designed to ensure that ambiguity has a lifespan, not a permanent residency.

---

## Concerns Addressed

| Concern | Description |
|---------|-------------|
| C2 — Decision velocity | The rate at which ambiguity expires |
| C8 — Governance effectiveness | Whether governance produces decisions |
| C10 — Responsibility diffusion | Whether accountability is explicit |
| C11 — Decision latency | The interval between recognition and binding resolution |

---

## Pulse System Components

| Component | Purpose |
|-----------|---------|
| **Pulse Rhythm** | The defined frequency — weekly, fortnightly, monthly by tier |
| **Pulse Cadence** | The agenda structure — what is reviewed, decided, and escalated |
| **Pulse Briefing** | Pre-event decision summary distributed before the session |
| **Pulse Board** | The decision tracking surface — live during the session |
| **Pulse Report** | Post-event record — decisions made, escalations triggered, next actions |

---

## Pulse Cadence Template

### Pre-Pulse (Pulse Briefing — distributed 48hrs before)
- Open decisions aging beyond threshold
- Decisions requiring binding resolution this session
- Escalations pending from previous session
- New questions raised since last Pulse

### During Pulse (Pulse Board — live)
1. Review open aging decisions — bind or escalate (max 5 mins each)
2. New decisions requiring commitment — present, decide, record
3. Escalations from VP3 — technical assumptions invalidated
4. Fitness function failures requiring architectural response
5. Ownership gaps — assign or escalate

### Post-Pulse (Pulse Report — distributed within 24hrs)
- Decisions made (with IDs, owners, dates)
- Escalations triggered
- Questions deferred (with new expiry dates)
- Actions outstanding

---

## Escalation Rules (CR-E2, CR-E3, CR-E4)

When a decision is escalated from a Pulse session:

1. **Scope must compress** — the question arriving at higher authority must be narrower than what left the session
2. **Ownership must intensify** — fewer people, not more, carry the escalation
3. **Terminal condition must be declared** — the escalation carries a defined point at which it binds
4. **Maximum two Pulse windows** — no decision may pass through more than two Pulse cycles without binding

---

## Analytic Test

> *Does each Pulse event produce at least one binding decision?*  
> If not, the Pulse is performing ceremony rather than governance.

---

## Pulse Briefing Template

→ [`pulse-system.md`](pulse-system.md)
