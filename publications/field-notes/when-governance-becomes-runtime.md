---
title: "When Governance Becomes Runtime"
subtitle: "A field note on moving governance from checkpoint to constraint, and what a governed worksite actually means."
author: "Phil Myint"
date: "2026-06-18"
series: "Coffee and Curiosity"
category: "Field Notes"
tags:
  - Architecture Governance
  - Velocity Architecture
  - StudioSix
  - Controlled Artefacts
  - AI Assisted Delivery
---

# When Governance Becomes Runtime

Most governance I have seen in my career was a meeting pretending to be a control.

That is not cynicism. It is a structural observation. The committee reviews the design after the design is substantially committed. The architecture board endorses the decision after the procurement is signed. The risk assessment is completed because the template requires completion, not because anyone expects it to change the build. The form of control is present. The force of control arrives too late to matter.

For years this was survivable, because delivery was slow enough that even late governance occasionally caught something before production did. AI-assisted delivery has removed that grace period. When a working system can exist by Thursday, a governance forum that meets monthly is not a control. It is a memorial service.

The last field note ended with the question this one has to answer: what happens when governance itself has to become runtime?

## From checkpoint to constraint

The shift I keep testing is simple to state and demanding to build. Governance stops being a stage in the process and becomes a property of the environment the work happens inside.

A checkpoint asks: did you follow the rules? A runtime constraint makes certain rule-breaking structurally difficult and makes the rest visible the moment it happens. The difference is the difference between a speed camera that posts you a fine three weeks later and a road that is physically designed so the safe speed is the natural speed.

This is what I mean when I call StudioSix a governed worksite rather than a workspace. The distinction is not branding. A workspace is where work happens. A worksite, in the construction sense, is a place you cannot enter without induction, where the hazardous zones are barricaded rather than merely signposted, where the permit to work is checked before the tools come out, and where an incident stops the line rather than feeding a lessons-learned register nobody reads.

Construction learned this the hard way, through fatalities. Software has mostly been spared that teacher, which is why our governance still leans on signage.

In practice, runtime governance looks unglamorous. Artefacts that cannot reach a client until they have passed through a controlled lifecycle: drafted, reviewed, versioned, approved, issued. Templates that carry their own guardrails so the dangerous sections cannot be silently deleted. Pipelines that refuse to deploy what has no owner. Agents that operate inside budget envelopes and capability boundaries declared before they run, not discovered after they have spent. Decision records that are generated as part of the work rather than reconstructed afterwards for the audit.

None of this is exotic engineering. Most of it is the governance we always claimed to have, finally moved to where the work actually happens.

## What AI changes, and what it does not

AI makes runtime governance both more possible and more necessary, and it is worth being precise about each.

More possible, because the machinery of control used to be too expensive. Keeping a decision log current, checking artefacts against standards, tracing which constraint applied to which build — this was clerical labour nobody funded. AI is genuinely good at exactly this class of work. The drafting of the control fabric can now be largely automated, which means the historic excuse for governance theatre, that real governance was unaffordable, is expiring.

More necessary, because the things being governed now act. A document cannot exceed its budget. An agent can. A template cannot quietly duplicate infrastructure across three regions overnight. An automated workflow can. When execution is continuous and partially autonomous, the only governance that means anything is governance that is present at the moment of action.

But here is what AI does not change, and this is the line I will keep redrawing as long as I write these notes. The constraint is only as good as the judgement that set it. A budget envelope drawn around the wrong capability governs nothing that matters. An automated control encoding a bad rule simply enforces the bad rule with perfect consistency and at machine speed. Runtime governance amplifies the quality of the architectural thinking behind it, in both directions.

AI drafts. Architect reviews. Clients receive controlled artefacts. In a runtime governance model, that principle stops being a slogan about documents and becomes the wiring diagram. The AI produces the candidate artefact inside the constrained environment. The review is a designed control point with a named human, not a courtesy. The thing that leaves the worksite is controlled not because someone remembered to check it, but because the site does not release uncontrolled things.

I want to be honest about the state of my own implementation, because these notes are field notes, not brochures. Parts of this exist and work. Parts are scaffolding held together by the fact that I am the only worker on the site, which means the induction lives in my head and the permit system is my own discipline. That is fine for one practitioner and completely inadequate for an organisation. Scaling the worksite means the constraints have to survive contact with people who did not write them and do not love them. That is the real test, and I have not passed it yet. I am building toward it.

What I can already see from inside the experiment is the direction of travel. Governance is migrating from the review calendar into the execution environment. The organisations that make that migration deliberately will get controls that operate at the speed of their delivery. The ones that do not will keep their forums and their packs, and the work will simply route around them, faster than ever, with AI helpfully generating the evidence of compliance on the way past.

There is, however, a cost to making governance fast that nobody warns you about. When the constraints bind at runtime and the signals arrive continuously, the system starts surfacing decisions faster than the humans inside it can responsibly make them. You remove every mechanical bottleneck and discover what was always standing behind them.

The next constraint is not the tooling, the telemetry, or the controls. It is judgement, and what happens when it becomes the bottleneck is where this series goes next.
