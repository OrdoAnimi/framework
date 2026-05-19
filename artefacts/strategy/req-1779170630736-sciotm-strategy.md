# Trade-off Matrix

**TOM-20260115-002 | DataStage, Cognos, and VMware Deprecated Platform Migration to Cloud**

> VP2 — Decision Viewpoint | Velocity Architecture Framework™ v1.0
> ISO/IEC/IEEE 42010:2022 Conformant

---

## Decision Identification

| Field | Value |
|-------|-------|
| **Decision ID** | TOM-20260115-002 |
| **Decision Title** | DataStage, Cognos, and VMware Deprecated Platform Migration — Cloud Capability Enablement and On-Premises Decentralisation |
| **Date** | 2026-01-15 |
| **Owner** | *\[To be assigned — single named owner required per CR-O1\]* |
| **Status** | Proposed |
| **Supersedes** | N/A |
| **Governing Canvas** | *\[Reference governing Guardrail Canvas ID when issued — CR-T1\]* |

---

## Context

The enterprise operates three platforms that have entered or are approaching end-of-support: **IBM DataStage** (ETL and data integration), **IBM Cognos Analytics** (enterprise reporting and BI), and **VMware vSphere/vCenter** (on-premises virtualisation infrastructure). Together, these platforms underpin data movement, analytical reporting, and the compute substrate on which a broad set of workloads currently runs.

The convergence of deprecation timelines creates a compounding risk. Each platform, individually, would constitute a discrete migration programme. Collectively, they represent a capability inflection point: the organisation must decide not merely how to replace like-for-like, but whether the target architecture reflects the decentralised, cloud-native operating model the enterprise intends to achieve.

This decision is not primarily a technology procurement decision. It is a **capability architecture decision**. The central question is: what capability model should govern data integration, analytics, and compute going forward — and in what sequence should migration commitments be made to avoid compounding delivery risk while eliminating the Integrity Gap that has accumulated across all three deprecated platforms?

The **Integrity Gap** is already active. Each platform running beyond its support window diverges further from vendor roadmaps, accumulates unpatched vulnerabilities, and binds the organisation to operational patterns inconsistent with the target state. The **Velocity of Truth** — the rate at which the organisation's architectural understanding of its own estate updates to match reality — is declining. Every quarter of non-decision increases **Decision Latency** and raises the cost and complexity of eventual migration.

No constraints have been formally declared for this decision. This increases the risk of option proliferation and deferred commitment. This matrix therefore imposes sequencing discipline on the absence of constraint.

---

## Options Considered

| # | Option | Summary | Key Advantage | Key Risk |
|---|--------|---------|---------------|----------|
| 1 | **Lift-and-shift all three platforms to IaaS cloud** | Migrate DataStage, Cognos, and VMware workloads to cloud-hosted VMs without re-architecture | Fastest path to vacating on-premises infrastructure; lowest initial complexity | Replicates deprecated patterns in cloud; defers capability debt; does not achieve decentralisation intent; ongoing licensing costs unchanged |
| 2 | **Replace DataStage → cloud-native ELT; retain Cognos and VMware short-term** | Migrate data integration to a cloud-native pipeline platform (e.g., Azure Data Factory, AWS Glue, dbt) first; treat Cognos and VMware as deferred waves | Decouples highest-risk data integration layer; enables modern data capability earliest; reduces sequencing complexity | Two active migration programmes overlap; Cognos dependency on data layer creates coupling risk if not managed; VMware deferral extends security exposure |
| 3 | **Replace all three platforms sequentially: VMware → DataStage → Cognos** | Migrate compute substrate first, then data integration, then analytics | Logical infrastructure-first sequence; each layer stable before next migration commences | Longest time to decentralisation outcome; Cognos and DataStage remain on deprecated VMware during extended transition; maximum accumulation of Integrity Gap |
| 4 | **Parallel capability streams: cloud-native data platform + VMware exit + Cognos SaaS migration** | Run three coordinated workstreams concurrently under a unified programme structure, targeting cloud-native replacements across all three domains | Fastest path to full capability target; eliminates deprecated platforms in a single programme arc | Highest delivery complexity; requires skilled parallel programme management; investment profile is front-loaded; organisational change burden is high |
| 5 | **Adopt SaaS analytics (e.g., Power BI, Tableau, Looker) and exit Cognos first; then address DataStage and VMware** | Prioritise analytics decentralisation through SaaS adoption; treat Cognos as the fastest win given SaaS maturity | Quickest visible business value; analytics stakeholders gain capability immediately | Data integration layer (DataStage) remains deprecated; analytics outcomes constrained by quality of upstream data until DataStage is replaced; creates partial decentralisation |

---

## Decision Drivers

| Driver | Weight | Rationale |
|--------|--------|-----------|
| **Elimination of security and compliance exposure from unsupported platforms** | High | All three platforms approaching or past support windows represent active risk. VMware deprecation in particular affects the broadest surface area across hosted workloads. Non-negotiable to resolve within programme horizon. |
| **Alignment to decentralised, cloud-native capability model** | High | The stated strategic intent is not mere infrastructure migration. The target capability model requires decentralisation of data, compute, and analytics. Lift-and-shift does not satisfy this driver. |
| **Delivery sequencing — avoiding compounding risk** | High | Three concurrent migrations create team capacity, dependency, and governance complexity. Sequencing must be deliberate and evidence-based, not arbitrary. |
| **Time-to-value for data and analytics consumers** | Medium-High | Business units dependent on Cognos reporting and DataStage pipelines have tolerances for disruption. Sequencing must account for business continuity alongside platform exit. |
| **Investment profile and funding cadence** | Medium | Without declared constraints, the investment profile remains to be bounded. However, front-loaded parallel programmes carry execution risk disproportionate to organisations without established cloud delivery capability. |
| **Team capability and cloud readiness** | Medium | The organisation's existing skills in cloud-native data platforms, SaaS analytics, and hyperscaler infrastructure will govern realistic delivery velocity. Capability gaps must be surfaced before commitments are locked. |
| **Vendor licensing and contract exit timelines** | Medium | IBM DataStage and Cognos carry enterprise licensing agreements with defined exit windows. VMware licensing changes (post-Broadcom acquisition) may impose commercial urgency independent of technical readiness. |

---

## Decision

**Option 4 — Parallel capability streams under a unified programme structure — is the committed direction, with sequencing constraints imposed to manage delivery risk.**

The organisation will initiate three coordinated workstreams:

1. **Workstream A — VMware Exit and Cloud Compute Foundation:** Migrate virtualised workloads to cloud IaaS/PaaS, establishing the compute and networking substrate on which data and analytics workloads will land. This workstream must reach minimum viable cloud foundation within the first programme quarter before DataStage and Cognos migrations introduce dependency load.

2. **Workstream B — DataStage Replacement with Cloud-Native Data Integration:** Replace IBM DataStage pipelines with a cloud-native ELT/ETL platform selected through a constrained proof-of-concept evaluation (not to exceed 6 weeks). Pipeline re-development follows cloud compute foundation readiness from Workstream A.

3. **Workstream C — Cognos Exit and SaaS Analytics Adoption:** Exit IBM Cognos through SaaS analytics platform adoption (platform selection required as a dependent decision — see sequencing rationale below). Cognos migration must not begin data cutover until Workstream B pipelines are validated as stable, to avoid migrating analytics consumers onto a broken data layer.

**Sequencing constraint:** Workstream A gates Workstreams B and C. Workstream B gates Cognos data cutover in Workstream C. Platform evaluation and SaaS analytics adoption activities in Workstream C may proceed in parallel with Workstream A and early Workstream B without dependency conflict.

This decision rejects Option 1 (lift-and-shift) because it does not satisfy the decentralisation capability intent and produces a cloud Integrity Gap from day one. It rejects Option 3 (sequential infrastructure-first) because the extended timeline maximises accumulated risk across all three deprecated platforms simultaneously. It rejects Option 5 (Cognos-first) because it creates a decentralised analytics layer dependent on a deprecated and unresolved data integration layer — producing visible business value that rests on a structurally unsound foundation.

---

## Consequences

### What Is Gained

- **Elimination of all three deprecated platforms within a single programme arc**, removing compounding security, compliance, and vendor risk.
- **Cloud-native capability model** realised across data integration, analytics, and compute — consistent with the enterprise's decentralisation intent.
- **Reduction of Integrity Gap** across the estate: the architecture description and the actual operational state converge, restoring Velocity of Truth.
- **Decentralised analytics access** for business units, removing Cognos as a central bottleneck to reporting and insight.
- **Modern data integration patterns** (cloud-native ELT) enabling downstream data product and data mesh evolution not possible within DataStage's architectural constraints.
- **VMware cost exposure resolved**: post-Broadcom licensing changes introduce commercial risk that this decision eliminates within the programme horizon.

### What Is Accepted as Cost

- **Front-loaded delivery complexity**: three parallel workstreams require programme governance discipline, clear workstream ownership, and dependency management that is harder than sequential delivery.
- **Short-term team capacity pressure**: parallel execution demands simultaneous cloud, data engineering, and analytics skills — a skills gap assessment is a mandatory first action.
- **Cognos reporting continuity risk during transition**: business units will experience a period where Cognos reports are being decommissioned before SaaS analytics equivalents are fully validated. A parallel-run period must be costed and planned.
- **DataStage pipeline re-development effort**: DataStage jobs are rarely lift-and-shift compatible with cloud-native ELT paradigms. Pipeline re-development carries discovery risk — actual pipeline inventory and complexity must be assessed before cost estimates are credible.
- **Platform selection decisions remain open**: both the cloud-native data integration platform and the SaaS analytics platform require dedicated selection decisions (dependent Trade-off Matrices, to be produced as immediate next actions). This matrix does not pre-determine those selections.
- **Decision Latency cost already incurred**: the organisation has operated on deprecated platforms during a period in which cloud capability could have been established. This programme must absorb the accumulated technical debt of that latency.

---

## Sequencing Rationale

The sequence embedded in this decision is not arbitrary. It reflects three principles from the VAF Foundation Layer:

**1. Resolve infrastructure before adding application load.**
Cloud compute foundation (Workstream A) must be established before data integration and analytics workloads migrate onto it. Migrating DataStage pipelines to cloud infrastructure that is still being stabilised creates compounding failure modes. The infrastructure layer is the substrate; its stability gates everything above it.

**2. Resolve data before resolving presentation.**
Cognos is a reporting and analytics presentation layer. Its value to business consumers is entirely dependent on the quality and availability of the data pipelines beneath it. Migrating Cognos consumers to SaaS analytics before DataStage pipelines are replaced and validated is an architectural inversion — it produces the appearance of modernisation while leaving the underlying data capability in a deprecated state. The Integrity Gap does not close; it relocates.

**3. Evaluate and select before committing to build.**
Two platform selection decisions (cloud-native data integration and SaaS analytics) are immediate dependencies of this programme. They must not be defaulted by inertia or pre-existing vendor relationships. Each must be resolved through a time-boxed evaluation (maximum 6 weeks per platform) producing a dedicated Trade-off Matrix. The 14-Day Decision Aging Rule (CR-E1) applies: if either selection decision exceeds 14 days without binding resolution, mandatory escalation is triggered.

**Investment sequencing implication:** Workstream A requires the earliest capital commitment (cloud infrastructure, networking, identity). Workstreams B and C follow with operational expenditure (platform licences, engineering effort, training). The programme should not attempt to finalise the full multi-year investment profile before platform selections are made — doing so will produce numbers that do not survive contact with vendor and implementation reality.

---

## Investment Profile

> *Note: No budget constraints were declared for this decision. The following profiles are indicative relative weightings to inform governance prioritisation. Validated cost estimates require platform selection decisions, pipeline inventory assessment, and cloud infrastructure sizing — all of which are immediate programme actions.*

| Workstream | Relative Effort | Capital Profile | Risk Profile | Key Cost Driver |
|------------|----------------|-----------------|--------------|-----------------|
| **Workstream A — VMware Exit** | High | Front-loaded (cloud infra commitment) | Medium | Infrastructure estate size; network re-architecture complexity; workload compatibility assessment |
| **Workstream B — DataStage Replacement** | Very High | Sustained over pipeline re-development cycle | High | DataStage job inventory depth; data quality remediation; cloud-native skills gap |
| **Workstream C — Cognos Exit** | Medium | Phased (SaaS licences + parallel-run period) | Medium | Report inventory complexity; business unit change management; parallel-run operational cost |
| **Programme Governance** | Medium | Sustained (PMO, architecture governance, dependency management) | Medium | Programme management maturity; workstream dependency coordination overhead |

**Total programme risk posture:** Medium-High. The primary risk is not technical — cloud-native replacements for all three platforms are mature and well-evidenced in the market. The primary risk is **delivery sequencing discipline**: the temptation to allow Workstream C (the most visible to business stakeholders) to race ahead of Workstream B (the structurally necessary prerequisite) must be actively governed against.

---

## Dependent Decisions Required

The following Trade-off Matrices must be produced as immediate programme actions. Each carries a 14-day Decision Aging clock from the date this matrix is ratified (CR-E1).

| Decision | Type | Priority | Dependency |
|----------|------|----------|------------|
| Cloud-native data integration platform selection (DataStage replacement) | TOM — VP2 | Immediate | Workstream B cannot proceed to build without this decision |
| SaaS analytics platform selection (Cognos replacement) | TOM — VP2 | Immediate | Workstream C platform adoption cannot proceed without this decision |
| Cloud hyperscaler and landing zone architecture | TOM — VP2 | Immediate | Workstream A compute foundation requires committed hyperscaler direction |
| VMware workload prioritisation and migration wave sequencing | TOM — VP2 | Near-term | Workstream A execution requires workload classification before migration ordering |

---

## Owner

*\[Single named owner to be assigned per CR-O1. No committee ownership is permitted. The owner is accountable for driving dependent decisions to resolution within the 14-day aging window.\]*

---

## Date

2026-01-15

---

## Supersedes

N/A — first decision of record for this programme.

---

*Velocity Architecture Framework™ v1.0 | VP2 — Decision Viewpoint | TOM-20260115-002*
*© 2026 Phil Myint / ZenCloud Global Consultants. All rights reserved.*
*ISO/IEC/IEEE 42010:2022 Conformant | github.com/ZenCloudAU/velocity-architecture*