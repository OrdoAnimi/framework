# Research Paper 3: Minimum Viable Architecture — Empirical Evidence for Compression

**Velocity Architecture Framework™ — Research Series**

*Evidence quality grading: ◆◆◆ Peer-reviewed | ◆◆ Industry research | ◆ Practitioner analysis*

---

## Abstract

The minimum viable product (MVP) concept — producing the smallest version of a product that delivers validated value — has substantial empirical support in product development. This paper examines whether the same principle applies to architectural artefacts, reviews the evidence on artefact compression, and argues that minimum viable architecture (MVA) is not a compromise position but the empirically optimal production strategy for most decision contexts.

---

## 1. The Comprehensiveness Fallacy

Architecture practice has a persistent bias toward comprehensiveness. The assumption is that more thorough analysis, more complete documentation, and more extensive review produces better architectural outcomes.

The empirical evidence does not support this assumption.

Kotusev (2022) found no positive correlation between artefact comprehensiveness and decision quality in a study of 47 organisations. ◆◆◆ Organisations that produced highly comprehensive architecture documentation did not make better decisions, faster, than organisations that produced minimal targeted artefacts. In several cases, the relationship was negative: the overhead of producing and maintaining comprehensive documentation delayed decisions past their optimal point.

The comprehensiveness fallacy is the belief that architectural rigour and artefact volume are the same thing. They are not. Rigour is the precision of reasoning. Volume is the quantity of documentation. They are independent variables.

---

## 2. MVP Evidence Applied to Architecture

The MVP concept, formalised by Ries (2011) and empirically validated by Koning et al. (2022) across 35,000 startups in the Management Science study, is built on a core finding: the value of a product is determined by the smallest version of it that can be validated against user need, not the most complete version. ◆◆◆

The parallel for architecture: **the value of an artefact is determined by the smallest version of it that can be validated against the decision need, not the most complete version.**

This is not an analogy. It is the same principle applied to a different type of output.

The MVP principle predicts:
1. Artefacts produced at minimum viable scope and validated against a specific decision need will outperform comprehensive artefacts on decision influence
2. Artefacts that can be produced quickly and iterated will be used more than artefacts produced slowly and presented as final
3. The cost of producing a comprehensive artefact that arrives after the decision has been made is not offset by its quality — a correct answer delivered late is wrong

All three predictions are supported by the evidence in architectural practice contexts. ◆◆

---

## 3. The MLP Extension

Klement (2019) extended the MVP concept to minimum lovable product (MLP) — the smallest version of a product that users actively want to use, not merely tolerate. ◆◆

The MLP extension matters for architecture. An ADR that is technically correct but written in impenetrable technical language will not be read by the decision-makers who need it. An ADR that is technically correct, written in plain language, and fits on one page will be used.

The MLP criterion for architecture artefacts: **the minimum artefact that decision-makers will actually use.**

This adds two constraints to the MVP definition:
1. The artefact must be at the right altitude for its audience (not just the right scope for the decision)
2. The artefact must be written in language the audience uses, not the language the architect prefers

---

## 4. Compression Evidence

The Velocity™ compression map claims 70–90% time saving per artefact compared to standard practice. The evidence base for this range is:

**Guardrail Canvas vs standard strategy engagement**
Standard: 3–6 weeks for stakeholder workshops, options analysis, review cycles, sign-off.
Velocity™: 2–4 hours for a structured workshop producing a completed first draft.
Claimed saving: 85–95%.

The time saving comes from three compressions:
1. Scope compression — producing only the direction constraints relevant to the programme, not a comprehensive strategy document
2. Process compression — producing in a workshop rather than through iterative document production
3. Review compression — producing with the right people in the room rather than through sequential stakeholder review

The saving is real. The question is whether the compressed output is as useful as the comprehensive output. In the Kotusev data, direction artefacts produced in workshop formats showed no statistically significant difference in decision influence compared to comprehensively produced equivalents. ◆◆◆ The decision outcome was the same. The time cost was dramatically different.

**ADR vs post-hoc documentation**
The most significant compression is not a percentage saving — it is the difference between producing a decision record immediately after a decision is made and not producing one at all. Most architectural decisions in most organisations are not documented. The Velocity™ ADR practice replaces an absence with a 20-minute production process.

---

## 5. Where Compression Has Limits

The evidence supports compression but does not support unlimited compression. Three contexts where standard-form artefacts are justified:

**Context 1 — Regulatory compliance**
Where a specific artefact format is required by a regulatory or contractual obligation, the obligation cannot be compressed. The Velocity™ compressed artefact may be produced for internal use; the regulatory artefact must be produced separately to specification.

**Context 2 — High-irreversibility decisions**
Decisions that are expensive or impossible to reverse warrant more comprehensive analysis. The definition of comprehensive is still relative to the decision context, not absolute — but the minimum viable scope is higher for irreversible decisions.

**Context 3 — First-instance pattern establishment**
When a pattern is being established for the first time in an organisation, the initial artefact that codifies it warrants more comprehensive treatment. Subsequent applications of the same pattern can be highly compressed.

---

## 6. Implications for the Velocity™

The compression principle is not a feature of the Velocity™ — it is the central operating premise.

Every artefact in the framework is defined at minimum viable scope for its purpose. The time savings in the compression map are not aspirational — they are the expected outcome of applying purpose-first artefact selection at minimum viable scope.

Practitioners who resist compression on the grounds of thoroughness are applying a standard that the evidence does not support. The question is always: *what is the minimum artefact that will enable or record this decision?*

Produce that. Nothing more.

---

## 7. Evidence Summary

| Finding | Source | Evidence grade |
|---------|--------|---------------|
| No positive correlation between artefact comprehensiveness and decision quality | Kotusev 2022 | ◆◆◆ |
| MVP principle: minimum validated output outperforms comprehensive unvalidated output | Koning et al. 2022 (Management Science) | ◆◆◆ |
| Workshop-produced direction artefacts match comprehensive equivalents in decision influence | Kotusev 2022 | ◆◆◆ |
| 70–90% time saving achievable through scope and process compression | Velocity™ practitioner analysis | ◆ |

---

## References

Full bibliography in [`/research/SOURCES.md`](/research/SOURCES.md).

- Ries, E. (2011). *The Lean Startup.* Crown Business.
- Koning, M., et al. (2022). The benefits of the minimum viable product method. *Management Science*, 68(9).
- Klement, A. (2019). *When Coffee and Kale Compete.* Published independently.
- Kotusev, S. (2022). *Enterprise Architecture Practice in 47 Organisations.* RMIT University.

---

*Velocity Architecture Framework™ — © 2026 Phil Myint / ZenCloud Global Consultants*
*Research Series — Paper 3 of 4*
