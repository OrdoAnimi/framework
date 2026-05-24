# Future Framework Lenses

**ZenCloud Global Consultants / Velocity Architecture Ecosystem**  
Classification: Internal Planning — Seed Documents  
Version: 1.0 — May 2026

---

## Governing Principle

The frameworks defined in this document are cross-cutting lenses on the parent Velocity Architecture Framework — not separate empires.

Each lens specialises the decision-first operating model for a domain. Each is governed by the same core principle: **decide first, then artefact**.

None of these frameworks are being built now. This document defines what they are, why they exist, and what they will become. Initial status: **planned / seed only**.

---

## Framework 1: Velocity Business Architecture

### Purpose

Velocity Business Architecture provides a structured lens for evaluating how architecture decisions connect to business capabilities, value streams, and operating model change.

Most architecture engagements treat business architecture as a separate upstream activity — something that happens before "real" architecture work begins. Velocity Business Architecture rejects this separation.

Business outcomes, capabilities, and value stream impacts are decision inputs — evaluated at every architecture gate, not confirmed once at the start and forgotten.

### Why It Exists

The gap between business architecture and solution architecture is one of the most common failure modes in enterprise programs. Business cases are approved. Solution designs proceed. The connection between the two is assumed, not verified.

Velocity Business Architecture makes that connection explicit — through structured decision criteria that include business capability impact, value stream alignment, and benefits realisation confidence.

### How It Fits

```
Velocity Architecture Framework
  ├── Enterprise Architecture lens
  ├── Business Architecture lens  ← this framework
  ├── Solution Architecture lens
  └── PMO / Delivery lens
```

Velocity Business Architecture occupies the Business Architecture box in the four-box operating model. It does not replace that box — it provides the structured method for operating within it using the decision-first model.

### Core Artefacts

| Artefact | Description |
|----------|-------------|
| Capability Impact Assessment | How does this decision affect business capabilities? |
| Value Stream Alignment Record | Which value streams are impacted and how? |
| Operating Model Impact Summary | What changes to the operating model does this decision require? |
| Benefits Realisation Register | What benefits are claimed, who owns them, and how will they be measured? |
| Stakeholder Impact Map | Who is affected, at what level, and when? |

### Example Use Cases

- Program business case validation — does the architecture decision deliver the claimed capability uplift?
- Operating model redesign — which architecture decisions are required to enable the target operating model?
- Benefits realisation governance — are the architecture decisions delivering against the committed benefits?
- Capability gap analysis — what is the delta between current and target capability, and what architecture decisions close it?

### Future Certification Possibility

A Velocity Business Architecture module within the Velocity Academy practitioner track.

Possible alignment with TOGAF Business Architecture, BIZBOK, and Value Stream Management frameworks for practitioners who hold external certifications in those methods.

### Future Tool Integration

VAF Agentic AI capability assessment prompt set. Capability Impact Assessment and Value Stream Alignment Record templates integrated into the VAF artefact engine.

### Recommended Repo Name

`velocity-ba` or `velocity-business-architecture`

### Initial Status

**Planned / seed only.** Do not build. Define only.

---

## Framework 2: Velocity Data Framework

### Purpose

Velocity Data Framework provides a structured lens for evaluating data readiness as a decision criterion in every architecture engagement.

Data is not a downstream technical concern. Data quality, availability, lineage, and AI-readiness determine whether architecture decisions can be executed — and whether AI adoption decisions are being made on a sound foundation.

### Why It Exists

The Data Readiness lens is already present in the Velocity Architecture Framework as one of the five cross-cutting lenses. The Velocity Data Framework is the specialised method for applying that lens in depth — for programs where data architecture is a primary architecture concern.

The most common failure: an organisation approves an AI adoption program without assessing whether its data is in a state that supports it. Architecture decisions are made. Implementation begins. Data quality problems surface at the integration layer and undermine the program.

Velocity Data Framework prevents this by making data readiness a decision gate, not a discovery.

### How It Fits

```
Velocity Architecture Framework
  ├── Enterprise Architecture lens
  ├── Business Architecture lens
  ├── Solution Architecture lens
  └── PMO / Delivery lens

Cross-cutting lenses:
  ├── Business Value
  ├── Data Readiness  ← Velocity Data Framework deepens this
  ├── Security Risk
  ├── AI Readiness
  └── Governance & Traceability
```

Velocity Data Framework extends the Data Readiness lens into a full diagnostic and decision-support method for data-intensive programs.

### Core Artefacts

| Artefact | Description |
|----------|-------------|
| Data Readiness Assessment | Structured evaluation of data quality, availability, and lineage |
| Source of Truth Register | Authoritative data sources identified and governed |
| Data Debt Register | Known data quality issues, their impact on program decisions, and remediation status |
| AI Readiness Data Profile | Assessment of whether data is in a state to support AI adoption in the engagement context |
| Continuous Pipeline Assessment | Evaluation of whether data pipelines can support ongoing decision intelligence |
| Data Decision Record | Formal record of data architecture decisions, including quality trade-offs accepted |

### Example Use Cases

- AI adoption programs — is the data ready for the AI use case being proposed?
- Data platform migration — what data quality risks are introduced by the migration architecture?
- Integration program design — what is the source of truth for each data domain in scope?
- Analytics and reporting uplift — what data debt must be addressed before reliable reporting is achievable?
- Regulatory compliance — what data lineage and quality evidence is required by the regulator?

### Future Certification Possibility

A Velocity Data Framework module in the Velocity Academy practitioner track.

Possible alignment with DAMA-DMBOK and the Data Management Body of Knowledge for practitioners holding data governance certifications.

### Future Tool Integration

VAF Agentic AI data readiness prompt set. Data Readiness Assessment and Data Debt Register templates. AI readiness scoring for data platforms integrated into the VAF scoring engine.

### Recommended Repo Name

`velocity-data` or `velocity-data-framework`

### Initial Status

**Planned / seed only.** Do not build. Define only.

---

## Framework 3: Velocity Security Framework

### Purpose

Velocity Security Framework provides a structured lens for evaluating security risk as a decision criterion in every architecture engagement.

Security is not a compliance gate at the end of an architecture program. Security risk, control requirements, and exception decisions are architecture decisions — and they must be made, recorded, and governed with the same rigour as any other design decision.

### Why It Exists

The Security Risk lens is already present in the Velocity Architecture Framework as one of the five cross-cutting lenses. The Velocity Security Framework is the specialised method for applying that lens in depth — for programs where security architecture is a primary concern, or where the organisation needs to improve how security decisions are integrated into architecture governance.

The most common failure: security is introduced at the final governance gate as a compliance check. The architecture is already decided. Security finds problems. Rework is expensive. Or worse — security approves what it cannot meaningfully challenge in the time available.

Velocity Security Framework prevents this by treating security as a decision input from the first architecture gate.

### How It Fits

```
Velocity Architecture Framework
  ├── Enterprise Architecture lens
  ├── Business Architecture lens
  ├── Solution Architecture lens
  └── PMO / Delivery lens

Cross-cutting lenses:
  ├── Business Value
  ├── Data Readiness
  ├── Security Risk  ← Velocity Security Framework deepens this
  ├── AI Readiness
  └── Governance & Traceability
```

Velocity Security Framework extends the Security Risk lens into a full diagnostic and decision-support method for security-intensive programs.

### Core Artefacts

| Artefact | Description |
|----------|-------------|
| Security Decision Record | Formal record of security architecture decisions, including controls selected and risks accepted |
| Control Selection Register | Which controls are applied, at what level, and why |
| Exception Register | Security exceptions formally approved, time-bound, and reviewed |
| Identity Architecture Decision | How identity, access, and authentication decisions are recorded and governed |
| Data Protection Decision | How sensitive data is classified, protected, and governed in the architecture |
| AI Security Readiness Assessment | Does the architecture's AI adoption introduce security risks that have been evaluated and governed? |
| Security Risk Register | Security-specific risks, rated by likelihood and impact, with mitigation actions and owners |

### Example Use Cases

- Cloud migration programs — what security architecture decisions are required and what risk is being accepted?
- AI adoption programs — what are the security implications of data exposure through AI tools?
- Identity and access management uplift — how are identity decisions made and governed?
- Regulatory compliance programs — how does the architecture demonstrate security control compliance?
- Third-party integration programs — what security decisions govern data exchange with external systems?

### Relationship to CISSP and Security Certifications

The Velocity Security Framework is not a replacement for CISSP or other security certifications. It is the method by which security-certified practitioners apply their expertise within the Velocity decision-first operating model.

A practitioner holding CISSP and Velocity Security Framework competency can operate as a security architecture advisor within ZenCloud engagements — applying security expertise through the decision-first lens rather than as a separate compliance function.

### Future Certification Possibility

A Velocity Security Framework module in the Velocity Academy practitioner track.

Possible alignment with ISC² (CISSP), ISACA (CISM), and ASD Essential Eight for practitioners holding external security certifications.

### Future Tool Integration

VAF Agentic AI security decision prompt set. Security Decision Record, Exception Register, and Control Selection Register templates. AI Security Readiness Assessment integrated into the VAF scoring engine.

### Recommended Repo Name

`velocity-security` or `velocity-security-framework`

### Initial Status

**Planned / seed only.** Do not build. Define only.

---

## Summary

| Framework | Domain | Cross-cutting lens | Repo | Status |
|-----------|--------|-------------------|------|--------|
| Velocity Business Architecture | Business outcomes, capabilities, value streams | Business Value | `velocity-ba` | Planned / seed |
| Velocity Data Framework | Data readiness, AI readiness, data debt | Data Readiness | `velocity-data` | Planned / seed |
| Velocity Security Framework | Security risk, controls, exceptions, identity | Security Risk | `velocity-security` | Planned / seed |

All three frameworks are extensions of the parent Velocity Architecture Framework. They share the same governing principle: **decide first, then artefact**. They operate within the four-box model. They are governed by the same engagement, IP, and data usage policies.

---

## When to Activate a Framework

A planned framework becomes an active development project when:

1. An enterprise engagement requires depth in that domain
2. Certification demand exists for the track
3. A research paper or book is ready to define the framework publicly
4. A partner consultancy requests the specialisation

Until then: seed only. Do not build, do not publish, do not create repos.

---

*ZenCloud Global Consultants — Brisbane*  
*Future Framework Lenses Version 1.0 — May 2026*
