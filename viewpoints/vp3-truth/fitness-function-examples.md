# Fitness Functions

**Velocity™ VP3 — Truth Viewpoint | Technical Architecture Layer**

> Fitness functions are executable assertions encoding architectural intent.  
> They are not documentation. They are enforcement.  
> When a fitness function breaks, an upstream assumption is no longer valid.

---

## What a Fitness Function Is

A fitness function is a test that runs continuously in the delivery pipeline to verify that the system still satisfies a declared architectural constraint. It converts intent (stated in an ADR or Trade-off Matrix) into a verifiable, binary signal.

**Key properties:**
- Executable — it runs, not just documents
- Traceable — linked to the ADR or Trade-off Matrix that defines the intent
- Continuous — runs on every deployment or on a defined schedule
- Binary — passes or fails; no partial credit

---

## Categories

### Performance

```python
# ADR-004: p95 API response time must remain under 50ms
def test_api_latency():
    assert p95_latency("api/orders") < 50  # ms

# ADR-011: Database query time must not degrade with scale
def test_db_query_budget():
    assert max_query_time("order_history") < 200  # ms at 10M rows
```

### Reliability

```python
# TOM-20240315-001: Deployment success rate must exceed 99%
def test_deployment_success():
    assert deployment_success_rate(last_30_days=True) > 0.99

# ADR-007: No single point of failure in payment path
def test_payment_redundancy():
    assert redundancy_level("payment-service") >= 2
```

### Security and Compliance

```python
# ADR-019: No dependency on vendor outside approved list
def test_vendor_dependencies():
    approved = load_approved_vendors()  # from Guardrail Canvas GC-20240101-001
    assert no_unauthorised_vendor_dependencies(approved_list=approved)

# TOM-20240601-003: All data at rest must be encrypted
def test_encryption_at_rest():
    assert all_storage_encrypted(regions=["ap-southeast-2"])

# ADR-022: No PII outside Australian data residency
def test_data_residency():
    assert pii_data_regions() == {"ap-southeast-2"}
```

### Architecture Layer Integrity

```python
# CR-L4: No direct calls from Tier 3 to Tier 1 (layer bypass)
def test_no_layer_bypass():
    assert no_direct_calls(from_tier=3, to_tier=1)

# CR-L1: No technology mandates in enterprise layer artefacts
def test_guardrail_canvas_scope():
    canvases = load_active_canvases()
    for canvas in canvases:
        assert not canvas_contains_technology_mandates(canvas)
```

### Decision Governance

```python
# CR-E1: No significant decision open beyond 14 days
def test_decision_aging():
    open_decisions = load_open_decisions()
    for decision in open_decisions:
        assert decision.age_days <= 14, f"Decision {decision.id} is {decision.age_days} days old"

# CR-T1: Every Trade-off Matrix references a Guardrail Canvas
def test_traceability_tom_to_canvas():
    matrices = load_all_trade_off_matrices()
    for m in matrices:
        assert m.governing_canvas_id is not None, f"TOM {m.id} has no canvas reference"
```

---

## Traceability Requirement

Every fitness function must carry a comment referencing the ADR, Trade-off Matrix, or Correspondence Rule that defines the intent it enforces.

```python
# REQUIRED FORMAT:
# [ADR-NNN | TOM-YYYYMMDD-NNN | CR-XX] — brief description of intent
def test_example():
    # ADR-004 — API latency budget for order service
    assert p95_latency("api/orders") < 50
```

Without this reference, the fitness function cannot be traced to its intent and is not compliant with Velocity™ correspondence rule CR-T4.

---

*Fitness Functions — Velocity™ VP3 | Velocity Architecture Framework™*  
*© 2026 Phil Myint / ZenCloud Global Consultants | ISO/IEC/IEEE 42010:2022 Conformant*
