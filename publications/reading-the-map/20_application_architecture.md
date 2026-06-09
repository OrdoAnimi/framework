# Chapter 20: Application Architecture — The Portfolio and What It Reveals

*Part 3 · The Core Concepts*

---

The application layer is where most IT investment lives and where most architectural debt accumulates.

Every application in your estate was a good decision at the moment it was made. The payroll system was the right choice in 2008. The clinical portal solved a real problem in 2011. The document management platform was procured to address a genuine gap in 2014. Each decision was locally rational. Collectively, over fifteen years, they produced an estate that nobody designed — a landscape of overlapping capabilities, undocumented integrations, and dependencies that nobody fully understands.

**Application architecture** is the discipline that makes that accumulated landscape visible, assessable, and governable. Its primary tool is the **application portfolio** — a structured catalogue of the applications in the estate, assessed against a consistent set of criteria, mapped to the business capabilities they support, and used to drive investment and rationalisation decisions.

This chapter explains what an application portfolio is, how it is built and used, and what Meridian's portfolio reveals about fifteen years of decisions made without shared architectural direction.

---

## What an Application Portfolio Is

An application portfolio is not a list of software licences. It is not a helpdesk asset register. It is a structured view of the applications the organisation depends on to operate, assessed against criteria that allow comparison and prioritisation.

A mature application portfolio contains, for each application:

**Identity** — name, version, vendor, and the internal owner accountable for the application's fitness for purpose. Not the technical contact. The business owner — the person who would notice if the application stopped delivering value.

**Capability mapping** — which business capabilities does this application support? This is the connection back to the capability map from Chapter 18. An application that cannot be mapped to at least one business capability has no justified place in the estate.

**Technical assessment** — how fit is the application technically? Is it current, supported, and performant? Is it approaching end of life? Is it running on infrastructure that is at risk? The technical assessment is factual, not evaluative.

**Business value assessment** — how well does the application currently support the capabilities it is supposed to deliver? This is the user perspective — whether the application actually does what it is supposed to do for the people who use it. A technically current application that users have worked around because it does not meet their needs is a business value failure.

**Cost** — total cost of ownership, including licences, hosting, support, and the internal effort required to maintain and operate it.

**Strategic fit** — does the application align with the organisation's current strategic direction and architecture principles? A perfectly functional application that violates the cloud-first principle has a strategic fit problem. An application that duplicates a capability being delivered by another application in the estate has a rationalisation problem.

---

## Building the Portfolio

Building an application portfolio for the first time surfaces things that nobody knew — or knew but had never seen assembled in one place.

The inventory exercise alone is revealing. Most organisations discover they have more applications than anyone thought. Some are shadow IT — applications procured by business teams without IT involvement that have become operationally critical. Some are zombie applications — systems still running, still being paid for, still being backed up, with no active users and no clear owner. Some are duplicates — two applications delivering the same capability, maintained in parallel because a consolidation programme was started and never finished.

*At Meridian, the inventory exercise that precedes the portfolio build produces 94 applications. The infrastructure team's asset register contained 71. The additional 23 were found through a combination of business interviews, network traffic analysis, and a trawl of purchase orders going back five years. Of the 94: eleven have no identified business owner. Seven are running on hardware that has already reached manufacturer end of life. Four are running versions of software for which vendor support expired more than two years ago. Two are identical applications procured by different clinical teams for the same purpose, maintained independently at a combined annual cost of £180,000. One application, used daily by the community nursing team to manage their caseload, is a spreadsheet stored on a shared drive. The person who built it left Meridian in 2019.*

---

## The Portfolio Assessment Matrix

Once the inventory is complete, each application is assessed and the results are plotted on a portfolio assessment matrix. The most commonly used version plots **business value** on one axis against **technical quality** on the other.

This produces four quadrants.

**High business value, high technical quality — Invest.** These applications are doing their job well and are technically sound. They warrant continued investment and may be candidates for enhancement.

**High business value, low technical quality — Migrate or Remediate.** These applications are critical to operations but are technically at risk — aging infrastructure, unsupported versions, architectural debt. They cannot be ignored. The decision is whether to remediate the technical issues in place or migrate the capability to a new platform.

**Low business value, high technical quality — Rationalise.** These applications are technically fine but not delivering proportionate value. They may be redundant, underused, or superseded by a better option in the estate. Candidates for decommissioning.

**Low business value, low technical quality — Eliminate.** These applications are not delivering value and are technically poor. They should be removed from the estate. Doing so reduces cost, reduces risk, and reduces the surface area that the architecture and operations teams have to maintain.

*Meridian's portfolio matrix is uncomfortable. Of the 94 applications: 18 fall in the Invest quadrant — largely the core clinical systems, though even here the dual-EPR situation means two systems that should probably be one. 31 fall in Migrate or Remediate — including the legacy clinical portal (high daily usage, end-of-life platform) and the document management system (operationally critical, unsupported version). 22 fall in Rationalise — many of these are departmental tools that were procured to fill gaps that have since been addressed by other systems. 23 fall in Eliminate — including the zombie applications, the end-of-life hardware systems, and one application whose business owner, when contacted, confirmed that the team had stopped using it eighteen months ago and assumed IT had already switched it off. Nobody had.*

---

## Application Rationalisation

The portfolio matrix is not an answer. It is a structured question: given where our applications sit, what should we do differently? **Application rationalisation** is the programme of work that acts on that question — decommissioning, consolidating, migrating, and remediating the estate based on the portfolio assessment.

Rationalisation is always harder than the portfolio analysis suggests it should be. Every application in the Eliminate quadrant has a constituency — people who procured it, people who use it occasionally, people who believe it might be useful one day. Decommissioning requires not just a technical decision but a governance decision: a body with the authority to say that this application will be removed, that its data will be migrated or archived, and that the people who depended on it will move to an alternative.

The most common failure in rationalisation programmes is identifying the right answer and then failing to execute it. The portfolio says eliminate. The business owner says they are not ready. The project gets deferred. The application stays on the estate, consuming cost and maintenance effort, until the next portfolio review arrives and the same conversation happens again.

Architecture governance — the Architecture Review Board — is the mechanism that prevents this cycle. The ARB provides the authority to enforce portfolio decisions that individual teams would prefer to ignore.

---

## Integration Architecture

An application portfolio without an integration map is incomplete. Applications do not exist in isolation. They are connected — to each other, to external systems, to data sources and reporting platforms — and those connections are where the most fragile parts of the estate typically live.

**Integration architecture** describes the connections between applications: what data flows between them, via what mechanism, at what frequency, and with what error handling.

The integration map reveals the **integration complexity** of the estate — how many connections exist, how many are point-to-point versus going through a shared integration platform, and how the complexity would change if a specific application were removed or replaced.

Point-to-point integration is the integration equivalent of technical debt. Each connection is individually rational — it was the quickest way to get data from System A to System B at the time. Collectively, they produce a web of dependencies that makes any change to any application a high-risk event, because the full set of connections is rarely documented and the consequences of breaking one are unpredictable.

*At Meridian, the integration map that the EA produces during the portfolio exercise reveals 34 point-to-point integrations. Eleven are undocumented — they were discovered through network traffic analysis, not through any documentation. Of the 34: nine connect to the legacy clinical portal that is a Migrate priority in the portfolio matrix. Decommissioning the portal does not just require migrating its functionality. It requires remediating nine integrations that currently depend on it — some of which connect to systems that are themselves in the Eliminate quadrant. The integration map turns what looked like a straightforward portal decommission into a sequenced programme of six interdependent workstreams. That is not a problem the portfolio matrix created. It is a problem the portfolio matrix revealed.*

---

## Application Architecture and the Other Domains

Application architecture sits in the middle of the BDAT stack — below business architecture and above technology architecture — and it mediates the relationship between the two.

**From business architecture:** The capability map drives the application portfolio. Every application should be traceable to a business capability. Capabilities assessed as red or amber on the heat map point to applications in the Migrate, Rationalise, or Eliminate quadrants. Investment in the portfolio should be proportionate to the strategic importance of the capabilities it serves.

**To data architecture:** Applications are the primary systems of record for the data assets identified in the data architecture. The master data question — which system holds the authoritative version of patient identity — is an application architecture decision. The data flow map — how data moves between systems — is an integration architecture view.

**To technology architecture:** Applications run on infrastructure. The technology architecture provides the platform that the application portfolio depends on. Meridian's VMware crisis is a technology architecture event with application architecture consequences: which applications are at risk, which can be migrated to cloud infrastructure, and which have technical dependencies that prevent migration. The technology architecture question cannot be answered without knowing what the application portfolio requires.

---

## Translator Panel

> **The Open Group says:** "Application architecture describes the individual applications deployed to support the business, their interactions and their relationships to core business processes."
>
> **What that means:** Application architecture is the view of the software estate — what systems exist, what they do, how they connect to each other, and how they connect to the business. The application portfolio is the tool that makes that view visible and assessable. Without it, the estate is managed reactively — one system at a time, one incident at a time, with no shared picture of where the whole is going.

> **Architects say:** "Before we approve this procurement we need to check it against the portfolio — we may already have something that does this."
>
> **What that means:** Every application procurement that happens without a portfolio review risks adding a duplicate to the estate. The portfolio review is not bureaucracy — it is the check that prevents the organisation from paying twice for the same capability, creating the integration complexity of two systems where one would do, and making the rationalisation problem harder than it already is.

---

## The Key Idea

The application portfolio is the most practical architecture artefact in most organisations — the one that directly drives investment decisions, rationalisation programmes, and procurement governance. Built honestly, it reveals an estate that accumulated over years of locally rational decisions that nobody coordinated. Used actively, it provides the evidence base for every significant IT investment decision: not "do we need this system?" but "given everything else in the estate, is this the right way to meet this capability need?" That is a better question, and it produces better answers.

**Next:** Chapter 21 moves to technology architecture — the foundation layer of the BDAT stack. Infrastructure patterns, cloud models, and what the VMware crisis looks like when you are standing in the technology domain trying to understand all of its implications.

---

## Further Reading

- **The Open Group — TOGAF Standard: Phase C, Application Architecture** (opengroup.org): The TOGAF guidance on application architecture defines the artefacts, the assessment approach, and the governance process. The application portfolio guidance is the most immediately practical section.
- **Gartner — Application Rationalization Methodology**: Gartner's application rationalisation framework is widely used and freely available through most enterprise subscriptions. The TIME model (Tolerate, Invest, Migrate, Eliminate) is the most commonly referenced portfolio categorisation approach — a variant of the matrix described in this chapter.
- **Simon Wardley — Wardley Maps** (medium.com/@swardley): The evolution axis from Chapter 13 is directly applicable to application portfolio assessment. Applications in the commodity stage should be bought or replaced with commodity services. Applications in the genesis stage warrant investment. The Wardley and portfolio views are complementary and powerful in combination.
- **Ian Gorton — Foundations of Software Architecture** (O'Reilly, 2022): The most accessible current introduction to application architecture as a technical discipline — the complement to this chapter's portfolio and governance perspective.
