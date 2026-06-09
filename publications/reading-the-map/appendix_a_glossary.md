# Appendix A — Full Glossary

*Reading the Map · Reference*

---

Every bold term from the book, defined. Each entry gives the **plain-English translation** first — what it actually means — followed by a one-line note on why it matters or when it comes up. Where a term has a formal source, it is named. Alphabetical.

---

## A

**ADM (Architecture Development Method)** — TOGAF's cycle of phases for developing an enterprise architecture, from vision through to governance. *The method most organisations borrow from, ideally used selectively rather than run in full as ritual.*

**Advisory function** — an architecture body that offers expert opinion others may take or leave, as opposed to a design authority that decides. *The distinction matters because an advisory body dressed in design-authority language produces governance theatre.*

**Application architecture** — the view of the software estate: what systems exist, what they do, and how they connect. *The BDAT layer where most IT investment and most accumulated debt live.*

**Application portfolio** — a structured, assessed catalogue of the applications an organisation depends on, mapped to capabilities. *The instrument that makes the application estate visible and governable; most organisations have a licence register, not a portfolio.*

**Architecture Building Block (ABB)** — a required capability described in solution-neutral terms — what is needed, before what implements it. *Specified before the Solution Building Block; reversing the order corrupts the requirement.*

**Architecture debt** — the accumulated cost of structural decisions that constrain future options, living between systems rather than inside them. *More dangerous than technical debt: wider scope, lower visibility, poorer reversibility. Must be translated into financial consequence to be acted on.*

**Architecture governance** — the practice of ensuring that decisions made for the whole are honoured by the parts. *Makes good analysis stick; its instrument is the Architecture Review Board.*

**Architecture principle** — an agreed commitment that guides architectural decisions (e.g. "cloud-first", "single patient identity"). *Rules with a why; transmitting the why is what makes them followed rather than evaded.*

**Architecture Review Board (ARB)** — the standing body that exercises architecture governance. *Works only with a clear threshold, real authority, and honesty about whether it decides or merely advises.*

**Architecture roadmap** — the ordered sequence of changes that moves an estate from current to target state, with transition states. *Not a project plan; answers "what, in what order, and why", not "what tasks by when".*

**Architecture Theatre** — governance that looks rigorous but produces nothing binding. *Recognisable by its inability to name a single decision it has prevented or reversed.*

**Architecture Vision** — a short, agreed statement of what a piece of architectural work is for: problem, stakeholders, scope, success, constraints, risks, approach. *TOGAF Phase A; the cheapest phase and the most expensive to skip.*

**ArchiMate** — the standard visual notation for enterprise architecture, showing business, application, and technology layers and their relationships. *Its signature value is the vertical trace from a business need down to its infrastructure.*

---

## B

**Baseline (current state)** — the documented architecture as it actually is. *Document it to the level of detail the decision requires, and no more — resist the pull to completeness.*

**BDAT** — the four architecture domains: Business, Data, Application, Technology. *The standard decomposition; each domain is a different view of the same enterprise.*

**Business architecture** — how the organisation is structured to do its work: capabilities, processes, value streams. *The top BDAT layer; what the organisation does, independent of the technology.*

**BIZBOK** — the Business Architecture Body of Knowledge, the reference for business architecture practice. *The domain framework for the business layer, including capability mapping.*

**Building block** — a reusable component of an architecture, defined once and used in many places. *Comes in two kinds: Architecture Building Blocks (what is needed) and Solution Building Blocks (what implements it).*

---

## C

**Capability** — a stable ability the organisation must have, independent of how or who delivers it (e.g. "manage patient records"). *The right unit of analysis because capabilities change slowly, outlasting reorganisations and process changes.*

**Capability map** — a structured picture of what an organisation does, organised into levels. *Read at board altitude (Level 1) or programme altitude (Level 3); becomes a decision tool when heat-mapped.*

**COBIT** — the framework for governing an enterprise's use of IT. *Sits downstream of architecture; the control environment, often invoked at audit time.*

**Component diagram** — a diagram of systems, their interfaces, and their dependencies. *Read for fragility (single points of failure, cycles) and, crucially, for what has been left out.*

**Cost of inaction** — the quantified, growing cost of not addressing a problem. *The phrase that unlocks budget by reframing a discretionary improvement as a non-discretionary cost already being incurred.*

**Current state** — see Baseline.

---

## D

**Data architecture** — how information is defined, owned, mastered, and made trustworthy. *The BDAT domain everyone underestimates; ownership and master data are its hardest questions.*

**Data owner** — the person accountable for whether a data entity is correct and trustworthy. *An unowned data entity is a problem nobody is fixing; ownership voids are where data quality dies.*

**Decision authority / design authority** — a body that makes binding architectural decisions, as opposed to one that only advises. *"No" must mean no, or it is not a design authority.*

**Decision latency** — the gap between when a decision could be made and when it is, and the cost of that gap. *Deferring a decision is itself a decision with a price, paid in money, risk, and forgone opportunity.*

**Dependency** — a relationship in which one thing requires another to function. *Reading dependency direction tells you the blast radius of a failure; hidden dependencies wreck migration plans.*

---

## E

**Enterprise architect** — the role holding the broadest, longest view of the estate and its relationship to strategy. *The most senior and abstract architecture role; risks losing touch with delivery.*

**Enterprise architecture (EA)** — the discipline of seeing and shaping the whole technology estate so the parts serve the organisation rather than fragment it. *A way of thinking — system-seeing, consequence-tracing — as much as a job title.*

**Event-driven** — an architecture pattern where systems react to events rather than calling each other directly. *Decouples systems and scales well; fails by becoming hard to trace and debug.*

---

## G

**Gap analysis** — the disciplined identification of the differences between current and target state, categorised and prioritised. *Its key insight: the most important gaps (enablers) are rarely the most obvious ones (visible problems).*

**Governance** — see Architecture governance.

---

## H

**Heat map** — a capability map coloured to show health (red/amber/green) against importance and performance. *The colours name business-level symptoms, not technical causes; reading red as "replace the system" is the classic error.*

**Horizon** — a time band on a roadmap, less precise the further out it goes. *Near horizons are concrete and costed; far horizons are directional and honestly vague.*

**Hub-and-spoke** — an integration pattern where systems connect through a central hub rather than to each other. *Collapses the connection count; fails by making the hub a critical single point.*

**Human-machine boundary** — within an AI-augmented capability, the designed division between machine judgement and human judgement. *Where accountability is designed in or accidentally lost; the central question of the People-Process-Technology-AI model.*

---

## I

**Integration architecture** — the description of how applications connect: what data flows, by what mechanism, with what error handling. *The integration map reveals the estate's fragility, especially its point-to-point connections.*

**Intent gap** — the distance between what was intended and what was understood, as meaning is lost through organisational handoffs. *Dooher's central concept; closed by teaching the why, not just policing the what.*

**ITIL** — the framework for IT service management — running what architecture builds. *Often the most consistently practised framework in an organisation, and rarely thought of as architecture.*

---

## M

**Master data** — the single authoritative version of a key data entity (e.g. patient identity). *Its absence forces every system to build its own version, the deepest kind of data debt.*

**Microservices** — an architecture pattern decomposing an application into many small, independently deployable services. *Buys flexibility; fails by operational sprawl and distributed complexity.*

---

## P

**Pattern** — a named, recurring shape of solution with documented consequences and failure modes. *Recognising a pattern imports the experience of everyone who met it before; naming a pattern is diagnosing its risk.*

**People-Process-Technology (PPT)** — the traditional triad for designing capabilities. *Davis argues AI breaks it, requiring a fourth element: People-Process-Technology-AI.*

**Point-to-point integration** — systems wired directly to each other rather than through a shared platform. *Simple per connection, disastrous in aggregate; fails by unmanageable proliferation and silent breakage.*

**Portfolio** — see Application portfolio.

---

## R

**Rationalisation** — the programme of decommissioning, consolidating, and remediating an application estate based on the portfolio assessment. *Hard not because the answer is unclear but because executing it requires governance with authority.*

**6R model** — the six dispositions for an application: Retire, Retain, Rehost, Replatform, Repurchase, Refactor. *Turns the portfolio assessment from diagnosis into committed decision.*

**Refactor** — re-architect an application significantly to remove debt and fit the target. *The most expensive 6R disposition; reserved for strategic capabilities with no commercial alternative.*

**Rehost (lift-and-shift)** — move an application to new infrastructure unchanged. *Fast and low-risk; carries the application's debt forward intact.*

**Repurchase** — replace an application with a different product, typically SaaS. *Right when the capability is a commodity the organisation has no reason to run itself.*

**Replatform** — move an application with modest changes to exploit the new environment. *Between rehost and refactor in cost and benefit.*

**Retain** — keep an application unchanged, as an active decision with a review date. *Legitimate, but passive retention is how estates ossify.*

**Retire** — decommission an application. *The most-identified and least-executed disposition, because every retirement has a constituency.*

---

## S

**SABSA** — the framework for security architecture, tracing security controls to business risk. *The domain framework for security; often absent, leaving security as a compliance checklist.*

**Sequence diagram** — a diagram of messages between participants over time, read top to bottom. *The most powerful artefact for surfacing failure, because it represents time and therefore failure-in-time.*

**Solution Building Block (SBB)** — the specific product or technology selected to fulfil an Architecture Building Block. *Selected after the ABB is defined; selecting it first corrupts the requirement.*

**Strategic capability** — the connection of a technical investment to an ability the organisation has decided matters. *One of the phrases that unlocks budget, by reframing spend from housekeeping to strategy.*

**Solution architect** — the role translating enterprise direction into a workable design for a specific programme. *Closest to delivery; the connective tissue between the enterprise view and the teams building.*

---

## T

**Target state** — the documented architecture as the organisation intends it to become. *Usually contested, because different stakeholders want different futures; the architect's job is to make the trade-offs explicit.*

**Technical debt** — the accumulated cost of implementation shortcuts, living inside systems. *Distinct from architecture debt, which lives between systems and is harder to reverse.*

**Technology architecture** — the infrastructure and platforms applications run on. *The foundation BDAT layer; Meridian's VMware crisis is a technology-architecture event with estate-wide consequences.*

**TOGAF** — The Open Group Architecture Framework, the most widely used EA method framework. *Provides the ADM; most valuable used selectively as a thinking structure rather than performed in full.*

**Transition architecture (transition state)** — a defined, stable, survivable intermediate configuration between current and target state. *Designed for safety rather than elegance, because organisations live in their transition states for months or years.*

---

## V

**Value chain** — on a Wardley map, the chain of needs from the visible user need down to the invisible foundations. *The vertical axis of a Wardley map; height means closer to the user need.*

---

## W

**Wardley map** — a strategy diagram plotting components by position in the value chain (vertical) and evolutionary stage (horizontal). *The one architecture diagram about the future; shows what is commoditising and where to invest effort.*

**Wave** — a coherent bundle of related change on a roadmap that moves the architecture between stable states. *Distinguishes a roadmap (a sequence of states) from a backlog (a list).*

---

## Z

**Zachman Framework** — a classification grid of six interrogatives crossed with six perspectives (36 cells), each a distinct kind of description. *Not a method; a taxonomy. Its lesson: the same system looks genuinely different from different cells, and confusing the cells causes much avoidable conflict.*
