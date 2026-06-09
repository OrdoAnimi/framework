# Chapter 14: ITIL — Running What Architecture Builds

*Part 2 · The Frameworks Explained*

---

Architecture designs the estate. ITIL runs it.

That one sentence explains why the relationship between the two disciplines is simultaneously essential and frequently misunderstood. Enterprise architects design the systems, the integrations, the platforms, the data flows. IT service management — governed in most organisations by **ITIL** — is the discipline that operates those systems once they exist. Without architecture, service management operates an estate it does not fully understand. Without service management, architecture produces designs that nobody maintains.

Most people in IT encounter ITIL before they encounter enterprise architecture. The incident management process, the change advisory board, the service desk — these are ITIL concepts, even when nobody calls them that. If you have ever logged a support ticket, attended a change freeze, or been told that a release has been blocked pending CAB approval, you have been inside an ITIL-governed service management process.

This chapter explains what ITIL is, where it came from, what its core concepts mean in plain language, and how it connects to the EA frameworks you have already met.

---

## Where ITIL Came From

**ITIL** — the IT Infrastructure Library — was developed by the UK government's Central Computer and Telecommunications Agency in the late 1980s. The problem it was designed to solve was the same problem Zachman was addressing in the same period: organisations had accumulated large, complex technology estates with no consistent way of operating them. Every organisation ran its IT services differently. Quality was inconsistent. Failures were managed reactively. There was no shared vocabulary for describing what good service management looked like.

ITIL collected best practices from organisations that were operating IT services well and documented them in a library of guidance. The name stuck even as the framework evolved far beyond its origins as a physical library of books.

The framework has been through four major versions. ITIL v2, published in the early 2000s, established the process-based approach that most practitioners over forty will recognise. ITIL v3, published in 2007, introduced the service lifecycle concept. **ITIL 4**, published in 2019, made the most significant structural shift: moving from a process library toward a more flexible system focused on value creation and explicitly acknowledging the realities of agile, DevOps, and cloud-native delivery.

ITIL is owned and published by **AXELOS**. The certification pathway is one of the most widely held in the IT profession globally. ITIL Foundation is frequently listed as a requirement in IT operations roles.

---

## The Service Management Concept

The central idea in ITIL is the **service**. Not a system. Not an application. A service.

A service is something that delivers value to a user without requiring the user to manage the underlying complexity that produces it. When a clinician at Meridian opens the patient record system, she is consuming a service. She does not know whether the EPR is running on-premises or in the cloud. She does not know which VMware host is serving her session. She knows that she can see the patient record she needs. That is the service.

This framing shifts the unit of accountability. ITIL is not primarily concerned with whether a server is running. It is concerned with whether the service is available to the user who needs it, performing to the level the organisation has committed to, and recoverable within an acceptable timeframe when things go wrong.

*At Meridian, the VMware estate is the infrastructure underneath a set of services. When the VMware licensing crisis threatens the infrastructure layer, the service management question is not "what happens to our VMs?" It is "which services fail, for which users, for how long, and what are the clinical consequences?" ITIL gives Meridian the vocabulary and the processes to answer that question before the failure happens rather than during it.*

---

## The Four Dimensions

ITIL 4 organises service management thinking around four dimensions that must all be considered for any service to work properly.

**Organisations and people** — who is responsible for delivering and consuming the service, what skills and culture are required, and how accountability is structured. A technically perfect service design fails if nobody owns the operational responsibility.

**Information and technology** — the data, tools, and systems that underlie the service. This is where architecture and service management most directly overlap: the application portfolio and infrastructure estate that the architect designs become the information and technology dimension of every ITIL service.

**Partners and suppliers** — the external organisations that contribute to service delivery. For Meridian, this includes the EPR vendors, the network provider, the cloud provider for the shared services arrangement, and any managed service partners.

**Value streams and processes** — how work flows through the organisation to deliver the service. The process dimension is where ITIL's detailed practice guidance lives — incident management, change management, problem management, and the rest.

---

## The Practices You Will Encounter

ITIL 4 uses the term **practices** rather than processes, partly to signal that the guidance covers people and tools as well as procedure. There are 34 practices in ITIL 4. Most people in IT encounter a core set of them regularly.

**Incident management** is the practice of restoring normal service operation as quickly as possible when something goes wrong. An incident is an unplanned interruption to a service. The incident management process prioritises, assigns, escalates, and resolves. It does not ask why the incident happened — that is problem management's job.

**Problem management** is the practice of finding and addressing the root causes of incidents. A problem is the underlying cause of one or more incidents. Problem management produces known errors — documented faults with identified workarounds — and drives permanent fixes where they are warranted.

**Change enablement** is the practice of controlling changes to the technology estate so that changes do not cause incidents. This is where the **Change Advisory Board** — the **CAB** — sits. Not every change goes to the CAB. Standard changes, pre-approved as low-risk, can be made without review. Normal changes require CAB review. Emergency changes have an expedited path for urgent situations.

**Service level management** is the practice of setting and monitoring the agreed levels at which services are delivered. A **Service Level Agreement** — an **SLA** — is the formal commitment between the service provider and the consumer, specifying availability, performance, and recovery time targets.

**Configuration management** maintains the **Configuration Management Database** — the **CMDB** — a record of the components that make up the IT estate and their relationships. The CMDB is where architecture and service management share the same data: the assets the architect models and the assets the service management team operates are the same assets. When they are recorded differently in different tools, both disciplines suffer.

*At Meridian, the CMDB is three years out of date. The configuration management team knows it. The architecture team knows it. Neither has had the resources or the mandate to address it. When the EA begins the Phase C baseline exercise for the VMware exit programme, she discovers 17 applications not in the CMDB at all. When she adds them, the service management team discovers three have no incident escalation path — meaning that if they fail outside business hours, nobody is automatically notified. The CMDB update is architectural work. The consequence is service management work. The boundary between the two disciplines is artificial.*

---

## ITIL and the EA Frameworks

ITIL connects to the EA frameworks at several specific points.

**With TOGAF Phases G and H:** Phase G establishes architecture governance — ensuring the estate is built as the architecture says it should be. Phase H maintains the architecture as the organisation evolves. Both phases depend on knowing what actually exists and how it is changing. The CMDB is the source of that truth. An architecture programme that ignores the CMDB produces governance artefacts that do not reflect operational reality.

**With the application portfolio:** The application portfolio catalogues the applications in the estate and assesses their fitness for purpose. The ITIL configuration management practice maintains the CMDB that the portfolio draws on. Keeping these two records aligned is one of the most practical and most neglected integration points in most organisations.

**With the capability map:** ITIL service management is itself a set of organisational capabilities — incident management capability, change management capability, problem management capability. A capability map that does not include these is incomplete.

> *Architecture without service management is a design that nobody maintains. Service management without architecture is an operation that nobody understands.*

---

## What ITIL Does Well and Where Its Limits Are

ITIL does several things exceptionally well. It gives organisations a shared vocabulary for service management that is understood globally. It provides a structured approach to incident, problem, and change management that, applied consistently, significantly reduces the operational chaos that large IT estates generate by default. ITIL 4's shift toward value orientation makes it easier to connect service management practice to business outcomes rather than treating it as an internal discipline disconnected from users.

Its limits are real. ITIL can become bureaucratic when applied as a compliance exercise rather than a value-delivery discipline. Change advisory boards that review every change regardless of risk, SLAs that measure what is easy to measure rather than what matters to users — these are ITIL applied as theatre rather than practice.

ITIL also does not tell you what architecture your services should have. It tells you how to operate services once they exist. An organisation with a poorly designed estate managed through excellent ITIL practice still has a poorly designed estate — it is just failing in a well-documented, consistently categorised, properly escalated way.

---

## Translator Panel

> **ITIL says:** "A service is a means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks."
>
> **What that means:** A service delivers a result to a user without the user needing to understand the complexity behind it. The clinician gets the patient record without managing the database, the network, or the server. ITIL is the discipline that makes that transparency possible and sustainable.

> **ITIL says:** "The purpose of the incident management practice is to minimise the negative impact of incidents by restoring normal service operation as quickly as possible."
>
> **What that means:** When something breaks, fix it fast. Do not spend time in the middle of an incident finding the root cause — that is problem management's job. Incident management has one goal: restore the service. Everything else comes after.

---

## The Key Idea

ITIL is the discipline that operates what architecture designs. The two are not competitors — they are sequential and interdependent. Architecture produces the estate. ITIL runs it. When they share data through the CMDB, speak a common language about services and components, and connect their governance cycles, both work better. When they operate in isolation — as they do in most organisations — both are weaker than they need to be.

**Next:** Chapter 15 moves to COBIT — the IT governance framework that sits above ITIL and connects IT management to enterprise risk, compliance, and board-level accountability.

---

## Further Reading

- **AXELOS — ITIL 4 Foundation** (axelos.com): The official starting point. The Foundation guide covers all the core concepts this chapter introduces. The certification exam is straightforward if you have read this chapter first.
- **AXELOS — ITIL 4 Managing Professional and Strategic Leader streams**: The post-Foundation tracks for practitioners going deeper. Managing Professional covers the delivery practices. Strategic Leader covers the governance and leadership layer.
- **Mark Smalley, Dave Wheeldon, and Wynne van Graan — ITIL 4: A Pocket Guide** (Van Haren Publishing): The most concise single-volume reference for ITIL 4. Useful as a lookup when you encounter a practice or term in the field.
- **The Open Group — TOGAF and ITIL integration guidance** (opengroup.org): Search for "TOGAF ITIL integration." Addresses the practical connection points between EA governance and service management that this chapter describes.
