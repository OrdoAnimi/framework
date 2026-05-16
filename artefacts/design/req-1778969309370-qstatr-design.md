# ADR-001 | Adopt a Federated Cloud Governance Model with Centralised Compliance Enforcement

---

## ADR Identification

| Field | Value |
|-------|-------|
| **ADR ID** | ADR-001 |
| **Title** | Adopt a Federated Cloud Governance Model with Centralised Compliance Enforcement |
| **Date** | 2026-01-22 |
| **Owner** | Principal Cloud Architect |
| **Status** | Proposed |
| **Supersedes** | N/A |
| **Governing Decision** | TOM-PENDING — Cloud Platform Strategy and Basel III Compliance Posture |

---

## Context

The firm operates across multiple cloud environments (AWS, Azure) with inconsistent governance practices applied at the team level. Workloads include trading systems, risk calculation engines, and customer data platforms — all subject to Basel III operational risk capital requirements, and specifically to the requirements of Basel III Article 239 (outsourcing risk) and the EBA Guidelines on ICT and Security Risk Management.

Current state produces a measurable **Integrity Gap**: documented governance controls diverge from operational reality. Infrastructure provisioning occurs outside approved patterns, policy-as-code enforcement is absent or inconsistently applied, and audit evidence is generated retrospectively rather than continuously. This constitutes a direct operational risk exposure and creates material uncertainty for internal audit and external regulatory review.

Four specific failure modes have been observed:

1. **Uncontrolled egress paths** — production data crossing tenancy boundaries without Data Loss Prevention (DLP) controls, in violation of documented data classification policy.
2. **Privilege accumulation** — standing administrative access persisting beyond approved change windows, inconsistent with least-privilege requirements under the firm's ISMS.
3. **Configuration drift** — resource configurations diverging from approved baselines between audit cycles, producing point-in-time compliance artefacts that do not reflect continuous state.
4. **Opaque third-party concentration risk** — Basel III Pillar 2 requires that the firm quantify and manage concentration risk across cloud service providers; current tooling does not produce the required signal.

The firm requires a governance model that enforces compliance continuously, produces machine-readable audit evidence, and closes the Integrity Gap between documented and operational architecture — without imposing governance friction that degrades engineering delivery velocity.

---

## Decision

**We will adopt a federated cloud governance model with centralised compliance enforcement, implemented via a Cloud Centre of Excellence (CCoE) and policy-as-code enforcement at the platform layer.**

The model has two layers:

**Layer 1 — Central Enforcement Platform (non-negotiable)**
A centralised policy-as-code platform (HashiCorp Sentinel or Open Policy Agent, to be resolved in a subsequent ADR) enforces mandatory controls at the provisioning layer. No resource may be deployed outside an approved landing zone. Policies encode Basel III-relevant controls directly: data residency, encryption-at-rest (AES-256 minimum), encryption-in-transit (TLS 1.2 minimum), network segmentation, and audit logging. These controls are not advisory — they are blocking gates in the CI/CD pipeline.

**Layer 2 — Federated Delivery Teams (bounded autonomy)**
Delivery teams retain autonomy within the approved landing zone pattern. Teams select services, deployment topologies, and tooling within the envelope established by Layer 1 controls. This preserves engineering velocity while enforcing the compliance boundary.

**Continuous Evidence Generation**
Compliance evidence is generated continuously from infrastructure state, not assembled retrospectively. The audit trail is a by-product of normal operations, not a separate exercise.

---

## Rationale

### Why federated over fully centralised

A fully centralised model was evaluated and rejected on two grounds:

1. **Delivery velocity** — centralised approval queues for every infrastructure change impose latency that is incompatible with the firm's deployment frequency targets. The 14-Day Decision Aging Rule (CR-E1) applies: governance that cannot resolve decisions within its operational window degrades into a blocker, not a control.
2. **Knowledge distribution** — domain-specific architectural decisions (e.g., trading system latency requirements, risk engine data locality) require team-level knowledge that cannot be efficiently centralised.

### Why federated over fully decentralised

A fully decentralised model was evaluated and rejected on two grounds:

1. **Regulatory non-compliance** — Basel III requires that the firm demonstrate centralised oversight and control of material ICT risks. Decentralised governance cannot produce the required consolidated audit evidence.
2. **Integrity Gap amplification** — without centralised enforcement, the observable pattern is that teams interpret governance requirements inconsistently. Each inconsistency is a potential finding under regulatory examination.

### Why policy-as-code at the provisioning layer

Governance documentation that is not machine-enforced produces the **Control Paradox**: the appearance of control without actual control. Policy-as-code eliminates the gap between documented policy and operational behaviour because the policy *is* the enforcement. Configuration drift — the primary source of the Integrity Gap observed in current state — is structurally eliminated at the provisioning layer, not managed reactively.

### Basel III alignment

| Basel III Requirement | Governance Control |
|-----------------------|--------------------|
| Operational risk management (Pillar 2) | CCoE owns cloud risk register; controls are traceable to risk appetite |
| Outsourcing/third-party risk (Art. 239 / EBA ICT) | CSP concentration risk dashboard; single-provider dependency threshold enforced by fitness function |
| Audit trail and evidence (Pillar 3 disclosure) | Continuous compliance evidence from infrastructure state; immutable audit log |
| Business continuity and resilience | Landing zone pattern mandates multi-AZ deployment for Tier 1 workloads |
| Data governance | Data residency controls enforced at the resource tag and network policy layer |

---

## Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| Fully centralised governance (CCoE approves all changes) | Introduces unacceptable delivery latency; ADRS observation: governance queues become the primary delivery bottleneck within 90 days of enforcement |
| Fully decentralised (teams own their governance) | Cannot produce consolidated audit evidence required under Basel III; reproduces the Integrity Gap at scale |
| Commercial CSPM tooling only (e.g., Prisma Cloud, Wiz) | Detective controls only — identifies violations after deployment, not before; does not satisfy the preventive control requirement under the firm's ISMS and EBA ICT guidelines |
| Manual governance via change advisory board (CAB) | Documented failure mode in current state; CAB review cycles are 5–10 business days, incompatible with CI/CD deployment frequency; violates CR-E1 in steady state |

---

## Consequences

### Positive

- **Regulatory posture** — Continuous, machine-readable audit evidence satisfies EBA ICT audit requirements and eliminates retrospective evidence assembly.
- **Integrity Gap closure** — Policy-as-code enforcement structurally closes the gap between documented governance and operational reality.
- **Velocity preservation** — Delivery teams retain autonomy within the approved envelope; governance friction is front-loaded into landing zone design, not distributed across every deployment event.
- **Concentration risk visibility** — CSP dependency metrics are produced automatically; Pillar 2 reporting on third-party concentration risk becomes a dashboard query, not a manual exercise.

### Negative

- **Landing zone build cost** — Establishing compliant landing zones for AWS and Azure requires 6–10 weeks of platform engineering effort before delivery teams can onboard. This is a front-loaded investment.
- **Policy-as-code maintenance** — Regulatory requirements change. Policy library requires an owner (the CCoE) and a defined update cycle aligned to regulatory change notices. If this is not resourced, the policy library drifts and the Integrity Gap re-opens at the policy layer.
- **Team onboarding friction** — Teams currently operating outside approved patterns must migrate workloads into landing zones. This is a one-time migration cost with compliance and operational risk during transition.
- **Federated model complexity** — The boundary between Layer 1 (non-negotiable) and Layer 2 (bounded autonomy) must be precisely documented and maintained. Ambiguity at this boundary produces governance disputes and delivery latency.

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Policy library diverges from regulatory requirements | Medium | High | CCoE owns regulatory change monitoring; policy update SLA = 30 days from regulatory notice |
| Teams bypass landing zones via shadow IT | Medium | High | Fitness function `test_no_unregistered_accounts()` detects out-of-band provisioning; escalation to CISO |
| CCoE becomes a bottleneck | Medium | Medium | CCoE role is platform maintenance, not approval authority; teams self-serve within the envelope |
| Landing zone pattern is over-constrained and blocks legitimate workloads | Low | Medium | Quarterly landing zone review cycle; exception process with 5-day SLA |

---

## Fitness Functions

All fitness functions must carry a reference to this ADR per CR-T4. Each runs continuously in the platform monitoring pipeline.

```python
# [ADR-001] — No cloud resources deployed outside registered landing zones
def test_no_resources_outside_landing_zones():
    unregistered = query_resources_without_landing_zone_tag()
    assert len(unregistered) == 0, f"Unregistered resources detected: {unregistered}"

# [ADR-001] — Encryption at rest enforced on all storage resources
def test_encryption_at_rest_universal():
    unencrypted = query_storage_resources(encryption_at_rest=False)
    assert len(unencrypted) == 0, f"Unencrypted storage resources: {unencrypted}"

# [ADR-001] — TLS 1.2 minimum enforced on all in-transit communication
def test_tls_minimum_version():
    violations = query_endpoints(tls_version_below="1.2")
    assert len(violations) == 0, f"Sub-TLS-1.2 endpoints detected: {violations}"

# [ADR-001] — No standing privileged access beyond approved change windows
def test_no_standing_privileged_access():
    standing_admin = query_iam_roles(standing_privilege=True, outside_change_window=True)
    assert len(standing_admin) == 0, f"Standing privileged access detected: {standing_admin}"

# [ADR-001] — CSP concentration: no single provider exceeds 70% of Tier 1 workload hosting
def test_csp_concentration_threshold():
    concentration = calculate_csp_workload_concentration(tier="Tier1")
    for provider, ratio in concentration.items():
        assert ratio < 0.70, f"CSP concentration breach: {provider} at {ratio:.0%}"

# [ADR-001] — Audit log coverage: all production accounts emit to centralised SIEM
def test_audit_log_centralisation():
    accounts_without_log_forwarding = query_accounts(siem_forwarding=False, env="production")
    assert len(accounts_without_log_forwarding) == 0, \
        f"Accounts without SIEM log forwarding: {accounts_without_log_forwarding}"

# [ADR-001] — No unregistered cloud accounts (shadow IT detection)
def test_no_unregistered_accounts():
    unregistered = query_accounts_outside_management_hierarchy()
    assert len(unregistered) == 0, f"Unregistered accounts detected: {unregistered}"

# [ADR-001] — Policy library current: no open regulatory change notices older than 30 days
def test_policy_library_currency():
    overdue_notices = query_regulatory_change_notices(status="open", age_days_gt=30)
    assert len(overdue_notices) == 0, f"Overdue regulatory change notices: {overdue_notices}"
```

---

## Implementation Notes

**Immediate actions (0–30 days)**
- Appoint CCoE lead (single named owner per CR-O1)
- Select policy-as-code platform (Sentinel vs. OPA — requires a subsequent ADR)
- Inventory all existing cloud accounts and classify against landing zone taxonomy
- Establish CSP concentration risk dashboard (baseline measurement for fitness function)

**Short-term (30–90 days)**
- Build and validate landing zone patterns for AWS and Azure
- Publish policy library v1.0 covering all Basel III-relevant controls
- Onboard Tier 1 workloads to compliant landing zones
- Activate all fitness functions in monitoring-only mode; establish baselines

**Medium-term (90–180 days)**
- Migrate all workloads to landing zones; decommission non-compliant configurations
- Transition fitness functions from monitoring to blocking enforcement in CI/CD pipeline
- Conduct first internal audit against continuous evidence output; validate against EBA ICT requirements
- Publish regulatory evidence pack to internal audit

---

## VAF Compliance Notes

| Rule | Status | Notes |
|------|--------|-------|
| CR-T2 — ADR references governing Trade-off Matrix | Conditional | TOM-PENDING; this ADR must be updated to reference the resolved TOM ID once the Cloud Platform Strategy decision is formalised. This is a known dependency. |
| CR-T4 — Fitness functions traceable to ADR | Satisfied | All fitness functions carry `[ADR-001]` reference |
| CR-O1 — Single named owner | Conditional | Owner is titled by role; must be replaced with a named individual at the point of acceptance |
| CR-L3 — Technical findings escalate to higher layers | Noted | The Integrity Gap finding documented in Context section constitutes a VP3 → VP1 escalation signal. Governance layer must acknowledge and respond. |

---

*Velocity Architecture Framework™ — VP3 Truth Viewpoint*
*ADR-001 | Status: Proposed | © 2026 Phil Myint / ZenCloud Global Consultants*
*ISO/IEC/IEEE 42010:2022 Conformant | github.com/ZenCloudAU/velocity-architecture*