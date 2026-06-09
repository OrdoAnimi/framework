# Chapter 33: The Architecture Function

*Part 3 · The Core Concepts*

---

Architecture is sometimes one person and sometimes a department, and the journey between the two is rarely planned. It starts, very often, the way it started at Meridian: with a single person given the title and very little else, expected to bring order to an estate that took decades to disorder. This chapter is about how that single person becomes a function — what roles a mature architecture function contains, where it sits in the organisation, and, most importantly, how it earns and keeps the mandate without which it is just an opinion with a job title.

---

## What an Architecture Function Does

Before the roles, the purpose. An architecture function exists to do at the level of the organisation what no project, team, or system owner is positioned to do: hold the picture of the whole, and ensure that decisions made in the parts serve the whole rather than fragment it.

Every other role in IT is, appropriately, optimised for a part. The project manager delivers the project. The system owner runs the system. The infrastructure lead keeps the platform up. Each is doing their job well by attending to their part. The architecture function is the one role whose part *is* the whole — whose job is the connections, the consistency, the long horizon, and the consequences that no single part can see. This is why architecture cannot simply be distributed among the existing roles: the perspective it provides is precisely the one that no part-optimised role can hold.

Stated this way, the function's purpose is also its justification. It earns its place not by producing documents but by improving the decisions that the part-optimised roles cannot make well alone.

---

## The Roles

A mature architecture function contains several roles, which may be several people or several hats on a few people.

The **enterprise architect** holds the broadest and longest view — the whole estate, the strategic horizon, the relationship between technology and the organisation's direction. This is the role that owns the capability map, the principles, the roadmap. It is the most senior and the most abstract, and its risk is drifting so far from delivery that it loses touch with reality (a danger Chapter 54 returns to).

The **solution architect** works at the level of a specific solution or programme — translating the enterprise direction into a workable design for a particular piece of work. This is the role closest to delivery, the one that ensures a project's design honours the principles and fits the estate. Solution architects are the connective tissue between the enterprise view and the teams building things.

The **domain architect** holds deep expertise in one domain — data, security, applications, infrastructure — across the estate. The data architect who owns the master-data question, the security architect who owns the SABSA-style risk-to-control traceability. Domain architects provide the specialist depth that the generalist enterprise architect cannot hold alone.

The **architecture practice lead** owns the function itself — its standards, its governance processes, its people, its relationship with the rest of the organisation. In a small function this is the enterprise architect wearing another hat; in a large one it is a distinct role, because running the practice is itself a job.

These roles form a rough hierarchy of altitude — enterprise highest and most abstract, solution closest to the ground, domain cutting across, practice lead holding it together — and a healthy function has clear lines between them so that a question lands with the role equipped to answer it.

---

## Where It Sits

The placement of the architecture function in the organisation determines much of its effectiveness, and there is no single right answer — only a set of trade-offs.

Placed **high**, reporting to the CIO or CTO, the function has the seniority to govern and the reach to see the whole estate, but it risks the altitude problem — becoming a strategy function disconnected from delivery, producing direction that the teams below experience as edicts from people who do not build anything.

Placed **low**, embedded in delivery teams, the function stays connected to reality and earns the trust of the people doing the work, but it loses the cross-estate view and the authority to govern — it becomes good at solution architecture and unable to do enterprise architecture, because it cannot see or influence beyond its team.

The arrangement that tends to work is a small, senior enterprise capability placed high enough to govern, with solution architects embedded low enough to stay connected to delivery, and a deliberate, constant flow between the two. The enterprise architect who never leaves the boardroom and the solution architect who never sees the roadmap are both failing; the function works when the altitudes are connected by people who move between them.

---

## Earning and Keeping the Mandate

A mandate is permission to matter. An architecture function with a mandate is one whose involvement is sought, whose decisions are honoured, and whose absence from a decision is noticed. A function without a mandate has a title and an org-chart box and no actual influence — it is consulted as a formality, ignored in substance, and routed around when inconvenient.

Mandate is not granted by the org chart. It is earned, repeatedly, by being useful, and it can be lost. Three things earn it.

**Demonstrated usefulness.** The function earns mandate by improving decisions in ways people can feel — catching the expensive mistake, surfacing the dependency that would have derailed the programme, translating the structural problem into the language that unlocked the budget. Each demonstration of usefulness is a deposit. A function that has made enough deposits is sought out; one that has only produced documents is endured.

**Restraint.** Counter-intuitively, mandate is earned partly by *not* governing everything. A function that reviews every decision, however trivial, becomes a bottleneck that teams resent and evade, and the resentment erodes the mandate. A function that governs the few decisions that matter and visibly trusts teams with the rest earns the cooperation that makes its governance effective. The high ARB threshold from Chapter 28 is a mandate-preservation strategy as much as an efficiency one.

**Connection over control.** A function positioned as a gatekeeper — whose role is to say no — accumulates enemies and loses mandate with every refusal. A function positioned as connective tissue — whose role is to help decisions be better — accumulates allies and gains mandate with every contribution. This is de Visscher's argument (Chapter 51), and it is the single most reliable mandate strategy: be the function people want in the room, not the one they have to get past.

---

## Meridian: Building a Function from One Person

*Meridian's architecture function is, at the start, one person with a title and no team, no budget, and no mandate. How it grows over the first year is the practical answer to this chapter's question.*

*The EA does not begin by asking for a team. She begins by being useful — producing the heat map, the portfolio, the gap analysis — and discovers, as Chapter 32 recounts, that usefulness is not the same as analysis. The mandate begins to form only when she translates the architecture debt into the VMware business case and the CFO finds her useful. That is the first deposit, and it is what makes the next request — to establish the ARB — credible.*

*The ARB is the function's first institutional foothold. It is not a team, but it is a governance mechanism that gives the function a place to matter, and the EA staffs it with senior people from across the organisation rather than building an architecture silo. This is deliberate: she is borrowing mandate from the seniority of the board members rather than asserting a mandate the function does not yet have.*

*The first additional role she argues for is a solution architect — not another enterprise architect, but someone embedded in the VMware programme to keep the design honest at the point of delivery. This is the altitude lesson applied: she has the enterprise view; what the function lacks is the connection to delivery, and the solution architect provides it. The data domain — the master-data question that underlies everything — she initially holds herself, adding a data architect only once the identity work (Wave 3) makes the specialist depth indispensable.*

*A year in, the function is three people: an enterprise architect, a solution architect, and an emerging data domain capability, governed through an ARB that borrows seniority from across the organisation. It has a mandate not because the org chart granted one but because it has made enough deposits of demonstrated usefulness, exercised enough restraint to be trusted, and positioned itself as connective tissue rather than gate. It is, recognisably, a function — built from one person with goodwill and no budget, exactly as most architecture functions actually begin.*

---

## Translator Panel

> **The org chart says:** "Enterprise Architecture reports to the CIO and is responsible for the architecture of the enterprise."
>
> **What that means:** The box exists. Whether it matters is a separate question the org chart cannot answer. Reporting lines grant authority on paper; mandate — the permission to actually influence decisions — is earned through usefulness and can be absent even when the box is present.

> **Experienced architects say:** "We earn the right to govern by being useful first."
>
> **What that means:** Governance imposed before usefulness is demonstrated breeds resentment and evasion. Usefulness demonstrated before governance is requested earns the cooperation that makes governance work. The order matters: be useful, earn trust, then govern the few things that need it.

---

## The Key Idea

An architecture function exists to do what no part-optimised role can: hold the picture of the whole and ensure the parts serve it. It contains roles at different altitudes — enterprise, solution, domain, practice lead — and works only when those altitudes stay connected, with seniority high enough to govern and embedding low enough to stay close to delivery. Its placement is a set of trade-offs with no perfect answer, and its mandate — the permission to actually matter — is never granted by the org chart but earned, repeatedly, through demonstrated usefulness, restraint about what it governs, and positioning itself as connective tissue rather than a gate. Most architecture functions begin as one person with a title and no budget, and they become functions not by acquiring headcount but by accumulating enough deposits of usefulness that the organisation comes to want them in the room.

**Next:** Part 4 turns from the concepts to the artefacts. You do not need to produce every diagram an architect draws — but you do need to be able to read them all. Chapter 34 begins with the capability map.

---

## Further Reading

- **The Open Group — TOGAF Standard: Architecture Capability** (opengroup.org): The formal model of the architecture function, its roles, and the "Architecture Capability" needed to sustain a practice. Read it for the role definitions; supplement with this chapter's emphasis on mandate, which the standard treats as given.
- **Gregor Hohpe — The Software Architect Elevator** (O'Reilly, 2020): Once more the essential companion — particularly its argument that architects earn their position by connecting the floors of the organisation rather than occupying any one of them.
- **Camille Fournier — The Manager's Path** (O'Reilly, 2017): Though written about engineering management, its treatment of how technical functions earn organisational influence and grow from individual contributor to discipline maps closely onto the architecture function's growth.
