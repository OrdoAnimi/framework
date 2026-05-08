# A Comparative Analysis of IT Governance Frameworks
## Investigating the Relationship Between Documented Intent and Reported Outcomes in the Australian Public Sector (2025–2026)

**Author:** Phil Myint
**Organisation:** ZenCloud Global Consultants
**Classification:** Independent Industry Working Paper
**Date:** May 2026
**Repository:** github.com/[your-handle]/velocity-architecture-framework

**Keywords:** Public sector IT governance, institutional decoupling, Australian Government Architecture, QGEA, DTA Investment Oversight Framework, COBIT, TOGAF, NIST Cybersecurity Framework, audit findings, Unify child safety system, runtime verification, attestation gap.

---

## Executive Summary

Australia ranks second globally in the 2025 OECD Digital Government Index. In the same period, six Australian jurisdictions produced audit findings documenting persistent, unresolved IT control failures across access management, asset visibility, and remediation effectiveness.

This is not a contradiction. It is the central diagnostic finding of this paper.

World-class governance design and persistent operational control failure can coexist because they measure different things. The OECD measures policy foundations and institutional capability — the architecture of intent. Audit offices measure whether controls are operating in production environments — the reality of execution. The gap between those two measurements is the governance-execution gap this paper examines.

**Five findings emerge from the evidence.**

**Finding 1 — The pattern is national, not jurisdictional.** Six Australian jurisdictions — federal, Queensland, New South Wales, Victoria, Western Australia, and the Australian Capital Territory — produced audit findings in 2025-2026 showing the same signature: persistent unresolved control deficiencies, asset visibility failures, and post-go-live system failures despite cleared assurance gates. South Australia, Tasmania, and the Northern Territory lack comparable standalone IT audit reporting at this granularity.

**Finding 2 — The dominant failure is verification, not design.** Framework design is sound and internationally validated. The OECD, McKinsey, and COBIT all confirm that governance is the most effective lever for IT delivery outcomes. The audit evidence does not challenge this. It shows that verification mechanisms are consistently positioned above the level where execution happens — producing a structural gap between what is attested and what is confirmed at the point of change.

**Finding 3 — The gap amplifies known operational constraints.** Staff turnover, legacy systems, third-party dependencies, and competing priorities are real and documented contributing factors. They do not independently explain the pattern. When verification is structurally distant from execution, these constraints generate more persistent outcomes than they would if verification were embedded at the delivery layer.

**Finding 4 — The operational consequence is measurable.** The ASD Annual Cyber Threat Report 2024-25 recorded over 84,700 cybercrime reports and over 1,200 significant incidents — an 11% increase year on year. State and local governments remained among the highest-incident sectors. The control gaps documented in audit reports and the incident rates documented in the ASD report are not unrelated. They are the same structural failure expressed in two different measurement systems.

**Finding 5 — A Trans-Pacific addendum extends this analysis to Canada and New Zealand.** That addendum is published separately as Document 1.1 in this series. It confirms the pattern is not specific to Australia's federated governance design.

**Three implications follow directly from these findings.**

First, new policies — including the DTA Whole-of-Government Cloud Computing Policy effective July 2026 — will not close the gap unless they change the structural positioning of verification. Policy addition at the design layer does not automatically embed verification at the execution layer.

Second, the jurisdictions with the clearest audit evidence share a common pattern: verification mechanisms that see documentation rather than live system states. This is a structural condition, not an organisational failing.

Third, further research examining whether new policies produce measurably different audit outcomes in subsequent cycles is the direct empirical next step this evidence base warrants.

---

## 1. Context and Scope

This paper examines the relationship between documented governance intent and reported operational outcomes in Australian public sector IT governance. It draws on official audit reports published between July 2024 and March 2026.

The scope covers the Australian federal government and six state and territory jurisdictions where standalone IT audit evidence is publicly available at sufficient granularity: federal (ANAO), Queensland (QAO), New South Wales (NSW Auditor-General), Victoria (VAGO), Western Australia (WAAGO), and the Australian Capital Territory (ACT Audit Office). South Australia, Tasmania, and the Northern Territory are acknowledged as examined jurisdictions where publicly available IT audit evidence does not meet the granularity threshold required for comparable inclusion.

A Trans-Pacific addendum extending this analysis to Canada and New Zealand is published separately as Document 1.1.

The paper does not assess individual agency performance. It identifies systemic patterns across jurisdictions. All findings are drawn from publicly available official sources. No agency engagement, client relationship, or commercial interest informs any conclusion in this paper.

---

## 2. The Governance Architecture: What the Frameworks Are Designed to Do

### 2.1 Federal Framework

The Digital Transformation Agency (DTA) operates the Whole-of-Government Digital and ICT Investment Oversight Framework (IOF) — a six-stage end-to-end framework covering strategic planning, prioritisation, contestability, assurance, sourcing, and operations. The Australian Government Architecture (AGA) functions as the meta-framework for interoperability across business, data, and technology layers.

In August 2025, the OECD finalised its review of the IOF as part of its Digital Government in Australia study. The review recognised the IOF as a key strength in Australia's investment approach, commending its comprehensive end-to-end lifecycle management and alignment with whole-of-government digital priorities. The OECD Digital Government Index 2025 subsequently ranked Australia second globally among 42 countries, behind Korea.

This finding is not in tension with the audit evidence that follows. It is the essential context for understanding it. The OECD measures governance design maturity. Audit offices measure whether controls are operating in production. These are different instruments measuring different things.

### 2.2 State and Territory Frameworks

Queensland operates the Queensland Government Enterprise Architecture (QGEA), supported by Architecture Review Boards functioning as formal quality gates. The Queensland Government committed $1 billion over four years from 2025 to drive whole-of-government digital investment, with legacy system remediation explicitly included in scope.

New South Wales embeds IT governance within its broader digital service delivery and cyber security strategy, including the NSW Cyber Security Policy administered by Cyber Security NSW. Victoria's governance model emphasises cloud-first principles and service-oriented cyber initiatives. Western Australia operates under the WA Government Cyber Security Policy administered by the Office of Digital Government, with the WAAGO conducting annual General Computer Controls audits. The ACT Audit Office conducts annual financial audits incorporating IT control assessments.

### 2.3 International Benchmarks and the Design-Execution Distinction

Australian governance structures align with established international standards. COBIT's governance and management objectives are reflected in the IOF's investment oversight. The AGA and QGEA reflect aspects of TOGAF's Architecture Development Method. The NIST Cybersecurity Framework is embedded in state-level cyber governance across multiple jurisdictions.

McKinsey's 2022 analysis of 1,355 public sector IT projects identified governance as the most effective lever for reducing cost and schedule overruns. Three governance cornerstones were identified: stakeholder involvement, talent planning, and capability building. McKinsey found that people issues — not technological issues — were the primary cause of transformation failure. This finding is important context for interpreting the Australian audit evidence. It does not contradict the structural positioning argument advanced in this paper. It reinforces that governance effectiveness depends on more than framework design.

Gartner's 2024 analysis predicted that 80% of data and analytics governance initiatives would fail by 2027 due to lack of an embedded forcing mechanism at the operational layer. This finding maps directly to the detection failure pattern documented across Australian jurisdictions.

International comparators are selected on structural grounds. The UK Government Digital Service operates mandatory service assessments as hard verification gates within a unitary governance model. Singapore GovTech integrates strategy and execution under a single authority. Canada — a federation with comparable governance complexity — is examined in the Trans-Pacific addendum. These comparators illuminate the specific structural trade-offs of Australia's federated advisory design. They are not offered as models to replicate.

---

## 3. Methodology

This paper employs qualitative documentary analysis and synthesis of official 2024-2026 artefacts. Purpose is defined as the stated objectives and mechanisms described in framework documents. Outcome refers to the findings and root causes explicitly reported in public audits. A prevention-detection-remediation mapping framework drawn from COBIT and NIST structures the comparative analysis across jurisdictions.

**Jurisdictional comparability limitations.** Audit methodologies differ across jurisdictions. The WAAGO and ACT Audit Office report General Computer Controls findings. The QAO reports IT control deficiencies with significance ratings. The NSW Auditor-General reports high-risk findings and cyber policy compliance data. VAGO conducts targeted technical audits. Direct numerical comparison across jurisdictions is not valid. Findings are interpreted as indicative patterns confirming a consistent structural signature rather than definitive performance rankings.

**Root cause categorisation.** The paper distinguishes between two categories of root cause. Structural constraints — governance positioning, legacy systems, federated design — require repositioning of verification mechanisms to address. Organisational variables — staff turnover, competing priorities, third-party dependencies — require resourcing or process change. The evidence indicates structural constraints as the higher-leverage root cause. Organisational variables compound the structural problem but do not independently produce the pattern observed. That prioritisation is explicit rather than assumed.

**Scope limitations.** The paper does not examine gateway bypass rates, political accountability dynamics, or ministerial oversight mechanisms. These represent distinct failure modes beyond the structural positioning analysis. The paper does not assess individual agency performance or attribute findings to named officials.

**Temporal context.** The evidence captures a period of genuine transition — post-pandemic remediation, Machinery of Government changes, and pre-implementation of the DTA Cloud Computing Policy effective July 2026. Some deficiencies may reflect temporary lag. The persistence of the same pattern across prior audit cycles — acknowledged in every jurisdiction's own reporting — indicates this is not primarily a transitional phenomenon.

---

## 4. Findings by Jurisdiction

### 4.1 Federal — Australian National Audit Office

**Evidence.** ANAO Interim Report on Key Financial Controls of Major Entities (Report No. 39, 2024-25, May 2025) documented 118 findings across 27 entities at the interim audit phase. Seventy-eight per cent of these interim findings were not new — carried forward unresolved from prior cycles. Sixty-five per cent of all interim findings related to the IT control environment. ANAO Auditor-General Report No. 17 2025-26 (March 2026) documented 178 audit findings for the 2024-25 financial year, down from 214 in 2023-24. IT control weaknesses remained the single largest finding category. The ANAO's December 2025 Audit Matters publication stated: "IT controls remain the most significant area of risk across the sector — at a time when cyber threats are increasing, reliance on IT systems for service delivery is growing, and IT environments are becoming more complex."

**Failure stage.** Primarily detection and remediation failure. The frameworks identify the requirement. They do not surface the gap or ensure closure.

**So what.** At the Commonwealth level, the dominant pattern is not new deficiencies emerging — it is existing deficiencies persisting. When 78% of interim findings are repeats, the verification mechanism is not positioned to confirm that remediation has actually occurred. Gate clearance and documented closure are not the same as operational effectiveness.

---

### 4.2 Queensland — Queensland Audit Office and Deloitte Unify Review

**Evidence.** QAO Report 6 2025-26 (December 2025) identified 13 significant and 198 total IT control deficiencies. Forty-three per cent of prior-year deficiencies remained unresolved. Root causes cited include competing priorities, staff turnover, organisational restructures, third-party governance challenges, and insufficient verification of control effectiveness. The QAO noted explicitly that entities are "not fully tackling root causes due to competing priorities and are not checking that implemented controls are effective."

The Deloitte Unify Review (December 2025, public summary February 2026) examined the $183 million child safety case management system that went live in April 2025 serving approximately 16,000 children's records. Key findings included gaps in system design, functionality, and performance; difficulties for frontline staff in accessing critical information; a staff approval rating of 1.79 out of 10; and challenges in information exchange with partner agencies. A remediation team of approximately 120 staff was mobilised. Queensland Parliament Hansard (11 December 2025) confirms the staff approval rating directly.

Architecture Review Boards functioned. Investment oversight gates were cleared. What the governance architecture could not confirm — because it was not positioned to confirm it — was whether the system would function for the people using it in the field.

**Failure stage.** Prevention failure at the assurance gate (Unify). Detection failure in operational readiness assessment (Unify). Remediation failure across the deficiency portfolio (43% unresolved rate).

**So what.** The Unify case is not an outlier within Queensland's governance environment. It is the highest-visibility expression of a pattern that the QAO simultaneously documented across 198 deficiencies. The assurance gate did not fail because it was poorly designed. It failed because it was not positioned to see what it needed to see.

---

### 4.3 New South Wales — Auditor-General and Cyber Security Insights

**Evidence.** NSW Auditor-General Internal Controls and Governance 2025 (October 2025) reported five high-risk IT findings across 26 major agencies collectively accounting for 95% of NSW Government total budgeted expenditure. Approximately half of all findings involved IT controls over financial systems. Gaps in formal cyber security risk management covering supply chain risks were identified. Third-party incident rates reported by Cyber Security NSW almost tripled in the reporting year.

NSW Cyber Security Insights 2025 (July 2025) provides additional granularity. Sixty-nine per cent of Protect mandatory requirements in the NSW Cyber Security Policy were not fully met by reporting agencies. One hundred and fifty-two significant, high, and extreme residual cyber security risks were reported by 27 agencies in FY2024. Fifty-nine per cent of reporting agencies had no independent assurance over their own assessment of NSW Cyber Security Policy requirements.

**Failure stage.** Prevention failure at the policy design layer (supply chain governance gaps). Detection failure in cyber risk visibility (59% of agencies without independent assurance over their own compliance assessment). Remediation failure in unresolved high-risk findings.

**So what.** The NSW evidence introduces a dimension not visible in other jurisdictions: agencies attesting compliance with a policy they have not independently verified. When 59% of agencies have no independent assurance over their own cyber policy compliance, the attestation mechanism is the problem — not the policy. Attestation without verification is not governance. It is paperwork.

---

### 4.4 Victoria — Victorian Auditor-General's Office

**Evidence.** VAGO Cybersecurity of IT Servers (29 October 2025) examined 10 government departments and Cenitex. No examined agency maintained a complete and accurate server inventory. Six agencies had automated asset discovery tools. None had configured them to scan their entire network. All agencies submitted incomplete server inventory information, missing critical details such as operating system versions, host names, or server locations. Twenty-five per cent of server entries reported by agencies had operating systems that are unsupported. A further 11 per cent had unknown operating systems.

**Failure stage.** Detection failure. The foundational visibility required to identify risk was absent. Without a complete inventory, every downstream risk assessment, every patching cycle, every cloud migration decision operates on assumption.

**So what.** Asset inventory is not a complex governance requirement. It is the prerequisite for every other security control. When six agencies have the tools and none have configured them fully, the issue is not intent or knowledge — it is that full configuration was harder than partial configuration. The compliant state was not the default state.

---

### 4.5 Western Australia — Office of the Auditor General

**Evidence.** WAAGO State Government 2025 Information Systems Audit Results (December 2025) examined 53 state government entities. Three hundred and fifty-nine General Computer Control findings were reported. Sixty-five per cent were unresolved from prior years — the highest unresolved rate in the Australian evidence base. Over 80% of findings were in information and cyber security control categories. Access management and endpoint security had the worst performance — fewer than 25% of entities met the benchmark in either category. The Auditor General stated: "It is disappointing that almost two thirds of these findings are unresolved from previous years."

**Failure stage.** Detection and remediation failure. Sixty-five per cent unresolved rate is the highest documented in the Australian evidence base for this period.

**So what.** Western Australia's 65% unresolved rate exceeds Queensland's 43% despite both jurisdictions having active audit functions and documented governance frameworks. The difference in unresolved rates does not indicate a difference in governance design quality. It indicates a difference in how effectively verification is embedded at the operational layer where remediation actually happens.

---

### 4.6 Australian Capital Territory — ACT Audit Office

**Evidence.** ACT Audit Office Financial Audit Results 2024-25 (December 2025) identified 40 IT control weaknesses across ACT Government agencies. Twenty-six of the 40 — 65% — were raised in previous years. Twenty-seven of the 40 findings, representing 68%, related to information security controls.

**Failure stage.** Detection and remediation failure. Sixty-five per cent repeat finding rate matches Western Australia's despite the ACT's smaller scale and more centralised governance structure.

**So what.** The ACT finding is analytically significant because the ACT has one of the most centralised public sector governance structures in Australia. Yet it produces the same repeat-finding signature as more federated jurisdictions. Centralisation of governance design does not automatically close the verification-execution gap.

---

## 5. Cross-Jurisdictional Pattern Analysis

### 5.1 The Pattern

Six jurisdictions. Different frameworks. Different scales. Different governance models. One audit signature.

**Prevention failures** occur when frameworks do not stop the gap from forming. The NSW supply chain risk management gap and the Unify assurance gate failure are prevention failures. The governance instrument was present. It was not positioned to prevent the outcome.

**Detection failures** occur when frameworks do not surface the gap once it exists. Victoria's server inventory finding is a pure detection failure. The NSW finding that 59% of agencies have no independent assurance over their own compliance is a detection failure at the attestation layer.

**Remediation failures** occur when frameworks do not close the gap once detected. Queensland's 43% unresolved rate, WA's 65%, the ACT's 65%, and the ANAO's 78% repeat interim findings all represent remediation failure. Detection occurred. Closure did not.

These three categories are mutually exclusive and collectively exhaustive. A gap either was not prevented, was not detected, or was not remediated. Addressing only one stage without the others will not resolve the pattern.

**Mapping Matrix: Prevention-Detection-Remediation Framework (2025-2026 Evidence)**

| Failure Stage | Stated Purpose (Design) | Reported Outcome (Execution) | Jurisdiction Evidence | Observed Gap |
|---|---|---|---|---|
| Prevention | Rigorous assurance gates (IOF/ARBs) | Unify: critical functionality gaps post-review | QLD | Gate not positioned for operational fitness |
| Prevention | Supply chain risk management (NSW Cyber Security Policy) | Third-party incidents tripled; supply chain gaps identified | NSW | Policy present; enforcement absent |
| Detection | Integrated asset inventories (AGA/QGEA) | No agency maintained complete server inventory | VIC | Foundational visibility absent |
| Detection | Independent assurance over compliance | 59% of agencies had no independent assurance over own compliance | NSW | Attestation substituted for verification |
| Remediation | Continual improvement tracking (COBIT) | 65-78% unresolved deficiencies across jurisdictions | All jurisdictions | Verification not embedded at execution layer |

### 5.2 The OECD Paradox Resolved

Australia ranks second globally in the 2025 OECD Digital Government Index. Australia simultaneously has 198 IT control deficiencies in Queensland alone, with 65% unresolved in WA and the ACT.

This appears contradictory. It is not.

The OECD Digital Government Index measures policy foundations and institutional capability — the architecture of intent. It does not measure whether access controls are operating in production, whether server inventories are complete, or whether audit findings from prior years have been closed.

Audit offices measure operational control effectiveness — whether the control is actually functioning at the point where a user provisions a resource, accesses a system, or deploys a change.

These are different measurement instruments with different objects. A country can simultaneously have world-class governance design and persistent operational control failure. The gap between those two measurements is precisely what this paper examines. The OECD ranking validates the design. The audit evidence documents the execution gap. Both are correct.

### 5.3 The Causal Mechanism

The causal mechanisms underlying the gap are not equal in leverage.

Structural constraints — governance positioning, legacy systems, federated design — increase control complexity and limit what can be automated or enforced at the execution layer. These are the primary lever.

Organisational variables — staff turnover, competing priorities, third-party dependencies — compound the structural problem. McKinsey's research confirms that people issues are the dominant cause of public sector transformation failure. This paper does not dispute that finding. It argues that structural positioning determines how much damage organisational variables cause. In an environment where verification is embedded close to execution, staff turnover produces less persistent audit findings than in an environment where verification sits at the committee level above delivery.

### 5.4 The Operational Consequence

The ASD Annual Cyber Threat Report 2024-25 (October 2025) recorded over 84,700 cybercrime reports — one every six minutes. Over 1,200 significant cyber security incidents were responded to — an 11% increase on the prior year. Attacks on critical infrastructure rose 111%. State and local governments remained among the highest incident-reporting sectors.

The control gaps documented in audit reports and the incident rates documented in the ASD report are not separate phenomena. They are the same structural failure expressed in two different measurement systems.

---

## 6. Policy Implications

The DTA Whole-of-Government Cloud Computing Policy effective July 2026 represents a meaningful step toward addressing legacy risk and strengthening accountability. The OECD review commended the direction.

If the mechanism connecting policy intent to operational reality remains structurally weak — if verification sits above the level where execution happens — the 2026 Cloud Policy will layer onto an operating model that cannot confirm what it claims to govern. New policy at the design layer does not automatically reposition verification at the execution layer.

The third-party governance problem documented across NSW and Queensland is a specific expression of this. When control verification is outsourced without embedding the verification mechanism within the provider relationship at the right level, the governance framework retains the language of oversight without the structural position to exercise it.

Future research should examine Canada as a structurally precise peer comparator — a federation navigating comparable governance complexity — and extend this analysis to New Zealand for a Trans-Tasman perspective. Both are addressed in the companion Trans-Pacific addendum published as Document 1.1.

---

## 7. Conclusion

Australia's IT governance frameworks are world-class in design. The OECD has confirmed this. The evidence in this paper does not challenge it.

What the 2025-2026 audit cycle documents — across six jurisdictions, in multiple failure categories, with external validation from McKinsey, Gartner, and the ASD — is that world-class design and persistent operational control failure can coexist when verification mechanisms are consistently positioned above the level where execution happens.

Three observations summarise the evidence.

First, the pattern is national and structural. The same audit signature appears across federal, Queensland, New South Wales, Victoria, Western Australia, and the ACT despite structurally different governance frameworks. The mechanism producing the gap is not inside the frameworks. It is in the space between the frameworks and the production environments they govern.

Second, the operational consequence is measurable and growing. The ASD documented over 1,200 significant cyber incidents in FY2024-25, an 11% increase year on year. The audit findings and the ASD incident data are the same structural failure in two measurement registers.

Third, new policy will not close the gap unless it changes the structural positioning of verification. The 2026 Cloud Computing Policy creates the mandate. What determines whether it produces different audit findings in 2027 is whether verification gets embedded closer to execution — or whether the policy sits at one level while the control environment operates at another.

Further research examining the structural conditions that sustain this gap — and what operational and architectural responses are most effective in closing it — is the direct next step this evidence base warrants. Future research should examine whether Australia's 2026 Cloud Computing Policy produces measurably different IT control findings in the 2027-2028 audit cycle, and whether the Trans-Pacific patterns documented in the companion addendum hold across subsequent audit cycles in Canada and New Zealand.

---

## References

- Queensland Audit Office. (2025). *Information systems 2025* (Report 6: 2025–26). https://www.qao.qld.gov.au/reports-resources/reports-parliament/information-systems-2025
- Deloitte Touche Tohmatsu. (2026). *Unify Review Report.* https://www.families.qld.gov.au/unify
- Queensland Parliament. (2025). *Hansard, 11 December 2025.* https://app.advoc8.co/public/feeds_v2/hansard_fragments/7mT4O95?contribution_id=545901
- Digital Transformation Agency. (2025). *Whole-of-Government Cloud Computing Policy.* https://www.digital.gov.au/cloud-policy
- Digital Transformation Agency. (2026). *Australia rises to second globally in the OECD Digital Government Index.* https://www.dta.gov.au/articles/australia-rises-second-globally-oecd-digital-government-index
- Australian National Audit Office. (2025). *Interim Report on Key Financial Controls of Major Entities* (Report No. 39, 2024–25). https://www.anao.gov.au/work/financial-statement-audit/interim-report-key-financial-controls-of-major-entities-2024-25
- Australian National Audit Office. (2025). *ANAO Annual Report 2024–25.* https://www.anao.gov.au/work/annual-report/anao-annual-report-2024-25
- Australian National Audit Office. (2026). *Auditor-General Report No. 17 2025–26.* https://www.anao.gov.au/sites/default/files/2026-03/Auditor-General_Report_2025-26_17c.pdf
- Australian National Audit Office. (2025). *Audit Matters 5 — December 2025.* https://www.anao.gov.au/work/audit-matters/audit-matters-5-december-2025
- NSW Auditor-General. (2025). *Internal controls and governance 2025: Procurement and Technology.* https://www.audit.nsw.gov.au/our-work/reports/internal-controls-and-governance-2025-procurement-and-technology
- NSW Auditor-General. (2025). *Cyber Security Insights 2025.* https://www.audit.nsw.gov.au/our-work/reports/cyber-security-insights-2025
- Victorian Auditor-General's Office. (2025). *Cybersecurity of IT Servers.* https://www.audit.vic.gov.au/report/cybersecurity-it-servers
- Office of the Auditor General Western Australia. (2025). *State Government 2025 — Information Systems Audit Results* (Report 7: 2025–26). https://audit.wa.gov.au/reports-and-publications/reports/state-government-2025-information-systems-audit-results/
- ACT Audit Office. (2025). *Financial Audit Results 2024–25.* https://www.audit.act.gov.au/reports-and-publications/audit-reports
- Australian Signals Directorate. (2025). *Annual Cyber Threat Report 2024–25.* https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2024-2025
- OECD. (2025). *Digital Government in Australia: Enhancing Digital Investment.* https://www.oecd.org/en/publications/digital-government-in-australia_91c22326-en.html
- McKinsey & Company. (2022). *Unlocking the potential of public-sector IT projects.* https://www.mckinsey.com/industries/public-sector/our-insights/unlocking-the-potential-of-public-sector-it-projects
- Gartner. (2024). *Gartner predicts 80% of data and analytics governance initiatives will fail by 2027.* https://www.gartner.com/en/newsroom/press-releases/2024-02-28-gartner-predicts-80-percent-of-data-and-analytics-governance-initiatives-will-fail-by-2027-due-to-a-lack-of-a-real-or-manufactured-crisis
- ISACA. (2019). *COBIT 2019 Framework.*
- The Open Group. *TOGAF Standard.*
- NIST. *Cybersecurity Framework.*

---

## Appendix A: Deficiency Summary by Jurisdiction (2025-2026)

| Jurisdiction | Source | Key Finding | Unresolved Rate | Primary Category |
|---|---|---|---|---|
| Federal (ANAO) | Report No. 39 2024-25; Report No. 17 2025-26 | 178 findings in 2024-25 (214 in 2023-24); 65% of interim findings IT controls | 78% of interim findings repeats | IT security, access management, change management |
| Queensland (QAO) | Report 6: 2025-26 | 198 total IT control deficiencies; 13 significant | 43% | System access, privileged accounts, authentication |
| New South Wales | Internal Controls 2025; Cyber Security Insights 2025 | 5 high-risk IT findings; 69% of Protect requirements not met | Not separately quantified | IT controls over financial systems; supply chain |
| Victoria (VAGO) | Cybersecurity of IT Servers 2025 | No agency maintained complete server inventory; 25% unsupported OS | Not applicable — foundational visibility absent | Asset identification; server security |
| Western Australia (WAAGO) | State Government 2025 Information Systems | 359 GCC findings to 53 entities | 65% | Access management; endpoint security |
| ACT | Financial Audit Results 2024-25 | 40 IT control weaknesses | 65% | Information security controls (68% of findings) |

---

## Appendix B: Unify Project Timeline with Failure Stage Classification

| Date | Event | Failure Stage |
|---|---|---|
| Pre-2025 | Planning and funding for $183M redevelopment | — |
| April 2025 | System go-live for ~16,000 children's records | Prevention failure confirmed at go-live |
| October 2025 | Deloitte review commissioned | Detection initiated |
| December 2025 | Review completed — 1.79/10 staff approval rating | Detection confirmed |
| February 2026 | Public summary released; 120-person remediation team mobilised | Remediation commenced |

---

## Appendix C: Prevention-Detection-Remediation Matrix (Expanded)

| Failure Stage | Stated Purpose | Reported Outcome | Jurisdiction | Observed Gap | Primary Root Cause |
|---|---|---|---|---|---|
| Prevention | Rigorous assurance gates (IOF/ARBs) | Unify: functionality gaps post-review | QLD | Gate not positioned for operational fitness | Structural positioning |
| Prevention | Supply chain risk governance | Third-party incidents tripled | NSW | Policy present; enforcement absent | Structural positioning |
| Detection | Integrated asset inventories | Agencies flying blind on server counts | VIC | Foundational visibility absent | Structural positioning |
| Detection | Independent compliance assurance | 59% of agencies with no independent assurance | NSW | Attestation substituted for verification | Structural positioning |
| Remediation | Continual improvement tracking | 65-78% unresolved deficiencies across jurisdictions | All | Verification not embedded at execution layer | Structural positioning + organisational variables |

---

## Appendix D: External Validation Summary

| Source | Finding | Relevance to This Paper |
|---|---|---|
| OECD Digital Government Index 2025 | Australia ranked 2nd globally; IOF commended as key strength | Validates design maturity; consistent with paper's finding that gap is not in design |
| OECD Digital Government in Australia (2025) | IOF provides comprehensive end-to-end lifecycle management | Confirms framework soundness; paper identifies execution gap not design gap |
| McKinsey — Unlocking Public Sector IT (2022) | Governance is most effective lever; people issues primary failure cause | Consistent with structural positioning argument; confirms operational variables compound structural gaps |
| Gartner — D&A Governance Prediction (2024) | 80% of governance initiatives will fail without embedded operational forcing mechanism | Maps directly to detection failure category across all jurisdictions |
| ASD Annual Cyber Threat Report 2024-25 | 84,700 cybercrime reports; 1,200+ significant incidents; 11% increase | Operational consequence of control gaps documented in audit reports |

---

*This analysis is published by Phil Myint under the ZenCloud Global Consultants brand as an independent contribution to public sector IT governance research. No commercial engagement is implied or intended. Full source citations from the 2024-2026 ANAO, QAO, NSW Auditor-General, VAGO, WAAGO, ACT Audit Office, ASD, OECD, and Deloitte Unify Review reports.*

*A Trans-Pacific addendum extending this analysis to Canada and New Zealand is published separately as Document 1.1 in this series.*

*This working paper is maintained in the ZenCloud research repository at github.com/[your-handle]/velocity-architecture-framework*
