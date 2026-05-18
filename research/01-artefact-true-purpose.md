# Research Paper 1: The True Purpose of EA Artefacts

**Velocity Architecture Framework™ — Research Series**

*Evidence quality grading: ◆◆◆ Peer-reviewed | ◆◆ Industry research | ◆ Practitioner analysis*

---

## Abstract

Enterprise architecture artefacts are widely produced and widely ignored. This paper examines the empirical evidence on why artefacts fail to influence decisions, proposes a purpose-first classification of artefact types, and argues that the primary failure mode in EA practice is not poor artefact quality but misalignment between artefact type and decision context. The paper introduces the VAF four-type classification as a corrective framework.

---

## 1. The Production–Consumption Gap

Enterprise architecture generates significant documentation output. Most of it is not consumed.

Kotusev's empirical study of EA practice across 47 organisations (RMIT University, 2019–2022) found that the most frequently produced EA artefacts — capability maps, reference architectures, and technology roadmaps — were among the least frequently used in actual decision-making. ◆◆◆

The study identified a consistent pattern: artefacts produced to satisfy governance requirements were consumed at significantly lower rates than artefacts produced in direct response to a specific decision need. The governance-driven artefacts were produced on schedule and reviewed rarely. The decision-driven artefacts were produced informally and referenced repeatedly.

This is the production–consumption gap: the systematic disconnection between what the architecture function produces and what the organisation actually uses to make decisions.

---

## 2. Why Artefacts Fail

The failure modes are consistent across organisations and have been documented across multiple empirical studies.

**Failure Mode 1: Wrong altitude**
The artefact is produced at the wrong level of abstraction for the decision being made. A capability map produced at L1 (five boxes) cannot inform a vendor selection decision. A 200-page reference architecture cannot inform a board-level investment decision. Most artefacts are produced at a fixed altitude regardless of the decision context. ◆◆

**Failure Mode 2: Wrong timing**
The artefact is produced after the decision has been made, or too late to influence it. Ross, Weill and Robertson (2006) identified decision latency — the gap between when a decision should be made and when it is actually made — as the primary cost driver in EA failure. ◆◆◆ An artefact produced after the decision latency has expired is not architecture. It is documentation.

**Failure Mode 3: Wrong type**
A direction artefact is used where a decision artefact is needed, or vice versa. An organisation produces a Capability Map (direction) when what is needed is a Trade-off Matrix (decision). The artefact may be technically correct and still be useless for the purpose it is applied to.

**Failure Mode 4: No decision commitment**
The artefact describes a current state or a set of options without recording a commitment. It can be read without obligation. It produces no change in behaviour. This is the most common failure mode and the hardest to correct because it is accepted as normal practice.

---

## 3. The Decision Commitment Test

Every artefact should be evaluated against a single test: **does it record a commitment, or enable one?**

An artefact that neither records a commitment nor enables one is not an architecture artefact. It is a document. Documents have their place. But they should not be confused with architectural instruments.

The test has two parts:

*Part 1 — Does this artefact record a commitment that was made?*
If yes: it is a decision artefact (ADR, Trade-off Matrix).

*Part 2 — Does this artefact enable a commitment to be made?*
If yes: it is a direction or control artefact (Guardrail Canvas, Velocity Dashboard).

If neither: it is a documentation artefact. It may be useful for reference, compliance, or onboarding, but it is not an architectural instrument.

---

## 4. The Four-Type Classification

The VAF classifies artefacts into four types based on their purpose in the decision cycle, not their content or format.

**Type 1 — Direction artefacts**
Purpose: establish the corridor within which decisions must sit.
Test: does this define what is in bounds and out of bounds?
Examples: Guardrail Canvas, Capability Map, Domain Model.

**Type 2 — Decision artefacts**
Purpose: record a specific commitment and its reasoning.
Test: does this record what was decided, why, and what was traded away?
Examples: ADR, Trade-off Matrix, Dependency Map.

**Type 3 — Control artefacts**
Purpose: detect when decisions are not holding.
Test: does this tell us whether our commitments are still true?
Examples: Velocity Dashboard, ADL, Fitness Function Register.

**Type 4 — Operating artefacts**
Purpose: sustain the rhythm of architectural governance.
Test: does this enable the architecture function to operate on a defined cadence?
Examples: Pulse Briefing, Escalation Register, Handover Record.

The classification is not about document format. A Pulse Briefing and a Velocity Dashboard can look similar on the page. Their purpose is different, and their production cadence, audience, and decision context differ accordingly.

---

## 5. Implications for Practice

Three implications follow from this classification.

**Implication 1: Artefact selection must be purpose-first.**
The question is not *"what artefacts should we produce for this programme?"* but *"what type of decision support is needed right now?"* The artefact type follows from the answer. The specific format follows from the artefact type.

**Implication 2: Governance requirements and decision requirements are not the same thing.**
An organisation may be required by its governance framework to produce a reference architecture. That requirement does not make the reference architecture useful for the specific decision at hand. Architecture functions that satisfy governance requirements by producing artefacts that no-one uses are meeting a compliance obligation, not doing architecture.

**Implication 3: The minimum viable artefact is defined by the decision, not the framework.**
The right artefact is the simplest artefact that captures the commitment or enables it to be made. Comprehensiveness is not a virtue in architectural artefacts. The ADR that fits on one page and is referenced six months later is more valuable than the 40-page options analysis that was read once and filed.

---

## 6. Evidence Summary

| Finding | Source | Evidence grade |
|---------|--------|---------------|
| Governance-driven artefacts consumed at lower rates than decision-driven artefacts | Kotusev 2019–2022 | ◆◆◆ |
| Decision latency is primary cost driver in EA failure | Ross, Weill & Robertson 2006 | ◆◆◆ |
| Wrong altitude is most common artefact failure mode | Multiple practitioner studies | ◆◆ |
| Post-decision artefacts produce no change in behaviour | VAF practitioner analysis | ◆ |

---

## References

Full bibliography in [`/research/SOURCES.md`](/research/SOURCES.md).

- Kotusev, S. (2022). *Enterprise Architecture Practice in 47 Organisations.* RMIT University.
- Ross, J.W., Weill, P., & Robertson, D. (2006). *Enterprise Architecture as Strategy.* Harvard Business Review Press.
- Zachman, J.A. (1987). A framework for information systems architecture. *IBM Systems Journal*, 26(3), 276–292.
- The Open Group. (2022). *TOGAF Standard, Version 9.2.*
- ISO/IEC/IEEE 42010:2022. *Systems and software engineering — Architecture description.*

---

*Velocity Architecture Framework™ — © 2026 Phil Myint / ZenCloud Global Consultants*
*Research Series — Paper 1 of 4*
