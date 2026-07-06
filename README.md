# The OrdoAnimi Framework

This repository is the public knowledge base for OrdoAnimi. It contains the framework, formal specification, research, published policies, practitioner guidance, diagnostics, templates, examples and authored publications.

**Public site:** https://framework.ordoanimi.com/

---

## Framework Structure

OrdoAnimi operates through two complementary structures. Understanding both is required before working with any artefact.

### Six Viewpoints — the operational structure

The framework is ISO/IEC/IEEE 42010:2022 conformant. Its operational structure is six viewpoints, each with a defined instrument, layer, and concern set.

| ID  | Viewpoint    | Instrument                 | Layer      |
|-----|--------------|----------------------------|------------|
| VP1 | Direction    | Guardrail Canvas           | Enterprise |
| VP2 | Decision     | Trade-off Matrix           | Solution   |
| VP3 | Truth        | ADRs + Fitness Functions   | Technical  |
| VP4 | Velocity     | Dashboard + ADL + Vault    | Control    |
| VP5 | Rhythm       | Pulse System               | Operating  |
| VP6 | Practitioner | Integrity Arc              | Human      |

The viewpoints define what artefacts exist, what concerns they address, and what correspondence rules govern their relationships. See [`spec/FRAMEWORK-SPEC.md`](spec/FRAMEWORK-SPEC.md) for the full conformance declaration.

### Seven Columns — the teaching and publication structure

The framework is also expressed through seven columns used in the book, presentations, and practitioner training. The columns organise the same content into a practitioner sequence rather than an ISO ontology.

| Column | Name                  | VP equivalent                  |
|--------|-----------------------|--------------------------------|
| 1      | Trademark             | Meta-level (no VP)             |
| 2      | Operating Model       | Foundation Layer               |
| 3      | Operating Rhythm      | VP5                            |
| 4      | Delivery System       | VP4 (ADL + Velocity Vault)     |
| 5      | Architectural Control | VP4 (Dashboard)                |
| 6      | Pattern & Playbook    | VP2, VP3 (applied patterns)    |
| 7      | Practitioner          | VP6                            |

VP1, VP2, and VP3 operate across Columns 2-5 in execution — they are not assigned to a single column because decision-making spans enterprise, solution, and technical layers simultaneously.

**The relationship in one sentence:** the seven columns are how the framework is taught and published; the six viewpoints are how it operates and conforms to ISO 42010.

---

## Browse the knowledge base

| Area | Purpose |
|---|---|
| `foundation/` | Foundational concepts and principles |
| `spec/` | Formal specification and conformance material |
| `viewpoints/` | OrdoAnimi viewpoint definitions |
| `correspondence-rules/` | Cross-viewpoint consistency rules |
| `vault/` | Velocity Vault — the permanent decision archive |
| `patterns/` | Architecture patterns and practitioner playbooks |
| `frameworks/` | Framework explanations and reference material |
| `research/` | Research papers, evidence and bibliography |
| `guides/` | Practitioner guidance |
| `diagnostics/` | Public diagnostic instruments |
| `templates/` | Reusable public templates |
| `examples/` | Worked examples |
| `policies/` | Published policies |
| `leadership/` | Leadership application of the framework |
| `publications/` | Reader-facing Thought Series, Signal and book archive |
| `book/`, `series/`, `signals-series/` | Canonical publication source |

---

## Publication boundary

Only material approved for public readers belongs in this repository. Commercial collateral, partner operations, internal planning, unpublished drafts, application code, deployment records, local workspace files and production notes are maintained outside the public knowledge base.

Repository paths that support public URLs must be changed with corresponding navigation and compatibility updates.

---

## Tooling

| Script | Purpose |
|---|---|
| `tools/generate_pages.py` | Auto-generates reader HTML pages from MD files in `research/` and `publications/` |
| `tools/sync_nav.py` | Syncs canonical nav and footer across all site HTML pages. Run locally or via CI. |
| `tools/sync_nav.py --check` | CI mode — exits 1 if any page is out of sync |

The GitHub Actions workflow (`.github/workflows/publish-articles.yml`) runs on every push to `main` that touches `.md` files. It syncs nav/footer, lints for stale anchor links, then generates reader pages for any new articles.

Adding a new article: drop a `.md` file into `research/` or `publications/` and push — the workflow handles the rest.

---

## Publishing Platform

The primary publishing platform for all OrdoAnimi content is **framework.ordoanimi.com**, not Medium.

| Channel | Status | Notes |
|---------|--------|-------|
| [framework.ordoanimi.com/publications](https://framework.ordoanimi.com/publications/) | **Primary** | All 50 book chapters + Thought Series + Signal |
| [Medium @ZencloudAU](https://medium.com/@ZencloudAU) | Secondary | Book chapters serialised — Chapter 30 of 50 |
| [LinkedIn in/pmyint](https://www.linkedin.com/in/pmyint) | Professional | Active presence |

---

## Ecosystem

OrdoAnimi is published alongside the **OrdoAnimi Architecture** practitioner framework — a field-level framework for solution architects.

- **framework.ordoanimi.com** — this repository, the governing framework
- **[OrdoAnimi Architecture](https://architecture.ordoanimi.com/)** — practitioner tools, field lexicon, engagement archetypes, workshop playbook

---

## Start reading

- [Framework home](https://framework.ordoanimi.com/)
- [OrdoAnimi Architecture practitioner site](https://architecture.ordoanimi.com/)
- [Research](https://framework.ordoanimi.com/research/)
- [Publications](https://framework.ordoanimi.com/publications/)
- [Framework documents](https://framework.ordoanimi.com/frameworks/)
- [Guides](https://framework.ordoanimi.com/guides/)
- [Diagnostics](https://framework.ordoanimi.com/diagnostics/)
- [Policies](https://framework.ordoanimi.com/policies/)
- [Site map](https://framework.ordoanimi.com/site-map.html)

---

## Contribution and reuse

See `CONTRIBUTING.md`, `LICENSE.md`, `LICENCE-TERMS.md` and `SECURITY.md` for the applicable contribution, licensing, trademark and security terms.

(c) 2026 Phil Myint / OrdoAnimi.
