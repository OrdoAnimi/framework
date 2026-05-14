# EA Artefact Value Over Time
## Four Trajectory Types and the Industry Evidence Base

**Author:** ZenCloud Global Consultants  
**Published:** May 2026  
**Classification:** Research Analysis

---

## The question

Do industry standards provide adequate tools for measuring EA artefact value over time?

The short answer: no — not at the artefact level.

Industry standards (Gartner ITScore, TOGAF maturity models, Forrester EA state reports) measure practice maturity progression and its aggregate outcomes. They do not measure individual artefact value trajectories. The artefact-level longitudinal study does not exist in the published literature.

This paper presents what the evidence does support: four structurally derived value trajectory types, grounded in artefact type logic and EA debt research, with the industry standard evidence mapped to what it can and cannot claim.

---

## What industry standards measure

### Gartner ITScore — Five EA Maturity Levels

Nonexistent → Reactive → Functioning → Integrated → Ubiquitous

Measured across eight dimensions: stakeholder support and involvement, team resources, architecture development method, organisational integration, deliverables, EA governance, metrics, and stakeholder perceptions.

**Empirical outcomes by level progression:**
- Advancing one maturity level: 15–20% improvement in project success rates
- Advancing one maturity level: 10–15% reduction in IT costs
- Mature EA practices overall: ~30% faster implementations
- Mature EA practices overall: ~25% lower total cost of ownership

Source: Gartner ITScore benchmarks; ASUG EA community analysis, 2025.

These are practice-level outcomes. Artefact quality is a dimension of maturity — it is not measured independently. The figures above cannot be attributed to specific artefacts.

### Gartner IT project success data (2024)

Only 48% of digital projects currently meet or exceed goals. Digital vanguard organisations — those with architectural co-ownership governance — reach 71%. The separator is architectural discipline, which is artefact-dependent but not artefact-specific.

### The research gap — stated explicitly

> "The different ways of evaluating architecture have mainly used a top-down approach deriving measures from theory rather than a bottom-up approach using empirical and practical studies. Research is especially lacking regarding empirical studies of how EA evaluation actually takes place."

— ResearchGate, EA ROI Framework Review (finding remains current as of 2024)

Artefact-level longitudinal ROI studies do not exist in the published literature. Anyone citing specific ROI figures for an individual artefact type is citing an industry blog, not research.

---

## EA debt research — what it adds

The EA debt literature provides the closest available evidence for artefact value decay over time.

**RWTH Aachen / KTH (CEUR-WS Vol. 2628, 2020)**

EA debt accumulates when artefacts are not maintained. The EADM framework identifies that identifying EA debts is intricate without systematic approaches. Future research directions include characterising EA debts and their indicators, assisting EA observation, and providing valuation criteria.

**SAC '26 — ACM/SIGAPP proceedings**

Enterprise Architecture Debt (EA Debt) arises from suboptimal design decisions and misaligned components that degrade an organisation's IT landscape over time. EA Smells are early indicators — currently detected manually or only from structured artefacts, leaving unstructured documentation under-analysed.

**Yallo (2026)**

Architectural debt expands faster than technical debt. Fragmented ownership, shifting priorities, and capability design weaknesses accelerate architectural drift. In the early stages, shifting enterprise priorities begin to introduce inconsistencies in design intent. As delivery progresses, fragmented ownership allows parallel decisions to diverge — creating mid-stage architectural drift that is rarely visible at the time.

**Architecture Technical Debt lifecycle study (arxiv, 2501.15387)**

Resolving ATD improves software quality in the short term but can make the architecture more complex by centralising dependencies. FAN-IN increases 57.5% on average post-repayment. ATD files are modified less frequently than non-ATD files, with changes accumulated in high-dependency portions.

---

## The four trajectory types

These trajectory types are structurally derived — not empirically measured at the artefact level. They represent the logical consequence of artefact type function combined with EA debt research on what happens when artefacts are and are not maintained.

### Type 1 — Decision instruments: front-loaded

**Pattern:** Value peaks at the point of commitment and decays as assumptions age.

**Mechanism:** The decision instrument's value is the commitment it produces. Once made, that commitment holds until the context changes. As context changes without the artefact being reviewed, the artefact provides false confidence — making it actively misleading rather than simply outdated.

**Implication:** Refresh triggers are mandatory. An Architecture Vision without a named refresh trigger is a liability after 12–18 months in a changing environment.

**Artefacts:** Architecture Vision, Application Portfolio (TIME classification), Technology Roadmap, Architecture Roadmap, Conceptual Data Model.

### Type 2 — Control mechanisms: slow build, stable plateau

**Pattern:** Value accumulates as the exception record grows, then plateaus when enforcement culture is established.

**Mechanism:** The exception process creates a decision record. The decision record creates accountability. The accumulation of accountability records over time is the forensic value. The plateau represents a mature enforcement culture where the control is self-sustaining.

**Implication:** Value is cumulative. Abandoning the exception process destroys the accumulated record and the enforcement culture simultaneously.

**Artefacts:** Architecture Principles, Technology Standards Catalogue, Data Flow Diagram, Architecture Compliance Review, Solution Architecture Document (as decision log).

### Type 3 — Signal generators: spike, then decay without action

**Pattern:** Value peaks at delivery, decays without structural response within 6–12 months.

**Mechanism:** The signal is fresh at delivery. It is at maximum credibility and relevance. Without a named structural response — an action owner, a funded decision, a governance change — the signal ages into evidence of acknowledged dysfunction. This is worse than no artefact: it demonstrates awareness without accountability.

**Implication:** A signal generator without a named action owner assigned at delivery has negative expected value after 12 months.

**Artefacts:** Business Capability Map (heat map), Value Stream Map, Organisation Map, Master Data Map (conflict documentation).

### Type 4 — Ground truth artefacts: accuracy-dependent bifurcation

**Pattern:** Two divergent trajectories. Maintained artefacts hold value indefinitely. Unmaintained artefacts decay at the rate of organisational change.

**Mechanism:** The value is entirely in the accuracy of the record. A current Integration Architecture that documents every integration relevant to the next planned change is worth the time it prevents in incident response and decommission planning. The same document, 18 months unmaintained, documents a landscape that no longer exists and will actively mislead anyone relying on it.

**Implication:** Maintenance is not optional — it is the entire value proposition. Maintenance must be owned by the people closest to the subject matter: operators, not architects.

**Artefacts:** Integration Architecture, Infrastructure Architecture, Business Process Model (as-is), Architecture Decision Records.

---

## What this means for practice

The four trajectory types produce three practical implications:

**1. Maintenance obligations differ by type.** Control mechanisms need the exception process enforced. Decision instruments need refresh triggers named. Signal generators need action owners assigned. Ground truth artefacts need continuous operator-level maintenance. Applying the same annual review cycle to all four types is the primary maintenance failure in EA practice.

**2. The cost of drift is asymmetric.** A stale Architecture Vision is an outdated document. A stale Infrastructure Architecture is a live risk — MTTR increases directly when incident response teams work from inaccurate documentation. The consequences of drift are not equivalent across types.

**3. The production sequence affects value.** A decision instrument produced before the decision conversation has been had is not yet an artefact — it is preparation material. A ground truth artefact produced from documentation rather than observation records what was supposed to be true, not what is true. Sequence matters: conversation first, record after.

---

## Sources

| Source | Type | Relevance |
|---|---|---|
| Gartner ITScore | Industry standard | Maturity level outcomes; 15–20% project success, 10–15% IT cost per level |
| ASUG EA community analysis, 2025 | Industry analysis | ~30% faster impl, ~25% lower TCO with mature EA governance |
| ResearchGate EA ROI framework review | Academic case study | Empirical evaluation of EA evaluation remains lacking |
| RWTH Aachen / KTH — CEUR-WS 2628, 2020 | Academic | EA debt management framework; identification and valuation criteria |
| SAC '26 — ACM/SIGAPP proceedings | Peer-reviewed | LLM-based EA debt detection; EA Smells as debt indicators |
| Yallo, 2026 | Practitioner analysis | Architectural debt expands faster than technical debt; fragmented ownership as accelerant |
| arxiv 2501.15387 | Academic | Architecture technical debt lifecycle; FAN-IN/OUT changes post-repayment |
| Gartner IT project success data, 2024 | Industry research | 48% vs 71% project success — governance discipline as separator |

---

*ZenCloud Global Consultants · May 2026*  
*Value trajectory types are structurally derived, not empirically measured at the artefact level. The longitudinal artefact-level study does not exist.*
