# TOGAF — What It Is and Where It Came From

*Part 2 · The Frameworks Explained*

TOGAF is the most widely used enterprise architecture framework in the world. Most people in IT will encounter it at some point. Many will be asked about it in interviews. Some will be certified in it. Very few will use the full framework as written.

That last sentence is not a criticism. It is a fact the framework itself acknowledges. TOGAF is designed to be applied selectively, adapted to context, and used as a thinking structure rather than a procedure manual. Understanding what it is and where it came from makes that approach easier.

## Where TOGAF came from

By the early 1990s the United States Department of Defense was managing thousands of technology systems built across decades by different contractors using different standards. Many could not communicate with each other. Some duplicated functions that already existed elsewhere in the estate at significant ongoing cost. The department was spending money maintaining redundancy nobody had planned and fixing integration failures nobody had anticipated.

In 1993 the DoD published the Technical Architecture Framework for Information Management — TAFIM. It was their structured response to that problem. The Open Group, a technology industry consortium, took TAFIM as its starting point and in 1995 published the first version of TOGAF. Where Zachman had given the profession a classification system, TOGAF gave it a process. A structured method for developing enterprise architectures from an initial vision through to ongoing governance.

The framework has been through ten major versions since 1995. TOGAF 9, published in 2009, is the version most architects learned. TOGAF 10, published in 2022, restructured the content and explicitly acknowledged that different organisations apply the framework differently depending on their context.

At Meridian Health Partnership the IT director has a TOGAF 9 certificate framed on her office wall. She passed the exam seven years ago. She has never applied the full ADM cycle. What she uses — without always naming it — is the Phase A thinking. Establishing what the architecture programme is trying to achieve before anyone starts drawing diagrams. That selective application is legitimate. That is how TOGAF is meant to work.

## What TOGAF covers

TOGAF has several components. The most important for most practitioners is the Architecture Development Method — the ADM. The ADM is the process at the heart of TOGAF. It gets its own chapter next because it deserves that attention.

## Why TOGAF became the standard

Three things made TOGAF the framework most organisations reach for.

It was comprehensive without being prescriptive. TOGAF addressed the business, data, application, and technology dimensions of architecture. It gave architects a vocabulary that covered the whole enterprise, not just the technology layer. And it did not tell you which products to buy or which platforms to use. That neutrality made it acceptable across industries and contexts where proprietary frameworks would have met resistance.

It had a certification programme that created a global community. The Open Group introduced TOGAF certification in the early 2000s. By the mid-2010s it had become a standard line in EA job descriptions. Employers could recognise it. Practitioners could demonstrate it. The credential created the common vocabulary the profession needed.

This is the point where the honest assessment matters. TOGAF certification tests recall of the framework. It does not test the ability to apply it. A practitioner can pass the exam and be unable to write an Architecture Vision for a real organisation. A practitioner can have no certification and be doing excellent EA work every day. The certification signals familiarity with the language. It is not the same as capability.

## What TOGAF does well and where its limits are

TOGAF does several things exceptionally well. It provides a comprehensive vocabulary understood globally. It gives practitioners a structured way of thinking through complex problems. It provides the institutional legitimacy that organisations often need before they will invest in an architecture programme.

The full ADM cycle is heavyweight for many contexts. Applied ceremonially — all nine phases regardless of whether each is warranted — it produces more documentation than value. Applied selectively, as a thinking structure rather than a procedure manual, it is genuinely useful. The difference between the two is the most important practical lesson in this book.

TOGAF was also designed for large stable organisations with long planning horizons. The framework has adapted through its versions to address agile and cloud-native contexts, but practitioners in fast-moving environments often draw on other frameworks alongside TOGAF rather than relying on it alone.

## How TOGAF works with other frameworks

TOGAF is designed to work alongside other frameworks rather than replace them.

ArchiMate, covered in Chapter 8, is the visual notation standard most TOGAF practitioners use to draw their architecture diagrams. The two frameworks are published by the same organisation — The Open Group — and are explicitly designed to complement each other. COBIT, in Chapter 14, provides the IT governance layer that TOGAF's Phases G and H rely on in regulated environments. Wardley Mapping, covered later, provides the strategic positioning lens that TOGAF's Phase A often needs but does not fully supply.

In practice most organisations mix. They rarely call it that. They use TOGAF's ADM for structure, ArchiMate for drawing, COBIT for governance, and whatever else serves the problem. That is not a failure of commitment to a single framework. It is what good practice looks like.

At Meridian the EA does not choose between TOGAF and the other frameworks. She uses the ADM to structure her thinking about the VMware exit. She uses ArchiMate to draw the architecture diagrams. She uses the COBIT governance model when designing the Architecture Board. She references Wardley Mapping when she needs to explain to the board why VMware is a commodity problem not a strategic differentiator. Different tools for different aspects of the same job.

## A glimpse of what Phase A looks like at Meridian

The ADM gets its own chapter because it deserves that attention. But here is enough of a preview to make the next chapter land.

Phase A is called Architecture Vision. At Meridian it looks like this. The new EA sits down with the CIO and asks one question: what does success actually mean for this programme? Not the technical success. The business success. The answer becomes the Architecture Vision — a single page that says Meridian will enable safe connected care across 180 sites by exiting its VMware estate and unifying its clinical systems. Every decision made in the programme from that moment is tested against that statement. If a proposed decision moves Meridian toward the vision it proceeds. If it does not it requires a formal justification. That is Phase A. One page. One test. Every subsequent decision measured against it.

Chapter 7 shows how to build it.

---

## Translator Panel

> **People say:** "We're TOGAF certified" or "we're a TOGAF shop."
>
> **What that means:** It signals a shared vocabulary and that someone passed the exam — not that the ADM is run in full. Most TOGAF shops borrow the structure selectively, which is the healthy way to use it.

> **Sceptics say:** "TOGAF is too heavy for us."
>
> **What that means:** Often true if it is run ceremonially, and false if it is used as a thinking structure. The weight is optional; the sequence of questions the method asks is the part worth keeping.

---

## The Key Idea

TOGAF is the profession's dominant method — not a statement of what your architecture should be, but a disciplined way of developing it, anchored by the Architecture Development Method. Its strength is a shared vocabulary and a defensible sequence; its risk is ceremony, because a framework built for large government and defence enterprises turns into pure overhead when every phase is performed regardless of need. The way to get value from TOGAF is to treat it as a structure for thinking rather than a procedure to perform — borrowing its sequence where it improves a decision and leaving the rest. Used that way it remains the most useful common language the field has.

**Next:** Chapter 7 goes inside the method itself — the ADM, and how to use it without being used by it.

---

## Further Reading

- **The Open Group — TOGAF Standard, 10th Edition** (opengroup.org): The method itself. Read the overview and the ADM summaries; apply the rest selectively.
- **Gregor Hohpe — The Software Architect Elevator** (O'Reilly, 2020): The best antidote to ceremonial TOGAF — architecture as decisions and connection rather than process for its own sake.
- **Svyatoslav Kotusev — The Practice of Enterprise Architecture** (SK Publishing, 2018): Research-based and candid about the gap between TOGAF as written and TOGAF as practised.
