# VAF Practitioner Operating Manual
## 18 Artefacts · Three Layers Each

**Framework:** Velocity Architecture Framework™ (VAF)  
**Author:** ZenCloud Global Consultants  
**Published:** May 2026

**The Word document version of this manual** (`VAF-Practitioner-Operating-Manual.docx`) contains the full formatted three-layer treatment with colour-coded sections and detailed tables. This Markdown version is the reference version for GitHub reading and linking.

---

## How to use this manual

Three layers. Sequential. Each depends on the previous.

| Layer | Name | Purpose |
|---|---|---|
| 1 | Extraction Guide | How to run the conversation that surfaces the content. Questions, facilitation method, red flags. |
| 2 | VAF Template | Minimum fields to serve the artefact's function. Nothing more. |
| 3 | Executive Framing | How to present the finding to the decision-maker. Format, structure, what never to do, template sentence. |

**Governing principle:** The artefact is the record of the decision made in the conversation. Not the input to it.

---

## The artefacts

- [Architecture Vision](#1-architecture-vision)
- [Business Capability Map](#2-business-capability-map)
- [Architecture Principles](#3-architecture-principles)
- [Value Stream Map](#4-value-stream-map)
- [Business Process Model](#5-business-process-model)
- [Organisation Map](#6-organisation-map)
- [Application Portfolio](#7-application-portfolio)
- [Integration Architecture](#8-integration-architecture)
- [Solution Architecture Document](#9-solution-architecture-document)
- [Conceptual Data Model](#10-conceptual-data-model)
- [Data Flow Diagram](#11-data-flow-diagram)
- [Master Data Map](#12-master-data-map)
- [Technology Roadmap](#13-technology-roadmap)
- [Technology Standards Catalogue](#14-technology-standards-catalogue)
- [Infrastructure Architecture](#15-infrastructure-architecture)
- [Architecture Decision Record](#16-architecture-decision-record)
- [Architecture Compliance Review](#17-architecture-compliance-review)
- [Architecture Roadmap](#18-architecture-roadmap)

---

## 1. Architecture Vision

**Type:** Decision instrument · **Layer:** Strategy · **Standard time:** 4–8 weeks · **VAF time:** 1 session + 2 hrs · **Saving:** ~85%

### Layer 1 — Extraction Guide

**Context:** You are entering a conversation with an executive who has not asked for an Architecture Vision. They have asked for a direction. Your job is to extract the commitment they are already ready to make and record it before it evaporates into the next meeting.

**Questions:**
- *"What is the one thing that must be true in two years for this to have been the right period of investment?"* — Forces a single direction without using the word 'strategy'. Executives answer this.
- *"If we do nothing differently from today, what breaks first?"* — Surfaces the burning platform without requiring the executive to admit there is one.
- *"What would have to change for you to say this was the wrong direction?"* — Extracts the invalidation trigger in the executive's own language.
- *"Who else needs to agree with this before it becomes real?"* — Identifies hidden veto holders.

**Facilitation:** Run this conversation before the session is formally scheduled. The best Architecture Vision conversations happen in corridors, before boards, and at the end of other meetings. The formal session is where you confirm and record — not where you discover.

**Red flags:**
- The executive answers with an existing strategy document. That is not a commitment — it is a reference. Ask what they personally believe.
- Multiple executives give different answers to the first question. Record the divergence — it is the most important output.
- The executive cannot name what would change their mind. The direction is preferred, not committed. Return when it is a commitment.

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Direction committed to | One sentence. If it takes more than one sentence it is not yet a direction. |
| Decision owner | The person who made the commitment — not who attended. |
| Date of commitment | Date the commitment was made. Not document creation date. |
| Assumptions live at the time | 3–5 assumptions this direction depends on. Specific. |
| First invalidation trigger | The single most likely event that would make this direction wrong. |
| What was not decided | Items raised and explicitly deferred or rejected. |
| Hidden veto holders | People not in the session who can block this direction. |
| Next decision required | The decision that must be made before this moves to funded delivery. |

### Layer 3 — Executive Framing

**Format:** Verbal — 3 minutes. One page maximum if written is required.

| Element | What to say |
|---|---|
| The situation | Name the burning platform in one sentence. Do not soften it. |
| The direction | "In our session on [date], you committed to [direction]." Confirmation, not proposal. |
| What this requires from you | One specific ask. Funding, stakeholder introduction, or the next decision. |
| What changes if we do not move | Cost of inaction in business terms — not IT terms. |

**Never do:**
- Never present the assumptions list. It reads as hedging.
- Never use the words "architecture vision." Say "what we agreed."
- Never ask for endorsement of a document. Ask for a decision or an action.

**Template sentence:** *"On [date] you committed to [direction]. That requires [specific next action] by [date]. The cost of delay is [consequence in business terms]. I need [single specific ask] from you before [date]."*

---

## 2. Business Capability Map

**Type:** Signal generator · **Layer:** Strategy · **Standard time:** 6–12 weeks · **VAF time:** 2–3 days · **Saving:** ~80%

### Layer 1 — Extraction Guide

**Context:** You are not building a capability taxonomy. You are surfacing an investment misalignment that already exists. Run the extraction before anyone commissions the artefact.

**Questions:**
- *"Which three things does this organisation need to be genuinely excellent at to deliver its strategy?"* — Gets strategic priority without consulting language.
- *"Where is the most money being spent in IT right now that you are least confident is the right investment?"* — Surfaces suspected misalignment from the executive's own suspicion.
- *"Where do we have capability on paper that does not actually work in practice?"* — Identifies phantom capabilities.
- *"Who owns [capability X]? If I need a decision about it, who do I call?"* — Extracts the accountability gap.

**Facilitation:** Use existing budget data and org structure. The strategic priority (H/M/L) must be answered by a business owner — not assigned by the EA. Draw the heat map in real time during the last conversation so the pattern is visible before you leave the building.

**Red flags:**
- Multiple executives claim ownership of the same capability. Record both — governance finding.
- An executive rates everything H. Ask: "if you could only fund two next year, which two?"
- Budget data does not match priority ratings. Do not reconcile — present them side by side.

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Capability (L1) | Name only. No definition. One row per capability. |
| Strategic priority (H/M/L) | Assigned by named business owner. Not the EA. |
| Current investment (H/M/L/None) | Sourced from budget data. Estimate noted. |
| Gap signal | Where Priority = H and Investment = L or None. Named. |
| Accountability gap | Capabilities with no named owner or disputed ownership. |
| Phantom capabilities | Capabilities rated existing but not functioning in practice. |
| Data sources | Org structure version, budget source, interview subjects, dates. |
| Accuracy date | Trigger for revision: strategic priority change or major budget reallocation. |

### Layer 3 — Executive Framing

**Format:** Heat map visual — one slide. Verbal narrative 4 minutes.

| Element | What to say |
|---|---|
| The pattern | Show the heat map. Let it land. Then: "The red cells are where we have high strategic need and low or no investment." |
| The specific gap | Name the most critical misalignment. One capability. Business-terms cost. |
| The accountability finding | "We have [X] capabilities with no named owner. There is no-one to call when they fail." |
| The ask | Funding decision on the priority gap, or accountability assignment. One ask. |

**Never do:**
- Never present the full capability list. Show the heat map only.
- Never explain the methodology. "We mapped investment against your strategic priorities" is sufficient.
- Never present a to-be capability map in the same session.

**Template sentence:** *"We mapped investment against your strategic priorities. [X] capabilities are critically underfunded. The most significant is [capability] — we are spending [investment level] on something you told me is your highest priority. The cost is [business consequence]. I need a decision on [specific ask]."*

---

## 3. Architecture Principles

**Type:** Control mechanism · **Layer:** Strategy · **Standard time:** 4–6 weeks · **VAF time:** 1 day · **Saving:** ~90%

### Layer 1 — Extraction Guide

**Context:** Principles are extracted from decisions that have already been made badly. Start with the organisation's failure patterns — not a framework template.

**Questions:**
- *"What is the most expensive architecture decision in the last three years you would make differently today?"* — The answer is the rationale. You do not need to write it down.
- *"What decision keeps coming back that should not need to come back?"* — The repeated decision a principle would make automatic.
- *"If a project team makes decision X without asking anyone, what is the worst thing that happens?"* — Tests whether the principle is enforced by consequence or process.

**Facilitation:** Interview the CIO, one delivery lead, and one project manager who has been through a review. Write principles during the interviews — not after. Test each against a recent decision: would this principle have changed what happened?

**Red flags:**
- A principle has no exception anyone can imagine. Either a law already enforced, or it will be ignored.
- Requires reading supporting material to understand. Not finished.
- More than seven principles proposed. Prioritise. Seven enforced > twenty ignored.

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Principle (≤10 words) | Sentence case. No jargon. |
| What this prevents | The specific failure pattern. One sentence. |
| Exception trigger | The specific condition for legitimate deviation. |
| Exception approval | Named role. One person. Not a committee. |
| Exception record pointer | Where approved exceptions are logged. |
| Principle owner | Named person for edge cases and annual review. |

### Layer 3 — Executive Framing

**Format:** Verbal — 2 minutes per principle. Written: one card per principle.

**Never do:**
- Never present more than three principles at once.
- Never call them "architecture principles." Say "decision rules" or "investment guardrails."
- Never present implication lists.

**Template sentence:** *"In [year], we spent [cost] on [failure]. This principle — [principle] — would have prevented that. The only exception is [exception], approved by [role]. I need your endorsement so I can use this to hold the line on [decision type] without escalating every case to you."*

---

## 4. Value Stream Map

**Type:** Signal generator · **Layer:** Business · **Standard time:** 3–6 weeks · **VAF time:** 1–2 days · **Saving:** ~75%

### Layer 1 — Extraction Guide

**Context:** The value stream map is drawn with the people doing the work — not about them.

**Questions:**
- *"Walk me through exactly what happens when [trigger event] occurs. Not the policy — what actually happens."* — The word "actually" is doing critical work.
- *"At this point, what are you waiting for? Who decides when you can move?"* — Surfaces handoff latency and ownership simultaneously.
- *"When this goes wrong, where does it go wrong first?"* — The failure point is almost always a handoff with no owner.
- *"What would have to be true for this step to take half the time?"* — Surfaces the constraint the operator already knows about.

**Facilitation:** Book a room. Get the people who do the work — not who manage it. Draw on whiteboard or stickies. Not software. Every step: named role, named system. Every handoff: named owner or named gap.

**Red flags:**
- A manager describes a step a practitioner then corrects. Record both — governance finding.
- A step has no system and no named role. Highest risk point.
- The stream cannot be completed because no-one knows a step. Name the unknown explicitly.

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Value stream name | Name and trigger event. |
| End state | What done looks like. Delivered to whom. |
| Steps in sequence | Named role. Named system. Observed, not documented. |
| Handoffs — named owner | Every transition between roles or systems. Owner on each side. |
| Handoffs — no owner | The signal. The deliverable. |
| Largest wait time | Single longest delay. Estimated duration. Named cause. |
| Unknown steps | Steps not described. Each is a risk position. |
| Action owner | Named person for primary gap. No owner = signal not received. |
| Observation date | Observed on this date. Not policy. |

### Layer 3 — Executive Framing

**Format:** One visual — stream with gaps highlighted. Verbal 5 minutes.

**Never do:**
- Never show the full stream map. Show only the section containing the primary gap.
- Never say "value stream map." Say "we followed the work."
- Never propose the to-be in this session.

**Template sentence:** *"We traced [process name] from trigger to completion. It takes [total time]. [X] days of that is wait time at a single handoff — between [role A] and [role B] — where no-one is accountable for moving it forward. That costs us [business consequence]. I need [specific person] named as the owner of that handoff."*

---

## 5. Business Process Model

**Type:** Ground truth · **Layer:** Business · **Standard time:** 6–10 weeks · **VAF time:** 3–5 days · **Saving:** ~70%

### Layer 1 — Extraction Guide

**Context:** The as-is model documents what actually happens. Shadow the process for at least two full cycles before drawing anything.

**Questions:**
- *"Show me the last time you completed this process. Walk me through exactly what you did — including workarounds."* — The workarounds are the most important data.
- *"When does this not follow the normal path? What causes the deviation?"* — Exception paths carry the most risk.
- *"If [system X] was unavailable, what would you do instead?"* — Reveals informal parallel processes.
- *"Who do you call when this goes wrong?"* — Names the informal authority structure.

**Red flags:**
- Documented process matches policy perfectly. You are being shown the formal version. Push for actual.
- A step is described as "it depends." Name what it depends on.
- Cannot be completed without a specific named individual. Single point of failure.

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Process name and scope | Start and end events. Boundary conditions. |
| As-is swim-lane | Drawn. Named roles. Named systems. Observation-based. No BPMN unless a system requires it. |
| Named roles | Actual role name, not department. Single points of failure flagged. |
| Named systems | In sequence. Multiple systems for same function = finding. |
| Workarounds in use | Every informal compensating behaviour observed. |
| Exception paths | Every deviation, trigger, handler. |
| Gaps identified | Steps with no system, role, or defined output. |
| Decision list | The to-be is this list. Not a diagram. Named owner per decision. |
| Observation date | Observed on this date by this person. Not the policy version. |

### Layer 3 — Executive Framing

**Format:** One slide — gap summary. Full swim-lane is supporting document only.

**Never do:**
- Never show the swim-lane to an executive.
- Never present the to-be process in the same session.
- Never say "workaround." Say "compensating behaviour" or "informal process."

**Template sentence:** *"We observed [process name] across [X] cycles. The formal and actual process diverge at [specific point]. The informal workaround compensating for this gap is [description]. When it fails, [consequence]. The decision required to close this is [decision]. I need [named person] to own that decision by [date]."*

---

## 6. Organisation Map

**Type:** Signal generator · **Layer:** Business · **Standard time:** 2–4 weeks · **VAF time:** Half day · **Saving:** ~90%

### Layer 1 — Extraction Guide

**Questions:**
- *"If [capability X] fails completely — who is the first person I call?"* — Names the real owner, not the nominal one.
- *"Who would be most upset if [capability X] underperformed?"* — Identifies stakeholder with real accountability interest.
- *"Is there anyone who believes they own [capability X] that we have not named yet?"* — Surfaces disputes before they become conflicts.

**Red flags:** Executive names a department rather than a person. Two executives name each other as owner. Executive says "we all own that."

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Capability | From BCM. No reproduced definitions. |
| Named owner (individual) | One person. Name and role. |
| Disputed ownership | Both claimants named. Nature of dispute. |
| Unowned capabilities | The map. The deliverable. |
| Informal owner | Person actually called when capability fails. |
| Resolution required | Date and named resolution owner. |

**Template sentence:** *"We mapped ownership across your [X] capabilities. [Y] have no named owner. The highest risk unowned capability is [name] — when it fails, there is no-one accountable for the response. I need [X] accountability assignments made."*

---

## 7. Application Portfolio

**Type:** Decision instrument · **Layer:** Application · **Standard time:** 8–16 weeks · **VAF time:** 1 week · **Saving:** ~85%

### Layer 1 — Extraction Guide

**Questions:**
- *"Does this application directly support a strategic priority funded for the next 12 months?"* — Force three options: yes, no, partially.
- *"If unavailable for a week, what breaks?"* — Operational criticality independent of strategic alignment.
- *"Who would you call right now if you wanted to replace this?"* — Names the decision owner.
- *"What does this cost annually — including the staff who support it?"* — Forces total cost view.

**Red flags:** No named owner after 30 minutes. "Critical" to business and "legacy" to IT with no resolution plan. Annual cost cannot be determined.

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Application name | Canonical name from asset register. |
| Owner (named individual) | If unknown after 30 minutes — orphaned. Flag. |
| Annual total cost | Licence + internal support + hosting. Estimate noted. |
| Strategic alignment (Y/N/Partial) | Business owner's answer. Not the EA's assessment. |
| Operational criticality | What breaks if unavailable one week. |
| TIME classification | Tolerate / Invest / Migrate / Eliminate. Applied immediately. |
| Classification blocker | Specific blocker and owner where TIME cannot be assigned. |
| Classification date | Review trigger: strategic or ownership change. |

**Template sentence:** *"We have [X] applications. [Y] are candidates for decommission — [total cost] annually, not aligned to any funded priority. Eliminating the top [X] frees [cost] annually. I need authority to begin that process."*

---

## 8. Integration Architecture

**Type:** Ground truth · **Layer:** Application · **Standard time:** 12–20 weeks · **VAF time:** 2–3 weeks · **Saving:** ~80%

### Layer 1 — Extraction Guide

**Questions:**
- *"If we turned off [system X] tomorrow, what breaks in the next 24 hours?"* — Real-time dependencies not in documentation.
- *"Does anything send data to [system X] that is not in the official documentation?"* — Permission to name undocumented connections.
- *"Does anything read directly from [system X]'s database rather than through an API?"* — Direct database reads — highest-risk undocumented integrations.
- *"Who would know if [system X] had been modified to connect to something new in the last 12 months?"* — Names the knowledge holder.

**Red flags:** Operator describes a connection the system owner does not know about. System has no named operator — only a vendor. Direct database connections confirmed.

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Scope — decision served | The specific change or decommission. Full-landscape mapping is not the scope. |
| Systems in scope | Only systems relevant to the named decision. |
| Documented integrations | System A → B, protocol, data, owner each end, direction. |
| Undocumented integrations | Every connection not in existing documentation. Discovery date, how found. |
| Direct database connections | Named separately. High risk. |
| Decommission blockers | Integration blocking planned change. System, dependency, resolution path. |
| Unknown connections | Systems with no named operator. Unquantified risk position. |
| Accuracy date and maintainer | Operator — not architecture team. |

**Template sentence:** *"We found [X] connections not in any existing documentation. [Y] are blockers to the planned change. The planned timeline needs to extend by [estimate], or we need a decision to accept the risk and proceed."*

---

## 9. Solution Architecture Document

**Type:** Control mechanism · **Layer:** Application · **Standard time:** 4–8 weeks · **VAF time:** 2–3 days · **Saving:** ~80%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Decision made | The solution chosen. One paragraph. Past tense. |
| Options rejected | Every option not chosen. For each: what it was, why rejected in one sentence. |
| Assumptions | What must be true for this decision to remain correct. |
| Constraints accepted | Acknowledged and accepted. Cannot be raised later as blockers. |
| Principles compliance | Compliant principles named. Non-compliance: exception and approval. |
| Invalidation triggers | Conditions under which this decision becomes wrong. |
| Decision owner and date | Named individual. Date of decision. |

**Template sentence:** *"We decided on [solution]. We evaluated [alternative] and rejected it because [reason]. This decision depends on [key assumption]. [Decision owner] made this on [date]. I need [ratification / escalation decision]."*

---

## 10. Conceptual Data Model

**Type:** Decision instrument · **Layer:** Data · **Standard time:** 4–8 weeks · **VAF time:** 1 day · **Saving:** ~88%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Entity in dispute | The entity requiring definitional alignment. |
| Agreed definition | Verbatim. Dated. Signed off by named authority. Business language. |
| What this explicitly excludes | The boundary condition. As important as the definition. |
| Definition authority | One named person. Not a committee. |
| Unresolved disputes | Nature. Owner. Date required. |
| Downstream dependencies | Systems, reports, decisions depending on resolution. |
| Session date | Revision trigger: any system change consuming this entity. |

**Template sentence:** *"Finance counts [X] customers. Sales counts [Y]. The board report uses whichever number is convenient. This has caused [consequence]. We have agreed a definition: [definition]. I need you to confirm [named person] as the authority so it holds across the organisation."*

---

## 11. Data Flow Diagram

**Type:** Control mechanism · **Layer:** Data · **Standard time:** 4–6 weeks · **VAF time:** 3–5 days · **Saving:** ~75%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Regulatory scope | The specific regulation. Named. |
| Personal data categories | Required by regulation. No broader. |
| Collection point | Every entry point. Named. |
| Flow path | Every system in sequence from collection to deletion. |
| Shadow copies | Any system retaining copies outside primary record. |
| Third-party transfers | Every external party. Legal basis for each. |
| Deletion mechanism | What is deleted, from which systems, on what trigger. Confirmed. |
| Compliance gaps | Flows without legal basis, retention schedule, or deletion mechanism. Findings. |
| Accuracy date and owner | Named owner. Not architecture team. |

**Template sentence:** *"We found [X] gaps. [Y] third-party transfers have no documented legal basis. The highest risk is [gap] — if identified in a regulatory audit, the consequence is [consequence]. I need legal review of [specific transfers] before [date]."*

---

## 12. Master Data Map

**Type:** Ground truth · **Layer:** Data · **Standard time:** 6–10 weeks · **VAF time:** 2–3 days · **Saving:** ~75%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Master entity | One row per entity. |
| Systems claiming authority | Every system claiming or implying authority. |
| Nature of the conflict | Different field coverage, update frequency, owner. |
| Actual authority | If established — name it with the governance decision. If not — say so explicitly. |
| Historical conflicts | Past instances. What happened. Resolved or not. |
| Arbitration mechanism | Process for resolving conflicts. If none — primary finding. |
| Resolution owner | Named executive with authority to establish true source of record. |
| Resolution deadline | Unresolved = named risk position. |

**Template sentence:** *"We have [X] systems that each believe they are the source of truth for [entity]. They disagree [description]. The operational cost is [consequence]. This cannot be resolved technically until a governance decision is made: which system is authoritative, confirmed by you, effective [date]."*

---

## 13. Technology Roadmap

**Type:** Decision instrument · **Layer:** Technology · **Standard time:** 8–12 weeks · **VAF time:** 3–5 days · **Saving:** ~80%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Components in scope | Only relevant to current strategic decisions. |
| Dependency sequence | What cannot start until what else is done. A list — not a timeline. |
| Funded initiatives | Each with: what it depends on, what depends on it, approved funding. |
| Unfunded dependencies | Items required but not funded. Named as risk positions. |
| Date range estimates | Ranges tied to named dependencies. Not committed dates. |
| Hidden initiatives | Funded work not previously in roadmap. Dependency impact assessed. |
| Invalidation triggers | Conditions that would change the sequence. |

**Template sentence:** *"Before [funded initiative] can begin, we need [unfunded prerequisite]. That prerequisite has no budget. Without a funding decision, [initiative] cannot start as planned. I need a funding decision or a revised commitment."*

---

## 14. Technology Standards Catalogue

**Type:** Control mechanism · **Layer:** Technology · **Standard time:** 4–8 weeks · **VAF time:** 1 day · **Saving:** ~90%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Approved technology | Name and category. |
| What this prevents | Specific sprawl or risk. One sentence. |
| Exception process | Step by step. Who requests, reviews, approves. Must be achievable in 48 hours. |
| Exception record | Every approved exception. Technology, requestor, reason, approval date, review date. |
| Cost of non-standard | Quantified where possible. |
| Enforcement authority | Named role with authority to block non-standard. One person. |

**Template sentence:** *"In [year], [technology] was selected without architecture review. It cost [amount] to remediate and cannot be integrated with our standard stack. For the catalogue to function, [named role] needs explicit authority to block non-standard selections. I need that authority confirmed."*

---

## 15. Infrastructure Architecture

**Type:** Ground truth · **Layer:** Technology · **Standard time:** 10–16 weeks · **VAF time:** 2–3 weeks · **Saving:** ~80%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Scope — critical path | Not full landscape. Named components only. |
| Component and owner | Named individual operator. Not team. |
| Upstream dependencies | What this depends on. Failure consequence. |
| Downstream dependencies | What depends on this. Named. |
| Recovery procedure | Actual steps. Validated with operator. Not policy version. |
| Recovery time (actual) | From last test or incident. Not the target. |
| Human knowledge dependencies | Any recovery requiring specific named individual. Flag. |
| Last validation date | When last tested under realistic conditions. |
| Accuracy date and maintainer | Operator who maintains. Not architecture team. |

**Template sentence:** *"Our infrastructure documentation was [accuracy assessment] before this review. We found [X] components whose recovery depends on named individual knowledge. [Y] recovery procedures have not been tested in 12+ months. I need [DR test schedule / knowledge documentation sessions] approved before [date]."*

---

## 16. Architecture Decision Record

**Type:** Ground truth · **Layer:** Governance · **Standard time:** 2–4 hours · **VAF time:** 20 minutes · **Saving:** ~80%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Decision | What was decided. One paragraph. Past tense. Written the same day. |
| What was rejected | Every alternative considered. For each: what it was, why not chosen. Written while fresh. |
| What would change this decision | Conditions for revisiting. If none — set a mandatory review date. |
| Decision owner | One named individual. Not a team. |
| Date | Date of the decision. Not document date. |

**Note:** No template. No review cycle. No approval chain. The discipline is writing it immediately. Format is irrelevant.

**Referencing language (when challenged):** *"On [date], [owner] decided [decision] after evaluating [alternatives]. The conditions assumed were [assumptions]. Those conditions [have/have not] changed."*

---

## 17. Architecture Compliance Review

**Type:** Control mechanism · **Layer:** Governance · **Standard time:** 2–4 weeks · **VAF time:** Half day · **Saving:** ~90%

### Layer 1 — Extraction Guide

Two questions. Everything else is context.

1. Does this solution compound or reduce technical debt over five years?
2. Does this solution violate an architecture principle?

If neither produces a clear finding: advisory. If either does: blocking — with a named recommendation, not a committee referral.

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Solution reviewed | Name. Reference to SAD. |
| Q1: Debt trajectory | Compound or reduce? Specific evidence. One paragraph. |
| Q2: Principle compliance | Violation? Name the principle, describe the violation, name the exception path. |
| Finding | Advisory or Blocking. Named clearly. |
| Recommendation | If blocking: specific change required, or exception approval path and who must approve. |
| Reviewer and date | Named architect. Date. |

**Template sentence:** *"The compliance review of [solution] found [finding]. Specifically, [one sentence]. The recommendation is [specific action]. If we proceed without this change, the consequence is [cost / risk]. I need [decision] from [named person] before [date]."*

---

## 18. Architecture Roadmap

**Type:** Decision instrument · **Layer:** Governance · **Standard time:** 8–16 weeks · **VAF time:** 1 week · **Saving:** ~85%

### Layer 2 — VAF Template

| Field | Guidance |
|---|---|
| Funded initiatives (in dependency order) | Named. Dependency they wait on. Dependency they create. Funding confirmed. |
| Unfunded items | Required but not funded. Named explicitly as risk positions — not omitted. |
| Dependency sequence | What cannot start until what else is done. The sequence — not the dates. |
| Date range estimates | "Contingent on X" — not calendar commitments. |
| Strategic priorities served | Each initiative mapped to a named priority. If no priority named — not on this roadmap. |
| Sequencing conflicts | Any initiative whose sequence conflicts with discovered dependencies. |
| Invalidation triggers | Conditions that would change this roadmap. Named. |
| Owner and review trigger | Named owner. Review triggered by conditions — not annual calendar. |

**Template sentence:** *"We have [X] funded initiatives for [period]. Before [most important initiative] can begin, we need [prerequisite] — which is not funded. Without [prerequisite], [initiative] cannot start as planned. The cost of the delay is [consequence]. I need a funding decision on [prerequisite] or a revised commitment on [initiative]."*

---

## Sources

See [SOURCES.md](/research/SOURCES.md) for the complete graded bibliography.

Key anchors for this manual:

- **Kotusev et al., Information and Software Technology, 2022** — empirical basis for artefact type classification across 47 organisations
- **Gartner ITScore** — practice maturity level outcomes (15–20% project success, 10–15% IT cost per level)
- **CB Insights, 2024** — 43% PMF failure as root cause; 70% capital depletion as symptom
- **Koning, Hasan & Chatterji, Management Science, 2022** — 30–100% performance improvement with validation discipline

---

*Velocity Architecture Framework™ · ZenCloud Global Consultants · May 2026*  
*Free to use. Free to share. Attribution appreciated.*
