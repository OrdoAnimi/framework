# Enterprise Architecture Artefacts — True Purpose, Value Metrics, and Empirical Evidence

**Author:** ZenCloud Global Consultants  
**Published:** May 2026  
**Classification:** Research Synthesis  
**Scope:** EA artefact effectiveness · MVP/MLP empirical evidence · Value-over-time analysis

---

## Executive Summary

Enterprise architecture produces artefacts. Most organisations treat them as documentation obligations. This report argues they are not. Every core EA artefact resolves to one of four true purposes: a decision instrument, a control mechanism, a signal generator, or a ground truth record. The purpose determines the value trajectory. The value trajectory determines the maintenance obligation. Organisations that confuse these types produce artefacts that look complete and deliver nothing.

The second question this report addresses is whether industry standards provide adequate tools for measuring artefact value over time. The answer is no — not at the artefact level. Standards measure practice maturity and produce aggregate outcomes. Artefact-level value curves must be derived from first principles, EA debt research, and the decay logic inherent in each artefact type.

The third question concerns MVP and MLP. Both are invoked in EA and product contexts as empirically grounded approaches. Only MVP has defensible empirical backing. MLP is a practitioner construct with no comparative effectiveness data. This distinction matters when either concept is used to justify investment decisions.

---

## Part 1: Core EA Artefacts — True Purpose

### The Four Types

Every EA artefact resolves to one of four functional categories. The stated purpose and the true purpose are frequently different. The gap between them is where investment is wasted.

| Type | Mechanism | Failure mode |
|---|---|---|
| **Decision instrument** | Forces commitment, shifts burden of proof | Produced without forcing a decision |
| **Control mechanism** | Operates without authority through exception process | No exception process attached |
| **Signal generator** | Makes invisible problems undeniable | Acknowledged and not acted upon |
| **Ground truth** | Accuracy-dependent organisational memory | Produced once and allowed to drift |

---

### Strategy Layer

**Architecture Vision** — *Decision instrument*

Forces the organisation to commit to a direction before money is spent. Exposes disagreement between executives that consensus language was hiding. The document is a by-product. The argument is the point. A Vision that does not produce a commitment is a slide deck.

**Business Capability Map** — *Signal generator*

Surfaces capability gaps that org charts and process maps obscure. The heat-mapped variant is the only version that matters — it shows where investment is misallocated before anyone has to say it out loud. Produced and filed without structural response, it becomes evidence of an acknowledged problem that was not addressed.

**Architecture Principles** — *Control mechanism*

A veto instrument that operates without authority. When a principle is invoked, the burden of proof shifts to the requester. Poorly maintained principles become noise. Maintained ones are the fastest way to kill bad decisions at the lowest organisational cost. Value depends entirely on the exception process — without it, the principles catalogue is a list.

---

### Business Layer

**Value Stream Map** — *Signal generator*

Makes wait time visible. Every handoff is a latency point that no-one owns. The map does not solve the problem — it makes the problem undeniable so someone has to own it. The as-is version generates the most signal. The to-be version is aspirational without structural change.

**Business Process Model** — *Ground truth*

The as-is version documents what actually happens — not what the policy says. The gap between the as-is and the to-be is where transformation risk lives. Most organisations skip the as-is and then wonder why the to-be fails. A to-be without an as-is baseline is not a model. It is a wish.

**Organisation Map** — *Signal generator*

Identifies accountability voids. When a capability exists but no role owns it, the map shows white space that the org chart never will. Also reveals duplicate ownership — the political problem no-one wants to name.

---

### Application Layer

**Application Portfolio** — *Decision instrument*

The TIME model classification (Tolerate / Invest / Migrate / Eliminate) is the only output that drives budget. Everything else is cataloguing. Without explicit classification, the portfolio is a list, not a position. A portfolio that has not forced TIME decisions has not been completed.

**Integration Architecture** — *Ground truth*

The as-is version is a liability map. Every undocumented integration is a decommission blocker. Most organisations discover these dependencies mid-project — after the commitment is made. The artefact's value is in the surprises it surfaces, not the connections everyone already knew about. Maintenance burden is the highest in the artefact set.

**Solution Architecture Document** — *Control mechanism*

A decision log in disguise. Every assumption, constraint, and option rejected is a future escalation avoided — if recorded. SADs that only describe the solution chosen have no forensic value. The ones that record what was rejected, and why, are the ones that survive audit.

---

### Data Layer

**Conceptual Data Model** — *Decision instrument*

Forces the business to agree on what a thing *is* before anyone builds it. "What is a customer?" cannot be answered by IT. The CDM is the mechanism that forces the business to answer it on record, so the data model built below it has a mandate.

**Data Flow Diagram** — *Control mechanism*

Privacy and regulatory compliance instrument. GDPR, Privacy Act, and equivalents require organisations to demonstrate they know where personal data flows. This artefact is the evidence. Organisations that treat it as documentation are exposed. Those that treat it as a control own the audit response.

**Master Data Map** — *Ground truth*

Exposes the master data fiction. Most organisations have no authoritative source — they have several competing systems each claiming authority. The map makes that conflict explicit. Resolving it is a political act, not an architectural one. The EA's job is to make the conflict undeniable.

---

### Technology Layer

**Technology Roadmap** — *Decision instrument*

A sequencing instrument, not a timeline. The critical output is dependency order — what must change before what can change. The dates are almost always wrong. The sequence is almost always right. Organisations that treat it as a calendar fail. Those that treat it as a dependency graph use it.

**Technology Standards Catalogue** — *Control mechanism*

Procurement veto and vendor sprawl prevention. Without it, every project selects its own stack. With it, deviations require an exception — which requires justification — which creates a decision record. The standards themselves matter less than the exception process.

**Infrastructure Architecture** — *Ground truth*

Continuity and risk instrument. The as-is version is what incident response teams reach for at 2am. If it does not reflect reality, every major incident takes longer to resolve. Its accuracy is a direct multiplier on MTTR. Organisations that let it drift pay in outage minutes.

---

### Governance Layer

**Architecture Decision Record** — *Ground truth*

Organisational memory. The decision matters less than the context that produced it. ADRs that record constraints, rejected options, and the assumptions live at the time allow future architects to know whether a decision is still valid — or whether the world it was made in no longer exists.

**Architecture Compliance Review** — *Control mechanism*

The moment architecture has teeth. Not a review of diagrams — a review of decisions. Compliance reviews that only check technical conformance are checkbox exercises. The ones that evaluate whether a solution will compound or reduce technical debt over five years are the ones worth running.

**Architecture Roadmap** — *Decision instrument*

Portfolio investment sequencer. Not a project plan — a statement of what the organisation is willing to fund, in what order, accepting which dependencies. The gaps in the roadmap are as important as what is on it. Unfunded capabilities are a risk position, not an omission.

---

## Part 2: Time Taken vs Value — The Honest Assessment

### Position by Artefact

The following positions are derived from artefact type logic, EA debt research, and practice evidence. They are not drawn from a single longitudinal study — no such study exists at the artefact level.

**High value / low time investment**

- Architecture Decision Record — lowest time per unit of value in the entire set. Compounds over time: each ADR reduces future ambiguity.
- Architecture Principles — cheap to produce, high leverage. Operates as a veto instrument without requiring authority.

**High value / high time investment**

- Integration Architecture — very high maintenance burden. As-is version is a liability map. Undocumented integrations are decommission blockers.
- Infrastructure Architecture — high maintenance. Accuracy is a direct multiplier on MTTR. Drift is measured in outage minutes.
- Architecture Roadmap — sequencing logic is the output that matters. Dates are almost always wrong. Dependency order is almost always right.
- Technology Roadmap — same pattern. Treat as a dependency graph, not a calendar.

**Moderate value / moderate investment**

- Business Capability Map — disproportionate signal value when heat-mapped. Often produced once and not maintained.
- Application Portfolio — TIME classification drives budget. The catalogue without classification is not complete.
- Data Flow Diagram — non-negotiable in regulated environments. Regulatory compliance instrument, not documentation.

**Value-dependent on what is recorded**

- Solution Architecture Document — SADs that only describe the chosen solution have no forensic value. Those that log rejected options and assumptions survive audit.
- Business Process Model — as-is delivers most value. To-be without as-is is the most common failure mode.

**Degrading artefacts — value collapses without action**

- Architecture Vision — decays as assumptions age. A two-year-old Vision that has not been refreshed is actively misleading, not neutral.
- Value Stream Map — signal is fresh at delivery. Without structural response within 6–12 months, the artefact becomes evidence of an acknowledged problem not addressed.

---

## Part 3: Value Over Time — Four Trajectory Types

### The Framework

EA artefact value does not behave uniformly over time. Four distinct trajectories exist. The type determines the maintenance obligation.

**Type 1 — Decision instruments: front-loaded**

Peak value is at the point of commitment. Value decays as assumptions age and the decision context changes. Architecture Vision, Application Portfolio (TIME classification), Conceptual Data Model, Architecture Roadmap.

*Implication:* Refresh triggers are mandatory. An untriggered review cycle makes these artefacts liabilities.

**Type 2 — Control mechanisms: slow build, stable plateau**

Value accumulates as the exception-and-deviation record grows. An organisation with three years of ACR records has a forensic trail. One with three months has a list. The plateau holds only while the exception process is enforced.

*Implication:* Value is cumulative. Abandoning the process destroys the accumulated record.

**Type 3 — Signal generators: spike, then decay without action**

Value is highest at delivery, when the signal is fresh. If no structural response follows, the artefact becomes evidence of an acknowledged problem that was not addressed — which is worse than no artefact at all.

*Implication:* A signal generator without an action owner has negative expected value after 12 months.

**Type 4 — Ground truth artefacts: accuracy-dependent bifurcation**

Two trajectories: maintained artefacts hold value indefinitely; unmaintained ones decay at the rate of organisational change. Integration Architecture and Infrastructure Architecture bifurcate here most severely.

*Implication:* Maintenance is not optional. It is the entire value proposition.

---

## Part 4: Industry Standards Evidence — What They Actually Measure

### What Standards Provide

Industry standards (Gartner ITScore, TOGAF maturity models, Forrester EA state reports) measure **practice maturity progression** and its aggregate outcomes. They do not measure individual artefact value trajectories.

**Gartner ITScore — Five EA Maturity Levels**

Nonexistent → Reactive → Functioning → Integrated → Ubiquitous

Measured across eight dimensions: stakeholder support, team resources, architecture development method, organisational integration, deliverables, EA governance, metrics, and stakeholder perceptions.

Empirical outcomes by progression:
- Advancing one maturity level: 15–20% improvement in project success rates
- Advancing one maturity level: 10–15% reduction in IT costs
- Mature EA practices: ~30% faster implementations
- Mature EA practices: ~25% lower total cost of ownership

These are practice-level outcomes. Artefact quality is a dimension of maturity — it is not measured independently.

**Gartner IT Project Success Data (2024)**

Only 48% of digital projects currently meet or exceed goals. Digital vanguard organisations — those with co-owned architectural governance — reach 71%. The separator is architectural discipline, which is artefact-dependent.

**EA Debt Research**

Architectural debt accumulates when artefacts are not maintained. Architectural drift accelerates at mid-delivery — fragmented ownership allows parallel decisions to diverge in ways that are rarely visible at the time (Yallo, 2026; RWTH Aachen / KTH, CEUR-WS 2020; SAC '26 proceedings).

Resolving architectural technical debt improves software quality short-term but can increase architectural complexity by centralising dependencies (FAN-IN increases 57.5% on average post-repayment).

### The Research Gap

> *"The different ways of evaluating architecture have mainly used a top-down approach deriving measures from theory rather than a bottom-up approach using empirical and practical studies. Research is especially lacking regarding empirical studies of how EA evaluation actually takes place."*
>
> — ResearchGate, EA ROI Framework Review (finding remains current)

Artefact-level longitudinal ROI studies do not exist in the published literature. Anyone citing specific ROI figures for an individual artefact type is citing an industry blog, not research.

---

## Part 5: MVP and MLP — The Empirical Evidence

### Why This Connects to EA

Both MVP and MLP are applied in enterprise transformation contexts — particularly in justifying phased delivery approaches, validating capability investment, and structuring governance checkpoints. The evidence base matters when either concept is used to justify architecture investment decisions.

### The Failure Context

**CB Insights, 2024 — 431 VC-backed companies analysed**

| Failure cause | % of failures | Classification |
|---|---|---|
| Capital depletion | 70% | Symptom, not root cause |
| Poor product-market fit | 43% | Root cause |
| Bad timing | 29% | Root cause |
| Wrong team | 23% | Root cause |
| Unsustainable unit economics | 19% | Root cause |

Capital depletion is where failure stories end. Poor product-market fit is where they begin. MVP exists to surface PMF failure before capital is committed.

A 2024–25 study of startups found 67% of failures happened because they built products nobody wanted — not because of bad code or technical problems (Softermii, 2024).

Product failure rates by sector: consumer packaged goods 70–85%, software and B2B products lower. PDMA research shows best-performing business units achieve 24% new product failure rates vs 46% for the rest — the separator is structured validation discipline.

### MVP — Evidence Assessment

**Strongest evidence: Management Science, 2022**

Koning, Hasan & Chatterji studied approximately 35,000 global high-technology startups over four years, exploiting the time-varying adoption of A/B testing technology.

> *"We find that, although relatively few firms adopt A/B testing, among those that do, performance improves by 30%–100% after a year of use."*
>
> — Management Science, Vol. 68, No. 9, September 2022

Mechanism: experimentation improves organisational learning, which helps startups develop more new products, identify and scale promising ideas, and fail faster when they receive negative signals.

**Practitioner-cited statistics**

- MVP-based projects: 60% lower failure rate vs traditional development (Full Scale / industry aggregation)
- Time-to-market: 35% faster with MVP approach (Gartner cited in SDH, 2024)
- User insights: 72% of startups using MVP gain better user insights (Gartner, 2024)
- Cost reduction: up to 60% vs full-build development

**Caveat:** The Management Science study measures experimentation culture broadly, not MVP methodology specifically. Practitioner statistics are industry aggregations, not controlled trials. MVP has stronger empirical backing than MLP, but the research still lags practice.

**Systematic mapping finding (arxiv, 2023)**

> *"Our analysis suggests that there are opportunities for solution proposals and evaluation studies to address literature gaps concerning technical feasibility assessment and effort estimation. Overall, more effort needs to be invested into empirically evaluating the existing MVP-related practices."*

### MLP — Evidence Assessment

**Origin:** Brian de Haaff, Aha! co-founder, coined the term in 2013. Expanded in *Lovability* (2017).

**Evidence base:** Practitioner case studies — Notion, Slack, Linear, Arc, Raycast. NPS logic and qualitative engagement metrics. No peer-reviewed comparative effectiveness trials.

**Claimed differentiators:**
- Targets retention and word-of-mouth from day one rather than functional validation first
- Primary metrics: NPS, 30-day engagement, activation rates, support burden per user
- Requires deeper problem understanding before build commences
- Higher initial investment; wrong assumptions are more expensive to correct

**The honest finding:** MLP has no peer-reviewed effectiveness evidence. The MLP claim — that emotional attachment from day one produces better retention outcomes than validated-functional-first — is theoretically coherent and practically compelling. It is empirically untested in any comparative study.

### The Correct Framing

| Dimension | MVP | MLP |
|---|---|---|
| Evidence base | Peer-reviewed (Management Science 2022), practitioner aggregation | Practitioner case studies only |
| Primary purpose | Market demand validation | Retention and emotional attachment |
| Primary metric | Learning velocity, PMF signal | NPS, 30-day engagement, activation |
| Risk profile | Lower initial investment, faster failure | Higher initial investment, assumption-sensitive |
| Best context | Unknown demand, high uncertainty | Known demand, competitive differentiation |
| Empirical status | Supported for experimentation discipline | No comparative effectiveness data |

Anyone citing MVP and MLP as equivalent evidence-backed approaches is overclaiming one of them.

---

## Consolidated Findings

### Finding 1 — Artefact type determines value trajectory

The four types — decision instrument, control mechanism, signal generator, ground truth — each follow a structurally different value curve. Treating all artefacts as equivalent documentation obligations produces the same artefact set with a fraction of the value.

### Finding 2 — Industry standards measure practice, not artefacts

Gartner ITScore, TOGAF maturity frameworks, and Forrester state reports provide practice-level evidence of EA effectiveness. They do not provide artefact-level value curves. Advancing one maturity level produces 15–20% project success improvement and 10–15% IT cost reduction — at the practice level. Attributing these figures to specific artefacts is not supported by the research.

### Finding 3 — Maintenance is not optional for ground truth artefacts

Integration Architecture, Infrastructure Architecture, and as-is process models bifurcate into two trajectories: maintained (sustained value) and unmaintained (accelerating decay). The unmaintained trajectory actively increases organisational risk. Accuracy of Infrastructure Architecture is a direct multiplier on MTTR.

### Finding 4 — Signal generators require action owners

A BCM heat map, VSM, or Organisation Map without a named action owner has negative expected value after 12 months. It becomes evidence of an acknowledged problem that was not addressed. This is structurally worse than no artefact.

### Finding 5 — MVP has empirical support; MLP does not

The Management Science 2022 study (35,000 startups, 4-year panel) provides the strongest evidence that iterative validation discipline improves performance 30–100%. MLP remains practitioner-constructed with compelling logic and no comparative effectiveness data. Both can be used — but they cannot be cited as equivalent in evidence terms.

### Finding 6 — The artefact-level research gap is significant

No longitudinal empirical study tracks the value trajectory of individual EA artefacts over time. The field measures inputs and proxies. Value-over-time curves must be derived from first principles, artefact type logic, and EA debt research. This is a legitimate research opportunity.

---

## Sources

| Source | Type | Finding |
|---|---|---|
| CB Insights (2024) | Industry research — 431 companies | 43% PMF failure; 70% capital depletion as symptom |
| Koning, Hasan & Chatterji — *Management Science* 68(9), 2022 | Peer-reviewed | 30–100% performance improvement with A/B testing; 35,000 startups |
| Stevenson et al. — *Journal of Management* 50(8), 2024 | Peer-reviewed | MVP theory-practice review; empirical evaluation underdeveloped |
| Systematic mapping study — arxiv 2305.08299 (2023) | Academic | More empirical evaluation needed for MVP practices |
| Gartner ITScore EA maturity model | Industry standard | Five levels; 15–20% project success / 10–15% IT cost per level |
| Gartner IT project success data (2024) | Industry research | 48% vs 71% project success — governance discipline is the separator |
| ASUG EA community analysis (2025) | Industry analysis | ~30% faster implementations; ~25% lower TCO with mature EA |
| RWTH Aachen / KTH — CEUR-WS Vol. 2628 (2020) | Academic | EA debt management framework; identification and valuation criteria |
| SAC '26 — ACM/SIGAPP proceedings | Peer-reviewed | LLM-based EA debt detection from unstructured documentation |
| Yallo (2026) | Practitioner analysis | Architectural debt expands faster than technical debt; mid-stage drift |
| ResearchGate EA ROI framework (2006, current) | Academic case study | Empirical studies of EA evaluation remain lacking |
| PDMA new product failure study | Industry research | Best units 24% failure rate vs 46% rest — validation discipline |
| Softermii (2024–25) | Practitioner analysis | 67% of failures built products nobody wanted |
| Nielsen / FMCG data | Industry research | 70–85% consumer product failure rate |
| NN/g (2026) | Practitioner | MVP as hypothesis test; high-performing teams pre-agree pivot criteria |
| Brian de Haaff — *Lovability* (2017) | Practitioner | MLP origin; practitioner construct, no peer-reviewed effectiveness data |

---

## Methodological Notes

This report synthesises practitioner analysis, industry research, and peer-reviewed academic sources. Where evidence quality varies, findings are explicitly graded. Peer-reviewed findings are distinguished from practitioner aggregations throughout.

Value-over-time curves in Part 3 are structurally derived from artefact type logic and EA debt research, not from a longitudinal empirical study of individual artefacts. That study does not exist. The curves represent the logical consequence of what each artefact type does, not measured trajectories.

Industry standard figures (maturity level progression outcomes) are Gartner/ASUG aggregations from client data. They are not independently peer-reviewed. They are the strongest practice-level evidence available.

---

*ZenCloud Global Consultants · Evidence-Based Research and Consulting*  
*For practitioner application, see the Velocity Architecture Framework™ (VAF) Series 5*
