# Chapter 17: Architecture Principles — The Rules That Drive Decisions

*Part 3 · The Core Concepts*

---

Every architecture decision is made inside a set of constraints. Some of those constraints are explicit — budget, regulation, existing contracts. Some are implicit — cultural preferences, political realities, the weight of existing investment. **Architecture principles** are the attempt to make the implicit explicit: to write down the rules that should govern architectural decisions before those decisions arrive, so that when they do, the organisation is not starting from scratch.

A good set of architecture principles is one of the most valuable things an EA function can produce. A bad set — vague, contradictory, or disconnected from real decisions — is one of the most reliable ways to make the EA function look decorative. Most organisations have principles somewhere. Most of those principles are doing less work than they should.

This chapter explains what architecture principles are, what makes them useful, how to recognise the difference between principles that drive decisions and principles that decorate documents, and how Meridian's principles — or lack of them — shape what is and is not possible when the VMware crisis forces the organisation's hand.

---

## What an Architecture Principle Actually Is

An **architecture principle** is a statement that expresses a fundamental belief about how the organisation should make architectural decisions. It is not a standard. It is not a policy. It is not a technology preference. It is a declared position on a question that will recur — a way of pre-answering the recurring question so that each instance does not have to be debated from first principles.

The distinction matters. A standard says: we use PostgreSQL as our database platform. A principle says: we prefer open standards over proprietary technology. The standard flows from the principle. If the principle changes, the standard changes. If the principle is missing, the standard has no justification — it is just a preference with no stated rationale, which means it will be overridden whenever someone with enough authority wants something different.

A well-formed architecture principle has four components.

**Name** — a short, memorable label. Not a sentence. Something that can be spoken in a conversation and immediately recalled. "Cloud first." "Single source of truth." "Design for failure." Names that require explanation every time they are used are not working as principles.

**Statement** — a clear declarative sentence that says what the principle requires. Not what it aspires to. Not what it hopes for. What it requires. "All new workloads are deployed to cloud infrastructure unless a specific exemption is approved." Not "we should consider cloud infrastructure where appropriate."

**Rationale** — the reason the principle exists. What problem it is solving. What experience or evidence it is based on. The rationale is what makes a principle defensible when it is challenged — and principles are always challenged eventually.

**Implications** — the consequences of applying the principle. What it will require. What it will prevent. What it will cost. Implications are the most commonly omitted component and the most important one. A principle without stated implications is an aspiration. A principle with stated implications is a decision.

---

## Where Principles Come From

Architecture principles are not invented by the architecture team in isolation. They are derived — from organisational strategy, from regulatory requirements, from hard-won operational experience, and from the governance frameworks that the organisation operates under.

A principle like "patient data never leaves the UK" does not come from an architect's preference. It comes from data protection law, NHS policy, and clinical governance requirements. The architect's job is to surface that constraint as a principle — to make it explicit, documented, and connected to the decisions it affects — not to invent it.

A principle like "we do not create new point-to-point integrations" comes from operational experience. Every organisation that has allowed uncontrolled point-to-point integration has eventually produced an estate that cannot be changed without breaking something unexpected. The principle encodes that lesson so that each new project does not have to rediscover it.

A principle like "we design for cloud portability" comes from strategic intent. If the organisation has decided that vendor lock-in is a risk worth managing, that decision should be reflected in architectural decisions about APIs, data formats, and deployment approaches. The principle makes the strategic intent operational.

*Meridian does not have a formally documented set of architecture principles. It has a collection of informal positions — things the infrastructure team has always done, things the clinical systems team insists on, things the finance team expects — none of which have been written down, reconciled with each other, or connected to the strategic decisions they are supposed to inform. When the VMware crisis forces a platform decision, there is no agreed principle about cloud adoption, vendor lock-in, or open standards to anchor the conversation. Every stakeholder argues from their own unstated position. The EA's first task is not to answer the technical question — it is to surface the implicit principles, write them down, and get them agreed before the technical options can be meaningfully evaluated.*

---

## What Good Principles Look Like

Good principles are few, specific, and consequential. They say something that is not obviously true to everyone already, they apply to real decisions that actually recur, and applying them changes what gets built.

Here are three examples of principles doing real work, with the Meridian context.

**Cloud first.** *Statement:* New workloads are deployed to approved cloud platforms unless a clinical safety, data governance, or cost case is made for an alternative and approved by the Architecture Review Board. *Rationale:* On-premises infrastructure at Meridian is aging, expensive to maintain, and not sustainable given the VMware licensing position. Cloud platforms provide commodity compute and storage at commodity prices, freeing capital for clinical system investment. *Implications:* All new projects must assess cloud deployment first. Infrastructure team skills and practices need to shift from on-premises management to cloud governance. Applications with cloud-incompatible dependencies must be remediated before migration or maintained on legacy infrastructure with explicit sunset plans.

**Single patient identity.** *Statement:* Every clinical system that references a patient uses the NHS number as the primary patient identifier. No new integration may use a local identifier as the primary key. *Rationale:* Meridian's dual-EPR estate has produced patient matching errors that have reached the clinical safety team. Different local identifiers in different systems create the risk of clinical decisions being made on the wrong patient record. *Implications:* The integration team must ensure NHS number matching is implemented in all existing integrations at next major version. New systems that cannot consume NHS numbers as primary identifiers are not approved for procurement.

**No new bespoke integrations.** *Statement:* New integrations between clinical systems are implemented using the agreed integration platform and approved messaging standards. Point-to-point integrations require ARB approval and a stated decommission plan. *Rationale:* Meridian currently has 34 point-to-point integrations. Eleven of them are undocumented. Changes to any core system require manual impact assessment across all 34. This is unsustainable at scale and creates clinical risk when integrations fail silently. *Implications:* The integration platform must be procured or designated before this principle can be enforced. Existing point-to-point integrations are catalogued, risk-assessed, and migrated on a priority order agreed with clinical governance.

Each of these principles says something specific. Each has a rationale grounded in Meridian's actual situation. Each has implications that require real decisions and real investment. None of them is comfortable. That is the test.

---

## What Bad Principles Look Like

Bad principles are common and recognisable. They share a set of failure modes.

**Vacuous agreement.** "We will use best-of-breed technology." Every organisation agrees with this. Nobody disagrees with best-of-breed. The principle decides nothing because no option has ever been presented as worst-of-breed. A principle that everyone agrees with immediately is not doing any work.

**Strategy disguised as principle.** "We will deliver excellent patient care through integrated technology solutions." This is a mission statement. It cannot be applied to an architectural decision. When someone proposes a new integration approach and asks whether it complies with this principle, the answer is always yes because the principle is too abstract to falsify.

**Uncosted implication.** "We will not create technical debt." This sounds rigorous but the implications have not been faced. Eliminating technical debt requires investment, time, and frequently delaying delivery of features the business wants. A principle that cannot be applied without a conversation about what it will cost is a principle whose rationale has not been completed.

**Contradiction without resolution.** A set of principles that includes both "we design for resilience and redundancy" and "we minimise infrastructure cost" is going to produce conflict in every project that encounters a trade-off between the two. Both are legitimate positions. But a principle set that does not establish which takes precedence — or under what conditions each applies — transfers the decision to whoever is in the room at the time, which is precisely what principles are supposed to prevent.

> *A principle that everyone agrees with immediately is not a principle — it is a platitude. A principle earns its place by saying something that someone, somewhere, will want to argue with.*

---

## Principles in the Architecture Governance Cycle

Principles are not a one-time exercise. They are part of the architecture governance cycle — the ongoing process of maintaining architectural direction as the organisation changes.

Principles are created when new strategic decisions create new architectural constraints, or when operational experience reveals a recurring decision that needs to be pre-answered. They are reviewed when the strategy changes, when a principle is found to be producing bad outcomes, or when two principles are found to be in conflict in a way that is causing problems.

They are applied through the **Architecture Review Board** — the governance body that assesses proposed changes to the estate against the agreed principles. The ARB does not approve or reject based on technical preference. It assesses whether a proposed solution complies with the organisation's declared principles, and where it does not, whether the exception is justified and what the conditions of that exception are.

*At Meridian, the ARB does not yet exist. The EA is building the case for it. Her argument is simple: without a body that applies principles consistently, every project team makes its own architectural decisions, those decisions accumulate into an estate nobody designed, and the organisation spends its operational budget managing the consequences. The VMware crisis is the consequence of decisions made without consistent governance over fifteen years. The ARB is the mechanism that prevents the next crisis from developing in the same way.*

---

## Translator Panel

> **TOGAF says:** "Architecture principles are general rules and guidelines, intended to be enduring and seldom amended, that inform and support the way in which an organisation sets about fulfilling its mission."
>
> **What that means:** Architecture principles are the standing rules that shape how architectural decisions get made. They are written before the decisions arrive, applied consistently when they do, and changed only when the organisation's strategic direction genuinely changes — not when a project finds them inconvenient.

> **Architects say:** "This proposal doesn't comply with the cloud-first principle — we need an ARB exception."
>
> **What that means:** The project wants to do something that contradicts a stated organisational rule. That contradiction needs to be made explicit, justified, and approved by the right governance body — not quietly set aside because it is inconvenient. The exception process is not bureaucracy. It is the mechanism that keeps principles from becoming fiction.

---

## The Key Idea

Architecture principles are the pre-answered questions that stop every architectural decision becoming a negotiation from scratch. Good principles are few, specific, consequential, and uncomfortable — they rule something out. Bad principles are vague, universally agreed, and disconnected from real decisions. The difference between an EA function that drives decisions and one that documents them after the fact is often found here: in whether the organisation has principles that actually govern what gets built, or principles that decorate the strategy document while the real decisions happen elsewhere.

**Next:** Chapter 18 goes deeper into the business architecture domain — capability maps in practice. How they are built, assessed, heat-mapped, and connected to the application portfolio decisions that follow.

---

## Further Reading

- **The Open Group — TOGAF Standard: Architecture Principles** (opengroup.org): The TOGAF guidance on architecture principles is concise and practical. The four-component structure — name, statement, rationale, implications — comes from here and is the most useful single framework for writing principles that do real work.
- **Gregor Hohpe — The Software Architect Elevator** (O'Reilly, 2020): Chapter 4 addresses the role of principles in architectural governance with the kind of honest, practitioner-grounded perspective that formal frameworks often avoid. Recommended alongside the TOGAF guidance.
- **Ruth Malan and Dana Bredemeyer — Less Is More with Architecture Principles** (bredemeyer.com): A short, freely available paper that makes the case for fewer, stronger principles over comprehensive principle catalogues. One of the most useful single pieces of writing on the subject.
- **NHS England — Architecture Principles for Health and Social Care** (england.nhs.uk/digitaltechnology): The NHS publishes its own architecture principles for the health and care system. For anyone working in or with NHS organisations, these principles are the regulatory and strategic context within which local principles like Meridian's must sit.
