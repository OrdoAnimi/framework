# Worked Example: Architecture Decision Log (ADL)

**The OrdoAnimi Framework — Examples**

> **Scenario:** CloudFirst Banking — Core Platform Modernisation
> **Snapshot date:** 2026-02-11 (end of Week 7)
> **ADL owner:** S. Rajan (Solution Architect, S2)
> **Governing Canvas:** GC-20260101-001

This example shows a populated ADL index at the close of the onboarding period and into delivery. The ADL is the living spine of all architectural decisions (VP4). It indexes decisions by ID; it does not contain the full text of each artefact — ADRs live in the codebase (VP3), Canvases and Matrices in the Vault (VP4).

---

# ADL/INDEX.md
**CloudFirst Banking — Core Platform Modernisation**
**Maintained by:** S. Rajan | **Last updated:** 2026-02-11

---

## Enterprise Layer — Guardrail Canvases (VP1)

| ID | Title | Owner | Status | Expiry / Review | Governed TOMs |
|----|-------|-------|--------|-----------------|---------------|
| GC-20260101-001 | Enterprise constraints — CloudFirst Core Modernisation | D. Nguyen (S5) | Active | 2026-07-14 (CR-X3) | TOM-20260115-001, TOM-20260115-002 |

**Constraint summary (GC-20260101-001):**
1. No vendor lock-in above hyperscaler level
2. All data must remain within Australian sovereign boundaries (APL data class)
3. Core banking system (Temenos T24) is out of scope for this engagement
4. Budget envelope: $4.2M. No budget increase authority below CTO (S5).
5. Go-live: 2026-08-31. Date is hard — not negotiable.

---

## Solution Layer — Trade-off Matrices (VP2)

| ID | Question decided | Owner | Status | Governing Canvas | Date decided | ADR |
|----|-----------------|-------|--------|-----------------|--------------|-----|
| TOM-20260115-001 | Integration layer: event-driven vs REST for core-to-channel | P. Walsh (S3) | Decided | GC-20260101-001 | 2026-02-06 | ADR-004 |
| TOM-20260115-002 | API gateway: managed service (AWS) vs custom-built | P. Walsh (S3) | Decided | GC-20260101-001 | 2026-02-11 | ADR-007 (pending) |
| TOM-20260204-001 | Audit log retention: 7-year vs 10-year requirement | M. Osei (S2) | Open | GC-20260101-001 | — | — |

### Open TOM notes

**TOM-20260204-001** — Decision owner: M. Osei. Opened: 2026-02-04. Expiry: 2026-02-18 (day 14). Status: awaiting regulatory reference from compliance. If unresolved by 2026-02-18, CR-E1 activates.

---

## Technical Layer — Architecture Decision Records (VP3)

ADRs are stored in the codebase at `decisions/`. This index records status and cross-references; full text is in the codebase.

| ADR | Title | Owner | Status | Governs | Date |
|-----|-------|-------|--------|---------|------|
| ADR-001 | Cloud platform selection — AWS primary, Azure secondary | D. Nguyen (S5) | Accepted | GC-20260101-001, TOM-20260115-001 | 2026-01-21 |
| ADR-002 | Identity provider — Azure AD B2C (retained from existing estate) | T. Clarke (S1) | Accepted | GC-20260101-001 | 2026-01-23 |
| ADR-003 | Network architecture — hub-and-spoke VPC with transit gateway | P. Walsh (S3) | Accepted | ADR-001 | 2026-01-28 |
| ADR-004 | Integration layer — event-driven (Kafka on MSK) for core-to-channel | P. Walsh (S3) | Accepted | TOM-20260115-001 | 2026-02-06 |
| ADR-005 | Data sovereignty boundaries for cross-border transaction data | T. Clarke (S1) | Open — Expiry 2026-02-12 | GC-20260101-001 | — |
| ADR-006 | Audit log retention period | M. Osei (S2) | Open — Expiry 2026-02-18 | TOM-20260204-001 | — |
| ADR-007 | API gateway — AWS API Gateway (managed) | P. Walsh (S3) | Draft — author by 2026-02-13 | TOM-20260115-002 | — |

### ADR–ADL relationship note

ADRs are the technical-layer decision record, authored and versioned in the codebase (VP3). This ADL index records the ADR's status and cross-references to its governing TOM and Canvas — it does not duplicate the ADR content. When an ADR is superseded, the original is retained; a new ADR is created with a `Supersedes: ADR-NNN` reference (CR-T3). The supersession is recorded in the Velocity Vault (VP4/Vault).

---

## Superseded Decisions

| Artefact | Title | Superseded by | Date |
|----------|-------|---------------|------|
| — | — | — | — |

*No superseded decisions at Week 7.*

---

## Risk Register

| Risk ID | Description | Likelihood | Impact | Owner | Status |
|---------|-------------|-----------|--------|-------|--------|
| RISK-001 | Compliance sign-off delay → ADR-005 cascades to integration design | High | High | T. Clarke (S1) | Active |
| RISK-002 | API gateway delay blocks infrastructure sprint | Medium | High | P. Walsh (S3) | Closed (2026-02-11, TOM-20260115-002 decided) |
| RISK-003 | FF-005 latency threshold failing under load | Low | Medium | P. Walsh (S3) | Active — spike in progress |

---

## Fitness Function Register

Full definitions in `decisions/fitness-functions/`. This table shows current status only.

| ID | Function | ADR | Threshold | Status | Last tested |
|----|----------|-----|-----------|--------|-------------|
| FF-001 | API response p95 < 200ms | ADR-004 | <200ms | ✅ Pass | 2026-02-10 |
| FF-002 | Event delivery ≥99.99% | ADR-004 | ≥99.99% | ✅ Pass | 2026-02-10 |
| FF-003 | Zero cross-region data residency violations | ADR-005 | 0 | ✅ Pass | 2026-02-10 |
| FF-004 | Event throughput >10k msg/sec at p99 | ADR-004 | >10,000 | ⬜ Pending | — |
| FF-005 | End-to-end latency <500ms @ 10k concurrent | ADR-003 | <500ms | ❌ Fail | 2026-02-09 |
| FF-006 | Audit log write success >99.99% | ADR-006 | >99.99% | ✅ Pass | 2026-02-10 |
| FF-007 | Zero unencrypted data at rest | ADR-001 | 0 | ✅ Pass | 2026-02-10 |
| FF-008 | DR RTO <4hrs | ADR-003 | <4hrs | ✅ Pass | 2026-02-07 |
| FF-009 | Build pipeline success >95% | ADR-001 | >95% | ✅ Pass | 2026-02-11 |

---

## Velocity Dashboard Snapshot — Week 7

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Open decisions | 4 | <5 | ✅ |
| Decisions aged >14 days | 0 | 0 | ✅ |
| Escalations active | 0 | — | ✅ |
| Fitness functions failing | 1 | 0 | ⚠ |
| Next CR-E1 trigger | ADR-005 (2026-02-12) | — | ⚠ Monitor |

---

## Pulse Log

| Date | Tier | Key decisions | Escalations | Report |
|------|------|--------------|-------------|--------|
| 2026-01-21 | Tier 1 | ADR-001 confirmed | — | Pulse Report 2026-01-21 |
| 2026-01-28 | Tier 1 | ADR-002, ADR-003 confirmed | — | Pulse Report 2026-01-28 |
| 2026-02-04 | Tier 1 | TOM-20260115-001 opened | — | Pulse Report 2026-02-04 |
| 2026-02-06 | Ad hoc | ADR-004 confirmed (binding session) | — | Pulse Report 2026-02-06 |
| 2026-02-11 | Tier 1 | TOM-20260115-002 confirmed | ADR-005 pending expiry | `examples/pulse-report-example.md` |

---

*ADL/INDEX.md — CloudFirst Banking Core Platform Modernisation*
*The OrdoAnimi Framework | © 2026 Phil Myint / OrdoAnimi*
*For ADL template, see: `viewpoints/vp4-velocity/adl-template.md`*
