# Chapter 29: Building Blocks — ABB and SBB

*Part 3 · The Core Concepts*

---

There is a distinction at the centre of TOGAF that sounds like jargon and turns out to be one of the most practically useful ideas in the whole discipline. It is the difference between an **Architecture Building Block** (ABB) and a **Solution Building Block** (SBB) — between what an architecture *needs* and what *implements* it.

The distinction matters because getting it backwards is the single most common cause of bad procurement. An organisation that selects the solution before specifying the requirement has decided what it is buying before it has decided what it needs — and then spends the rest of the project bending its needs to fit the thing it bought.

This chapter explains the two kinds of building block, why ABBs are specified before SBBs are selected, and how Meridian's integration platform became its first formally defined ABB — a definition that changed how the platform was procured.

---

## What a Building Block Is

A **building block** is a reusable component of an architecture — a package of function that can be defined once and used in many places. The point of the building-block concept is reuse and clarity: instead of describing the same capability differently every time it appears, you define it once, name it, and refer to the name.

Building blocks come in two kinds, and the two kinds answer two different questions.

An **Architecture Building Block (ABB)** answers *what is needed?* It describes a required capability in solution-neutral terms — what function must be provided, what it must connect to, what constraints it must satisfy — without saying what product or technology will provide it. An ABB for integration says: "a capability that moves data between clinical systems reliably, with auditing, error handling, and monitoring, supporting these message types and these volumes." It does not say "Azure Integration Services" or "MuleSoft." It says what the architecture requires.

A **Solution Building Block (SBB)** answers *what implements it?* It is the specific product, technology, or component selected to fulfil an ABB. The SBB for the integration ABB might be a named integration platform from a named vendor, configured in a particular way. The SBB is concrete, purchasable, and deployable.

The relationship is deliberately one-directional in time: the ABB is specified first, and the SBB is selected to satisfy it. The architecture defines the requirement; the solution fulfils it.

---

## Why Order Matters

The reason ABBs come before SBBs is not methodological purity. It is that reversing the order corrupts the requirement.

When an organisation selects a solution first — chooses the product, signs the contract, commits to the technology — and only then works out what it needs, something predictable happens. The requirement quietly reshapes itself around the solution's capabilities. Features the product happens to have become "requirements." Needs the product cannot meet become "nice to haves" that get dropped. The organisation ends up with a system that does what the product does, which is not necessarily what the organisation needed. The tail wags the dog.

Specifying the ABB first prevents this. With the requirement defined in solution-neutral terms, the organisation can evaluate candidate solutions against a fixed standard — *does this product satisfy what we said we need?* — rather than discovering its needs by reading product brochures. The ABB is the specification the procurement is judged against, and its existence is what makes the procurement honest.

This is also why the ABB/SBB distinction is a governance instrument as much as a design one. An Architecture Review Board (Chapter 28) that asks "what is the ABB this procurement satisfies?" is asking the question that exposes solution-first thinking. A procurement that cannot point to a pre-existing ABB is, very often, a solution in search of a justification.

---

## The Common Failure

The failure mode is so common it is worth naming precisely: **technology selection ahead of requirement definition**.

It usually starts innocently. A vendor gives a compelling demonstration. A senior leader returns from a conference impressed by a product. A neighbouring organisation adopts something and recommends it. A "strategic partnership" makes a particular technology cheap. In each case, the solution arrives before the requirement, carrying its own momentum, and the requirement is then written to fit.

The cost is paid twice. First, the organisation may buy the wrong thing — a solution well-matched to the vendor's pitch and poorly matched to the actual need. Second, even if the solution is adequate, the absence of a defined ABB means there is no reusable specification: the next time a similar capability is needed, the work is done again from scratch, often selecting a different product, and the estate accumulates another inconsistency. Solution-first procurement does not just risk the wrong answer; it forfeits the reuse that was the whole point of building blocks.

---

## Meridian's Integration Platform as an ABB

*Meridian's integration problem — 34 point-to-point connections, eleven of them undocumented — is, by Wave 5 of the roadmap, due to be replaced by a managed integration platform. The instinct in the organisation, shaped by years of solution-first procurement, is to ask "which integration product should we buy?" The EA insists on a different first question: "what is the ABB?"*

*Defining the Architecture Building Block forces the organisation to articulate what integration actually requires at Meridian, independent of any product. The ABB specifies the capability in solution-neutral terms: it must support the clinical message standards in use (HL7 and FHIR), handle the documented data flows between the core systems, provide auditing sufficient for information-governance obligations, offer monitoring and alerting so that a failed clinical data flow is detected rather than discovered, support the message volumes the estate generates with headroom for growth, and degrade safely — a failure in integration must never silently lose a patient record. None of this names a product. All of it is a requirement the architecture can be held to.*

*The act of writing the ABB surfaces a requirement nobody had stated: safe degradation. The existing point-to-point integrations fail silently — when a connection breaks, data simply stops flowing, and the gap is noticed only when a clinician cannot find a record. The ABB makes "failure must be detected, not discovered" an explicit requirement, which immediately changes what counts as an acceptable solution. A cheap integration product that lacks robust monitoring, which might have won a solution-first procurement on price, fails the ABB on a requirement that turns out to be a patient-safety issue.*

*Only once the ABB is agreed does the SBB selection begin. Now the candidate products are evaluated against a fixed, Meridian-specific standard rather than against each other's marketing. Two products that looked similar in demonstrations turn out to differ sharply on the safe-degradation and monitoring requirements — a difference invisible in a feature comparison but decisive against the ABB. The platform Meridian selects is chosen because it satisfies the building block, and the ABB remains on file as the reusable specification: the next integration need is measured against the same standard, and the estate gains the consistency that fifteen years of solution-first procurement had denied it.*

---

## Reading the Distinction in the Field

For a reader, the ABB/SBB distinction is most useful as a diagnostic question to carry into procurement and design conversations.

When a specific product is being proposed, ask: *what is the requirement this satisfies, stated without reference to the product?* If the room can answer crisply, the ABB exists, explicitly or implicitly, and the procurement is grounded. If the room can only describe the product's features, the requirement is being reverse-engineered from the solution, and the conversation has the order backwards.

When a requirement is being defined, resist the pull to name a technology. The moment someone says "so we'll use [product]" while the requirement is still being written, the ABB is collapsing into an SBB prematurely, and the requirement will start bending to fit.

The distinction also clarifies a frequent confusion in architecture diagrams: an architecture-layer diagram should show ABBs (the capabilities required), while a solution-layer diagram shows SBBs (the products selected). A diagram that mixes them — "a layer of capabilities, one of which is suddenly a named vendor product" — is usually a sign that solution-first thinking has crept into the architecture.

---

## Translator Panel

> **TOGAF says:** "Architecture Building Blocks describe required capability and shape the specification of Solution Building Blocks. ABBs are defined in the Architecture phases; SBBs are defined and assembled in the Solutions phase."
>
> **What that means:** Decide what you need before you decide what you are buying. The ABB is the need, expressed so that any candidate solution can be measured against it; the SBB is the thing you actually procure and deploy. The method puts a phase boundary between them on purpose.

> **Vendors say:** "Our platform does everything you need — let us show you."
>
> **What that means:** This is solution-first procurement arriving as a demonstration. The defence is the ABB: if you have written down what you need independently of any product, you can watch the demonstration and check it against your requirement. If you have not, the demonstration becomes your requirement, and you will buy what the product does rather than what you need.

---

## The Key Idea

The distinction between Architecture Building Blocks and Solution Building Blocks is the difference between what an architecture needs and what implements it — and the order is not negotiable. The ABB, specified in solution-neutral terms, defines the requirement; the SBB is selected to satisfy it. Reversing the order corrupts the requirement, because needs silently reshape themselves around whatever solution arrived first, and the organisation ends up buying what a product does rather than what it actually needs. Specifying the ABB first keeps procurement honest, gives governance a question that exposes solution-first thinking, and preserves the reusable specification that makes building blocks worth the name. The single most useful habit the distinction teaches is to ask, of any proposed product, what requirement it satisfies stated without reference to the product itself.

**Next:** Chapter 30 turns to the building blocks' temporal cousin — the transition architecture — and the intermediate states an estate must pass through safely on its way from current to target.

---

## Further Reading

- **The Open Group — TOGAF Standard: Building Blocks** (opengroup.org): The canonical definition of ABBs and SBBs and their place across the ADM phases. The worked examples are dry but clarify the boundary the chapter describes.
- **Eric Evans — Domain-Driven Design** (Addison-Wesley, 2003): Evans's insistence on modelling the problem domain before choosing implementation technology is the software-design expression of the same ABB-before-SBB discipline.
- **Tom Graves — Real Enterprise Architecture** (Tetradian, 2008): Graves is unusually clear that architecture describes requirement-level abstractions and that confusing them with solutions is a recurring source of EA failure — a practitioner's complement to the TOGAF formalism.
