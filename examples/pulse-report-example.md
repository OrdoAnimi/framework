# Worked Example: Pulse Report

**The OrdoAnimi Framework — Examples**

> **Scenario:** CloudFirst Banking — Core Platform Modernisation (continued from pulse-briefing-example.md)
> **Pulse Tier:** Tier 1 (Weekly) — Post-session report
> **Session date:** 2026-02-11
> **Report prepared by:** S. Rajan (Solution Architect, S2)
> **Report recipient:** D. Nguyen (CTO, S5) + Architecture Review Board (S6)
> **Issued:** 2026-02-11 (same day, within 2 hours of session close)

---

# Pulse Report
**CloudFirst Banking — Core Platform Modernisation**
**Tier 1 Pulse | 2026-02-11 | Week 7 of 24**

---

## Summary

One decision confirmed. One escalation risk active. One fitness function failure in remediation. Engagement health: **At Risk** — reducing to **On Track** conditional on ADR-005 compliance sign-off by 2026-02-12.

---

## Decisions Made This Session

### TOM-20260115-002: API gateway strategy — CONFIRMED
**Decision:** AWS API Gateway (managed service) selected as the API gateway layer for all external-facing integration.
**Owner:** P. Walsh (Technical Architect, S3)
**Bound by:** D. Nguyen (CTO, S5) — verbal confirmation, this session
**Rationale:** Managed service eliminates operational overhead estimated at 1.2 FTE. Aligns with GC-20260101-001 constraint (no lock-in above hyperscaler level — AWS API Gateway is a hyperscaler service, not a third-party SaaS).
**ADR:** ADR-007 to be authored by P. Walsh — due 2026-02-13
**ADL update:** TOM-20260115-002 status → Decided (2026-02-11)
**Downstream:** Infrastructure sprint can commence. P. Walsh to notify delivery lead (S4) within 24 hours.

---

## Escalation Status

### ADR-005: Data sovereignty — ESCALATION PENDING
**Status at session close:** T. Clarke confirmed compliance review is complete. Legal sign-off expected 2026-02-12.
**Outcome:** CR-E1 trigger (day 14 = 2026-02-12) will be observed as scheduled. If sign-off is confirmed by EOD 2026-02-12, CR-E1 does not activate. If sign-off is not confirmed by EOD 2026-02-12, ADR-005 escalates to D. Nguyen at Tier 2 Pulse (2026-02-19).
**T. Clarke action:** Confirm sign-off with S. Rajan by email by 16:00 on 2026-02-12.

---

## Items Deferred to Next Pulse

| Item | Reason | Expiry |
|------|--------|--------|
| ADR-006 (audit log retention) | No compliance reference received — monitoring | 2026-02-18 |
| FF-005 latency failure | Spike in progress — results due 2026-02-14 | Results before next Pulse |

---

## Risk Register Changes

| Risk | Change | Note |
|------|--------|------|
| RISK-002 (API gateway delay) | **Closed** | TOM-20260115-002 confirmed this session |
| RISK-001 (compliance delay) | **Unchanged** — monitoring | Escalation pre-authorised 2026-02-12 |
| RISK-003 (FF-005 latency) | **Unchanged** — spike in progress | Results due 2026-02-14 |

---

## Next Pulse

**Date:** 2026-02-18 | Tier 1 (Weekly) | 10:00
**Decision items (binding or escalating):**
- ADR-005 (if sign-off not received by 2026-02-12 — will be at escalation tier by 2026-02-18)
- ADR-006 — expiry on this date, must bind
- FF-005 spike result

**No further items to be added to this session's agenda without prior notice to the architect.**

---

## Decision Velocity Metric — Week 7

| Metric | This week | Cumulative |
|--------|-----------|------------|
| Decisions opened | 1 (ADR-006) | 7 |
| Decisions confirmed | 2 (ADR-004, TOM-20260115-002) | 5 |
| Decisions aged >14 days | 0 | 0 |
| Escalations activated | 0 | 0 |
| Fitness functions failing | 1 (FF-005) | — |

**Velocity observation:** Two consecutive weeks without a decision aging beyond 14 days. The Pulse rhythm is functioning. The ADR-005 sign-off is the only active risk to this metric.

---

*Pulse Report — CloudFirst Banking Core Platform Modernisation*
*The OrdoAnimi Framework | © 2026 Phil Myint / OrdoAnimi*
*See also: `examples/pulse-briefing-example.md` (pre-session), `examples/adl-example.md` (full register)*
