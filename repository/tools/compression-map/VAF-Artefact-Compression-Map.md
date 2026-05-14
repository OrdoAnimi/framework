# VAF Artefact Compression Map
## Architecture at the Speed of the Decision

**Framework:** Velocity Architecture Framework™ (VAF)  
**Evidence base:** Kotusev et al. — 47 organisations, RMIT University (2019–2022)  
**Governing principle:** The artefact is the record of the decision. Not the input to it.

---

## Three Compression Principles

**1. Resolution discipline.** Identify the decision the artefact serves. Build only to that resolution. Stop.

**2. Sequence inversion.** The artefact is produced after the conversation, not before it. It records the commitment. It does not create the conditions for the commitment.

**3. Artefact merging.** Where two artefacts serve the same decision, merge them into one instrument. Eliminate the separate production cost entirely.

---

## The Compression Map

| Artefact | Type | Standard time | VAF time | Saving | VAF substitution |
|---|---|---|---|---|---|
| Architecture Vision | Decision | 4–8 wks | 1 session | ~85% | One structured executive conversation. Three outputs written immediately after: direction committed to, assumptions live at the time, first decision that would invalidate it. One page. Dated. |
| Business Capability Map | Signal | 6–12 wks | 2–3 days | ~80% | Existing org structure + budget allocation data + 3–5 executive interviews. Heat map produced directly from investment vs strategic priority gap. No taxonomy workshop. No consensus sessions. The gaps are named, not negotiated. |
| Architecture Principles | Control | 4–6 wks | 1 day | ~90% | 5–7 principles maximum. Each written as: the rule, what it prevents, the exception trigger. No rationale sections. No implication lists. Principles that cannot be stated in two sentences are not principles — they are policies in disguise. |
| Value Stream Map | Signal | 3–6 wks | 1–2 days | ~75% | Walk the value stream with the people doing the work. Draw it in the room. Complete when every handoff has a named owner and a wait time estimate. The handoffs with no owner are the signal. That is the only output that matters. |
| Business Process Model | Ground truth | 6–10 wks | 3–5 days | ~70% | As-is only, at the resolution the decision requires. Swim-lane, named roles, named systems. No BPMN notation unless a system is consuming the model. The to-be is a decision list from the as-is gap analysis — not a separate artefact. |
| Organisation Map | Signal | 2–4 wks | Half day | ~90% | Capability list from the BCM (already done). Assign an owner to each. Where no owner exists — that is the map. The white space is the deliverable, not the org chart reproduction. |
| Application Portfolio | Decision | 8–16 wks | 1 week | ~85% | CMDB or existing asset register + annual support cost + strategic alignment question (yes/no/partial). TIME classification applied immediately. Any application without a classification answer in 30 minutes does not have an owner — that is the finding. |
| Integration Architecture | Ground truth | 12–20 wks | 2–3 wks | ~80% | Start from the decommission list, not the full landscape. Map only the integrations that would block the next 3 planned changes. Completeness is not the goal — decommission risk coverage is. |
| Solution Architecture Doc | Control | 4–8 wks | 2–3 days | ~80% | Three sections only: the decision made, the options rejected and why, the assumptions that would invalidate this decision. Everything else belongs in delivery documentation, not architecture documentation. |
| Conceptual Data Model | Decision | 4–8 wks | 1 day | ~88% | One whiteboard session with the business owner of each entity in dispute. Output: agreed definitions, unresolved disputes, who has authority to resolve each. The CDM is the record of that session — not a modelling exercise. A commitment exercise. |
| Data Flow Diagram | Control | 4–6 wks | 3–5 days | ~75% | Scope to personal data flows only unless the regulatory requirement is broader. Map from point of collection to point of deletion. Produced as a compliance instrument first — the architecture view is a secondary output. |
| Master Data Map | Ground truth | 6–10 wks | 2–3 days | ~75% | For each master entity: list every system claiming to be the source of truth. Where more than one system claims authority — that is the map. The conflict is the deliverable. Resolution is a governance decision, not an architecture decision. |
| Technology Roadmap | Decision | 8–12 wks | 3–5 days | ~80% | Dependency sequencing only. What cannot start until what else is done. Dates are placeholders. The sequence is the deliverable. If the executive asks for dates, give ranges tied to named dependencies — not commitments. |
| Technology Standards | Control | 4–8 wks | 1 day | ~90% | Approved list plus one page: what the exception process is, who approves it, and what the cost of non-standard is. No exception process — no standards catalogue. Just a list. |
| Infrastructure Architecture | Ground truth | 10–16 wks | 2–3 wks | ~80% | Scope to components on the critical path for the next major incident. Accuracy over completeness. Maintained continuously by the people operating it — not reviewed annually by the architecture team. |
| Architecture Decision Record | Ground truth | 2–4 hrs | 20 mins | ~80% | Written immediately after the decision. Three fields: what was decided, what was rejected, what would change this decision. No template. No review cycle. The discipline is writing it the same day — not the format. |
| Compliance Review | Control | 2–4 wks | Half day | ~90% | Two questions only: does this compound or reduce technical debt over 5 years, and does this violate a principle? If neither produces a clear finding, the review is advisory. If either does, the finding is named and escalated with a recommendation — not referred to a committee. |
| Architecture Roadmap | Decision | 8–16 wks | 1 week | ~85% | What is funded, in what sequence, with what dependencies. Unfunded items are listed explicitly as risk positions — not omitted. A roadmap that does not show what was decided against is not a decision instrument. |

---

## What VAF Eliminates Entirely

**Taxonomy workshops**  
Consensus sessions that negotiate entity definitions before anyone has named the decision the definition serves. If there is no decision requiring the definition, there is no workshop.

**To-be modelling without as-is**  
Future-state artefacts produced before the current-state gap is documented. The to-be is a decision list derived from as-is analysis — not a standalone artefact.

**Full-landscape documentation**  
Completeness as a goal. VAF scopes every ground truth artefact to the decision it serves: critical path coverage, decommission risk, compliance scope. Not the full landscape.

**Review cycles before decisions**  
Artefacts reviewed by committees before they serve a decision. In VAF, the artefact is the record of the decision already made — not the input to a future approval process.

**Rationale sections in principles**  
Principles with rationale, implications, and examples are policies. A principle that requires explanation to be followed is not enforced — it is negotiated.

---

## The Kotusev Evidence Base

Svyatoslav Kotusev (RMIT University) conducted empirical analysis of EA artefacts across 47 diverse organisations (predominantly Australian) from 2019–2022. Key findings directly supporting VAF compression:

> *"Most organisations do not follow EA methodologies and frameworks strictly but adapt them to their own needs or use them only as idea contributors."*

> *"The real purpose of EA artifacts is always manifested in their usage. All artifacts can be classified into facts EA artifacts and decisions EA artifacts."*

> *"Organizations guided by consultants' best practices already wasted billions of dollars on creating aimless architectural descriptions of little or no business value."*

> *"We never show business stakeholders all the connections and stuff like that — they are not interested in understanding what the interfaces are. The roadmap is a document that helps the business make decisions about their IT investment, so it has to be framed that way."*  
> — Enterprise Architect, Organisation 5 (Kotusev et al., Information and Software Technology, 2022)

VAF is the compression of that empirical finding into an operating model. Every artefact produced at the resolution the decision requires. No more. Every artefact produced after the conversation that surfaces the decision. Not before.

---

## The VAF Operating Model — In One Statement

> The decision conversation happens first. The artefact records the commitment made in that conversation, at the resolution required to protect the decision over time. Everything not serving that function is production overhead, not architecture.

---

*Velocity Architecture Framework™ — Series 5*  
*Evidence base: Kotusev et al. (2019–2022) · Gartner ITScore · CB Insights (2024) · Management Science (2022)*
