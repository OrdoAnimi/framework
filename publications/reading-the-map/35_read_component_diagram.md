# Chapter 35: How to Read a Component Diagram

*Part 4 · Reading the Diagrams*

---

A component diagram is the most common technical diagram a non-architect will encounter, because it is the one engineers reach for to explain how a set of systems fits together. It shows the **components** — the systems or significant parts of systems — the **interfaces** through which they connect, and the **dependencies** between them. Read well, it tells you not just how something is built but where it is fragile and what would break if a piece were removed.

This chapter teaches that reading, using Meridian's clinical-systems estate. The most important skill it develops is counter-intuitive: learning to read what is *missing* from a component diagram, because the gaps are frequently where the real risk lives.

---

## The Anatomy: Boxes, Lines, and Arrows

A component diagram has three basic elements, and reading it begins with reading them precisely.

**Components** are the boxes — each one a system, service, or significant module. The first reading question is always *what is the boundary of this box?* A box labelled "EPR" might be a single system or a shorthand for a dozen integrated modules; the diagram's level of abstraction determines what a box hides.

**Interfaces** are the points where components connect — often drawn as small circles, sockets, or labelled connection points. An interface is a contract: it says "this is how you talk to me." Reading interfaces tells you the seams of the system, the places where one component's responsibility ends and another's begins.

**Dependencies** are the lines and arrows between components, and arrow *direction* carries meaning that is easy to misread. An arrow from A to B usually means "A depends on B" or "A calls B" — A needs B to function. This matters because dependency direction tells you the blast radius of a failure: if A depends on B and B fails, A is affected; the reverse is not necessarily true. Reading arrow direction backwards inverts your understanding of what breaks what.

A simple way to fix the convention in mind:

```
  [ Clinical Portal ] ──────▶ [ EPR ]
        depends on / calls
```

The portal points to the EPR because the portal needs the EPR. If the EPR is down, the portal is degraded. The arrow is a statement about who suffers when the target fails.

---

## Reading Dependencies for Fragility

The pattern of dependencies, read across the whole diagram, reveals where the estate is fragile — and fragility shows up as particular shapes.

A component with **many incoming arrows** is a shared dependency — lots of things rely on it. Its failure has a wide blast radius. These are the components whose resilience matters most, and a diagram that shows a heavily-depended-on component with no redundancy is showing you a single point of failure.

A component with **many outgoing arrows** depends on many things — it is fragile in a different way, because it fails if any of its many dependencies fails. Its reliability is the product of all of theirs.

A **cycle** — A depends on B depends on C depends on A — is almost always a warning. Circular dependencies make systems hard to change, hard to start up cleanly, and hard to reason about, because there is no clean order in which the components can be brought up or modified. Spotting a cycle in a component diagram is spotting a structural problem the authors may not have intended.

---

## Reading Meridian's Clinical Estate

*Meridian's current-state component diagram for the clinical systems estate is, like most real ones, busier than anyone would like. Reading it for fragility surfaces three findings the leadership team had not articulated.*

*The first finding is a heavily-depended-on component with no redundancy. The legacy clinical portal — the end-of-life system from Chapter 20 — has nine incoming dependency arrows. Nine other components rely on it. Reading the diagram, this is immediately the most dangerous box on the page: its blast radius is enormous and it is running on an unsupported platform. The diagram makes visible, in arrow-counting terms, exactly why decommissioning the portal (a portfolio "migrate" decision) is not a simple swap — nine things depend on it, and each dependency must be remediated before the portal can go.*

*The second finding is the dual EPR drawn honestly. Both EPRs appear as components, and crucially the diagram shows that several downstream components depend on one EPR while others depend on the other — the dependency pattern *is* the fragmentation. A reader who only heard "we have two EPRs" learns from the diagram something sharper: the estate has organised itself around the split, with different systems wired to different EPRs, so consolidation means re-pointing every one of those dependencies, not just retiring a box.*

*The third finding is a dependency cycle, and it is the kind of thing only a diagram reveals. The portal depends on a departmental system for one data feed, and that departmental system depends back on the portal for patient context — a two-component cycle. Nobody designed this; it emerged from two separately-rational integrations. The cycle explains a long-standing operational mystery: why bringing the estate back up after maintenance is fragile and order-dependent. The diagram shows the cause that years of incident reports had only described.*

---

## Reading What Is Missing

Here is the skill that separates a literate reader from a passive one: reading what the diagram does *not* show.

Every component diagram is drawn at a level of abstraction, and every level hides things. The discipline is to ask, of any diagram, *what has been left out, and is the omission innocent or significant?*

Some omissions are innocent abstraction — a box labelled "EPR" reasonably hides its internal modules because they are not relevant to the conversation. Some omissions are significant and sometimes self-serving. A component diagram drawn to justify a migration may quietly omit the awkward dependency that makes the migration harder. A diagram of a proposed solution may omit the error-handling, the monitoring, the failure paths — showing the happy path and hiding the parts that are not yet designed.

The reader's questions are: *Where does the data come from before it enters this diagram, and where does it go after it leaves?* (Edges of the diagram often hide critical external dependencies.) *What happens when this connection fails — is there an error path, and is it drawn?* (Diagrams that show only success are hiding their hardest parts.) *Is anything here that everyone depends on but nobody owns?* (Shared components with no clear owner are organisational risks the diagram makes visible.)

*At Meridian, the most significant omission is the community nursing caseload tool — the spreadsheet from Chapter 20. It does not appear on the official component diagram at all, because it is "just a spreadsheet" and beneath the diagram's notice. But clinicians depend on it daily, and it depends, informally, on data exported from the EPR. Its absence from the diagram is exactly why it was nearly migrated into chaos in Chapter 22: a critical dependency that the official picture did not show. Reading the diagram for what is missing is what would have caught it.*

---

## Translator Panel

> **Engineers say:** "The portal has nine downstream dependencies, so decommissioning it is non-trivial."
>
> **What that means:** Nine other systems rely on the portal, so it cannot simply be switched off — each of the nine connections has to be understood and remediated first. The diagram makes the nine visible; the arrow count is the measure of how hard the change will be.

> **Architects say:** "What's not on this diagram? Where are the failure paths and the external dependencies?"
>
> **What that means:** They are reading the omissions. A component diagram that shows only the components and only the happy path is hiding the parts most likely to cause trouble — the error handling, the things at the edges, the critical-but-unofficial dependencies. The question forces those into view.

---

## The Key Idea

A component diagram shows components, interfaces, and dependencies, and reading it well starts with reading the elements precisely — especially arrow direction, which states who suffers when the target fails. The pattern of dependencies reveals fragility: heavily-depended-on components are single points of failure, heavily-depending components inherit all their dependencies' unreliability, and cycles are structural warnings. But the most valuable reading skill is for what the diagram omits — the innocent abstractions versus the significant or self-serving gaps, the failure paths that are not drawn, the critical-but-unofficial dependencies that never made the official picture. A diagram that shows only success and only the components someone chose to include is hiding exactly the places where the real risk lives.

**Next:** Chapter 36 turns to the sequence diagram — the artefact that shows not what connects to what, but what happens in what order over time, and where failure appears in the flow.

---

## Further Reading

- **Simon Brown — The C4 Model for Visualising Software Architecture** (c4model.com): The clearest modern guidance on component diagrams and, crucially, on choosing a consistent level of abstraction — the single most common cause of unreadable component diagrams.
- **UML 2.5 specification — Component Diagrams** (omg.org): The formal notation, if you need to read strictly-drawn diagrams. Most real-world component diagrams are informal, but knowing the formal conventions helps you read both.
- **Michael Nygard — Release It!** (Pragmatic Bookshelf, 2nd ed. 2018): The definitive treatment of how dependencies become failure paths — essential for understanding why arrow direction and shared dependencies matter so much when reading for fragility.
