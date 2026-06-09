# Chapter 39: How to Read a Zachman Cell

*Part 4 · Reading the Diagrams*

---

The Zachman Framework, introduced in Chapter 5, is not a diagram in the way the previous four chapters' artefacts are. It is a **classification grid** — six rows and six columns, thirty-six cells, each cell representing a distinct kind of description of the same enterprise. You do not read a Zachman grid the way you read a sequence diagram. You read it as a map of perspectives, and its great lesson is that the same system genuinely looks different — and *should* look different — depending on which cell you view it through.

This chapter teaches that reading. It is the most abstract chapter in Part 4, and also, for many readers, the most clarifying, because it explains a confusion that pervades architecture conversations: people looking at the same system, describing it accurately, and disagreeing completely — because they are standing in different cells.

---

## The Grid: Rows and Columns

Zachman's grid has two axes, and reading it begins with reading the axes.

The **columns** are the interrogatives — the six fundamental questions you can ask about anything: **What** (data), **How** (function), **Where** (network/location), **Who** (people), **When** (timing), and **Why** (motivation). These are exhaustive: any aspect of any system answers one of these six questions. The columns are the *aspects* of the enterprise.

The **rows** are the perspectives — the points of view of different stakeholders, from the most abstract to the most concrete. From the top: the **Executive** perspective (scope, the boardroom view), the **Business Management** perspective (the business model), the **Architect** perspective (the system logic), the **Engineer** perspective (the technology model), the **Technician** perspective (the detailed build), and the **Enterprise** itself (the running reality). The rows are the *audiences*, each needing a description pitched at its own level.

A **cell** is the intersection — a specific aspect seen from a specific perspective. The "What, from the Architect's perspective" cell holds the logical data model. The "What, from the Executive's perspective" cell holds a list of the important things the business cares about. Same column (What/data), different rows (different audiences), genuinely different artefacts.

---

## Why the Same System Looks Different

The framework's central insight, and the thing reading it teaches, is that descriptions in different cells are not better or worse versions of each other. They are *different and equally necessary* descriptions of the same thing.

Consider patient identity at Meridian, read across one column.

In the **What** column, from the **Executive** row, patient identity is "knowing who our patients are" — a one-line strategic concern about the organisation's ability to recognise the people it serves. From the **Business Management** row, the same What becomes a definition: what constitutes a patient, what attributes identify them, what the business rules are for matching. From the **Architect** row, it becomes a logical data model — entities, attributes, relationships, the master-data design. From the **Engineer** row, it becomes a physical database schema. From the **Technician** row, it becomes the actual table definitions in a specific database. From the **Enterprise** row, it is the live patient data in the running systems.

Every one of these is "patient identity." Every one is correct. None substitutes for another. The executive's one-liner is not a vague version of the database schema; it is the right description *for the executive's purpose*, and the schema would be useless to the executive just as the one-liner would be useless to the engineer building the table.

This is why architecture conversations so often involve people talking past each other while all being right. The clinical director describes patient identity from the Executive/Business row; the engineer describes it from the Engineer/Technician row; they use the same words and mean descriptions three rows apart. Reading the situation through Zachman tells you they are not disagreeing — they are standing in different cells, and the fix is not to argue but to recognise which cell each is in and translate between them.

---

## Reading a Cell Correctly

To read any architectural description well, the Zachman discipline is to locate it in the grid first — to ask *which cell is this?* before evaluating it.

Locating the cell means asking two questions. *Which interrogative does this answer?* — is this about data (What), function (How), location (Where), people (Who), timing (When), or motivation (Why)? And *which perspective is this pitched at?* — is this the executive's scope, the architect's logic, the engineer's technology, or the technician's detail?

Once you have located the cell, two common errors become avoidable. The first is judging a description by the standards of the wrong cell — criticising the executive's one-line scope statement for lacking the detail of an engineer's schema, when detail is precisely not its job. The second is mistaking a description in one cell for the whole picture — treating the architect's logical model as if it were the running reality (the Enterprise row), and being surprised when the live system behaves differently from the model.

---

## Meridian's Patient Record Through Six Perspectives

*Meridian's EA uses the Zachman grid not to produce thirty-six artefacts — which would be the ceremonial misuse of the framework — but as a diagnostic lens to understand why the patient-record problem had resisted resolution. Reading the patient record through six perspectives explains the impasse.*

*The **clinical director** sees the patient record from the Business row: a complete, trustworthy account of a patient's care, available wherever the patient is seen. Her concern is completeness and availability. From her cell, the problem is "I can't trust that I'm seeing everything about this patient."*

*The **enterprise architect** sees it from the Architect row: a logical model in which patient identity is the master entity that every other record references. From her cell, the problem is "there is no authoritative identity entity, so the logical model is incoherent."*

*The **database engineer** sees it from the Engineer row: two physical schemas, in two EPRs, with overlapping but non-identical patient tables and no reliable key to match them. From his cell, the problem is "I can't join these two databases reliably because there's no shared identifier."*

*The **information governance lead** sees it from the Why column: the regulatory motivation — the legal obligation to maintain accurate records and control access. From her cell, the problem is "we may be in breach because we cannot guarantee record accuracy across systems."*

*Each is describing the same problem — the absent patient-identity master — from a different cell, and each description is correct and incomplete. The reason the problem had resisted resolution was that it had only ever been discussed within single cells: the clinicians raised it as a trust problem, IT heard it as a database problem, governance heard it as a compliance problem, and no one had assembled the cells into the single architectural finding underneath them. The EA's contribution was not a new analysis; it was reading the existing complaints as different cells describing one root cause, which is exactly what the Zachman grid is for. Once the cells were assembled, the identity-master decision (Wave 3 of the roadmap) became obviously the thing that resolved all four perspectives at once.*

---

## Translator Panel

> **Zachman says:** "The Framework is a schema for classifying the artefacts that constitute the architecture of an enterprise — a two-dimensional classification of descriptive representations."
>
> **What that means:** It is a filing system for the different kinds of description an enterprise needs, organised by what they describe (the six questions) and who they are for (the six perspectives). It does not tell you how to build anything; it tells you what kinds of description exist and stops you from confusing one for another.

> **People in a meeting say (without realising it):** the same words, from different rows.
>
> **What that means:** When a clinician, an architect, and an engineer describe "the patient record" and seem to disagree, they are usually in different cells — same column, different rows — describing the same thing at different levels. Recognising this turns an argument into a translation exercise: identify each person's cell and connect the descriptions, rather than treating them as competing claims.

---

## The Key Idea

The Zachman Framework is a classification grid, not a diagram — six interrogatives (What, How, Where, Who, When, Why) crossed with six perspectives (from Executive scope down to the running Enterprise), making thirty-six cells, each a distinct and necessary kind of description. Reading it teaches that the same system looks genuinely different from different cells, and that descriptions in different cells are not better or worse versions of each other but equally valid views for different purposes. The practical payoff is diagnostic: when people use the same words and seem to disagree, they are usually standing in different cells, and recognising this converts an argument into a translation. The grid's value is rarely in producing all thirty-six artefacts — that is its ceremonial misuse — but in locating any description in the grid before judging it, and in assembling single-cell complaints into the whole-picture finding underneath them.

**Next:** Chapter 40 turns to the Wardley map — the strategy diagram that adds an axis the others lack, evolution, and shows not just what exists but what is moving and in which direction.

---

## Further Reading

- **John Zachman — "The Zachman Framework for Enterprise Architecture"** (zachman.com): The framework from its author, including the full grid and the rationale for the rows and columns. The official source, and clearer than most secondary summaries.
- **Roger Sessions — comparison writing on Zachman as a taxonomy** (objectwatch.com): Helpful for understanding Zachman specifically as a classification scheme rather than a method, which is the distinction that makes it readable.
- **Len Silverston & Paul Agnew — The Data Model Resource Book**: For the What column specifically — how the same data concept is expressed differently from the conceptual through logical to physical perspectives, which is the single-column trace this chapter uses for patient identity.
