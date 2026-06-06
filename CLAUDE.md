# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Who I Am

**Phil Myint** — Principal Architect, ZenCloud Global Consultants, Brisbane.

I have zero coding background. I think in systems, decisions, and frameworks. I have designed, directed, and shipped live production software to Azure using Claude as my implementation layer. That is the model we use.

---

## How We Work

**I direct. Claude writes.**

- I define the problem, the constraints, and the outcome. Claude writes all code.
- I read and review output. I do not edit code manually.
- Execute-only. No filler, no commentary outside the task, no unsolicited suggestions.
- If you need a file to proceed, ask for it. Do not assume.

**Fix everything in one pass.**

- Before touching any file: read every relevant file, identify all issues, resolve everything in a single complete implementation.
- Never fix one file without checking what it connects to. Map dependencies first.
- No incremental patches. No "this should work, try it and see." Deliver the complete, correct solution.

**One complete fix, not a sequence of attempts.**

- If something is broken, find the root cause. Do not treat symptoms.
- If a path is referenced in multiple files, find all references before changing any of them.
- If a config value is used downstream, trace it downstream before committing to a change.

---

## Active Repos

### VAF Agentic Architect
**Repo:** github.com/ZenCloudAU/velocity-architecture  
**Live:** http://velocityarchitectureframework.com  
**Stack:** TypeScript 5.3, Node.js 20, Express 4.18, Anthropic SDK (claude-sonnet-4-6), Docker, GitHub Actions, Azure Container Instances  
**Azure:** Resource group `vaf-rg` · Container `vaf-agentic-architect` · Region `australiasoutheast` · IP `20.190.118.105`  
**Registry:** `ghcr.io/zencloudau/velocity-architecture:latest`  
**Secrets:** `AZURE_CREDENTIALS`, `ANTHROPIC_API_KEY`, `GH_TOKEN`  
**Architecture:** Express → Orchestrator → [gc-agent | tom-agent | adr-agent] → Claude API; kb-loader reads VAF KB from GitHub; action-engine commits artefacts back to the repo

### VAF Solution Architecture Framework
**Repo:** github.com/ZenCloudAU/vaf-sa  
**Stack:** Static HTML/CSS — published framework

### Agentic Cert Study Hub
**Repo:** github.com/ZenCloudAU/agentic-cert  
**Stack:** Markdown — CCA-F and GH-600 study content

### ZenCloud OS Automation
**Repo:** github.com/ZenCloudAU/zencloud-os  
**Stack:** Python — daily workflow automation scripts

### Learn With Claude
**Repo:** github.com/ZenCloudAU/learn-with-claude (this repo)  
**Stack:** Markdown — structured learning and reference documentation

---

## Ecosystem Design System

These standards apply to all three sites. Never deviate without explicit instruction.

### Three-Site Ecosystem
- **ZenCloud** (`zencloud.com.au`) — advisory front door, React + TypeScript + Vite
- **StudioSix** (`studiosix.com.au`) — AI delivery engine, React + TypeScript + Vite
- **VAF** (`velocityarchitectureframework.com`) — open method vault, static HTML/CSS

### Triumvirate Footer Rule
Each site footer links ONLY to the other two sites + GitHub. No Medium, no LinkedIn, no other links.
- ZenCloud footer: StudioSix · Velocity · GitHub
- StudioSix footer: ZenCloud Advisory · Velocity · GitHub
- VAF footer: ZenCloud · StudioSix · GitHub

### Colour Tokens
| Token | Value | Use |
|-------|-------|-----|
| Orange / Accent | `#E8630A` | CTAs, section labels, hover bars |
| Navy | `#1E3A5F` | Dark panels, footer bg |
| Page bg | `#f8fafc` | Page background |
| Border | `#e2e8f0` | Card/section borders |

### Typography
| Role | Font | Use |
|------|------|-----|
| Display / headings | Playfair Display, serif | h1, h2, h3, nav wordmarks |
| Body | DM Sans, sans-serif | All body copy |
| Labels / CTAs | DM Mono, monospace | Section labels, nav CTAs, eyebrows |

**DM Mono rules:** uppercase · `letter-spacing: 0.18em` (section labels) · `letter-spacing: 0.1em` (CTAs) · `border-radius: 4px` on CTA buttons — this is the ecosystem fingerprint.

### Nav Standards (all three sites)
- Height: **64px** exactly
- Nav CTA: DM Mono, uppercase, `border-radius: 4px`, orange bg
- ZenCloud: "Book Health Check" · StudioSix: "Start via ZenCloud" · VAF: "ZenCloud Advisory →"

### Dark Panel Pattern
Right-column hero aside (ZenCloud) and hero-panel (StudioSix):
- Background: `#1E3A5F` (navy) · 3px orange top bar · no border
- Label: DM Mono orange · Heading: Playfair Display `#f1f5f9` · Body: `rgba(241,245,249,0.68)`

### Card Hover State
Orange top bar slides in from left on hover (`::before` scaleX 0→1, transform-origin: left).

### Brand Marks
Always ™ on first use: ZenCloud™ Advisory · StudioSix™ · Velocity Architecture Framework™

### StudioSix Narrative
StudioSix IS the AI. Never name the underlying model. "Agents draft. Architect reviews. Clients receive."

### ZenCloud Responsive System
All ZenCloud grid layouts use named CSS classes in `src/App.css` — never inline `gridTemplateColumns`. Breakpoints: 960px (tablet) and 768px (mobile). Named classes:
- `.zc-hero-grid` · `.zc-services-grid` · `.zc-about-inner` · `.zc-ecosystem-grid`
- `.zc-offers-*` · `.zc-nav-links` + `.zc-nav-toggle` (hamburger at 768px)

### StudioSix Responsive System
Responsive CSS is in `src/App.css`. Key breakpoints: 900px (grids collapse) and 720px (full mobile). Already complete — do not rebuild.

### VAF Responsive System
Responsive CSS is embedded in `index.html`. Uses `auto-fit minmax()` grids + explicit breakpoints for footer/artefacts/ecosystem. Already complete — do not rebuild.

---

## Rules for Every Session

1. **Read before writing.** Read every file that could be affected before changing anything.
2. **Map dependencies.** Understand what connects to what. A change in one file may break three others.
3. **One complete implementation.** Deliver the full solution. Do not deliver a partial fix with instructions to "try this."
4. **No placeholders.** No `// TODO`, no `[your value here]`, no stubs. Everything in the output must be production-ready.
5. **Own the path.** If you identify a problem adjacent to the task, fix it. Do not deliver a correct solution sitting next to a broken one.
