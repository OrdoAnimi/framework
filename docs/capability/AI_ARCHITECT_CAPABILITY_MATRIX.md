# AI Architect Capability Matrix

**Status:** Internal evidence-based capability assessment  
**Purpose:** Compare the current founder and estate capability against a senior enterprise AI Architect market benchmark.

## Assessment method

Capability is assessed against repository evidence, working implementations, architecture doctrine, operating history, and demonstrable production depth.

Evidence levels:

- **Aware** — understands the concern and can discuss it accurately.
- **Assisted** — can produce a bounded result with AI, specialist, or procedural support.
- **Working** — can independently design, implement, diagnose, and explain a bounded solution.
- **Lead** — can set standards, govern other practitioners, and own production outcomes.

The target role combines two profiles that are often separate: senior enterprise/solution architect and senior AI application/platform engineer. Current alignment is therefore reported by domain rather than reduced to a single inflated claim.

## Executive assessment

| Capability domain | Current level | Role target | Assessment |
|---|---:|---:|---|
| Enterprise and solution architecture | Lead | Lead | Strong match |
| Architecture governance and design authority | Lead | Lead | Strong match |
| Customer and executive communication | Lead | Lead | Strong match |
| Cloud architecture | Lead on primary platform; Working cross-cloud | Lead cross-cloud | Strong foundation; broaden current service evidence |
| Responsible AI and governance | Lead in architecture doctrine; Working in implementation | Lead | Strong differentiation; operating evidence still required |
| Agentic AI architecture | Working | Lead | Credible implementation base; deepen orchestration, state, tools, and failure testing |
| LLM application engineering | Assisted to Working | Lead/Working | Current TypeScript implementation exists; increase independent engineering depth |
| AI evaluation engineering | Aware to Assisted | Lead | Material gap |
| Prompt management and security | Working in policy; Assisted in executable testing | Lead | Material implementation gap |
| AI data architecture and RAG | Working conceptually; Assisted hands-on | Lead | Material gap in vector and retrieval implementation |
| Distributed systems and API architecture | Lead architecturally; Assisted to Working hands-on | Lead | Evidence gap in current implementation |
| Infrastructure as code and GitOps | Assisted | Working/Lead | Material gap |
| AI observability and drift detection | Aware to Assisted | Working/Lead | Material gap |
| Model serving, GPU optimisation, inference engineering | Aware | Working/Lead | Specialist gap; do not overclaim |
| Python | Assisted | Working/Lead | Material gap |
| TypeScript/JavaScript | Working with AI assistance | Working/Lead | Continue depth and diagnosis practice |
| AI FinOps | Lead conceptually; Assisted in runtime measurement | Lead | Strong architecture position; add measured inference economics |
| Team leadership and mentoring | Lead | Lead | Strong match |

## Domain evidence and required proof

### Enterprise, solution, and governance architecture

**Current evidence**

- Velocity coordinates enterprise, business, solution, data, security, and PMO concerns around explicit decisions.
- The estate contains architecture decision records, guardrails, correspondence rules, artefact models, engagement packs, practitioner guidance, and delivery governance.
- The founder has substantial prior design-authority, cloud-transformation, security, delivery, and stakeholder leadership experience.

**Conclusion:** Lead-level and directly relevant.

**Additional proof required:** AI-specific customer case study showing strategy-to-production architecture ownership.

### Agentic AI architecture

**Current evidence**

- A TypeScript/Node application uses specialised governance, strategy, design, validation, velocity, rhythm, and practitioner agents.
- The implementation loads a framework knowledge base, routes generation, validates outputs, logs activity, and can commit generated artefacts through the GitHub API.
- Hermes doctrine defines routing, permissions, human approval, action logging, and client-data boundaries.

**Conclusion:** Working-level architecture and prototype implementation. This is more substantial than prompt-only experimentation, but it is not evidence of leading production multi-agent systems across customers.

**Required proof**

- controlled multi-agent or supervisor pattern with explicit shared-state rules
- durable execution traces
- tool permission enforcement
- failure injection and recovery tests
- comparative evidence showing why multiple agents outperform a simpler design
- operational runbook and incident scenarios

### AI evaluation engineering

**Current evidence**

- Velocity includes validation concepts, risk controls, pilot success criteria, readiness gates, and a validation agent.
- The current project declares Jest and describes scoring and validation, but a repeatable model evaluation harness, golden dataset, benchmark history, and regression gate are not yet established as estate-wide evidence.

**Conclusion:** Aware to Assisted. This is the largest gap relative to the role benchmark.

**Required proof**

- versioned evaluation dataset
- deterministic and LLM-as-judge measures with limitations documented
- task-success, groundedness, safety, structured-output, latency, and cost metrics
- baseline and regression thresholds
- CI evaluation workflow
- human calibration and disagreement analysis
- published evaluation report for the Velocity agent

### Prompt management and AI security

**Current evidence**

- Data and tool classification policies exist.
- Human review, least privilege, explicit action permissions, no-confidential-data rules, and agent shutoff principles are documented.
- Prompts are assembled from versioned framework sources in the TypeScript implementation.

**Conclusion:** Working in governance design; Assisted in executable security assurance.

**Required proof**

- prompt and system-instruction registry with versions and owners
- prompt-injection test corpus
- indirect-injection and poisoned-retrieval scenarios
- output encoding and tool-argument validation
- least-privilege runtime identities
- secret and sensitive-data leakage tests
- security exception and residual-risk evidence

### AI data architecture, retrieval, and vector search

**Current evidence**

- Velocity contains data-readiness, classification, lineage, source-of-truth, privacy, and governance doctrine.
- Current repositories do not yet provide strong evidence of a production RAG implementation using managed search or vector infrastructure.

**Conclusion:** Lead conceptual architecture; Assisted implementation.

**Required proof**

- one working RAG reference architecture
- ingestion and transformation pipeline
- chunking, metadata, embedding, indexing, tenancy, and access strategy
- implementation using pgvector, OpenSearch, Azure AI Search, or another selected platform
- retrieval-quality evaluation and source citation
- deletion and re-indexing controls

### Cloud AI managed services

**Current evidence**

- Strong cloud and Azure architecture history.
- Current estate includes container, GitHub Actions, Azure deployment, Cloudflare, and direct Anthropic API patterns.
- Limited repository evidence currently demonstrates comparative hands-on use of Azure OpenAI, Amazon Bedrock/SageMaker, or Google Vertex AI.

**Conclusion:** Strong foundation, incomplete current AI-platform evidence.

**Required proof**

- primary reference implementation on Azure using managed identity, private networking, secrets, logging, policy, and cost controls
- comparative architecture notes for AWS and GCP
- one bounded deployment on a second cloud platform
- build-versus-buy and portability ADR

### Software engineering, APIs, and distributed systems

**Current evidence**

- Current TypeScript service exposes HTTP endpoints, uses typed contracts, structured logging, knowledge caching, retry patterns, direct GitHub integration, and specialised components.
- The founder can direct and review AI-assisted implementation, but current evidence does not establish deep independent mastery of distributed systems, event-driven implementation, GraphQL, gRPC, and microservice operations.

**Conclusion:** Lead architecture literacy; Assisted to Working current implementation depth.

**Required proof**

- independently explained and diagnosed service implementation
- asynchronous event pattern and idempotency example
- API versioning, authentication, rate limiting, retries, circuit breaking, and failure-mode tests
- service contract and integration test suite
- architecture trade-off paper comparing modular monolith, functions, and microservices

### Infrastructure as code, GitOps, and platform engineering

**Current evidence**

- GitHub Actions, deployment files, Docker, static hosting, and Cloudflare deployment patterns exist.
- Terraform, Pulumi, CDK, policy-as-code, repeatable environment provisioning, and formal GitOps promotion are not established consistently across the estate.

**Conclusion:** Assisted.

**Required proof**

- Terraform-based AI reference environment
- environment separation and remote state
- secrets and identity configuration
- policy and security scanning in CI
- deployment promotion and rollback evidence
- cost and teardown controls

### AI observability

**Current evidence**

- Structured logging and conceptual observability institutions exist.
- Velocity identifies monitoring, model/tool review, cost, and operational ownership as required controls.
- End-to-end AI tracing, evaluation telemetry, prompt/model versions, retrieval metrics, and drift alerts are not yet demonstrated.

**Conclusion:** Aware to Assisted.

**Required proof**

- OpenTelemetry or equivalent traces
- model, prompt, retrieval, and tool-call metadata
- latency, token, cost, success, failure, and escalation metrics
- evaluation drift dashboard
- alert and incident runbook

### Model serving, GPU, and inference optimisation

**Current evidence**

- The estate primarily consumes managed frontier-model APIs.
- There is no current evidence of self-hosted model serving, GPU capacity planning, quantisation, batching, KV-cache optimisation, autoscaling, or inference server operation.

**Conclusion:** Awareness only. This is a specialist gap.

**Required position:** Do not market this as current expertise. Build enough knowledge to govern decisions and partner with a specialist. Develop hands-on depth only if the chosen market role makes it a hard requirement.

### Programming languages

**TypeScript/JavaScript:** Working with AI assistance. The estate contains multiple React, Vite, Node, and TypeScript systems. The development objective is independent diagnosis, safe modification, testing, and architectural review rather than syntactic speed.

**Python:** Assisted. The dedicated learning pathway exists, but production AI service, evaluation, data-pipeline, and retrieval evidence must be built.

## Market-position conclusion

The current defensible identity is:

> Principal Enterprise AI Architect and Design Authority with strong cloud, governance, delivery, and agentic-system foundations, developing deeper production AI engineering evidence.

The current evidence does not support presenting the founder as a deep AI platform engineer, ML engineer, GPU specialist, or expert Python AI developer.

For a role that genuinely weights architecture, customers, governance, cloud, and technical leadership most heavily, the profile is a credible adjacent candidate. For a role that uses “architect” as a label for a principal hands-on AI engineer, the current profile is a stretch until the engineering proof programme is completed.
