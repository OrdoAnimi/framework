# Example: Architecture Decision Record

**ADR-001 | Use gRPC for internal service-to-service communication**

> This is a worked example demonstrating how an ADR is completed.  
> Replace all content with your actual decision context.

---

## ADR Identification

| Field | Value |
|-------|-------|
| **ADR ID** | ADR-001 |
| **Title** | Use gRPC for internal service-to-service communication |
| **Date** | 2026-01-22 |
| **Owner** | Sarah Chen, Senior Engineer |
| **Status** | Accepted |
| **Supersedes** | N/A |
| **Governing Decision** | TOM-20260115-001 — API Gateway Platform Selection |

---

## Context

Following the selection of AWS API Gateway for external-facing APIs (TOM-20260115-001), we need to define the protocol for internal service-to-service calls within the platform boundary. Currently there is no standard — services use REST with JSON inconsistently. We have 14 microservices that will need to communicate with each other. The dominant concern is latency: the order processing pipeline requires sub-10ms internal calls to meet the p95 < 50ms SLA for the external API.

---

## Decision

**We will use gRPC with typed Protobuf contracts for all internal service-to-service communication.**

---

## Rationale

REST with JSON was evaluated and rejected for internal calls because:
- JSON serialisation overhead is measurable at our target latency (<10ms per internal hop)
- No enforced contract — services have drifted on field names and types, causing integration bugs
- HTTP/1.1 connection overhead is unnecessary for persistent service meshes

gRPC was selected because:
- Binary serialisation via Protobuf is 5–10x faster than JSON for our payload sizes (benchmarked)
- Strongly typed contracts enforced at compile time — eliminates integration drift
- HTTP/2 multiplexing reduces connection overhead
- Team has sufficient Go and Java experience to implement without significant ramp-up

---

## Alternatives Considered

| Alternative | Why not chosen |
|------------|----------------|
| REST/JSON | Latency overhead; no enforced contract; integration drift already causing bugs |
| REST with OpenAPI contracts | Solves contract drift but does not solve serialisation latency |
| GraphQL | Appropriate for client-facing APIs; adds unnecessary complexity for service mesh |
| AMQP / async messaging | Correct for event-driven flows but this decision covers synchronous request-response only |

---

## Consequences

**Positive:**
- p95 internal latency target of <10ms is achievable
- Protobuf contracts are version-controlled and enforced at build time
- Bidirectional streaming available for future use cases

**Negative / accepted costs:**
- gRPC is less human-readable than REST — debugging requires tooling (e.g. grpcurl, Postman gRPC)
- Higher onboarding cost for engineers unfamiliar with Protobuf
- Protobuf schema management requires discipline — breaking changes to schemas will cause build failures (which is also a feature)

**New concerns raised by this decision:**
- We need a Protobuf schema registry and versioning policy — this is a follow-on ADR (ADR-002)
- Service mesh tooling (Istio or Envoy) should be evaluated to manage gRPC traffic at scale — flagged for Phase 2

---

## Fitness Functions

```python
# ADR-001 — Internal service latency budget
def test_internal_service_latency():
    # All internal gRPC calls must complete in under 10ms p95
    assert p95_latency("internal/*") < 10  # ms

# ADR-001 — No REST calls between internal services
def test_no_internal_rest():
    # Internal service mesh must use gRPC only
    assert no_rest_calls_on_internal_mesh()
```

---

## Review / Revisit Criteria

This decision should be revisited if:
- A service language is introduced that has poor gRPC support
- The team grows beyond 20 engineers and onboarding cost becomes material
- A Phase 2 evaluation of service mesh tooling identifies a reason to change protocol

---

## Change Log

| Date | Owner | Note |
|------|-------|------|
| 2026-01-22 | Sarah Chen | Accepted at architecture working session |

---

*Example ADR — Velocity™ VP3 | Velocity Architecture Framework™*  
*© 2026 Phil Myint / ZenCloud Global Consultants*
