# Pulse System — VAF VP5

**DataStage / Cognos / VMware Deprecated Platform → Cloud Migration**
**Capability Model for Cloud Solution and Decentralisation of On-Premises**

---

## Tier Determination

**Selected Tier: Tier 2 (Fortnightly)**

This engagement operates across three deprecated platform domains (DataStage, Cognos, VMware), each carrying distinct migration pathways, capability gaps, and vendor dependencies. Decision authority sits above individual delivery teams but below strategic board — the Programme Director and Enterprise Architect own the binding layer. Weekly cadence would over-rotate on tactical noise before the capability model is stabilised; monthly cadence would allow the Integrity Gap to widen across three concurrent workstreams. Fortnightly Tier 2 is the correct rhythm: sufficient frequency to prevent decision latency, sufficient scope to bind cross-platform dependencies.

---

## Pulse Configuration

| Field | Value |
|---|---|
| **Programme / Engagement** | DataStage, Cognos, and VMware Deprecated Platform to Cloud — Capability Decentralisation Programme |
| **Pulse Tier** | Tier 2 — Fortnightly |
| **Pulse Owner** | Enterprise Architect / Programme Director |
| **Participants** | Enterprise Architect (facilitator); Programme Director (binding authority); DataStage Migration Lead; Cognos Analytics Lead; VMware / Infrastructure Lead; Cloud Platform Architect; Data Governance Lead; Finance / FinOps Representative |
| **Session Duration** | 75 minutes — no extensions. Decisions not reached within time-box escalate per CR-E4 |
| **Effective From** | 2026-02-03 |

---

## Pulse Briefing

*Distributed 48 hours before Session 1. No surprises in the room.*

---

**PULSE BRIEFING**
Programme: DataStage / Cognos / VMware → Cloud | Date: 2026-02-03 | Tier: 2

---

### Decisions Requiring Binding This Session

| ID | Decision | Age (days) | Owner | Recommendation |
|---|---|---|---|---|
| TOM-20260120-001 | Target cloud platform selection for DataStage replacement — AWS Glue vs. Azure Data Factory vs. Databricks. Capability model cannot progress without platform commitment. | 14 | DataStage Migration Lead | **Decide** — capability mapping is blocked. Default to Azure Data Factory if no binding reached; log as forced resolution per CR-E1. |
| TOM-20260127-002 | Cognos retirement date and interim reporting continuity model — whether Power BI or Looker serves as transitional reporting layer during decentralisation phase. | 7 | Cognos Analytics Lead | **Decide** — business units are making shadow decisions. Silence at programme level is producing fragmentation. |
| TOM-20260124-003 | VMware workload classification — which workloads are lift-and-shift to IaaS cloud vs. re-platformed to PaaS vs. decommissioned outright. Without classification, cloud cost modelling cannot proceed. | 10 | VMware / Infrastructure Lead | **Decide or escalate** — if classification criteria cannot be agreed this session, escalate to Tier 3 with compressed scope: reframe as a boundary rule question, not a workload-by-workload review. |

---

### Open Questions Approaching Expiry

| Question | Raised | Expiry | Age (days) | Risk if Not Closed |
|---|---|---|---|---|
| Does the decentralisation model require a federated data mesh operating model, or does the central data platform persist in cloud form with domain consumption layers? This question directly determines the DataStage replacement architecture and the Cognos successor governance model. | 2026-01-19 | 2026-02-02 | 15 | **Critical.** Expired. Without a decision on operating model, the DataStage and Cognos capability maps are being built against incompatible target architectures. Escalate immediately if not bound this session. |
| What is the agreed data sovereignty and residency requirement for cloud-hosted workloads migrated from VMware on-premises? Region locking may constrain cloud provider selection and affect DataStage target platform choice. | 2026-01-26 | 2026-02-09 | 8 | **High.** Cloud provider finalisation is blocked until sovereignty posture is declared. Legal / Compliance input required before next session if not resolved here. |

---

### Escalations from Previous Session

*Session 1 — no prior escalations. Escalation register opens from this session forward.*

---

### Attendance Confirmation Required

Programme Director and Cloud Platform Architect are required participants for TOM-20260120-001 and TOM-20260124-003. If either is absent, those items do not proceed — they age into CR-E1 breach and trigger automatic Tier 3 escalation.

---

## Pulse Board

*Live during the session. Managed by the Pulse Owner. Not a discussion surface — a decision surface.*

---

### PULSE BOARD — Session 1 | 2026-02-03

---

#### Segment 1 — Aging Decisions (max 10 minutes per item)

| # | Item | Status entering session | Action required | Time-box |
|---|---|---|---|---|
| 1 | TOM-20260120-001 — DataStage target platform | Age 14 days — CR-E1 triggered | Bind today or escalate to Tier 3 with scope compressed to: "Which cloud provider is the strategic anchor for data integration?" | 10 min |
| 2 | Open question — federated mesh vs. centralised cloud platform | Age 15 days — expired | Bind operating model direction or formally escalate with terminal condition declared | 10 min |

---

#### Segment 2 — New Decisions for Commitment (max 10 minutes per item)

| # | Item | Owner | Decision required | Time-box |
|---|---|---|---|---|
| 3 | TOM-20260127-002 — Cognos transitional reporting layer | Cognos Analytics Lead | Select Power BI or Looker as transitional reporting layer. Decision binds the Cognos decommission schedule and business unit communication plan. | 10 min |
| 4 | TOM-20260124-003 — VMware workload classification | VMware / Infrastructure Lead | Approve classification framework (lift-and-shift / re-platform / decommission) and assign workload tiers. Does not require individual workload decisions today — framework only. | 10 min |

---

#### Segment 3 — Escalation Review

| # | Escalation scenario | Source | Compressed scope | Terminal condition |
|---|---|---|---|---|
| 5 | If data sovereignty posture is not declared by Legal / Compliance before 2026-02-09, cloud provider selection escalates to Tier 3 with a single question: "Is multi-region cloud operation permitted for data integration workloads?" | Cloud Platform Architect | Single yes/no sovereignty posture — not a full data classification exercise | Tier 3 Pulse on 2026-02-17. Decision binds regardless of remaining Legal review. |

---

#### Segment 4 — Ownership Gaps (max 5 minutes)

| Gap | Resolution required |
|---|---|
| No named owner for cloud FinOps governance model. Cloud cost accountability is unassigned across DataStage, Cognos, and VMware migration tracks. | Assign FinOps owner this session or escalate to Programme Director as a programme-level accountability failure. |
| Data Governance Lead not yet engaged in DataStage capability model. Data lineage and quality rules for migrated pipelines have no governance owner. | Data Governance Lead to be formally assigned to DataStage workstream by end of this session. |

---

## Pulse Report

*Distributed within 24 hours of session close.*

---

**PULSE REPORT**
Programme: DataStage / Cognos / VMware → Cloud | Session: 1 | Date: 2026-02-03 | Tier: 2

---

### Decisions Made This Session

| ID | Decision | Owner | Date Bound | Notes |
|---|---|---|---|---|
| TOM-20260120-001 | **Azure Data Factory selected as the strategic target platform for DataStage replacement.** AWS Glue excluded on grounds of existing Azure enterprise agreement and Entra ID integration. Databricks retained as a candidate for advanced analytics workloads only — separate decision required. | DataStage Migration Lead | 2026-02-03 | Capability model may now proceed against Azure Data Factory as target. Databricks scoping to be raised at Session 2. |
| TOM-20260127-002 | **Power BI selected as transitional reporting layer during Cognos decommission phase.** Looker excluded — no existing organisational licensing, procurement lead time incompatible with decommission schedule. Business units to be notified within five business days. | Cognos Analytics Lead | 2026-02-03 | Cognos decommission schedule to be drafted before Session 2. |
| OM-20260203-001 | **Operating model direction bound: centralised cloud data platform with domain consumption layers.** Full federated data mesh deferred — capability and staffing prerequisites not yet met. Decision to be revisited at Tier 3 quarterly review if domain maturity warrants. | Enterprise Architect | 2026-02-03 | DataStage and Cognos capability maps are now unblocked against a single target architecture direction. |

---

### Escalations Triggered This Session

| Escalation ID | Item | Escalated To | Compressed Scope | Terminal Condition | Responsible |
|---|---|---|---|---|---|
| ESC-20260203-001 | VMware workload classification framework — no agreement reached within time-box. Classification criteria disputed between Infrastructure Lead and Cloud Platform Architect. | Tier 3 — CIO / Architecture Review Board | Single question only: "Is the default disposition for non-classified VMware workloads lift-and-shift to IaaS, or decommission unless justified?" All individual workload decisions remain at Tier 2. | Tier 3 Pulse session 2026-02-17. Decision binds. No further deferral. | Programme Director to brief Tier 3 owner by 2026-02-10. |

---

### Questions Deferred — New Expiry Dates Assigned

| Question | Reason for Deferral | New Expiry | Owner |
|---|---|---|---|
| Data sovereignty and residency requirements for cloud-hosted workloads | Legal / Compliance representative absent. Input required before a position can be formed. | 2026-02-09 | Cloud Platform Architect to obtain written Legal position by 2026-02-09. If not received, this item triggers automatic Tier 3 escalation at Session 2. |
| Databricks scoping for advanced analytics workloads | Out of scope for Session 1 following ADF decision. Requires separate capability assessment. | 2026-02-17 | DataStage Migration Lead to initiate scoping before Session 2. |

---

### Ownership Assignments Made

| Gap closed | Assigned to | Effective |
|---|---|---|
| Cloud FinOps governance model | FinOps Representative — formal assignment confirmed by Programme Director | 2026-02-03 |
| Data Governance Lead assigned to DataStage workstream | Data Governance Lead — data lineage and quality rules for migrated pipelines | 2026-02-03 |

---

### Outstanding Actions Before Session 2 (2026-02-17)

| Action | Owner | Due |
|---|---|---|
| Notify business units of Power BI selection and Cognos decommission timeline | Cognos Analytics Lead | 2026-02-10 |
| Draft Cognos decommission schedule for review at Session 2 | Cognos Analytics Lead | 2026-02-14 |
| Obtain written Legal / Compliance position on cloud data sovereignty | Cloud Platform Architect | 2026-02-09 |
| Brief Tier 3 owner on ESC-20260203-001 VMware classification escalation | Programme Director | 2026-02-10 |
| Initiate Databricks advanced analytics scoping assessment | DataStage Migration Lead | 2026-02-14 |
| Produce first-pass cloud FinOps model across all three migration tracks | FinOps Representative | 2026-02-14 |

---

### Session Health Check

| Metric | Result |
|---|---|
| Decisions made | 3 |
| Escalations triggered | 1 |
| Decisions deferred without new expiry | 0 |
| Ownership gaps closed | 2 |
| Time-box breached | Yes — VMware classification (triggered escalation per CR-E4) |
| Pulse performing governance (not ceremony) | **Yes** — three binding decisions produced |

---

## Escalation Protocol

---

### Protocol: Tier 2 → Tier 3

**When triggered:**
Any decision that has not bound within two consecutive Tier 2 Pulse sessions escalates to Tier 3 (CIO / Architecture Review Board). Escalation is not optional — it is automatic under CR-E4.

**Scope compression rule (CR-E2):**
The question arriving at Tier 3 must be smaller than the question that left Tier 2. The Tier 2 session is responsible for compressing the scope before escalating. Presenting an unresolved Tier 2 debate in full to Tier 3 is a process violation. The Programme Director is accountable for scope compression quality.

**Format for Tier 3 escalation:**

| Field | Content |
|---|---|
| Escalation ID | ESC-YYYYMMDD-NNN |
| Source session | Tier 2, Session N, Date |
| Original question | Full statement as it entered Tier 2 |
| Compressed question | Single, binary or bounded-choice question only |
| Options considered at Tier 2 | Maximum three — with brief rationale for why Tier 2 could not bind |
| Recommended option | Named recommendation from Enterprise Architect |
| Terminal condition | "This decision binds at Tier 3 Pulse on [date]. It does not re-enter circulation unless [specific revisitation criterion] is met." |
| Tier 3 decision authority | CIO / Architecture Review Board Chair |

**Terminal binding condition for this engagement:**
All VMware workload classification decisions bind no later than the Tier 3 Pulse on 2026-02-17.
All cloud platform decisions bind no later than the Tier 3 Pulse on 2026-02-17.
Any decision that has not bound by 2026-03-03 is treated as a programme governance failure and reported to the programme sponsor.

**Maximum cycle rule (CR-E4):**
No decision passes through more than two Tier 2 Pulse cycles. No decision passes through more than one Tier 3 Pulse cycle without binding.

---

## Context-Specific Anti-Patterns

---

### Anti-Pattern 1: The Capability Map That Moves Without a Platform Decision

**Description:** The team continues building the cloud capability model — mapping DataStage pipelines, Cognos reports, VMware workloads — without binding the target platform. The map grows in detail and gives the appearance of progress, but every deliverable is provisional. When the platform decision finally lands, significant rework is triggered, or the team retroactively justifies the platform that matches what they have already built.

**Why this engagement is vulnerable:** Three platforms, three migration leads, each with a preferred cloud target. The capability mapping work can absorb months of effort before the platform question forces itself to a decision. The DataStage lead defaults to Azure. The VMware lead defaults to AWS. Cognos lead follows whoever moves first.

**Response:** Platform selection (TOM-20260120-001) is classified as a blocking decision. No capability map artefact advances to Decided status until the cloud platform anchor is bound. The Pulse Board enforces this — platform decisions are Segment 1 items, not background context.

---

### Anti-Pattern 2: Decentralisation as Endless Architecture Design

**Description:** The decentralisation of on-premises capability becomes a continuous operating model design exercise. Every Pulse session surfaces a new question about domain boundaries, ownership models, or data mesh principles. Decisions are deferred because "we need to finish the operating model first." The operating model never finishes. On-premises platforms continue operating past their deprecated end-of-life while the design debate continues.

**Why this engagement is vulnerable:** The federated data mesh vs. centralised cloud platform question is architecturally live and genuinely complex. It attracts strong opinions and sustained debate. The decentralisation framing invites scope expansion — every domain wants input into their future model.

**Response:** Operating model direction is bound at Session 1 to a single architectural stance (centralised cloud platform with domain consumption layers). This is not the final operating model — it is the directional binding that permits delivery to proceed. The Pulse Owner is authorised to close debate and bind at any point where discussion is producing elaboration rather than new decision-relevant information. Revisitation of this decision requires a formal CR-X2 trigger, not a standing agenda item.

---

### Anti-Pattern 3: VMware as the Gravity Well

**Description:** The VMware work