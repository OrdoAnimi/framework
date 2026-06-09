# Chapter 11: The Business Layer — What BIZBOK Actually Tells You

## Opening

You have spent ten chapters learning how to read a map. Now it is time to look at the territory itself — the business.

Enterprise architecture frameworks spend a lot of energy on the technology layers: applications, data, infrastructure. They are concrete, observable, and easier to draw. But every one of those layers exists to serve the business. If you do not understand what the business is trying to do — not the org chart, not the mission statement, but the actual operating logic — you will build technically elegant solutions to the wrong problems.

This is where **business architecture** comes in, and where the **Business Architecture Guild's** reference guide, the **BIZBOK**, becomes useful.

You do not need to read the BIZBOK cover to cover. Most of it is definitional scaffolding. What you need is the mental model underneath it — the idea that a business has describable structure, and that structure can be mapped, compared, and used to make decisions. This chapter gives you that mental model in plain language, then shows you how it applies at Meridian.

---

## What Business Architecture Actually Is

Business architecture is the practice of describing how an organisation works — not how it is organised on paper, but how value actually flows through it. It answers four questions:

- What does this organisation do? (**capabilities**)
- Why does it do those things? (**strategy and motivation**)
- Who does what? (**organisation and roles**)
- How does value move? (**value streams**)

The BIZBOK provides a vocabulary and a set of cross-mapping techniques for answering all four questions consistently, so that different teams — IT, finance, operations, HR — can have conversations without talking past each other.

> **Pull quote:** "Business architecture is not about org charts. It is about making the operating logic of an organisation visible enough to reason about."

The most important shift BIZBOK asks you to make is from *function* to *capability*. Functions describe what a department does. Capabilities describe what the organisation *can do*, regardless of which department does it. That is a quiet but radical difference.

---

## Capabilities: The Core Concept

A **business capability** is a particular ability that an organisation has or needs in order to deliver value. It is defined by *what* is done, not *who* does it or *how* it is currently done.

*At Meridian, "Patient Scheduling" is a capability. It exists whether the scheduling is done by a receptionist in a GP surgery, an automated text message system, or a contact centre agent. The capability is the thing — the ability to match a patient to an available appointment slot. The technology and the team are implementation details.*

Capabilities have three characteristics that make them useful:

**First, they are stable.** Technology changes. Teams reorganise. Processes get redesigned. But the underlying capability — schedule a patient, dispense a medication, invoice a commissioner — stays recognisable for years. This makes capability maps a durable anchor for architecture conversations.

**Second, they are assessable.** Once you have named a capability, you can ask: how well can we do this today? You can rate it on a simple scale — inadequate, adequate, good, excellent — and plot the result on a **heat map**. That heat map immediately shows you where the pain is, without anybody having to write a business case.

**Third, they are technology-agnostic.** A capability sits above the application layer. "Patient Scheduling" does not care whether it is implemented in System A or System B. This is exactly what you need when you are trying to rationalise a dual-EPR environment, because it lets you ask: which capabilities are served by which system, and where is the overlap?

---

## The Capability Map

A **capability map** is a hierarchical list of business capabilities, usually presented as a grid or tree. Level 1 contains the broadest categories — Clinical Care, Patient Administration, Finance, Workforce Management, and so on. Level 2 breaks those into recognisable sub-capabilities. Level 3 gets specific enough to be useful for application mapping.

*Imagine Meridian's capability map laid out as a heat map. Most of Level 1 is either green (adequate) or amber (under strain). But two blocks glow red: Patient Record Management and Clinical Decision Support. Both are served by the dual-EPR estate. Both have been under investment for years because nobody could agree which system to fix first. The heat map does not solve that problem, but it makes the problem visible in a language that the executive team can act on.*

Building a capability map for the first time is not a long research project. A decent first pass takes two or three workshops with people who actually run operations. You are not trying to be exhaustive — you are trying to be *good enough to be useful*. The map will improve with use.

---

## Value Streams

If capabilities describe what an organisation *can* do, **value streams** describe what it *actually does* to deliver something of value to a stakeholder. A value stream is a sequence of stages that transforms inputs into outcomes a stakeholder cares about.

The BIZBOK distinguishes between value streams that serve *external* stakeholders (patients, commissioners, regulators) and those that serve *internal* stakeholders (staff, teams, governance bodies). Both matter.

*Meridian has a value stream called "From Referral to First Appointment." It begins when a GP submits a referral and ends when the patient sits down in the outpatient clinic. In between: triage, scheduling, letter generation, reminder, check-in. Each stage consumes capabilities. Some of those capabilities are performed by people, some by systems, some by a combination. The value stream makes the whole sequence visible as a single object you can reason about, rather than a collection of departmental hand-offs that nobody owns end-to-end.*

Value streams and capabilities are connected by a cross-mapping. Each stage in a value stream *uses* one or more capabilities. Laying that mapping out exposes two things: capabilities that appear in many value streams (high leverage, high risk if they fail), and value stream stages where no capability is clearly mapped (governance gaps, grey areas where things fall through).

---

## Motivation: Strategy Made Visible

BIZBOK includes a motivation model — a way of connecting an organisation's goals, strategies, directives, and constraints into a coherent picture. At its simplest, it is a way of answering: *why does this organisation do what it does, and what constraints does it operate under?*

**Ends** are what the organisation is trying to achieve: visions, goals, objectives. **Means** are how it intends to achieve them: strategies, tactics, directives. **Influences** are the forces acting on the organisation from outside: regulations, market conditions, technology shifts, NHS policy.

*Meridian's strategic plan says it wants to "deliver integrated care across 14,000 staff and 180 sites." That is an End. One of its Means is "rationalise the application estate to reduce fragmentation." One of its Influences is the NHS Cloud-first policy — which Meridian has not yet acted on, partly because of the VMware crisis absorbing senior attention. The motivation model does not resolve these tensions, but it names them clearly enough that a conversation can happen.*

The practical value of the motivation model is alignment checking. When a team proposes a new initiative, you can ask: which goal does this serve? Which strategy does it advance? If nobody can answer those questions cleanly, the initiative probably should not be prioritised.

---

## Organisation and Roles

The fourth pillar of BIZBOK is the organisation view — mapping which parts of the organisation are responsible for which capabilities and which value streams. This is where business architecture connects to governance.

The key tool here is the **RACI-style capability ownership matrix**: for each capability, who is *accountable* (there is exactly one answer), who *performs* it (there may be many), and who is *informed* of its performance?

*At Meridian, capability ownership is patchy. Patient Scheduling is performed by six different teams across the 180 sites, with different systems and different processes. Nobody is accountable for the capability as a whole. When the scheduling system goes down, there is no single person who owns the problem — there are six teams pointing at each other. A capability ownership matrix would make that gap explicit in a way that a list of IT tickets does not.*

Mapping organisation to capabilities also reveals something useful about outsourcing and shared services decisions. If a capability is non-differentiating — Payroll, say, or Facilities Management — and nobody in the organisation owns it clearly, that is a signal it could be standardised or bought in. If a capability is genuinely differentiating — like Meridian's community nursing coordination model, which is the thing that makes it distinctive as an integrated care provider — you want to protect it and invest in it.

---

## How BIZBOK Connects to the Rest of the Framework

BIZBOK is sometimes criticised for existing in isolation — a business architecture practice that does not connect to application or technology architecture. That criticism is fair if you use BIZBOK as a standalone discipline. It is unfair if you use it as the business layer of a broader framework.

In the TOGAF terms you met in earlier chapters, the Business Architecture is the first architecture domain — it sits above Application, Data, and Technology. In practice, the connection is made through three cross-mappings:

- **Capabilities to applications**: which applications support which capabilities? (This is how you rationalise your application portfolio.)
- **Capabilities to data**: which data objects are consumed and produced in each capability? (This is how you identify your critical data flows.)
- **Capabilities to technology**: which infrastructure underlies each capability? (This is how you assess the impact of the VMware crisis.)

*At Meridian, the capability-to-application mapping immediately shows something uncomfortable: the Patient Record Management capability is served by two EPR systems, a legacy clinical portal, a scanning and document management platform, and four departmental databases. None of them talk to each other reliably. The capability map did not cause that problem. But it made the problem visible in a single diagram instead of buried across seventeen support contracts.*

---

## A Practical Starting Point

You do not need to implement the full BIZBOK to get value from business architecture. Here is what you can do this week:

Start with a Level 1 capability map. List the ten to fifteen broadest things your organisation does. Do not agonise over the names — you will refine them. Run it past two or three operational colleagues and ask: does this feel right? What is missing?

Then colour-code it. For each capability, mark whether your current IT provision is inadequate, adequate, or genuinely good. Be honest. The heat map you get back will tell you more about where to focus than six months of application portfolio analysis.

Then pick one value stream — ideally one that crosses departmental boundaries and is currently painful — and walk it through from stakeholder need to delivered outcome. Name the stages. Ask which capabilities each stage uses. Ask who owns each capability. The gaps and ambiguities that appear are your real architecture agenda.

---

## Translator Panel

> **BIZBOK says:** "A business capability defines what a business does or can do, and can be supported by people, processes, information, and tools."
>
> **What that means:** A capability is the stable label for an ability your organisation has, independent of how it is currently delivered. It is the thing you map, assess, and cross-reference to everything else.

> **BIZBOK says:** "A value stream is an end-to-end collection of value-adding activities that create an overall result for a customer, stakeholder, or end user."
>
> **What that means:** It is the sequence of things that actually happen when someone gets something from your organisation. It reveals hand-offs, gaps, and ownership problems that org charts hide.

---

## The Key Idea

The business layer is not soft architecture. It is the part that tells you *why* the technology exists. A capability map gives you a stable, technology-agnostic vocabulary for talking about what the organisation does. A value stream shows you how value actually flows. Together they give you the two questions that unlock every technology decision: which capabilities does this serve, and which value stream does this improve?

**Next:** Chapter 12 moves into the Application Architecture domain — how to map your application portfolio against the capabilities you have just defined, and what to do when the map looks like Meridian's.

---

## Further Reading

- **Business Architecture Guild — BIZBOK Guide** (bizbok.org): The definitive reference. Dense but thorough. The sections on capability mapping and value streams are the most immediately practical.
- **Jeanne Ross, Cynthia Beath, Martin Mocker — Designed for Digital** (MIT Press, 2019): Not a BIZBOK book, but the best practical account of why capability thinking matters for digital transformation.
- **Roger Burlton — Business Process Management: Profiting from Process** (Sams, 2001): Older but still the clearest treatment of value streams in plain language.
- **NHS England — Operating Framework and Service Specifications**: The regulatory context that shapes Meridian's motivation model — what the NHS mandates, what it incentivises, and what it merely suggests.
