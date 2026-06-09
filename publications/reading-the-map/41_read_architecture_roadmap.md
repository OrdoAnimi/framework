# Chapter 41: How to Read an Architecture Roadmap

*Part 4 · Reading the Diagrams*

---

Part 4 closes where the practical work converges: the **architecture roadmap**, the artefact that sequences everything else. Chapter 25 explained what a roadmap is and how it differs from a project plan. This chapter applies the diagram-reading discipline of Part 4 to it — treating the roadmap not as a plan to be accepted but as a diagram to be *read critically*, and learning the questions that distinguish a governed plan from a wish list dressed up with arrows and dates.

This is the most directly useful chapter in Part 4 for most readers, because the roadmap is the diagram you are most likely to be asked to approve, fund, or commit to. Reading it well is the difference between endorsing a real plan and endorsing a hope.

---

## What You Are Looking At

A roadmap diagram typically shows time running left to right, with **waves** or **phases** as horizontal bands or columns, **initiatives** as bars or boxes positioned in time, **dependencies** as connecting arrows, and **transition states** as marked milestones between waves. There are many visual styles, but the underlying structure is always the same: a sequence of changes laid out against time, with the dependencies and the stopping points shown.

The first reading move is to orient: find the time axis, identify the waves, and locate the current state (left edge) and the target state (right edge). Everything between them is the claim the roadmap is making — *this is how we get from here to there.* Reading critically means interrogating that claim rather than absorbing it.

---

## The Four Critical Questions

Chapter 25 introduced four questions for assessing a roadmap. Here they become a reading procedure you can run against any roadmap diagram in roughly a minute.

**Where are the transition states, and is each one survivable?** Look for the marked stopping points between waves. A roadmap with no transition states — just initiatives running from current to target — has not thought about what the estate looks like partway through. For each transition state that *is* shown, ask the survivability question from Chapter 30: if the organisation had to stop here for a year, could it operate safely? A roadmap whose intermediate states are only safe if you keep moving is a roadmap of cliff edges.

**What drives the sequence — dependency, risk, or value?** For each arrow showing that one wave precedes another, ask *why this order?* Dependency-driven order (this needs what that produces) is robust. Risk- and value-driven order are legitimate choices that can be challenged. A roadmap whose author can name the driver for each sequence decision has thought it through; one whose sequence is "the order we thought of them" has not, and will stall when it meets a dependency it ignored.

**What is the governance mechanism?** This is the question that most often goes unasked and most reliably separates a plan from a wish. A roadmap is a statement of intent; what makes it real is the body with authority to hold the organisation to it — to stop a project jumping the queue, to prevent a wave being skipped, to enforce a transition state. Look for the named governance. If there is none, you are reading a wish list, however elegant its sequencing.

**Where does it get vaguer?** Trace the precision from left to right. It should decrease — the near waves detailed and costed, the far waves directional and loose. A roadmap equally precise three years out is either dishonest about its certainty or has confused itself with a project plan.

---

## Spotting the Wish List

A wish list masquerading as a roadmap has recognisable tells, and learning to spot them is the chapter's core skill.

The **dependency-free wish list** shows initiatives in parallel with no connecting arrows — everything happening at once, nothing waiting for anything. Real estates are full of dependencies; a roadmap that shows none has either not found them or chosen not to show them, and both are warnings.

The **uniformly-precise wish list** shows year three in the same detail as quarter one — every initiative neatly bounded and dated far into the future. This is the diagram pretending to a certainty no one has, and it will be wrong in detail in ways that discredit the whole.

The **governance-free wish list** shows a beautiful sequence with no mechanism to enforce it. It is the most common and most dangerous, because it looks complete. The test is simple: ask "what stops a project from ignoring this?" If the answer is "nothing, but everyone has agreed to it", the roadmap has no teeth, and agreement without enforcement decays the moment the first project finds the roadmap inconvenient.

The **all-value-front-loaded wish list** shows every visible benefit early and all the unglamorous enabling work pushed late or omitted. This inverts the dependency logic from Chapter 24 — it promises outcomes before building the enablers they depend on, and it tends to collapse when the early visible wins turn out to need the foundations that were deferred.

---

## Reading Meridian's Roadmap Critically

*Meridian's five-wave roadmap, designed in Chapter 25, is worth re-reading here through the critical lens, because a good roadmap should survive its own scrutiny.*

*Transition states: present and survivable. Three are marked, and the EA designed each (Chapter 30) to be safe to hold — the first transition state, in particular, is the one most likely to be forced by a funding review and was deliberately made the most comfortable to camp in. Reading the roadmap, the stopping points are real, not cosmetic. It passes the first test.*

*Sequence drivers: predominantly dependency, honestly labelled. The arrows show platform-and-governance before everything (Wave 1), low-risk migrations before clinical (Wave 2), identity before EPR consolidation (Wave 3), consolidation before integration modernisation (Wave 5). Each arrow has a dependency reason the EA can state. The one value-driven concession — quick reporting wins folded into Wave 2 to sustain executive patience — is annotated as a political accommodation rather than a necessity. A reader can see exactly which sequencing is robust and which is a defensible choice. It passes the second test, and passes it honestly because it does not disguise the one soft sequencing decision as a hard one.*

*Governance: named and real. The roadmap names the Architecture Review Board (Chapter 28) as the body that enforces the sequence, with the escalation path to the IT executive for unresolved objections. This is the answer to "what stops a project ignoring this?" — and crucially, by the time the roadmap is presented, the ARB has already demonstrated it can enforce a decision (the conditional-yes on the integration exception). The governance is not a promise; it has a track record. It passes the third test.*

*Vagueness gradient: correct. Wave 1 and Wave 2 are costed and scoped; Waves 4 and 5 are directional, with the EPR-consolidation cost explicitly marked as an estimate to be refined once identity is resolved. The roadmap is honest that it cannot yet cost year three precisely. It passes the fourth test.*

*The point of the exercise is not that Meridian's roadmap is perfect — it makes a political accommodation it is candid about, and its later waves are genuinely uncertain. The point is that it survives critical reading because it was built to be read critically. A roadmap that cannot answer the four questions is not necessarily wrong, but it is not yet ready to be funded, and a reader who runs the four questions can tell the difference between a plan to commit to and a hope to send back for more work.*

---

## Translator Panel

> **Programme leads say:** "Here's the roadmap — five waves, here's the sequence and the milestones."
>
> **What that means:** They are presenting the plan for how the estate moves from now to the target. The literate response is not to absorb it but to read it critically: where are the transition states, what drives the sequence, what enforces it, and where does it get vague? A good roadmap welcomes these questions; a wish list dressed as a roadmap deflects them.

> **A reader can ask:** "What stops a project from ignoring this sequence?"
>
> **What that means:** This single question tests whether the roadmap has governance — the mechanism that makes it real rather than aspirational. If the answer names a body with authority and, ideally, a track record of using it, the roadmap has teeth. If the answer is "nothing, but we've all agreed", it is a wish list, and the agreement will not survive the first inconvenient project.

---

## The Key Idea

An architecture roadmap is a diagram to be read critically, not a plan to be absorbed: a sequence of changes against time, with dependencies and stopping points shown. Four questions, run in about a minute, separate a governed plan from a wish list — where are the transition states and is each survivable, what drives the sequence (dependency is robust, risk and value are challengeable choices), what is the governance mechanism that enforces it, and does the precision honestly decrease with distance. The wish-list tells are recognisable: no dependencies shown, uniform precision into the far future, no enforcement mechanism, and all the visible value front-loaded ahead of the enablers it depends on. The decisive question is almost always the governance one — "what stops a project from ignoring this?" — because a roadmap without teeth is a hope, and a roadmap with a governing body that has already used its authority is a plan worth committing to.

**Next:** Part 5 turns from the diagrams to the words. Being understood, it turns out, is not the same as being right — and Chapter 42 begins the language map with the case for treating language as a professional discipline.

---

## Further Reading

- **The Open Group — TOGAF Standard: Phases E and F** (opengroup.org): The roadmap and migration-planning material; re-read alongside this chapter to connect the critical-reading questions to where each element is produced.
- **Steve McConnell — Software Estimation: Demystifying the Black Art** (Microsoft Press, 2006): The definitive treatment of why precision should decrease with distance — the "cone of uncertainty" — which is the rigorous basis for the fourth critical question.
- **Edward Tufte — The Visual Display of Quantitative Information** (Graphics Press, 2nd ed. 2001): On reading any diagram critically — distinguishing the data from the decoration, and spotting where a chart's visual confidence outruns its actual content. Applies directly to telling a real roadmap from a well-drawn wish.
