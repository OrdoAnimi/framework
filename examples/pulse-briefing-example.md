# Worked Example: Pulse Briefing

**The OrdoAnimi Framework — Examples**

> **Scenario:** CloudFirst Banking — Core Platform Modernisation
> **Engagement:** Migrating core banking infrastructure to AWS. Current focus: integration layer architecture.
> **Pulse Tier:** Tier 1 (Weekly — Tuesday 10:00)
> **Session date:** 2026-02-11
> **Prepared by:** S. Rajan (Solution Architect, S2)
> **Owner authority:** D. Nguyen (CTO, S5)

---

# Pulse Briefing
**CloudFirst Banking — Core Platform Modernisation**
**Week 7 of 24 | Tier 1 Pulse | 2026-02-11**

---

## 1. Status at a Glance

| Dimension | Status | Note |
|-----------|--------|------|
| Decision velocity | ⚠ At risk | Two open items approaching 14-day trigger |
| Open decisions | 4 | 2 within expiry window |
| Confirmed this week | 1 | ADR-004 bound — event-driven integration confirmed |
| Escalations active | 0 | — |
| Fitness functions passing | 8/9 | 1 failing: latency threshold under load |

---

## 2. Decision Register — Open Items

### ADR-005: Data sovereignty boundaries for cross-border transaction data
**Owner:** T. Clarke (Enterprise Architect, S1)
**Opened:** 2026-01-29 | **Expiry:** 2026-02-12 (day 14 — CR-E1 triggers tomorrow)
**Status:** In progress — legal review received; compliance sign-off pending
**Blocking:** Data residency layer design cannot proceed without this decision
**Pulse action required:** T. Clarke to confirm compliance sign-off date today. If not confirmed, CR-E1 activates and this item escalates to D. Nguyen at next Tier 2 Pulse (2026-02-19).

---

### TOM-20260115-002: API gateway strategy — managed service vs custom
**Owner:** P. Walsh (Technical Architect, S3)
**Opened:** 2026-01-31 | **Expiry:** 2026-02-14 (day 14 in 3 days)
**Status:** Trade-off Matrix scored; options presented to delivery lead (S4). Awaiting binding decision.
**Blocking:** Three downstream services are waiting on this selection before infrastructure provisioning.
**Pulse action required:** P. Walsh to present final recommendation today. Decision to bind this session or formally escalate — no third option.

---

### ADR-006: Audit log retention — 7 years vs 10 years
**Owner:** M. Osei (Solution Architect, S2)
**Opened:** 2026-02-04 | **Expiry:** 2026-02-18
**Status:** Awaiting regulatory reference from compliance team. Risk if extended: storage cost model may need revision.
**Pulse action:** Monitor. Expiry in 7 days.

---

### GC-20260101-001: Enterprise constraint — no vendor lock-in above hyperscaler level
**Owner:** D. Nguyen (CTO, S5)
**Opened:** 2026-01-14 | **Expiry:** 2026-07-14 (Canvas review date — CR-X3)
**Status:** Active. Governing constraint for all current TOMs.
**Pulse action:** No action. Review date note recorded.

---

## 3. Decisions Confirmed This Session (Prior Week)

| Artefact | Decision | Owner | Date |
|----------|----------|-------|------|
| ADR-004 | Event-driven integration selected for core-to-channel layer (Kafka on MSK) | P. Walsh | 2026-02-06 |

**ADR-004 consequence:** delivery team can now proceed with Kafka cluster configuration. Infrastructure sprint unblocked. Fitness function FF-004 (event throughput >10k msg/sec at 99th percentile) activated against ADR-004.

---

## 4. Risk Register Snapshot

| Risk ID | Description | Likelihood | Impact | Owner | Action |
|---------|-------------|-----------|--------|-------|--------|
| RISK-001 | Compliance sign-off delay causes ADR-005 to cascade into integration design | High | High | T. Clarke | Escalation pre-authorised if delay exceeds 2026-02-12 |
| RISK-002 | API gateway decision delay blocks infrastructure sprint start | Medium | High | P. Walsh | Decision binding this session |
| RISK-003 | Latency threshold FF-005 failing under load test | Low | Medium | P. Walsh | Spike planned — results by 2026-02-14 |

---

## 5. Fitness Function Status

| ID | Fitness Function | Threshold | Current | Status |
|----|-----------------|-----------|---------|--------|
| FF-001 | API response p95 < 200ms | <200ms | 145ms | ✅ Pass |
| FF-002 | Event delivery guarantee ≥99.99% | ≥99.99% | 99.997% | ✅ Pass |
| FF-003 | Zero cross-region data residency violations | 0 | 0 | ✅ Pass |
| FF-004 | Event throughput >10k msg/sec at p99 | >10,000 | Not yet tested | ⬜ Pending ADR-004 |
| FF-005 | End-to-end transaction latency <500ms under 10k concurrent users | <500ms | 620ms | ❌ Fail — spike in progress |
| FF-006 | Audit log write success rate >99.99% | >99.99% | 99.998% | ✅ Pass |
| FF-007 | Zero unencrypted data at rest | 0 | 0 | ✅ Pass |
| FF-008 | Disaster recovery RTO <4hrs | <4hrs | 2.3hrs | ✅ Pass |
| FF-009 | Build pipeline success rate >95% | >95% | 97% | ✅ Pass |

**FF-005 failing:** end-to-end latency exceeds threshold under load. Spike in progress (P. Walsh). Results due 2026-02-14. Not yet an escalation trigger — spike in progress within window.

---

## 6. Next Pulse

**Date:** 2026-02-18 (Tuesday 10:00)
**Tier:** Tier 1 (Weekly)
**Standing items:**
- ADR-005 compliance sign-off — or CR-E1 escalation declared
- TOM-20260115-002 — must be confirmed at this session (decision already binding; recording only)
- FF-005 latency spike result
- ADR-006 — expiry at 2026-02-18 — must bind or escalate

**Tier 2 Pulse:** 2026-02-19 (Monthly cadence not yet active; Tier 2 activated if ADR-005 escalates)

---

*Pulse Briefing — CloudFirst Banking Core Platform Modernisation*
*The OrdoAnimi Framework | © 2026 Phil Myint / OrdoAnimi*
*Canonical template: see `templates/pulse-briefing.md`*
