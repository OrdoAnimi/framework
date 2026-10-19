# VP4 — Flow Viewpoint

**Instruments:** Flow Dashboard + Architectural Decision Log (ADL)  
**Layer:** Architectural control  
**ISO/IEC/IEEE 42010 conformant viewpoint**

---

## Purpose

The Flow Viewpoint makes decision movement visible.

It measures and governs decision latency, decision aging, and ownership gaps. It is the control layer — the instrument by which the health of the entire decision system is monitored and managed.

> *Flow is not speed. It is the rate at which ambiguity expires.*

---

## Concerns Addressed

| Concern | Description |
|---------|-------------|
| C1 — Decision clarity | Whether decisions are clear and acted upon |
| C2 — Decision throughput | The rate at which ambiguity expires |
| C3 — Decision traceability | Whether decisions can be traced over time |
| C7 — Architectural integrity | Whether the architecture remains coherent |
| C8 — Governance effectiveness | Whether governance produces decisions |
| C11 — Decision latency | The interval between recognition and binding resolution |
| C13 — Alignment with intent | Whether outcomes reflect direction |
| C14 — Knowledge preservation | Whether decisions survive personnel change |

---

## Model Kind 1: Architectural Decision Log (ADL)

The ADL is the living spine of all architectural decisions. It is not a template — it is the aggregate of all Trade-off Matrices and ADRs, indexed and searchable.

**Structure:**
```
ADL/
├── INDEX.md              ← Master index of all decisions by ID, date, status, owner
├── canvases/             ← All Guardrail Canvas records
├── decisions/            ← All Trade-off Matrix records
├── adrs/                 ← All Architecture Decision Records
└── superseded/           ← Closed decisions (retained, not deleted)
```

**Fixed folder model** — the structure does not change between engagements. This enables:
- Consistent client handover
- Onboarding without explanation
- Automated governance checks (fitness functions against the ADL itself)

**14-Day Decision Aging Rule:**  
Any significant decision open for more than 14 calendar days without binding resolution triggers a mandatory escalation event (CR-E1).

### ADL and ADR Relationship

ADRs (Architecture Decision Records) are the technical-layer instrument of VP3. They are authored in and versioned by the codebase — the single source of truth for the technical decision text. The ADL does not duplicate ADR content. The ADL indexes each ADR by ID and records its current status, governing TOM reference, and owner. This separation is intentional: the codebase holds the decision text; the ADL holds the decision state.

When an ADR is superseded, the original is retained in `superseded/` and the new ADR carries a `Supersedes: ADR-NNN` reference (CR-T3). Both the original and the supersession are indexed in the ADL.

See `viewpoints/vp3-truth/README.md` for the full ADR specification.

---

## Model Kind 2: Flow Dashboard

The Flow Dashboard is a real-time operational view of decision health. It is not a reporting tool — it is a control surface.

**Seven required components:**

| Component | What it shows |
|-----------|--------------|
| Decision Throughput Metrics | Decisions made per week, by layer (VP1/VP2/VP3) |
| Decision Aging Monitor | All open decisions colour-coded by age: green (<7d), amber (7–14d), red (>14d) |
| Ownership Map (RACI) | Current named owners for all open decisions |
| Heat Map (System Health) | Domains by decision health — where is ambiguity accumulating? |
| Risk Inventory | Open risks with aging dates |
| Risk Aging | Risks approaching or past their expiry dates |
| Fitness Function Status | Current pass/fail state of all architectural fitness functions; VP3 signals requiring VP4 response |

**Primary metric:** Decisions per week, by layer  
**Secondary metric:** Decision latency — median days between recognition and binding resolution

**Diagnostic test:**  
*How many significant decisions remain open beyond 30 days? How many have passed through more than one review forum without binding? These are structural readings, not performance metrics.*

---

## Correspondence Rules (from this viewpoint)

- **CR-T3:** Superseded decisions retained in ADL, not deleted
- **CR-E1:** 14-Day Decision Aging Rule — triggers mandatory escalation
- **CR-O2:** Ownership Map updated within 5 days of any ownership transfer
- **CR-X1:** Every open question must be assigned an expiry date
- **CR-X3:** Guardrail Canvas review dates enforced through the ADL

---

## ADL Index Template

→ [`adl-template.md`](adl-template.md)  
→ [`flow-dashboard.md`](flow-dashboard.md)  
→ Worked example: [`examples/adl-example.md`](../../examples/adl-example.md)
