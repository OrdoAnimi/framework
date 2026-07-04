# Velocity Dashboard

**OrdoAnimi VP4 — Velocity Viewpoint | Architectural Control Layer**

> The Velocity Dashboard is a control surface, not a reporting tool.  
> It answers one question at all times: where is ambiguity accumulating?

---

## Dashboard Configuration

| Field | Value |
|-------|-------|
| **Programme / Engagement** | |
| **Dashboard Owner** | |
| **Update Frequency** | Continuous / Daily / Per Pulse session |
| **Last Updated** | YYYY-MM-DD HH:MM |

---

## Component 1: Decision Velocity Metrics

*How many decisions is this system producing, by layer, per week?*

| Layer | Decisions this week | Decisions last week | 4-week average | Trend |
|-------|--------------------|--------------------|----------------|-------|
| VP1 — Direction (Canvases) | | | | ↑ / → / ↓ |
| VP2 — Decision (Trade-off Matrices) | | | | |
| VP3 — Truth (ADRs) | | | | |
| **Total** | | | | |

**Median decision latency (days):** ___  
*Latency = days between question raised and binding resolution*

**Target:** Median latency < 7 days for VP2/VP3. Trending up over two consecutive weeks = structural signal requiring investigation.

---

## Component 2: Decision Aging Monitor

*What is currently open, and how old is it?*

| ID | Decision / Question | Layer | Owner | Date Raised | Age (days) | Status |
|----|--------------------|----|-------|-------------|------------|--------|
| | | VP[X] | | YYYY-MM-DD | | 🟢 / 🟡 / 🔴 |

**Colour coding:**
- 🟢 Green — open < 7 days
- 🟡 Amber — open 7–14 days (approaching CR-E1 threshold)
- 🔴 Red — open > 14 days (CR-E1 triggered; escalation mandatory)

**Current red count:** ___  
Any red count > 0 requires immediate action in the next Pulse session.

---

## Component 3: Ownership Map

*Is every open decision owned by a single named person?*

| ID | Decision | Named Owner | Role | Assigned | Last Confirmed |
|----|----------|------------|------|----------|---------------|
| | | | | YYYY-MM-DD | YYYY-MM-DD |

**Ownership gaps** (decisions without a single named owner):

| ID | Decision | Gap identified | Escalation status |
|----|----------|---------------|------------------|
| | | YYYY-MM-DD | Pending / Escalated |

---

## Component 4: Heat Map — System Health

*Where is ambiguity accumulating across domains?*

| Domain | Open decisions | Avg age (days) | Fitness failures | Health |
|--------|---------------|----------------|-----------------|--------|
| Enterprise direction | | | | 🟢 / 🟡 / 🔴 |
| Integration / APIs | | | | |
| Data and analytics | | | | |
| Security and compliance | | | | |
| Cloud infrastructure | | | | |
| Delivery and operations | | | | |
| [Add domains as needed] | | | | |

**Health thresholds:**
- 🟢 Green — 0–1 open decisions, avg age < 7 days, no fitness failures
- 🟡 Amber — 2–3 open decisions, or avg age 7–14 days, or 1 fitness failure
- 🔴 Red — 4+ open decisions, or avg age > 14 days, or 2+ fitness failures

---

## Component 5: Risk Inventory

*What risks are currently open, and are they aging?*

| Risk ID | Description | Owner | Date Raised | Expiry | Age | Severity | Status |
|---------|-------------|-------|-------------|--------|-----|----------|--------|
| RISK-001 | | | YYYY-MM-DD | YYYY-MM-DD | | H/M/L | Open |

---

## Component 6: Risk Aging

*Which risks are approaching or past their expiry dates?*

| Risk ID | Description | Expiry | Days to expiry | Action required |
|---------|-------------|--------|---------------|----------------|
| | | YYYY-MM-DD | | Mitigate / Accept / Escalate |

**Risks past expiry (action overdue):**

| Risk ID | Description | Days overdue | Owner | Escalation status |
|---------|-------------|-------------|-------|------------------|
| | | | | |

---

## Component 7: Fitness Function Status

*Are the executable architectural constraints passing?*

| Function | ADR / TOM Reference | Last run | Status | Failure detail |
|----------|--------------------|----|--------|---------------|
| `test_api_latency` | ADR-004 | YYYY-MM-DD | ✅ Pass / ❌ Fail | |
| `test_decision_aging` | CR-E1 | YYYY-MM-DD | ✅ / ❌ | |
| `test_traceability_tom_to_canvas` | CR-T1 | YYYY-MM-DD | ✅ / ❌ | |
| `test_data_residency` | ADR-019 | YYYY-MM-DD | ✅ / ❌ | |
| `test_no_layer_bypass` | CR-L4 | YYYY-MM-DD | ✅ / ❌ | |

**Failing functions requiring architectural response:**

| Function | Failure | Upstream assumption at risk | Escalation status |
|----------|---------|----------------------------|------------------|
| | | | |

---

## Dashboard Summary (Single-page view for Pulse Briefing)

| Metric | Value | Status |
|--------|-------|--------|
| Decisions made this week | | |
| Median decision latency | | 🟢 / 🟡 / 🔴 |
| Decisions aged > 14 days (CR-E1) | | |
| Ownership gaps | | |
| Domains in red (Heat Map) | | |
| Fitness functions failing | | |
| Risks past expiry | | |
| **Overall velocity signal** | | 🟢 High / 🟡 Moderate / 🔴 Low / ⚫ Stalled |

---

## Structural Diagnostics

Run these monthly. They reveal patterns that weekly metrics miss.

| Diagnostic question | Answer | Action if concerning |
|--------------------|--------|---------------------|
| How many decisions have passed through more than one Pulse cycle without binding? | | Invoke CR-E4 |
| How many decisions have been revisited without meeting CR-X2 criteria? | | Name and stop |
| What is the ratio of decisions made to artefacts produced? | | If < 0.3, Architecture Theatre is present |
| Are the same domains appearing on the heat map red three weeks in a row? | | Structural root cause investigation |
| Are any practitioners carrying decisions outside their scope? | | VP6 assessment required |

---

*Velocity Dashboard — OrdoAnimi VP4 | The OrdoAnimi Framework*  
*© 2026 Phil Myint / OrdoAnimi | ISO/IEC/IEEE 42010:2022 Conformant*
