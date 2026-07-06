# CLAUDE.md — The OrdoAnimi Framework
*Project memory for Claude. Read this at the start of every session before doing any work on this project.*

---

## What This Project Is

**The OrdoAnimi Framework** is Phil Myint's primary intellectual property — a decision governance framework for enterprise and solution architecture, conformant with ISO/IEC/IEEE 42010:2022. It is also the underlying framework for a leadership extension that applies the same ideas to any organisational authority responsible for making decisions move.

This is not a side project. It is the primary framework, IP, and publishing platform for OrdoAnimi. Every change must maintain the integrity of the whole.

**Core thesis:**
> *Architecture exists to create clarity that leads to better decisions.*
> *Velocity is not speed. It is the rate at which ambiguity expires.*

**Owner:** Phil Myint, Principal Architect, The OrdoAnimi Group
**License:** CC BY 4.0 — free to use, attribution appreciated
**Copyright:** © 2026 Phil Myint / The OrdoAnimi Group

---

## Strategic Context (Background — Not Blocking Current Work)

**OrdoAnimi** (`github.com/OrdoAnimi`) is the single umbrella brand for everything Phil Myint publishes and builds — this framework, the Valour product console, and Executive Fast Track all sit under it. There is no longer a separate framework brand distinct from the company: this repository's public identity, the company's identity, and the product house's identity are all "OrdoAnimi." ZenCloudAU repos will migrate under this banner as each is ready; this is future work.

**Trademark note — resolved:** The "Velocity" trademark issue is settled. The framework is renamed **The OrdoAnimi Framework**. ZenCloud and StudioSix are retired entirely, not carried forward as sub-brands. The book's use of "velocity" as a philosophical concept (the rate at which ambiguity expires) is untouched — that's the framework's own vocabulary, not the retired brand name.

---

## The Ecosystem — All Working Sites and Artefacts

### Primary Repository
- **GitHub:** https://github.com/ZenCloudAU/velocity-architecture
- **Local mirror:** `D:\VelocityArchitecture\`
- **Public site:** https://framework.ordoanimi.com/
- **Status:** Public, v1.0

**Critical:** The repo IS the website backend. A GitHub Actions workflow (`.github/workflows/publish-articles.yml`) runs on every push to `main` that touches `.md` files — it syncs nav/footer, lints stale anchors, and auto-generates HTML reader pages from MD files in `research/` and `publications/`. Do not push broken Markdown.

### Publishing Channels
- **framework.ordoanimi.com/publications** — ALL 50 book chapters published + Thought Series + Signal. **This is the primary publishing platform, not Medium.**
- **Medium @ZencloudAU** — Book chapters serialised; at Chapter 30 of 50 (secondary discovery channel — 20 chapters behind)
- **LinkedIn in/pmyint** — Professional presence; active
- **www.ordoanimi.com** — OrdoAnimi client entry point (was zencloud.com.au)

### Related Artefacts (Off-Repo)
- **OrdoAnimi Book** — 50 chapters complete, published on framework.ordoanimi.com (Book 1 — Architecture domain)
- **Leadership Book** — Book 2; same OrdoAnimi framework, leadership language. Seed: `leadership/LEADERSHIP-EXTENSION.md`
- **The Living Bible for Enterprise & Solution Architects** — domain knowledge reference base (location TBC — confirm with Phil)
- **Presentation materials / slide decks** — exist for client and conference use (location TBC)

### The Legacy Agent (Deprecated, internally "VAF v2")
- A separate product, internally called "VAF v2" in the old UI, hosted at `framework.ordoanimi.com/app/portal.html`
- It has been **deprecated** — the portal.html page now redirects to the framework site
- Nav links to it have been removed from vaf-sa (all HTML files cleaned in Session 2)
- It is NOT part of the current framework or publishing stack, and not part of the OrdoAnimi brand
- Do not add links to `app/portal.html` anywhere in either repo

### Working Folders
- Local repo files: `D:\VelocityArchitecture\`
- Review file: `D:\VelocityArchitecture\REVIEW.md`
- Ecosystem audit: `D:\VelocityArchitecture\ECOSYSTEM-AUDIT.md`

---

## Framework Structure — What You Must Know Before Touching Anything

### The Six Viewpoints (primary operational structure)

| ID | Viewpoint | Instrument | Layer | Files |
|----|-----------|------------|-------|-------|
| VP1 | Direction | Guardrail Canvas | Enterprise | `viewpoints/vp1-direction/` |
| VP2 | Decision | Trade-off Matrix | Solution | `viewpoints/vp2-decision/` |
| VP3 | Truth | ADRs + Fitness Functions | Technical | `viewpoints/vp3-truth/` |
| VP4 | Velocity | Dashboard + ADL | Control | `viewpoints/vp4-velocity/` |
| VP5 | Rhythm | Pulse System | Operating | `viewpoints/vp5-rhythm/` |
| VP6 | Practitioner | Integrity Arc | Human | `viewpoints/vp6-practitioner/` |

### The Seven Columns (book/presentation structure — maps onto viewpoints)

| Column | Name | VP equivalent |
|--------|------|---------------|
| 1 | Trademark | Meta-level (no VP) |
| 2 | Operating Model | Foundation Layer |
| 3 | Operating Rhythm | VP5 |
| 4 | Delivery System | VP4 (ADL + Vault) |
| 5 | Architectural Control | VP4 (Dashboard) |
| 6 | Pattern & Playbook | NOT YET CREATED — gap to fill |
| 7 | Practitioner | VP6 |

**VP1, VP2, VP3 sit across Columns 2–5 in execution.** The column model is the book/teaching structure; the viewpoint model is the ISO 42010-conformant operational structure. A bridging explanation is needed in the README (tracked in REVIEW.md P1).

### Foundation Layer
`foundation/EPISTEMOLOGY.md` — sits beneath all viewpoints. Not a viewpoint itself. Contains the philosophical warrant for the entire framework.

**Eight coined concepts** (the framework's core vocabulary — precise terms, use carefully):
1. Velocity of Truth
2. Integrity Gap
3. Decision Latency
4. Expiry
5. Control Paradox
6. Auctor Custos
7. Architecture Theatre
8. Responsibility Diffusion

These terms must never be altered, diluted, or used carelessly. They are the IP.

---

## Artefact Hierarchy and Correspondence Rules

```
Guardrail Canvas (VP1 — GC-YYYYMMDD-XXX)
    └── Trade-off Matrix (VP2 — TOM-YYYYMMDD-XXX)  [must reference governing Canvas]
            └── ADR (VP3 — ADR-NNN)                  [must reference governing TOM]
                    └── Fitness Functions              [must reference ADR or TOM]

All of the above indexed in:
    └── ADL (VP4 — adl-template.md)
            └── Velocity Dashboard (VP4 — velocity-dashboard.md)
                    └── Pulse Sessions (VP5 — pulse-system.md)
                            └── Practitioner assessment (VP6 — integrity-arc.md)
```

### Correspondence Rules (17 total — must be maintained on every change)

| ID | Rule | What it means in practice |
|----|------|--------------------------|
| CR-T1 | TOM → Canvas | Every Trade-off Matrix must reference a Guardrail Canvas |
| CR-T2 | ADR → TOM | Every ADR must reference a Trade-off Matrix |
| CR-T3 | Supersession traceability | Never delete — always supersede with a new record |
| CR-T4 | Fitness Function → ADR/TOM | Every fitness function must carry a comment reference |
| CR-E1 | 14-Day Decision Aging | Open decisions >14 days trigger mandatory escalation |
| CR-E2 | Scope compression on escalation | Escalations narrow — they never widen |
| CR-E3 | Escalation terminal condition | Every escalation carries a defined binding point |
| CR-E4 | Pulse escalation window | Max two Pulse cycles before binding |
| CR-O1 | Single named owner | No committee ownership anywhere |
| CR-O2 | Ownership Map currency | Update within 5 business days of any ownership transfer |
| CR-O3 | Practitioner scope declaration | Written scope for engagements >3 months |
| CR-L1 | Enterprise layer constraint | Canvases must not prescribe technology or solutions |
| CR-L2 | Solution layer decisiveness | TOMs must produce commitment sufficient for delivery to begin |
| CR-L3 | Technical layer feedback | VP3 findings that invalidate upstream assumptions must escalate |
| CR-L4 | No layer substitution | No layer may substitute for another |
| CR-X1 | Ambiguity lifespan | Every open question must have an expiry date |
| CR-X2 | Revisitation criteria | Decisions may only be reopened under defined conditions |
| CR-X3 | Canvas review date | Every canvas carries a Review Date; expired = inactive |

---

## Artefact ID Conventions

| Artefact | ID format | Example |
|----------|-----------|---------|
| Guardrail Canvas | GC-YYYYMMDD-NNN | GC-20260101-001 |
| Trade-off Matrix | TOM-YYYYMMDD-NNN | TOM-20260115-001 |
| ADR | ADR-NNN | ADR-001 |
| Risk | RISK-NNN | RISK-001 |

---

## Stakeholder Register (S1–S10)

| ID | Stakeholder | Primary viewpoints |
|----|-------------|-------------------|
| S1 | Enterprise Architect | VP1, VP2 |
| S2 | Solution Architect | VP2, VP3 |
| S3 | Technical Architect / Engineer | VP3 |
| S4 | Delivery Lead | VP2, VP5 |
| S5 | Executive / CIO / CTO | VP1, VP5 |
| S6 | Architecture Review Board | VP1, VP4 |
| S7 | [TO CONFIRM — not yet defined in repo] | TBC |
| S8 | Auditor / Compliance Officer | VP3 |
| S9 | Delivery Team Member | VP2, VP3 |
| S10 | Client / Sponsor | VP1 |

*Note: S7 is referenced in the numbering sequence but not yet defined. Needs resolution.*

---

## Concern Register (C1–C14)

| ID | Concern |
|----|---------|
| C1 | Decision clarity |
| C2 | Decision velocity |
| C3 | Decision traceability |
| C4 | Direction coherence |
| C5 | Layer separation |
| C6 | Trade-off visibility |
| C7 | Architectural integrity |
| C8 | Governance effectiveness |
| C9 | Practitioner integrity |
| C10 | Responsibility diffusion |
| C11 | Decision latency |
| C12 | Technical truth |
| C13 | Alignment with intent |
| C14 | Knowledge preservation |

---

## Known Issues — Open Review Findings (2026-06-28)

Full detail in `REVIEW.md`. Summary for session awareness:

### Priority 1 — Structural (blocking)
- [ ] `spec/FRAMEWORK-SPEC.md` §2 and §3 are placeholders — Stakeholder Register and Concern Register not populated
- [ ] 7-column model and 6-viewpoint model not reconciled in README
- [ ] Column 6 (Pattern & Playbook) — no directory, no content, zero artefacts
- [ ] CR-E1 classified as "Hard rule" — orphan category not defined in the classification system
- [ ] 14-Day Rule (CR-E1) vs. monthly Tier 3 Pulse (CR-E4) tension unresolved

### Priority 2 — Content gaps
- [ ] Velocity Vault — named in Column 4 but never defined
- [ ] No Pulse Briefing or Pulse Report worked example
- [ ] No ADL worked example
- [ ] Engagement onboarding guide missing
- [ ] S7 stakeholder not defined

### Priority 3 — Polish
- [ ] `templates/` directory relationship to `viewpoints/` templates unclear
- [ ] Pulse Briefing content duplicated across `pulse-system.md`, VP5 README, and `templates/`
- [ ] Velocity Dashboard has 7 components; VP4 README table lists only 6
- [ ] EPISTEMOLOGY.md header says "Five Core Premises" — doesn't signal the 8 coined concepts that follow
- [ ] ADR-in-codebase vs. ADL relationship not explained
- [ ] FRAMEWORK-SPEC.md conformance table says "Satisfied" for placeholder sections (false)
- [ ] `LICENSE` not machine-readable (GitHub reports "Unknown")

---

## File Map — Full Repository

```
D:\VelocityArchitecture\ (github.com/ZenCloudAU/velocity-architecture)
│
├── CLAUDE.md                          ← This file
├── SKILL.md                           ← OrdoAnimi working skill for Claude
├── REVIEW.md                          ← Full review (2026-06-28)
├── ECOSYSTEM-AUDIT.md                 ← Full ecosystem audit (2026-06-28, updated Session 2)
├── README.md                          ← Public-facing framework overview
├── CONTRIBUTING.md
├── CITATION.cff
├── LICENSE / LICENSE.md / LICENCE-TERMS.md
├── SECURITY.md
│
├── spec/
│   └── FRAMEWORK-SPEC.md             ← ISO 42010 conformant spec (§2, §3 are stubs — P1)
│
├── foundation/
│   └── EPISTEMOLOGY.md               ← 5 premises + 8 coined concepts
│
├── viewpoints/
│   ├── vp1-direction/
│   │   ├── README.md
│   │   └── guardrail-canvas.md
│   ├── vp2-decision/
│   │   ├── README.md
│   │   └── trade-off-matrix.md
│   ├── vp3-truth/
│   │   ├── README.md
│   │   ├── adr-template.md
│   │   └── fitness-function-examples.md
│   ├── vp4-velocity/
│   │   ├── README.md
│   │   ├── adl-template.md
│   │   └── velocity-dashboard.md
│   ├── vp5-rhythm/
│   │   ├── README.md
│   │   └── pulse-system.md
│   └── vp6-practitioner/
│       ├── README.md
│       └── integrity-arc.md
│
├── correspondence-rules/
│   └── RULES.md                      ← All 17 rules
│
├── frameworks/                        ← Framework explanations and reference material
├── research/                          ← Research papers, evidence, bibliography
│                                        Feeds auto-generated HTML via tools/generate_pages.py
├── guides/                            ← Practitioner guidance
├── diagnostics/
│   ├── decision-velocity-diagnostic.md
│   └── organisation-health-check.md
│
├── templates/                         ← Standalone templates (relationship to viewpoints/ TBC — P3)
│   ├── guardrail-canvas.md
│   ├── trade-off-matrix.md
│   ├── adr.md
│   └── pulse-briefing.md
│
├── policies/                          ← Published governance and responsible-use policies
│
├── leadership/
│   └── LEADERSHIP-EXTENSION.md       ← Book 2 seed
│
├── examples/
│   ├── guardrail-canvas-example.md  ← GC-20260101-001
│   ├── trade-off-matrix-example.md  ← TOM-20260115-001
│   └── adr-example.md               ← ADR-001
│
├── publications/                      ← Reader-facing Thought Series, Signal, book archive
│                                        Feeds auto-generated HTML via tools/generate_pages.py
├── book/                              ← Canonical book source (all 50 chapters)
├── series/                            ← Thought Series canonical source
├── signals-series/                    ← Signal canonical source
│
├── tools/
│   ├── generate_pages.py             ← Auto-generates reader HTML from MD in research/ and publications/
│   └── sync_nav.py                   ← Syncs canonical nav/footer across all site HTML pages
│
├── .github/
│   └── workflows/
│       └── publish-articles.yml      ← CI: sync nav, lint anchors, generate reader pages on MD push
│
└── [TO CREATE]
    ├── patterns/                      ← Column 6 — Pattern & Playbook (P1 gap)
    ├── vault/                         ← Velocity Vault specification (P2 gap)
    └── onboarding/                    ← Engagement onboarding guide (P2 gap)
```

---

## Working Conventions

### Before Making Any Change
1. Check `REVIEW.md` — does this change address an open finding?
2. Identify which viewpoint(s) and correspondence rule(s) are affected
3. Check artefact hierarchy — does a change here require downstream updates?
4. Never delete — supersede with a new record and retain the old one
5. **If the change touches `.md` files under `research/` or `publications/`, the GitHub Actions pipeline will auto-generate HTML on push. Ensure the Markdown is clean.**

### When Creating New Artefacts
- Use the correct ID format (see Artefact ID Conventions above)
- Every new TOM must reference a Guardrail Canvas (CR-T1)
- Every new ADR must reference a TOM (CR-T2)
- Every new fitness function must carry a comment reference (CR-T4)
- Every new open question must have an expiry date (CR-X1)
- Every new decision must have a single named owner (CR-O1)

### When Editing Existing Files
- Do not modify a decided/accepted artefact — create a new one that supersedes it (CR-T3)
- Update the ADL index when any decision changes status
- Update the Velocity Dashboard ownership map within 5 business days of any ownership change (CR-O2)

### Language and Tone
- The coined terms are precise — use them exactly as defined in EPISTEMOLOGY.md
- Avoid hedging. The framework's voice is assertive. Architecture exists to produce decisions, not analysis.
- "We choose X" not "we recommend considering X"
- Every artefact is judged by one test: *Did this help someone decide?*

### Publishing Synchronisation
When content is updated in the repo, consider whether it needs to be reflected in:
- framework.ordoanimi.com (automated for `research/` and `publications/` via GitHub Actions — manual for all other directories)
- Medium articles (especially if a coined concept definition changes)
- LinkedIn series
- The book (in `book/`)
- The Leadership Extension

Changes to coined concepts or correspondence rules are the highest-risk changes — they ripple across all publishing channels simultaneously.

---

## Session Startup Checklist

At the start of any working session on this project:
1. Read this file
2. Check `REVIEW.md` for current open issues
3. Confirm which P1 issues remain unresolved
4. Ask Phil which area he wants to work on today
5. Before any edit, identify the affected viewpoint and correspondence rules

---

*CLAUDE.md — The OrdoAnimi Framework*
*Created: 2026-06-28 | Updated: 2026-06-28 (Session 2) | Owner: Phil Myint / OrdoAnimi*
*Update this file whenever the project structure, ecosystem, or working conventions change.*
