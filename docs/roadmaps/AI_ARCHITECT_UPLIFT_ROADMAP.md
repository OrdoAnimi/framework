# AI Architect Uplift Roadmap

**Status:** Active capability programme  
**Owner:** Founder / Velocity Architecture  
**Objective:** Close the gap between current enterprise AI architecture capability and a senior hands-on AI Architect market benchmark without abandoning the founder's design-authority advantage.

## Programme principle

Do not attempt to become an ML researcher, GPU specialist, senior Python engineer, cloud platform engineer, security specialist, and enterprise architect simultaneously.

The target is a T-shaped AI Architect:

- deep authority in enterprise architecture, solution architecture, governance, cloud transformation, customer leadership, and operating models;
- working implementation depth across agentic systems, AI evaluations, RAG, managed AI services, APIs, IaC, security, observability, and cost;
- sufficient specialist literacy to challenge and govern model-serving, data-science, and GPU engineering decisions.

## Priority sequence

The role benchmark contains many technologies, but the highest-value capability gaps are not equal. The required sequence is:

1. evaluation engineering;
2. one production-grade agentic reference architecture;
3. RAG and vector retrieval;
4. Azure managed-AI deployment;
5. infrastructure as code and GitOps;
6. AI observability and security testing;
7. Python implementation depth;
8. comparative AWS/GCP patterns;
9. model-serving and GPU governance literacy.

## Phase 1 — Evidence baseline and operating discipline

**Target:** 30 days

### Outcomes

- current AI systems and repositories classified;
- one canonical AI Architect capability matrix adopted;
- all new AI work follows the AI Architect Operating Guide;
- current Velocity agent has a defined evaluation specification;
- claims are separated into demonstrated, working, assisted, and planned.

### Deliverables

- AI system card for Velocity Agentic Architect;
- current-state architecture diagram;
- threat model;
- model and tool decision record;
- prompt and system-instruction registry;
- evaluation plan and initial golden dataset;
- operational and cost baseline;
- project-state update identifying prototype versus production boundaries.

### Exit criteria

- no production-ready claim without evidence;
- every AI implementation change identifies model, prompt, retrieval, tool, test, security, cost, and observability impact;
- the current agent can be built, run, and diagnosed from a clean environment.

## Phase 2 — Evaluation-first agent engineering

**Target:** 60 days

### Reference build

Use the Velocity Agentic Architect as the primary proving ground.

Build an evaluation harness that measures:

- artefact structural validity;
- correspondence-rule compliance;
- factual and contextual grounding;
- decision ownership and actionability;
- prohibited-content handling;
- prompt-injection resistance;
- tool-selection and action accuracy;
- latency, token usage, and cost;
- human reviewer score and disagreement.

### Engineering requirements

- versioned test cases;
- baseline results;
- repeatable local command;
- CI evaluation gate;
- failure-report output;
- model and prompt comparison;
- documented limitations of automated judging;
- regression threshold and exception process.

### Skill evidence

The founder must be able to explain the test harness, add a case, diagnose a failure, change a threshold, and defend the metric design without delegating the reasoning to an AI assistant.

## Phase 3 — RAG and AI data architecture reference implementation

**Target:** 90 days

### Reference build

Convert the Velocity knowledge-base loading pattern into a controlled RAG architecture.

The implementation should include:

- source ingestion;
- content normalization;
- chunking and metadata;
- embeddings;
- vector or hybrid index;
- access filters;
- retrieval and reranking;
- citations and provenance;
- deletion and re-indexing;
- retrieval evaluation;
- cost and latency measurement.

### Platform choice

Use Azure as the primary implementation platform because it best leverages the founder's existing cloud credibility. A suitable bounded pattern may use Azure OpenAI or an approved model API, Azure AI Search or PostgreSQL/pgvector, managed identity, Key Vault, Application Insights, and private networking where practical.

### Exit criteria

- working ingestion-to-answer path;
- retrieval-quality results against a controlled dataset;
- data-flow and threat model;
- tenancy and access design;
- provider and retention boundary;
- reproducible deployment.

## Phase 4 — Infrastructure as code, GitOps, and production deployment

**Target:** 120 days

### Deliverables

- Terraform modules for development and production-like environments;
- remote state and environment separation;
- managed identity and secrets configuration;
- network and access controls;
- CI build, test, evaluation, security scan, and deployment workflow;
- release approval and rollback process;
- teardown path and cost controls;
- architecture and operational runbook.

### Exit criteria

- a clean environment can be created from source;
- a failed release can be rolled back;
- build and evaluation evidence is retained;
- no manual configuration is required without an explicit exception record.

## Phase 5 — AI observability, security, and operations

**Target:** 150 days

### Observability

Capture:

- trace and request identifiers;
- model, prompt, retrieval, and tool versions;
- tool calls and outcomes;
- token and inference cost;
- latency and timeout rate;
- task success and evaluation score;
- user feedback;
- fallback and escalation rate;
- policy and security events.

### Security testing

Implement test cases for:

- direct prompt injection;
- indirect injection through retrieved documents;
- tool-argument manipulation;
- sensitive-data leakage;
- cross-user or cross-tenant exposure;
- poisoned sources;
- excessive action permissions;
- denial-of-wallet behaviour;
- insecure output handling.

### Operations

Create:

- incident runbook;
- model/provider outage response;
- fallback and degraded-mode strategy;
- evaluation drift alert;
- cost threshold alert;
- scheduled access and dependency review;
- retirement and data-deletion procedure.

## Phase 6 — Cross-cloud and advanced architecture

**Target:** 180 days

### AWS and GCP comparative patterns

Produce architecture decision papers and one bounded second-cloud implementation covering:

- managed model services;
- identity and private access;
- model invocation;
- retrieval/search;
- observability;
- deployment;
- policy and cost controls.

The objective is not to claim equal operational depth across three clouds. It is to demonstrate that the architect can compare platforms, select deliberately, and transfer the architecture pattern.

### Distributed architecture depth

Implement and explain:

- asynchronous work queue;
- idempotent tool execution;
- event-driven status updates;
- retry and dead-letter handling;
- API authentication and rate limits;
- service versioning;
- one gRPC or GraphQL comparison exercise where justified;
- modular-monolith versus microservice decision.

## Continuous learning tracks

### Python for AI architecture

Focus on practical capability rather than general language completion:

- typed Python and packaging;
- FastAPI;
- data transformation;
- model API clients;
- evaluation harnesses;
- notebooks only for exploration, not production control;
- pytest;
- async I/O;
- structured logging;
- deployment and debugging.

### TypeScript engineering depth

Continue using the current estate, but require independent explanation and diagnosis of:

- async control flow;
- type contracts;
- error propagation;
- testing and mocking;
- API design;
- dependency boundaries;
- security controls;
- performance and resource behaviour.

### Model serving and GPU literacy

Develop architecture literacy in:

- managed versus self-hosted inference;
- throughput, latency, batching, and concurrency;
- model size, quantisation, and memory constraints;
- autoscaling and cold starts;
- context caching;
- inference servers and scheduling;
- GPU cost and utilisation;
- availability and fallback patterns.

This track remains governance literacy unless a strategic decision requires direct platform ownership.

## Portfolio controls

All new AI experiments must answer:

1. Which capability gap does this close?
2. Which production evidence will it create?
3. Which existing repository or reference architecture owns it?
4. What will be retired or consolidated when it is complete?
5. What can the founder independently explain and diagnose after completion?

No new repository should be created solely to learn a technology when the learning can be implemented as a controlled work package inside the reference architecture.

## Role application position

### Apply now when

- the role prioritises enterprise architecture, customer engagement, governance, cloud, design authority, and technical leadership;
- the organisation has specialist platform, ML, and engineering teams around the architect;
- the role accepts strong adjacent experience with demonstrable agentic prototypes and a credible uplift plan.

### Treat as a stretch when

- the architect is expected to personally implement production Python services, Terraform estates, vector platforms, evaluation pipelines, and observability from day one;
- deep GPU, inference-server, or ML platform optimisation is a core hiring gate;
- “AI Architect” is effectively a principal AI engineer title.

## Completion standard

The capability programme is complete when the founder can present one end-to-end AI reference solution and defend:

- the business and architecture decisions;
- data and security boundaries;
- agent and retrieval design;
- model and platform selection;
- source code and API contracts;
- evaluation metrics and results;
- infrastructure and release process;
- observability and incident response;
- unit economics;
- limitations and residual risks.

That reference solution becomes the proof asset for employment, advisory, StudioSix, and Velocity.
