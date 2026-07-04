# Guardrail Canvas

**OrdoAnimi VP1 — Direction Viewpoint | Enterprise Architecture Layer**

> One canvas = one organisational domain or strategic period.  
> This is a declaration of intent, not a design document.

---

## Canvas Identification

| Field | Value |
|-------|-------|
| **Canvas ID** | GC-YYYYMMDD-XXX |
| **Organisation / Domain / Period** | |
| **Owner** | Name and role |
| **Status** | Proposed \| Active \| Under Review \| Superseded |
| **Review Date** | YYYY-MM-DD |
| **Supersedes** | GC-[prior ID] or N/A |

---

## Core Optimisation

> *What do we prioritise when forced to choose?*  
> One clear statement. Not a list of values.

```
We prioritise [X] over [Y] when trade-offs are required.
```

---

## Non-Negotiables

> *What cannot be traded away under any circumstances?*  
> Keep this short. If everything is non-negotiable, nothing is.

- **Compliance:** [e.g. GDPR zero-tolerance / Essential Eight Maturity Level 2 minimum]
- **Security boundary:** [e.g. No customer PII outside Australian data residency]
- **Technical debt cap:** [e.g. No more than 20% of delivery capacity on unplanned work]
- **Vendor constraint:** [e.g. No sole-source contracts above $X without board approval]

---

## Explicit Trade-offs

> *Where we have made a conscious choice between competing goods.*  
> Name the tension. State the position. Own it.

| Tension | Our Position | Rationale (one line) |
|---------|-------------|---------------------|
| Speed vs Scale | We choose Scale | Core platform must support 10x growth |
| Innovation vs Stability | Stability in core; innovation at edge | Core systems serve regulated functions |
| Cost vs Resilience | Resilience for Tier 1; cost optimisation for Tier 2 | Downtime cost exceeds hosting cost |
| Build vs Buy | Buy unless differentiated capability | Reduce operational burden |
| Centralisation vs Autonomy | [State position] | |

---

## What This Canvas Does NOT Do

This canvas does not:
- Specify which technology to use
- Design any system or integration
- Replace solution architecture decisions
- Prescribe implementation patterns

Those decisions belong to VP2 (Trade-off Matrix) and below.

---

## Change Log

| Date | Owner | Change |
|------|-------|--------|
| YYYY-MM-DD | Name | Initial canvas |

---

*Guardrail Canvas — OrdoAnimi VP1 | The OrdoAnimi Framework*  
*© 2026 Phil Myint / OrdoAnimi | ISO/IEC/IEEE 42010:2022 Conformant*
