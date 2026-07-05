# OrdoAnimi Unified Kanban — MVP & MLP
*The OrdoAnimi Framework | Owner: Phil Myint*
*Covers: velocityarchitectureframework.com · zencloudau.github.io/vaf-sa · OrdoAnimi Agent*
*Created: 2026-06-28 | Updated as work progresses*

---

## Definitions

**MVP** — Both sites are production-ready, internally consistent, and free of broken links, false claims, and structural gaps. ISO 42010 conformance is defensible. GitHub Pages serves correctly.

**MLP** — Both sites are genuinely excellent: complete, polished, cross-linked, with worked examples for everything and a coherent ecosystem a visitor can navigate.

---

## 🟥 MVP

### 🔵 Framework Site — velocityarchitectureframework.com (velocity-architecture repo)

| # | Item | File(s) | Source |
|---|------|---------|--------|
| M1 | Populate Stakeholder Register | `spec/FRAMEWORK-SPEC.md` §2 | REVIEW P1.1 |
| M2 | Populate Concern Register | `spec/FRAMEWORK-SPEC.md` §3 | REVIEW P1.1 |
| M3 | Fix conformance table — "Satisfied" is false for §2 and §3 | `spec/FRAMEWORK-SPEC.md` §8 | REVIEW P3 |
| M4 | Fix CR-E1 classification from "Hard rule" → "Mandatory" (or define "Hard rule" as a third tier) | `correspondence-rules/RULES.md` | REVIEW P1.4 |
| M5 | Resolve 14-Day Rule vs Tier 3 Pulse tension — clarifying note | `correspondence-rules/RULES.md` + `viewpoints/vp5-rhythm/pulse-system.md` | REVIEW P1.5 |
| M6 | Define S7 stakeholder (or renumber to remove the gap) | `spec/FRAMEWORK-SPEC.md` §2 | REVIEW P2.4 |
| M7 | Reconcile 7-column model and 6-viewpoint model in README — add bridging explanation | `README.md` | REVIEW P1.2 |
| M8 | Define Velocity Vault | New: `vault/README.md` | REVIEW P2.1 |
| M9 | Create Column 6 — `patterns/` directory with README + first pattern | New: `patterns/README.md` + `patterns/stalled-decision-pattern.md` | REVIEW P1.3 |
| M10 | Fix homepage book card — "thirty-three chapters" is stale; book is complete at 50 | velocityarchitectureframework.com homepage HTML | Site audit |
| M11 | Resolve version discrepancy — repo/spec says v1.0; OrdoAnimi Agent says "OrdoAnimi v2". Decide canonical version and align everywhere. | `spec/FRAMEWORK-SPEC.md`, `app/portal.html` | Agent audit |

### 🟠 OrdoAnimi Architecture Site — zencloudau.github.io/vaf-sa/

| # | Item | File(s) | Source |
|---|------|---------|--------|
| M12 | Fix GitHub Pages — site returns 404. Enable Pages in repo settings pointing to `master` branch (or rename `master` → `main`) | GitHub repo settings | Site audit |
| M13 | Fix OG meta URLs — all pages reference `zencloudau.github.io/OrdoAnimi-sa/` (trademark symbol in URL); should be `zencloudau.github.io/vaf-sa/` | All HTML files (`og:url` meta tags) | Site audit |
| M14 | Verify `workshop-playbook.html` exists and is complete (nav links to it but not confirmed) | `workshop-playbook.html` | Site audit |
| M15 | Verify `escalation-protocol.html` exists and is complete (nav links to it but not confirmed) | `escalation-protocol.html` | Site audit |
| M16 | Verify `cloud-reference/` exists and is complete (nav links to it but not confirmed) | `cloud-reference/index.html` | Site audit |
| M17 | Verify all 6 module pages exist and are complete | `modules/module-01` through `module-06` | Site audit |
| M18 | Verify all 4 engagement archetype pages exist | `engagement-archetypes/obfuscation.html`, `negligent-void.html`, `institutional-paralysis.html`, `silo.html` | Site audit |
| M19 | Verify all toolkit files exist (10 diagrams, 8 templates referenced in toolkit.html) | `diagrams/`, `templates/`, `toolkit/` | Site audit |
| M13 | Fix OG meta URLs — all pages reference `zencloudau.github.io/OrdoAnimi-sa/` (trademark symbol in URL) | All HTML files | Site audit |

### In Progress

*(none)*

### Done

| # | Item | Completed |
|---|------|-----------|
| M1 | Populate Stakeholder Register — S1–S10, S7 defined as Risk Officer / Risk Manager | 2026-06-28 |
| M2 | Populate Concern Register — C1–C14 with definitions and stakeholder mapping | 2026-06-28 |
| M3 | Fix conformance table — §2 and §3 now genuinely Satisfied | 2026-06-28 |
| M4 | Fix CR-E1 classification: "Hard rule" → "Mandatory"; classification system now consistent | 2026-06-28 |
| M5 | Resolve 14-Day / Tier 3 Pulse tension — clarifying note added to CR-E1 | 2026-06-28 |
| M6 | Define S7 stakeholder — Risk Officer / Risk Manager, VP1 + VP3 | 2026-06-28 |
| M7 | Reconcile 7-column and 6-viewpoint models — bridging section added to README | 2026-06-28 |
| M8 | Define Velocity Vault — `vault/README.md` created | 2026-06-28 |
| M9 | Create Column 6 — `patterns/README.md` + PAT-01 stalled-decision-pattern.md | 2026-06-28 |
| M10 | Fix homepage book card — "thirty-three chapters" → "all fifty chapters" | 2026-06-28 |
| M11 | Resolve version discrepancy — framework v1.0 canonical; Agent "VAF v2" was tool version, Agent now deprecated in repo | 2026-06-28 |
| M12 | Fix GitHub Pages — vaf-sa now serving from `master` branch | 2026-06-28 |
| M14 | Verify workshop-playbook.html — confirmed live and complete | 2026-06-28 |
| M15 | Verify escalation-protocol.html — confirmed live and complete | 2026-06-28 |
| M16 | Verify cloud-reference/ — confirmed live (AWS, Azure, GCP, OCI, Landing Zone) | 2026-06-28 |
| M17 | Verify all 6 module pages — confirmed live and complete | 2026-06-28 |
| M18 | Verify all 4 engagement archetype pages — confirmed live and complete | 2026-06-28 |
| M19 | Verify all toolkit files — 7 Mermaid + 3 PlantUML + 8 templates confirmed | 2026-06-28 |
| M13 | Fix OG meta URLs + GitHub footer link — `OrdoAnimi-sa` → `vaf-sa` across all HTML files | 2026-06-28 |

---

## 🟦 MLP

### 🔵 Framework Site

| # | Item | File(s) | Source |
|---|------|---------|--------|
| L1 | Patterns — add 2 more patterns (e.g. Escalation Failure, Architecture Theatre Trap) | `patterns/` | REVIEW P1.3 |
| L2 | Playbooks — first playbook: Onboarding a New Engagement | `patterns/onboarding-playbook.md` | REVIEW P2.5 |
| L3 | Worked example — Pulse Briefing (Cloud Platform Modernisation scenario) | New: `examples/pulse-briefing-example.md` | REVIEW P2.2 |
| L4 | Worked example — Pulse Report | New: `examples/pulse-report-example.md` | REVIEW P2.2 |
| L5 | Worked example — populated ADL (GC-20260101-001, TOM-20260115-001, ADR-001 indexed) | New: `examples/adl-example.md` | REVIEW P2.3 |
| L6 | Clarify `templates/` vs `viewpoints/` relationship — one canonical location | `README.md` + `templates/` | REVIEW P3.1 |
| L7 | Consolidate Pulse Briefing — 3 files → 1 canonical + links | `viewpoints/vp5-rhythm/pulse-system.md`, `viewpoints/vp5-rhythm/README.md`, `templates/pulse-briefing.md` | REVIEW P3.2 |
| L8 | Add Component 7 (Fitness Function Status) to VP4 README table | `viewpoints/vp4-velocity/README.md` | REVIEW P3.3 |
| L9 | Fix EPISTEMOLOGY.md — add "Eight Coined Concepts" as explicit section heading | `foundation/EPISTEMOLOGY.md` | REVIEW P3.4 |
| L10 | Clarify ADR-in-codebase vs ADL relationship | `viewpoints/vp3-truth/README.md` or `viewpoints/vp4-velocity/README.md` | REVIEW P3.5 |
| L11 | Fix LICENSE to be machine-readable (GitHub reports "Unknown") | `LICENSE` | REVIEW P3 |
| L12 | Add cross-link from README → vaf-sa site | `README.md` | Ecosystem |
| L13 | State publishing hierarchy explicitly in README | `README.md` | Ecosystem |
| L14 | Medium backlog — cross-post Chapters 31–50 | Medium @ZencloudAU | Ecosystem |

### 🟠 OrdoAnimi Architecture Site

| # | Item | File(s) | Source |
|---|------|---------|--------|
| L15 | Add cross-link from vaf-sa homepage → velocityarchitectureframework.com framework library | `index.html` | Ecosystem |
| L16 | Add cross-link from framework site → vaf-sa | velocityarchitectureframework.com | Ecosystem |
| L17 | Align lexicon terms with EPISTEMOLOGY.md coined concepts — Decision Altitude, Governance Drag, Pattern Locking map to OrdoAnimi coined concepts; ensure no contradictions | `lexicon.html` vs `foundation/EPISTEMOLOGY.md` | Content integrity |
| L18 | Add vaf-sa to site map at velocityarchitectureframework.com | velocityarchitectureframework.com/site-map.html | Ecosystem |

### 🤖 OrdoAnimi Agent

| # | Item | File(s) | Source |
|---|------|---------|--------|
| L19 | Document the OrdoAnimi Agent in CLAUDE.md and ECOSYSTEM-AUDIT.md | `CLAUDE.md`, `ECOSYSTEM-AUDIT.md` | Session audit |
| L20 | Align Agent "OrdoAnimi v2" branding once version decision is made (M11) | `app/portal.html` | Agent audit |
| L21 | Add link to OrdoAnimi Agent from framework site nav or guides | velocityarchitectureframework.com nav | Discoverability |

### In Progress

*(none)*

### Done

| # | Item | Completed |
|---|------|-----------|
| L1 | Patterns — PAT-02 (Escalation Failure) + PAT-03 (Architecture Theatre Trap) added to `patterns/` | 2026-06-28 |
| L2 | Onboarding Playbook — PBK-01 created: `patterns/onboarding-playbook.md` | 2026-06-28 |
| L3 | Worked example — Pulse Briefing (CloudFirst Banking scenario): `examples/pulse-briefing-example.md` | 2026-06-28 |
| L4 | Worked example — Pulse Report: `examples/pulse-report-example.md` | 2026-06-28 |
| L5 | Worked example — populated ADL at Week 7: `examples/adl-example.md` | 2026-06-28 |
| L6 | Templates/ vs viewpoints/ relationship clarified — `templates/README.md` created | 2026-06-28 |
| L7 | Pulse Briefing consolidation — canonical reference note added; `templates/pulse-briefing.md` is authoritative | 2026-06-28 |
| L8 | Component 7 (Fitness Function Status) added to VP4 README dashboard table | 2026-06-28 |
| L9 | EPISTEMOLOGY.md — "Eight Coined Concepts" added as explicit numbered section heading | 2026-06-28 |
| L10 | ADR-in-codebase vs ADL relationship — full explanation added to VP3 README and VP4 README | 2026-06-28 |
| L11 | LICENSE — SPDX headers added: machine-readable for GitHub | 2026-06-28 |
| L12 | Cross-link from README → vaf-sa — Ecosystem section added to README.md | 2026-06-28 |
| L13 | Publishing hierarchy stated in README — Publishing Platform table added | 2026-06-28 |
| L14 | Medium backlog (Chapters 31–50) — external platform action; deferred to Phil | — |
| L15 | vaf-sa homepage → framework library link updated to `/frameworks/` (was root); Agent link removed | 2026-06-28 |
| L16 | Framework site → vaf-sa cross-link — "Practitioner tools" section added to index.html | 2026-06-28 |
| L17 | Lexicon alignment — Framework Connection notes added to Decision Altitude, Governance Drag, Pattern Locking | 2026-06-28 |
| L18 | vaf-sa added to site-map.html — "Practitioner Tools" card with link | 2026-06-28 |
| L19 | Agent deprecated — CLAUDE.md updated; Agent nav links removed from all vaf-sa HTML files | 2026-06-28 |
| L20 | Agent branding — moot; Agent deprecated | — |
| L21 | Agent link in nav — moot; Agent deprecated; vaf-sa links updated to framework library | — |

---

## 🟩 Ecosystem (Naming resolved 2026-07-05 — transfers still pending)

| # | Item | Status |
|---|------|-----------|
| E1 | ~~Resolve Velocity trademark~~ | ✅ Resolved — framework renamed **The OrdoAnimi Framework** |
| E7 | ~~brand decision~~ | ✅ Resolved — **OrdoAnimi** is the single umbrella brand for the framework, the company, and the product line (Valour, Executive Fast Track). No separate framework brand. |
| E2 | Transfer velocity-architecture repo under the OrdoAnimi banner | Pending — destination org/repo location not yet finalised |
| E3 | Transfer ea-artefact-generator → OrdoAnimi/Fabrica | Pending Phil decision (unrelated to naming resolution) |
| E4 | Transfer velocity-academy → OrdoAnimi/Arcadium | Pending Phil decision (unrelated to naming resolution) |
| E5 | Archive/remove unused ZenCloudAU repos after audit | Repo audit (see the OrdoAnimi consolidation plan) |
| E6 | DNS fix: velocityarchitecture.com.au → Academy | Blocked on E4 |
| E8 | vaf-sa → transfer under the OrdoAnimi banner once E2 lands | Blocked on E2 |

---

## Work Order

**Immediate — unblock the sites:**
M12 (vaf-sa Pages fix) → M13 (OG URLs) → M14–M19 (verify vaf-sa content exists) → M10 (homepage book card)

**Framework spec sitting (one session):**
M1 → M2 → M3 → M6 (all in FRAMEWORK-SPEC.md)

**Rules sitting (one session):**
M4 → M5 (RULES.md + pulse-system.md)

**README + new files (one session):**
M7 → M8 → M9 (README, vault, patterns)

**Version decision (one conversation):**
M11 — decide v1.0 vs v2, then propagate

**MLP in priority order:**
L3/L4/L5 (worked examples) → L2 (onboarding playbook) → L1 (more patterns) → L17 (lexicon alignment) → L12–L13 (cross-links) → remaining polish

---

*OrdoAnimi Unified Kanban — The OrdoAnimi Framework*
*© 2026 Phil Myint / OrdoAnimi*
