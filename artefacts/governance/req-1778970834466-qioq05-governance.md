# Guardrail Canvas — Capability Model

**GC-20260601-001 | NGO Healthcare — Infrastructure Capability Consolidation Programme**

---

## Canvas Identification

| Field | Value |
|-------|-------|
| **Canvas ID** | GC-20260601-001 |
| **Organisation / Domain / Period** | NGO Healthcare — Infrastructure Capability Model — FY2026–2028 |
| **Owner** | *[Enterprise Architect — Named Individual Required: CR-O1 not satisfied until named]* |
| **Status** | Active |
| **Review Date** | 2026-12-01 |
| **Supersedes** | N/A |

---

## Core Optimisation

We prioritise **patient data continuity and platform stability across all 200 sites** over **infrastructure modernisation velocity and cost reduction** when trade-offs are required.

*Rationale: 20,000 users across distributed care delivery sites depend on platform availability for clinical and administrative operations. VMware platform aging has created a compounding Integrity Gap — the gap between documented capability and operational reality widens with every deferred remediation cycle. Consolidation to 2–3 geolocation-aligned data centres is a structural prerequisite for closing that gap. No modernisation programme that sacrifices continuity during transition is acceptable.*

---

## Non-Negotiables

- **Regulatory compliance:** All production systems must comply with the Australian Privacy Act 1988 (Privacy Act), the My Health Records Act 2012, and applicable state health records legislation — without exception or deferral
- **Data sovereignty:** All patient and clinical data must remain within Australian jurisdiction at all times — no offshore replication, no cross-border routing, no exception below Executive and Board sign-off
- **Clinical continuity:** No site may experience unplanned downtime exceeding 4 hours for any clinical-facing system during the consolidation programme — violation triggers immediate programme pause and root cause review
- **Identity and access:** Role-based access control aligned to clinical role definitions must be enforced at platform level before any site is migrated — no migration proceeds without verified access governance in the target environment
- **Essential Eight:** Minimum Maturity Level 2 across all production systems in scope — any system failing this threshold is flagged as migration-blocked until remediated
- **Vendor independence:** No hypervisor or DC hosting contract may be signed as sole-source above $500k/year without an approved exit strategy and Board-ratified justification

---

## Explicit Trade-offs

| Tension | Our Position | Rationale |
|---------|-------------|-----------|
| Migration velocity vs. site stability | Site stability | 200 sites carry uneven risk profiles; velocity that destabilises clinical operations is inadmissible |
| Consolidation scope vs. transition risk | Phased consolidation (2–3 DCs, sequenced by risk tier) | Full simultaneous migration creates an unacceptable continuity exposure across the user base |
| Cost reduction vs. platform resilience | Platform resilience for Tier 1 clinical; cost optimisation for Tier 2–3 administrative | Clinical system downtime cost exceeds hosting cost at all tiers |
| VMware retention vs. hypervisor modernisation | Controlled exit from VMware — no forced renegotiation under duress | Broadcom licensing trajectory makes VMware retention a strategic liability; exit must be planned, not reactive |
| Centralised DC vs. distributed edge | Centralised DC with defined edge exceptions for sites with connectivity constraints | Connectivity to 200 sites is not uniform — edge exceptions require documented justification per site |
| Build vs. Buy for platform capability | Buy for commodity infrastructure; build only where clinical workflow integration requires it | This organisation is not a platform engineering business |
| Innovation vs. stability during consolidation | Stability across the consolidation window | No net-new capability work is authorised that consumes consolidation programme capacity |

---

## Decision Authority

> *Altitude Collapse Risk: HIGH. Without explicit authority mapping, operational teams will make platform decisions that belong at enterprise level. VMware exit and DC geolocation decisions have already been observed drifting to infrastructure leads without executive ratification. This canvas arrests that drift.*

| Decision Domain | Authority | Escalation Path | Binding Threshold |
|----------------|-----------|-----------------|-------------------|
| DC geolocation selection (2–3 sites) | Executive Leadership + Board ratification | CEO → Board | Any commitment to DC lease or hosting contract |
| VMware exit strategy and timeline | Enterprise Architect + CTO/CIO | CTO/CIO → Executive | Any decision that modifies VMware contract terms |
| Site migration sequencing and risk tiering | Enterprise Architect | EA → CTO/CIO | Any change to phasing that affects Tier 1 clinical sites |
| Platform hypervisor selection | CTO/CIO with EA recommendation | CTO/CIO → Executive | Binding procurement decision |
| Clinical system downtime exception | Clinical Operations Lead + CTO/CIO joint authority | Both must agree; no unilateral exception | Any planned outage window for clinical-facing systems |
| Vendor contracts > $500k/year | CFO + CTO/CIO + Board Audit | CFO → Board | Contract execution |
| Essential Eight compliance deferral | CTO/CIO | CTO/CIO → Executive + Board Audit notification | Any deferral, no matter the duration |
| Edge site exception to DC consolidation | Enterprise Architect | EA → CTO/CIO | Any site not migrating to the consolidated DC model |

---

## Governance Drag Analysis

> *Governance Drag: the friction created by governance structures that slow decisions without adding clarity or reducing risk. Identified drag is a programme risk, not a governance success.*

| Drag Source | Classification | Impact | Resolution |
|------------|---------------|--------|------------|
| VMware contract renegotiation deferred pending strategy clarity | **Decision Latency** | Broadcom licensing costs accrue; exit window narrows with each deferral cycle | Enterprise Architect must produce a platform exit decision within 14 days of this canvas activation (CR-E1) |
| DC geolocation under informal discussion without binding authority | **Altitude Collapse** | Infrastructure leads are scoping DC options without executive mandate — creates sunk cost and false commitment | Geolocation decision must be escalated to Executive within this programme cycle with a declared terminal condition (CR-E3) |
| Site migration sequencing undocumented | **Integrity Gap** | 200 sites with uneven clinical risk profiles; without a documented risk tier, every site is implicitly treated as equal — which is false | Risk tiering matrix required as a VP2 Trade-off Matrix artefact before any migration begins |
| Essential Eight compliance status unknown across 200 sites | **Integrity Gap** | Compliance posture is undeclared; migration of non-compliant systems into a consolidated DC compounds the risk surface | Compliance baseline assessment is a migration gate — not a parallel workstream |
| Identity and access governance not validated pre-migration | **Decision Latency** | RBAC for clinical roles has not been confirmed in the target environment; migration without this creates a clinical safety and privacy exposure | Access governance validation is a hard gate; no site migration proceeds without it |
| No defined Pulse cycle for programme governance | **Governance Drag** | Without a cadenced decision forum, open decisions will age beyond 14 days routinely (CR-E1 violation) | A Pulse governance cycle must be established within 30 days of programme initiation |

---

## Compliance Mappings

> *All compliance obligations are non-negotiable. They are not risk acceptance candidates. They are migration gates.*

| Obligation | Instrument | Scope | Migration Gate? |
|-----------|-----------|-------|----------------|
| Australian Privacy Act 1988 — APP 8 (cross-border) | Federal legislation | All patient data, all systems, all sites | **Yes — hard gate** |
| My Health Records Act 2012 | Federal legislation | All systems interacting with My Health Record | **Yes — hard gate** |
| State health records legislation (jurisdiction-specific) | State legislation (VIC, NSW, QLD, WA, SA, TAS, ACT, NT as applicable) | All sites in relevant jurisdictions | **Yes — per site** |
| ACSC Essential Eight — Maturity Level 2 | ASD framework | All production systems | **Yes — hard gate** |
| ISO/IEC 27001 (if certified or in scope) | International standard | Confirm organisational scope | Confirm before DC selection |
| NHSX / ADHA Digital Health Standards | ADHA framework | All systems interoperating with national digital health infrastructure | Confirm per system before migration |
| NDIS data handling requirements | Federal — NDIS Act 2013 | If organisation delivers NDIS-funded services | Confirm organisational scope |
| Healthcare Identifier Service requirements | Federal — HI Act 2010 | All systems using IHI, HPI-I, HPI-O | Confirm per system |

---

## Altitude Collapse Risk Assessment

> *Altitude Collapse: the condition in which enterprise-level decisions are made at operational level without authority, or in which operational constraints are presented to executives as architectural decisions. Both are failures of governance discipline.*

| Risk | Type | Severity | Indicator | Countermeasure |
|------|------|----------|-----------|----------------|
| Infrastructure leads selecting DC geolocation without executive mandate | **Downward altitude collapse** | Critical | DC shortlisting in progress without a published authority decision | This canvas establishes geolocation as an Executive decision — any shortlist produced without a mandate is advisory only and carries no commitment |
| VMware exit framed as a procurement decision rather than a strategic capability decision | **Upward altitude collapse** | High | Procurement team engaging Broadcom/alternative vendors without EA-led platform strategy | VMware exit is a capability model decision — it must be resolved at VP1 before any vendor engagement binds the programme |
| Site migration sequencing driven by vendor availability rather than clinical risk tiering | **Downward altitude collapse** | High | Migration schedule shaped by DC provider readiness, not clinical risk | Clinical risk tiering owns sequencing — vendor availability is a constraint, not the driver |
| Compliance obligations treated as a post-migration audit activity | **Downward altitude collapse** | Critical | Essential Eight or Privacy Act compliance deferred to post-go-live review | Compliance is a migration gate at this canvas. Any team treating it as a post-migration activity is operating outside this governance framework |
| "Capability model" scoped as an IT asset inventory rather than an enterprise capability declaration | **Upward altitude collapse** | High | Programme team producing CMDB outputs and calling it a capability model | A capability model at VP1 declares what the organisation must be able to do, not what it currently owns. Asset inventory is a VP3 artefact |

---

## VAF Concept Application

| Concept | Application to This Programme |
|---------|-------------------------------|
| **Integrity Gap** | The gap between the documented VMware platform capability and its actual operational state has been accumulating across the consolidation deferral period. Every site operating on aging VMware infrastructure without a ratified exit plan widens this gap. The consolidation programme exists to close it — but closing it requires declaring the current state honestly, not optimistically. |
| **Decision Latency** | DC geolocation, VMware exit, and migration sequencing are all open decisions. None has a binding owner, a declared terminal condition, or a Pulse cycle to govern resolution. At the current rate, all three will exceed the 14-day aging threshold (CR-E1) before the programme has formally started. |
| **Velocity of Truth** | The rate at which the organisation's understanding of its 200-site infrastructure state updates to match reality is currently low. No compliance baseline exists. No risk tiering exists. The programme cannot move at architectural velocity until the Velocity of Truth is increased — which requires immediate baseline assessment, not deferred discovery. |
| **Governance Drag** | Three sources of Governance Drag are active: (1) informal DC geolocation discussions without binding authority, (2) VMware contract decisions deferred pending clarity that will not arrive without a decision, (3) absence of a Pulse cycle to force open decisions to closure. This drag is consuming programme time that does not exist — the VMware platform will not wait. |

---

## Canvas Activation Conditions

This canvas is **Active** upon:

1. Named owner confirmed (CR-O1 — currently unresolved)
2. Executive acknowledgement of decision authority table (required within 14 days of programme initiation)
3. Pulse governance cycle established (required within 30 days)
4. Compliance baseline assessment commissioned (required before any migration gate is opened)

This canvas is **invalid** if:
- The named owner field remains unpopulated beyond 14 days of programme initiation
- The Review Date passes without formal reaffirmation or supersession (CR-X3)
- A downstream Trade-off Matrix (VP2) is produced without reference to this canvas (CR-T1 violation)

---

## Open Decisions Requiring Immediate Resolution

> *These decisions are not deferred. They are aged. Each is subject to CR-E1.*

| Decision | Current State | Owner (Required) | Terminal Condition |
|----------|--------------|------------------|-------------------|
| DC geolocation — 2 or 3 sites, which regions | Open — informal discussion only | CTO/CIO → Executive | Executive ratification of geolocation before any DC contract engagement |
| VMware exit — timeline and target hypervisor platform | Open — no binding decision | Enterprise Architect + CTO/CIO | Published platform decision within 14 days of canvas activation |
| Site risk tiering for migration sequencing | Open — not commenced | Enterprise Architect | Risk tiering matrix (VP2) published before first site migration gate |
| Essential Eight baseline across 200 sites | Open — not assessed | CTO/CIO | Baseline assessment report commissioned within 30 days |

---

*Velocity Architecture Framework™ — VP1 Guardrail Canvas*
*GC-20260601-001 | NGO Healthcare Infrastructure Capability Consolidation*
*© 2026 Phil Myint / ZenCloud Global Consultants. All rights reserved.*
*ISO/IEC/IEEE 42010:2022 Conformant | VAF v1.0*
*github.com/ZenCloudAU/velocity-architecture*