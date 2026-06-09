# The ADM — How to Use It

*Part 2 · The Frameworks Explained*

The ADM is not a checklist. It is a thinking structure.

That distinction matters more than almost anything else in this book. Every architect who has applied TOGAF badly has done so by treating the ADM as a procedure to follow. Every architect who has applied it well has done so by treating it as a way of organising their thinking about a complex problem. Same framework. Completely different results.

At Meridian the EA has a mandate: exit the VMware estate and move to cloud. Before she draws a single diagram she asks herself which ADM phases serve this specific problem. Phase A: establish what success means. Phases C and D: understand what exists. Phase E: identify the options. Phase F: sequence the migration. Phases G and H: keep the decisions honest as delivery teams execute. She does not run all nine phases. She runs the six that serve the problem. That is the ADM applied well.

## The nine phases at a glance

The ADM has nine phases plus a Requirements Management thread that runs continuously through all of them. Each phase answers one central question and produces one primary artefact.

## The minimum viable ADM

Not every problem requires all nine phases. Most architecture work uses a core of four phases with others added as the complexity demands.

Phase A is never optional. Every programme needs to know what success means before any other work begins. An architecture programme without a signed Architecture Vision is building on sand. Every subsequent decision lacks a test. Phase A takes as long as it takes to get clarity and commitment from the right person. Sometimes one conversation. Sometimes three months.

Phases C and D are the baseline. Before you can plan where you are going you need to know where you are. The application portfolio and technology inventory are the evidence base for every subsequent phase. Organisations that skip these produce migration plans for systems they do not fully understand. The surprises come out anyway — just later and at greater cost.

Phase E is the decision. The gap analysis and options paper are the architect’s primary output for decision-makers. Three paths with explicit tradeoffs. The CIO chooses. The architect makes the choice possible, not the choice itself.

Phase F is the sequence. Once the option is chosen, Phase F turns it into a programme. Which workloads move first. What depends on what. Where the quick wins are. The migration roadmap that delivery teams can actually execute.

How long does it take to get value from the ADM? Phase A alone, applied well, can change the direction of a programme in a single conversation. The full cycle in a large organisation takes months. You choose the scope based on the problem.

## Phase A in depth — Architecture Vision

Architecture Vision is the output of Phase A. It is the single document that governs every subsequent decision in the programme. It answers three questions: what are we trying to achieve, what principles will govern how we get there, and who has committed to the direction.

The Architecture Vision is not a strategy document. It is not a slide deck. It is one page. It is signed by a named executive. It exists before any design work begins. And it is the test every subsequent decision is measured against.

Meridian’s Architecture Vision reads: Enable safe, connected, person-centred care across 180 community and mental health sites by exiting the legacy VMware infrastructure, consolidating onto a unified clinical system, and building an ICS-aligned digital platform that meets all NHSE Frontline Digitisation obligations. Five architecture principles follow: cloud by default, single identity layer, no shadow platforms, FHIR-compliant integration, patient safety over delivery speed. One page. Signed by the CIO. Every subsequent decision tested against it.

## Phases C and D — the baseline you cannot skip

Phase C builds the application portfolio and data architecture baseline. Phase D builds the technology baseline — the infrastructure inventory, the network topology, the platform estate.

Together they answer the question: what actually exists? The answer is almost always different from what anyone believed before the exercise was done.

At Meridian the Phase C exercise discovers 47 applications in active use. The IT manager believed there were 30. Of the additional 17, three are running on systems with no support contract, two contain patient data with no documented data governance, and one has been maintained by a single contractor who left the organisation eight months ago. None of this was in anyone’s system records. The baseline exercise took four weeks. The cost of not doing it would have been migration surprises at programme execution. Surprises at that stage cost ten times more to resolve.

## Phase E — options not recommendations

Phase E produces options, not recommendations. This distinction is the most important one in the architect’s relationship with decision-makers.

An architect who presents a single recommendation is making the decision on behalf of the CIO. That is the wrong role. The architect's job is to make the decision possible by structuring the options clearly enough that the person with accountability can choose with confidence.

Good Phase E options have three properties. Each option is genuinely different — not three versions of the same approach with different labels. Each option has explicit costs, timelines, and risks rather than general descriptions. And each option has a clear statement of what it is best suited for — which context makes this option the right choice.

Meridian’s EA presents three options to the CIO. Option A: lift and shift VMware workloads to Azure IaaS. Fast VMware exit. Higher long-term cloud run cost. Lower programme risk. Option B: re-platform workloads to Azure PaaS. Slower VMware exit. Lower long-term cost. Higher programme complexity. Option C: retire low-value applications, replace strategic ones with SaaS, re-host only what cannot be replaced. Medium timeline. Predictable operating cost. Dependent on procurement. The EA explains the tradeoffs. The CIO decides. The recommendation was Option C with Option A for the first wave. The EA’s job was to make that decision possible, not to make it.

## Phase F — the sequence that makes delivery possible

Phase F turns the chosen option into a sequenced programme. The sequencing is not arbitrary. It is driven by dependencies. The question for each workload or capability is not ‘how complex is this?’ or ‘how valuable is this?’ It is ‘what must be true before this can be done?’

The answer to that question produces the wave structure. The dependencies create the sequence. The sequence creates the migration roadmap.

At Meridian the EA maps the dependencies before sequencing the waves. Identity — Entra ID — must come first because every subsequent wave depends on it for authentication. Without identity in place nothing else can move to cloud securely. M365 migration comes second because Exchange and SharePoint can move immediately once identity is established and the savings begin at once. VMware re-hosting comes third. EPR consolidation comes fourth because it is the most complex and depends on the cloud platform being stable. DC exit comes last because it cannot happen until everything that runs in the DC has moved. That sequence was not a preference. It was a dependency map.

## Phases G and H — governance that produces decisions

Phase G establishes governance. Phase H keeps the architecture current as the organisation changes. Together they answer the question that Phase F leaves open: how do we make sure delivery teams actually build what the architecture says they should?

Governance that produces documents but not decisions is Architecture Theatre. The test for whether Phase G governance is working is simple: did this governance process result in at least one decision being made that would not have been made without it? If the answer is consistently no, the governance is not working.

Phase H is often ignored entirely. Architecture programmes that stop at the end of Phase F treat the roadmap as permanent. But organisations change. Business priorities shift. New technology appears. Regulations arrive. An architecture that cannot evolve in response to these changes becomes irrelevant. Phase H is the mechanism that keeps it relevant.

Meridian’s Architecture Board meets fortnightly. Before each session the EA distributes a one-page briefing: decisions pending, decisions made since last session, deviations from the architecture principles, and one item for the board to resolve. The board resolves the item. The EA updates the decision log. That is Phases G and H working. Not a governance process performing itself. A governance process producing decisions.

---

## Translator Panel

> **TOGAF says:** "Move through the ADM phases, A to H."
>
> **What that means:** A sound sequence of questions, not a mandatory waterfall. Run the phases that improve the decision in front of you; lighten or skip the rest. The "minimum viable ADM" is usually the right starting point.

> **Delivery teams say:** "The ADM will slow us down."
>
> **What that means:** It will if it is performed as ceremony. Used selectively — a one-page vision, the baseline you genuinely cannot skip, a real roadmap — it speeds delivery by preventing the rework that comes from skipping the thinking.

---

## The Key Idea

The ADM is the engine of TOGAF: a cycle of phases that moves an organisation from vision through baseline and target, gap analysis, roadmap, and governance. Read as a checklist to be completed in full, it produces shelfware; read as a sequence of questions to be answered to the depth each decision requires, it is one of the most useful thinking structures in the field. The discipline is selective application — run Phase A almost always, scope the domain phases to the decision, and stop when the question is answered — keeping the method an instrument rather than a ritual.

**Next:** Chapter 8 turns from method to notation — ArchiMate, the visual language for drawing what the ADM produces.

---

## Further Reading

- **The Open Group — TOGAF Standard: the ADM** (opengroup.org): The canonical phase-by-phase description. Read for the questions each phase answers, not the artefact lists.
- **Appendix C — ADM Phase Reference** (this book): A one-page version of every phase with when to apply it and when to skip it.
- **Michael Watkins — The First 90 Days** (Harvard Business Review Press, 2013): The listen-before-acting discipline that makes the early ADM phases work in a real organisation.
