# Where the Frameworks Stop
## A Position on the Governance-Execution Gap in Australian, Canadian, and New Zealand Public Sector IT

**Published under the OrdoAnimi Framework**
**By Phil Myint · Principal Architect · OrdoAnimi**
**Date:** May 2026
**Reading time:** approximately 20 minutes

*This position paper builds directly on the comparative analysis of 2024-2026 public sector audit findings published separately under the OrdoAnimi brand. That paper established the pattern across six Australian jurisdictions, Canada, and New Zealand. This paper examines the structural conditions that sustain it — and names the mechanisms through which it persists.*

---

There is a moment in every governance review when the documentation ends and the real question begins.

The policy is current. The framework is signed off. The assurance gate cleared without objection. Yet the system launched with a staff approval rating of 1.79 out of 10, holding the records of some fifteen thousand children.

That moment is not a failure of rules. It is a failure of where oversight sat relative to the work.

The research paper established that this moment is not unique to Queensland. It appears in Victoria, where no agency maintained a complete server inventory despite having the tools to do so. It appears in Western Australia, where 65% of IT control findings were unresolved from prior years. It appears in the ACT, where the most centralised governance structure in Australia produced the same unresolved rate as the most federated. It appears in Canada, where a federal asset inventory project began in 2017 and remained incomplete in 2025 with completion now expected no earlier than 2027. It appears in New Zealand, where most examined public organisations carried higher residual cyber security risk than their stated appetite — with governors uncertain whether the gap could be closed.

Six Australian jurisdictions. Two international comparators. Eight governance models of varying design and centralisation. One structural condition.

The research paper identified the pattern. This paper names the mechanism.

---

## A Distinction That Matters

Before examining the mechanism, a distinction needs drawing that the rest of the argument depends on.

Most governance models operate on attestation. Someone produces a document. Someone else reviews it. A committee endorses it. The artefact represents a claim that a control exists, a standard is met, a risk is managed. Attestation tells you the organisation believes something to be true. It does not tell you whether it is true at the point where technology change actually occurs.

Runtime verification is different. It confirms that a control is operating in production — not in a document, but in the live configuration of a platform, a pipeline, or a network. It does not ask whether a standard was approved. It asks whether the standard is enforced the moment someone provisions a resource or deploys a change.

Runtime verification is a positioning principle, not a product category. It does not require any specific tool or methodology. It requires that the structural conditions for confirming operational truth exist at the level where decisions are made — regardless of what technology implements them.

The persistent audit findings documented in the research paper share a common property. They are failures of runtime verification being treated as though periodic attestation were sufficient. That gap — between what is attested and what can be confirmed at the point of execution — is the central thread.

In New South Wales, 59% of agencies had no independent assurance over their own compliance with the NSW Cyber Security Policy. That is attestation without verification at its most direct. In Victoria, six agencies had automated asset discovery tools and none had configured them to scan their entire network. The tool existed. The attestation of intent existed. The verification of operational truth did not. In Canada, the federal government attested to a comprehensive cyber security strategy while 58% of federal organisations operated outside the central protective services that strategy depended on.

The OrdoAnimi Framework calls the space where this gap accumulates Governance Drag.

---

## What Governance Drag Looks Like at Scale

Governance Drag is the accumulated friction that arises when verification is structurally positioned above the level where execution occurs, preventing timely detection, closure, and learning from deviation. It is the measurable outcome of that misalignment — not the cause but the symptom that becomes self-sustaining when deviation accumulates without correction.

Governance Drag is not the absence of process. It is not bureaucracy under a different name. Bureaucracy describes volume. Governance Drag describes position — specifically, where in the structural hierarchy verification has detached from execution.

The Queensland experience illustrates the mechanism precisely. Architecture Review Boards functioned. Investment oversight gates were cleared. The governance architecture performed its documented role. What it did not do — what it structurally could not do — was maintain visibility into whether controls were actually operating at the delivery layer. The 43% unresolved rate is not evidence that the remediation framework failed. It is evidence that verification was not embedded where execution happened. The framework sat at one altitude. The work sat at another.

Western Australia's 65% unresolved rate tells the same story at larger scale. The WAAGO conducted its audits. The findings were documented. The governance layer confirmed the deficiencies existed. What it could not confirm — because it was not positioned to confirm it — was whether remediation had actually occurred in the production environment where the control needed to operate.

Canada's asset inventory failure is the most extended expression of Governance Drag in the Trans-Pacific evidence base. The project to establish a complete inventory of government IT devices was initiated in 2017. For eight years the governance layer acknowledged the gap. For eight years the gap persisted. The Auditor General's 2023 modernisation report documented that the same legacy problem was first identified in 1999 — twenty-four years before that audit. The governance instruments saw the problem continuously. They were not positioned to resolve it.

This is what Governance Drag looks like when it compounds not across quarters but across decades.

---

## The Altitude Problem

Decision Altitude in OrdoAnimi describes the structural level at which a decision is made — specifically, the combination of three dimensions: authority to close the item, observability of whether it is done, and enforcement proximity to act when it is not. Every decision has an appropriate altitude where all three dimensions are sufficient. When decisions sit at the wrong altitude, two failure modes emerge.

The first is Altitude Collapse. This occurs when a decision that belongs at the structural layer gets absorbed into the operational layer — when governance weight lands on a delivery team that lacks the structural position to carry it. A remediation cycle managed entirely at the operational layer tracks individual issues without seeing the pattern. It resolves the presenting problem without addressing the mechanism that produced it.

The Unify case is a studied example. Formal governance processes operated correctly at their designed altitude. The system cleared its review. What the assurance gate could not see — because it was not positioned to see it — was whether the system would actually work for frontline staff in the field. The gate was positioned to see documents. It was not positioned to see production.

The New Zealand finding names a related but distinct expression of this failure at the governance layer itself. The Mind the Gap report found that most examined organisations carried higher residual risk than their stated appetite — and that governors were uncertain whether they could close the gap or what it would cost to do so. New Zealand's centralised model produces a gap located in the translation from risk appetite to operational mandate, rather than the attestation substitution seen in Australia. Both reflect structural distance between governance intent and the execution layer. The remedy for each is different.

These represent two distinct expressions of Altitude Collapse. The first occurs when the gate is positioned correctly within its authority but cannot see the execution layer — the signal exists but is invisible from the governance altitude. The second occurs when the strategic layer has authority and visibility but cannot translate risk appetite into verifiable operational requirements — the intent exists but the translation mechanism is absent. Both produce persistent gaps.

The second failure mode is the inverse: decision weight held too high, leaving the delivery layer without the authority or context to manage its own control environment. Canada's governance coverage problem is this failure mode expressed at national scale. Central cyber security services were available. Fifty-eight per cent of federal organisations were not required to use them. Of those eligible, many did not. The governance model held decision authority at the centre without embedding the enforcement mechanism at the level where adoption actually occurs. The result is a fragmented protective landscape where the central authority cannot see — and therefore cannot govern — the majority of the environment it is responsible for.

On accountability: altitude-based thinking clarifies accountability rather than diffusing it. When a control fails, the question is not simply who was responsible — it is at what altitude the responsibility sat and whether that altitude had the authority, observability, and enforcement proximity to discharge it. Australia's audit findings cannot reliably answer that question. They document outcomes without locating the decision that produced them. That distinction is the difference between finding a problem and being able to fix it.

---

## Three Conditions That Sustain the Pattern

The research paper identified that the prevention-detection-remediation gap appears across structurally different governance frameworks in eight jurisdictions. Three structural conditions sustain it consistently.

**First, verification operates at a remove from execution.** Most compliance checks — audit committees, periodic reviews, assurance gates, board reporting — see documents and attestations rather than live system states. They can confirm a policy exists but not whether it is enforced when a team makes a configuration change or a third party modifies a network rule.

This is not a question of organisational hierarchy alone. It is a combination of the three altitude dimensions: where the observer sits in the chain of decision rights, what the observer can see at runtime, and how close the observer is to the mechanism that can act on a deviation. When all three dimensions are distant from the execution layer, findings become chronic. No one with authority to close them can see them clearly. No one who can see them clearly has the authority to act.

The 78% repeat rate in ANAO interim findings is the clearest quantitative expression of this condition at the federal level. The findings are seen. They are documented. They are carried forward. They are not closed. The mechanism for closing them is not positioned where closing actually happens.

**Second, the path of least resistance does not lead to compliance.** In most environments, the easiest way to ship is still a manual path that sidesteps the control. The secure configuration is not the default. Access controls are documented rather than enforced by the platform. When the easiest path is the wrong path, correct behaviour becomes an act of individual discipline — and at scale, across hundreds of decisions under deadline pressure, discipline alone cannot hold.

Victoria's server inventory finding is the case in point. Six agencies had automated discovery tools. Full configuration was harder than partial configuration. Partial became the steady state, six times across six agencies. Canada's non-engagement pattern is the same condition expressed at the governance layer. Using central security services required active engagement. Not using them required nothing. The path of least resistance led away from the compliant state.

The OrdoAnimi Framework calls the route that makes correct behaviour the default The Compliant Path. When it exists, compliance does not require discipline. It requires following the path of least resistance, because that path has been engineered to be the correct one. A Compliant Path exists when the action that requires the fewest permissions, the least manual documentation, and the shortest approval chain is also the action that satisfies the relevant control.

The Compliant Path is a positioning principle, not a product category. It does not require specific tooling or a DevSecOps methodology. Those disciplines focus on pipeline speed and integration. The Compliant Path focuses on whether the structural conditions for correct behaviour exist at the altitude where decisions are made. A team can have a fully integrated delivery pipeline and still operate in an environment where the correct governance behaviour is harder than the incorrect one. Pipeline speed does not resolve structural position.

The audit evidence across eight jurisdictions is, in aggregate, evidence that The Compliant Path was not built into the control environments being governed.

**Third, deviation does not become intelligence.** When a control is bypassed — through a workaround, a deferred remediation, a non-engaged service — the system rarely logs it in a way that aggregates into a pattern. Each deviation is treated as an isolated event. A single unresolved finding might be defensible. Sixty-five per cent of findings unresolved from prior years across Western Australia and the ACT is a signal. Without aggregated, attributable deviation data reviewed by someone with the authority to adjust the control, the signal never forms. The governance system cannot calibrate itself. It accumulates unresolved findings instead.

Canada's January 2024 cyberattack response failure illustrates this at the incident level. Lack of information sharing between TBS, CSE, and Shared Services Canada delayed response and allowed the attacker prolonged access. The information existed across three bodies. It was not aggregated in a way that enabled coordinated action. The deviation — an active attack — did not become intelligence at the speed and level required to respond.

Underpinning all three conditions is a reality that public sector governance cannot simply wish away. Accountability is distributed by design. Decisions move through committees, partly to guard against concentrated authority and partly to satisfy the architecture of ministerial oversight. That distribution has a structural consequence: when no single person is on the hook for closing a finding, and when being the person who signs off carries career cost while staying verbal carries none, the incentive to keep a finding alive is powerful. This is not dysfunction. It is rational behaviour inside the system as currently constructed.

This represents a genuine structural tension. The very mechanisms that prevent autocratic risk-taking also prevent decisive risk closure. Any attempt to close the gap has to work with that reality, not against it.

---

## What the Operational Consequence Tells Us

The ASD Annual Cyber Threat Report 2024-25: over 84,700 cybercrime reports, over 1,200 significant cyber security incidents, an 11% increase year on year, and a 111% rise in attacks on critical infrastructure. State and local governments remained among the highest incident-reporting sectors.

These numbers are not separate from the audit findings. They are the same structural failure expressed in two different measurement registers. Unresolved access management deficiencies, incomplete server inventories, fragmented protective service adoption, and absent independent compliance assurance are not administrative imperfections. They are the attack surface. The ASD data quantifies what happens when that surface remains open.

Canada blocked 6.6 trillion malicious cyber events in a single year while simultaneously lacking a complete inventory of the devices it was protecting. New Zealand's public organisations carried residual risk above their stated appetite while governors were uncertain whether closure was achievable. The operational consequence is not a future risk. It is a present and measurable reality across all three countries.

---

## What This Means for Practitioners

Three questions worth carrying directly into current work.

If your remediation backlog holds items from prior years, the useful question is not why each individual item remains open. It is whether your verification mechanism sits close enough to where remediation actually happens — close in authority to close the item, close in observability to see whether it is done, and close in enforcement proximity to act when it is not. The QAO flagged that entities are not checking that implemented controls are effective. That is the distance problem in audit language.

If an assurance gate cleared a system that later stumbled in the field, the gate saw what it was designed to see. The sharper question is whether a verification checkpoint closer to the execution layer — a pipeline gate, a runtime compliance check, a realistic pre-go-live environment — might have surfaced the gap. A system can pass every security control and still fail the people who have to use it. That is a different kind of gap and it deserves its own structural attention.

If your third-party providers consistently appear in audit findings, the issue is rarely the providers alone. It is that the mechanism for verifying their controls sits too far from where those controls operate. The NSW Auditor-General identified weak oversight including unclear contractual roles and agencies not receiving control compliance reports from vendors. Where execution is outsourced the question shifts: can the contract, the SLA, and the evidence-gathering provisions be structured so that verification is possible at the execution layer, or is the agency structurally limited to checking paperwork? That distinction determines whether third-party findings can be closed or only documented.

---

## The Trans-Pacific Pattern and What It Settles

The research paper's most significant analytical finding is that the governance-execution gap is not a product of any specific governance architecture. It persists across federated models, centralised models, and unitary models. It persists across jurisdictions with internationally validated framework designs. The OECD ranked Australia second globally in digital government in 2025. Canada and New Zealand have their own internationally acknowledged governance frameworks. All three produce the same underlying structural condition.

This settles one important question. The gap is not closed by framework sophistication, governance model design, or policy addition alone. The OECD review of Australia's IOF confirms the framework is sound. The audit evidence confirms the gap persists. Both are true simultaneously because they measure different things. The OECD measures design maturity. Audit offices measure operational reality. The space between those two measurements is where the problem lives.

New policies — including Australia's DTA Cloud Computing Policy effective July 2026 — are necessary and represent meaningful steps. The Canadian evidence gives the clearest indication of what happens when structural change does not accompany policy addition over extended periods. Canada identified its legacy modernisation problem in 1999. It has issued policies, strategies, and frameworks continuously since then. As of 2025, two thirds of federal applications remain in poor health and the asset inventory project initiated in 2017 remains incomplete. Policy without structural change in how verification is positioned produces documentation of the problem rather than resolution of it.

---

## A Note on Culture

The counterargument that culture — not structure — is the real problem is valid up to a point. The pattern the research paper identifies across eight jurisdictions is precisely about the gap between formal structures and actual behaviour. Culture is a genuine contributing factor.

But culture is not the root cause. It is the residue of repeated structural incentives. When The Compliant Path is absent, an organisation's culture gradually normalises workarounds — not because people are negligent, but because the structure rewards the workaround over time. Changing culture without changing the structural conditions in which behaviour occurs is an intervention that operates against the grain of the system rather than with it.

---

## Where This Leads

The evidence base established across both papers leaves three questions open for further research and practice.

Does Canada's 2017 asset inventory project — if completed by 2027 as now projected — produce measurably different audit outcomes in subsequent cycles? That is a direct empirical test of whether structural change in verification positioning changes operational results.

Does New Zealand's development of baseline cyber security standards for public service organisations — signalled in the April 2025 OAG report — reduce the gap between residual risk and stated risk appetite in subsequent audit cycles? That is the most precise Trans-Tasman empirical question the current evidence makes possible.

Does Australia's 2026 Cloud Computing Policy produce measurably different IT control findings in the 2027-2028 audit cycle — or does the unresolved rate remain consistent with prior years? That is the domestic test of whether policy addition without structural repositioning of verification changes outcomes.

These are not rhetorical questions. They are researchable. The audit infrastructure to answer them already exists across all three countries. The next audit cycle will either confirm or challenge the structural positioning argument this paper advances.

---

## A Note on the Trans-Tasman Context

New Zealand's more centralised all-of-government model offers a genuinely useful contrast to Australia's federated design. The Mind the Gap finding — that most organisations carry higher residual risk than their stated appetite — is a different expression of the governance-execution gap than Australia's attestation substitution problem. New Zealand's centralised model produces a gap located in the translation from risk appetite to operational mandate. Australia's federated model produces a gap in the substitution of attestation for verification. Both reflect structural distance between governance intent and the execution layer.

The empirical question a serious Trans-Tasman comparison must answer is whether New Zealand's centralised model produces measurably lower unresolved deficiency rates than Australian jurisdictions when compared at equivalent scale. The current evidence does not answer that question. The NZ report deliberately does not identify organisations or provide deficiency counts comparable to WAAGO or QAO reporting. That data exists within the NZ audit process. Its public availability would make the Trans-Tasman comparison empirically precise rather than structurally inferential.

---

*The neutral comparative analysis this position paper draws from is published separately under the OrdoAnimi brand, with full source citations from the 2024-2026 ANAO, QAO, NSW Auditor-General, VAGO, WAAGO, ACT Audit Office, ASD, OECD, Office of the Auditor General of Canada, and NZ Office of the Auditor-General reports.*

*OrdoAnimi concepts referenced — Governance Drag, Decision Altitude, Altitude Collapse, The Compliant Path — are components of the OrdoAnimi Framework.*
