# Integrity Arc — VP6 Practitioner Assessment

**VAF VP6 — Practitioner Viewpoint | Human Layer**
**Instrument: Auctor Custos — Custodian of Architectural Integrity**

> This is not a checklist. It is a set of positions.
> Each position is available to the practitioner at any point in an engagement.
> The arc does not move in one direction only.

---

## Engagement Context

| Field | Value |
|-------|-------|
| **Practitioner** | Architect — Platform Transition and Capability Design |
| **Engagement / Programme** | DataStage, Cognos, and VMware Deprecated Platform Migration to Cloud — Capability Model for Decentralisation of On-Premises Workloads |
| **Date of assessment** | 2025-07-14 |
| **Current position in arc** | Authorship — contested. Boundaries — not yet declared. Refusal — one trigger already visible. Staying — conditional. Exit — not yet triggered but proximity is real. |

---

## Position 1: Authorship

**Assessment: Authorship is structurally at risk in this engagement — not yet absent, but conditions are present that will convert it to facilitation if boundaries are not drawn now.**

This engagement involves three deprecated platforms — DataStage (ETL/data integration), Cognos (BI/reporting), and VMware (on-premises compute virtualisation) — being displaced simultaneously in the context of a broader capability model and decentralisation strategy. The combination is not a migration. It is a capability transformation that organisations routinely mislabel as a migration in order to reduce its apparent complexity and avoid committing to new operating model decisions.

The absence of stated constraints is the first signal. A migration of this scope with no declared constraints means either the constraints exist but have not been surfaced — ownership questions, budget hard stops, organisational appetite for cloud-native rearchitecting — or the engagement has been scoped as a capability mapping exercise in order to defer those decisions. Either condition suppresses authorship and replaces it with documentation of options.

**Indicators that authorship is present:**
- The practitioner is naming cloud-native replacements for DataStage and Cognos specifically — not presenting a landscape of candidates and asking the organisation to choose
- The capability model is being written with decentralisation as a design intent, not as one option among several
- Trade-offs between cloud-native rebuild and lift-and-shift are named and concluded, not listed
- The VMware displacement is being treated as a compute operating model decision, not a hosting question

**Indicators that authorship is absent:**
- The engagement is being framed as a capability mapping exercise with no binding capability ownership assigned
- DataStage replacement options are being documented without a stated recommendation
- Cognos is being listed as a reporting tool to be "assessed for cloud equivalence" rather than being evaluated against a declared BI architecture direction
- The practitioner is described as "supporting the platform team" or "facilitating the discovery process"

**Condition that will determine this:**
Whether the practitioner is being asked to produce a capability model as a precondition for a decision that someone else will make later — in which case authorship is structurally absent — or whether the practitioner is empowered to write the capability model as the decision. These are different instruments. If it is the former, the practitioner is a researcher. Name that cleanly or refuse the framing.

☐ Authorship present
☑ Authorship contested — condition named above must be resolved before the next artefact is produced

---

## Position 2: Boundaries

**Assessment: Boundaries have not been declared. They must be written before the capability model proceeds.**

The scope of this engagement spans three platforms, a cloud transition, a capability model, and a decentralisation strategy. Without a written boundary declaration, the practitioner will be held accountable for outcomes that depend on decisions that have not yet been made — cloud provider selection, budget approval, business domain ownership of decentralised capabilities, and the operating model that governs them post-migration.

**What the practitioner will design, decide, and own:**

- The capability model for cloud-native equivalents of DataStage, Cognos, and VMware workloads — including recommended target capabilities, not a neutral inventory
- The architecture position on decentralisation: which capabilities belong at domain level and which remain central, with explicit rationale
- The trade-off assessment between cloud-native rearchitecture and lift-and-shift for each deprecated platform, with a stated recommendation
- The boundary conditions under which each migration decision is architecturally sound versus operationally risky

**What the practitioner will not own — and who must own it instead:**

- Cloud provider selection: this is a commercial and procurement decision. Architecture informs it. The practitioner will not own the outcome of a vendor decision that has not been made
- Business domain readiness for decentralisation: capability decentralisation requires business domain owners to accept accountability for the capabilities they will own. The practitioner will not absorb that accountability by proxy through the capability model
- DataStage pipeline inventory and data lineage audit: if this has not been done, it must be scoped as a separate workstream with a named owner. The practitioner will not embed an undone data audit inside a capability model and present the result as architecture
- VMware estate inventory: the compute and workload inventory is an infrastructure operations input. The practitioner requires it. The practitioner will not produce it
- Timeline and resourcing decisions: migration sequencing that depends on funding, resourcing, or organisational change decisions is not an architecture output. The practitioner will provide sequencing recommendations contingent on named inputs. The practitioner will not own the schedule

**The conditions under which the practitioner's involvement has meaning:**
- At least one named decision-maker with authority over cloud platform direction is engaged
- The capability model will produce binding decisions, not recommendations for further review
- Business domain owners are identified and will be consulted on decentralisation scope

**The conditions under which it does not:**
- The capability model is being produced to satisfy a programme milestone rather than to make decisions
- No one with authority to commit to cloud-native replacement tooling is in the room
- The engagement is expected to produce a unified strategy document that avoids naming trade-off conclusions

---

## Position 3: Refusal

**Assessment: One specific refusal is already indicated. The practitioner should not produce it without prior decisions in place.**

**The piece of work that must be refused without prior commitment:**

**A cloud migration roadmap that spans DataStage, Cognos, and VMware as a unified programme without binding capability ownership decisions.**

This engagement will almost certainly generate a request for a "cloud migration roadmap" or "platform transition plan" that presents all three deprecated platforms on a single timeline with capability model alignment. This document is not architecture. It is the appearance of a plan built on top of unresolved decisions about who owns what, which capabilities are being rebuilt versus replicated, and what the cloud operating model actually looks like.

Producing this document — which will look complete, will be used to report programme progress, and will be cited in steering committee updates — without the underlying decisions being made converts the practitioner into a document producer. It also absorbs ambiguity from three separate platform replacement decisions into one artefact and makes the practitioner responsible for the coherence of decisions that were never actually made.

**Refusal sounds like this:**

> "I can produce a sequenced migration recommendation once we have binding decisions on cloud provider, capability ownership for each domain, and the operating model position on decentralisation. What I will not produce is a migration plan that presents those as resolved when they are not. If the programme needs a progress document for steering, I can write a decision register that names exactly what is open and what it is blocking. That is an accurate representation of where we are."

**The second piece of work to watch:**

A Cognos-to-cloud BI capability assessment that presents a tool landscape without naming a recommendation. If the organisation has not committed to a BI architecture direction, the practitioner will be asked to map Cognos capabilities against cloud BI tools — Power BI, Looker, Tableau, native cloud analytics — and present "options." This is not architecture. Refuse the neutrality. State the recommendation or decline to produce the document.

---

## Position 4: Staying

**Assessment: Staying is currently warranted — conditionally and with a defined review point.**

The engagement has legitimate architectural work in it. Deprecated platforms with end-of-life trajectories on three distinct infrastructure and tooling layers, combined with a genuine capability model requirement, constitute real architectural scope. The decentralisation intent, if it is a real intent and not a political gesture, requires architectural authorship — someone has to draw the capability boundary lines and defend them.

The practitioner can stay and do meaningful work if:

- The boundary declaration from Position 2 is accepted and the capability model is treated as a decision instrument
- At least one of the three platform replacement decisions reaches binding resolution within the first engagement cycle
- The practitioner is not being used to produce documentation that gives the appearance of programme progress while the actual platform decisions remain open

**Staying becomes provisional — assessed weekly — if:**

- The capability model is reviewed by a steering committee that provides feedback but makes no decisions
- The DataStage replacement discussion loops back to "we need more discovery" after two sessions
- The VMware decisionhas been delegated to infrastructure operations with no architecture authority attached
- Cognos is being treated as a reporting tool replacement rather than a BI capability decision, reducing it to a procurement exercise that architecture is decorating

**Staying ends if:**

- The practitioner is asked to present the capability model as a completed strategy when the underlying decisions are not made
- The engagement converts to a documentation service for a programme that has no intention of making binding capability decisions
- All three platform tracks operate independently with no governing capability model authority, and the practitioner's role becomes coordination rather than architecture

---

## Position 5: Exit

**Assessment: Exit is not yet triggered. Proximity is real. One condition would trigger it immediately.**

Exit is not yet required. The engagement is at early assessment stage and the practitioner has not yet been asked to misrepresent the state of the work.

**The condition that would trigger immediate exit:**

Being asked to sign off a cloud migration roadmap — or present one to a steering committee — that represents the capability model as complete and the migration as sequenced, when the business domain ownership decisions, cloud operating model, and at least one platform replacement decision are unresolved.

This is the specific form of misrepresentation this engagement is likely to produce. It will not be framed as misrepresentation. It will be framed as "we need to show progress" or "the steering committee just needs high-level comfort." The document will be written, will be presented, and will be used as evidence that the programme is on track. The practitioner's name will be on it. That is the exit condition.

**Secondary exit signal:**

If the decentralisation strategy is used to distribute accountability without distributing authority — that is, if business domains are told they own capabilities they will not be resourced or empowered to operate — and the practitioner is expected to design an operating model that ratifies that arrangement, exit is appropriate. Designing an operating model that the practitioner knows is not viable is not architecture. It is cover.

**Exit, if reached, looks like this:**

> "I am not in a position to continue as architect on this programme. The decisions that would allow me to produce architecture with integrity have not been made, and the programme is not structured to make them. I am prepared to document the open decisions and their current state as a handover record. I am not prepared to present the current work as a completed architecture."

---

## Sacred Cows Register

These are the beliefs active in this type of engagement that will resist clarity by protecting dysfunction over design. They must be named.

---

### SC-01: "The migration is the strategy."

**The belief:** Moving DataStage, Cognos, and VMware to cloud is itself the strategic outcome. Once the platforms are in cloud, the organisation will be modern, agile, and decentralised.

**What it protects:** The absence of any genuine capability or operating model decision. If the migration is the strategy, no one needs to decide what the cloud capabilities will actually do differently, who will own them, or how the operating model changes. The migration becomes a logistics exercise dressed as transformation.

**What it prevents:** A capability model that distinguishes between replicated legacy capabilities and genuinely redesigned cloud-native ones. The moment the practitioner draws that distinction, someone has to decide which capabilities are being rebuilt and which are being preserved — and that decision has owners and consequences.

**How it presents:** "We don't need to redesign — we just need to get off the deprecated platforms. We can evolve once we're in the cloud."

---

### SC-02: "DataStage is too complex to replace — we'll cloud-host it instead."

**The belief:** The DataStage pipeline estate is so large, so undocumented, and so deeply embedded in data flows that replacing it with a cloud-native integration capability is not realistic. The safe option is to cloud-host DataStage via a managed VM or container and call it cloud.

**What it protects:** The absence of a data integration capability decision and the absence of a data lineage audit. If DataStage cannot be replaced, the practitioner cannot demand a recommendation. The work reduces to hosting logistics.

**What it prevents:** A genuine decision about the organisation's cloud-native data integration capability — whether that is Azure Data Factory, AWS Glue, Databricks, or a domain-owned pattern — and the data lineage audit that would reveal what the pipelines actually do and which ones should be retired.

**How it presents:** "DataStage has thirty years of business logic in it. We can't just swap it out. Let's lift and shift first and then assess."

---

### SC-03: "Cognos is a reporting tool — the business just needs equivalent reports in the cloud."

**The belief:** Cognos is a presentation layer. Replacing it means finding a cloud BI tool that produces the same reports. This is a tool substitution, not a capability decision.

**What it protects:** The absence of a BI architecture decision. If Cognos is just a reporting tool, no one has to decide what the organisation's data and analytics capability model looks like, who owns it, how it is governed, or what the relationship is between centralised BI and domain-level analytics under decentralisation.

**What it prevents:** A genuine BI and analytics capability model that distinguishes between operational reporting, self-service analytics, and governed data products — and that makes the decentralisation of analytics capability a designed outcome rather than an accident of tool migration.

**How it presents:** "The business just wants their dashboards to work. Can we get a lift of the Cognos reports into Power BI and move on?"

---

### SC-04: "Decentralisation means letting each team choose their own tools."

**The belief:** Decentralising the on-premises capability means removing central control and letting business domains make their own technology decisions. This is empowerment. It is what cloud enables.

**What it protects:** The absence of a governed decentralisation model. If decentralisation means each domain chooses its own tools, no one needs to design the capability boundaries, the shared services model, the data exchange standards, or the governance layer that makes a decentralised architecture coherent rather than fragmented.

**What it prevents:** An operating model that distinguishes between domain autonomy over capability execution and architectural coherence over data, integration, and security standards. Decentralisation without a governing model is not architecture. It is the dissolution of architecture.

**How it presents:** "We're moving to a federated model. Teams will be empowered to make their own choices. The cloud gives us that flexibility."

---

## Analytic Tests

### Test 1: Is the practitioner being asked to clarify decisions or manufacture them?

**Reading:** The engagement is currently asking the practitioner to produce a capability model for a cloud solution and decentralisation strategy. Without a declared owner of the decentralisation decision, a named cloud platform direction, and a stated position on whether DataStage, Cognos, and VMware are being replaced or replicated, the practitioner is being asked to produce a document that gives the appearance of a strategy without the underlying decisions existing. This is manufacturing, not clarifying. The practitioner must name this explicitly and make the decision inputs a precondition for the capability model.

---

### Test 2: Who absorbs the consequences if the architecture is wrong?

**Reading:** In this engagement, the consequence absorption risk is concentrated on the practitioner and distributed away from the decision-makers. If the capability model recommends a cloud-native DataStage replacement that the organisation later abandons because the pipeline audit was never done, the practitioner's recommendation will be cited as the reason the approach failed. If the decentralisation model does not work because business domains were not resourced to own their capabilities, the capability model will be cited as having "missed" the operating model requirements. The practitioner must write the boundary declaration in a way that names these consequence-absorption risks explicitly and assigns them to the correct owners.

---

### Test 3: Has the engagement already converted the practitioner into a document producer?

**Reading:** Not yet — but the trajectory is toward it. The framing of the engagement as a "capability model for cloud solution and decentralisation of on-premises" is an analytic and documentation task. If the practitioner accepts that framing without inserting authorship — by stating recommendations, drawing capability boundaries, and naming what decisions the model requires — the engagement will default to documentation. The practitioner produces a capability map. The map is reviewed. Feedback is incorporated. Another version is produced. No decisions are made. The practitioner is a document producer within two cycles if the authorship position is not asserted now.

---

### Test 4: What is the honest velocity of this engagement — how fast is ambiguity actually expiring?

**Reading:** Low. Three deprecated platforms with end-of-life urgency create the appearance of velocity — the organisation must move because the platforms are going out of support. But urgency from platform obsolescence is not the same as decision velocity. The DataSt