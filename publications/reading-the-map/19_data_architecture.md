# Chapter 19: Data Architecture — The Domain Everyone Underestimates

*Part 3 · The Core Concepts*

---

Every application problem is eventually a data problem.

Systems can be replaced. Integrations can be rewritten. Infrastructure can be migrated. But data — the accumulated record of everything the organisation has ever done, every patient seen, every transaction processed, every decision made — does not move cleanly. It carries history, inconsistency, and meaning that no migration tool fully preserves. Organisations that treat data as a byproduct of their application estate, rather than as an asset in its own right, discover this the hard way, usually in the middle of a programme that was supposed to take eighteen months and is now in its fourth year.

**Data architecture** is the discipline that prevents that discovery from being a surprise. It describes what data the organisation uses, where it comes from, how it moves, who is responsible for it, and what rules govern its quality and use. It is the second domain in the BDAT stack, and the one most commonly underdeveloped — not because organisations do not care about data, but because data problems are invisible until they are catastrophic.

This chapter explains what data architecture covers, what the key concepts mean in plain language, and what Meridian's data situation reveals about the consequences of treating data as an afterthought.

---

## What Data Architecture Actually Covers

Data architecture is broader than most people expect when they first encounter it. It is not just database design. It is not just data modelling. It covers the full lifecycle of data — from the moment it is created or received, through how it is stored, transformed, moved, used, and eventually disposed of.

The discipline organises itself around four questions.

**What data exists?** The data inventory — a catalogue of the data assets the organisation holds. What entities are recorded, in which systems, at what granularity, and with what coverage. For Meridian, the entities include patients, clinicians, appointments, clinical events, medications, diagnoses, referrals, and staff. Each entity is recorded somewhere. The data inventory maps where.

**Where does it live and who owns it?** Data governance — the framework of accountability that assigns ownership and stewardship to each data asset. Ownership is accountability for the data's quality, accuracy, and fitness for purpose. Stewardship is day-to-day responsibility for maintaining it. In most organisations, ownership is contested or unclear. That unclarity is the root cause of most data quality problems.

**How does it move?** Data flows — the paths along which data travels between systems, people, and processes. A data flow diagram shows where data is created, where it is consumed, and how it gets from one place to the other. Integration architecture and data architecture overlap here: every integration is a data flow, and every data flow is an integration.

**What rules govern it?** Data policy — the constraints that apply to data use. Data protection law, clinical governance requirements, retention schedules, access controls, and quality standards. For Meridian, operating under NHS information governance and UK data protection law, the policy layer is significant and non-negotiable.

---

## Master Data and Why It Matters

The single most important concept in data architecture for most organisations is **master data**.

Master data is the data that the whole organisation depends on to be consistent, accurate, and agreed. It is the data about the core entities — the patients, the staff, the locations, the products, the accounts — that every system needs to reference and that every system needs to reference in the same way.

When master data is managed well, a patient record in one system refers to the same patient as a record in another system. A staff record in HR matches the account in the identity management system. A location record in the estates database matches the address in the clinical system. Everything connects cleanly because everything is referencing the same authoritative source.

When master data is managed badly, different systems hold different versions of the same entity. One system records a patient's date of birth as entered at registration in 2009. Another holds a corrected version from 2016 that was never propagated. A third holds a transcription error that has never been caught. None of the three systems knows the others exist, and nobody is accountable for which version is correct.

*At Meridian, master data management does not formally exist. The NHS number is the mandated patient identifier across the NHS, and Meridian's clinical systems do use it — but inconsistently. The legacy clinical portal uses NHS number as a secondary identifier and local hospital number as the primary key. The community nursing system uses NHS number but has a known data quality issue where approximately 3% of records have incorrect NHS numbers from a 2014 migration that was never fully validated. The two EPR systems use NHS number as the primary identifier but have different demographic data for approximately 12% of patients they both hold records for — the result of updates applied in one system that were never synchronised to the other. The EA's recommendation from Chapter 18 that Information and Analytics requires a data architecture decision before a technology decision was pointing directly at this. You cannot build a reliable reporting system on top of unresolved master data.*

---

## The Data Model

A **data model** is a formal description of the data an organisation holds — what entities exist, what attributes each entity has, and how entities relate to each other.

Data models exist at three levels of abstraction, each useful for different purposes.

A **conceptual data model** describes entities and relationships in business terms, without technical detail. Patient has Appointments. Appointment involves Clinician. Clinician belongs to Service. Used in architecture conversations with business stakeholders — it shows the domain structure without requiring anyone to understand database technology.

A **logical data model** adds detail — attributes, cardinality, and business rules. A patient has one or more NHS numbers over time. An appointment transitions through scheduled, confirmed, attended, and discharged. A clinical event must associate both a patient and a clinician.

A **physical data model** describes how data is stored in a specific technology — tables, data types, indexes. This is the province of database administrators and developers.

Enterprise architecture operates at the conceptual and logical levels. The physical model is an implementation detail belonging in the application and technology layers.

---

## Data Flows and Integration

Every integration between systems is a data flow. Data architecture maps those flows — not at the technical level of connection strings and message formats, but at the level of what data is moving, why, and what happens to it. The data flow view reveals things that application-level thinking misses.

It reveals **data latency** — how long after a clinical event occurs does the record of it appear in the systems that need it? At Meridian, community nursing records created in the field appear in the main EPR with a lag of up to 24 hours due to batch synchronisation. A clinician seeing the patient the following morning may be working from yesterday's record. That is not an application problem. It is a data architecture problem — the decision to use batch synchronisation rather than real-time integration was a data flow decision with clinical consequences.

It reveals **data duplication** — where the same data is held in multiple places, creating the risk of divergence. Meridian holds patient demographic data in both EPR systems. Both systems receive updates from external sources. Neither has a clear rule about which version takes precedence when they conflict.

It reveals **data loss** — where data is created in one system but never reaches the systems that need it. Meridian's legacy clinical portal generates clinical correspondence that is scanned and stored as a document. The content of that correspondence — diagnoses mentioned, medications changed, follow-up appointments requested — is never extracted into structured data. It exists, but it is invisible to any system that processes structured clinical data.

---

## Data Governance: Ownership and Stewardship

Data without governance is an accident waiting to happen. **Data governance** is the framework of policies, roles, and accountabilities that ensures data is managed as an asset rather than as a byproduct.

The key role in data governance is the **data owner** — the person or body that is accountable for a data asset's quality, accuracy, and fitness for purpose. Data ownership is a business role, not a technical one. The data owner for patient demographic data at Meridian is not the database administrator who maintains the tables. It is the clinical director accountable for patient safety — because inaccurate patient demographic data creates clinical risk.

The **data steward** is the person responsible for the day-to-day management of the data asset — monitoring quality, applying corrections, managing access requests, and escalating issues to the owner. Stewardship is operational. Ownership is accountable.

Most organisations have neither role clearly defined for most of their data assets. The result is that data quality problems are noticed by the people who encounter them — usually in reports, usually too late — and nobody is accountable for fixing them at the source.

*At Meridian, the first data governance exercise produces an uncomfortable finding: for 23 of the 31 data entities in the conceptual data model, there is no identified data owner. The patient record exists in two EPR systems with conflicting demographic data, and nobody is accountable for resolving the conflict. The clinical events data exists in the legacy portal as unstructured documents, and nobody has the mandate to extract and structure it. The staff data is maintained by HR but consumed by clinical systems that are not notified when staff records change — leading to clinical events being attributed to staff who have left the organisation. None of these problems is technically complex to fix. All of them require someone to be accountable for the data before the technical fix makes sense.*

---

## Data Architecture and the Other Domains

Data architecture connects to every other domain in the BDAT stack.

**Above it, business architecture:** The capability map identifies which capabilities depend on which data. Clinical Documentation depends on patient record data. Information and Analytics depends on clinical events data, demographic data, and activity data. When a capability is assessed as red, the data architecture question is always part of the explanation: is the capability weak because the application is inadequate, or because the data the application depends on is incomplete, inaccurate, or inaccessible?

**Below it, application architecture:** Applications are, from a data perspective, systems that create, transform, and consume data. The application portfolio question — which applications to keep, consolidate, or replace — cannot be answered without understanding the data each application holds and what would happen to that data in each scenario. The EPR consolidation question at Meridian is fundamentally a data question: can two patient records from different systems be merged into one without clinical harm?

**Below it, technology architecture:** Where data is stored, how it is backed up, how it is encrypted, and how it is recovered after failure are technology architecture questions with data architecture implications. The data residency requirements that constrain cloud adoption — patient data must remain in the UK — are data governance policies that the technology architecture must respect.

---

## Translator Panel

> **DAMA says:** "Data architecture defines the blueprint for managing data assets by aligning with organisational strategy to establish strategic data requirements and designs to meet those requirements."
>
> **What that means:** Data architecture is not about databases. It is about deciding what data matters, who is responsible for it, how it moves through the organisation, and what rules govern its use. It is as much a governance discipline as a technical one.

> **Architects say:** "We have a master data problem — we need to resolve patient identity before we can consolidate the EPRs."
>
> **What that means:** Two systems hold records for the same patients but cannot reliably confirm they are referring to the same person. Until that identity matching problem is solved — until there is one authoritative patient record that both systems agree on — consolidating the two systems will produce a merged database with unresolved conflicts. That is worse than two separate systems. Data architecture has to come before application architecture here, not after.

---

## The Key Idea

Data is the most durable thing in an enterprise architecture. Applications are replaced every ten to fifteen years. Infrastructure refreshes every five to seven. Data accumulates for decades. An organisation that manages its data well — that knows what it holds, who is responsible for it, how it moves, and what rules govern it — can survive almost any application or infrastructure change. An organisation that treats data as a byproduct of its systems discovers, at the worst possible moment, that the systems were ephemeral and the data was the real asset all along.

**Next:** Chapter 20 moves to application architecture — the third domain in the BDAT stack, and the one where most IT investment is concentrated. What an application portfolio is, how it is built and maintained, and what Meridian's portfolio reveals about fifteen years of decisions made without a shared architectural direction.

---

## Further Reading

- **DAMA International — DAMA-DMBOK: Data Management Body of Knowledge, 2nd edition** (Technics Publications, 2017): The authoritative reference for data management as a discipline. Comprehensive and practitioner-focused. The chapters on data governance, master data management, and data architecture are the most directly relevant to this chapter.
- **Thomas Redman — Data Driven: Profiting from Your Most Important Business Asset** (Harvard Business Review Press, 2008): The clearest executive-level argument for treating data as a managed asset rather than a technical byproduct. Accessible without being shallow.
- **NHS England — Data Standards and Information Governance** (england.nhs.uk): The national information governance framework for NHS organisations. The data standards — including NHS number as the primary patient identifier — are the policy layer within which Meridian's data architecture must operate.
- **Martin Fowler — Patterns of Enterprise Application Architecture** (Addison-Wesley, 2002): Not a data architecture book by title, but the integration and data management patterns it describes are the building blocks of the data flow architecture that this chapter introduces. The canonical reference for how data moves between systems.
