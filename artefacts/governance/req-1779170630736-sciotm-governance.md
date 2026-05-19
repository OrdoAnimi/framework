# Guardrail Canvas — VP1

**GC-20260101-002 | DataStage, Cognos, and VMware Deprecated Platform to Cloud Migration Programme**

---

## Canvas Identification

| Field | Value |
|-------|-------|
| **Canvas ID** | GC-20260101-002 |
| **Organisation / Domain / Period** | Enterprise Architecture — Data and Compute Platform Modernisation — FY2026 |
| **Owner** | [Enterprise Architect — Name Required] |
| **Status** | Active |
| **Review Date** | [Insert date — mandatory; canvas is inactive without this field] |
| **Supersedes** | N/A |

> ⚠️ **Incomplete Canvas Warning:** Owner name and Review Date are missing from the provided context. This canvas is provisionally structured but cannot be declared Active until both fields are populated by the named authority. Per CR-X3, a canvas without a Review Date is inactive. Per CR-O1, a canvas without a named owner has no binding force.

---

## Core Optimisation

We prioritise **platform decommission velocity and cloud capability establishment** over **feature parity with legacy systems and cost minimisation** when trade-offs are required.

*Rationale: DataStage, Cognos, and VMware have reached or are approaching vendor end-of-life or deprecated support status. Continued operation on these platforms compounds the Integrity Gap — the divergence between documented architecture and the actual state of the enterprise. Every month of deferred migration increases Governance Drag: undocumented workarounds, informal support arrangements, and shadow integrations accumulate faster than they are retired. The cost of delay is not linear; it is compounding. Cloud capability establishment is the primary concern. Cost optimisation is a second-order concern.*

---

## Non-Negotiables

- **Platform sunset:** DataStage, Cognos, and VMware workloads must have a declared migration or decommission decision for every identified workload before any new capability investment is approved on the legacy stack. No net-new development on deprecated platforms.
- **Capability model primacy:** All cloud platform decisions must be traceable to an approved capability model. No cloud service is adopted without a declared capability owner and a mapped capability domain. Undeclared capability adoption is a governance violation.
- **Decentralisation boundary:** Decentralisation of on-premises workloads does not mean ungoverned distribution. Every decentralised capability must carry a named domain owner, a stated data classification, and a defined integration contract. Decentralisation without boundary definition produces uncontrolled Integrity Gap expansion.
- **Data residency:** Data residency and sovereignty constraints inherited from the legacy environment carry forward to the cloud environment unchanged unless explicitly reviewed and approved by the named compliance authority.
- **Decision traceability:** Every platform selection decision (replacement for DataStage ETL, Cognos reporting, VMware compute) must be recorded as a Trade-off Matrix entry referencing this canvas (CR-T1). No verbal or informal platform selections are architecturally binding.
- **Decommission confirmation:** A workload is not considered migrated until the legacy instance is decommissioned and confirmed removed. Migration without decommission is duplication, not transformation.

---

## Explicit Trade-offs

| Tension | Our Position | Rationale |
|---------|-------------|-----------|
| **Lift-and-shift vs Re-architect** | Re-architect where capability model demands it; lift-and-shift only as a time-bounded transitional state with a declared re-architecture date | Lifting and shifting a deprecated workload to cloud without re-architecture transfers technical debt to the cloud estate. Transitional lift-and-shift is permitted only with a binding sunset date recorded in the ADL. |
| **Centralised ETL (DataStage pattern) vs Decentralised data platform** | Decentralised by capability domain, with a shared integration contract standard | The DataStage centralised ETL pattern is not replicated in the target architecture. Each capability domain owns its data pipelines. Shared standards — not shared infrastructure — provide coherence. |
| **Monolithic BI (Cognos pattern) vs Federated reporting** | Federated reporting aligned to capability domains, with a governed semantic layer | Cognos replacement is not a like-for-like tool swap. Reporting authority decentralises to capability owners. A common semantic/metrics layer enforces definitional consistency without centralising delivery. |
| **VMware private compute vs Cloud-native compute** | Cloud-native for net-new; VMware workloads migrate to managed compute services, not cloud-hosted VMs | Rehosting VMware to cloud-hosted VMs is not cloud adoption. It is infrastructure cost transfer. Cloud-native compute services are the target state. Exceptions require Trade-off Matrix entries. |
| **Speed of migration vs Stability of production** | Stability of production-critical workloads; velocity on non-critical workloads | Migration sequencing is governed by workload criticality. Revenue or compliance-critical workloads are migrated with full parallel-run validation. Non-critical workloads are migrated at maximum velocity. |
| **Decentralisation vs Governance coherence** | Decentralisation of delivery; centralisation of standards | Domain teams own their platforms and pipelines. The enterprise retains authority over integration contracts, data classification standards, security baselines, and capability model alignment. These are not negotiable at the domain level. |
| **Cost of cloud vs Cost of legacy maintenance** | Legacy maintenance cost is not the floor for cloud cost comparisons | Cloud cost comparisons must include the full cost of legacy: vendor support, internal operational overhead, risk of unplanned failure, and the cost of the Integrity Gap. Cloud cost optimisation is pursued post-stabilisation, not as a precondition for migration. |

---

## Decision Authority

| Decision Class | Authority | Escalation Path | Binding Mechanism |
|----------------|-----------|-----------------|-------------------|
| **Platform selection (replacement for DataStage, Cognos, VMware)** | Enterprise Architect | Architecture Review Board (ARB) | Trade-off Matrix entry referencing this canvas |
| **Capability domain boundary definition** | Enterprise Architect with Domain Owner co-sign | Programme Steering Committee | Capability Model artefact — formally versioned |
| **Decentralisation boundary approval** | Architecture Review Board | CIO / CTO | ARB decision record |
| **Data residency exception** | CIO / CTO + Compliance Authority | Board | Formal exception register entry with signed approval |
| **Lift-and-shift transitional approval (with sunset date)** | Enterprise Architect | ARB | Trade-off Matrix entry with mandatory sunset date field |
| **Net-new cloud service adoption** | Domain Architect with capability model reference | Enterprise Architect | ADR referencing Trade-off Matrix and this canvas (CR-T1, CR-T2) |
| **Decommission confirmation** | Domain Owner + Enterprise Architect joint sign-off | Programme Director | Decommission record in ADL |
| **Revisitation of any canvas constraint** | Enterprise Architect initiates; ARB decides | CIO / CTO | New canvas version; this canvas superseded with CR-T3 reference |

> **Decision Latency Rule (CR-E1):** Any platform selection, capability boundary, or decommission decision open for more than 14 calendar days without binding resolution triggers mandatory escalation to the next authority level. Decision latency on this programme is the primary risk to achieving decommission velocity.

---

## Governance Drag Analysis

The following are identified sources of Governance Drag on this programme — implicit decision points, informal authority, and structural ambiguities that will slow the Velocity of Truth if not made explicit.

| Drag Source | Description | Remediation |
|-------------|-------------|-------------|
| **Undefined capability domain ownership** | If capability domains are not formally bounded and owned before cloud platform decisions are made, platform selections will be made by infrastructure teams without capability context. This produces the wrong cloud architecture. | Define and publish capability model with named domain owners before any platform RFP or selection process begins. |
| **Informal DataStage workload inventory** | If the full inventory of DataStage jobs, dependencies, and downstream consumers is not formally documented, migration decisions will be made on incomplete information. Undocumented jobs will be discovered post-migration and re-open closed decisions. | Mandate a formal DataStage workload census as a gate-zero artefact. No migration planning begins without it. |
| **Cognos report ownership ambiguity** | Cognos report catalogues are typically large, undocumented, and informally owned. Without formal ownership, every report becomes a potential escalation point during decommission. | Conduct a Cognos report rationalisation exercise: catalogue, classify (active / redundant / unknown), and assign a named business owner to every active report before migration. |
| **VMware workload classification** | VMware hosts an undifferentiated mix of workloads across criticality tiers. Without a formal criticality classification, migration sequencing defaults to technical convenience rather than business risk management. | Classify all VMware workloads by criticality tier before migration sequencing begins. Tier 1 workloads require parallel-run validation plans. |
| **Decentralisation without integration contracts** | Decentralising platforms to domain teams without declared integration contracts produces immediate integration inconsistency. The Integrity Gap widens from day one of decentralisation. | Establish integration contract standards (API, event, file) before the first decentralised domain platform goes live. Standards are non-negotiable at the domain level (see Non-Negotiables above). |
| **Cloud cost governance absence** | Cloud native consumption models produce unexpected cost outcomes when domain teams provision independently without financial guardrails. | Establish cloud cost governance (tagging standards, budget alerts, FinOps ownership) before domain teams are granted independent provisioning rights. |
| **Parallel operation period governance** | During migration, legacy and cloud platforms will operate in parallel. Without a formal parallel operation governance model, operational teams will indefinitely defer decommission decisions. | Define a maximum parallel operation window per workload class. Parallel operation beyond this window is a governance escalation trigger. |

---

## Altitude Collapse Risk

> **Altitude Collapse** is the condition in which enterprise-level strategic intent is displaced by operational-level concerns, producing delivery outcomes that are locally rational but strategically incoherent.

The following altitude collapse risks are identified for this programme:

| Risk | Description | Signal | Mitigation |
|------|-------------|--------|------------|
| **Tool-first platform selection** | Teams select cloud-native replacements for DataStage, Cognos, and VMware based on vendor familiarity or market position rather than capability model requirements. Strategic intent (capability decentralisation) is displaced by procurement convenience. | RFPs issued before capability model is finalised. Platform selections made at project level without ARB review. | Enforce capability model gate before any platform selection begins. ARB review is mandatory for all three platform replacement decisions. |
| **Migration mistaken for transformation** | Lift-and-shift of DataStage jobs, Cognos reports, and VMware VMs to cloud is declared as programme success. The capability model is not implemented. The Integrity Gap transfers intact to the cloud estate. | Migration velocity metrics used as primary programme KPIs. Decommission confirmed without re-architecture review. | Track capability model adoption as a primary KPI alongside migration count. Lift-and-shift workloads are explicitly flagged as incomplete until re-architecture is confirmed. |
| **Decentralisation as a cost-cutting exercise** | Decentralisation of on-premises platforms is pursued primarily to reduce central IT costs. Domain teams receive platforms without capability model alignment, governance standards, or integration contracts. | Domain teams provisioning cloud services without ARB visibility. Integration contract standard not established. | Maintain ARB visibility of all domain-level platform adoption. Cost reduction is a second-order outcome, not the primary driver (see Core Optimisation). |
| **Legacy decommission deferral** | Operational risk aversion produces indefinite parallel operation of legacy and cloud platforms. The programme achieves cloud adoption without legacy decommission. The organisation pays for both indefinitely. | Parallel operation windows not defined. Decommission decisions repeatedly reopened after closure. | Apply CR-E1 (14-Day Decision Aging Rule) to decommission decisions. Parallel operation windows are declared at migration initiation and enforced by the programme governance authority. |
| **Compliance assumption inheritance** | Teams assume that compliance posture from the legacy VMware environment (network segmentation, access controls, audit logging) automatically transfers to cloud. Cloud-native environments require explicit compliance re-establishment. | No cloud compliance baseline established. Security architecture not engaged at programme initiation. | Establish cloud compliance baseline (referencing applicable regulatory and internal standards) as a gate-zero artefact. No workload migrates without a declared compliance mapping. |

---

## VAF Concept Application

| VAF Concept | Application to This Programme |
|-------------|-------------------------------|
| **Integrity Gap** | The DataStage, Cognos, and VMware platforms represent an accumulated Integrity Gap — the divergence between the architecture the organisation believes it has and the architecture it actually operates. Shadow integrations, undocumented DataStage jobs, and informal VMware configurations are the primary manifestations. This programme must close the Integrity Gap, not transfer it to the cloud estate. |
| **Decision Latency** | The deprecation of these three platforms is not a new constraint. Organisations that have not yet made binding migration decisions have accumulated Decision Latency. Every month of continued Decision Latency increases migration complexity, vendor risk, and the cost of the eventual transition. This canvas establishes a decision boundary: no new capability investment on deprecated platforms. |
| **Velocity of Truth** | The rate at which the organisation's understanding of its workload inventory, capability ownership, and platform dependencies updates to match reality. Current Velocity of Truth on this programme is assumed to be low — the workload census, Cognos report catalogue, and capability domain boundaries are likely undocumented or informally maintained. Increasing Velocity of Truth is the prerequisite for all migration decisions. |
| **Governance Drag** | Identified above. The primary sources are undefined capability ownership, informal workload inventories, and the absence of integration contract standards. These are structural drag sources that will not resolve without explicit organisational intervention. |
| **Control Paradox** | The risk on this programme is that governance processes designed to manage migration risk instead produce the illusion of control: status reports, migration trackers, and steering committee presentations that do not reflect actual workload complexity or integration risk. The antidote is artefact-based governance — every decision is a Trade-off Matrix entry; every migration is a confirmed decommission. |

---

## Compliance Mappings

> **Note:** No specific regulatory or standards constraints were provided in the programme context. The following mappings represent the minimum compliance considerations applicable to a programme of this type. They must be reviewed and confirmed against the organisation's actual compliance obligations by the named compliance authority before this canvas is declared Active.

| Compliance Domain | Applicable Consideration | Required Action |
|-------------------|--------------------------|-----------------|
| **Data sovereignty** | Cloud migration of data workloads (DataStage, Cognos) must confirm data residency compliance. Data that was resident in on-premises infrastructure does not automatically satisfy residency requirements in cloud. | Confirm applicable data residency obligations. Declare cloud regions as compliant or non-compliant before workload migration. Record as a Non-Negotiable or canvas exception. |
| **Access control and identity** | VMware environments typically operate with on-premises identity (Active Directory, local accounts). Cloud-native identity models differ materially. Access control must be re-established, not assumed to transfer. | Establish cloud identity and access management baseline before first workload migration. No workload migrates without declared access control mapping. |
| **Audit and logging** | Regulatory and internal audit requirements for data processing (satisfied by DataStage) and reporting (satisfied by Cognos) must be re-established in the replacement platforms. | Confirm audit logging requirements for all workloads. Declare compliance mapping for replacement platforms before decommission of legacy systems. |
| **Vendor risk** | Engaging new cloud-native vendors (replacing DataStage, Cognos, VMware) introduces vendor risk that must be assessed. Sole-source dependency on a single cloud provider for all three replacements is a concentration risk. | Conduct vendor risk assessment for each platform replacement. Sole-source cloud provider dependency requires explicit Trade-off Matrix entry and ARB approval. |
| **Change management** | Decentralisation of platforms to domain teams materially changes the operational and support model. Change management obligations (internal policy, employment agreements, service agreements) must be assessed. | Engage HR, Legal, and Service Management before decentralisation model is communicated to domain teams. |

---

## Analytic Test

*Did this canvas remove a debate from a portfolio or funding discussion?*

This canvas removes the following debates:

1. **"Should we stay on DataStage / Cognos / VMware?"** — No. Deprecated platforms receive no net-new investment. This is not a discussion point.
2. **"Should we lift-and-shift or re-architect?"** — Lift-and-shift is a time-bounded transitional state only. Re-architecture to the capability model is the required end state. The debate is about timing, not direction.
3. **"Who decides which cloud platform replaces DataStage?"** — The Enterprise Architect, with a Trade-off Matrix entry referencing this canvas, subject to ARB review.
4. **"Can we decentralise without integration standards?"** — No. Integration contracts are a Non-Negotiable. This is not a discussion point.
5. **"Is the programme complete when workloads are in the cloud?"** — No. The programme is complete when legacy platforms are decommissioned and confirmed removed, and when capability domain ownership is established and operating.

---