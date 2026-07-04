# AI Architect Operating Guide

**Status:** Internal practitioner doctrine  
**Owner:** OrdoAnimi / Founder  
**Purpose:** Define the operating boundary, delivery method, evidence obligations, and engineering expectations for an enterprise AI architect.

## Role thesis

An AI Architect is the technical design authority that converts business intent into secure, scalable, observable, cost-aware, and operable AI capability.

The role is not satisfied by prompt fluency, policy authorship, cloud familiarity, or generated code alone. It requires integration of enterprise architecture, solution architecture, data architecture, software engineering, cloud platforms, AI application patterns, assurance, and production operations.

Velocity positions the AI Architect as the coordination authority across these concerns:

```text
Business outcome
  -> use-case and risk classification
  -> data and trust boundary
  -> model and platform decision
  -> agent and integration architecture
  -> engineering and evaluation contract
  -> deployment and operational controls
  -> measured value and continuous review
```

## Practitioner boundary

The AI Architect is accountable for the architecture and technical governance of AI-powered solutions. The role may prototype and review code, but it does not replace specialist data scientists, ML engineers, platform engineers, security engineers, SREs, or product owners.

The architect must be able to challenge those specialists, understand their implementation evidence, and make or govern cross-domain decisions.

The architect must not claim specialist expertise in foundation-model training, model-weight optimisation, advanced GPU kernel engineering, or ML research unless independently demonstrated.

## Core accountabilities

### 1. Strategy to technical architecture

The architect converts the business problem into a bounded AI use case with an accountable owner, users, measurable outcome, non-goals, failure tolerance, and explicit human authority.

Required evidence:

- AI use-case canvas
- capability and value map
- risk tier
- success and stop criteria
- build-versus-buy decision
- architecture decision records

### 2. End-to-end solution design

The architect designs the complete solution across experience, application, service, data, AI, integration, identity, security, platform, and operations layers.

The design must identify synchronous and asynchronous flows, state boundaries, failure handling, scaling assumptions, external dependencies, API contracts, and support ownership.

Required evidence:

- context and container views
- sequence and data-flow diagrams
- service and integration contracts
- non-functional requirements
- threat model
- deployment view
- operational ownership model

### 3. Agentic AI architecture

Agentic systems must be designed as controlled software systems rather than personalities attached to language models.

The architecture must define:

- objective and bounded task domain
- planner or routing approach
- tools and permissions
- state and memory boundaries
- retrieval sources
- approval and escalation points
- retry, fallback, timeout, and termination behaviour
- action logging
- evaluation and regression strategy
- kill switch and recovery path

Multi-agent designs require an explicit reason for distribution. A single bounded agent is preferred unless specialisation, parallelism, isolation, or independent control materially improves the system.

Private chain-of-thought is not an enterprise audit mechanism. The controlled evidence surface is the system's inputs, selected plan, tool calls, outputs, state transitions, approvals, exceptions, and results.

### 4. AI data architecture

The architect defines how information is ingested, transformed, classified, stored, indexed, retrieved, retained, and deleted.

The design must distinguish operational data, model inputs, prompts, retrieved context, embeddings, generated outputs, feedback, telemetry, and evidence.

Required evidence:

- source-of-truth register
- data classification and lineage
- retrieval and indexing design
- chunking and metadata strategy where RAG is used
- access and tenancy model
- retention and deletion rules
- data quality controls
- provider processing boundary

### 5. Model and platform selection

Model selection must be architecture-led rather than vendor-led.

The architect compares options using quality, latency, cost, context requirements, security, privacy, residency, contractual terms, observability, portability, operational support, and exit constraints.

Managed AI services, direct model APIs, self-hosted models, and hybrid patterns must be evaluated according to the use case rather than preference.

Required evidence:

- option assessment
- benchmark results
- cost model
- selected model and version policy
- fallback and substitution strategy
- provider risk record

### 6. Evaluation and quality engineering

Every non-deterministic capability requires a repeatable evaluation system before production approval.

The minimum evaluation model includes:

- representative golden dataset
- task-success criteria
- groundedness and factuality checks
- relevance and completeness measures
- safety and policy adherence
- tool-selection accuracy
- structured-output validity
- latency and cost measurements
- human-review rubric
- adversarial and prompt-injection cases
- regression thresholds

Evaluations must run against controlled model, prompt, retrieval, tool, and configuration versions. A demonstration is not an evaluation.

### 7. Prompt and agent security

Prompts are controlled application assets. System instructions, tool descriptions, schemas, policies, and retrieval rules must be versioned and reviewed.

The architecture must address:

- direct and indirect prompt injection
- untrusted retrieved content
- secret and sensitive-data leakage
- excessive agency
- tool abuse
- insecure output handling
- cross-tenant data exposure
- poisoned knowledge sources
- denial-of-wallet and resource exhaustion

Security controls should be enforced through identity, permissions, schemas, isolation, validation, and runtime policy rather than prompt wording alone.

### 8. Cloud and platform architecture

The architect must design deployable patterns using managed AI services, containers, serverless systems, event services, API gateways, storage, search, identity, secrets management, networking, and observability.

Cloud expertise is demonstrated through working reference implementations and architecture decisions, not by listing services.

The practitioner should maintain one primary production platform and sufficient comparative knowledge of the other major platforms to make defensible selection decisions.

### 9. Engineering governance

AI architecture must create an implementable engineering contract.

The contract includes:

- repository and service boundaries
- API and event contracts
- coding and review standards
- environment strategy
- infrastructure as code
- automated tests and evaluations
- supply-chain controls
- release gates
- rollback and recovery
- operational evidence

AI-generated implementation remains subject to the same engineering controls as human-written implementation.

### 10. AI observability and operations

The architect defines the telemetry needed to understand both software and AI behaviour.

Minimum signals include:

- request and trace identifiers
- model, prompt, tool, and retrieval versions
- token and inference cost
- latency and timeout rates
- tool-call outcomes
- task success and failure
- policy violations
- evaluation drift
- user feedback
- fallback and human-escalation rate

The design must include incident handling, operational ownership, change review, capacity and cost thresholds, and retirement conditions.

## Velocity AI architecture lifecycle

### Gate 1 — Intent

Confirm the business problem, owner, users, value hypothesis, non-goals, and whether AI is necessary.

### Gate 2 — Classification

Classify use-case type, consequence, autonomy, data sensitivity, customer exposure, and regulatory context.

### Gate 3 — Architecture

Approve the end-to-end architecture, data boundary, model/platform decision, integration pattern, security model, and operational responsibilities.

### Gate 4 — Engineering contract

Define APIs, repositories, environments, IaC, tests, evaluations, telemetry, deployment gates, and acceptance criteria.

### Gate 5 — Controlled build

Implement through reviewed work orders. AI coding agents may build, but cannot change product intent, architecture authority, policy boundaries, or acceptance criteria without an approved decision.

### Gate 6 — Evaluation and assurance

Run deterministic tests, AI evaluations, security tests, failure tests, cost tests, and human review. Record evidence and exceptions.

### Gate 7 — Production authorisation

Confirm support owner, monitoring, rollback, incident response, provider terms, release evidence, and approved residual risk.

### Gate 8 — Operation and adaptation

Measure value, quality, safety, reliability, cost, and user outcomes. Material model, prompt, retrieval, tool, or provider changes trigger reassessment.

## Minimum architecture review questions

1. What business decision or capability is this system supporting?
2. Why is AI required rather than deterministic software or process redesign?
3. What information enters the system, and under what classification and authority?
4. Which model, platform, retrieval, and tool decisions have been made, and why?
5. What actions can the system perform, and where is human approval mandatory?
6. How will quality be measured repeatedly rather than demonstrated once?
7. How are prompt injection, data leakage, excessive agency, and supply-chain risks controlled?
8. What happens when the model, retrieval source, tool, dependency, or provider fails?
9. How will the system be traced, monitored, supported, rolled back, and retired?
10. What is the cost per successful outcome, and when should operation stop?

## Evidence standard

Capability claims use four evidence states:

- **Aware:** understands the terminology and purpose.
- **Assisted:** can perform the task with substantial guidance or AI assistance.
- **Working:** can independently design, implement, diagnose, and explain a bounded solution.
- **Lead:** can establish standards, review other engineers, govern trade-offs, and own production outcomes.

No capability is recorded as Lead solely because an artefact, generated repository, or training course exists. Lead status requires working implementation evidence, review evidence, failure diagnosis, and an ability to defend the design without relying on generated prose.

## Current Velocity boundary

Velocity is already strong in decision architecture, governance, human accountability, architecture artefacts, agent boundaries, data classification, FinOps framing, and traceability.

The operating method must now deepen its production engineering layer through executable evaluations, AI security testing, managed-service reference implementations, retrieval architecture, infrastructure as code, end-to-end observability, and operational runbooks.

The intended practitioner identity is:

> Enterprise AI Architect and Design Authority: architecture-led, engineering-literate, governance-driven, and capable of carrying AI systems from strategy through production evidence.
