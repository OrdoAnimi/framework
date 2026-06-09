# Chapter 27: Application Portfolio and the 6Rs

*Part 3 · The Core Concepts*

---

Chapter 20 introduced the application portfolio — the structured catalogue of what is in the estate, assessed and mapped to capabilities. It ended with a matrix that sorted Meridian's 94 applications into four quadrants: invest, migrate, rationalise, eliminate. That matrix is a diagnosis. This chapter is about the prescription — the decision framework that turns "this application is in the migrate quadrant" into "and therefore we are going to do *this specific thing* with it."

The framework is the **6R model**: a set of six dispositions, each of which is a concrete decision about an application's future. Retire, retain, rehost, replatform, repurchase, refactor. Every application in the estate gets exactly one R, and assigning it forces the organisation to convert assessment into commitment.

This chapter explains each of the six, how they map to the portfolio matrix, and what Meridian's 6R breakdown reveals that the four-quadrant matrix alone did not.

---

## Why Most Organisations Have No Portfolio

Before the 6Rs, a blunt observation worth restating: most organisations do not have an application portfolio at all. They have a licence register, a helpdesk asset list, and a collective folk memory of what runs where. These are not portfolios. A portfolio is an *assessed* catalogue — each application evaluated against consistent criteria and mapped to the capabilities it supports.

The absence is not laziness. Building a portfolio surfaces uncomfortable facts: shadow IT nobody approved, zombie systems nobody owns, duplications nobody consolidated. The portfolio is the instrument that makes the architecture debt of the application layer visible, and visibility creates obligation. An organisation without a portfolio can plausibly claim not to know. An organisation with one cannot.

The 6R model is what makes the portfolio actionable rather than merely revealing. It is the bridge from "now we can see the estate" to "now we have decided what to do about it."

---

## The Six Dispositions

Each R is a different answer to the question "what is this application's future?"

**Retire.** Decommission it. The application delivers no proportionate value — it is redundant, unused, or superseded. Retiring it removes cost, removes risk, and shrinks the surface area the estate has to maintain. This is the disposition for the eliminate quadrant, and it is the one most often identified and least often executed, because every retirement has a constituency that would rather defer.

**Retain.** Leave it as it is, for now. The application works, it is fit for purpose, and there is no compelling reason to change it. Retain is a legitimate decision, but it must be an active one — "we have assessed this and chosen to keep it unchanged" — not the default that applies to everything nobody got around to assessing. Passive retention is how estates ossify.

**Rehost.** Move it, unchanged, to new infrastructure. The classic "lift and shift" — take the application as it is and run it somewhere else, typically cloud. Rehosting is fast and low-risk because the application itself does not change. It is also the disposition that carries the most debt forward: a badly architected application rehosted to cloud is a badly architected application with a cloud bill.

**Replatform.** Move it with modest changes that take advantage of the new environment — swapping a self-managed database for a managed one, say, without rewriting the application. Replatforming sits between the speed of rehosting and the cost of refactoring. It captures some of the new platform's benefits without the full expense of a rewrite.

**Repurchase.** Replace it with a different product — typically moving from a self-hosted or bespoke application to a commercial SaaS equivalent. Repurchasing eliminates the application and its maintenance burden entirely, at the cost of migrating data and adapting to someone else's product. It is the right answer when the capability is a commodity that the organisation has no reason to run itself.

**Refactor.** Re-architect it significantly — rewrite, restructure, or rebuild to remove its accumulated debt and fit it to the target architecture. Refactoring is the most expensive and most disruptive disposition, justified only where the application supports a strategically important capability and no commercial alternative fits.

The six form a rough spectrum of cost and change. Retire and retain change nothing. Rehost and replatform change the surroundings. Repurchase and refactor change the application itself. The skill is matching the disposition to the application's value, its debt, and the organisation's appetite — not defaulting every system to the same R.

---

## How the 6Rs Map to the Matrix

The four-quadrant matrix from Chapter 20 and the 6R model are complementary. The matrix tells you *which applications need a decision*. The 6Rs tell you *what the decision is*.

The eliminate quadrant — low value, low quality — maps almost entirely to **retire**. These applications should leave the estate.

The rationalise quadrant — low value, high quality — maps to **retire** or **repurchase**. The application is technically fine but not earning its place; either remove it or replace it with something cheaper to own.

The invest quadrant — high value, high quality — maps to **retain** or **refactor**. These applications matter and work; keep them as they are, or invest further if the target architecture demands it.

The migrate quadrant — high value, low quality — is where the interesting decisions live, and where all four of the "change" Rs come into play. The application matters but is technically at risk, and the question is *how* to address the risk. Rehost for speed. Replatform for moderate benefit. Repurchase if a commercial alternative now exists. Refactor if the capability is strategic and bespoke. The migrate quadrant is a single diagnosis with four possible prescriptions, and choosing among them is the heart of portfolio decision-making.

---

## Meridian's 6R Breakdown

*When Meridian's EA assigns a disposition to each of the 94 applications, the breakdown surprises the leadership team — not because the numbers are dramatic, but because they expose how much of the estate had been carried forward by default.*

*Twenty-three applications are assigned **retire**. These are the eliminate-quadrant systems from Chapter 20 — the zombies, the end-of-life hardware systems, the application whose owner had assumed IT had switched it off eighteen months ago. The surprise is not that they exist but that retiring them is harder than expected: nine of the twenty-three have at least one integration dependency, so even a system with no users cannot simply be switched off without checking what still quietly reads from it.*

*Eighteen applications are assigned **retain** — chiefly the core clinical systems that are working well. The EA insists this be recorded as an active decision with a review date, not a permanent exemption, precisely to prevent the passive retention that created the estate's problems in the first place.*

*Thirty-one applications fall in the migrate quadrant, and the EA's distribution across the change-Rs is where the strategy shows. Most are assigned **rehost** in the near term — moved to the cloud platform unchanged — not because rehosting is ideal but because the VMware deadline does not allow time to refactor everything first. The EA is explicit that several of these rehosts carry debt forward and will need a second disposition later. A smaller set is assigned **replatform** where a managed service offers an easy win. Two are assigned **repurchase** — including one of the two duplicate clinical tools, which a commercial SaaS product can now replace, allowing the £180,000-a-year duplication to be collapsed. Only a handful are assigned **refactor**, reserved for strategically important systems with no commercial alternative.*

*The deepest insight is one the four-quadrant matrix could not show. The dual EPR cannot be resolved by a single R. One EPR will eventually be **retired** and its capability **consolidated** into the other, but only after the patient-identity master is established (Wave 3 of the roadmap). The disposition of the most important application decision in the organisation is therefore not a disposition at all yet — it is a dependency on a data decision that has to come first. The 6R exercise makes that dependency unavoidable to see: you cannot assign an R to the second EPR until you have resolved identity, and pretending otherwise would be assigning a disposition the architecture cannot yet support.*

---

## Translator Panel

> **Cloud vendors say:** "We'll help you migrate using the 6Rs — most of your estate can be rehosted quickly."
>
> **What that means:** Rehosting is the vendor-friendly disposition because it is fast, low-risk, and gets workloads onto the platform with minimal change. It is often the right near-term move under deadline pressure. But a portfolio rehosted wholesale carries its architecture debt onto the new platform intact, and "most can be rehosted" should always prompt the follow-up: *and then what — what is the second disposition for the ones we rehosted to buy time?*

> **Architects say:** "We need to assign a disposition to every application before we sequence the migration."
>
> **What that means:** No application should move without a decision about its future. Migrating without dispositions is just relocating the existing mess. The 6R assignment is what turns a migration from a relocation into a rationalisation.

---

## The Key Idea

The application portfolio is the diagnosis; the 6R model is the prescription. Retire, retain, rehost, replatform, repurchase, refactor — every application gets exactly one, and assigning it converts assessment into commitment. The four "change" dispositions form a spectrum of cost and disruption, and matching the right one to each application's value and debt is the heart of portfolio decision-making. The model's deeper value is what it forces into the open: that retirement is harder than it looks because of hidden dependencies, that retention must be active rather than passive, that rehosting under deadline pressure carries debt forward and demands a later second disposition, and that some dispositions cannot be assigned at all until a prior data or governance decision is made. The 6Rs do not just tell you what to do with the estate; they reveal what you cannot yet decide, and why.

**Next:** Chapter 28 turns to the mechanism that makes portfolio decisions — and every other architecture decision — actually stick: architecture governance, and what an Architecture Review Board looks like in operation rather than on paper.

---

## Further Reading

- **AWS — "6 Strategies for Migrating Applications to the Cloud"** (aws.amazon.com): The widely cited articulation of the 6Rs in a migration context. Read it for the definitions, but read it critically — its centre of gravity is naturally the rehost-and-replatform path that suits a cloud vendor.
- **Gartner — TIME Model (Tolerate, Invest, Migrate, Eliminate)**: The portfolio-categorisation counterpart to the 6Rs; the matrix in Chapter 20 is a variant of it. Useful for the assessment step that precedes disposition.
- **Michael Nygard — Release It!** (Pragmatic Bookshelf, 2nd ed. 2018): Essential background on why some applications resist rehosting — the stability and dependency patterns that determine whether "lift and shift" is actually safe.
