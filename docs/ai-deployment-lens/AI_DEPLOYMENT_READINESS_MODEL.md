# AI Deployment Readiness Model

## Status

Internal assessment model. Not yet a public certification or benchmark.

## Purpose

Assess whether an organisation is ready to move an AI use case from interest or pilot into governed operational deployment.

## Dimensions

### 1. Business Alignment

- named business owner
- clear problem statement
- measurable outcome
- defined users
- explicit non-goals

### 2. Architecture Readiness

- solution boundary defined
- enterprise dependencies understood
- integration pattern selected
- non-functional requirements captured
- architecture decision recorded

### 3. Data Readiness

- data owner identified
- classification completed
- quality assessed
- access approved
- retention and residency understood

### 4. Model and Tool Readiness

- model/tool purpose defined
- alternatives compared
- provider terms reviewed
- quality limitations understood
- cost and capacity assumptions recorded

### 5. Security and Risk Readiness

- threat and misuse scenarios considered
- identity and access model defined
- logging and monitoring planned
- regulatory and contractual obligations reviewed
- shutoff or rollback control available

### 6. Human Accountability

- output reviewer named
- approval boundary defined
- escalation path documented
- prohibited autonomous actions listed
- accountability retained by a human role

### 7. Delivery Readiness

- pilot scope defined
- success and exit criteria documented
- test approach agreed
- repository and deployment path identified
- support owner named

### 8. Operational Readiness

- monitoring metrics defined
- incident process defined
- review cadence agreed
- model/tool changes governed
- retirement criteria documented

### 9. Financial and Value Readiness

- expected cost estimated
- budget owner named
- free-tier and subscription limits known
- business value measure defined
- continue/scale/retire decision rule agreed

## Rating Scale

| Rating | Meaning |
|---|---|
| 0 | Not considered |
| 1 | Informal or incomplete |
| 2 | Defined but not validated |
| 3 | Validated for pilot |
| 4 | Controlled for production |

## Readiness Decision

- 0-12: Discovery only
- 13-23: Architecture framing required
- 24-29: Pilot may proceed with conditions
- 30-35: Deployment candidate
- 36: Fully evidenced against this draft model

The score does not replace professional judgement. Any critical data, security, legal, or accountability gap can stop deployment regardless of total score.

## Required Output

The assessment should produce:

- readiness score by dimension
- critical blockers
- assumptions
- risk treatments
- next architecture decisions
- 30/60/90-day action path
