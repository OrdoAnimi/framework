# Chapter 4: The Landscape at a Glance

## Opening

Before Part 2 takes you through each framework in depth, you need a map of the territory itself.

Part 2 covers fourteen frameworks. If you encounter them one by one without any sense of how they relate, you will accumulate fourteen separate mental models that do not connect. That is not how the profession works. These frameworks are not alternatives. They are not competitors. Most of them address different aspects of the same problem, and an architect working in a large organisation typically uses several of them simultaneously.

This chapter gives you the overview before the detail. Every major framework named. The type it belongs to. What problem it was designed to solve. How it relates to the others. By the end of this chapter you will have a working map of the landscape. Part 2 walks you through each location on that map.

---

## The four types

The frameworks in Part 2 divide into four types. Knowing which type you are dealing with tells you what to expect from it — and prevents the frustration of reaching for something it was never designed to provide.

**Classification systems** organise architecture descriptions. They do not tell you how to develop architecture. They tell you what types of description exist and where each one belongs. Zachman is the primary example. It does not give you a process. It gives you a grid — a way of ensuring that every type of description of an enterprise has a home and nothing important is confused with something else.

**Development methodologies** provide a process for doing architecture work. They tell you how to move from where you are to where you need to be, what phases to move through, and what to produce at each stage. TOGAF and its ADM is the primary example. It tells you how to approach the work. It does not tell you which technology to choose or which products to buy.

**Notation standards** provide a visual language for drawing architecture so that other practitioners can read it. They are not methodologies and not classification systems. They are shared vocabularies for diagrams. ArchiMate is the primary example. Without a notation standard, every architect draws differently. With one, a diagram produced in one organisation can be read by an architect from another without being told what the shapes mean.

**Domain-specific frameworks** apply architecture thinking to a particular domain — security, business, government, defence. SABSA for security architecture. BIZBOK for business architecture. FEAF and DODAF for government and defence contexts. SAP EA for SAP technology landscapes. Each addresses a domain that general frameworks cover only partially.

*Meridian's new enterprise architect spends her first week cataloguing what frameworks the organisation nominally uses. TOGAF is referenced in the EA strategy document from 2021. Nobody is sure which version. ArchiMate is mentioned in a job description posted eighteen months ago for a role that was never filled. SABSA appears in a security policy document as something the organisation "intends to align with." The actual practice bears little resemblance to any of them. That is not unusual. Knowing the frameworks and applying them are different things, and most organisations are somewhere on the journey between the two.*

---

## The frameworks at a glance

| **Framework** | **Type** | **Primary problem it solves** | **Where you encounter it** |
|---|---|---|---|
| **Zachman** | Classification system | Organising every type of architecture description so nothing is missed or confused | Government IT, formal EA education, completeness checking |
| **TOGAF / ADM** | Development methodology | Structured process for developing enterprise architectures from vision to governance | Almost everywhere EA is practised formally |
| **ArchiMate** | Notation standard | Common visual language for drawing architecture so any practitioner can read it | Alongside TOGAF; architecture tools like Archi and Sparx |
| **FEAF** | Domain-specific (government) | Common EA approach for US federal agencies | US federal government programmes and their contractors |
| **DODAF** | Domain-specific (defence) | Standardised architecture descriptions for US defence systems | US defence programmes; defence contractors |
| **MODAF / NAF** | Domain-specific (defence) | UK MoD and NATO equivalents to DODAF | UK defence; NATO multi-nation programmes |
| **SABSA** | Domain-specific (security) | Security architecture traceable to business risk rather than technical checklists | Regulated industries; anywhere security architecture is taken seriously |
| **BIZBOK** | Domain-specific (business) | Business architecture — capabilities, value streams, motivation models | Large organisations doing capability mapping; public sector transformation |
| **SAP EA** | Domain-specific (SAP) | Governing complex SAP landscapes across their development, QA, and production tiers | Any organisation running SAP S/4HANA or legacy ECC |
| **Wardley Mapping** | Adjacent discipline | Positioning technology decisions on an evolution curve to inform strategy | Technology strategy; cloud adoption decisions; build-vs-buy reasoning |
| **ITIL** | Adjacent discipline | IT service management — how to operate the estate the architecture designs | Everywhere IT services are delivered formally |
| **COBIT** | Adjacent discipline | IT governance — how to ensure IT delivers value and manages risk | Regulated environments; audit and compliance contexts |

---

## Why there are so many

The variety is not an accident or a failure of the profession to consolidate. It reflects three real things.

**Different problems require different tools.** A framework designed to govern the procurement and interoperability of US defence systems does not look like a framework designed to help a retail bank map its business capabilities. The contexts are different. The stakeholders are different. The failure modes are different. Specialist frameworks exist because generic frameworks cannot serve every context equally well.

**The profession grew in layers.** Zachman came first, in 1987, with the classification insight. TOGAF came next, in 1995, with the process. ArchiMate came later, in the 2000s, with the notation. SABSA, BIZBOK, and the domain-specific frameworks developed as practitioners in specific fields found that generic frameworks did not fully address their domain's concerns. Each addition was a response to a real gap, not an academic exercise.

**No single framework is complete.** This is the most important point. TOGAF tells you how to develop architecture but does not tell you how to draw it. ArchiMate tells you how to draw architecture but does not tell you how to develop it. SABSA tells you how to design security architecture but relies on TOGAF or another methodology for the broader development process. The frameworks are not competing attempts to solve the same problem. They are complementary instruments that cover different aspects of a problem too large for any single framework to address fully.

*An architect joining Meridian from a banking background arrives with TOGAF certification, ArchiMate fluency, and solid COBIT knowledge from years of working in a regulated environment. She has never used SABSA formally but understands the principles. She has never used BIZBOK but has done capability mapping using her own approach. On day one she does not need to be told which frameworks to use. She draws on what she knows, identifies where the gaps are for this specific context, and fills them as the work requires. That is how every experienced practitioner operates. The frameworks are a toolkit. The work determines which tools you reach for.*

---

## How they relate

The relationships between the frameworks matter as much as the frameworks themselves.

**TOGAF and ArchiMate are designed to work together.** Both are published by The Open Group. TOGAF provides the development process. ArchiMate provides the notation for the outputs that process produces. In practice they are almost always used in combination. An architect running a TOGAF ADM programme produces ArchiMate views at each phase. The frameworks are not alternatives — they are complementary halves of the same practice.

**TOGAF and COBIT address adjacent concerns.** TOGAF governs how architecture is developed. COBIT governs how IT delivers value and manages risk. In regulated environments — financial services, healthcare, government — both are typically in use simultaneously, with COBIT providing the governance structure that TOGAF's Phase G relies on.

**SABSA and TOGAF are explicitly designed to integrate.** SABSA contributes the security architecture layer to each ADM phase. An organisation using TOGAF for its EA programme and SABSA for security architecture is not running two separate processes — it is running one process with a security architecture dimension embedded at each phase.

**BIZBOK sits above TOGAF in the architecture stack.** Business architecture — capabilities, value streams, motivation models — is the starting point from which application and technology architecture are derived. In TOGAF terms, the business architecture domain is the first domain. BIZBOK provides the depth of method for that domain that TOGAF does not fully supply.

**Wardley Mapping, ITIL, and COBIT are adjacent disciplines.** They are not enterprise architecture frameworks by self-description, but they address problems that EA also addresses, and the communities overlap significantly. An architect who cannot read a Wardley Map is missing a strategic tool that is increasingly common in technology leadership conversations. An architect who does not understand ITIL and COBIT is missing the operating model that sustains the estate they design.

---

## What this means for how you read Part 2

Part 2 covers each framework in a separate chapter. Each chapter tells you what the framework is, where it came from, what problem it solves, what it does well, and where its limits are. Each chapter includes a translator panel — the official definition on one side, the plain English on the other. Each chapter connects the framework to Meridian so you can see it in a real context.

You do not need to read Part 2 in order. If you encounter a specific framework in your work and need to understand it quickly, go directly to that chapter. The chapters are designed to stand alone as well as to build on each other.

What you do need to carry from this chapter into every chapter in Part 2 is the type question. Every time you encounter a framework, ask: is this a classification system, a development methodology, a notation standard, or a domain-specific framework? The answer tells you what it can do for you and what it cannot. That is the single most useful filter in the landscape.

---

## Translator Panel

> **The profession says:** "Enterprise architecture frameworks provide structured approaches for developing, governing, and communicating enterprise architectures across business, data, application, and technology domains."
>
> **What that means:** Different teams and organisations have packaged their accumulated knowledge about how to do architecture work into frameworks — structured sets of concepts, methods, and vocabulary. Some of those packages cover the whole development process. Some cover a specific domain. Some just define how to draw things. Knowing which type of package you are holding tells you whether it will do what you are hoping for.

---

## The Key Idea

The landscape of frameworks is not a menu — you do not pick one and ignore the rest. It is a toolkit where each instrument addresses a different aspect of the same broad challenge. Classification systems, development methodologies, notation standards, and domain-specific frameworks are complementary, not competing. Most experienced architects use several simultaneously.

**Next:** Chapter 5 begins Part 2 with Zachman — the classification system that gave the profession its first way of thinking about itself, and the intellectual foundation that makes every framework that followed easier to understand.

---

## Further Reading

- **The Open Group Architecture Framework — TOGAF Standard, 10th Edition** (opengroup.org): The most complete single source for understanding how TOGAF positions itself relative to other frameworks. The introduction section explicitly addresses how TOGAF relates to Zachman, ArchiMate, and COBIT.
- **Zachman International** (zachman.com): John Zachman's own site includes the framework specification and a substantial library of explanatory material, including his original 1987 IBM Systems Journal paper.
- **The Business Architecture Guild** (bizbok.org): The BIZBOK guide is available to members. The guild's public resources include a useful overview of how business architecture relates to enterprise architecture more broadly.
- **AXELOS — ITIL 4 Foundation** (axelos.com): The starting point for understanding ITIL. The Foundation guide is intentionally accessible and covers the service management concepts that any EA working alongside an ITIL-aligned operations team needs to recognise.
