# Chapter 53: AI and the Capability Model — Davis

*Part 7 · The Practitioner's Compass*

---

The third practitioner argument looks forward. Graham Davis contends that artificial intelligence is not simply another technology to be modelled in the application layer — another box on the diagram. It is a disruption to the foundational model that has underpinned most capability thinking for decades: the People-Process-Technology triad. Davis's argument is that AI has become capable enough to perform work that previously required human judgement, and that this forces a rethink of how capabilities are designed, where the human-machine boundary sits, and what governance a capability needs.

This is the most speculative chapter in the book, because it is about a moving target. But the argument matters now, because the organisations building capability models today are building them with a triad that AI is quietly turning into a quartet.

---

## People, Process, Technology — and Now AI

The People-Process-Technology model has been the workhorse of capability design for a generation. A capability, on this model, is delivered by *people* following *processes* supported by *technology*. The three are distinct: people supply judgement, processes supply structure, technology supplies tools. Technology, crucially, was always a *tool* — something people used to execute a process. It did not exercise judgement; it did what it was instructed to do.

Davis's argument is that AI breaks this clean division, because AI does exercise something that functions like judgement. An AI that triages clinical messages, drafts documentation, or schedules resources is not a tool a person uses to execute a process — it is performing a part of the process that previously required a person. It sits in the place the model reserved for people (judgement) while being, in another sense, technology. The triad has no clean slot for it, and forcing it into the technology layer — treating it as just another application component — misrepresents what it does and obscures the questions its presence raises.

Davis's proposal is to make AI a first-class element of the capability model: **People-Process-Technology-AI**. Not because AI is more important than the others, but because it is *different in kind* from all three, and designing capabilities as though it were merely technology produces capabilities that are mis-designed and under-governed. The fourth element forces the questions the triad lets organisations skip.

---

## The Human-Machine Boundary

The central design question Davis's quartet raises is the **human-machine boundary**: within a capability, which judgements are made by people and which by AI, and how is the handoff between them designed?

On the old triad, this question barely existed, because technology did not make judgements — the boundary between human judgement and tool use was obvious. With AI in the model, the boundary becomes a deliberate design decision with real consequences. Which decisions does the AI make autonomously? Which does it recommend for a human to confirm? Which remain wholly human? Where exactly does the AI hand control to a person, and on what trigger? These are architecture questions — they are about the structure of the capability — and they have no good answers if AI has been quietly absorbed into the technology layer rather than designed for explicitly.

The boundary also has to be designed for *failure and accountability*, which is where the stakes are highest. When a human makes a judgement and it goes wrong, the accountability is clear. When an AI makes a judgement and it goes wrong, the accountability has to have been designed in advance — who is responsible, how is the AI's decision audited, what is the human override, and how does a person retain enough involvement to be meaningfully accountable rather than rubber-stamping outputs they cannot evaluate. A capability with AI in it but no designed human-machine boundary is a capability with an accountability gap, and accountability gaps in domains like healthcare are not acceptable.

---

## Davis Applied to Meridian in 2027

*The book imagines Meridian a year forward, in 2027, as AI enters two of its capabilities — clinical documentation and scheduling — and Davis's argument becomes concrete rather than theoretical.*

*AI arrives in clinical documentation as a drafting assistant: it listens to a consultation and drafts the clinical note for the clinician to review. On the old People-Process-Technology model, this would be filed as a new technology component supporting the existing documentation capability — a better tool. Davis's quartet forces the harder questions the tool-framing hides. Where is the human-machine boundary? The AI drafts; the clinician must review and sign — but does the clinician genuinely review, or does time pressure turn the review into a rubber stamp, leaving the AI effectively making the clinical record with a human signature on top? The boundary is not a technicality; it is the difference between an AI that assists a clinician and an AI that quietly replaces the clinician's judgement while the clinician carries the accountability. Designing that boundary explicitly — what the AI may draft, what the clinician must actively confirm, how the system ensures real review rather than reflexive approval — is an architecture decision that the technology-layer framing would never have surfaced.*

*AI arrives in scheduling as an optimiser: it allocates appointments and resources to maximise utilisation. Here Davis's argument bites differently. The AI is making allocation judgements that affect which patients are seen when — judgements with fairness and clinical-priority dimensions that the old triad, treating scheduling as a process supported by a tool, would not have flagged as needing governance. The quartet asks: what values is the AI optimising, who decided them, how are they audited, and where can a human intervene when the optimisation produces a clinically or ethically wrong allocation? The scheduling AI needs governance of a kind a scheduling tool never did, because it is exercising judgement, not executing instructions.*

*Reading Meridian's 2027 capability map through Davis's lens, the EA finds that AI has not simply added new technology to two capabilities — it has changed what those capabilities *are*, by moving judgement that was human into a machine and creating human-machine boundaries that have to be designed and governed. The capabilities that were People-Process-Technology are now genuinely People-Process-Technology-AI, and the ones designed without acknowledging the fourth element are exactly the ones with hidden accountability gaps. Davis's argument, speculative in the abstract, is concrete the moment AI enters a real capability in a real organisation that has people's health depending on it.*

---

## What Stays the Same

In keeping with the book's closing argument — which the next chapter makes fully — it is worth saying what Davis's argument does *not* change, because the forward-looking chapter should not lose the book's grounding.

AI changes what sits inside a capability; it does not change what a capability *is*, or the discipline of mapping, assessing, and governing capabilities. The capability map (Chapter 34) is still the right instrument; it now has a fourth element to account for. The governance function (Chapter 28) is still necessary; it now has AI judgements to govern as well as human ones. The human-machine boundary is a new design question, but it is answered with the same architectural thinking — seeing the system, tracing consequences, asking who owns the decision — that the rest of the book has taught. AI is a profound change in the *content* of capabilities and a modest change in the *method* of architecture.

This matters because the temptation, faced with a genuinely disruptive technology, is to believe that everything is new and the old discipline no longer applies. Davis's more careful argument is that the discipline applies *more* than ever — that an organisation putting AI into capabilities without architectural thinking about boundaries, accountability, and governance is building exactly the kind of unexamined, ungoverned estate that the whole book has been warning against, only now with machine judgement inside it. The frameworks are a map; AI is new territory; and the map-reading skills the book teaches are how you navigate territory you have not seen before.

---

## Translator Panel

> **The old model says:** "AI is a new technology component in the application layer — model it like any other system."
>
> **What that means:** AI gets treated as a tool, slotted into the technology layer, governed like an application. This misses that AI exercises something like judgement — it does work that used to require people — so the tool-framing hides the human-machine boundary and accountability questions its presence actually raises.

> **Davis's view says:** "Make AI a first-class element — People-Process-Technology-AI — and design the human-machine boundary explicitly."
>
> **What that means:** AI is different in kind from technology and needs its own place in the capability model, so that the design questions it raises — which judgements are the machine's, which are the human's, where control hands off, who is accountable — are confronted rather than skipped. The capability is mis-designed and under-governed if AI is absorbed silently into the technology layer.

---

## The Key Idea

Graham Davis argues that AI is not merely another technology component but a disruption to the People-Process-Technology model, because AI performs work that previously required human judgement and so has no clean slot in the triad — forcing his proposed quartet of People-Process-Technology-AI. The central new design question is the human-machine boundary: which judgements within a capability belong to the machine, which to the person, where control hands off, and how accountability is preserved so that humans remain meaningfully responsible rather than rubber-stamping outputs they cannot evaluate. Meridian in 2027 makes the argument concrete — AI in clinical documentation and scheduling does not just add a tool but changes what those capabilities are and creates accountability gaps wherever the boundary is left undesigned. Yet what AI changes is the content of capabilities, not the method of architecture: the map, the governance, and the architectural thinking apply more than ever, because putting AI into capabilities without that thinking builds exactly the unexamined estate the book has warned against, now with machine judgement inside it.

**Next:** Chapter 54 closes the book by returning to its opening argument — how to use the frameworks without being used by them, and how to stay grounded in the territory rather than lost in the map.

---

## Further Reading

- **Graham Davis — writing on AI and the capability model** (search his published work and talks): The People-Process-Technology-AI argument in the author's own words, and the most direct treatment of AI as a first-class architectural element rather than a technology component.
- **Stuart Russell — Human Compatible** (Viking, 2019): The foundational arguments for designing human oversight of AI systems and maintaining meaningful human control — the rigorous basis for Davis's boundary-design point.
- **UK Government / NHS — guidance on AI in clinical decision-making**: Real, evolving governance frameworks for AI in healthcare, which make Davis's accountability and human-oversight concerns concrete in exactly the setting Meridian represents.
