# Example: Trade-off Matrix

**TOM-20260115-001 | API Gateway Platform Selection**

> This is a worked example demonstrating how a Trade-off Matrix is completed.  
> Replace all content with your actual decision context.

---

## Decision Identification

| Field | Value |
|-------|-------|
| **Decision ID** | TOM-20260115-001 |
| **Decision Title** | API Gateway Platform Selection — Cloud Platform Modernisation Programme |
| **Date** | 2026-01-15 |
| **Owner** | Phil Myint, Principal Architect |
| **Status** | Decided |
| **Supersedes** | N/A |
| **Governing Canvas** | GC-20260101-001 — Cloud Platform Modernisation FY2026 |

---

## Context

The programme requires a centralised API gateway to manage authentication, rate limiting, routing, and observability across 14 microservices being migrated to cloud. The platform must be production-ready within 8 weeks. The current environment has no API gateway — all inter-service calls are direct and unmanaged. The team has 3 engineers with AWS experience and 1 with Azure. Budget ceiling for tooling is $80k/year.

---

## Options Considered

| Option | Summary | Key advantage | Key risk |
|--------|---------|--------------|----------|
| AWS API Gateway | Native AWS managed service | Zero infrastructure overhead; team familiar with AWS | Vendor lock-in to AWS; limited advanced routing |
| Kong Gateway (self-managed) | Open-source, platform-agnostic | Flexibility; portable across clouds | Operational overhead; team has no Kong experience |
| Azure API Management | Microsoft managed service | Strong enterprise features, good governance tooling | Team has minimal Azure experience; cost higher |
| MuleSoft Anypoint | Enterprise integration platform | Richest feature set; strong enterprise adoption | Significantly over-budget; 6-month implementation minimum |

---

## Decision Drivers

| Driver | Weight | Notes |
|--------|--------|-------|
| Delivery speed (8-week target) | High | Non-negotiable given programme timeline |
| Team capability match | High | Ramp-up risk is real with 8-week window |
| Operational overhead | Medium | Small team; cannot absorb heavy ops burden |
| Cost within $80k/year ceiling | High | Hard constraint from canvas GC-20260101-001 |
| Vendor lock-in risk | Low | Acceptable at this stage; revisit at Phase 2 |
| Feature completeness | Low | Basic routing and auth is sufficient for Phase 1 |

---

## Decision

**We choose AWS API Gateway for Phase 1.**

---

## Consequences

**Gains:**
- Delivery target is achievable — team can be productive within 2 weeks
- Zero infrastructure management overhead
- Cost within ceiling (~$12k/year at projected traffic)
- Native integration with existing AWS services (IAM, CloudWatch, Lambda)

**Accepted costs / risks:**
- Vendor lock-in to AWS API Gateway increases migration cost if we move to multi-cloud in future
- Limited advanced routing capability — acceptable for Phase 1, may require revisit in Phase 2
- Some features available in Kong/APIM not available here (e.g. advanced rate limiting by customer tier)

**What this decision closes off:**
- Platform-agnostic API management in the short term
- Azure-native API governance tooling

---

## Required Actions

| Action | Owner | Due |
|--------|-------|-----|
| Deploy AWS API Gateway in dev environment | Sarah Chen, Senior Engineer | 2026-01-22 |
| Define authentication and rate limiting standards | Phil Myint | 2026-01-22 |
| Create ADR documenting AWS API Gateway configuration decisions | Sarah Chen | 2026-01-29 |
| Add fitness function for API latency budget | Dev Team | 2026-02-05 |

---

## Review / Revisit Criteria

This decision should be revisited if:
- Programme expands to require multi-cloud deployment
- Traffic volume exceeds AWS API Gateway pricing threshold making cost unacceptable
- Advanced routing requirements emerge that AWS API Gateway cannot satisfy
- Phase 2 planning identifies a material reason to change platform

---

## Change Log

| Date | Owner | Change |
|------|-------|--------|
| 2026-01-15 | Phil Myint | Decision made at Architecture Review session |

---

*Example Trade-off Matrix — Velocity™ VP2 | Velocity Architecture Framework™*  
*© 2026 Phil Myint / ZenCloud Global Consultants*
