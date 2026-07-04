# Chapter 4: Sacred Cows

*Where Architecture Truly Creates Value · Phil Myint · OrdoAnimi*

---

**The Question That Stops the Room**

There is a question that stops most architecture conversations in their tracks, and it is deceptively simple.

If clarity is so obviously valuable — if the case for fewer artefacts, sharper decisions, and cleaner layer separation is as straightforward as the previous chapters suggest — why don’t organisations choose it?

The question deserves more than a shrug. By the time an organisation has experienced enough dysfunction to recognise the diagnosis — the collapsed layers, the indecisive artefacts, the governance that produces ceremony rather than decisions — it has also experienced enough pain to understand the cost. The people inside these organisations are not indifferent to the cost. Many of them have absorbed it personally, in the form of overtime, stress, and the quiet erosion of confidence that comes from doing work that does not produce what it is supposed to produce.

And yet the patterns persist. The same governance ceremonies recur. The same monolithic documents are produced. The same decisions are deferred through the same consultation processes to the same inconclusive outcomes. Not because the people are ignorant of the problem. Not because they lack the capability to do better. But because the system they are operating inside has been shaped — not deliberately, but effectively — by a set of beliefs that make poor design feel not just acceptable but necessary.

These beliefs are sacred cows. They are not written down in any governance charter or architecture standard. They are rarely discussed explicitly. But they are defended with remarkable consistency, across industries and organisations of every scale, by intelligent people who have fully internalised them without ever having chosen to do so.

Understanding them is not optional. Until the beliefs that sustain architectural dysfunction are named precisely, every intervention aimed at changing the practice will be absorbed by the system that the beliefs protect.

**The First Sacred Cow: Effort as Virtue**

The most pervasive belief in dysfunctional architecture practices is also the most emotionally loaded: the belief that effort is itself evidence of value. That the person who works the longest, absorbs the most pressure, and keeps moving when everything else has stalled is demonstrating a form of professional virtue that deserves recognition and reward.

This belief does not begin as dysfunction. In the early stages of any complex programme, effort is genuinely required. The work is hard. The constraints are real. The people who push through difficulty and deliver results against the odds are, in that context, genuinely valuable.

The problem begins when the relationship inverts — when effort becomes not a response to genuine difficulty but a substitute for the design decisions that would make extraordinary effort unnecessary. When the organisation begins to celebrate the people who compensate for ambiguity through personal endurance rather than addressing the ambiguity that requires compensation.

At that point, effort has become the mechanism by which design failure is made invisible.

Consider what happens in a programme where a critical architectural decision has been deferred for six weeks. The delivery team cannot wait. They proceed on assumption. The assumption requires constant adjustment as the incomplete direction shifts with each governance cycle. The architects closest to the delivery team absorb the adjustment — revising designs, facilitating alignment conversations, producing revised artefacts that reflect the latest interpretation of a direction that has not yet been formally set. They work evenings. They attend additional meetings. They are described as highly committed, genuinely indispensable, exceptional contributors.

And because they are absorbing the cost of the deferred decision, the system receives no signal that anything is wrong. The governance cycle that is producing the delay has no visibility of the overtime, the stress, or the rework it is generating. From the perspective of the programme’s senior leadership, delivery is proceeding — with some difficulty, but proceeding. The signal that should trigger an intervention — the programme is suffering because a decision has not been made — is being suppressed by the effort of the people closest to the work.

**This is the perverse mechanism at the heart of the effort-as-virtue belief: the better the people, the longer the dysfunction can persist.** Organisations with highly capable, deeply committed practitioners can sustain fundamentally broken design practices for years, because the practitioners absorb the cost that would otherwise force a reckoning. The system is not fixed. It is buffered. And buffered dysfunction is permanent dysfunction, because it never accumulates to the threshold that would demand a response.

The cost is paid personally. The architects who absorb the most carry the most. They are the last to acknowledge that the work is unsustainable, because they have been rewarded — in recognition, in advancement, in the identity that comes from being indispensable — for absorbing precisely this kind of cost. By the time they leave, or burn out, or quietly stop caring, the belief that made their sacrifice necessary has been reinforced by their example. The next generation of architects learns, by observing what is rewarded, that endurance is the professional norm.

Organisations do not change this belief by telling people to work less. They change it by designing systems in which the decisions that currently require extraordinary effort to compensate for are made clearly, early, and on record — so that the extraordinary effort is not required.

**The Second Sacred Cow: Ambiguity as Protection**

The second belief is less visible than the first because it operates from a position of power rather than a position of endurance. It is the belief — held most reliably by the people with the most authority — that ambiguity is a form of protection.

Clarity, from the perspective of someone who holds authority and accountability for outcomes, is genuinely threatening. A clear decision is a visible decision. A visible decision can be evaluated. An evaluated decision can be found to be wrong. A wrong decision can be attributed to the person who made it. In an environment where the attribution of a wrong decision carries significant personal and reputational cost, the rational response is to avoid making decisions that are specific enough to be wrong.

The instruments through which this avoidance is achieved are sophisticated and largely invisible. The comprehensive position paper that describes the organisation’s strategic intent without committing to specific choices. The governance forum that invites input from a broad range of stakeholders and produces a record of the discussion without a binding outcome. The principle that is stated at a level of abstraction high enough to be consistent with any specific decision — we value security, we prioritise the customer, we embrace innovation — and therefore provides no basis for distinguishing between competing choices.

These instruments do not look like avoidance. They look like thoroughness. They look like inclusive leadership. They look like the kind of considered, stakeholder-sensitive approach that sophisticated governance requires. From inside the system, they feel like maturity.

**From the perspective of delivery, they feel like obstruction. And they produce the same outcome as deliberate obstruction, even though no one intended them to.**

When the direction from above is ambiguous enough that any specific approach can be justified against it, the delivery team is operating without a guardrail. They will proceed. They will make choices. Those choices will be locally rational — the best interpretation available given the information they hold. When the choices turn out to be inconsistent with what senior leadership actually intended, the accountability will migrate downward. The delivery team will be held responsible for a misalignment that was produced by the ambiguity of the direction they were given.

The people who produced the ambiguous direction will not experience this as accountability. They will experience it as a delivery failure. The belief that ambiguity protects them will be reinforced, because the ambiguity did protect them — the cost of the misalignment was absorbed by the people below them rather than returning to the people who produced the conditions that made misalignment inevitable.

**Clarity names trade-offs. It creates winners and losers. It makes accountability visible and therefore unavoidable.** This is not a comfortable property from the perspective of the people who hold authority for outcomes they cannot fully control. But it is the only property that allows delivery teams to make the right choices without the benefit of a direct line to the decision-maker’s actual intent.

Organisations that want to break this pattern cannot do so by asking leaders to be more decisive. They can do so by designing systems in which the cost of ambiguity is visible to the people who produce it — systems in which decision latency is measured, rework is attributed to its source, and the protection that ambiguity provides is reduced by making its consequences legible.

**The Third Sacred Cow: Governance as Performance**

The third belief is perhaps the most insidious, because it looks most like the solution to the problem it is actually perpetuating.

Most organisations that have experienced architectural dysfunction respond by strengthening governance. More review gates. More sign-off requirements. More comprehensive documentation standards. More checkpoints between conception and delivery. The logic is straightforward: if decisions are being made poorly, the answer is more oversight. If artefacts are being produced without sufficient rigour, the answer is more stringent standards. If delivery is proceeding without adequate architectural input, the answer is more mandatory architecture engagement.

Each of these responses is individually defensible. None of them addresses the actual problem. And together, they produce a governance apparatus that is heavier, slower, and more disconnected from the delivery reality it is supposed to serve — while creating the appearance of stronger oversight precisely because it is more visible, more formal, and more demanding of everyone’s time.

This is governance as performance. **The governance forum that meets weekly, reviews comprehensive documentation, asks searching questions, notes risks and assumptions, produces detailed minutes, and issues no binding decisions is performing governance rather than practising it.** It has all the visual properties of strong oversight — the frequency, the formality, the thoroughness — without the functional property that makes oversight valuable: the production of decisions that resolve ambiguity and allow delivery to proceed with clarity.

The performance is not cynical. The people running these forums genuinely believe that the process is adding value. The questions are good questions. The risks being noted are real risks. The documentation is thorough and accurate. The problem is that the forum has no mechanism for converting all of this excellent input into a binding architectural decision. It was not designed to produce decisions. It was designed to produce oversight — and oversight, in the absence of decisions, is simply a more expensive form of ambiguity.

Real governance is uncomfortable in ways that governance as performance is not. Real governance stops work when the conditions for proceeding do not exist. It forces decisions under pressure rather than deferring them for more information. It sometimes accepts loss — kills initiatives that have already consumed significant investment, enforces constraints that delivery teams would prefer to be treated as guidelines, holds accountability for outcomes in ways that are personally costly for the individuals involved.

The organisation that practises real governance will occasionally feel, in the short term, like it is moving more slowly. The initiation phase that now requires a genuine architectural decision before proceeding will take longer than the initiation phase that proceeded on assumption. The governance forum that now produces binding decisions will feel more intense than the forum that produced considered discussion.

Over time, the organisation that practises real governance moves significantly faster. Because the decisions that are made clearly at the front of a programme do not produce the rework, the integration failures, and the late-stage crises that decisions deferred to delivery always produce. The cost of clarity is paid once, at the beginning. The cost of ambiguity is paid repeatedly, throughout delivery, by the people least positioned to absorb it.

**The Fourth Sacred Cow: Pragmatism as Abdication**

The fourth belief is the one most frequently invoked in the moment when a difficult architectural decision must be made and the people responsible for making it are looking for a way not to.

*Let’s just be pragmatic.*

It sounds reasonable. It sounds mature. It sounds like the kind of thing that senior professionals say when they have learned that not every situation requires a perfect answer and that moving forward with imperfect information is sometimes the right call.

In practice, in architecture contexts, it almost always means something different. It means: proceed without making the decision, make assumptions quietly, let delivery figure it out, and deal with the consequences when they arrive — because dealing with them now would require a conversation that nobody wants to have.

True pragmatism is not the absence of decision. True pragmatism is the explicit acceptance of a trade-off — the deliberate choice to prioritise one thing over another, made clearly and recorded honestly, so that the organisation understands what it has chosen and what it has given up. *We are choosing delivery speed over architectural coherence in this phase, and we accept that the coherence debt will need to be addressed in the next.* That is a pragmatic decision. It is also a clear one. It can be evaluated. It can be held to. It can be reversed if the circumstances change.

The abdication that masquerades as pragmatism produces none of these properties. It is not a decision. It is the absence of one, dressed in the language of maturity. And because it is not recorded as a decision, it cannot be evaluated, cannot be held to, and cannot be reversed — because there is nothing in the record to reverse.

**The cost of this form of pragmatism is always paid downstream, always by the people least positioned to absorb it, and always at a higher price than the cost of making the decision clearly at the moment it was required.**

This is where architecture becomes ethically compromised. When decisions are avoided by those with the authority to make them, the architects closest to the delivery are asked to absorb the tension. To work something out. To find a compromise. To produce an artefact that captures the options without choosing between them — because choosing between them would require someone to own the consequence.

The architects who do this work are not doing architecture. They are performing a social function — translating the organisation’s unwillingness to decide into documentation that allows work to continue under the illusion that a decision has been made. It is skilled work. It is not architecture. And it is precisely the work that burns architects out — not because it is technically difficult, but because it requires them to produce outputs that they know are insufficient, in the service of a system that they know is broken, on behalf of a function that they were told would allow them to shape the direction of complex systems.

**Why Sacred Cows Persist**

Sacred cows persist not because the people who hold them are foolish or malicious, but because within the system that produced them, they are rational. The belief that effort is virtue is rational in an environment that rewards visible contribution and makes design failure invisible. The belief that ambiguity protects is rational in an environment where the cost of a wrong decision is personal and the cost of ambiguity is distributed across the delivery teams below. The belief that governance as performance is sufficient is rational in an environment where the appearance of oversight satisfies the governance obligation. The belief that pragmatism justifies abdication is rational in an environment where having the difficult conversation is costly and its avoidance is costless.

**Each belief is a rational adaptation to an environment that has been designed — not deliberately, but effectively — to reward it.** And because the beliefs are rational adaptations rather than simple errors, they cannot be changed by arguing that they are wrong. They can only be changed by changing the environment that makes them rational.

That is the structural argument this book is making. Not that the people inside these systems need to develop better beliefs. But that the systems themselves need to be redesigned so that the beliefs that currently make dysfunction survivable become irrational — so that the cost of ambiguity is visible to the people who produce it, the cost of effort-as-compensation is measured and attributed, the performance of governance is distinguishable from its substance, and the abdication that calls itself pragmatism is legible as what it actually is.

What that redesign requires is the subject of what follows.

The beliefs do not change first. The design changes first. And when the design changes, the beliefs follow.Sacred Cows: Why Organisations Choose Sacrifice Over Design

---

*Phil Myint · OrdoAnimi*
