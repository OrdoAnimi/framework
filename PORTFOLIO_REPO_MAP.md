# Portfolio Repository Map

**ZenCloud Global Consultants / Velocity Architecture Ecosystem**  
Classification: Internal Planning  
Version: 1.0 — May 2026

---

## Overview

This document inventories the current GitHub repository portfolio, classifies each repo by its role in the ecosystem, and defines what each should become.

**Governing principle:** Repos remain separate. The correct model is separate repos with shared naming conventions, README standards, brand system, and a central portfolio map (this document).

Do not consolidate everything into one repo. Consolidation destroys context, history, and the ability to manage public vs private independently.

---

## Categories

| Code | Category |
|------|----------|
| **FIP** | Framework / IP |
| **PAC** | Practitioner / Academy |
| **TLP** | Tool / Product |
| **SSM** | StudioSix Media / Products |
| **CRL** | Certification / Learning |
| **LAB** | Labs / Personal Research |
| **PFF** | Planned Future Frameworks |

---

## Repository Inventory

---

### velocity-architecture

| Field | Value |
|-------|-------|
| **Current name** | velocity-architecture |
| **Proposed future name** | velocity-architecture *(no change — control plane repo)* |
| **Category** | FIP — Framework / IP |
| **Current role** | VAF Agentic AI application, GitHub Pages portal, architecture artefacts, planning documents |
| **Future role** | Parent / control-plane repo for the Velocity ecosystem. Hosts VAF Agentic AI, planning documents, engagement pack, brand system, portfolio map. Acts as the canonical reference for ecosystem governance. |
| **Public / private** | Public |
| **Live URL** | http://velocityarchitectureframework.com |
| **Rename risk** | None — keep as-is |
| **README update required** | Yes — update to reflect parent repo role and link to planning docs |
| **GitHub description suggestion** | Velocity Architecture Framework — decision-first enterprise architecture ecosystem and VAF Agentic AI |
| **Move / merge decision** | Retain. This is the ecosystem control plane. |

---

### vaf-sa

| Field | Value |
|-------|-------|
| **Current name** | vaf-sa |
| **Proposed future name** | vaf-sa *(or velocity-sa)* |
| **Category** | FIP — Framework / IP |
| **Current role** | Static HTML/CSS — published Solution Architecture Framework |
| **Future role** | Velocity Solution Architecture practitioner method. Public-facing framework site. Links back to parent ecosystem. |
| **Public / private** | Public |
| **Live URL** | TBD |
| **Rename risk** | Low — internal links may need updating |
| **README update required** | Yes — align to brand system and ecosystem navigation |
| **GitHub description suggestion** | Velocity Solution Architecture Framework — practitioner method for decision-first solution design |
| **Move / merge decision** | Retain. Separate practitioner framework with its own URL. |

---

### agentic-cert

| Field | Value |
|-------|-------|
| **Current name** | agentic-cert |
| **Proposed future name** | velocity-academy-agentic *(or retain agentic-cert)* |
| **Category** | CRL — Certification / Learning |
| **Current role** | Markdown — CCA-F and GH-600 study content |
| **Future role** | Velocity Academy certification content for agentic AI practitioner tracks. Feeds into StudioSix training production pipeline. |
| **Public / private** | Public (study content) |
| **Live URL** | TBD |
| **Rename risk** | Low — minimal external references |
| **README update required** | Yes — align to Velocity Academy brand |
| **GitHub description suggestion** | Velocity Academy — agentic AI certification study content (CCA-F, GH-600) |
| **Move / merge decision** | Retain. Certification content is a separate product. |

---

### SAPEACertification

| Field | Value |
|-------|-------|
| **Current name** | SAPEACertification |
| **Proposed future name** | velocity-academy-ea *(or cert-sapea)* |
| **Category** | CRL — Certification / Learning |
| **Current role** | Study and reference content for SAPEA (SAP EA) certification |
| **Future role** | Velocity Academy EA certification study track. May be folded into a unified academy repo or retained as a specialist track. |
| **Public / private** | Public |
| **Live URL** | TBD |
| **Rename risk** | Low |
| **README update required** | Yes |
| **GitHub description suggestion** | Velocity Academy — SAP Enterprise Architecture certification study content |
| **Move / merge decision** | Retain for now. Review whether to consolidate certification repos into a single velocity-academy repo at Phase 4. |

---

### CISSPCertification

| Field | Value |
|-------|-------|
| **Current name** | CISSPCertification |
| **Proposed future name** | velocity-academy-security *(or cert-cissp)* |
| **Category** | CRL — Certification / Learning |
| **Current role** | Study and reference content for CISSP certification |
| **Future role** | Velocity Academy security certification study track. Connects to the Velocity Security Framework (planned). |
| **Public / private** | Public |
| **Live URL** | TBD |
| **Rename risk** | Low |
| **README update required** | Yes |
| **GitHub description suggestion** | Velocity Academy — CISSP certification study content |
| **Move / merge decision** | Retain. Feeds future Velocity Security Framework content. |

---

### AzureSACertification

| Field | Value |
|-------|-------|
| **Current name** | AzureSACertification |
| **Proposed future name** | velocity-academy-azure *(or cert-azure-sa)* |
| **Category** | CRL — Certification / Learning |
| **Current role** | Study and reference content for Azure Solution Architect certification |
| **Future role** | Velocity Academy Azure practitioner track. Links to VAF-SA and tool deployment guidance. |
| **Public / private** | Public |
| **Live URL** | TBD |
| **Rename risk** | Low |
| **README update required** | Yes |
| **GitHub description suggestion** | Velocity Academy — Azure Solution Architect certification study content |
| **Move / merge decision** | Retain. Azure is the primary deployment platform for VAF. |

---

### vsf-match

| Field | Value |
|-------|-------|
| **Current name** | vsf-match |
| **Proposed future name** | vsf-match *(retain or rename to velocity-scorer)* |
| **Category** | TLP — Tool / Product |
| **Current role** | VSF scoring/matching tool |
| **Future role** | Decision-support scoring tool. Feeds into VAF Agentic AI or operates as standalone tool. Candidate for StudioSix productisation. |
| **Public / private** | Private (until productised) |
| **Live URL** | TBD |
| **Rename risk** | Low — currently private |
| **README update required** | Yes |
| **GitHub description suggestion** | Velocity Scoring Framework — decision scoring and option matching tool |
| **Move / merge decision** | Retain separately. Evaluate productisation vs integration into VAF. |

---

### learn-with-claude

| Field | Value |
|-------|-------|
| **Current name** | learn-with-claude |
| **Proposed future name** | zencloud-learning *(or retain learn-with-claude)* |
| **Category** | LAB — Labs / Personal Research |
| **Current role** | Structured learning and reference documentation — personal research |
| **Future role** | Personal learning repository. Not public-facing as a product. Source material for StudioSix content and Velocity Academy. |
| **Public / private** | Private |
| **Live URL** | N/A |
| **Rename risk** | None — private repo |
| **README update required** | Optional |
| **GitHub description suggestion** | Personal learning repository — source material for ZenCloud advisory and Velocity Academy |
| **Move / merge decision** | Retain. Keep private. Do not surface as a product. |

---

### ea-artefact-generator

| Field | Value |
|-------|-------|
| **Current name** | ea-artefact-generator |
| **Proposed future name** | velocity-artefact-engine *(or retain)* |
| **Category** | TLP — Tool / Product |
| **Current role** | EA artefact generation tooling |
| **Future role** | Artefact production layer for Velocity engagements. Candidate for integration into VAF Agentic AI or separate tool product under StudioSix. |
| **Public / private** | Private (until productised) |
| **Live URL** | TBD |
| **Rename risk** | Low — private |
| **README update required** | Yes |
| **GitHub description suggestion** | Velocity Artefact Engine — AI-assisted architecture artefact generation |
| **Move / merge decision** | Retain separately. Evaluate integration with VAF Agentic AI. |

---

### pmi-portal

| Field | Value |
|-------|-------|
| **Current name** | pmi-portal |
| **Proposed future name** | velocity-pmo-portal |
| **Category** | TLP — Tool / Product |
| **Current role** | PMO delivery governance portal |
| **Future role** | PMO / Program Delivery portal within the Velocity ecosystem. Sits in the PMO box of the four-box operating model. Public product candidate. |
| **Public / private** | Public (when productised) |
| **Live URL** | TBD |
| **Rename risk** | Medium — rename clearly separates from PMI (Project Management Institute) brand |
| **README update required** | Yes |
| **GitHub description suggestion** | Velocity PMO Portal — delivery governance workspace for program and architecture teams |
| **Move / merge decision** | Retain. Rename to velocity-pmo-portal to align with ecosystem naming and avoid PMI brand confusion. |

---

### trading-dashboard

| Field | Value |
|-------|-------|
| **Current name** | trading-dashboard |
| **Proposed future name** | studiosix-trading-lab *(or retain)* |
| **Category** | LAB — Labs / Personal Research |
| **Current role** | Personal trading dashboard and research tooling |
| **Future role** | StudioSix Labs boundary — personal research, clearly separated from commercial advisory. Not a Velocity product. May produce public content under StudioSix Labs with appropriate disclaimers. |
| **Public / private** | Private |
| **Live URL** | N/A |
| **Rename risk** | None — private |
| **README update required** | Yes — add clear StudioSix Labs / personal research designation |
| **GitHub description suggestion** | StudioSix Labs — personal trading research dashboard (not financial advice) |
| **Move / merge decision** | Retain separately. Keep clearly separated from ZenCloud advisory and Velocity Framework. Never co-brand with enterprise clients. |

---

### studiosix

| Field | Value |
|-------|-------|
| **Current name** | studiosix |
| **Proposed future name** | studiosix *(or studiosix-hub)* |
| **Category** | SSM — StudioSix Media / Products |
| **Current role** | StudioSix product studio, media, publishing |
| **Future role** | StudioSix hub repo — production pipeline, media assets, publishing templates, book frameworks, podcast scripts, research papers. Public-facing brand. |
| **Public / private** | Public (brand and content pipeline) |
| **Live URL** | TBD |
| **Rename risk** | None |
| **README update required** | Yes — align to StudioSix brand role |
| **GitHub description suggestion** | StudioSix — product studio, media production, and publishing for the Velocity ecosystem |
| **Move / merge decision** | Retain. Separate brand with separate production pipeline. |

---

## Summary Table

| Repo | Category | Future Name | Public | Action |
|------|----------|-------------|--------|--------|
| velocity-architecture | FIP | No change | Yes | README update |
| vaf-sa | FIP | velocity-sa (optional) | Yes | README update |
| agentic-cert | CRL | velocity-academy-agentic | Yes | README update |
| SAPEACertification | CRL | velocity-academy-ea | Yes | README + naming |
| CISSPCertification | CRL | velocity-academy-security | Yes | README + naming |
| AzureSACertification | CRL | velocity-academy-azure | Yes | README + naming |
| vsf-match | TLP | velocity-scorer (optional) | Private | Productisation review |
| learn-with-claude | LAB | zencloud-learning (optional) | Private | Keep private |
| ea-artefact-generator | TLP | velocity-artefact-engine | Private | VAF integration review |
| pmi-portal | TLP | velocity-pmo-portal | Yes (when ready) | Rename + README |
| trading-dashboard | LAB | studiosix-trading-lab | Private | Keep private + label |
| studiosix | SSM | studiosix-hub (optional) | Yes | README update |

---

## Naming Convention Standard

All public Velocity ecosystem repos should follow:

- `velocity-[function]` for framework and practitioner repos
- `velocity-academy-[track]` for certification and learning repos
- `studiosix-[product]` for StudioSix media and product repos
- `zencloud-[type]` for internal ZenCloud tooling and reference repos

Private and lab repos are exempt from naming convention enforcement but should carry a clear designation in the README.

---

## README Standard

Every repo should have a README that includes:

1. One-sentence description of the repo
2. Ecosystem position (which brand / which category)
3. Status (active / planned / archived / personal research)
4. Link to the parent ecosystem (`velocity-architecture`)
5. Public/private rationale

---

*ZenCloud Global Consultants — Brisbane*  
*Portfolio Map Version 1.0 — May 2026*
