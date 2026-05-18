# VAF Practitioner Operating Manual

**For architects who need to move faster.**

Version 1.0 — Velocity Architecture Framework™

---

## How to use this manual

This manual covers all 18 VAF artefacts. Each entry has three layers:

1. **Extraction guide** — how to run the conversation that produces the artefact
2. **VAF template** — what to write, at what resolution
3. **Executive framing** — how to present the finding to leadership

The artefacts are grouped by type. Use the type that matches the decision context, not the one that matches the governance requirement.

---

## The 18 Artefacts

| # | Artefact | Type | Viewpoint |
|---|----------|------|-----------|
| 1 | Guardrail Canvas | Direction | VP1 |
| 2 | Trade-off Matrix | Decision | VP2 |
| 3 | Architecture Decision Record | Decision | VP3 |
| 4 | Fitness Function Register | Control | VP3 |
| 5 | Velocity Dashboard | Control | VP4 |
| 6 | Architectural Decision Log | Control | VP4 |
| 7 | Pulse Briefing | Operating | VP5 |
| 8 | Escalation Register | Operating | VP5 |
| 9 | Integrity Arc Assessment | Operating | VP6 |
| 10 | Capability Map | Direction | VP1 |
| 11 | Domain Model | Direction | VP1 |
| 12 | Risk Register | Control | VP4 |
| 13 | Technology Radar | Control | VP4 |
| 14 | Dependency Map | Decision | VP2 |
| 15 | Handover Record | Operating | VP5 |
| 16 | Pattern Catalogue | Direction | VP6 |
| 17 | Playbook | Operating | VP6 |
| 18 | Decision Velocity Diagnostic | Direction | VP1 |

---

## Type 1 — Direction Artefacts

---

### 1. Guardrail Canvas

**What it is:** A single-page declaration of enterprise direction for a programme, initiative, or domain. It does not prescribe the solution — it defines the corridor within which solutions must sit.

**Standard time:** 3–6 weeks (stakeholder workshops, review cycles, sign-off)
**VAF time:** 2–4 hours (structured workshop with the right people in the room)
**Time saving:** 85–95%

---

#### Extraction Guide

Run a 90-minute workshop with: the programme sponsor, the lead architect, and one representative from delivery.

Ask in sequence:

1. *What outcome are we trying to achieve in plain language?* (10 min)
2. *What constraints are non-negotiable — regulatory, financial, organisational?* (15 min)
3. *What are we explicitly not doing in this programme?* (10 min)
4. *What does success look like in 12 months?* (10 min)
5. *What would cause us to stop?* (10 min)
6. *What assumptions are we treating as true that we have not yet verified?* (15 min)

Capture answers in real time on the canvas. Do not leave the room without a completed first draft. Iteration happens asynchronously after.

---

#### VAF Template

```
GUARDRAIL CANVAS
Programme / Initiative: _______________
Date: _______________    Owner: _______________

OUTCOME
[One to two sentences. What are we trying to achieve?]

GUARDRAILS (non-negotiable constraints)
1.
2.
3.

OUT OF SCOPE
[What are we explicitly not doing?]

SUCCESS CRITERIA (12 months)
[What does good look like?]

STOP CONDITIONS
[What would cause us to halt or pivot?]

UNVERIFIED ASSUMPTIONS
[What are we treating as true that we have not yet confirmed?]

SIGN-OFF
Sponsor: _______________ Date: _______________
Architect: _______________ Date: _______________
```

---

#### Executive Framing

Present as: *"This is the corridor. Everything inside it is in play. Everything outside it is not."*

Do not walk leadership through every field. Present three things:
1. The outcome in one sentence
2. The three guardrails
3. The stop conditions

Ask: *"Does this accurately describe what we are trying to do and what we will not compromise on?"*

If the answer is yes, proceed. If no, update before leaving the room.

---

### 10. Capability Map

**What it is:** A structured view of what the organisation does — not how it does it, not what systems support it, not what it should do in future. A current-state capability inventory at the right level of abstraction for the decision being made.

**Standard time:** 4–8 weeks
**VAF time:** Half-day workshop + 2-hour review
**Time saving:** 80–90%

---

#### Extraction Guide

The most common failure mode for capability maps is wrong altitude. Most maps are produced at too low a level (function-by-function) or too high a level (three boxes labelled "Plan, Build, Run").

The right altitude is determined by the decision. Ask: *what capability boundaries matter for the decision we are trying to make?* Map at that level only.

Run a 3-hour session. Use sticky notes or a whiteboard. Group by: what we do for customers, what we do internally to enable that, what we do to govern and direct.

Do not include:
- Organisational structure (capabilities are not org units)
- Systems or technology (a different artefact)
- Future capabilities (a different conversation)

---

#### VAF Template

```
CAPABILITY MAP
Organisation / Domain: _______________
Date: _______________    Level: L1 / L2 / L3
Decision context: _______________

CUSTOMER-FACING CAPABILITIES
[List. One line each.]

ENABLING CAPABILITIES
[List. One line each.]

GOVERNING CAPABILITIES
[List. One line each.]

CAPABILITY GAPS (relative to decision context)
[What is absent or underdeveloped that matters for this decision?]

NOTES
[Altitude rationale. Scope boundaries. What was excluded and why.]
```

---

#### Executive Framing

Present as: *"This is what we do, at the level that matters for this decision."*

Do not present the full map to leadership. Present the gaps. Leadership cares about what is missing or at risk, not the complete inventory.

---

### 11. Domain Model

**What it is:** A bounded view of the key concepts in a domain, how they relate, and what they mean. Not a data model. Not a class diagram. A vocabulary alignment tool.

**Standard time:** 2–4 weeks
**VAF time:** 2-hour facilitated session
**Time saving:** 70–85%

---

#### Extraction Guide

Domain models fail when they try to be data models. They succeed when they align vocabulary across teams that use the same words to mean different things.

Start with: *"Name the five most important things in this domain."* Write each on a card. Then: *"How do these relate to each other?"* Draw lines. Label them.

The conversation is the artefact. The diagram is the record of the conversation.

---

#### VAF Template

```
DOMAIN MODEL
Domain: _______________
Date: _______________    Facilitator: _______________

KEY CONCEPTS
[List. Name + one-sentence definition for each.]

RELATIONSHIPS
[Describe key relationships between concepts in plain language.]

CONTESTED DEFINITIONS
[Where do teams use the same word to mean different things?]

AGREED DEFINITIONS
[What was resolved in this session?]

DIAGRAM REFERENCE
[Link to or embed the concept diagram.]
```

---

#### Executive Framing

Present as: *"These are the things that matter in this domain and how they connect. This is the vocabulary we are committing to."*

Value to leadership: prevents the rework that comes from teams building on different definitions of the same concept.

---

### 18. Decision Velocity Diagnostic

**What it is:** A structured assessment of how fast and how well an organisation makes architectural decisions. Produces a baseline score and identifies the specific failure modes present.

**Standard time:** 4–6 weeks (surveys, interviews, analysis)
**VAF time:** 2-hour diagnostic session
**Time saving:** 75–90%

---

#### Extraction Guide

See [`/diagnostics/decision-velocity-diagnostic.md`](/diagnostics/decision-velocity-diagnostic.md) for the full diagnostic instrument.

Run with: the lead architect, one delivery lead, one business sponsor. Ask each to score independently before discussing. The gaps between scores are as informative as the scores themselves.

---

#### VAF Template

```
DECISION VELOCITY DIAGNOSTIC
Organisation / Domain: _______________
Date: _______________    Facilitator: _______________

VELOCITY SCORE: ___ / 10

DIMENSION SCORES
Decision clarity:     ___ / 10
Decision speed:       ___ / 10
Decision recording:   ___ / 10
Decision retention:   ___ / 10
Decision reuse:       ___ / 10

PRIMARY FAILURE MODES
[Top 3 identified failure modes with evidence.]

RECOMMENDED INTERVENTIONS
[Specific, time-bounded actions.]

BASELINE DATE
[When to re-run the diagnostic to measure improvement.]
```

---

#### Executive Framing

Present as: *"This is how fast we are currently making good decisions. This is the gap. These are the three things that would close it."*

---

## Type 2 — Decision Artefacts

---

### 2. Trade-off Matrix

**What it is:** A structured comparison of options against weighted criteria, producing a traceable record of why one option was chosen over others.

**Standard time:** 2–3 weeks (options analysis, stakeholder review)
**VAF time:** 1–2 hours
**Time saving:** 80–90%

---

#### Extraction Guide

The failure mode for trade-off matrices is false precision — scoring options to three decimal places without agreeing on what the criteria mean or how important they are.

Run in two parts:

**Part 1 (30 min) — agree the criteria:**
Ask: *"What does a good decision look like here?"* Generate 5–8 criteria. Weight them (must sum to 100). Record any criteria that were rejected and why.

**Part 2 (30 min) — score the options:**
Score each option against each criterion (1–5). Weight × score = weighted score. Sum for total. The highest score is not automatically the recommendation — it is the input to the recommendation.

---

#### VAF Template

```
TRADE-OFF MATRIX
Decision: _______________
Date: _______________    Owner: _______________

CRITERIA AND WEIGHTS
| Criterion | Weight |
|-----------|--------|
| [criterion 1] | [%] |
| [criterion 2] | [%] |
| [criterion 3] | [%] |
Total: 100%

OPTIONS AND SCORES
| Option | [C1 w%] | [C2 w%] | [C3 w%] | Total |
|--------|---------|---------|---------|-------|
| [A]    |         |         |         |       |
| [B]    |         |         |         |       |
| [C]    |         |         |         |       |

RECOMMENDATION
[Which option, and the deciding factor in plain language.]

REJECTED CRITERIA
[Criteria considered but excluded, and why.]

REJECTED OPTIONS
[Options considered but excluded before scoring, and why.]
```

---

#### Executive Framing

Do not present the matrix to leadership. Present: option chosen, the one deciding factor, and what was traded away.

*"We chose option B. The deciding factor was operational risk. We traded away a lower initial cost for a significantly lower probability of unplanned outage in year one."*

---

### 3. Architecture Decision Record

**What it is:** A single-page record of one significant architectural decision — the context, the options, the reasoning, and the consequences.

**Standard time:** Often never produced, or produced weeks after the decision
**VAF time:** 20–30 minutes, immediately after the decision is made
**Time saving:** Infinite (replacing zero with something)

---

#### Extraction Guide

The ADR must be produced immediately. A decision not recorded within 48 hours will lose its reasoning within two weeks and its context within six months.

Ask the decision-maker five questions:

1. *What was the situation that required a decision?*
2. *What was decided?*
3. *What else was on the table?*
4. *Why this option?*
5. *What is now true because of this decision?*

Write the answers. That is the ADR.

---

#### VAF Template

```
ADR-[number]: [Title — verb + noun]

Status: Proposed / Accepted / Superseded / Deprecated
Date: _______________
Author: _______________
Deciders: _______________

CONTEXT
[Two to four sentences. What situation required a decision?]

DECISION
[One sentence. What was decided?]

OPTIONS CONSIDERED
- [Option A]
- [Option B]
- [Option C]

REASONING
[Three to five sentences. Why this option?]

CONSEQUENCES
[What is now binding? What constraints does this create?
What follow-on decisions does this require?]

RELATED DECISIONS
[Links to related ADRs.]
```

---

#### Executive Framing

ADRs are rarely presented to leadership individually. They are referenced when decisions are questioned or reversed. The executive framing is: *"This decision was made on [date] by [deciders]. The reasoning is recorded. Here it is."*

The value of an ADR is highest when someone asks *"why did we do it this way?"* six months after the decision was made.

---

### 4. Fitness Function Register

**What it is:** A set of automated or manual checks that verify architectural decisions are still holding in the running system.

**Standard time:** Typically never produced in most organisations
**VAF time:** 2-hour definition session + implementation time per function
**Time saving:** Replaces manual architecture review cycles

---

#### Extraction Guide

For each significant ADR, ask: *"How would we know if this decision stopped being true?"*

The answer is a fitness function. It may be automated (a CI pipeline check, a performance threshold alert, a compliance scan) or manual (a monthly review question).

Focus on the decisions that, if they drifted, would cause the most damage before anyone noticed.

---

#### VAF Template

```
FITNESS FUNCTION REGISTER
Domain: _______________
Date: _______________    Owner: _______________

| ID | ADR | Function description | Automated? | Threshold | Frequency | Owner |
|----|-----|---------------------|------------|-----------|-----------|-------|
|    |     |                     | Y/N        |           |           |       |

CURRENT STATUS
| ID | Last checked | Status | Notes |
|----|-------------|--------|-------|
|    |             | Pass/Fail/At risk | |
```

---

#### Executive Framing

Present as: *"These are the automated guardrails on our most significant decisions. They tell us when drift is occurring before it becomes a problem."*

---

### 14. Dependency Map

**What it is:** A structured view of the dependencies between systems, teams, or capabilities that are relevant to a decision or delivery programme.

**Standard time:** 2–4 weeks
**VAF time:** 90-minute facilitated session
**Time saving:** 75–85%

---

#### Extraction Guide

Do not attempt to map all dependencies. Map only the dependencies that matter for the decision or programme at hand.

Ask: *"What does this system/team/capability depend on to function? What depends on it?"*

Mark criticality: which dependencies, if broken, would halt delivery or cause failure?

---

#### VAF Template

```
DEPENDENCY MAP
Context: _______________
Date: _______________

INBOUND DEPENDENCIES (what this depends on)
| Dependency | Criticality | Owner | Status |
|------------|-------------|-------|--------|

OUTBOUND DEPENDENCIES (what depends on this)
| Dependent | Criticality | Owner | Status |
|-----------|-------------|-------|--------|

CRITICAL PATH
[Which dependency chain, if broken, causes the most damage?]

RISK FLAGS
[Dependencies with no clear owner, unknown status, or known fragility.]
```

---

#### Executive Framing

Present as: *"These are the three dependencies that could stop this programme. Here is what we are doing about each."*

---

## Type 3 — Control Artefacts

---

### 5. Velocity Dashboard

**What it is:** A living view of the current health of architectural commitments across a domain or programme. Not a project status report — a decision integrity report.

**Standard time:** Typically never produced systematically
**VAF time:** 30-minute weekly update
**Time saving:** Replaces ad-hoc architecture review meetings

---

#### Extraction Guide

The dashboard is updated, not produced. The first version takes 2 hours to establish. Subsequent updates take 30 minutes.

The three questions it answers:
1. Which decisions are holding?
2. Which are drifting?
3. Which have been superseded but not recorded?

---

#### VAF Template

```
VELOCITY DASHBOARD
Domain: _______________
Last updated: _______________    Owner: _______________

DECISION HEALTH
| ADR | Status | Last reviewed | Drift detected? | Action required? |
|-----|--------|---------------|-----------------|------------------|

OPEN DECISIONS (required but not yet made)
| Decision required | Owner | Target date | Blocker? |
|-------------------|-------|-------------|----------|

RECENTLY SUPERSEDED
| ADR | Superseded by | Date | Communicated? |
|-----|---------------|------|---------------|

VELOCITY SCORE THIS CYCLE: ___ / 10
TREND: ↑ / → / ↓
```

---

#### Executive Framing

One page. Three numbers: decisions holding, decisions drifting, decisions overdue.

*"Of the 14 significant decisions in this domain, 11 are holding, 2 are drifting and being addressed, 1 has been superseded and is being updated. Decision velocity this cycle: 7/10, up from 6 last month."*

---

### 6. Architectural Decision Log

**What it is:** A chronological index of all ADRs in a domain, their current status, and their relationships. The ADL is the navigation layer over the individual ADRs.

**Standard time:** Not typically maintained as a separate artefact
**VAF time:** 15-minute update per cycle
**Time saving:** Replaces manual trawling through decision history

---

#### Extraction Guide

The ADL is a table. It does not contain the decisions — it indexes them. Every ADR gets a row when it is created. The row is updated when the status changes.

---

#### VAF Template

```
ARCHITECTURAL DECISION LOG
Domain: _______________
Last updated: _______________

| ADR | Title | Date | Status | Supersedes | Superseded by |
|-----|-------|------|--------|------------|---------------|
| ADR-001 | | | Accepted | | |
| ADR-002 | | | Superseded | ADR-001 | ADR-007 |
```

---

#### Executive Framing

Not presented to leadership directly. Referenced when a decision is questioned: *"The decision log shows this was addressed in ADR-004, accepted in March, reviewed in July, still current."*

---

### 12. Risk Register

**What it is:** A structured log of architectural risks — decisions not yet made, dependencies not yet resolved, assumptions not yet validated — that could cause delivery or operational failure.

**Standard time:** Typically exists as a project risk register, not architecture-specific
**VAF time:** 1-hour initial session, 30-minute fortnightly update

---

#### Extraction Guide

An architectural risk register is different from a project risk register. It captures:
- Decisions deferred past their decision latency (the point at which deferral starts causing damage)
- Dependencies with no clear resolution path
- Assumptions being carried without a validation plan

Do not copy the project risk register. Build from architectural decisions and their status.

---

#### VAF Template

```
ARCHITECTURAL RISK REGISTER
Domain: _______________
Last updated: _______________    Owner: _______________

| ID | Risk description | Type | Likelihood | Impact | Decision latency | Owner | Mitigation |
|----|-----------------|------|------------|--------|-----------------|-------|------------|
| R-001 | | Decision deferred / Dependency / Assumption | H/M/L | H/M/L | [date past which this becomes critical] | | |

OVERDUE ITEMS (past decision latency date)
| ID | Risk | Days overdue | Escalation status |
|----|------|-------------|-------------------|
```

---

#### Executive Framing

Present the overdue items only. *"Three architectural decisions have passed their latency date. Here they are, here is what is blocking them, and here is what we need to proceed."*

---

### 13. Technology Radar

**What it is:** A structured view of the technologies in use, under evaluation, on hold, and deprecated across a domain. Used to manage technology proliferation and guide adoption decisions.

**Standard time:** Quarterly cycle, 2–4 weeks per update
**VAF time:** 2-hour quarterly session
**Time saving:** 70–80%

---

#### Extraction Guide

Use four rings: Adopt (use now), Trial (use with caution, learning), Assess (worth exploring), Hold (do not start new work with this). Four quadrants: Languages & Frameworks, Tools, Platforms, Techniques.

Do not attempt to be comprehensive. Cover only the technologies that are decision-relevant for the current quarter.

---

#### VAF Template

```
TECHNOLOGY RADAR
Domain: _______________
Quarter: _______________    Owner: _______________

ADOPT (use now)
[List with one-line rationale each]

TRIAL (use with caution)
[List with one-line rationale and conditions]

ASSESS (worth exploring)
[List with one-line rationale]

HOLD (do not start new work)
[List with one-line rationale and migration path if applicable]

CHANGES FROM LAST QUARTER
[What moved and why]
```

---

#### Executive Framing

Present only movements: what entered Adopt, what entered Hold, and why. *"This quarter we moved Kubernetes to Adopt and placed our legacy ESB on Hold. Here is what that means for the programme."*

---

## Type 4 — Operating Artefacts

---

### 7. Pulse Briefing

**What it is:** A fortnightly or monthly one-page briefing covering the architectural state of a programme — decisions made, decisions pending, risks surfaced, and the single most important action required.

**Standard time:** Not typically produced; ad-hoc status updates used instead
**VAF time:** 30–45 minutes per cycle

---

#### Extraction Guide

Produced by the architect from the Velocity Dashboard and Risk Register. Not a meeting — a document. Distributed before the governance meeting, not during it.

Five sections, maximum one page.

---

#### VAF Template

```
PULSE BRIEFING — [Month/Fortnight]
Programme: _______________    Author: _______________

DECISIONS MADE THIS CYCLE
[List. ADR reference + one-line summary.]

DECISIONS PENDING
[List. What is outstanding, owner, target date.]

RISKS SURFACED
[New items added to the risk register this cycle.]

DRIFT DETECTED
[Any decisions showing signs of not holding.]

ACTION REQUIRED
[Single most important action. Owner. Deadline.]
```

---

#### Executive Framing

The Pulse Briefing is the executive framing. Send it. Do not present it — send it 24 hours before the governance meeting and reference it in the room: *"You have the pulse briefing. The one action required this cycle is on the last line."*

---

### 8. Escalation Register

**What it is:** A log of architectural issues that have been escalated beyond the architecture function — decisions that require executive sponsorship, funding, or cross-domain authority to resolve.

**Standard time:** Not typically maintained as a distinct artefact
**VAF time:** 15-minute update per cycle

---

#### Extraction Guide

An item enters the Escalation Register when the architect has identified the required decision, has been unable to get it made within normal operating rhythm, and the decision latency date is approaching or has passed.

The register is not a complaint log. It is an accountability tool.

---

#### VAF Template

```
ESCALATION REGISTER
Domain: _______________
Last updated: _______________

| ID | Issue | Date raised | Escalated to | Response received | Resolution | Days open |
|----|-------|-------------|-------------|-------------------|------------|-----------|
```

---

#### Executive Framing

Present at governance meetings. *"Two items have been in the escalation register for more than 30 days. Here they are. Here is what we need. Here is the cost of continued delay."*

---

### 9. Integrity Arc Assessment

**What it is:** A structured self-assessment of the architect's own operating integrity — the degree to which their decisions and recommendations are driven by architecture reasoning rather than political, social, or organisational pressure.

**Standard time:** Not typically formalised
**VAF time:** 30-minute quarterly reflection

---

#### Extraction Guide

This is a solo instrument. It is not reviewed by leadership. It is a practitioner discipline tool.

Ask:
1. Which recommendations did I make this quarter that I would stand behind without qualification?
2. Which recommendations did I soften, delay, or change because of pressure that was not architectural?
3. What is the cost of the gap between those two lists?

---

#### VAF Template

```
INTEGRITY ARC ASSESSMENT
Architect: _______________    Period: _______________

DECISIONS MADE WITH FULL ARCHITECTURAL INTEGRITY
[List]

DECISIONS WHERE INTEGRITY WAS COMPROMISED
[List — be specific about the nature of the compromise]

THE GAP
[What is the cost of the decisions in column 2?]

CORRECTIVE INTENT
[What will I do differently next quarter?]
```

---

#### Executive Framing

Not presented to leadership. The Integrity Arc is a practitioner instrument. Its value is in the honesty of the private assessment.

---

### 15. Handover Record

**What it is:** A structured record produced when an architect transitions off a programme — capturing the state of all decisions, open items, risks, and the reasoning behind choices made.

**Standard time:** Rarely produced; institutional knowledge walks out the door
**VAF time:** Half-day to produce

---

#### Extraction Guide

Produce the Handover Record two weeks before transition, not on the last day. Use the ADL as the input — walk through every ADR and record what the incoming architect needs to know that is not in the document.

The ADL + Handover Record together must enable a competent architect to pick up the work without a handover meeting.

---

#### VAF Template

```
HANDOVER RECORD
Programme / Domain: _______________
Outgoing architect: _______________    Incoming architect: _______________
Transition date: _______________

DECISION INVENTORY
[Reference to ADL. Note any ADRs with significant undocumented context.]

OPEN ITEMS
[List. What is in flight, what is blocked, what is urgent.]

CRITICAL RELATIONSHIPS
[Who are the key stakeholders, what do they care about, what is the history?]

RISKS NOT YET IN THE REGISTER
[What are you worried about that is not yet formally captured?]

THINGS I WOULD DO DIFFERENTLY
[Honest retrospective for the benefit of the incoming architect.]
```

---

#### Executive Framing

Not presented to leadership. Referenced if the incoming architect surfaces issues within 90 days of transition: *"This was documented in the handover record."*

---

### 16. Pattern Catalogue

**What it is:** A curated library of architectural patterns in use or approved for use in a domain — with rationale, constraints, and examples for each.

**Standard time:** Years to build organically; often never formalised
**VAF time:** Initial catalogue in one 3-hour session; updated as patterns are identified

---

#### Extraction Guide

Do not attempt to catalogue everything. Start with: *"What are the five patterns we use most often? What are the two we keep arguing about?"*

Document those seven. Add to the catalogue as decisions create new patterns worth recording.

---

#### VAF Template

```
PATTERN CATALOGUE
Domain: _______________
Last updated: _______________    Owner: _______________

PATTERN: [Name]
Problem: [What situation does this pattern address?]
Solution: [What does this pattern prescribe?]
Constraints: [When should this pattern NOT be used?]
Examples: [Where is this pattern in use in this domain?]
ADR reference: [Which decision established or validated this pattern?]
Status: Approved / Experimental / Deprecated
```

---

#### Executive Framing

Not presented to leadership. Referenced by delivery teams. Value is in reducing the time spent relitigating solved problems.

---

### 17. Playbook

**What it is:** A step-by-step operating guide for a specific architectural scenario — how to onboard a new system, how to deprecate a legacy component, how to conduct an architecture review under time pressure.

**Standard time:** Rarely formalised; each event reinvented from scratch
**VAF time:** 2 hours to produce per playbook

---

#### Extraction Guide

A playbook is produced after the first time an event is handled well. Immediately after: *"We just did this well. Write down how we did it."*

The person who ran the event writes the first draft. The architect reviews and formalises. Done.

---

#### VAF Template

```
PLAYBOOK: [Scenario name]
Version: _______________    Owner: _______________
Last used: _______________

WHEN TO USE THIS PLAYBOOK
[Describe the triggering scenario precisely.]

PRE-CONDITIONS
[What must be true before starting?]

STEPS
1.
2.
3.

DECISION POINTS
[Where in the process does a judgement call occur? What are the options?]

COMMON FAILURE MODES
[What goes wrong, and how to avoid it.]

OUTPUT
[What does done look like?]
```

---

#### Executive Framing

Not presented to leadership. Operational instrument. Value is in consistency and speed of execution across events.

---

## Compression Map Summary

| Artefact | Standard time | VAF time | Saving |
|----------|--------------|----------|--------|
| Guardrail Canvas | 3–6 weeks | 2–4 hours | 90%+ |
| Trade-off Matrix | 2–3 weeks | 1–2 hours | 85%+ |
| ADR | Often never | 20–30 min | ∞ |
| Fitness Function Register | Often never | 2 hours | ∞ |
| Velocity Dashboard | Often never | 30 min/week | ∞ |
| Capability Map | 4–8 weeks | Half day | 85%+ |
| Domain Model | 2–4 weeks | 2 hours | 80%+ |
| Technology Radar | 2–4 weeks/quarter | 2 hours | 80%+ |
| Pulse Briefing | Ad-hoc | 30–45 min | ∞ |
| Decision Velocity Diagnostic | 4–6 weeks | 2 hours | 85%+ |

*Velocity Architecture Framework™ — © 2026 Phil Myint / ZenCloud Global Consultants*
