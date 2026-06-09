# Chapter 21: How the Frameworks Work Together

*Part 3 · The Core Concepts*

---

By this point in the book you have met more than a dozen frameworks. Zachman for classification. TOGAF for method. ArchiMate for notation. SABSA for security. BIZBOK for business architecture. Wardley for evolution. ITIL for operations. COBIT for governance. If the experience has left you wondering which one you are supposed to choose, that is the correct reaction — and the honest answer is the one the certification courses are reluctant to give.

You do not choose one. You use several, for different purposes, and the skill is knowing which one answers which question.

This chapter is the join. It explains how the frameworks layer and connect rather than compete, why the question "which framework should we adopt?" is usually the wrong question, and what a working architect's actual toolkit looks like once the marketing language is stripped away.

---

## The Category Error

The single most common mistake in enterprise architecture is treating frameworks as if they were alternatives — as if Zachman and TOGAF were competing products and adopting one meant rejecting the other. They are not alternatives. They occupy different categories.

A **classification framework** tells you what kinds of description exist and how they relate. Zachman is the canonical example. It does not tell you how to produce anything. It tells you what a complete set of descriptions would contain and stops there.

A **method framework** tells you how to do the work. TOGAF's Architecture Development Method is the canonical example. It gives you a sequence of phases, a set of activities, and a governance cycle. It is largely silent on notation and classification.

A **notation framework** gives you a visual language. ArchiMate is the canonical example. It tells you how to draw a business process, an application component, and a technology node so that another architect can read your diagram without a key.

A **domain framework** goes deep on one part of the estate. SABSA for security. BIZBOK for business architecture. Each assumes you have a method and a notation and supplies the specialist content the general frameworks treat lightly.

A **strategy and evolution framework** helps you reason about movement and competition. Wardley mapping is the canonical example. It answers a question the others barely ask: which parts of our landscape are commoditising, and what should we therefore stop building ourselves?

An **operating and governance framework** governs what happens after architecture has done its work. ITIL runs the service. COBIT governs the enterprise's use of IT. They sit downstream of architecture and constrain it.

Asking whether you should use Zachman *or* TOGAF is like asking whether a builder should use a tape measure *or* a method statement. The categories do not overlap enough to compete.

---

## How the Layers Stack

The frameworks form a rough stack, and seeing the stack is more useful than memorising any single framework.

At the top sits **strategy** — where Wardley mapping and business architecture help you decide what matters and where to invest. Below that sits **method** — where TOGAF's ADM gives you a disciplined way to move from vision to roadmap. Cutting across the method sits **classification** — where Zachman reminds you which descriptions you still owe. Expressing the outputs sits **notation** — where ArchiMate turns the descriptions into diagrams a stakeholder can read. Specialising the content sit the **domain frameworks** — SABSA folding security into every phase, BIZBOK deepening the business layer. And underneath everything sits **governance and operations** — COBIT setting the control environment, ITIL running the result.

No organisation uses all of these formally. Most use two or three explicitly and several others implicitly without naming them. The mark of architectural literacy is recognising which framework is doing the work in a given conversation, even when nobody says its name.

---

## The Frameworks in Use at Meridian

*Meridian Health Partnership runs on a framework mix that nobody chose deliberately. Its enterprise architect spends a fortnight mapping what is actually in use across the estate, and the result is instructive precisely because it is so untidy.*

*TOGAF is the nominal standard. It is named in the IT strategy document, two members of staff hold Foundation certificates, and the document templates carry TOGAF artefact names. But the ADM has never been run as a cycle. The framework is referenced rather than used — its vocabulary borrowed for credibility, its discipline never applied.*

*ITIL, by contrast, is genuinely operational. The service desk runs ITIL incident and change management because the outsourced infrastructure contract mandated it. It is the most consistently practised framework in the organisation, and nobody in the architecture conversation thinks of it as architecture at all.*

*COBIT appears in fragments. The annual IT audit uses COBIT control references, so the language exists in the governance committee's papers, but no continuous control environment has been built around it. It is invoked once a year and then filed.*

*SABSA is absent. There is an information governance function, mandated by NHS data protection obligations, but no security architecture discipline connecting security decisions to business risk. Security is treated as a compliance checklist rather than an architecture domain — which is exactly the gap SABSA exists to close.*

*The EA's conclusion is not that Meridian should adopt a framework. It is that Meridian is already using four, badly, without coordination — and that the immediate opportunity is not adoption but alignment.*

---

## The Honest Answer to "Which Framework?"

When a leadership team asks an architect which framework the organisation should adopt, they are usually asking a different question underneath: *how do we get our technology decisions under control?* The framework question is a proxy for an anxiety about disorder.

The honest answer has three parts.

First, you almost certainly need a **method**, and TOGAF's ADM — used selectively, as a thinking structure rather than a procedure to be performed in full — is the most widely understood option. Choosing it buys you a shared vocabulary and a defensible sequence. It does not buy you outcomes.

Second, you need a **notation** if more than a handful of people are going to read each other's diagrams, and ArchiMate is the lingua franca. For a small team, a consistent set of conventions matters more than the specific standard.

Third, you need to be honest about which **domain and governance frameworks** are already operating whether you named them or not. ITIL is probably running your service desk. Your auditors are probably using COBIT references. Your regulator is probably imposing security obligations that a discipline like SABSA would organise. Naming these makes them improvable.

What you do not need is to adopt a framework ceremonially — to run every ADM phase regardless of whether it is warranted, to model every cell of the Zachman grid, to produce ArchiMate views nobody reads. Ceremonial adoption is the failure mode that gives enterprise architecture its reputation for producing process instead of value.

---

## Choosing Your Path Through the Frameworks

For a reader trying to navigate rather than practise, the practical guidance is simpler than the framework literature suggests.

If you want to **understand a decision**, ask which category of question is being answered. Is this a strategy question (reach for Wardley and business architecture), a method question (reach for the ADM), a classification question (reach for Zachman), or a governance question (reach for COBIT)? Naming the category tells you which framework's vocabulary will clarify the conversation.

If you want to **contribute to a decision**, you rarely need framework depth. You need to recognise the shape of the problem and ask the question the relevant framework would prompt. You do not need to have read SABSA to ask "what is the business risk this security control is managing, and who owns it?" That is a SABSA question asked in plain English, and it is often more useful than a SABSA diagram.

If you want to **go deeper later**, the frameworks are a reading list, not a curriculum. Start with the one closest to the problem in front of you. The others will make more sense once you have used one in anger.

---

## Translator Panel

> **The framework vendors say:** "Adopt our framework to bring rigour and alignment to your enterprise architecture practice."
>
> **What that means:** Each framework solves a real problem within its category. None solves the whole problem, and adopting one does not, by itself, change anything. Rigour comes from using a framework to make better decisions, not from owning the certificate.

> **Architects say:** "We're TOGAF-aligned but we don't run the full ADM — we use it where it adds value."
>
> **What that means:** This is the healthy position, stated honestly. It means the organisation borrows the method's structure and vocabulary without performing every phase as ritual. The phrase "where it adds value" is doing the important work, and it should always be followed up: *value to whom, and how would you know?*

---

## The Key Idea

The frameworks are not competitors. They are a toolkit, and like any toolkit, the skill is selection rather than ownership. Classification, method, notation, domain depth, strategy, and governance are different categories of tool, and a mature practice uses several at once for different purposes. The question "which framework should we adopt?" almost always dissolves on inspection into a set of more specific questions, each of which points to a different tool. Recognising which framework is doing the work in any given conversation — even when nobody names it — is the single most useful piece of framework literacy this book can give you.

**Next:** Chapter 22 turns to the most important and most frequently skipped piece of architectural work — the Architecture Vision. Before you can stack frameworks or run a method, someone has to say what the work is actually for.

---

## Further Reading

- **The Open Group — TOGAF Standard, 10th Edition** (opengroup.org): The introduction and the section on using TOGAF with other frameworks are the most relevant here. The Open Group is explicit that TOGAF is designed to be combined with Zachman, ArchiMate, and domain frameworks — a point often lost in practice.
- **Roger Sessions — A Comparison of the Top Four Enterprise-Architecture Methodologies** (objectwatch.com): An older but still-cited essay that treats Zachman, TOGAF, FEAF, and Gartner as complementary lenses rather than rivals. The framing has aged well even as the specifics have moved on.
- **Simon Brown — Software Architecture for Developers** (Leanpub): Not an EA text, but its argument that notation should serve communication rather than compliance applies directly to the framework-selection question.
