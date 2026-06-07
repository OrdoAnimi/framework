# ZAF Conformance Statement
## ISO/IEC/IEEE 42010:2022

**Framework:** ZenCloud Architecture Framework™ (ZAF)  
**Author:** Phil Myint / ZenCloud Global Consultants  
**Date:** May 2026  
**Standard:** ISO/IEC/IEEE 42010:2022 — Systems and software engineering — Architecture description

---

## Conformance claim type

The ZenCloud Architecture Framework™ claims conformance as an **Architecture Description Framework (ADF)** under ISO/IEC/IEEE 42010:2022.

An ADF is a framework used to define and govern the creation of architecture descriptions. ZAF satisfies the ADF requirements by:

- Establishing the conventions and practices for creating architecture descriptions
- Defining the viewpoints to be applied in an architecture description
- Specifying the correspondence rules that govern consistency between views
- Providing the artefact templates and instruments that implement each viewpoint

ZAF does not claim conformance as an Architecture Description (AD) — it is the framework that produces ADs, not an AD itself.

---

## Entity of interest

ZAF architecture descriptions address the following entities of interest:

**Primary entity:** The enterprise or organisation as a decision-making system — its capabilities, processes, applications, data, technology, and governance structures.

**Scope boundaries:**
- In scope: all architectural concerns that affect strategic decisions, investment allocation, risk management, and operational governance
- Out of scope: project-level implementation details, vendor-specific configuration, operational runbooks not affecting architectural position

**Temporal scope:** Current state (as-is), transition states, and target state (to-be) as required by the specific engagement or decision under consideration.

---

## Stakeholders and concerns

| Stakeholder | Primary concerns | Addressed by |
|---|---|---|
| Executive / SLT | Strategic direction, investment allocation, risk position | VP1 Direction, VP2 Decision |
| Enterprise Architect | Architectural integrity, decision quality, framework compliance | VP1–VP6 all viewpoints |
| Solution Architect | Solution design, trade-off analysis, technical decisions | VP2 Decision, VP3 Truth |
| IT Executive / Manager | Governance, portfolio management, roadmap alignment | VP4 Velocity, VP1 Direction |
| Business Owner / SME | Capability gaps, process effectiveness, accountability | VP1 Direction, VP2 Decision |
| Delivery team | Technical constraints, decision records, fitness functions | VP3 Truth, VP5 Rhythm |
| Auditor / Compliance | Decision traceability, evidence of architectural governance | VP3 Truth, VP4 Velocity |

---

## Viewpoints declared

Six viewpoints are defined in ZAF. Each viewpoint is formally specified in `/viewpoints/` and catalogued in `spec/VIEWPOINT-CATALOGUE.md`.

| ID | Viewpoint | Concerns addressed | Instrument |
|---|---|---|---|
| VP1 | Direction | Strategic intent, capability gaps, architectural vision | Guardrail Canvas |
| VP2 | Decision | Trade-off analysis, option evaluation, solution decisions | Trade-off Matrix |
| VP3 | Truth | Decision records, technical fitness, ground truth maintenance | ADRs + Fitness Functions |
| VP4 | Velocity | Architectural control, debt management, decision latency | Velocity Dashboard + ADL |
| VP5 | Rhythm | Operating cadence, escalation, pulse governance | Pulse System |
| VP6 | Practitioner | Practitioner integrity, operating model, Auctor Custos role | Integrity Arc |

---

## Correspondence rules declared

Seventeen correspondence rules are defined in `/correspondence-rules/RULES.md`. These rules govern consistency between views and are summarised in `spec/CORRESPONDENCE-MATRIX.md`.

All correspondence rules are of the form: if view X states condition Y, then view Z must be consistent with Y in the following way.

---

## Artefact set

ZAF defines 18 core artefacts across six layers (Strategy, Business, Application, Data, Technology, Governance). Each artefact is:

- Mapped to one of four functional types: decision instrument, control mechanism, signal generator, or ground truth
- Assigned to one or more viewpoints
- Provided with a compressed template and extraction guide in `/guides/VAF-Practitioner-Operating-Manual.md`

The full artefact classification is in `/frameworks/EA-Artefact-Type-Classification.md`.

---

## Evidence of conformance

| 42010 requirement | ZAF evidence |
|---|---|
| AD shall identify stakeholders and concerns | This document — stakeholders and concerns table |
| AD shall employ one or more viewpoints | VP1–VP6 defined in `/viewpoints/` and catalogued in `spec/VIEWPOINT-CATALOGUE.md` |
| Each viewpoint shall address specific concerns | VP concerns mapped in `spec/VIEWPOINT-CATALOGUE.md` |
| AD shall include one or more views conforming to declared viewpoints | View instruments defined per viewpoint in `/viewpoints/` |
| Correspondence rules shall be defined | 17 rules in `/correspondence-rules/RULES.md`, matrix in `spec/CORRESPONDENCE-MATRIX.md` |
| Rationale for viewpoint selection shall be stated | Rationale per viewpoint in `spec/VIEWPOINT-CATALOGUE.md` |

---

## Known gaps and limitations

The following items represent areas where ZAF conformance evidence is currently incomplete or developing:

**Model kinds:** Formal model kind specifications (conventions, notations, operations) are partially documented. VP3 Truth (ADRs) and VP2 Decision (Trade-off Matrix) have complete model kind definitions. VP4, VP5, and VP6 are partially specified.

**Formal consistency checking:** Correspondence rules are stated in natural language. Formal automated consistency checking is not yet implemented.

**Conformance assessment:** ZAF has not undergone independent third-party conformance assessment against ISO/IEC/IEEE 42010:2022. Self-assessment is the current basis for the conformance claim.

These gaps are acknowledged explicitly in accordance with the ZAF governing principle of evidence honesty: the research says so explicitly. These items are priorities for Version 2 of the framework.

---

## Revision history

| Date | Change | Author |
|---|---|---|
| May 2026 | Initial conformance statement produced | Phil Myint / ZenCloud |

---

*ZenCloud Global Consultants · ZenCloud Architecture Framework™ · May 2026*
