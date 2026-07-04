# Plain Language Guide to the The OrdoAnimi Framework

**Start here if you have never heard of enterprise architecture.**

---

## What this guide is

This guide explains what enterprise architecture is, why most organisations produce it incorrectly, and what one useful artefact looks like in practice. It requires no prior knowledge of architecture frameworks, ISO standards, or technical methodology.

If you are an architect, start with the [Framework Specification](/spec/FRAMEWORK-SPEC.md).

---

## The problem this framework solves

Most organisations face the same decision problem.

Something needs to change — a system, a process, a capability, a supplier. A decision needs to be made. The people who need to make that decision do not have the right information, presented at the right level, at the right time. So the decision either:

- Gets made badly, because it was made on incomplete or unclear information
- Gets delayed, because no-one is confident enough to commit
- Gets made, reversed, and made again, because the original reasoning was not recorded

Enterprise architecture, done correctly, solves this problem. It creates the clarity that enables better decisions to be made faster, with less rework.

Enterprise architecture, done incorrectly — which is most of the time — creates the opposite: documents that no-one reads, frameworks that no-one uses, and processes that slow everything down without improving anything.

This framework is built on a single test: **did this help someone decide?**

If an artefact, process, or document cannot pass that test, it is not architecture. It is administration.

---

## What an artefact is

An artefact is a document that records a decision, or the reasoning required to make one.

That is the entire definition.

An artefact is not:
- A process diagram produced to satisfy a governance requirement
- A capability map that nobody looks at after it is produced
- A document that describes what already exists without making any recommendation
- A deliverable produced to demonstrate that architecture work is happening

An artefact is the record of a decision made in a conversation, or the record of the reasoning that made that decision possible. Nothing more, nothing less.

---

## Why most organisations produce artefacts incorrectly

The standard sequence used in most organisations runs:

1. Produce artefacts
2. Have conversations
3. Make decisions

This sequence is backwards.

The artefact is produced first, before the conversation has happened, before the decision context is understood, before anyone knows what level of resolution is actually needed. The result is a document that either contains too much (a comprehensive capability map when a one-page decision brief was needed) or too little (a diagram without any reasoning, recommendation, or commitment).

The sequence that works is:

1. Have the decision conversation
2. Identify what needs to be recorded
3. Produce the minimum artefact that captures the commitment

The difference is not cosmetic. It changes everything about how architecture work is scoped, prioritised, and delivered.

---

## The four types of artefact

Every artefact in this framework falls into one of four categories. Understanding the categories tells you what the artefact is for and what level of detail it needs.

**Type 1 — Direction artefacts**
These declare intent at the enterprise level. They answer: *what are we trying to do, and what constraints apply to how we do it?* The primary instrument is the Guardrail Canvas. One per programme or initiative. Updated when strategic direction changes.

**Type 2 — Decision artefacts**
These record a specific architectural decision, the options considered, and the reasoning for the choice made. They answer: *what did we decide, why did we decide it, and what did we trade away?* The primary instruments are the Trade-off Matrix and the Architecture Decision Record (ADR). One per significant decision.

**Type 3 — Control artefacts**
These track the current state of architectural commitments over time. They answer: *are our decisions still holding, and where is drift occurring?* The primary instruments are the Velocity Dashboard and the Architectural Decision Log. Living documents, updated on a defined cadence.

**Type 4 — Operating artefacts**
These support the rhythm of architectural governance. They answer: *what needs attention this cycle, and who is responsible for what?* The primary instrument is the Pulse Briefing. Produced on a fortnightly or monthly cadence.

---

## What one useful artefact looks like

The most commonly needed artefact is the Architecture Decision Record (ADR).

An ADR does five things:

1. States the decision that was made, in one sentence
2. Names the context — what situation required a decision
3. Lists the options that were considered
4. Records the reasoning for the choice made
5. States the consequences — what was traded away, and what is now binding

A good ADR fits on one page. A decision that cannot be described in one page has not been understood well enough to be made.

Here is the minimum viable structure:

```
Title: [Decision name — verb + noun, e.g. "Adopt PostgreSQL as primary data store"]

Status: [Proposed / Accepted / Superseded / Deprecated]

Context:
[Two to four sentences. What situation existed that required a decision?]

Decision:
[One sentence. What was decided?]

Options considered:
[List. What else was on the table?]

Reasoning:
[Three to five sentences. Why this option over the others?]

Consequences:
[What is now true because of this decision? What constraints does it create?]
```

That structure, completed honestly, is more valuable than a forty-page architecture document that took six weeks to produce and will not be read.

---

## The compression principle

The OrdoAnimi is built on a compression principle: the right artefact at the right resolution, produced in the time actually available, is more valuable than the comprehensive artefact produced after the moment for decision has passed.

Most architecture processes are calibrated for the comprehensive artefact. The OrdoAnimi is calibrated for the minimum artefact that captures the commitment.

The savings are significant. A Guardrail Canvas produced in a two-hour workshop replaces a six-week strategy engagement. A Trade-off Matrix produced in a one-hour session replaces a three-week options analysis. An ADR produced immediately after a decision is made replaces a month of archaeology later when no-one can remember why the choice was made.

Architecture is not slow by nature. Most architecture processes are slow by design — calibrated for a thoroughness that is rarely needed and a comprehensiveness that is rarely used.

---

## Where to go from here

**If you need to make a decision now:**
Go to [`/templates/`](/templates/) and use the ADR template. Fill in the five fields. That is architecture.

**If you need to set direction for a programme:**
Go to [`/viewpoints/vp1-direction/guardrail-canvas.md`](/viewpoints/vp1-direction/guardrail-canvas.md) and follow the template.

**If you are running an architecture function:**
Go to [`/guides/VAF-Practitioner-Operating-Manual.md`](/guides/VAF-Practitioner-Operating-Manual.md) for the full operating model.

**If you want to understand the evidence base:**
Go to [`/research/`](/research/) for the four supporting papers.

**If you want the complete formal specification:**
Go to [`/spec/FRAMEWORK-SPEC.md`](/spec/FRAMEWORK-SPEC.md).

---

*The OrdoAnimi Framework — © 2026 Phil Myint / OrdoAnimi*
*ISO/IEC/IEEE 42010:2022 Conformant*
