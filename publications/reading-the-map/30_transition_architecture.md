# Chapter 30: Transition Architecture

*Part 3 · The Core Concepts*

---

No organisation moves from its current state to its target state in a single step. The journey passes through intermediate states, and each intermediate state is a real configuration of the estate that real people have to operate, real patients depend on, and real money funds. A **transition architecture** is the deliberate design of one of those intermediate states — a defined, stable, survivable configuration partway between where the organisation is and where it is going.

The chapter that the roadmap (Chapter 25) gestured at is this one. The roadmap shows the waves and names the transition states. This chapter is about what those transition states *are*, why designing them well is different from designing the target, and what it costs when the intermediate states are left undesigned — which is where the related idea of **decision latency** enters the book.

---

## The Intermediate State Is Where You Actually Live

There is a temptation, in architecture, to lavish attention on the target state and treat the path to it as mere logistics. The target is the elegant destination; the transitions are just how you get there. This gets the risk exactly backwards.

The target state, by definition, is where you arrive at the end — and you may never fully arrive, because by the time you get close the target has usually moved. The transition states, by contrast, are where the organisation actually operates for months or years at a time. Meridian will live in its first transition state — partially off VMware, clinical estate intact — for the better part of a year. That intermediate configuration has to work, day in and day out, with the same reliability as any other operating state. It is not a way-point glimpsed in passing; it is home for a while.

This reframes what a transition architecture is for. It is not designed for elegance, because nobody is meant to admire it. It is designed for **survivability** — it has to be operable, supportable, and safe for as long as the organisation has to live in it. A transition state that is theoretically clever but operationally fragile is a worse design than one that is inelegant but robust, because the people in it have to keep a hospital running from inside it.

---

## Designed for Safety, Not Beauty

The defining discipline of transition architecture is accepting ugliness in exchange for safety.

A transition state almost always involves running old and new in parallel — the old EPR alongside the new one, the VMware estate alongside the cloud platform, the point-to-point integrations alongside the emerging integration platform. Parallel running is inelegant. It duplicates cost, it requires reconciliation, it carries the cognitive load of two ways of doing the same thing. An architect optimising for elegance hates it.

But parallel running is frequently the safe choice, because it preserves a fallback. If the new EPR has a problem, the old one is still there. If a cloud migration misbehaves, the VMware workload has not yet been switched off. The transition state's inelegance *is its safety mechanism* — the redundancy that lets the organisation move without betting everything on a single cutover.

The architect's job in transition design is therefore to ask a question that target-state design never asks: *if this intermediate state has to hold for longer than planned — because funding slips, because a dependency is late, because a wave is paused — is it safe to stay here?* A transition state that is only safe if you leave it on schedule is not a transition state; it is a cliff edge with a deadline. Good transition architecture assumes the schedule will slip and designs each intermediate state to be survivable even if the organisation has to camp in it.

---

## Meridian's Three Transition States

*Meridian's roadmap defines three transition states, and the EA designs each one to be survivable rather than merely passed through.*

*The first transition state, after Wave 2, has Meridian partially migrated to the cloud platform — the low-risk workloads moved, the migration pattern proven, the clinical estate untouched on VMware. The EA designs this state to be genuinely stable: if the programme had to pause here for a year, Meridian could operate indefinitely, paying for both platforms but safe on both. The clinical systems, the highest-risk workloads, remain on the platform the organisation knows. This is deliberate — the first stopping point is the one most likely to be forced by a funding review, so it is designed to be the most comfortable to hold.*

*The second transition state, after Wave 3, adds the resolved patient-identity master while both EPRs still run. This is the subtlest of the three, because the value it delivers is invisible — there is no new system to show, only a data foundation that did not exist before. An organisation impatient for visible results is tempted to skip straight from "two EPRs" to "one EPR" without pausing at "two EPRs reconciled against a single identity master." The EA holds the line that this transition state must be reached and stabilised before EPR consolidation begins, because consolidating without it carries the identity problem into the new system. Designing this transition state is an act of resisting the pressure to skip the unglamorous middle.*

*The third transition state, after Wave 4, has a single EPR on the cloud platform with integration still running through the legacy point-to-point connections. Integration modernisation is deliberately left for last (Wave 5), so this transition state runs a modern application estate over legacy plumbing. It is inelegant — new systems, old connections — and the EA accepts the inelegance because integrating systems that are still moving would mean doing the integration work twice. The transition state is ugly and safe, which is the correct trade.*

---

## Decision Latency

Transition architecture introduces a cost that runs underneath the whole discipline and is rarely named directly: **decision latency** — the gap between when a decision *could* be made and when it actually *is* made, and what that gap costs.

Every transition state holds a set of pending decisions. While Meridian runs two EPRs, the decision about which one to consolidate to is open. While the integration platform is unbuilt, the decision about each integration's future is deferred. Some deferral is rational — the EPR decision genuinely depends on the identity master being in place first. But deferral has a cost, and the cost compounds the longer a decision stays open.

Decision latency costs in three currencies. It costs **money**, because an open decision usually means running parallel options — paying for two EPRs, two platforms, two ways of working — and the parallel cost accrues every day the decision stays open. It costs **risk**, because an undecided estate is a more complex estate, and complexity is where failure lives; every day in a transition state is a day exposed to that state's particular risks. And it costs **opportunity**, because resources tied up holding an undecided configuration cannot be deployed elsewhere, and decisions that depend on this one cannot proceed.

The insight that decision latency offers is that *deferring a decision is itself a decision with a price tag*. The organisation that puts off the EPR consolidation choice for another budget cycle is not avoiding a cost; it is choosing to pay another year of parallel-running cost and another year of carried risk in exchange for not deciding. Sometimes that is the right trade — the decision genuinely is not ready. But it should be made knowingly, with the latency cost visible, rather than by default. The most expensive decisions in many organisations are not the wrong ones; they are the right ones made too late, with the cost of the delay never counted.

---

## Translator Panel

> **TOGAF says:** "A Transition Architecture describes the enterprise at an architecturally significant state between the Baseline and Target Architectures. It is used to describe transitional states where this is useful — for example, to provide an implementable increment."
>
> **What that means:** Define the intermediate states the estate will actually pass through, and treat each one as a real architecture in its own right rather than a blur between the start and the end. "Architecturally significant" means a state stable enough to stop at and operate from.

> **Delivery teams say:** "Why are we designing the in-between state? We're only going to be in it for six months."
>
> **What that means:** Six months is long enough to need the lights to work. And "six months" has a way of becoming eighteen when a dependency slips or funding pauses. Designing the transition state is how you ensure that, however long you end up living in it, it is safe to live in.

---

## The Key Idea

A transition architecture is the deliberate design of an intermediate state between current and target — and because organisations live in their transition states for months or years, those states deserve as much design attention as the target, oriented around survivability rather than elegance. Good transition design accepts inelegance, especially parallel running, in exchange for the safety of a fallback, and it assumes the schedule will slip, designing each intermediate state to be safe to stay in. Underneath the discipline runs decision latency: the cost, in money, risk, and forgone opportunity, of the gap between when a decision could be made and when it is. Deferring a decision is itself a decision with a price, and the most expensive decisions in many organisations are the right ones made too late, with the cost of the delay never counted.

**Next:** Chapter 31 steps back from sequence to structure and introduces the vocabulary of architecture patterns — the recurring shapes that let you recognise a problem, and its known failure modes, by name.

---

## Further Reading

- **The Open Group — TOGAF Standard: Phase E, Transition Architectures** (opengroup.org): The formal placement of transition architectures within migration planning. Read alongside Chapter 25's roadmap material.
- **Niek de Visscher and others on decision latency**: The decision-latency concept has become central to recent EA thinking about why architecture functions add or destroy value; searching the term surfaces the practitioner literature that frames latency as the cost architecture exists to reduce.
- **Sam Newman — Monolith to Microservices** (O'Reilly, 2019): Newman's patterns for incremental migration — strangler fig, parallel run, branch by abstraction — are transition architectures in the software domain, and the clearest practical illustrations of designing safe intermediate states.
