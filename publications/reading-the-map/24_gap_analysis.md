# Chapter 24: Gap Analysis

*Part 3 · The Core Concepts*

---

Once you have an honest baseline and an agreed target, the question becomes mechanical in appearance and political in reality: what stands between them? **Gap analysis** is the discipline of answering that question — identifying, categorising, and prioritising the differences between the current state and the target state so that the architecture roadmap has something to act on.

Done well, gap analysis is the bridge between description and action. Done badly, it is a list — comprehensive, accurate, and useless, because a list of every difference between two states tells you nothing about which differences matter.

This chapter explains how gap analysis is conducted, how to read one critically, and why the most important gaps are usually not the most obvious ones.

---

## What a Gap Actually Is

A gap is not simply "something we do not have yet." A gap is a specific, named difference between the baseline and the target that requires work to close. The discipline is in the naming, because a vague gap cannot be planned, costed, or assigned.

"Our data architecture needs improvement" is not a gap. It is a feeling. "Patient identity has no authoritative master system; three systems hold conflicting patient records and there is no agreed rule for which wins" is a gap. It is specific enough to be assigned, scoped, and sequenced.

Good gaps are stated as the distance between two concrete things. *We have X. The target requires Y. The gap is the work to get from X to Y.* This framing forces precision and makes the gap actionable. It also makes the gap arguable — and that is a feature, because gaps that cannot be argued about cannot be prioritised.

---

## The Six Domains

Gap analysis is conducted domain by domain, because a gap in one domain often has consequences in another, and the domains make those consequences traceable. The conventional domains extend the BDAT model from Chapter 16 with security and governance.

**Business gaps** are differences in capability — a capability the target requires that the organisation cannot currently perform, or performs poorly. These are read directly off the capability heat map.

**Data gaps** are differences in the data architecture — missing ownership, absent master data, quality problems, entities the target requires that do not exist or are not trustworthy.

**Application gaps** are differences in the application portfolio — capabilities with no supporting system, capabilities supported by systems that must be retired, duplications the target eliminates.

**Technology gaps** are differences in infrastructure and platform — the absence of a cloud platform the target depends on, end-of-life hardware, capacity or resilience shortfalls.

**Security gaps** are differences in the security architecture — controls the target requires that do not exist, risks the current state carries that the target must not.

**Governance gaps** are differences in the decision-making machinery itself — the absence of an Architecture Review Board, the lack of a portfolio governance process, the missing mechanism to enforce the principles.

The governance domain is the one most often omitted, and its omission is telling. An organisation that analyses gaps in five domains but not in its own decision-making is assuming the decision-making works — which is frequently the largest gap of all.

---

## Categorising and Prioritising

A raw gap list is overwhelming. The work that makes it useful is categorisation and prioritisation.

Categorisation sorts gaps by type and by the kind of response they require. Some gaps are closed by **building** something new. Some by **buying** a capability. Some by **retiring** something. Some by **changing a process** rather than a system. Some by **establishing governance** rather than technology. Sorting gaps by response type reveals that not every gap is a project — a fact that surprises organisations conditioned to treat every problem as a procurement.

Prioritisation ranks gaps by two dimensions that should be assessed separately: **impact** (how much does closing this gap matter to the target?) and **dependency** (what else depends on this gap being closed first?). A gap can be low-impact in itself but high-priority because everything else depends on it. The classic example is the cloud platform: building it is not, by itself, a business outcome, but nothing else in the roadmap can happen until it exists.

This is why the most important gaps are rarely the most obvious. The obvious gaps are the visible business problems — the failing system, the manual workaround, the capability everyone complains about. The important gaps are often the unglamorous enablers underneath them, the dependencies that have to close first before any of the visible problems can be addressed.

---

## Meridian's Gap Analysis

*Meridian's EA conducts the gap analysis across all six domains, and the result reorders the leadership team's intuitions about what matters.*

*The obvious gaps are the ones everyone already knew. The dual EPR is a glaring application gap. The aging infrastructure is a glaring technology gap. The complaints about reporting are a visible data gap. These are real, and they are what the executive team would have listed if asked.*

*The gap analysis surfaces three less obvious gaps that turn out to be more important.*

*The first is a governance gap: there is no body with the authority to enforce an architecture decision across the estate. Every previous attempt at rationalisation had failed not for want of a correct answer but for want of a mechanism to make the answer stick. Until this gap is closed, closing any other gap is provisional — a decision any project can quietly ignore. The EA categorises it as the highest-priority gap not because it is the most visible but because every other gap depends on it.*

*The second is a data gap underneath the EPR gap: patient identity has no master. The leadership team had framed the dual EPR as the problem to solve. The gap analysis shows that consolidating to a single EPR without first resolving which system holds the authoritative patient record would simply move the identity problem into the new system. The identity gap has to close before the EPR gap can close cleanly — a sequencing insight the raw problem list did not reveal.*

*The third is a technology gap that is also an enabler: there is no cloud platform. This is not a business outcome anyone cares about directly. But the VMware exit, the EPR consolidation, and the integration modernisation all depend on a landing platform that does not yet exist. It is low-glamour and high-dependency — the kind of gap that gets deprioritised in favour of visible problems and then blocks everything.*

*The EA's prioritised gap list therefore leads with governance, identity, and platform — three gaps that no stakeholder had named as priorities, because all three are enablers rather than outcomes. The visible problems everyone cared about sit behind them in the sequence, not because they matter less but because they cannot be solved until the enablers are in place.*

---

## How to Read a Gap Analysis

When a gap analysis appears in a meeting — and it will, usually as a table or a heat-mapped grid — there are a few questions that tell you whether it is actionable or academic.

Ask whether each gap is stated as a specific difference between two concrete states, or as a vague aspiration. Vague gaps signal an analysis that has not done its work.

Ask whether the governance domain is present. Its absence usually means the analysis has assumed the decision-making works.

Ask how gaps were prioritised, and specifically whether dependency was assessed separately from impact. An analysis that ranks gaps purely by business impact will systematically under-prioritise the enablers, and a roadmap built on it will stall when it hits the dependency it skipped.

Ask which gaps are *not* projects. An analysis in which every gap requires a procurement is an analysis that has mistaken its only tool for the whole toolbox.

---

## Translator Panel

> **TOGAF says:** "Gap analysis is a technique used to validate an architecture by identifying the differences between the Baseline and Target Architectures, including gaps that should be addressed and gaps that were unintentionally introduced."
>
> **What that means:** List the differences between what you have and what you want, in a disciplined way, so the roadmap has something concrete to act on. The reference to "unintentionally introduced" gaps is a useful warning: a target architecture can accidentally drop a capability the current state quietly relied on. Gap analysis catches that.

> **Delivery teams say:** "We know what the gaps are, we don't need a formal analysis."
>
> **What that means:** They usually know the visible gaps — the ones that cause daily pain. The formal analysis exists to surface the dependency gaps and the governance gaps that are not visible from inside the daily work, and to order them so the roadmap does not stall on a missing enabler.

---

## The Key Idea

Gap analysis is the bridge between description and action: a disciplined account of the specific, named differences between the baseline and the target, categorised by the kind of response they require and prioritised by impact and dependency assessed separately. Its central insight is that the most important gaps are rarely the most obvious. The visible gaps are the business problems everyone already complains about; the important gaps are often the unglamorous enablers underneath them — the governance mechanism, the master-data resolution, the platform — that have to close first. A gap analysis that ranks purely by visible impact will under-prioritise exactly the gaps the roadmap depends on, and the roadmap built on it will stall the moment it reaches one.

**Next:** Chapter 25 turns the prioritised gaps into a sequence — the architecture roadmap — and explains how it differs from a project plan and what the order of the work actually tells you.

---

## Further Reading

- **The Open Group — TOGAF Standard: Phase E and the Gap Analysis technique** (opengroup.org): The formal description of the technique and its place in the ADM. The gap matrix format described there is the one most likely to appear in practice.
- **Donella Meadows — Thinking in Systems** (Chelsea Green, 2008): Meadows's account of leverage points — where a small intervention produces large change — is the conceptual foundation for distinguishing high-dependency enabling gaps from high-visibility outcome gaps.
- **Gartner — IT Score for Enterprise Architecture**: A maturity instrument that, used as a gap-analysis lens, helps surface the governance and capability gaps that domain-by-domain technical analysis tends to miss.
