# EA Artefact Type Classification
## The Four-Type Framework

**Author:** ZenCloud Global Consultants  
**Framework:** Velocity Architecture Framework™ (VAF)  
**Published:** May 2026

---

## The classification

Every core EA artefact resolves to one of four functional types. The type determines the value trajectory, the maintenance obligation, and the failure mode when misapplied.

This classification is not a theoretical construct. It is derived from Kotusev's empirical analysis of EA artefact usage across 47 diverse organisations (RMIT University, 2019–2022), which found that all artefacts classify as either facts artefacts or decisions artefacts — and that the real purpose of any artefact is always manifested in its usage, not its documentation.

The VAF four-type classification extends that binary into a functional framework that maps directly to how each artefact type is produced, maintained, and presented.

---

## Type 1 — Decision Instruments

**Function:** Force commitment and shift the burden of proof.

**Mechanism:** A decision instrument exists to make a commitment concrete and on the record. Before the instrument exists, the organisation can move without deciding. After it exists, movement requires either honouring the commitment or explicitly overriding it. The burden of proof shifts to whoever wants to deviate.

**Value trajectory:** Front-loaded. Peak value is at the moment of commitment. Value decays as the assumptions that produced the commitment age and the decision context changes. An untriggered review makes a decision instrument a liability — it provides false confidence in a direction that may no longer be correct.

**Maintenance obligation:** Explicit refresh triggers. Not calendar reviews — condition-based reviews. "This vision is revisited when [named assumption] changes."

**Failure mode:** Produced without forcing a decision. The artefact exists. The commitment does not. This is the most common EA failure mode — producing the form without the function.

**Artefacts:** Architecture Vision, Business Capability Map (TIME heat map), Application Portfolio (TIME classification), Conceptual Data Model, Technology Roadmap, Architecture Roadmap.

---

## Type 2 — Control Mechanisms

**Function:** Operate without authority through the exception process.

**Mechanism:** A control mechanism does not require the EA to have authority over delivery decisions. It creates a process that requires justification for deviation. Justification creates a decision record. A decision record creates accountability. The control operates through the cost of the exception — not through veto power.

**Value trajectory:** Slow build, stable plateau. Value accumulates as the exception record grows. An organisation with three years of compliance review records has a forensic trail. One with three months has a list. The plateau holds only while the exception process is enforced.

**Maintenance obligation:** The exception process must be enforced consistently. A control mechanism that allows undocumented exceptions is decorative. The exception record is the evidence of enforcement.

**Failure mode:** No exception process attached. A standards catalogue without an exception process is a list. Architecture principles without an exception approval mechanism are aspirations. The mechanism is the value — not the content.

**Artefacts:** Architecture Principles, Technology Standards Catalogue, Solution Architecture Document (as decision log), Data Flow Diagram, Architecture Compliance Review.

---

## Type 3 — Signal Generators

**Function:** Make invisible problems undeniable.

**Mechanism:** A signal generator does not solve a problem. It makes a problem visible to the point where it cannot be ignored. The signal is the deliverable. The structural response to the signal is a separate, subsequent activity — requiring political will that the artefact alone cannot provide.

**Value trajectory:** Spike at delivery, then decay without action. Value is highest when the signal is fresh. If no structural response follows within 6–12 months, the artefact becomes evidence of an acknowledged problem that was not addressed. This is worse than no artefact — it demonstrates awareness without accountability.

**Maintenance obligation:** An action owner must be named against every significant signal finding. No action owner means the signal has not been received — it has been filed.

**Failure mode:** Acknowledged and not acted upon. The most dangerous failure mode for this type. An organisation that produces a Business Capability Map heat map showing critical investment gaps, discusses it in a leadership meeting, and then continues existing investment patterns has not benefited from the artefact. It has insulated itself from the discomfort of the finding without addressing the finding.

**Artefacts:** Business Capability Map (heat map), Value Stream Map, Organisation Map, Master Data Map.

---

## Type 4 — Ground Truth Artefacts

**Function:** Accuracy-dependent organisational memory.

**Mechanism:** A ground truth artefact records what is actually true — not what policy says should be true, not what was intended, but what the investigation found. Its value is entirely dependent on the accuracy of what it records and the currency of that accuracy over time.

**Value trajectory:** Bifurcated. Two trajectories exist and there is no middle ground. Maintained artefacts hold value indefinitely — an Integration Architecture kept current is as valuable in year five as in year one. Unmaintained artefacts decay at the rate of organisational change — and in most organisations, that rate is fast enough to render them misleading within 18 months.

**Maintenance obligation:** Continuous, by the people closest to the subject matter — not the architecture team. An Infrastructure Architecture maintained by the architecture team on an annual review cycle will be wrong. The same document maintained by the operators who work with it daily will be right.

**Failure mode:** Produced once and allowed to drift. The drift is the failure. A stale Integration Architecture does not simply become useless — it becomes dangerous. Decisions made on the basis of an inaccurate integration map produce decommission blockers, integration failures, and incident response delays.

**Artefacts:** Integration Architecture, Infrastructure Architecture, Business Process Model (as-is), Master Data Map (authority conflicts), Architecture Decision Records.

---

## The type determines the template

This classification is not academic. It determines what goes in the artefact, how the artefact is maintained, and how the finding is presented to an executive.

A decision instrument is presented as a commitment. The executive is being asked to confirm or make a decision.

A control mechanism is presented as an enforcement request. The executive is being asked to confirm authority for the exception process.

A signal generator is presented as a finding with an ask. The executive is being asked to name an action owner or make an investment decision.

A ground truth artefact is presented as evidence when challenged, or as a risk summary when its accuracy is in question.

Presenting any artefact as something other than its type produces the wrong conversation. Presenting a signal generator (BCM heat map) as if it were a decision instrument (asking for investment approval in the same session) before the finding has been received and owned is the most common executive presentation failure in EA practice.

---

## Classification of all 18 core artefacts

| Artefact | Type | Layer |
|---|---|---|
| Architecture Vision | Decision instrument | Strategy |
| Business Capability Map | Signal generator | Strategy |
| Architecture Principles | Control mechanism | Strategy |
| Value Stream Map | Signal generator | Business |
| Business Process Model | Ground truth | Business |
| Organisation Map | Signal generator | Business |
| Application Portfolio | Decision instrument | Application |
| Integration Architecture | Ground truth | Application |
| Solution Architecture Document | Control mechanism | Application |
| Conceptual Data Model | Decision instrument | Data |
| Data Flow Diagram | Control mechanism | Data |
| Master Data Map | Ground truth | Data |
| Technology Roadmap | Decision instrument | Technology |
| Technology Standards Catalogue | Control mechanism | Technology |
| Infrastructure Architecture | Ground truth | Technology |
| Architecture Decision Record | Ground truth | Governance |
| Architecture Compliance Review | Control mechanism | Governance |
| Architecture Roadmap | Decision instrument | Governance |

---

## Sources

Kotusev, S., Kurnia, S., Dilnutt, R. — *The Practical Roles of Enterprise Architecture Artifacts: A Classification and Relationship.* Information and Software Technology, 147, 2022.

Kotusev, S. — *Enterprise Architecture Artifacts: Facts and Decisions.* RMIT University, 2019.

Gartner — ITScore for Enterprise Architecture. Five maturity levels across eight dimensions of EA practice.

---

*Velocity Architecture Framework™ · ZenCloud Global Consultants · May 2026*
