# Chapter 43: The Full Translation Table

*Part 5 · The Language Map*

---

This is a reference chapter, not a reading chapter. It is built for lookup — for the moment in a meeting when a term goes past and you want to know what it means in language you use, or the moment before a presentation when you want to find the plain-English version of something you would normally say in architecture vocabulary.

The table runs in three columns. **EA language** is the formal architecture term. **Delivery language** is how the same idea tends to be expressed by engineers, project managers, and delivery teams. **Business language** is how it lands — or should land — with executives, clinicians, and non-technical stakeholders. Translation runs in every direction: read across to convert a term you have into a term your audience shares.

The terms are grouped by theme. Within each group they are ordered roughly as they arise in practice. Bold terms appear in the glossary (Appendix A) with full definitions.

---

## Strategy and Direction

| EA language | Delivery language | Business language |
|---|---|---|
| **Architecture Vision** | the brief / what we're building and why | what this is for and what success looks like |
| **Target state** | where we're heading / the end goal | what the organisation will be able to do when we're done |
| **Baseline / current state** | what we've got now / as-is | where we are today, honestly |
| **Capability** | what the system needs to do | something the organisation must be able to do |
| **Strategic fit** | does it match the direction | does this help us do what we said matters |
| **Architecture principle** | the rule / the standard we follow | the commitments we've agreed to guide decisions |

---

## The Estate and Its Problems

| EA language | Delivery language | Business language |
|---|---|---|
| **Application portfolio** | the list of systems / our apps | everything we run, assessed for value and risk |
| **Architecture debt** | the mess / accumulated cruft | the growing cost and risk of past decisions nobody coordinated |
| **Technical debt** | shortcuts in the code / cleanup backlog | corners cut to ship faster that now slow us down |
| **Point-to-point integration** | direct connections / spaghetti | systems wired straight to each other, fragile at scale |
| **Integration complexity** | how tangled the connections are | how risky it is to change anything without breaking something |
| **Rationalisation** | cleaning up / consolidating systems | reducing duplication to cut cost and risk |
| **Master data** | the source of truth | the one trustworthy version of key information |
| **Data owner** | who's responsible for the data | the person accountable for whether the information is right |

---

## Decisions and Building

| EA language | Delivery language | Business language |
|---|---|---|
| **Architecture Building Block (ABB)** | the requirement / what we need | what we need it to do, before we pick a product |
| **Solution Building Block (SBB)** | the actual tool / the product | the specific thing we buy or build to meet the need |
| **6R disposition** | what we do with each app | keep, move, replace, rebuild, or retire each system |
| **Rehost / lift-and-shift** | move it as-is | relocate it without changing it |
| **Refactor / re-architect** | rebuild it properly | invest to rework it so it fits where we're going |
| **Decommission / retire** | switch it off | stop running and paying for it |
| **Transition state / transition architecture** | the in-between state / interim setup | a safe stopping point partway through the change |
| **Decision latency** | how long it takes us to decide | the cost of putting off a decision |

---

## Sequence and Governance

| EA language | Delivery language | Business language |
|---|---|---|
| **Architecture roadmap** | the plan / the phasing | the order we'll do things and why |
| **Wave / horizon** | phase / release train | a stage of the journey |
| **Dependency** | what's blocking what | what has to happen before something else can |
| **Gap analysis** | what's missing / the delta | the work between where we are and where we want to be |
| **Architecture Review Board (ARB)** | the review / the gate | the group that checks big decisions fit the whole |
| **Architecture governance** | sign-off / the process | making sure agreed decisions are actually followed |
| **Design authority** | who gets the final say | the body that can say yes or no and mean it |
| **Architecture Theatre** | box-ticking / rubber-stamping | the appearance of control without the substance |

---

## Domains and Layers

| EA language | Delivery language | Business language |
|---|---|---|
| **BDAT (Business, Data, Application, Technology)** | the four layers | the four views: what we do, what we know, what runs it, what it runs on |
| **Business architecture** | the process side | how the organisation is structured to do its work |
| **Data architecture** | the data side / the data model | how information is defined, owned, and trusted |
| **Application architecture** | the app side / the systems | what software we have and how it fits together |
| **Technology architecture** | the infra / the platform | the kit and platforms everything runs on |
| **Capability map** | the capability model | a picture of everything the organisation must be able to do |
| **Heat map** | the RAG status | a colour-coded view of what's healthy and what's at risk |

---

## Patterns and Notation

| EA language | Delivery language | Business language |
|---|---|---|
| **Hub-and-spoke** | central broker / integration platform | one central connector instead of many direct wires |
| **Event-driven** | pub/sub / messaging | systems that react to things happening rather than calling each other |
| **Microservices** | small services / decomposed | one big system broken into many small independent ones |
| **API-first** | proper interfaces / contracts | stable, documented ways for systems to talk |
| **ArchiMate** | the architecture diagram | the standard picture linking business, apps, and infrastructure |
| **Sequence diagram** | the flow / the call sequence | a step-by-step picture of what happens, in order |
| **Wardley map** | the evolution map | a picture of what's worth building versus buying |

---

## How to Use This Table

The table is a working instrument, and there are three ways to use it.

**To decode**, when a term goes past in a meeting that you do not recognise, find it in the EA column and read across to the language you think in. You will rarely need to interrupt; a quiet decode in your own head is usually enough to follow the thread.

**To translate before speaking**, when you are preparing to explain something to a particular audience, find the idea and read across to the column for that audience. Going to the board? Use the business column. Briefing the delivery team? Use the delivery column. The substance stays constant; only the register changes.

**To diagnose a miscommunication**, when a conversation is going badly and people seem to be talking past each other, the table often reveals that two people are using different columns for the same row — the architect in the EA column, the clinician hearing it as if it were the business column, neither realising they share a meaning. Naming the row they are both circling around is frequently what unblocks the conversation.

A caution: translation loses something. The business-language version of "architecture debt" is easier to grasp and slightly less precise than the EA term. That trade is usually worth it — a slightly-less-precise idea that the audience can act on beats a perfectly-precise one they cannot. But when precision genuinely matters for the decision, say so, and spend the time to bring the audience up to the precise term rather than deciding on the approximate one. The table is a bridge, not a replacement for the precise vocabulary where precision is load-bearing.

---

## The Key Idea

This chapter is a reference instrument: a three-column table mapping each architecture term across EA, delivery, and business language, grouped by theme and built for lookup rather than linear reading. It is used three ways — to decode a term you hear, to translate before you speak to a particular audience, and to diagnose a miscommunication in which two people are using different columns for the same meaning. Translation always loses a little precision, and that trade is usually worth it, because an idea the audience can act on beats a precise one they cannot — but where precision is load-bearing for a decision, the right move is to bring the audience up to the exact term rather than to decide on the approximation. The table is a bridge between registers, not a substitute for precision where precision matters.

**Next:** Chapter 44 narrows from the full table to the specific vocabulary that does the most consequential work — the words that turn a technical problem into a funded one.

---

## Further Reading

- **Appendix A — Full Glossary** (this book): The companion to this table — every bold term defined with its official source, plain-English translation, and a one-line note on when it matters.
- **Appendix B — Framework Comparison Table** (this book): Where the framework names in this table are placed in context, so a term like "ArchiMate" or "Wardley map" connects to the framework it comes from.
- **The Open Group — TOGAF Standard, definitions section** (opengroup.org): The authoritative source for the formal EA-column definitions, useful when a translation needs to be checked against the precise original meaning.
