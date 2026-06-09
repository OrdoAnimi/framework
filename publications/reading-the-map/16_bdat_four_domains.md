# Chapter 16: BDAT — The Four Domains

*Part 3 · The Core Concepts*

---

Every enterprise architecture, regardless of which framework produced it, describes the same four things.

What the business does. What data it uses. What applications it runs. What technology those applications run on. Business, Data, Application, Technology. **BDAT**.

This is not a TOGAF invention, though TOGAF uses it. It is not unique to any single framework. It is the underlying structure of the discipline — the four domains that every EA framework organises itself around, named differently in different places but recognisable everywhere. Zachman's grid implicitly contains all four. ArchiMate's three layers map to them. FEAF's reference models address them. They are the common architecture of enterprise architecture itself.

Understanding BDAT is the prerequisite for everything in Part 3. Every concept that follows — capability maps, value streams, application portfolios, data architecture, infrastructure patterns — lives in one of these four domains or describes the relationship between them. The four domains are the territory. Part 3 is the map of that territory.

---

## The Four Domains

**Business architecture** describes what the organisation does and why. Its primary artefacts are capability maps, value streams, organisation models, and motivation models. It answers the questions: what can we do, how does value flow through us, who is responsible for what, and what are we trying to achieve? Business architecture sits at the top of the stack because everything else exists to serve the business. If the business architecture is wrong — if the organisation does not understand its own capabilities and value flows — then the application and technology layers built to support it will be wrong too.

**Data architecture** describes what information the organisation uses, where it comes from, how it moves, and who is responsible for it. Its primary artefacts are data models, data flow diagrams, data governance frameworks, and master data definitions. Data architecture answers the questions: what data exists, where does it live, who owns it, and how does it get from where it is created to where it is needed? Data is the connective tissue of the organisation — it crosses every business boundary, feeds every application, and accumulates every operational decision.

**Application architecture** describes the software systems that the organisation uses to do its work. Its primary artefacts are application portfolios, integration maps, system context diagrams, and application capability mappings. Application architecture answers the questions: which systems do we run, what business capabilities do they support, how do they connect to each other, and where are the redundancies and the gaps? The application layer is where most IT programmes live — the place where business change meets technology delivery.

**Technology architecture** describes the infrastructure that the applications run on. Its primary artefacts are infrastructure topology diagrams, network architecture, hosting models, and platform specifications. Technology architecture answers the questions: where do our applications actually run, how is that infrastructure managed, what is the reliability and performance of the platform, and what are the risks in the infrastructure estate? Technology architecture is the foundation layer — the one that everything else ultimately rests on.

---

## Why the Order Matters

BDAT is almost always presented top-to-bottom: Business first, then Data, then Application, then Technology. That order is not arbitrary. It reflects a dependency chain — each layer exists to serve the layer above it.

Technology exists to run applications. Applications exist to process data. Data exists to support business operations. Business operations exist to deliver value to the people the organisation serves.

When you read that chain bottom-to-top, it tells you the direction of constraint. Technology choices constrain what applications can do. Application choices constrain how data can be managed. Data management choices constrain what business capabilities are possible. Every decision made in a lower layer shapes what is possible in the layers above it.

When you read the chain top-to-bottom, it tells you the direction of requirement. Business needs drive data requirements. Data requirements drive application choices. Application choices drive technology investment. Every legitimate technology investment should be traceable upward to a business need.

*At Meridian, the VMware crisis is a technology layer event. But its consequences travel up through all four domains. At the technology layer: infrastructure is unstable, at risk, and expensive. At the application layer: the applications running on VMware — including both EPR systems — are exposed to platform failure. At the data layer: patient records stored in those EPR systems are at risk of being inaccessible if the platform fails during a clinical event. At the business layer: the capability to deliver safe, informed patient care depends on clinicians accessing accurate records in the field. The VMware problem is not a technology problem. It is a business risk that happens to originate in the technology layer. BDAT makes that connection visible.*

---

## The Ripple Chain

The BDAT dependency chain is sometimes called the **ripple chain** — a change at any layer sends ripples upward and downward through the stack.

A change introduced at the technology layer — migrating from VMware to a cloud provider — ripples upward. Applications need to be validated for cloud hosting. Data residency requirements need to be checked. Business processes that depend on specific performance characteristics need to be assessed. The technology decision is not just a technology decision.

A change introduced at the business layer — deciding to consolidate from dual EPR to single EPR — ripples downward. The data layer needs to resolve how patient records from two different schemas are unified without clinical harm. The application layer needs to determine which system survives and what integrations are removed. The technology layer needs to assess what infrastructure is no longer needed. The business decision generates a cascade of technical consequences.

The ripple chain is why architecture matters. Without an explicit model of the four domains and their relationships, organisations make changes in one layer without understanding the consequences in the others. Every "unexpected" IT project cost overrun, every integration that breaks when a system is upgraded, every data quality problem that surfaces in a new reporting tool — most of these are ripple chain effects that were not mapped because nobody was maintaining a picture of how the four domains connect.

> *The ripple chain runs in both directions. Business decisions have technology consequences. Technology decisions have business consequences. Architecture is the discipline that makes those consequences visible before they are expensive.*

---

## BDAT in Practice

Most organisations do not apply all four domains with equal rigour. Understanding where the gaps typically are helps you read an organisation's architecture maturity quickly.

Business architecture is the most commonly underdeveloped domain. Many IT functions have detailed application and technology architecture but have never formally mapped their business capabilities or value streams. They can tell you every system in the estate. They cannot tell you which systems support which capabilities, or what would happen to those capabilities if a system failed.

Data architecture is the most commonly underestimated domain. Organisations that have invested heavily in applications frequently discover, too late, that their data is the real constraint. Systems cannot be consolidated because data models are incompatible. Reports cannot be produced because the data needed does not exist in a usable form. Migrations take twice as long as planned because nobody mapped the data flows before the project started.

Application architecture is where most IT investment is concentrated, and consequently where most architecture attention focuses. Application portfolios are the most commonly maintained architecture artefact in most organisations — though even they are frequently incomplete or out of date.

Technology architecture is the most crisis-driven domain. It receives intense attention when the infrastructure fails or faces a forced change — as Meridian's VMware crisis demonstrates — and relative neglect otherwise. Technology architecture decisions made under crisis conditions are rarely the best ones.

*Meridian's architecture maturity, assessed against BDAT, looks like this: technology architecture exists in the form of infrastructure diagrams maintained by the infrastructure team, though they are 18 months out of date. Application architecture exists partially — there is an application list but no integration map and no capability mapping. Data architecture does not formally exist — there are database administrators who know where the data lives, but no formal data architecture documentation. Business architecture does not exist at all. The new EA's first priority, before any framework or methodology question is answered, is to identify where in the BDAT stack the most critical gaps are and address them in order of business risk. She starts with business architecture — not because it is the most technically urgent, but because without it, every decision in the other three layers lacks its justification.*

---

## BDAT and the Frameworks

Every framework you have met in Part 2 addresses BDAT, either explicitly or implicitly.

TOGAF uses the term **Architecture Domains** and identifies Business, Data, Application, and Technology as the four. The ADM explicitly produces architecture definition documents for each domain in Phases B, C, and D. Phase B is business architecture. Phase C covers information systems — data and application. Phase D covers technology.

ArchiMate's three-layer model maps directly: the Business layer maps to B, the Application layer maps to A, and the Technology layer maps to T. Data sits across the Application and Technology layers in ArchiMate, surfacing as data objects at the application layer and artefacts at the technology layer.

BIZBOK operates in the business architecture domain. The capability maps and value streams from Chapter 11 are business architecture artefacts. They sit at the top of the BDAT stack and drive requirements into the layers below.

SABSA, the security architecture framework from Chapter 10, applies across all four domains. Security is not a layer — it is a dimension that cuts through every domain. SABSA makes this explicit through its own layered model, which mirrors the BDAT structure.

COBIT's governance objectives, from Chapter 15, apply to all four domains. The benefits delivery objective applies to business outcomes. The risk optimisation objective applies to data, application, and technology risks. The resource optimisation objective applies to technology investment. COBIT does not distinguish which domain a governance question belongs to — it governs the whole stack.

---

## Translator Panel

> **TOGAF says:** "The TOGAF framework is based on four architecture domains that together provide a comprehensive description of an enterprise: Business Architecture, Data Architecture, Application Architecture, and Technology Architecture."
>
> **What that means:** Enterprise architecture has four parts. The top part describes what the business does and why. The second part describes what data the business uses. The third part describes the software systems. The fourth part describes the infrastructure those systems run on. All four are necessary. None of them is the whole picture on its own.

> **Architects say:** "We need to understand the ripple chain before we approve this change."
>
> **What that means:** Before committing to a change, someone needs to trace what it does in each of the four domains — not just the domain where the change originates. A technology change has application, data, and business consequences. A business change has technology, application, and data consequences. The ripple chain is that set of consequences, mapped before they become problems.

---

## The Key Idea

BDAT — Business, Data, Application, Technology — is the four-domain structure that organises everything in enterprise architecture. The domains are ordered by dependency: each layer exists to serve the layer above it. Changes ripple in both directions through the stack. An organisation that understands all four domains and their relationships can make technology decisions with full awareness of their business consequences, and business decisions with full awareness of their technology implications. That is the discipline. Every concept in Part 3 lives inside this structure.

**Next:** Chapter 17 goes inside the business architecture domain — the top of the BDAT stack — and shows how the concepts from Part 2 become working tools: capability maps built, assessed, and connected to the decisions that matter.

---

## Further Reading

- **The Open Group — TOGAF Standard, 10th Edition, Part II: Architecture Development Method** (opengroup.org): Phases B, C, and D of the ADM address the Business, Information Systems, and Technology domains in sequence. Reading those three phase descriptions alongside this chapter shows exactly how BDAT becomes architecture work.
- **Gregor Hohpe — The Software Architect Elevator** (O'Reilly, 2020): Not a BDAT book by name, but the clearest account available of why the four-domain view matters in practice — how decisions in the technology basement affect the business penthouse and vice versa.
- **DAMA International — DAMA-DMBOK: Data Management Body of Knowledge** (Technics Publications): The authoritative reference for data architecture as a discipline. The data domain is the most commonly underdeveloped in the BDAT stack — DMBOK is the starting point for anyone who needs to go deeper.
- **Jeanne Ross, Peter Weill, and David Robertson — Enterprise Architecture as Strategy** (Harvard Business Review Press, 2006): The book that made the business case for the four-domain view in terms senior leadership could engage with. Older but still the most readable executive-level argument for why architecture across all four domains produces measurably better business outcomes.
