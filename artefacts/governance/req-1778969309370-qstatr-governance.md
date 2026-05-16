# Guardrail Canvas — VP1: Direction Viewpoint

**GC-20260601-001 | Cloud Governance Model — Financial Services**

---

## Canvas Identification

| Field | Value |
|-------|-------|
| **Canvas ID** | GC-20260601-001 |
| **Organisation / Domain / Period** | Financial Services Enterprise — Cloud Governance Model — FY2026 |
| **Owner** | *\[Chief Architect — name required before activation\]* |
| **Status** | Proposed — awaiting Owner confirmation |
| **Review Date** | 2026-12-01 |
| **Supersedes** | N/A |

> **Activation Condition:** This canvas is inactive until a named Owner is recorded. CR-O1 requires a single named authority. A canvas without an owner cannot bind downstream decisions.

---

## Core Optimisation

We prioritise **regulatory integrity and audit-readiness** over **delivery velocity and cost efficiency** when trade-offs are required.

*Rationale: Basel III imposes binding capital adequacy, liquidity, and operational risk obligations. Cloud adoption that cannot be demonstrated compliant under regulatory examination is not an option — it is a liability. Velocity is subordinate to defensibility.*

---

## Non-Negotiables

- **Regulatory floor:** All cloud workloads hosting, processing, or transmitting material financial data must satisfy Basel III Pillar 2 operational risk standards. No exception without written sign-off from Chief Risk Officer and Group General Counsel.
- **Data sovereignty:** Customer financial data and regulatory reporting artefacts must reside within jurisdictions approved by the applicable prudential regulator. Cross-border data flows require documented legal basis and regulator notification where mandated.
- **Audit traceability:** Every architectural decision that affects risk exposure, capital calculation, or liquidity reporting must produce a traceable, time-stamped decision record (ADR or Trade-off Matrix entry). Undocumented decisions in these domains are treated as control failures.
- **Concentration risk ceiling:** No single cloud provider may host more than 60% of Tier 1 workloads by criticality-weighted compute. This ceiling operationalises Basel III Principle 9 (concentration risk management).
- **Exit viability:** Every cloud service contract above \$250k annual value must carry a documented exit strategy with a tested recovery path. Vendor lock-in that eliminates operational continuity is a risk management failure, not a commercial negotiation.
- **Incident notification:** Any cloud-hosted system failure affecting capital reporting, liquidity buffers, or risk data aggregation (BCBS 239) triggers mandatory incident logging within 4 hours and regulator notification within the period prescribed by the applicable prudential standard.

---

## Explicit Trade-offs

| Tension | Our Position | Rationale |
|---------|-------------|-----------|
| Deployment speed vs. compliance validation | Compliance validation — always | Deploying non-compliant workloads into production creates regulatory exposure that cannot be retrospectively remediated without material cost and reputational risk. Speed is not a defence under examination. |
| Multi-cloud complexity vs. operational resilience | Resilience — managed complexity is the cost | Basel III concentration risk requirements mandate multi-provider capability for Tier 1 workloads. Operational simplicity that creates single-point-of-failure is a compliance failure, not an architectural preference. |
| Shared cloud services vs. data isolation | Isolation for regulated data; shared services permissible at edge | Customer financial data, capital models, and liquidity positions require strict tenancy isolation. Infrastructure and DevOps tooling may use shared services with appropriate access controls. |
| Innovation velocity vs. platform stability | Stability in regulated core; experimentation in sandboxed non-production environments only | Instability in capital calculation or risk reporting infrastructure is a Pillar 2 operational risk event. Innovation that introduces instability into the regulated core is prohibited without a formal change authority decision. |
| Cost optimisation vs. resilience investment | Resilience — cost is a second-order variable for Tier 1 | The cost of a Basel III breach — capital penalty, supervisory action, remediation — exceeds achievable hosting savings by orders of magnitude. Cost optimisation applies at Tier 2 and below. |
| Proprietary cloud services vs. portability | Portability for regulated workloads; proprietary permissible for commodity functions | Workloads subject to regulator-directed remediation must be portable. Dependency on proprietary services that cannot be migrated within 90 days is a concentration risk. |

---

## Decision Authority

> This section declares who decides what. Ambiguity in decision authority is the primary source of Governance Drag in cloud adoption programmes. Every row below eliminates a category of undecided authority.

| Decision Domain | Authority | Escalation Path | Binding Constraint |
|----------------|-----------|-----------------|-------------------|
| Cloud platform classification (Tier 1 / 2 / 3) | Chief Architect + CRO joint sign-off | CIO → Board Risk Committee | Cannot be delegated below EA + Risk joint authority |
| Cloud provider selection for Tier 1 workloads | Architecture Review Board (ARB) with CRO concurrence | CIO → Board | Provider must satisfy third-party risk assessment before ARB vote |
| Data residency exceptions | Group General Counsel + CRO | Board Risk Committee | Regulator notification required before exception activates |
| Concentration risk threshold breach | CRO — must be notified within 24 hours of threshold breach | Board Risk Committee | Immediate remediation plan required; no new workload deployment to breaching provider until plan is approved |
| Architecture decisions affecting capital models | Chief Architect + Head of Risk Technology | CRO | ADR required; no verbal approvals accepted |
| Cloud security control derogations | CISO — no derogation below Essential Eight equivalent baseline | CRO + CIO joint | Every derogation carries a time-bound remediation commitment |
| Exit strategy sign-off for contracts \>$250k | Chief Architect — mandatory pre-execution review | CIO | Contract does not execute without documented exit strategy |
| Incident response (cloud-hosted regulated systems) | Head of Operational Risk — incident commander | CRO → Regulator | 4-hour internal log; regulator notification per prudential standard |

**Single Owner Rule (CR-O1):** Every decision domain above has one named authority class. Where joint authority is specified, one party holds the decision right and the other holds a veto. Joint authorities without a declared tiebreaker are a governance failure and must be resolved before this canvas activates.

---

## Compliance Mappings

> These mappings declare how this canvas's constraints operationalise Basel III and associated regulatory obligations. They are not aspirational. They are the minimum required to demonstrate compliance under examination.

| Guardrail | Regulatory Obligation | Standard Reference | Integrity Test |
|-----------|-----------------------|-------------------|----------------|
| Regulatory floor — Pillar 2 operational risk | Cloud as an operational risk domain; third-party risk management | Basel III Pillar 2; BCBS 239; local prudential standard (APRA CPS 231 / equivalent) | Annual third-party risk assessment on all Tier 1 cloud providers; results tabled to Board Risk Committee |
| Data sovereignty | Cross-border data transfer restrictions; regulator data access rights | Local prudential data localisation rules; GDPR (where applicable); BCBS 239 Principle 11 | Quarterly data residency attestation from cloud providers; regulator-accessible audit log |
| Audit traceability | Risk data aggregation and reporting; supervisory review readiness | BCBS 239 Principles 1–3 (governance and infrastructure); Basel III Pillar 2 ICAAP | Every ADR in the regulated decision domain is searchable and produceable within 24 hours of regulatory request |
| Concentration risk ceiling | Operational risk — third-party concentration | Basel III Pillar 2; BCBS 239 Principle 6; local outsourcing standards | Automated concentration metric reported monthly to CRO; breach triggers immediate escalation |
| Exit viability | Operational continuity; supervisory portability requirements | Local outsourcing and cloud guidance (APRA CPS 231 / EBA Cloud Guidelines / equivalent); Basel III Pillar 2 | Exit strategy tested annually for all Tier 1 providers; test results recorded and retained for 7 years |
| Incident notification | Operational risk event reporting | Basel III Pillar 2 operational risk; local incident reporting obligations | Incident log and notification timeline auditable; non-compliance with 4-hour window treated as a Pillar 2 control failure |
| BCBS 239 — Risk data aggregation | Accuracy, completeness, and timeliness of risk data in cloud-hosted systems | BCBS 239 Principles 4–9 | Cloud-hosted risk data pipelines subject to automated data quality fitness functions; failures reported to CRO within 24 hours |

---

## Governance Drag Analysis

> Governance Drag is the measurable latency introduced by governance processes that exceed the latency required to make a sound decision. The following are the primary Governance Drag sources identified for this enterprise context. Each is named and its resolution mechanism declared.

**Drag Source 1 — Undefined cloud tier classification criteria**  
Cloud workloads cannot be governed until they are classified. Without explicit Tier 1 / 2 / 3 criteria, every classification becomes a negotiation. Negotiation introduces Decision Latency. Resolution: Tier classification criteria must be published and owned by the Chief Architect before any workload migration commences. Classification is a decision, not a conversation.

**Drag Source 2 — Joint authority without tiebreaker**  
Wherever two authorities are listed as co-approvers with no declared tiebreaker, decisions stall. In financial services cloud governance, the most common stall point is Chief Architect vs. CRO on risk-performance trade-offs. Resolution: CRO holds the veto right on all decisions affecting Tier 1 operational risk classification. Chief Architect holds the veto right on all decisions affecting technical architecture integrity. Neither may override the other's domain without Board Risk Committee escalation.

**Drag Source 3 — Compliance interpretation latency**  
Regulatory obligations (Basel III, BCBS 239, local prudential standards) are subject to interpretation. When Legal, Risk, and Architecture interpret the same standard differently, decisions enter recursive review loops. Resolution: A single Regulatory Interpretation Authority is designated — Group General Counsel for legal effect; CRO for risk quantification; Chief Architect for architectural implication. Disagreements escalate once to CIO and resolve within 5 business days. CR-E3 terminal condition applies.

**Drag Source 4 — ARB cycle time exceeding decision urgency**  
Architecture Review Boards operating on fixed monthly cycles introduce structural Decision Latency for cloud adoption decisions. A 30-day ARB cycle is incompatible with cloud deployment timelines. Resolution: ARB must operate an expedited track (5-business-day turnaround) for decisions that do not affect Tier 1 risk classifications. CR-E1 (14-Day Decision Aging Rule) applies to all decisions in the ARB queue. Decisions aged beyond 14 days trigger mandatory escalation, not continued deferral.

**Drag Source 5 — Implicit non-negotiables**  
Non-negotiables that are understood but not written down are not non-negotiables — they are negotiation starting points. The primary source of Governance Drag in financial services cloud programmes is undeclared constraints that surface mid-delivery. Resolution: Every constraint in this canvas was previously implicit. It is now explicit. Any stakeholder who identifies an additional implicit constraint is obligated to surface it to the Owner within 30 days of canvas activation for formal inclusion or rejection.

---

## Altitude Collapse Risk

> Altitude Collapse occurs when enterprise-level direction is overridden, ignored, or gradually displaced by solution-level decisions made without reference to it. The following risks are declared, not speculative. Each has occurred in comparable financial services cloud programmes.

**Risk 1 — Cloud provider selection driven by team familiarity, not risk assessment**  
*Pattern:* Delivery teams select cloud providers based on existing skills and tooling. Risk assessment is performed after selection to justify a pre-made decision. Concentration risk accumulates invisibly.  
*Indicator:* Provider selection decisions are not traceable to an ARB decision record.  
*Control:* CR-T1 requires every provider selection Trade-off Matrix entry to reference this canvas. Untraceable selections are treated as unauthorised. Chief Architect conducts quarterly decision record audit.

**Risk 2 — Compliance treated as a project phase, not an operational state**  
*Pattern:* Compliance validation is performed at deployment and not revisited. Configuration drift, new service adoption, and regulatory updates create an Integrity Gap between the documented compliance position and actual operational state.  
*Indicator:* Compliance attestations are dated more than 12 months ago. No automated compliance monitoring is in place.  
*Control:* Compliance is continuous. Automated fitness functions enforce Basel III and BCBS 239 alignment on a continuous integration cadence. Attestation is quarterly, not annual. The Velocity of Truth for compliance state must be less than 30 days — meaning the documented compliance position must reflect actual operational state within 30 days of any change.

**Risk 3 — Guardrail Canvas superseded by project steering committee decisions**  
*Pattern:* Programme steering committees make scope, cost, and timeline decisions that implicitly override canvas constraints — particularly the resilience vs. cost trade-off — without acknowledging that a canvas override has occurred.  
*Indicator:* Steering committee minutes contain workload or cost decisions that contradict declared trade-off positions without an explicit canvas amendment record.  
*Control:* Any steering committee decision that affects a declared trade-off position in this canvas requires an explicit canvas amendment (new GC ID, new Owner sign-off) or a documented override with CIO authority. Undocumented overrides are CR-T1 violations. The Programme Architect is responsible for monitoring steering committee outputs against this canvas monthly.

**Risk 4 — BCBS 239 compliance assumed from vendor assurance**  
*Pattern:* Cloud providers supply compliance documentation. Delivery teams treat vendor documentation as sufficient evidence of BCBS 239 compliance without assessing whether the organisation's use of the service meets the principles.  
*Indicator:* BCBS 239 compliance records reference vendor certifications rather than organisational data governance assessments.  
*Control:* Vendor compliance documentation is a necessary but not sufficient condition. The organisation must separately demonstrate that its data aggregation and reporting processes — including those hosted on cloud infrastructure — meet BCBS 239 Principles 4–9. This assessment is owned by the CRO and is required before Tier 1 workload activation.

**Risk 5 — Decision Latency creating shadow governance**  
*Pattern:* When formal governance is too slow, delivery teams make architectural decisions informally to maintain momentum. These decisions are undocumented, unreviewed, and accumulate as technical and regulatory debt. This is the canonical Integrity Gap failure mode.  
*Indicator:* Deployed cloud architecture does not match the architecture described in the most recent ARB submission.  
*Control:* CR-E1 (14-Day Decision Aging Rule) is enforced without exception. Governance that consistently exceeds 14 days loses decision authority to the next level. The cure for shadow governance is faster formal governance — not more controls on shadow decisions.

---

## VAF Concept Applications

| Concept | Application in This Canvas |
|---------|---------------------------|
| **Integrity Gap** | The gap between documented compliance position and actual operational cloud state. Closed by continuous automated fitness functions and 30-day Velocity of Truth constraint. |
| **Decision Latency** | Introduced by undefined tier criteria, joint authorities without tiebreakers, and slow ARB cycles. Each source is named and has a declared resolution mechanism. |
| **Velocity of Truth** | Compliance state must reflect reality within 30 days. Architecture documentation must reflect deployed state within 14 days of any material change. Both are measured, not assumed. |
| **Governance Drag** | Five named sources identified. Each has a resolution mechanism. Governance Drag that is not named cannot be managed. |
| **Altitude Collapse** | Five named risk patterns. Each has an indicator (detectable signal) and a control (named owner, named action). Altitude Collapse that is not anticipated is guaranteed. |

---

## Analytic Test (VP1 Requirement)

*Did this canvas remove a debate from a portfolio or funding discussion? If not, the canvas is incomplete.*

**Applied:** This canvas removes the following recurring debates:
1. Whether compliance can be deferred to post-deployment — **No. It cannot. Non-negotiable.**
2. Whether cost optimisation can override resilience for Tier 1 workloads — **No. Resilience is the position. Non-negotiable.**
3. Which authority approves cloud provider selection — **ARB with CRO concurrence. Declared.**
4. Whether vendor compliance documentation satisfies BCBS 239 — **No. Organisational assessment is required. Declared.**
5. What happens when a decision ages beyond 14 days — **CR-E1 escalation. No debate required.**

Any debate not resolved by this canvas represents an incomplete constraint. Surface it to the Owner within 30 days.

---

## Correspondence Rules Compliance

| Rule | Status | Evidence |
|------|--------|---------|
| **CR-T1** — Every Trade-off Matrix must reference this canvas | Satisfied | Trade-off table declares positions; all downstream TOM entries must reference G