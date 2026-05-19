# VAF Agentic Architect v2

**Live:** [velocityarchitectureframework.com](https://velocityarchitectureframework.com)

An agentic TypeScript/Node.js application that generates enterprise architecture artefacts using Claude. Submit a topic and context. Three specialised agents run — governance, strategy, design — each producing a VAF-compliant artefact. Results are rendered in the browser and committed back to this repository.

---

## What it does

1. Accepts an EA request via a web portal (topic, context, constraints, artefact selection)
2. Loads the VAF framework from this repository as the knowledge base
3. Runs three Claude-powered agents in parallel — Governance (VP1), Strategy (VP2), Design (VP3)
4. Validates artefact quality and cross-alignment
5. Commits the generated artefacts to `/artefacts/` in this repository
6. Renders full Markdown output in the browser

---

## Tech stack

| Component | Detail |
|-----------|--------|
| Language | TypeScript 5.3 |
| Runtime | Node.js 20 |
| Framework | Express 4.18 |
| AI | Anthropic SDK — `claude-sonnet-4-6` |
| Proxy | nginx (port 80 → Node port 3000) |
| Container | Docker — `ghcr.io/zencloudau/velocity-architecture:latest` |
| Hosting | Azure Container Instances — `vaf-rg` / `australiasoutheast` |
| CI/CD | GitHub Actions — `.github/workflows/deploy.yml` |

---

## The three viewpoints

Each request generates one artefact per selected viewpoint.

**VP1 — Direction: Guardrail Canvas**
Declares organisational non-negotiables, trade-off positions, and what the system optimises for. Sets constraints that all downstream decisions must operate within.

**VP2 — Decision: Trade-off Matrix**
Produces a binding solution-level decision with explicit options, decision drivers, chosen direction, and accepted costs. Actionable the day it is agreed.

**VP3 — Truth: Architecture Decision Record (ADR)**
Records a technical architectural decision in full: context, decision, rationale, consequences, and fitness functions. Stored in version control, immutable once accepted.

---

## Run locally

**Prerequisites:** Node.js 20+, an Anthropic API key, a GitHub token with write access to this repo.

```bash
git clone https://github.com/ZenCloudAU/velocity-architecture
cd velocity-architecture
npm install
cp .env.example .env
```

Edit `.env` — set `ANTHROPIC_API_KEY` and `VAF_GITHUB_TOKEN`.

```bash
npm run dev        # ts-node, port 3000 — open http://localhost:3000
```

**Build and run compiled:**
```bash
npm run build
npm start
```

**Run with Docker (matches production):**
```bash
docker build -t vaf-agentic-architect .
docker run -p 80:80 \
  -e ANTHROPIC_API_KEY=sk-ant-... \
  -e VAF_GITHUB_TOKEN=ghp_... \
  -e NODE_ENV=production \
  vaf-agentic-architect
```

---

## API

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Portal UI |
| `GET` | `/health` | Health check |
| `GET` | `/status` | Operational status |
| `POST` | `/artefacts/generate` | Generate EA artefacts |

**Generate request body:**
```json
{
  "topic": "Cloud governance model for financial services",
  "context": "Mid-size bank, Azure-first, Basel III compliance required",
  "constraints": ["Basel III compliance", "reduce governance drag"],
  "requestedArtefacts": ["governance", "strategy", "design"]
}
```

---

## Repository structure

```
velocity-architecture/
│
├── .github/workflows/
│   └── deploy.yml              ← CI/CD: build image, deploy to Azure
│
├── app/                        ← Application source (TypeScript)
│   ├── agents/
│   │   ├── governance-agent.ts ← VP1 Guardrail Canvas generation
│   │   ├── strategy-agent.ts   ← VP2 Trade-off Matrix generation
│   │   ├── design-agent.ts     ← VP3 ADR generation
│   │   └── validation-agent.ts ← cross-artefact quality validation
│   ├── types/
│   │   └── index.ts            ← shared TypeScript interfaces
│   ├── action-engine.ts        ← commits artefacts to GitHub
│   ├── app.ts                  ← Express server and route definitions
│   ├── kb-loader.ts            ← loads VAF framework from GitHub at runtime
│   ├── logger.ts               ← pino structured logging
│   ├── orchestrator.ts         ← planning → generation → validation → publishing
│   └── portal.html             ← web UI served at /
│
├── artefacts/                  ← generated artefacts committed by the agent
│   ├── design/
│   ├── governance/
│   └── strategy/
│
├── viewpoints/                 ← VAF framework specification (read by kb-loader)
│   ├── vp1-direction/          ← VP1 spec + Guardrail Canvas template
│   ├── vp2-decision/           ← VP2 spec + Trade-off Matrix template
│   ├── vp3-truth/              ← VP3 spec + ADR template + fitness function examples
│   ├── vp4-velocity/           ← VP4 spec + ADL template + Velocity Dashboard
│   ├── vp5-rhythm/             ← VP5 spec + Pulse System
│   └── vp6-practitioner/       ← VP6 spec + Integrity Arc
│
├── correspondence-rules/
│   └── RULES.md                ← cross-viewpoint alignment rules (used by validation agent)
│
├── examples/                   ← reference artefacts (used as generation examples)
│   ├── guardrail-canvas-example.md
│   ├── trade-off-matrix-example.md
│   └── adr-example.md
│
├── spec/
│   └── FRAMEWORK-SPEC.md       ← master VAF specification document
│
├── foundation/
│   └── EPISTEMOLOGY.md         ← foundational principles loaded by agents
│
├── frameworks/                 ← supporting framework documents
├── guides/                     ← practitioner guides and operating manuals
├── research/                   ← ZenCloud research papers
├── templates/                  ← blank artefact templates
├── tools/                      ← compression maps and reference tools
│
├── vsf-scorer/                 ← standalone React tool (Vite) — VSF career scorer
│
├── Dockerfile                  ← multi-stage: builder + nginx/node runtime
├── nginx.conf                  ← proxies port 80 → Node port 3000
├── start.sh                    ← entrypoint: starts nginx + node
├── package.json
└── tsconfig.json
```

---

## Deployment

Push to `main`. GitHub Actions builds the Docker image, pushes to GHCR, deletes the existing Azure container, and creates a new one. The container is live at `vaf-architect.australiasoutheast.azurecontainer.io`.

Secrets required in the repository: `AZURE_CREDENTIALS`, `ANTHROPIC_API_KEY`, `GH_TOKEN`.

---

*ZenCloud Global Consultants · VAF Agentic Architect v2 · May 2026*
