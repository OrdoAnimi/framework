# ArchiMate — The Visual Language

*Part 2 · The Frameworks Explained*

Architecture diagrams are only useful if people can read them. ArchiMate is the standard that makes that possible.

Most architecture diagrams are drawn in PowerPoint or Visio using whatever shapes the author felt like using that day. The result looks different from every architect who produces it. A diagram produced by one team cannot be read reliably by another. ArchiMate solves this by providing a standardised visual language — specific shapes, specific meanings, specific rules for how they connect. Two architects using ArchiMate produce diagrams that any third architect can read without being told what the shapes mean.

Meridian’s current architecture diagrams are spread across 47 PowerPoint files. Each one uses different shapes, different colours, and different conventions. The new EA cannot read one diagram and transfer what she learned to the next. Every diagram requires its own orientation. When she starts producing ArchiMate views the change is immediate. Anyone on the architecture team can read any diagram from the first line. The investment in learning the notation pays back on the first shared diagram.

## The three layers

ArchiMate is organised into three layers. Each layer corresponds to one of the BDAT domains covered in Part 3. The layers are always drawn in the same order: Business at the top, Application in the middle, Technology at the bottom. This is not arbitrary. Business depends on Application. Application depends on Technology. The visual hierarchy reflects the dependency.

## The three aspects

Within each layer, ArchiMate elements are classified by aspect. The aspect tells you what role an element plays.

## The relationships

ArchiMate elements connect through relationships. The relationships are as standardised as the elements. Each type of relationship means something specific.

## ArchiMate versus UML

ArchiMate and UML — the Unified Modelling Language — are both visual languages for describing systems. They are not competitors. They are designed for different purposes and the right choice depends on what you are trying to show.

## How to start reading ArchiMate

You do not need to memorise all of this before you can read an ArchiMate diagram. You need four things.

First, identify which layer you are looking at. Business, Application, or Technology. The colour convention in most tools makes this visible immediately. Second, identify the element types. Rounded rectangles are typically active structure elements. Plain rectangles are typically passive structure. Third, read the relationships as directional. An arrow from A to B means A connects to or depends on B in some way. Fourth, look for the label on the relationship. Serving, realisation, triggering, composition. The label tells you the type of dependency.

The first ArchiMate diagram Meridian’s new EA shares with the clinical director is the current state technology layer. Two VMware nodes. Active Directory. The MPLS network. The EA walks the clinical director through it in ten minutes using just four questions: what are these boxes, what do the arrows mean, what is missing from this picture, and what happens if the bottom layer fails. The clinical director leaves understanding for the first time why a VMware licensing problem is her problem. ArchiMate made the connection visible. The conversation did the rest.

---

## Translator Panel

> **Architects say:** "Here's the ArchiMate view."
>
> **What that means:** A layered picture linking business, application, and technology. Read one vertical thread at a time; you do not need to decode every element to follow the dependency that matters.

> **Stakeholders say:** "This diagram is too complicated."
>
> **What that means:** Usually the view is showing too much at once. Ask for the single trace from the capability you care about down to its infrastructure — that thread is readable even when the whole view is not.

---

## The Key Idea

ArchiMate is the profession's standard notation — a visual language that links the business, application, and technology layers so a diagram can be read the same way by everyone. Its distinctive value is the vertical trace: following a business need down through the application that delivers it to the infrastructure it runs on, in a single picture. A reader does not need to memorise every element type; they need to know the lines carry specific meanings and to follow one thread at a time. Dense views are not a sign of rigour — they are usually a sign the author tried to show everything at once, and the cure is to narrow to the one trace the decision needs.

**Next:** Chapter 9 turns to the government and defence frameworks — FEAF, DODAF, MODAF, and NAF — and why they exist.

---

## Further Reading

- **The Open Group — ArchiMate 3.2 Specification** (opengroup.org): The full notation. Skim the layer overview and the relationships summary so the line types stop being mysterious.
- **Gerben Wierda — Mastering ArchiMate** (R&A, 3rd ed. 2017): The best practitioner guide, and honest about which parts of the notation earn their keep.
- **Simon Brown — the C4 model** (c4model.com): On choosing a consistent level of abstraction — the single most common cause of unreadable diagrams, in ArchiMate or any other notation.
