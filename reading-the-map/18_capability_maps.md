# Chapter 18: Capability Maps in Practice

*Part 3 · The Core Concepts*

---

Chapter 11 introduced the capability map as a concept — what it is, why it exists, how it differs from an org chart or a process model. This chapter shows what one actually looks like when it is being used: built in workshops, assessed against the current IT estate, heat-mapped to show where the pain is, and connected to the application portfolio decisions that follow.

The capability map is the most practically useful artefact in the business architecture domain. It is also the artefact most commonly produced once, filed, and never looked at again. The difference between a capability map that drives decisions and one that decorates a strategy document is not in the map itself — it is in how the map is maintained and what questions it is used to answer.

This chapter stays on the literacy side of that line. You are not learning to run a capability mapping workshop. You are learning to read the outputs, understand the assessment methods, and follow the conversations that capability maps generate — so that when you are in a room where one appears, you know what you are looking at and what it means for the decisions on the table.

---

## What a Capability Map Looks Like

A capability map is a hierarchical grid. Level 1 contains the broadest capability categories — typically eight to fifteen boxes that name the highest-level things the organisation can do. Level 2 breaks each of those into recognisable sub-capabilities. Level 3, where it exists, gets specific enough to be useful for application mapping and investment decisions.

For Meridian, Level 1 might look like this:

| Clinical Care | Patient Administration | Workforce Management |
|---|---|---|
| **Community Services** | **Referral Management** | **Finance and Procurement** |
| **Clinical Governance** | **Communications** | **Facilities and Estates** |
| **Research and Education** | **Information and Analytics** | **Technology Services** |

Each box is a capability — a stable label for something Meridian can do, independent of which team does it or which system supports it. Level 2 breaks Clinical Care into Patient Assessment, Treatment Planning, Medication Management, Clinical Documentation, and so on. Level 3 breaks Clinical Documentation into Record Creation, Record Amendment, Record Access, and Discharge Summary.

The map is not an org chart. Finance and Procurement appears once, even though the finance function, the procurement team, and the shared services partner all contribute to it. Clinical Documentation appears once, even though it is performed across 180 sites using two different EPR systems. The capability is the stable thing. The organisation and the technology are the variable things that sit underneath it.

---

## Building the Map

A first-pass capability map does not require months of research. It requires two or three workshops with people who actually run operations, a facilitator who can keep the conversation at the right level of abstraction, and enough intellectual honesty to name capabilities as they are rather than as the organisation wishes they were.

The most common failure mode in capability mapping workshops is slipping from capabilities to processes. A process is a sequence of steps. A capability is an ability. "Process a referral" is a process. "Referral Management" is a capability. The distinction matters because capabilities are stable across process changes — Meridian will always need Referral Management capability, even if the process by which referrals are managed changes completely when the new EPR goes live.

The second failure mode is mapping the org chart rather than the capabilities. If every Level 1 box corresponds exactly to a department, the map is reflecting organisational structure rather than business capability. Capabilities cut across departmental lines. A map that does not do that has not been pushed far enough.

*At Meridian, the first workshop produces a Level 1 map with eleven boxes. The clinical team immediately wants to split Clinical Care into Inpatient Care, Outpatient Care, and Community Care — arguing that they are fundamentally different capabilities. The EA holds them at Level 1 for now and notes the split as a Level 2 detail. The finance team is surprised to see Finance and Procurement as a single box — they consider finance and procurement to be completely separate functions. The EA explains the difference between a functional structure and a capability structure. The procurement manager, who has been trying to get a seat at the IT governance table for two years, immediately grasps that capability mapping gives her a language for that conversation. By the end of the workshop, the map has eleven Level 1 boxes, each with two to five Level 2 sub-capabilities sketched in. Nobody agrees on everything. That is expected. The map is a first draft.*

---

## Assessing Capability Health

Once the map exists, the first thing you do with it is an assessment. For each capability, you ask: how well can we currently do this?

The standard assessment uses a four-point scale:

**Inadequate** — the capability exists in name but cannot reliably deliver the outcome it is supposed to. There are significant gaps in people, process, or technology. This capability is a material risk to the organisation.

**Developing** — the capability works some of the time, for some use cases, with significant manual intervention or workarounds. It is functional but fragile. Improvement is needed but the situation is not critical.

**Adequate** — the capability delivers its intended outcome reliably under normal conditions. It is not excellent but it is sufficient. No immediate investment required.

**Strong** — the capability is a genuine organisational strength. It delivers consistently, efficiently, and to a standard that the organisation is confident in.

The assessment is conducted through structured conversations with the people who run each capability — not through IT surveys or system audits. The question is not "does the system work?" It is "can the organisation do this reliably?" Those are different questions with frequently different answers.

---

## The Heat Map

Once capability assessments are complete, the map is colour-coded — and becomes a **capability heat map**.

Inadequate capabilities are red. Developing capabilities are amber. Adequate capabilities are green. Strong capabilities are dark green or blue.

The heat map is the artefact that makes capability assessment communicable to people who will not read a fifty-page analysis. A board member who would not engage with a detailed systems review will look at a heat map and immediately ask why Clinical Documentation and Patient Scheduling are both red. That question is the beginning of an architectural conversation that could not have started from a project proposal or a budget request.

*Meridian's first heat map produces an uncomfortable picture. Seven of the eleven Level 1 capabilities are red or amber. Clinical Documentation is red — partly because of the dual-EPR problem, partly because document scanning and management are handled by a system that has not been updated in six years. Patient Scheduling is amber — it works but differently across the 180 sites, with no consistent process and no single view of capacity. Referral Management is red — the paper referral process for community services has never been digitised. Information and Analytics is red — Meridian cannot produce a reliable report of its own activity without a week of manual data extraction and reconciliation. Technology Services is amber — the VMware crisis has been known for eighteen months and the response has been reactive rather than planned. The heat map does not contain a single piece of information that individual teams did not already know. What it does is make all of that information visible in one place, at one moment, to the same audience. That is its value.*

---

## Connecting the Map to the Application Portfolio

A capability map without an application portfolio mapping is incomplete. The map tells you what the organisation can do and how well. The application mapping tells you what technology is supporting each capability — and therefore explains why the capability assessment looks the way it does.

The cross-mapping is produced by asking, for each capability: which applications currently support this capability? The answers reveal three things.

**Over-supported capabilities** — capabilities served by multiple competing applications. Meridian's Clinical Documentation capability is served by two EPR systems, a legacy clinical portal, a document management platform, and four departmental databases. The capability fragmentation is explained by the application fragmentation. Consolidating the capability requires consolidating the applications — and that requires understanding which application is doing what, for whom, and whether any of it can be safely removed.

**Under-supported capabilities** — capabilities with no application support, or with application support so inadequate that the capability is effectively running on manual effort. Meridian's Referral Management capability is in this position for community services. There is no system. There is a spreadsheet, a shared inbox, and a lot of phone calls.

**Correctly supported capabilities** — capabilities served by a single well-functioning application whose cost and performance are proportionate to the importance of the capability. These are the green cells in the heat map with a clean application mapping. They are also the capabilities that should be left alone while the red and amber capabilities receive investment.

> *A capability map without an application mapping tells you what hurts. A capability map with an application mapping tells you why — and what it would take to fix it.*

---

## Capability Investment Prioritisation

The heat map, combined with the application portfolio mapping, produces the input to the investment prioritisation conversation.

Not all red capabilities are equal. The prioritisation question is not simply "which capabilities are weakest?" It is "which weak capabilities carry the most business risk if they are not improved?" A weak capability in a non-differentiating area — Facilities Management, say — carries different risk than a weak capability at the heart of clinical service delivery.

The framework for prioritisation has three dimensions.

**Strategic importance** — how central is this capability to the organisation's mission? For Meridian, Clinical Documentation and Patient Scheduling are core. Facilities Management is important but not differentiating.

**Current performance** — how inadequate is the capability today? Red capabilities need investment more urgently than amber.

**Risk trajectory** — is the gap getting wider? A capability that is developing slowly under current investment is different from one that is actively deteriorating because the platform supporting it is failing.

*Meridian's prioritisation exercise produces a top-three list: Clinical Documentation (red, core, platform failing), Referral Management for community services (red, strategic gap, no digital capability at all), and Information and Analytics (red, blocking every governance and planning conversation the trust needs to have). The VMware exit programme addresses the platform risk underneath Clinical Documentation. The EA recommends that the community services referral system is the next capital investment case. Information and Analytics requires a data architecture decision before a technology decision — which data is authoritative, where it lives, and who is responsible for it. That decision leads directly to the next chapter.*

---

## Translator Panel

> **BIZBOK says:** "A capability assessment evaluates the current state of each business capability against the target state required to deliver the organisation's strategic objectives, typically using a maturity or performance scale."
>
> **What that means:** Once you have named your capabilities, you assess how well you can actually do each one today. The assessment is not about whether a system exists — it is about whether the capability reliably delivers the outcome it is supposed to. The gap between current and required performance is what drives investment decisions.

> **Architects say:** "We need to heat-map this against the application portfolio before we take it to the investment board."
>
> **What that means:** The capability assessment tells you which capabilities are underperforming. The application mapping tells you which systems are responsible for that underperformance. Before proposing investment, you need to show the connection — this capability is red because this application is inadequate, and fixing the application is what will move the capability from red to green. Without that connection, the investment case is speculative.

---

## The Key Idea

A capability map is not a picture of the organisation. It is a decision-making instrument. Built honestly, assessed rigorously, and connected to the application portfolio, it produces the clearest available answer to the question that every IT investment decision is trying to answer: where does the organisation most need to improve its ability to do the things that matter, and what technology change would most improve that ability? The heat map makes that answer visible to anyone in the room — not just the architects.

**Next:** Chapter 19 moves to data architecture — the second domain in the BDAT stack, and the one most commonly underdeveloped. What data architecture is, why it is harder than it looks, and what Meridian's data situation actually reveals about the limits of application-level thinking.

---

## Further Reading

- **Business Architecture Guild — BIZBOK Guide** (bizbok.org): The capability assessment methodology is covered in the BIZBOK guide in significantly more detail than this chapter provides. For practitioners who need to run assessments rather than read them, the BIZBOK guidance on capability heat mapping and investment prioritisation is the primary reference.
- **Scott Bernard — An Introduction to Enterprise Architecture** (AuthorHouse, 3rd edition): Chapter 7 covers capability-based planning in a way that is accessible to non-specialists and connects the capability map to investment decision-making clearly.
- **NHS England — Capability Framework for Digital, Data and Technology** (england.nhs.uk): For anyone working in NHS organisations, the national capability framework provides the reference capability model that local organisations like Meridian are expected to align with. Understanding it is the starting point for any NHS capability mapping exercise.
- **Jeanne Ross, Cynthia Beath, and Martin Mocker — Designed for Digital** (MIT Press, 2019): The clearest account of how capability thinking connects to digital transformation investment. Not a BIZBOK book — but the most readable executive-level argument for why capability maps drive better technology investment decisions than project-by-project business cases.
