# Decision Velocity Diagnostic

**Velocity™ — Organisational Health Check**

> Use this diagnostic to assess your organisation's decision health before engaging the full Velocity™.  
> It takes 15 minutes. The results will tell you which viewpoints to engage first.

---

## How to Use This

Score each question 0–3:
- **0** — This does not exist or is not true
- **1** — This exists in theory but rarely in practice
- **2** — This is mostly true, with exceptions
- **3** — This is consistently and reliably true

---

## Section A: Direction (VP1 — Guardrail Canvas)

| # | Question | Score |
|---|----------|-------|
| A1 | Our organisation has a written declaration of what we prioritise when forced to choose between competing goods | |
| A2 | Our non-negotiables (compliance, security, vendor constraints) are written down and known by delivery teams | |
| A3 | Our trade-off positions (speed vs scale, cost vs resilience) are explicitly stated — not inferred | |
| A4 | Enterprise architects can describe direction without specifying solutions | |
| A5 | Delivery teams can identify one document that tells them what they cannot compromise | |

**Section A Total: /15**

---

## Section B: Decision Quality (VP2 — Trade-off Matrix)

| # | Question | Score |
|---|----------|-------|
| B1 | Solution-level decisions are recorded in writing with explicit rationale | |
| B2 | When a decision is made, delivery can begin the same day without further clarification | |
| B3 | Decision records name a single owner — not a committee | |
| B4 | Alternatives considered are documented alongside the chosen option | |
| B5 | Decisions are traceable to the enterprise constraints that governed them | |

**Section B Total: /15**

---

## Section C: Technical Truth (VP3 — ADRs + Fitness Functions)

| # | Question | Score |
|---|----------|-------|
| C1 | Technical decisions are recorded in version control alongside the code | |
| C2 | The same architectural argument has not happened more than once in the past 12 months | |
| C3 | New team members can understand why the system was built the way it was | |
| C4 | Architectural intent is enforced by automated tests, not just documented | |
| C5 | When the system diverges from declared architecture, this is surfaced immediately | |

**Section C Total: /15**

---

## Section D: Decision Velocity (VP4 — Dashboard + ADL)

| # | Question | Score |
|---|----------|-------|
| D1 | We know how many significant decisions are currently open | |
| D2 | We know how long each open decision has been open | |
| D3 | We have a defined threshold at which an open decision triggers escalation | |
| D4 | Our architecture decisions are indexed and searchable | |
| D5 | When someone leaves, their decisions and rationale remain accessible | |

**Section D Total: /15**

---

## Section E: Governance Rhythm (VP5 — Pulse)

| # | Question | Score |
|---|----------|-------|
| E1 | Architecture governance operates on a defined, predictable cadence | |
| E2 | Each governance session produces at least one binding decision | |
| E3 | Escalations have a defined path and a defined endpoint | |
| E4 | Decisions not resolved in one session do not simply return to the next session unchanged | |
| E5 | Our governance forums are known for making decisions, not reviewing documents | |

**Section E Total: /15**

---

## Section F: Practitioner Integrity (VP6 — Integrity Arc)

| # | Question | Score |
|---|----------|-------|
| F1 | Architects in our organisation assert positions — they do not only facilitate | |
| F2 | The architect's scope of accountability is clearly defined | |
| F3 | Architects are not used as buffers for decisions that leadership should make | |
| F4 | Architectural work is not produced to satisfy governance rather than to guide delivery | |
| F5 | Our architects would describe their work as meaningful, not ceremonial | |

**Section F Total: /15**

---

## Scoring

| Total Score | Interpretation |
|-------------|----------------|
| 75–90 | **High velocity** — Framework is largely in place. Use Velocity™ to formalise and strengthen. |
| 55–74 | **Moderate velocity** — Meaningful gaps exist. Prioritise the lowest-scoring sections. |
| 35–54 | **Low velocity** — Decision latency is structural. Begin with VP1 (direction) and VP4 (control). |
| 0–34 | **Stalled** — Responsibility diffusion is embedded. Begin with the Foundation Layer and VP6 (practitioner). |

---

## Lowest-Scoring Section: Engagement Priority

| Lowest section | Start here |
|---------------|------------|
| A — Direction | VP1: Deploy a Guardrail Canvas for the most contested domain |
| B — Decision Quality | VP2: Replace the next major meeting with a Trade-off Matrix |
| C — Technical Truth | VP3: Introduce ADRs into the next sprint; add one fitness function |
| D — Velocity | VP4: Stand up the ADL; instrument the 14-Day Decision Aging Rule |
| E — Governance Rhythm | VP5: Redesign the next governance forum as a Pulse session |
| F — Practitioner | VP6: Name the sacred cows; clarify scope for every architect in the team |

---

## One Question to Ask Your Leadership Team

> *How many significant decisions are currently open in your organisation, and how long have they been open?*

If no one can answer this, the diagnostic has already told you what you need to know.

---

*Decision Velocity Diagnostic — Velocity™ | Velocity Architecture Framework™*  
*© 2026 Phil Myint / ZenCloud Global Consultants | ISO/IEC/IEEE 42010:2022 Conformant*
