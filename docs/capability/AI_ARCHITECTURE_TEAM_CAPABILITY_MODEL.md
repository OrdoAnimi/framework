# AI Architecture Team Capability Model

**Status:** Internal operating standard  
**Authority:** Chief AI Architect / Velocity Architecture  
**Purpose:** Define the specialist capabilities required to design, build, assure, and operate enterprise AI systems across the ZenCloud and StudioSix estate.

## Core principle

The senior AI Architect market benchmark describes an organisational capability, not one person performing every task.

The Chief AI Architect owns the technical vision, architecture coherence, cross-domain decisions, standards, review gates, and acceptance of evidence. Specialist teams own implementation depth.

## Team topology

| Function | Primary accountability | Estate authority | Current coverage | Principal gap |
|---|---|---|---|---|
| Chief AI Architecture | End-to-end technical vision, reference architectures, ADRs, design authority, cross-domain trade-offs | Velocity / Founder | Strong | Formal review cadence and evidence-based release authority |
| Product and Value | User problem, product outcome, roadmap, value, customer fit, lifecycle | StudioSix / Imperium / Mercatus | Moderate to strong | Customer validation, pricing, case studies, support boundaries |
| AI Application and Agent Engineering | Services, agents, tools, prompts, state, APIs, code, deterministic controls | Ordo Animi / product repos | Working prototype coverage | Production testing, state management, failure engineering, independent code ownership |
| AI Data and Retrieval Engineering | Ingestion, transformation, RAG, embeddings, indexes, lineage, tenancy, retention | Memoria / Fabrica / Nexus | Strong doctrine, limited implementation | Working shared RAG platform and retrieval evaluation |
| Cloud and Platform Engineering | Managed AI services, networking, identity, secrets, containers, serverless, IaC, CI/CD, resilience | Praesidium | Partial | Reproducible Terraform environments, GitOps, production rollback, platform SRE |
| AI Evaluation and Quality Engineering | Golden datasets, benchmarks, regression, human calibration, quality gates | Probatio | Early doctrine | Executable evaluation harness and release gate |
| AI Security and Privacy Engineering | Threat models, prompt injection, tool abuse, data leakage, privacy, supply chain | Lex / Praesidium | Strong doctrine, partial evidence | Automated adversarial testing, runtime enforcement, independent security review |
| AI Observability and Operations | Traces, logs, metrics, drift, incidents, cost, reliability, service ownership | Specula | Conceptual to partial | End-to-end telemetry, SLOs, alerting, incident exercises |
| Identity and Authority Engineering | Tenant, role, engagement, human approval, runtime permissions | Civitas | Constitutional | Implemented identity and authorisation model |
| Evidence and Records | Release evidence, decisions, accepted artefacts, retention, deletion, handover | Archivum | Strong manual pattern | Automated evidence capture and controlled client archive operations |
| Integration Engineering | APIs, events, adapters, external writes, idempotency, transfer audit | Nexus | Constitutional | Canonical contracts and working adapters |
| Experience and Interaction Design | Design system, interaction patterns, accessibility, human-AI control surfaces | Forma | Emerging | Versioned components, agent interaction standards, accessibility evidence |
| Capability and Enablement | Learning pathways, practical labs, role assessments, mentoring | Velocity Academy | Broad learning estate | Evidence-based role pathways tied to production work |

## Role scorecards

### Chief AI Architect and Design Authority

Must lead:

- business-to-technology translation;
- enterprise and solution architecture;
- architecture principles and reference patterns;
- model, platform, integration, and build-versus-buy decisions;
- risk and autonomy classification;
- design reviews and exceptions;
- specialist team direction;
- customer and executive architecture communication;
- technical acceptance and residual-risk recommendation.

Must understand at working depth:

- agentic patterns and tool control;
- AI evaluations and their limitations;
- RAG and data architecture;
- managed AI services;
- identity, APIs, events, IaC, security, observability, and FinOps;
- production failure modes and operational evidence.

Does not need to be the primary implementer for specialist platform, ML, data, security, or SRE work.

### AI Application and Agent Engineer

Required skills:

- Python and/or TypeScript production engineering;
- model API and managed-service SDKs;
- agent state, tools, workflows, retries, and fallbacks;
- REST and event-driven integration;
- schemas and structured outputs;
- test automation;
- prompt and configuration versioning;
- secure tool execution;
- performance and cost diagnosis.

Required evidence:

- working service;
- automated unit and integration tests;
- failure and recovery tests;
- code review history;
- operational runbook contribution.

### AI Data and Retrieval Engineer

Required skills:

- ingestion and transformation pipelines;
- document processing and metadata;
- embeddings and vector/hybrid search;
- chunking and retrieval strategies;
- reranking and citations;
- data lineage and quality;
- access filtering and multi-tenancy;
- deletion, retention, and re-indexing;
- retrieval evaluation.

Required evidence:

- reproducible ingestion-to-retrieval pipeline;
- quality benchmark;
- lineage and security model;
- scale and cost tests.

### Cloud and AI Platform Engineer

Required skills:

- Azure primary platform depth, with comparative AWS/GCP knowledge;
- managed identity, networking, secrets, policy, and private connectivity;
- containers, functions, queues, gateways, storage, and search;
- Terraform or equivalent IaC;
- CI/CD and GitOps;
- resilience, scaling, rollback, and teardown;
- platform monitoring and cost controls.

Required evidence:

- clean-environment deployment;
- infrastructure plan and apply evidence;
- security and policy scan results;
- release and rollback test;
- cost baseline.

### AI Evaluation and Quality Engineer

Required skills:

- evaluation design for non-deterministic systems;
- golden dataset creation;
- deterministic metrics and LLM-as-judge limitations;
- human calibration;
- safety, grounding, relevance, completeness, tool, and structured-output measures;
- regression thresholds;
- CI integration;
- statistical and qualitative failure analysis.

Required evidence:

- versioned evaluation suite;
- benchmark history;
- release gate;
- false-positive/false-negative analysis;
- human-review calibration record.

### AI Security Engineer

Required skills:

- AI threat modelling;
- direct and indirect prompt injection;
- tool and agent abuse;
- identity and least privilege;
- sensitive-data handling;
- secure retrieval and output processing;
- supply-chain and dependency security;
- adversarial testing;
- incident and kill-switch design.

Required evidence:

- threat model;
- automated security cases;
- control implementation mapping;
- findings and remediation record;
- accepted residual risks.

### AI SRE and Observability Engineer

Required skills:

- distributed tracing and structured logging;
- model, prompt, retrieval, and tool metadata;
- latency, quality, reliability, and cost metrics;
- SLOs and alert thresholds;
- incident response;
- provider outage and fallback patterns;
- evaluation and data drift monitoring;
- capacity and denial-of-wallet controls.

Required evidence:

- operational dashboard;
- alerts and runbooks;
- incident exercise;
- service review and reliability report.

## Current operating allocation

Until human teams are established, use controlled AI-assisted role simulation:

| Function | Interim mechanism | Required separation |
|---|---|---|
| Strategy and architecture | Founder with ChatGPT analysis support | Architecture decisions approved by Founder |
| Product planning | Founder / StudioSix with ChatGPT | Product brief completed before build |
| Implementation | Claude coding work orders | Claude cannot redefine architecture or product intent |
| Evaluation review | Separate Probatio review session or agent | Must not rely solely on the generating agent's self-assessment |
| Security review | Separate Praesidium review session or specialist | Must challenge implementation independently |
| Operational review | Specula checklist and telemetry review | Must occur before and after deployment |
| Evidence and continuity | GitHub plus Archivum/Obsidian | Outputs must leave the conversation surface |

One AI tool may technically perform several functions, but separate prompts, artefacts, acceptance criteria, and review events must preserve the organisational boundary.

## Capability-acquisition model

### Build internally now

The estate should directly build capability in:

- enterprise AI architecture;
- agentic application patterns;
- AI evaluations;
- RAG and retrieval architecture;
- Azure managed-AI reference architecture;
- Terraform and release automation;
- AI observability and FinOps;
- prompt and agent security;
- product and client governance.

These capabilities are central to the StudioSix and Velocity proposition.

### Use fractional specialists or partners first

Use external depth for:

- production ML engineering;
- self-hosted model serving;
- GPU optimisation;
- advanced data science and model training;
- formal penetration testing;
- high-scale SRE;
- specialised privacy or legal interpretation;
- cloud-specific platform implementation outside the primary Azure pattern.

The Founder retains architecture authority while specialists retain professional accountability for their technical evidence.

### Hire when demand is proven

Do not create a full permanent engineering organisation before validated product or client demand. The likely hiring order is:

1. senior AI application/platform engineer;
2. AI data and retrieval engineer;
3. evaluation and quality engineer;
4. AI security/platform engineer;
5. SRE/observability engineer;
6. product and customer success capacity.

Some roles may initially be combined, but evaluation and security review should remain independent from generation where consequence is material.

## Estate capability gaps to close first

1. One enterprise AI reference architecture.
2. One production-grade flagship implementation.
3. Repeatable AI evaluation and regression testing.
4. Working RAG and retrieval infrastructure.
5. Infrastructure as code and GitOps.
6. AI security test suite and runtime controls.
7. End-to-end observability and operational runbooks.
8. Explicit API, event, identity, and tenancy contracts.
9. Provider, model, prompt, and tool registries.
10. Product support, commercial, and client evidence boundaries.

## Definition of organisational readiness

The estate is ready to operate as an AI company when:

- the Chief AI Architect can approve an end-to-end reference architecture;
- engineering teams can implement from bounded contracts;
- independent teams can prove quality and security;
- operations can observe and recover the service;
- product teams can measure customer and economic value;
- evidence is preserved outside conversations;
- no critical capability depends solely on undocumented founder memory or one AI coding session.
