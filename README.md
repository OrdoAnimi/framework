# Velocity Architecture Framework

Velocity Architecture Framework(TM) is a practical architecture framework and tooling ecosystem for enterprise architecture, solution architecture, decision governance, and AI-assisted delivery.

**Framework site:** [velocityarchitectureframework.com](https://velocityarchitectureframework.com)

**Reader-facing GitHub Pages site:** [zencloudau.github.io/velocity-architecture](https://zencloudau.github.io/velocity-architecture/)

## Start Here

If you landed in this repository from LinkedIn, Medium, Substack, ZenCloud, or a search result, use the rendered pages first rather than raw GitHub files.

| Need | Use this |
|---|---|
| Understand the framework | [Framework home](https://zencloudau.github.io/velocity-architecture/) |
| Navigate the whole public site | [Public site map](https://zencloudau.github.io/velocity-architecture/site-map.html) |
| Read research papers | [Research reader](https://zencloudau.github.io/velocity-architecture/research/) |
| Read the IT governance working paper | [A Comparative Analysis of IT Governance Frameworks](https://zencloudau.github.io/velocity-architecture/research/it-governance-frameworks-australian-public-sector-2025-2026/) |
| Use the VAF agent | [VAF Agentic Architect](https://velocityarchitectureframework.com) |
| Browse source files | Continue in this GitHub repository |

GitHub is the source of truth. GitHub Pages is the reader-facing publication layer.

## Purpose

Velocity Architecture Framework exists to reduce architecture drag: unclear decision ownership, governance theatre, disconnected artefacts, and slow movement from architecture intent to delivery action.

This repository combines the framework material, practitioner guidance, templates, generated artefacts, research, and an agentic architecture application that can generate VAF-aligned outputs from a structured request.

The goal is not to create more documentation volume. The goal is to make architecture decisions explicit, traceable, and usable.

## Who It Is For

- Enterprise architects responsible for decision governance, strategic alignment, and architecture operating models.
- Solution architects working in complex delivery environments with unclear ownership, vendor pressure, or incomplete documentation.
- Architecture governance teams that need clearer artefacts, viewpoints, and cross-artefact alignment rules.
- Consultants and delivery leads using StudioSix or ZenCloudAU methods to turn architecture thinking into working assets.
- Practitioners exploring AI-assisted architecture delivery without removing professional accountability.

## What It Does

The repository currently contains two related bodies of work:

1. **The framework:** VAF specifications, viewpoints, correspondence rules, examples, templates, guides, research, and supporting documents.
2. **The tooling:** A TypeScript/Node.js application that accepts an architecture request, loads VAF knowledge, runs specialised generation agents, validates output alignment, and can commit generated artefacts back to the repository.

The application supports these artefact types in the current code:

- Governance
- Strategy
- Design
- Velocity
- Rhythm
- Practitioner

The Express app exposes:

- `GET /` - portal UI
- `GET /health` - health check
- `GET /status` - operational status
- `POST /artefacts/generate` - generate EA artefacts

## What Is Inside This Repo

Key areas in the current repository:

| Path | Purpose |
|---|---|
| `app/` | TypeScript application source, Express routes, orchestrator, agents, knowledge loader, GitHub action engine, logging, and shared types |
| `app/agents/` | Specialised generation agents for governance, strategy, design, velocity, rhythm, practitioner, and validation |
| `artefacts/` | Generated architecture artefacts organised by type |
| `viewpoints/` | VAF viewpoint specifications and instruments |
| `correspondence-rules/` | Cross-viewpoint alignment rules used by the validation layer |
| `examples/` | Reference examples for framework-aligned artefacts |
| `foundation/` | Foundational principles used by the framework and tooling |
| `frameworks/` | Supporting framework documents |
| `guides/` | Practitioner guides and operating material |
| `research/` | ZenCloud research papers and supporting analysis |
| `templates/` | Blank artefact templates |
| `tools/` | Supporting tools and reference material |
| `website/` | Website material for the framework presence |
| `vsf-scorer/` | Standalone Vite-based scoring tool inside the broader repository |

Operational files currently present include:

- `Dockerfile`
- `nginx.conf`
- `start.sh`
- `deploy.yml`
- `.github/workflows/deploy.yml`
- `tsconfig.json`
- `package.json`
- `vaf-architecture-v2.json`

## How It Fits the Ecosystem

Velocity Architecture Framework is the centre of the architecture ecosystem.

- **VAF-SA** is the solution architecture delivery module. It translates VAF thinking into field practice for solution architects working in stalled, unclear, or politically difficult engagements.
- **EA Artefact Generator** is a practical workspace for generating structured EA outputs and export-ready repository content.
- **StudioSix** is the commercial delivery wrapper for architecture-led AI delivery, using VAF methods and tools as part of client-facing work.
- **Certification repositories** such as SAP EA, Azure SA, CISSP, and agentic AI certification support the learning and credibility layer around enterprise architecture, cloud architecture, security architecture, and AI-assisted delivery.
- **ZenCloudAU** is the public GitHub organisation and consulting context for the ecosystem.

This repo should remain the source of truth for the core framework and the agentic architecture platform. Adjacent tools should link back here rather than duplicate the framework.

## Tech Stack

Confirmed from the current files:

- TypeScript
- Node.js 20+
- Express
- Anthropic SDK
- Axios
- dotenv
- Pino logging
- Jest / ts-jest
- ESLint
- Prettier
- Docker
- nginx
- GitHub Actions
- Azure deployment configuration

The repo also contains static HTML and website/framework assets.

## How to Run Locally

Commands confirmed from `package.json`:

```bash
npm install
npm run dev
```

Build and run compiled output:

```bash
npm run build
npm start
```

Other available scripts:

```bash
npm test
npm run lint
npm run format
```

`npm run dev` runs `ts-node app/app.ts`. The app uses port `3000` by default unless configured otherwise.

## Environment Configuration

The app uses environment configuration for runtime behavior. Current code references environment variables for:

- server port
- runtime environment
- log level
- VAF knowledge-base URL and cache TTL
- GitHub owner/repo targeting
- GitHub token used by the action engine

The previous README also documented an Anthropic API key requirement for generation.

Do not commit real environment files or secrets. Use example configuration only for documentation.

## Project Status

Usable.

The repository contains substantial framework material and a working TypeScript application structure. It is not yet product-ready because the public packaging still needs clearer demo boundaries, stronger onboarding, and cleaner separation between framework source, generated artefacts, and operational deployment material.

## Roadmap

Near-term improvements:

- Add a concise architecture diagram showing request intake, knowledge loading, agent generation, validation, and artefact publishing.
- Clarify which deployment endpoint is the primary public demo.
- Separate framework user onboarding from developer/operator onboarding.
- Add a short relationship map linking VAF, VAF-SA, EA Artefact Generator, StudioSix, and certification repositories.
- Review whether generated artefacts should remain in the main repository or move to examples/output storage.
- Add a contributor-safe environment setup section using placeholders only.

## Security and Data Notes

This project can use external AI and GitHub integrations. Architecture requests may be processed by an AI provider and generated artefacts may be committed back to GitHub depending on configuration.

Do not submit confidential client data, credentials, regulated information, or private environment values unless the deployment, storage, and provider controls are explicitly approved for that use.

Environment files such as `.env` should remain local and must not be committed.

## License

Licensed under CC BY 4.0. See LICENSE.md for terms.
Velocity Architecture Framework™ is a trademark of ZenCloud Consulting (Class 42).

---

# Velocity Architecture

Public professional framework and standards authority.

## Place In Ordo Animi

Velocity Architecture is part of the Ordo Animi institutional estate. Authoritative for professional method and public framework standards.

The canonical institutional relationship is:

- Magister Automatorum governs the estate.
- Imperium determines what deserves investment.
- Mercatus takes products to market.
- Velocity Architecture defines the professional method.
- Lex defines policy and processing rules.
- Ordo Animi operates the intelligence and user experience.
- Civitas manages identity, organisations, engagements and authority.
- Memoria manages approved and consented runtime context.
- Fabrica produces canonical artefacts.
- Probatio validates claims and evidence.
- Archivum preserves artefacts, evidence and engagement history.
- Nexus transfers canonical objects into external systems.
- Praesidium protects infrastructure, deployments and supply chains.
- Specula observes runtime and governance behaviour.
- Forma provides shared experience and design standards.
- Arcadium presents authorised Archivum content to clients.

## Current Maturity

v0.1 Fundamentum - constitutional baseline.

## Contains

accepted product, framework, documentation and constitutional governance files.

## Does Not Contain

This repository does not own client-specific artefacts, runtime policy enforcement, credentials, private Ordo Animi implementation, claims of universal certification or automatic compliance. During v0.1 it must not add application code, deployment automation, dependencies, workflows, credentials, or external integrations.

## v0.1 Baseline Status

The v0.1 constitutional package is established when the files below exist, validate, and are marked Perfectum in KANBAN.md.

## Constitutional Documents

- [Charter](CHARTER.md)
- [Agent Instructions](AGENTS.md)
- [Security](SECURITY.md)
- [Data Rules](DATA.md)
- [Interfaces](INTERFACES.md)
- [Roadmap](ROADMAP.md)
- [Kanban](KANBAN.md)
- [Architecture](docs/architecture/README.md)
- [Decisions](docs/decisions/README.md)
- [Releases](docs/releases/README.md)
- [Schemas](schemas/README.md)
- [Examples](examples/README.md)
