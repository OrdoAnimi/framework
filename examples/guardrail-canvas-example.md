# Example: Guardrail Canvas

**GC-20260101-001 | Cloud Platform Modernisation Programme**

> This is a worked example demonstrating how a Guardrail Canvas is completed.  
> Replace all content with your actual organisational context.

---

## Canvas Identification

| Field | Value |
|-------|-------|
| **Canvas ID** | GC-20260101-001 |
| **Organisation / Domain / Period** | ZenCloud Consulting — Cloud Platform Modernisation — FY2026 |
| **Owner** | Phil Myint, Principal Architect |
| **Status** | Active |
| **Review Date** | 2026-07-01 |
| **Supersedes** | N/A |

---

## Core Optimisation

We prioritise **platform resilience and delivery velocity** over **feature breadth and cost minimisation** when trade-offs are required.

*Rationale: Our delivery teams are currently absorbing the cost of an unstable platform. Until the platform is stable, every new feature compounds the problem. Cost optimisation is a second-order concern.*

---

## Non-Negotiables

- **Compliance:** Essential Eight Maturity Level 2 minimum across all production systems — no exceptions without board sign-off
- **Data residency:** No customer data outside Australian data centres (ap-southeast-2, canberra regions)
- **Technical debt cap:** No more than 20% of sprint capacity on unplanned/reactive work — if exceeded, delivery stops and root cause is addressed
- **Vendor constraint:** No sole-source contracts above $500k/year without an approved exit strategy

---

## Explicit Trade-offs

| Tension | Our Position | Rationale |
|---------|-------------|-----------|
| Speed vs Scale | Scale | Platform must support 5x current load within 18 months |
| Innovation vs Stability | Stability in core, experimentation at edge | Core systems are revenue-critical; edge services can absorb more risk |
| Cost vs Resilience | Resilience for Tier 1; cost optimisation for Tier 2–3 | Downtime cost to business exceeds hosting cost by 40:1 |
| Build vs Buy | Buy unless genuinely differentiated | We are not a software product company |
| Centralisation vs Autonomy | Central platform, autonomous delivery | Teams own their services; platform team owns the foundation |

---

## What This Canvas Does NOT Do

This canvas does not specify which cloud provider to use, which deployment platform to adopt, or what API standards to apply. Those decisions belong to the Trade-off Matrix layer (VP2).

---

## Change Log

| Date | Owner | Change |
|------|-------|--------|
| 2026-01-01 | Phil Myint | Initial canvas, approved at Architecture Review Board |

---

*Example Guardrail Canvas — Velocity™ VP1 | Velocity Architecture Framework™*  
*© 2026 Phil Myint / ZenCloud Global Consultants*
