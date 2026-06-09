# Chapter 15: COBIT — Governing What IT Does

*Part 2 · The Frameworks Explained*

---

ITIL tells you how to run IT services. COBIT tells you whether IT is doing the right things, doing them correctly, and being held accountable for the outcomes.

That distinction matters. An organisation can have excellent incident management, a clean CMDB, and well-documented SLAs — and still have an IT function that is investing in the wrong things, taking on risks it has not disclosed, and failing to demonstrate value to the board. COBIT addresses that gap. It is the framework that connects IT management to enterprise governance — to the risk appetite, the compliance obligations, and the strategic accountability that boards and executives carry.

**COBIT** — Control Objectives for Information and Related Technologies — is published by **ISACA**, a global professional association for IT governance, audit, and security professionals. It is less commonly discussed in day-to-day IT conversations than ITIL, but in regulated environments — financial services, healthcare, government, utilities — it is frequently the framework that determines how IT decisions are made and how they are audited.

If you work in or around IT governance, audit, compliance, or risk, you will encounter COBIT directly. If you work in architecture in a regulated environment, you will encounter its consequences — the governance structures, the control frameworks, and the audit requirements that COBIT shapes.

---

## Where COBIT Came From

COBIT was first published in 1996 by ISACA, initially as an audit framework — a way for IT auditors to assess whether IT controls were adequate and whether IT was being governed appropriately. The first versions were primarily checklists for auditors rather than guidance for practitioners.

Over six major versions, COBIT evolved from an audit tool into a comprehensive IT governance framework. COBIT 5, published in 2012, was the version that most organisations currently running COBIT-aligned governance will recognise. **COBIT 2019**, the current version, restructured the framework around a design approach — allowing organisations to tailor the framework to their specific governance context rather than applying it wholesale.

The evolution reflects a genuine maturation in thinking about IT governance. Early COBIT asked: are the controls in place? Current COBIT asks: are the right governance structures in place to make the right decisions about IT, and is IT demonstrably serving the organisation's goals?

---

## The Core Concept: Separating Governance from Management

The most important conceptual contribution COBIT makes is the explicit separation of **governance** from **management**. This distinction sounds academic until you are in a room where the two are being confused — which is most rooms.

**Governance** is about setting direction, evaluating options, and holding the organisation accountable for outcomes. Governance asks: are we doing the right things? It is the domain of boards, executive committees, and senior leadership. Governance bodies do not run IT. They set the objectives, the risk appetite, and the accountability framework within which IT is run.

**Management** is about planning, building, running, and monitoring activities in pursuit of the direction governance has set. Management asks: are we doing things correctly, and are we getting the results we committed to? This is the domain of the CIO, the IT leadership team, and the practitioners — including architects — who deliver the work.

*At Meridian, the governance question is: should we invest in the cloud migration? That decision belongs to the executive committee and the board — they set the strategic direction and the risk appetite. The management question is: how do we execute the migration safely within the parameters the board has set? That belongs to the CIO, the EA, and the delivery teams. When the board starts making architectural decisions and the architecture team starts deciding whether the investment is strategically justified, the governance-management boundary has collapsed. COBIT makes that boundary explicit and argues, with evidence, that keeping it clear produces better outcomes.*

---

## The COBIT Framework Structure

COBIT 2019 organises its guidance around a set of **governance and management objectives** — specific outcomes that a well-governed IT function should be able to demonstrate.

These objectives are grouped into two domains. The governance domain contains five objectives focused on evaluating, directing, and monitoring IT. The management domain contains 35 objectives organised across four areas: aligning, planning, and organising; building, acquiring, and implementing; delivering, servicing, and supporting; and monitoring, evaluating, and assessing.

The framework provides, for each objective, a description of the outcome, a set of practices that contribute to achieving it, a set of activities within each practice, and capability levels that allow an organisation to assess how well it is performing against that objective.

This structure is what makes COBIT useful for auditors. An auditor can select the objectives relevant to their scope, assess the organisation's practices against the framework, and produce a structured finding. It is also what makes COBIT dense for first-time readers — there is a lot of it, and it is not designed to be read cover to cover.

*Meridian's audit committee has asked for assurance that the VMware exit programme is being governed appropriately. The internal audit team uses COBIT's managed change management objective to assess whether the programme has adequate controls: is there a defined change process, are changes being approved at the right level, is impact being assessed before changes are implemented, and are post-implementation reviews happening? The audit does not assess the technical quality of the migration plan. It assesses whether the governance of the plan is adequate. That is COBIT's contribution — and it is different from what any EA framework provides.*

---

## The Five Governance Objectives

The governance domain — **Evaluate, Direct, and Monitor** — is where COBIT is most directly relevant to enterprise architects and senior IT leaders.

**EDM01 — Ensured Governance Framework Setting and Maintenance** asks whether the organisation has a governance framework for IT that is appropriate to its context, regularly reviewed, and actively used. This is the meta-objective: the governance of the governance system itself.

**EDM02 — Ensured Benefits Delivery** asks whether IT investments are delivering the value that was committed when they were approved. This is the objective that connects IT governance to business outcomes — and the one most frequently under-addressed in organisations where IT investment decisions are made without systematic tracking of whether the benefits materialised.

**EDM03 — Ensured Risk Optimisation** asks whether IT-related risks are identified, assessed, and managed within the organisation's risk appetite. Risk appetite is the key concept here — governance sets how much risk the organisation is willing to accept, and management operates within that boundary. An architecture decision that introduces risk beyond the approved appetite is a governance issue, not just a technical one.

**EDM04 — Ensured Resource Optimisation** asks whether IT resources — people, technology, and information — are being allocated appropriately to support the organisation's strategic objectives.

**EDM05 — Ensured Stakeholder Engagement** asks whether stakeholders are engaged appropriately in IT governance and whether their needs are being understood and addressed.

---

## COBIT and the EA Frameworks

COBIT connects to the EA frameworks you have already met at specific and important points.

**With TOGAF Phases G and H:** TOGAF's architecture governance phases — ensuring the estate is built as designed and maintained as the organisation evolves — operate within the governance framework that COBIT defines. The Architecture Review Board that Phase G establishes is a management structure. The executive accountability for architectural direction sits in the governance layer that COBIT addresses. COBIT defines the governance context within which TOGAF operates.

**With ITIL:** ITIL provides the service management practices. COBIT provides the governance framework within which those practices are overseen. The CAB is an ITIL structure. The decision about what risk level requires CAB escalation to executive governance is a COBIT question. The two frameworks are sequential — ITIL runs the operation, COBIT ensures the operation is being run within the boundaries the organisation has set.

**With the application portfolio:** COBIT's benefits delivery objective (EDM02) is directly relevant to application portfolio management. Decisions about which applications to invest in, maintain, or retire should be traceable to business outcomes. An application portfolio that cannot demonstrate its contribution to approved strategic objectives is failing the benefits delivery test.

> *COBIT does not tell you what architecture to build. It tells you whether the process by which you decided to build it was governed appropriately, and whether the outcome delivered what was promised.*

---

## What COBIT Does Well and Where Its Limits Are

COBIT does several things exceptionally well. It provides the clearest and most comprehensive framework available for connecting IT management to enterprise governance. Its explicit separation of governance from management resolves one of the most persistent sources of confusion and dysfunction in IT organisations. And its audit-friendly structure makes it the framework of choice in regulated environments where external assurance is required.

Its limits are equally clear. COBIT is comprehensive to the point of density. Implementing the full framework in a small or medium-sized organisation is disproportionate — the overhead exceeds the benefit. Most organisations that use COBIT apply a subset relevant to their regulatory context and governance maturity. COBIT 2019's design approach explicitly supports this tailoring, but it requires enough framework literacy to make the right selection.

COBIT is also not a methodology for doing architecture work, designing services, or managing delivery. It provides the governance context within which all of those activities happen. Organisations that confuse governance with management — treating COBIT as an operational framework — produce governance overhead without the clarity that good governance is supposed to provide.

---

## Translator Panel

> **COBIT says:** "Governance ensures that stakeholder needs, conditions, and options are evaluated to determine balanced, agreed-on enterprise objectives to be achieved; setting direction through prioritisation and decision making; and monitoring performance and compliance against agreed-on direction and objectives."
>
> **What that means:** Governance is the process by which the organisation decides what IT should be doing, ensures IT is actually doing it, and holds IT accountable for the results. It is not the same as running IT. It is the oversight structure within which IT is run.

> **COBIT says:** "Management plans, builds, runs, and monitors activities in alignment with the direction set by the governance body to achieve the enterprise objectives."
>
> **What that means:** Once governance has set the direction and the boundaries, management figures out how to deliver within them. The CIO manages. The board governs. Keeping those roles separate — and clear — is one of the most valuable things COBIT does.

---

## The Key Idea

COBIT is the framework that makes IT accountable to the organisation rather than accountable only to itself. It connects IT investment to strategic outcomes, IT risk to enterprise risk appetite, and IT management to board-level governance in a way that no service management or architecture framework fully addresses. In regulated environments it is not optional — it shapes the governance structures within which every other framework operates.

**Next:** Chapter 16 begins Part 3 — the core concepts of enterprise architecture. After two parts of framework landscape, Part 3 goes inside the practice: the tools, the artefacts, and the thinking patterns that architects use every day, explained in plain language for everyone who works alongside them.

---

## Further Reading

- **ISACA — COBIT 2019 Framework: Introduction and Methodology** (isaca.org): The foundational document. Available from ISACA. The introduction and design guidance sections are the most useful starting points before engaging with the full objective library.
- **ISACA — COBIT 2019 Design Guide**: The companion document to the framework that explains how to tailor COBIT to a specific organisational context. Essential if you are involved in implementing rather than just reading COBIT.
- **Steven De Haes, Wim Van Grembergen, Anant Joshi, and Tim Huygh — Enterprise Governance of Information Technology** (Springer, 3rd edition): The academic foundation for COBIT's conceptual model. More detailed than most practitioners need but valuable for understanding why the governance-management distinction matters structurally.
- **ISACA — COBIT and TOGAF alignment guidance**: ISACA has published mapping guidance between COBIT and TOGAF. Search isaca.org for the alignment document. It shows specifically where the two frameworks connect and where each picks up where the other leaves off.
