# Research Paper 4: Architecture Value Over Time — The Decay Problem

**The OrdoAnimi Framework — Research Series**

*Evidence quality grading: ◆◆◆ Peer-reviewed | ◆◆ Industry research | ◆ Practitioner analysis*

---

## Abstract

Architecture artefacts decay. A decision record that was accurate when produced becomes misleading when the system it describes has changed and the record has not been updated. This paper examines the decay problem in EA documentation, reviews evidence on decay rates and their costs, and proposes the OrdoAnimi aging and expiry model as a systematic response. The central argument is that an outdated artefact is not merely useless — it is actively harmful, because it creates false confidence in a state that no longer exists.

---

## 1. The Decay Problem

Architecture documentation decays from the moment it is produced.

This is not a quality problem. It is a temporal problem. The world changes; the documentation does not. The rate at which a document becomes misleading depends on the rate of change of the system or domain it describes.

Three types of decay:

**Factual decay:** The document describes a state that has changed. The system it describes has been modified, replaced, or decommissioned.

**Contextual decay:** The reasoning in the document was sound at the time, but the context has changed in ways that would have changed the decision. The document is factually accurate but contextually obsolete.

**Relevance decay:** The decision the document was produced to support has been made, superseded, or abandoned. The document remains in the repository but has no current decision context.

All three types are present in most EA repositories. Most EA repositories do not distinguish between current, aged, and expired documents. The result is a repository that cannot be trusted — practitioners do not know which documents are reliable without independently verifying the state they describe.

---

## 2. The Cost of Outdated Documentation

The cost of an outdated architecture document is not zero. It is negative.

A practitioner who consults an outdated document and acts on it will:
1. Make a decision based on a false state of the system
2. Experience the cost of that decision when the discrepancy is discovered
3. Lose confidence in the architecture repository as a reliable source

The third cost compounds. An organisation where practitioners have learned not to trust the architecture repository has effectively dismantled its architectural governance regardless of what the repository contains.

CB Insights (2024) found that 43% of VC-backed startup failures traced to poor product-market fit — a category that includes building on false assumptions about the current state of the market or system. ◆◆ The parallel in enterprise architecture: decisions made on the basis of documentation that does not reflect the current state of the system are decisions made on false assumptions.

The cost is not theoretical. Most practitioners have experienced a project that discovered, mid-delivery, that the architecture document it was building on described a state that no longer existed.

---

## 3. Decay Rates by Artefact Type

Not all artefacts decay at the same rate. The OrdoAnimi aging model is built on empirical observation of decay rates across artefact types. ◆

**High decay rate (review cycle: monthly or shorter)**
- Velocity Dashboard
- Pulse Briefing
- Risk Register
- Escalation Register

These artefacts describe current operational state and decay rapidly. A Velocity Dashboard that is 90 days old is not architecture — it is history.

**Medium decay rate (review cycle: quarterly)**
- Technology Radar
- Dependency Map
- ADR (active decisions under implementation)
- Fitness Function Register

These artefacts describe state that changes on a programme or delivery cadence. Quarterly review is the minimum viable maintenance cadence.

**Low decay rate (review cycle: annually or on trigger)**
- ADR (accepted, fully implemented decisions)
- Guardrail Canvas (stable programmes)
- Pattern Catalogue
- Domain Model

These artefacts describe stable architectural commitments. They decay when the underlying system or strategic context changes, not on a calendar schedule. Review is triggered by change events, not time.

**Permanent record (no decay — expires only on explicit supersession)**
- Handover Record
- Historical ADRs (status: Superseded or Deprecated)

These artefacts are historical records. They are accurate descriptions of past state and do not decay. They should never be deleted — only marked as superseded.

---

## 4. The Expiry Model

The OrdoAnimi introduces explicit expiry for architecture artefacts — a defined date after which an artefact is treated as expired and requires review before being relied upon.

Expiry is not the same as deletion. An expired artefact remains in the repository, marked as expired. It may still be accurate. Expiry is a signal that the artefact has not been reviewed within its defined cycle and cannot be relied upon without verification.

The expiry model serves three functions:

**Function 1 — Trust calibration**
Practitioners can distinguish between current (reviewed within cycle), aged (approaching expiry), and expired (not reviewed within cycle) artefacts. They know what they can rely on and what requires verification.

**Function 2 — Maintenance forcing**
Expiry creates an obligation to review. Without explicit expiry, documents accumulate without review because there is no forcing function. With expiry, the review cycle is embedded in the artefact itself.

**Function 3 — Repository health metric**
The percentage of active artefacts that are current vs aged vs expired is a direct measure of architecture repository health. A repository where 40% of active artefacts are expired is a repository that practitioners will not trust.

---

## 5. The Velocity of Truth

The OrdoAnimi's governing principle — *velocity is the rate at which ambiguity expires* — has a corollary: **an artefact that does not expire is not architecture. It is decoration.**

An architecture artefact that is treated as permanent, never reviewed, never updated, and never expired has abandoned its function. It is no longer a record of the current state of architectural commitments. It is a historical document being used as a current document — the most dangerous possible condition for organisational decision-making.

The Velocity of Truth concept holds that architectural truth is not a fixed state but a rate. The truth of a system description is valid for a period, after which it must be revalidated. The period varies by artefact type. The obligation to revalidate does not.

---

## 6. Implications for Repository Governance

Three governance practices follow from the decay model.

**Practice 1 — Every artefact has an expiry date**
Set at creation. Based on artefact type decay rate. Displayed prominently in the document header.

**Practice 2 — Expiry triggers review, not deletion**
An expired artefact is reviewed. If still accurate, the expiry date is extended. If no longer accurate, it is updated. If superseded, it is marked as such and retained as a historical record.

**Practice 3 — Repository health is a governance metric**
The percentage of active artefacts that are current is reported in the Pulse Briefing. Below 70% current: repository is unreliable. Below 50% current: repository is harmful.

---

## 7. The Longitudinal Study Gap

This paper notes an important gap in the evidence base.

There is no published longitudinal study of EA artefact decay rates at the artefact level across a significant sample of organisations. The decay rates cited in this paper are based on practitioner observation and inference from related empirical work.

This gap is named explicitly rather than papered over with false confidence. The decay model is well-reasoned and consistent with available evidence. It is not empirically validated at the level of rigour that Kotusev's cross-organisational studies provide for other findings in this research series.

The absence of this study is itself a finding. EA research has focused heavily on artefact production and under-studied artefact maintenance and decay. This is a significant gap in the evidence base.

---

## 8. Evidence Summary

| Finding | Source | Evidence grade |
|---------|--------|---------------|
| Outdated documentation creates negative value through false confidence | OrdoAnimi practitioner analysis | ◆ |
| 43% of VC-backed failures traced to decisions on false assumptions | CB Insights 2024 | ◆◆ |
| Repository trust loss compounds once practitioners learn not to rely on it | OrdoAnimi practitioner analysis | ◆ |
| Artefact-level longitudinal decay study does not exist | Literature review | ◆ (gap noted) |

---

## References

Full bibliography in [`/research/SOURCES.md`](/research/SOURCES.md).

- CB Insights. (2024). *The Top Reasons Startups Fail.*
- Kotusev, S. (2022). *Enterprise Architecture Practice in 47 Organisations.* RMIT University.
- Ross, J.W., Weill, P., & Robertson, D. (2006). *Enterprise Architecture as Strategy.* Harvard Business Review Press.

---

*The OrdoAnimi Framework — © 2026 Phil Myint / OrdoAnimi*
*Research Series — Paper 4 of 4*
