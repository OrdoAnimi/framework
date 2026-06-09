# Chapter 12: SAP EA — Architecture Inside the Machine

## Opening

If your organisation runs SAP, architecture is not optional. It is built into the product. Every configuration decision, every integration, every customisation is an architectural choice — whether anyone calls it that or not.

SAP is the world's most widely deployed enterprise software platform. Globally, it runs the back office of most large organisations: finance, procurement, supply chain, HR, manufacturing. In the public sector and healthcare, it frequently runs payroll, finance, and logistics. If Meridian were a local government body rather than an NHS trust, there is a good chance SAP would be at the centre of its technology estate.

Understanding what **SAP Enterprise Architecture** is — and what the **SAP EA Framework** provides — matters for two reasons. First, because SAP environments are architecturally complex in ways that general frameworks do not fully address. Second, because SAP has its own vocabulary, its own patterns, and its own governance expectations, and if you walk into a room where SAP is live you need to be able to follow the conversation.

This chapter gives you that foundation. Not how to configure SAP. Not how to become an SAP architect. Just what SAP EA is, what it covers, and how it connects to the broader frameworks you have already met.

---

## What SAP EA Actually Is

**SAP EA** refers to the architectural discipline of designing, governing, and evolving an organisation's SAP landscape. It is not a single product — it is a practice, supported by SAP's own reference materials, tools, and certification pathway.

At its core, SAP EA addresses a specific challenge: SAP systems are not islands. A typical SAP implementation connects finance to procurement to HR to logistics, and increasingly to cloud services, third-party applications, and real-time data feeds. The decisions made in one part of the landscape affect every other part. SAP EA is the discipline that makes those connections visible and governable.

*Meridian's finance and procurement function is run by a neighbouring NHS trust under a shared services agreement. That trust runs SAP S/4HANA. When Meridian needs to submit a capital expenditure request, it crosses into SAP territory — a system it does not own, governed by an architecture team it has no direct relationship with. An architect working at Meridian does not need to know SAP deeply, but they do need to understand what they are looking at when the integration diagram goes up on screen.*

The **SAP Reference Architecture** is SAP's own library of recommended designs — how to configure modules, how to integrate systems, which patterns to use for which business scenarios. Think of it as SAP's version of a pattern library: documented, tested approaches that avoid the most common mistakes. Experienced SAP architects use these references to avoid reinventing solutions that SAP has already worked out.

---

## The SAP Landscape

SAP environments are described in terms of their **landscape** — the arrangement of systems, instances, and integrations that make up the full SAP estate. Understanding landscape is the first thing you need to be able to do to follow an SAP architecture conversation.

A typical SAP landscape has three tiers:

**Development** is where changes are built and initially tested. Configuration changes, custom code, new integrations — all of this starts in the development system.

**Quality Assurance** (QA or test) is where changes are tested against realistic data before going live. This is where integration testing happens — checking that a change in the finance module does not break something in procurement.

**Production** is the live system. Changes only move to production after they have passed through development and QA. The movement of changes between these tiers is called the **transport system**, and managing transports is one of the fundamental governance activities in any SAP environment.

*At Meridian's shared services partner, a change to the procurement approval workflow has to travel through all three landscape tiers before it affects the live system. If the change is tested inadequately in QA, it goes live with defects. If it goes live with defects in procurement approval, invoices do not get paid on time. This is not an IT problem — it is a finance and supplier relationship problem. The landscape makes those connections visible.*

The distinction between landscape tiers seems straightforward but has real consequences. Many incidents in SAP environments happen because a change was tested in isolation in QA but broke something in production that depended on a configuration that was only present in the live system. SAP EA includes the discipline of managing this risk.

---

## S/4HANA and the Move to the Cloud

The most significant shift in SAP architecture over the last decade is the move to **SAP S/4HANA** — the current generation of SAP's core ERP platform. If you encounter SAP in a new organisation today, you are likely to encounter either S/4HANA already running, or a programme underway to migrate to it.

S/4HANA differs from its predecessor (SAP ECC) in three important ways for architecture purposes.

First, it runs on SAP's own in-memory database (**SAP HANA**), which changes the performance characteristics of the system significantly. Processes that took hours in batch mode can run in near real-time. This opens up new design possibilities but also requires architectural decisions about what to process in real-time and what to batch.

Second, S/4HANA has a simplified data model. The predecessor system had accumulated decades of complexity — redundant tables, legacy structures, overlapping data objects. S/4HANA rationalises this, which is architecturally cleaner but means organisations migrating from ECC have to resolve how their existing data maps to the new structure.

Third, S/4HANA is available as a **cloud deployment** — either as a public cloud (SAP's infrastructure, SAP's update cycle) or private cloud (dedicated infrastructure, more control). This is where SAP EA intersects with the broader cloud architecture questions most organisations are navigating.

*Meridian's situation is a useful contrast. Meridian has no cloud. Its technology strategy has not yet addressed cloud adoption in any substantive way, partly because the VMware crisis has absorbed leadership attention, and partly because the dual-EPR situation makes cloud migration feel like a second-order problem. If Meridian were to inherit an SAP estate through a shared services arrangement, it would suddenly have a cloud-hosted system in its landscape — whether it was ready for that or not.*

---

## How SAP EA Connects to Other Frameworks

SAP has its own architecture methodology, but it does not exist in isolation. If you are working in an organisation that uses TOGAF as its EA framework and also runs SAP, you need to understand how they relate.

The honest answer is that they address different levels of the same problem. TOGAF provides the overarching methodology — the ADM phases, the architecture domains, the governance approach. SAP EA provides the deep domain knowledge for the SAP-specific parts of the landscape. An architect working in an SAP environment typically uses both: TOGAF to structure the architecture process and SAP's reference materials to make the right decisions within that process.

**ArchiMate**, the modelling language you met in Chapter 8, has specific conventions for representing SAP landscapes. SAP systems appear in the technology and application layers. Integrations between SAP and other systems are represented as application interfaces. The three-tier landscape maps naturally onto ArchiMate's layering. If you can read an ArchiMate diagram, you can read an SAP landscape diagram — the vocabulary is the same even if the specific elements are different.

**BIZBOK** and business architecture connect to SAP EA through capability mapping. The business capabilities that SAP supports — procurement, finance, supply chain — can be mapped to the specific SAP modules that deliver them. This is exactly the kind of cross-mapping that Chapter 11 described: which capabilities are served by which systems, and what happens when those systems are under strain.

---

## The SAP EA Certification

SAP offers its own EA certification — the **SAP Certified Associate: SAP Enterprise Architect** (and more advanced levels). This is separate from TOGAF and from the general EA certifications you may encounter. It is specifically for architects who work in SAP environments and need to demonstrate competence in SAP's architectural approach, tools, and reference materials.

For most people reading this book, the SAP EA certification is not an immediate goal. But knowing it exists tells you something useful: SAP environments are architecturally complex enough to warrant their own certification pathway. When you encounter SAP in a new role, that complexity is real. The organisation almost certainly has people whose job is specifically to govern the SAP landscape. Understanding their role and their vocabulary helps you work alongside them effectively.

---

## What You Will Hear in the Room

If you are in a meeting where SAP is being discussed, you are likely to hear some combination of the following:

**Landscape** — the arrangement of SAP systems and their tiers. "What does the landscape look like?" means: how many systems, how are they connected, and what tier are we talking about?

**Transport** — the mechanism for moving changes between tiers. "The transport failed in QA" means a change did not successfully move from development to test. This is usually a technical problem but can have business consequences.

**Module** — the functional areas within SAP. Finance (FI), Controlling (CO), Materials Management (MM), Sales and Distribution (SD), Human Resources (HR) — each is a module. "Which modules are in scope?" means which functional areas are affected by the change or programme being discussed.

**RISE with SAP** — SAP's commercial offering for cloud migration. If someone mentions RISE, the organisation is in conversation with SAP about moving their landscape to the cloud. This is a significant architectural and commercial decision.

**Fit-to-standard** — the principle that an organisation should adapt its processes to fit SAP's standard configuration, rather than customising SAP to fit existing processes. This sounds simple but is culturally and politically difficult in most organisations. It is one of the central tensions in any SAP implementation.

*At Meridian's shared services partner, fit-to-standard was the stated principle for the S/4HANA implementation. In practice, the finance team had seventeen years of custom reports built on the old system and was unwilling to lose them. The tension between the architectural principle and the operational reality consumed six months of governance conversations. This is not unusual. It is the normal condition of large SAP programmes.*

---

## Translator Panel

> **SAP says:** "The SAP Reference Architecture provides a structured collection of best practices, reference solutions, and architectural patterns to support the design of SAP landscapes."
>
> **What that means:** SAP has documented the most common ways to configure and connect its systems, based on what has worked across thousands of implementations. These are the recommended starting points — not rules, but tested patterns that save experienced architects from reinventing solutions that already exist.

> **SAP says:** "Fit-to-standard means adopting SAP's standard business processes rather than customising the software to match existing ways of working."
>
> **What that means:** Instead of bending SAP to fit how you currently do things, you adopt how SAP thinks you should do things. In theory this reduces cost and complexity. In practice it requires organisations to change established processes, which is harder than it sounds and is frequently where SAP programmes run into difficulty.

---

## The Key Idea

SAP is not just software — it is an architectural landscape in its own right. Organisations that run SAP have made thousands of interconnected configuration decisions that function as their architecture. Understanding the landscape tiers, the module structure, and the fit-to-standard principle gives you enough to follow the conversation and understand why SAP programmes are complex, expensive, and consequential.

**Next:** Chapter 13 moves to Wardley Mapping — a fundamentally different way of thinking about the technology landscape, focused on evolution and competitive positioning rather than structure and compliance.

---

## Further Reading

- **SAP Architecture Centre** (architecture.sap.com): SAP's own library of reference architectures, patterns, and best practice guidance. The most authoritative source for SAP-specific architectural decisions.
- **SAP Certified Associate: SAP Enterprise Architect**: The official certification pathway for SAP architects. The exam guide gives a clear picture of what SAP considers core to the discipline.
- **Thomas Saueressig and Sven Denecken — SAP S/4HANA: The Reference Guide** (SAP Press): The most comprehensive introduction to S/4HANA for people who need to understand the platform without becoming developers.
- **Michael Missbach et al. — SAP on AWS: Architecture and Best Practices** (SAP Press): For organisations moving SAP to cloud infrastructure — what the architectural decisions look like in practice.
