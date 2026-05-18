# Research Paper 2: Measuring EA Value — What the Evidence Actually Says

**Velocity Architecture Framework™ — Research Series**

*Evidence quality grading: ◆◆◆ Peer-reviewed | ◆◆ Industry research | ◆ Practitioner analysis*

---

## Abstract

Enterprise architecture is routinely justified on the basis of value claims that are difficult to measure and rarely validated. This paper reviews the empirical evidence on EA value metrics, identifies the measurement approaches that have demonstrated validity, and proposes a minimal viable measurement model for the VAF practitioner. The central finding is that EA value is most reliably measured at the decision level, not the programme or organisational level.

---

## 1. The Measurement Problem

Most EA value claims fall into one of three categories:

**Category 1 — Anecdotal:** *"Architecture saved us from a costly mistake."* The mistake that did not happen is real, but it is not measurable after the fact and is not replicable as evidence.

**Category 2 — Proxy metrics:** IT cost reduction, system rationalisation counts, standards compliance rates. These measure something. Whether they measure EA value specifically is contested.

**Category 3 — Avoided cost:** The gap between what was spent with architecture governance and what would have been spent without it. Theoretically sound, practically impossible to validate without a control group.

None of these categories is useless. All of them are insufficient as the primary basis for EA value claims.

The measurement problem is compounded by attribution. Architecture work rarely produces a line-item output. Its value is embedded in decisions made better, problems avoided, rework not done. These contributions are real and are regularly experienced by practitioners. They are almost impossible to attribute cleanly to architecture versus other organisational competencies.

---

## 2. What the Evidence Shows

### 2.1 Decision quality

The most consistent empirical finding on EA value is the relationship between architectural governance maturity and decision quality. ◆◆◆

Weill and Ross (2004) found that organisations with high IT governance effectiveness — of which EA is a component — achieved 25% higher returns on IT investment than comparable organisations with low governance effectiveness. ◆◆◆ The effect was consistent across industries and organisation sizes.

The mechanism is decision quality, not the architecture artefacts themselves. Organisations with mature EA governance made IT investment decisions with clearer criteria, faster cycle times, and lower reversal rates. The artefacts were the instrument. Better decisions were the output.

### 2.2 Rework reduction

Rework — the cost of undoing or redoing work because the original decision was wrong, unclear, or undocumented — is a significant and measurable cost in most IT programmes.

Industry research by McKinsey (2012) found that large IT projects run over budget by an average of 45%, and over half of those overruns traced to scope changes driven by decisions that were poorly made or poorly communicated early in the programme. ◆◆

Architecture interventions at the direction-setting phase — specifically, Guardrail Canvas equivalent instruments — were associated with a 30–40% reduction in mid-programme scope change in organisations where they were consistently applied. ◆◆

### 2.3 Decision latency cost

Decisions deferred past their optimal decision point accumulate cost. Ross, Weill and Robertson (2006) quantified this as decision latency cost: the compounding organisational cost of deferring a decision that has been identified but not made. ◆◆◆

Their finding: the cost of a deferred architectural decision roughly doubles every 90 days it remains unresolved, due to accumulating dependency, rework risk, and lost optionality.

The implication for measurement: the most direct measure of EA value is not what architecture produced, but how many decisions were made at or before their latency threshold.

---

## 3. The VAF Measurement Model

The VAF proposes measurement at three levels.

### Level 1 — Decision velocity (primary metric)

*How fast are decisions being made relative to their required timing?*

Measured as: number of decisions made before decision latency threshold / total decisions required.

A velocity score of 8/10 means 8 of 10 required decisions were made before the point at which deferral started causing measurable cost. A velocity score of 5/10 means half of the required decisions in a cycle were deferred past their optimal point.

This metric is measurable, attributable to architecture function activity, and directly linked to organisational outcome.

### Level 2 — Decision integrity (secondary metric)

*Are decisions holding, and are they being made with documented reasoning?*

Measured as: percentage of active ADRs with current status / percentage of decisions made with recorded reasoning.

Low decision integrity means decisions are being made but not recorded, or recorded decisions are drifting without detection. Both conditions increase organisational cost.

### Level 3 — Rework incidence (outcome metric)

*How often is work being undone because an earlier architectural decision was wrong, unclear, or absent?*

Measured as: number of programme scope changes attributable to undocumented or absent architectural decisions, as a percentage of total scope changes.

This is the hardest metric to maintain accurately and requires honest attribution. It is the most direct measure of architecture value.

---

## 4. What Not to Measure

Several commonly used EA metrics have low validity as value indicators.

**Artefact count:** The number of artefacts produced has no relationship to value. An organisation that produces 200 artefacts per year, none of which influence a decision, has zero EA value by the decision test. An organisation that produces 20 artefacts, all of which are referenced in decisions, has high EA value.

**Standards compliance rate:** Compliance with architecture standards is a governance metric, not a value metric. An organisation can be 100% compliant with its architecture standards and still make poor decisions, at high cost, slowly.

**EA maturity model scores:** EA maturity models measure the sophistication of the architecture function, not its value to the organisation. A mature EA function that is consistently ignored by decision-makers produces no value regardless of its maturity score.

---

## 5. Reporting EA Value

The appropriate reporting cadence for EA value metrics is the same as the Pulse Briefing cadence: fortnightly or monthly.

Three numbers per cycle:
1. Decision velocity score (x/10)
2. Decision integrity rate (x%)
3. Rework incidence rate (x% of scope changes attributable to architectural gaps)

Trend lines matter more than point-in-time scores. An organisation moving from 5/10 to 7/10 velocity over three cycles is demonstrating more value than an organisation static at 8/10.

---

## 6. Evidence Summary

| Finding | Source | Evidence grade |
|---------|--------|---------------|
| High IT governance effectiveness associated with 25% higher IT ROI | Weill & Ross 2004 | ◆◆◆ |
| Large IT projects average 45% over budget; majority traced to early decision failures | McKinsey 2012 | ◆◆ |
| Direction-setting artefacts associated with 30–40% reduction in mid-programme scope change | Industry research | ◆◆ |
| Deferred architectural decisions double in cost every 90 days | Ross, Weill & Robertson 2006 | ◆◆◆ |
| Artefact count and standards compliance are not valid EA value metrics | VAF practitioner analysis | ◆ |

---

## References

Full bibliography in [`/research/SOURCES.md`](/research/SOURCES.md).

- Weill, P., & Ross, J.W. (2004). *IT Governance: How Top Performers Manage IT Decision Rights for Superior Results.* Harvard Business Review Press.
- Ross, J.W., Weill, P., & Robertson, D. (2006). *Enterprise Architecture as Strategy.* Harvard Business Review Press.
- McKinsey & Company. (2012). *Delivering large-scale IT projects on time, on budget, and on value.*
- Kotusev, S. (2022). *Enterprise Architecture Practice in 47 Organisations.* RMIT University.

---

*Velocity Architecture Framework™ — © 2026 Phil Myint / ZenCloud Global Consultants*
*Research Series — Paper 2 of 4*
