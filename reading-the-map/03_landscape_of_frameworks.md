# Chapter 3 — The Landscape of Frameworks

*Part 1 · What Is Enterprise Architecture*

Enterprise architecture has produced a lot of frameworks. This can feel overwhelming when you first encounter the landscape. TOGAF. Zachman. ArchiMate. FEAF. DODAF. MODAF. SABSA. BIZBOK. SAP EA. Wardley Mapping. ITIL. COBIT. Each with its own vocabulary, its own certification programme, its own community of practitioners.

There is a reason for this apparent complexity. Different frameworks emerged to address different problems in different contexts. A framework designed for US federal government IT management does not look the same as a framework designed for enterprise security architecture or for mapping business capabilities to value chains. The variety reflects the genuine diversity of the problems the profession has been asked to solve.

The purpose of this chapter is not to explain each framework in detail. Part 2 does that. The purpose here is to give you a map of the landscape so that when a framework name appears in a conversation, you have a sense of what territory it occupies, why it exists, and how it relates to the others.

## How to think about the frameworks

The simplest way to organise the landscape is by what problem each framework was primarily designed to solve.

Some frameworks are classification systems. They provide a way of organising descriptions of an enterprise so that every type of description has a home and nothing important is missed. Zachman is the primary example. It does not tell you how to develop architecture. It tells you how to classify what you produce.

Some frameworks are development methodologies. They provide a process for moving from where an organisation is to where it needs to be. TOGAF and its ADM is the primary example. It tells you how to approach the work, what phases to move through, what to produce at each stage.

Some frameworks are notation standards. They provide a visual language for drawing architecture in a way that other practitioners can read. ArchiMate is the primary example. It is not a methodology. It does not tell you how to develop architecture. It tells you how to draw what you have developed so that other people can read it.

Some frameworks are domain-specific. They apply the principles of enterprise architecture to a specific domain — security, business, government, defence. SABSA for security architecture. BIZBOK for business architecture. FEAF and DODAF for government and defence contexts.

Some frameworks are adjacent disciplines. They do not describe themselves as enterprise architecture but they address problems that EA also addresses, and the communities overlap significantly. ITIL for IT service management. COBIT for IT governance. Wardley Mapping for technology strategy.

Knowing which type of framework you are dealing with helps you understand what to expect from it. A classification system will not tell you how to do the work. A development methodology will not tell you how to draw the results. A notation standard will not tell you what to build. Each type of framework does one thing well and is not designed to do the others.

## The frameworks at a glance

The landscape sorts into a handful of categories. The table below places each framework by the kind of problem it was built to solve. It is a quick orientation, not the full picture — Appendix B carries the fuller version with origins, best uses, and known limits.

| Framework | Type | What it is for |
|---|---|---|
| Zachman | Classification | Organising the kinds of description an enterprise needs |
| TOGAF (and the ADM) | Development methodology | A repeatable process for developing architecture |
| ArchiMate | Notation | A visual language for drawing architecture others can read |
| SABSA | Domain — security | Tracing security controls to business risk |
| BIZBOK | Domain — business | Business architecture: capabilities and value streams |
| SAP EA | Domain — vendor | Architecture aligned to the SAP landscape |
| FEAF / DODAF / MODAF / NAF | Domain — government & defence | Architecture for public-sector and defence estates |
| Wardley Mapping | Adjacent — strategy | Reasoning about evolution and what to build versus buy |
| ITIL | Adjacent — service management | Running the services that architecture builds |
| COBIT | Adjacent — governance | Governing the enterprise's use of IT |

Read down the "type" column rather than the list of names: it is the category, not the brand, that tells you what a framework will and will not do for you.

## A note on the relationship between frameworks

The frameworks in this table are not competitors. They address different aspects of the same broader challenge. An organisation can use TOGAF as its development methodology, ArchiMate as its notation standard, SABSA for security architecture, COBIT for IT governance, and ITIL for service management. These are not contradictory choices. They are complementary instruments, each operating at a different layer of the enterprise.

In practice, most organisations do not formally adopt every framework. They use what serves their context and ignore the rest. A small technology company might use TOGAF's ADM selectively, produce architecture diagrams in Lucidchart with informal notation, and have no formal governance framework at all. A government defence agency might operate under DODAF mandates with SABSA for security, formal COBIT governance, and ITIL for service management. Both approaches can be correct for their context.

The important thing is not which frameworks you use but whether you understand what each one is for. A framework applied to the wrong problem produces overhead without benefit. A framework applied to the right problem in the right context produces clarity and coherence.

## What to do with this landscape

You do not need to study all of these frameworks to navigate the EA world. You need to know they exist, understand broadly what each one is for, and know where to look when you encounter one in practice.

Part 2 of this book gives you that working knowledge for each framework. Not a certification guide. Not an exhaustive reference. A plain English explanation of what each framework is, where it came from, what problem it solves, what it does well, and where you will encounter it.

The appendices at the back of the book contain the framework comparison table in a format you can return to as a quick reference, and the further reading list for when you want to go deeper into any specific framework.

For now, the landscape is visible. You know what exists. In Part 2, we walk through it.

---

## Translator Panel

> **People say:** "Which framework should we adopt?"
>
> **What that means:** Usually the wrong question. Ask first which *category* of problem you have — classification, method, notation, domain, strategy, or governance — because that is what tells you which framework will help and which will just add overhead.

> **Vendors say:** "Our framework covers the whole lifecycle."
>
> **What that means:** No single framework does. Each is strong in its category and silent outside it; "covers everything" usually means "thin everywhere." The landscape is a toolkit, not a contest, and the mature practice combines several.

---

## The Key Idea

The framework landscape looks crowded, but it organises cleanly once you sort by the kind of problem each framework was built to solve: classification (Zachman), method (TOGAF and the ADM), notation (ArchiMate), domain depth (SABSA, BIZBOK, SAP, the government and defence frameworks), strategy (Wardley), and governance and operations (COBIT, ITIL). The frameworks are not competitors; they are complementary instruments operating at different layers. The skill is not memorising them all but recognising which category a conversation is in, so you reach for the framework that fits the problem rather than the one you happen to know.

**Next:** Chapter 4 walks the whole landscape at a glance, before Part 2 takes each framework in turn.

---

## Further Reading

- **Appendix B — Framework Comparison Table** (this book): The full version of this chapter's at-a-glance table, with origins, best uses, and known limits for each framework.
- **Roger Sessions — A Comparison of the Top Four Enterprise-Architecture Methodologies** (objectwatch.com): An older but still-useful essay that treats the major frameworks as complementary lenses rather than rivals.
- **The Open Group — TOGAF Standard, on using TOGAF with other frameworks** (opengroup.org): Explicit guidance that TOGAF is designed to be combined with Zachman, ArchiMate, and domain frameworks — the point this chapter rests on.
