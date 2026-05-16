# Trade-off Matrix

**TOM-20260115-002 | Cloud Governance Model — Financial Services Basel III Programme**

> VP2 — Decision Viewpoint | Velocity Architecture Framework™ v1.0
> ISO/IEC/IEEE 42010:2022 Conformant

---

## Decision Identification

| Field | Value |
|-------|-------|
| **Decision ID** | TOM-20260115-002 |
| **Decision Title** | Cloud Governance Model Selection — Basel III Compliant Financial Services Platform |
| **Date** | 2026-01-15 |
| **Owner** | Principal Architect (to be named at programme initiation) |
| **Status** | Decided |
| **Supersedes** | N/A |
| **Governing Canvas** | GC-20260101-002 — Cloud Platform Governance FY2026 (Basel III Compliance Programme) |

---

## Context

A regulated financial services firm is migrating workloads to cloud infrastructure under active Basel III operational risk obligations. Basel III imposes explicit requirements on data residency, audit traceability, concentration risk management, and third-party vendor oversight — all of which cloud adoption directly implicates.

The firm currently operates under a fragmented governance posture: infrastructure decisions are made at team level, there is no consistent cloud policy enforcement mechanism, and compliance evidence is assembled retrospectively at audit time rather than produced continuously. This is a textbook **Integrity Gap** — the documented architecture does not reflect the actual operating state, and the gap is widening as cloud adoption accelerates without structural governance to contain it.

Three symptoms define the urgency of this decision:

1. **Decision Latency:** Cloud adoption decisions are being made informally at team level without reference to a governing framework. Each uncoordinated decision narrows future options and accumulates regulatory exposure.
2. **Velocity of Truth Collapse:** Audit evidence is reconstructed after the fact. Regulators under Basel III expect continuous, contemporaneous traceability — not retrospective assembly.
3. **Concentration Risk Accumulation:** Without a governing model that enforces vendor diversity constraints, the firm is drifting toward unmanaged dependency on a single hyperscaler, which Basel III's operational risk pillars treat as a material risk event.

The decision cannot be deferred. Every week without a binding governance model is a week of regulatory exposure accumulating silently. The 14-Day Decision Aging Rule (CR-E1) applies immediately upon programme initiation.

---

## Options Considered

| Option | Summary | Key Advantage | Key Risk |
|--------|---------|---------------|----------|
| **A — Centralised Cloud Centre of Excellence (CCoE)** | A single central governance body owns all cloud policy, enforces standards, and gates deployment approvals | Maximum control; single source of truth for compliance evidence; clean audit trail | Delivery bottleneck; CCoE becomes a chokepoint; innovation velocity collapses under approval queues |
| **B — Federated Governance with Guardrails** | Business domains own cloud decisions within centrally defined, machine-enforced guardrails; compliance evidence generated continuously | Scales with the organisation; domain autonomy preserved; compliance embedded in delivery pipeline | Higher initial investment in tooling and policy-as-code; requires discipline to prevent guardrail erosion |
| **C — Reactive Compliance Overlay** | Cloud adoption proceeds with minimal governance; compliance evidence assembled at audit time via manual review | Near-zero upfront governance investment; maximum short-term delivery speed | Catastrophic regulatory exposure; Integrity Gap widens continuously; unsustainable at scale; fails Basel III continuous monitoring expectations |
| **D — Outsourced Governance (Managed Service)** | Third-party managed service provider assumes governance and compliance responsibility | Transfers operational burden; access to specialist expertise | Introduces third-party concentration risk (directly contrary to Basel III operational risk requirements); governance accountability cannot be outsourced under regulatory frameworks |

---

## Decision Drivers

| Driver | Weight | Notes |
|--------|--------|-------|
| **Basel III compliance — continuous audit traceability** | Critical | Non-negotiable regulatory obligation; retrospective assembly is not compliant |
| **Delivery velocity preservation** | High | Governance must not become the reason delivery stalls; the CCoE bottleneck pattern is a known failure mode in financial services |
| **Concentration risk management** | High | Basel III operational risk framework treats single-vendor dependency as a material exposure; governance model must enforce diversity constraints |
| **Integrity Gap closure** | High | The gap between documented and actual architecture must close, not stabilise; governance model must generate truth continuously |
| **Scalability of enforcement** | Medium | A model that works for 10 teams must work for 40; manual governance does not scale |
| **Time to first compliance evidence** | Medium | Regulators expect evidence of control from programme initiation, not at go-live |
| **Internal capability uplift** | Medium | Outsourcing governance capability creates long-term dependency risk and is inconsistent with regulatory accountability requirements |

---

## Decision

**Option B — Federated Governance with Guardrails is the committed direction.**

The firm will implement a federated cloud governance model in which:

- A central architecture function defines policy, enforces guardrails, and owns the compliance evidence framework
- Business domains retain autonomous deployment rights within guardrail boundaries
- Policy is expressed as code, machine-enforced at pipeline level, and audit evidence is generated continuously as a by-product of delivery — not assembled retrospectively
- Vendor diversity constraints are encoded as guardrails, not advisory principles, directly addressing Basel III concentration risk obligations

This decision is binding. Option A is rejected because centralised gatekeeping has a documented failure mode in regulated financial services: it creates the appearance of control while destroying the delivery velocity that makes compliance sustainable. Option C is rejected without further analysis — it is not a governance model, it is the absence of one, and it fails Basel III's continuous monitoring expectation categorically. Option D is rejected because regulatory accountability in financial services cannot be contractually transferred to a third party; the firm remains the responsible entity regardless of who operates the controls.

---

## Consequences

### What Is Gained

| Consequence | Description |
|-------------|-------------|
| **Continuous compliance evidence** | Audit trail is a pipeline by-product, not a project. Basel III continuous monitoring obligations are met structurally, not manually |
| **Integrity Gap closure** | Policy-as-code enforced at deployment time means the documented architecture reflects the actual architecture; the gap closes as a structural property of the model |
| **Delivery velocity preserved** | Domain teams deploy within guardrails without approval queues; the governance model accelerates compliant delivery rather than taxing it |
| **Concentration risk containment** | Vendor diversity constraints encoded as guardrails prevent unmanaged single-vendor dependency accumulation |
| **Velocity of Truth restored** | Architecture truth is generated continuously at pipeline execution; it does not depend on human documentation discipline |
| **Regulatory defensibility** | A federated model with machine-enforced guardrails produces a governance posture that regulators can inspect, test, and validate — not trust on assertion |

### What Is Accepted as Cost

| Cost | Description | Mitigation |
|------|-------------|------------|
| **Higher initial tooling investment** | Policy-as-code infrastructure, pipeline integration, and guardrail authoring require upfront investment before delivery velocity improves | Phased implementation — core guardrails in Wave 1; full coverage by Wave 3 |
| **Guardrail authoring discipline** | Guardrails must be maintained as the regulatory environment evolves; stale guardrails are as dangerous as no guardrails | Quarterly guardrail review cadence owned by central architecture function; CR-T1 enforced |
| **Domain team capability uplift required** | Federated governance only works if domain teams understand the guardrail model; adoption without understanding produces workarounds | Embedded architecture enablement programme in Wave 1; not optional |
| **Initial Decision Latency on guardrail design** | The first guardrail set requires significant investment to design correctly; errors here propagate at scale | Dedicated guardrail design sprint before any domain team onboarding begins |

---

## Sequencing Rationale

The following sequence reflects the principle that **governance infrastructure must precede governed delivery**. Inverting this sequence — allowing delivery to proceed while governance is designed in parallel — is the root cause of the Integrity Gap the firm currently exhibits. That pattern will not be repeated.

### Wave 1 — Foundation (Months 1–3)
**Objective:** Establish the guardrail framework before any net-new cloud workload is committed.

- Define the minimum viable guardrail set covering: data residency, identity and access, audit logging, and vendor diversity thresholds
- Express all guardrails as policy-as-code; no advisory-only controls
- Integrate guardrail enforcement into the CI/CD pipeline; deployment without passing guardrail validation is not possible
- Establish the compliance evidence registry — the authoritative store of continuous audit artefacts
- Onboard the central architecture function with ownership of guardrail authoring and review

**Decision Latency Target:** Guardrail framework binding and enforced by end of Week 10. No cloud deployment proceeds past Wave 1 without passing guardrail validation.

**Velocity of Truth Metric:** By end of Wave 1, 100% of new deployments generate continuous audit evidence. Retrospective assembly is retired as a practice.

---

### Wave 2 — Domain Onboarding (Months 3–6)
**Objective:** Extend federated governance to all cloud-active business domains.

- Onboard each business domain team with embedded architecture enablement
- Map existing cloud workloads against guardrail framework; identify and remediate violations
- Establish domain-level governance contacts responsible for local compliance posture
- Introduce concentration risk reporting — automated vendor dependency tracking against Basel III thresholds

**Decision Latency Target:** All existing workloads assessed and remediated or formally risk-accepted by end of Month 5.

**Integrity Gap Metric:** Integrity Gap (documented vs. actual architecture) measured and reported at each Pulse session; target <5% variance by end of Wave 2.

---

### Wave 3 — Maturity and Continuous Improvement (Months 6–12)
**Objective:** Embed governance as a continuous organisational capability, not a programme.

- Quarterly guardrail review cycle operational
- Fitness functions testing governance health automated in pipeline (`test_traceability_tom_to_canvas()`, `test_decision_aging()`)
- Regulatory change feed integrated — guardrails updated within 30 days of material regulatory change
- Pulse escalation model (CR-E4) operational for governance decisions exceeding 14-day aging threshold

---

## Investment Profile

| Category | Wave 1 | Wave 2 | Wave 3 | Notes |
|----------|--------|--------|--------|-------|
| **Policy-as-code tooling and pipeline integration** | $180k | $40k | $20k/yr | Open policy agent or equivalent; pipeline integration labour-intensive in Wave 1 |
| **Architecture function (central)** | 2 FTE | 2 FTE | 1.5 FTE | Guardrail authoring, review, and compliance evidence oversight |
| **Domain enablement programme** | $60k | $40k | $15k/yr | Training, embedded support, documentation |
| **Compliance evidence registry** | $30k | $10k | $8k/yr | Tooling and integration; feeds directly into Basel III audit artefacts |
| **Governance tooling (Velocity Dashboard equivalent)** | $25k | $10k | $10k/yr | Decision aging monitoring, Pulse cadence support |
| **Estimated Total** | **$295k** | **$100k** | **~$53k/yr ongoing** | Year 1 total: ~$395k. Year 2+: ~$53k/yr operational |

**Comparative Risk Basis:** Option C (reactive compliance overlay) carries an estimated regulatory remediation exposure of $2M–$8M based on peer-institution Basel III enforcement actions for equivalent control failures. The investment case for Option B does not require optimistic assumptions — it requires only that the cost of non-compliance be taken seriously.

---

## Correspondence Rule Compliance

| Rule | Status | Notes |
|------|--------|-------|
| **CR-T1** | Satisfied | This decision operates within GC-20260101-002; any guardrail override requires explicit canvas reference |
| **CR-T2** | Pending | ADRs implementing Wave 1 guardrail framework must reference TOM-20260115-002 upon creation |
| **CR-T3** | N/A | No prior decision superseded; first binding governance decision for this programme |
| **CR-O1** | Pending | Single named owner to be assigned at programme initiation; committee ownership is not compliant with this rule |
| **CR-E1** | Active | 14-Day Decision Aging Rule applies from date of this record; governance model must be binding and enforced within that window or escalation is triggered |

---

## Analytic Test

*Could a delivery team begin work the same day this was agreed?*

**Yes.** Wave 1 activities are immediately actionable: guardrail design sprint commences, tooling procurement begins, and the moratorium on ungoverned cloud deployment is enforceable from day one. No further interpretation is required.

---

*Velocity Architecture Framework™ — VP2 Trade-off Matrix*
*TOM-20260115-002 | © 2026 Phil Myint / ZenCloud Global Consultants. All rights reserved.*
*ISO/IEC/IEEE 42010:2022 Conformant | github.com/ZenCloudAU/velocity-architecture*