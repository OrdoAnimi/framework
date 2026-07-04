# International Comparative Addendum: Canada and New Zealand
## Extending the Prevention-Detection-Remediation Framework Beyond Australia

**Document:** 1.1 — Addendum to the OrdoAnimi IT Governance Working Paper (May 2026)
**Author:** Phil Myint
**Organisation:** OrdoAnimi
**Classification:** Independent Industry Working Paper — Addendum
**Date:** May 2026
**Primary Paper:** A Comparative Analysis of IT Governance Frameworks — Australian Public Sector (2025-2026)
**Repository:** github.com/[your-handle]/velocity-architecture-framework

---

## Executive Summary

The main working paper established that six Australian jurisdictions with structurally different governance frameworks produce the same audit signature — persistent unresolved control deficiencies, asset visibility failures, and post-go-live system failures despite cleared assurance gates. It proposed that the mechanism producing this pattern is not inside the frameworks but in the space between the frameworks and the production environments they govern.

This addendum tests that proposition against two peer jurisdictions selected on structural grounds: Canada, a federation with comparable governance complexity to Australia, and New Zealand, a unitary all-of-government model with more centralised accountability than any Australian jurisdiction.

**Three findings emerge.**

**Finding 1 — Canada produces an almost identical audit signature to Australia.** The 2025 Auditor General of Canada report on Cyber Security of Government Networks and Systems and the 2023 report on Modernising Information Technology Systems document the same pattern: comprehensive strategy and framework design acknowledged as sound; persistent operational gaps in asset visibility, monitoring coverage, and remediation effectiveness. Canada's federal asset inventory project — begun in 2017, still incomplete in 2025, now expected no earlier than 2027 — is the most direct international parallel to Victoria's server inventory finding.

**Finding 2 — New Zealand produces a related but distinct governance-execution gap.** The NZ Office of the Auditor-General's April 2025 report Mind the Gap: Governing Cyber Security Risks found that most examined public organisations had higher levels of residual cyber security risk than their stated risk appetite. New Zealand's centralised model produces a gap located in the translation from risk appetite to operational mandate, rather than the attestation substitution seen in Australia. Both, however, reflect structural distance between governance intent and the execution layer.

**Finding 3 — The pattern is not explained by governance model design.** It persists across federated models (Australia, Canada), centralised models (New Zealand), and hybrid models (ACT within Australia). The mechanism producing the gap is structural and consistent. What varies across jurisdictions is how the gap is expressed — not whether it exists.

**Note on evidential asymmetry.** The Canada evidence base for this addendum is substantially stronger than the New Zealand evidence base. Canada has two major OAG reports with specific statistics and quantified findings. The NZ Mind the Gap report deliberately does not identify the organisations examined and provides no deficiency counts comparable to WAAGO or QAO reporting. Analytical conclusions about New Zealand are pattern-level observations rather than quantitative comparisons and should be read accordingly.

---

## 1. Canada: A Federation in the Same Position

### 1.1 Governance Architecture

Canada's federal IT governance operates through three primary bodies. The Treasury Board of Canada Secretariat (TBS) provides oversight policy, sets standards, and monitors the health of government IT applications. Shared Services Canada delivers central IT infrastructure and cyber security services to 45 partner departments and agencies. Communications Security Establishment Canada (CSE) provides advanced cyber defence services.

This is a federated advisory model structurally comparable to Australia's DTA and AGA architecture — central coordination with distributed implementation. TBS plays the role of the DTA. Shared Services Canada plays the role of the AGA's technology layer. The 45 partner departments and agencies correspond to the portfolio of Commonwealth entities subject to the IOF. Both countries operate frameworks that set standards and provide services centrally while implementation remains distributed.

### 1.2 The 2025 Cyber Security Audit — A Direct Parallel

The Auditor General of Canada tabled the report Cyber Security of Government Networks and Systems in October 2025 — the same audit period as the Australian evidence base.

The framework was found to be sound. Canada had developed a comprehensive enterprise cyber security strategy. The tools existed. Central cyber defence services were available. The Auditor General acknowledged the strategy as appropriate.

The operational findings tell a different story.

**Asset inventory — the direct Victorian parallel.** Shared Services Canada and CSE did not have a comprehensive up-to-date inventory of all government IT devices — laptops, smartphones, and servers. Shared Services Canada began work to address this gap in 2017. As of the audit completion in late 2025, the project remained incomplete. Completion is now expected no earlier than 2027 — a decade after the work began. The Auditor General stated directly: "Without up-to-date IT information across all departments and agencies, the federal government risks not being aware of — let alone being able to quickly respond to — changing cybersecurity challenges."

This is the Victorian flying blind finding applied to a federation with a different governance model, a different constitutional structure, and a different geographic and political context. The structural condition is identical. The tools existed. The mandate existed. The structural conditions that translate mandate into operational truth did not.

**Governance coverage gap — a distinct failure mode.** The OAG found that 58% of federal organisations are not required to use CSE's cyber security defence services. Of those eligible, many did not engage. The Auditor General found that inconsistent deployment of cyber defence sensors across federal organisations created security gaps affecting the government's ability to defend networks, systems, and devices.

This represents a specific mechanism of prevention failure — where the governance instrument is available but structurally cannot be applied universally, leaving the majority of the environment outside the protective layer. It is distinct from the attestation substitution seen in Australia and the risk appetite translation failure seen in New Zealand. It speaks to the authority architecture of governance: when adoption is voluntary rather than mandatory, comprehensive visibility is structurally impossible regardless of framework sophistication.

**Incident response failure.** A significant cyber attack in January 2024 saw delayed response due to lack of information sharing between TBS, CSE, and Shared Services Canada. The attacker had prolonged access to personal information. An initiative to set up a cyber security collaboration platform and incident case management tool had not received funding at the time of the audit.

**So what.** Canada's federal governance framework is structurally sound by its own assessment and its Auditor General's acknowledgment. The operational gap is not in strategy or intent. It is in the distance between the central governance layer and the execution environments it attempts to govern — and in the voluntary nature of key protective services that makes comprehensive visibility structurally impossible. This is the same structural condition documented across Australia, expressed through Canada's specific governance architecture.

### 1.3 The 2023 IT Modernisation Audit — Legacy as Structural Constraint

The 2023 Auditor General report on Modernising Information Technology Systems provides the legacy context that explains why the 2025 cyber security gaps persist.

Two thirds of approximately 7,500 federal software applications were in poor health as of the audit. Five hundred and sixty-two of 1,480 mission-critical applications — those supporting critical services to Canadians — were in poor health. The percentage of healthy applications grew from 33% in 2019 to only 38% in 2023. Against a target of 60% healthy by 2030, the Auditor General estimated that at the current pace only 45% would be healthy by that date.

The Benefits Delivery Modernisation Programme — responsible for Employment Insurance, Old Age Security, and Canada Pension Plan — was at the audit's midpoint still running entirely on systems between 20 and 60 years old. Cost had been revised from $1.75 billion in 2017 to $2.5 billion in 2022 — a 43% increase — with no benefits yet migrated to the new platform.

The Auditor General noted that the government first identified aging IT systems as a significant issue in 1999. Twenty-four years later, TBS still had no strategy to drive modernisation. TBS monitored only 22 high-risk IT projects out of approximately 2,100 active projects.

The Canadian legacy evidence also illustrates a compounding dynamic: while the asset inventory project remains incomplete, the inventory itself is a moving target as modernisation efforts simultaneously retire and introduce systems. This creates a decade-long timeline not simply because of inaction but because the gap is structurally dynamic — the target changes faster than the visibility mechanism can track it.

It is worth noting that Australia's 2026 Cloud Computing Policy and Queensland's 2025 $1 billion digital investment commitment represent more recent structural responses than the Canadian evidence documents for the equivalent period. Whether those responses produce different outcomes is precisely what future Australian audit cycles will determine. The Canadian evidence gives the clearest available indication of what happens when structural change does not accompany policy addition over an extended period.

**So what.** Canada's legacy debt is the structural constraint that makes the cyber security gaps persistent rather than transitional. The oversight body cannot adequately govern what it cannot see. The pattern is the same as Australia's but the legacy dimension is more extensively documented and quantified — providing a timeline of what sustained failure to address legacy technical debt looks like when left unresolved across multiple governance cycles.

---

## 2. New Zealand: Centralisation Does Not Close the Gap

### 2.1 Governance Architecture

New Zealand's digital governance operates through a more centralised architecture than Australia's. The Government Chief Digital Officer at the Department of Internal Affairs sets digital policy and standards. The Government Chief Information Security Officer sets information security standards through the New Zealand Information Security Manual. The National Cyber Security Centre (NCSC) — part of the Government Communications Security Bureau — provides cyber security services to nationally significant organisations. The System Assurance team at DIA provides independent assurance oversight over high-risk digital investments.

This is a unitary all-of-government model. There is no federal-state split. Accountability lines are more consolidated. The governance instruments are more centralised than any Australian state jurisdiction — including the ACT, which the main working paper identified as Australia's most centralised governance model.

### 2.2 Mind the Gap: The April 2025 Audit Finding

The Office of the Auditor-General published Mind the Gap: Governing Cyber Security Risks in April 2025 — examining selected public organisations across the NZ public sector. To protect the integrity of their cyber security practices, the OAG did not identify the specific organisations examined. This limits direct numerical comparison to Australia's evidence base. Analytical conclusions about New Zealand in this section are pattern-level observations rather than quantitative comparisons.

The central finding: most of the public organisations examined had higher levels of residual cyber security risk than their stated risk appetite. Governors were taking cyber security seriously. They were engaged. They understood the risk landscape. The gap between the risk they were comfortable with and the risk they actually faced persisted regardless.

The Auditor General identified three conditions sustaining the gap. Governors were not always able to set a clear understood risk appetite. The cost of achieving the desired risk level was not always fully understood, making prioritisation difficult. Rapid technological change meant that simply maintaining existing controls — without active investment — could lead to higher residual risk over time.

The report noted that the NZ National Cyber Security Centre was preparing baseline cyber security standards for public service organisations — a signal that minimum operational standards at the execution layer had not yet been established at the time of publication.

**So what.** New Zealand's centralised model produces a related but distinct governance-execution gap — one located in the translation from risk appetite to operational mandate — rather than the attestation substitution seen in Australia. In Australia, the dominant pattern is agencies declaring compliance they have not independently verified. In New Zealand, the dominant pattern is governors who cannot translate their risk appetite into verifiable operational requirements, and who are uncertain whether the gap can be closed or what it would cost to do so. Both reflect structural distance between governance intent and the execution layer. The remedy for each is different.

### 2.3 The ACT Parallel

The ACT finding from the main working paper is analytically critical here. The ACT has the most centralised governance structure in Australia. It produced a 65% unresolved deficiency rate — matching Western Australia's and significantly higher than Queensland's. Centralisation of governance design did not produce materially different operational outcomes.

New Zealand's audit result confirms this pattern at the national level. A unitary governance model with consolidated accountability — more centralised than any Australian jurisdiction — produces its own version of the execution gap. If centralisation changes the expression of the gap rather than eliminating it, the ACT may represent an intermediate case: accountability is less fragmented than the federated states, yet the translation layer between governance intent and operational control remains incomplete.

The gap is not a function of federation. It is a function of structural distance between governance intent and execution reality. That distance exists in federated models and centralised models. What varies is how it is expressed and what conditions sustain it.

---

## 3. The Trans-Pacific Pattern

### 3.1 Three Models, One Structural Condition

Three governance models. Three distinct constitutional structures. One structural condition.

Australia — federated advisory model across six jurisdictions — produces prevention failures at assurance gates, detection failures in asset visibility and compliance assurance, and remediation failures across all jurisdictions with unresolved rates between 43% and 78%.

Canada — federated model with central infrastructure delivery — produces the same asset visibility failure documented in Victoria, a governance coverage gap in protective service adoption not seen in Australia, and a legacy modernisation gap documented over 24 years without resolution.

New Zealand — unitary centralised model — produces a risk appetite translation gap where most organisations carry higher residual risk than their stated appetite and governors cannot confirm whether the gap can be closed or at what cost.

**Trans-Pacific Mapping Matrix**

| Jurisdiction | Governance Model | Primary Failure Stage | Key Finding | Structural Condition |
|---|---|---|---|---|
| Australia — Federal | Federated advisory | Detection and remediation | 178 findings in 2024-25; 78% interim findings repeats | Verification above execution layer |
| Australia — Queensland | Federated state | Prevention, detection, remediation | 198 deficiencies; 43% unresolved; Unify 1.79/10 | Assurance gate not positioned for operational fitness |
| Australia — Victoria | Federated state | Detection | No agency maintained complete server inventory | Foundational visibility absent |
| Australia — WA | Federated state | Remediation | 359 findings; 65% unresolved | Verification not embedded at execution |
| Australia — ACT | Centralised territory | Remediation | 40 findings; 65% unresolved | Same pattern despite centralisation |
| Canada — Federal | Federated central infrastructure | Detection and legacy | Asset inventory begun 2017 still incomplete 2025; 58% of organisations outside central security services | Protective layer fragmented; visibility structurally incomplete |
| New Zealand | Unitary centralised | Risk appetite translation | Most organisations carry higher residual risk than appetite; governors uncertain whether gap can close | Translation layer between risk intent and operational mandate absent |

### 3.2 What the Pattern Reveals

The main working paper proposed that the mechanism producing the governance-execution gap is structural and consistent — not a function of framework quality, governance model design, or organisational capability in isolation. The Trans-Pacific evidence confirms this.

The pattern persists across federated governance (Australia, Canada) and unitary governance (New Zealand). It persists across internationally acknowledged framework designs. It persists across different constitutional structures.

What the pattern does not persist across is the specific expression of the gap. Canada's governance coverage gap — where central protective services exist but adoption is voluntary and fragmented — is distinct from Australia's attestation substitution failure and New Zealand's risk appetite translation failure. These are not the same failure mode. They are different expressions of the same structural condition: when verification is not embedded at the level where execution happens, the gap between governance intent and operational reality accumulates in whatever form the specific governance architecture makes most likely.

### 3.3 The Legacy Timeline

Canada's 2023 modernisation audit adds a dimension not fully quantified in the Australian evidence. The 24-year documentation of the same legacy problem, the 43% cost overrun in the Benefits Delivery Modernisation Programme, and the finding that only 38% of applications are healthy against a 60% target — these numbers give the legacy constraint a scale and timeline that the Australian evidence implies but does not fully document.

The Australian evidence base notes legacy systems as a structural constraint. The Canadian evidence quantifies what that constraint looks like when it is not resolved over two decades. It is the most explicit documentation in the Trans-Pacific evidence base of what sustained failure to address legacy technical debt looks like at national scale across multiple governance cycles.

---

## 4. Implications for the Australian Evidence

The Trans-Pacific comparison produces three analytical refinements to the main working paper's conclusions.

**First — the pattern is not specific to Australia's federated design.** The main working paper was careful to avoid overclaiming that Australia's federated advisory model was the primary cause of the gap. The Canada and New Zealand evidence confirms this caution was warranted. The gap appears in federated models, centralised models, and unitary models. Federation is not the explanation.

**Second — governance coverage gaps represent a distinct prevention failure mechanism.** Canada's finding that 58% of federal organisations are not required to use central cyber security services — and many of those eligible did not engage — identifies a failure mode not visible in the Australian evidence. Future Australian audit cycles should examine whether equivalent non-engagement patterns exist in the take-up of central DTA services and ASD cyber security programs. If central services are available but adoption is voluntary, the governance coverage question is directly relevant to the Australian context.

**Third — the legacy timeline matters.** Canada's 24-year documented legacy problem gives a timeline to what the Australian evidence describes as legacy constraint. The Australian 2026 Cloud Computing Policy and Queensland's 2025 digital investment commitment represent more recent structural responses. Whether those responses produce different outcomes is the empirical question future audit cycles will answer. The Canadian evidence provides a reference point for what persistence of the structural condition looks like over extended periods.

---

## 5. New Zealand: A Genuine Trans-Tasman Research Agenda

The main working paper flagged New Zealand as a subject for future comparative research. The Mind the Gap report confirms that the research question is now empirically grounded rather than speculative.

The specific questions that Trans-Tasman comparative research should examine:

Does New Zealand's more centralised accountability architecture produce measurably lower unresolved deficiency rates than Australian jurisdictions when compared at equivalent scale? The NZ report does not provide comparable deficiency counts. That data exists within the NZ audit process but is not publicly available at the same granularity as WAAGO or QAO reporting.

Does the NZ National Cyber Security Centre's development of baseline cyber security standards for public service organisations — signalled in the April 2025 report — produce different verification outcomes than Australia's Essential Eight framework when compared in subsequent audit cycles?

Does the System Assurance team at DIA — providing independent assurance over high-risk digital investments — produce different prevention failure rates than Australia's ARB model? This is the most structurally precise question the Trans-Tasman evidence makes possible.

These questions cannot be answered with currently available evidence. They are the direct subject for a dedicated Trans-Tasman comparative study — the natural extension of both this addendum and the main working paper.

---

## 6. Conclusion

Canada and New Zealand confirm the main working paper's central finding: the governance-execution gap is not a product of Australia's specific governance architecture. It is a structural condition that persists across federated and centralised models, across different constitutional arrangements, and across jurisdictions with internationally acknowledged framework designs.

Canada produces an almost identical asset inventory failure to Victoria's — begun eight years before the audit, still incomplete, with completion deferred to 2027. It adds a governance coverage gap not visible in the Australian evidence. New Zealand's centralised model produces a risk appetite translation failure rather than an attestation substitution problem — a different expression of the same underlying condition.

The most precise statement of what the Trans-Pacific evidence establishes is this: the gap between governance intent and operational reality is a structural condition of modern public sector IT governance. It is not fixed by framework sophistication, governance model design, or policy addition alone. It is addressed by changing the structural positioning of verification — embedding it at the level where execution happens rather than holding it at the committee level above delivery.

That is the argument the main working paper makes. Canada and New Zealand confirm it.

---

## References

- Office of the Auditor General of Canada. (2025). *Cyber Security of Government Networks and Systems.* https://www.oag-bvg.gc.ca/internet/English/parl_oag_202510_04_e_44720.html
- Office of the Auditor General of Canada. (2023). *Report 7 — Modernizing Information Technology Systems.* https://www.oag-bvg.gc.ca/internet/English/parl_oag_202310_07_e_44348.html
- Office of the Auditor-General New Zealand. (2025). *Mind the Gap: Governing Cyber Security Risks.* https://oag.parliament.nz/2025/cyber-security
- Office of the Auditor General of Canada. (2025). *Opening Statement to the News Conference — Fall 2025 Reports.* https://www.oag-bvg.gc.ca/internet/English/osm_20251021_e_44732.html

---

*This addendum is published by Phil Myint under the OrdoAnimi brand as an independent contribution to public sector IT governance research. No commercial engagement is implied or intended. It extends the comparative analysis published in the main working paper: A Comparative Analysis of IT Governance Frameworks — Investigating the Relationship Between Documented Intent and Reported Outcomes in the Australian Public Sector (2025–2026), Document 1 in this series.*

*This addendum is maintained in the OrdoAnimi research repository at github.com/[your-handle]/velocity-architecture-framework*
