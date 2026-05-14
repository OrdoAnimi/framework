# Velocity Architecture Framework™ — Formal Specification

**ISO/IEC/IEEE 42010:2022 Conformant Architecture Description Framework**  

Version 1.0 | © 2026 Phil Myint / ZenCloud Global Consultants  
TM Class 42, ZenCloud Consulting

---

## Framework Identification

| Field                  | Value |
|------------------------|-------|
| Full name              | Velocity Architecture Framework™ |
| Abbreviation           | VAF |
| Version                | 1.0 |
| Status                 | Published Specification |
| Owner                  | Phil Myint, Principal Architect, ZenCloud Global Consultants |
| Trademark              | TM filed — Class 42, ZenCloud Consulting |
| Primary domain         | Enterprise and solution architecture |
| Extended application   | Organisational leadership and decision governance |
| Conformance standard   | ISO/IEC/IEEE 42010:2022 |
| Repository             | github.com/ZenCloudAU/velocity-architecture |

---

## Central Thesis

> *Architecture exists to create clarity that leads to better decisions.*  
> *Velocity is not speed. It is the rate at which ambiguity expires.*

---

## 1. Scope and Conditions of Applicability

### 1.1 Entity of Interest (EoI)
The primary **Entity of Interest** is an **Enterprise Programme, Organisational Capability, or Solution under transformation**.  
Secondary EoIs include systems, platforms, and governance operating models.  
VAF explicitly supports multi-scale and nested EoIs.

### Primary Domain
VAF applies where architectural decisions must be made, owned, and acted upon across multiple layers with competing stakeholder concerns.

### Extended Domain
Applies to organisational leadership and governance where decision records replace traditional architecture descriptions.

### Not Applicable When
- Single technical component with no cross-boundary concerns
- Environments without governance or decision traceability requirements

---

## 2. Stakeholder Register

(Your original table retained — unchanged for now)

---

## 3. Concern Register

(Your original table retained — unchanged for now)

---

## 4. Architecture Viewpoints

(Your six viewpoints retained with only minor formatting/cleanup — unchanged in substance)

---

## 5. Architecture Description Life Cycle (New)

VAF defines four explicit states for every architecture artefact:

- **Proposed** → **Decided** → **Active** → **Superseded / Archived**

Transitions are governed by:
- Single owner rule (CR-O1)
- 14-Day Decision Aging Rule (CR-E1)
- Supersession traceability (CR-T3)
- Pulse escalation rules

---

## 6. Correspondence Rules (Summary)

Full rules: [`/correspondence-rules/RULES.md`](../correspondence-rules/RULES.md)

(Your original table retained)

---

## 7. ISO/IEC/IEEE 42010 Ontology Mapping

| 42010 Term                  | VAF Equivalent |
|-----------------------------|----------------|
| Entity of interest          | Enterprise Programme / Organisational Capability / Solution |
| Architecture                | Accumulated body of binding decisions |
| Architecture description    | Complete VAF artefact set |
| Stakeholder                 | Section 2 Stakeholder Register |
| Concern                     | Section 3 Concern Register |
| Architecture viewpoint      | VP1–VP6 |
| Architecture view           | Instantiated VAF artefact |
| Model kind                  | Specific instruments (Guardrail Canvas, Trade-off Matrix, ADR, etc.) |
| Architecture decision       | Trade-off Matrix + ADR |
| Architecture rationale      | Rationale fields + Context/Consequences |
| Correspondence rule         | Section 6 Correspondence Rules |
| Architecture framework      | Velocity Architecture Framework™ |

---

## 8. Conformance Declaration

The Velocity Architecture Framework, Version 1.0, claims **full conformance** with ISO/IEC/IEEE 42010:2022 as an **Architecture Description Framework (ADF)**.

| Requirement                          | Status     | Reference |
|--------------------------------------|------------|---------|
| Framework identification             | Satisfied  | Section above |
| Entity of Interest definition        | Satisfied  | Section 1.1 |
| Stakeholders & concerns              | Satisfied  | Sections 2 & 3 |
| Viewpoints & model kinds             | Satisfied  | Section 4 |
| Correspondence rules                 | Satisfied  | Section 6 |
| Architecture Description Life Cycle  | Satisfied  | Section 5 |
| Conditions of applicability          | Satisfied  | Section 1 |
| Consistency with conceptual model    | Satisfied  | Section 7 |

---

*Velocity Architecture Framework™ — Formal Specification v1.0*  
*© 2026 Phil Myint / ZenCloud Global Consultants. All rights reserved.*  
*ISO/IEC/IEEE 42010:2022 Conformant | TM Class 42, ZenCloud Consulting*  
*github.com/ZenCloudAU/velocity-architecture*
