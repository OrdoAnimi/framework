# AI and Client Data Usage Policy

**ZenCloud Global Consultants**  
Classification: Governance — All Engagements  
Version: 1.0 — May 2026

---

## Purpose

This policy governs how AI tools and client data are used in ZenCloud advisory engagements. It applies to all practitioners operating under the Velocity Architecture Framework, including subcontractors and partner-embedded delivery resources.

All practitioners must understand and apply this policy before using AI tools in any client engagement.

---

## Core Principles

1. **No confidential client data in public AI tools**
2. **AI generates drafts — practitioners review and own the output**
3. **No automatic decisions without human validation**
4. **Client data remains client property**
5. **Velocity Framework IP is separate from client IP**

---

## Section 1: Data Classification

Before any data enters a tool or system, classify it:

| Class | Description | Examples |
|-------|-------------|---------|
| **Public** | Freely available, no restrictions | Published reports, public standards, framework documentation |
| **Internal** | Not confidential but not for public release | Client operating model descriptions, program overviews |
| **Confidential** | Sensitive business, commercial, or operational data | Revenue data, customer data, system credentials, M&A context |
| **Restricted** | Highest sensitivity — regulatory, legal, personal | PII, health data, legal privilege, board-level commercial terms |

---

## Section 2: Tool Classification

| Tool | Classification | Approved for |
|------|---------------|-------------|
| **VAF Agentic AI** | ZenCloud-operated | Internal + Confidential (per deployment configuration) |
| **Claude.ai (personal/web)** | Third-party public tool | Public data only |
| **GitHub Copilot / IDE AI** | Third-party tool | Public and Internal (no Confidential or Restricted) |
| **Microsoft Copilot (M365)** | Enterprise-configured | Per client's own M365 AI policy |
| **Generic LLM chat tools** | Third-party public tool | Public data only |

When in doubt: use Public or Internal data only, and use ZenCloud-operated tooling.

---

## Section 3: Prompt and Input Handling

### What can go into an AI prompt

**Allowed in any tool:**
- Anonymised or synthetic scenarios based on the engagement context
- Framework descriptions and method templates
- Publicly available reference material
- Generic architecture patterns and principles

**Allowed only in approved tools (VAF Agentic AI, enterprise-configured environments):**
- Internal client context (program names, operating model descriptions, general capability gaps)
- Client-supplied architecture documentation (non-confidential)

**Never allowed in any public AI tool:**
- Client names, personnel names, or identifiable organisational details
- Revenue, budget, or commercial data
- Customer or employee personal data
- Legal or regulatory-sensitive information
- System credentials, connection strings, or configuration secrets
- Board-level or commercially sensitive strategy content

### Prompt construction guidance

When using public tools for framework development, template generation, or thinking support:

- Replace client-specific terms with generic equivalents ("a large financial services firm" not "ANZ Bank")
- Replace specific figures with representative ranges ("a $50M–$200M program" not the actual budget)
- Strip identifiers before pasting any document excerpt

---

## Section 4: AI Output Handling

All AI-generated outputs are draft artefacts.

**No AI-generated output may be:**
- Delivered to a client without practitioner review
- Presented as a final recommendation without practitioner sign-off
- Used as the basis for an automated decision without human validation
- Treated as legal, financial, or regulatory advice

**Every AI-generated output delivered to a client must:**
- Have been reviewed by the practitioner responsible for the engagement
- Carry the practitioner's accountability — not the AI system's
- Be clearly within the scope of the engagement, not a hallucinated extrapolation

When reviewing AI-generated outputs, the practitioner must verify:
- Factual accuracy of all claims
- Appropriateness of any recommendations
- Consistency with engagement context and decisions already made
- Absence of confidential data from other contexts

---

## Section 5: Client Data Ownership

All data, artefacts, and outputs produced from a client engagement are client property upon delivery, unless otherwise agreed in writing.

This includes:
- Architecture Board Packs
- ADRs and Decision Registers
- Risk Registers and Assumptions Registers
- Trade-off Matrices
- Program-specific framework adaptations

ZenCloud retains:
- Generalised, anonymised patterns derived from engagement experience
- Velocity Framework methods and templates (pre-dating or independent of the client engagement)
- Tool configuration and prompt engineering developed by ZenCloud

---

## Section 6: IP Boundaries

| Asset | Owner |
|-------|-------|
| Client data provided to ZenCloud | Client |
| Engagement deliverables (upon delivery) | Client |
| Velocity Framework methods and templates | ZenCloud / Velocity |
| VAF Agentic AI configuration and prompts | ZenCloud |
| Anonymised patterns derived from engagement | ZenCloud (Velocity IP) |
| Partner-contributed methods and templates | Consultancy partner |

AI-generated content produced during an engagement does not create any IP claim for the AI provider. The AI system is a tool. The practitioner and client own the output.

---

## Section 7: Data Storage and Retention

- Engagement working data is stored in practitioner-controlled environments only
- No client engagement data is stored in public cloud services without client consent
- Engagement data is retained for the duration of the engagement plus 12 months, then deleted or returned to the client unless a longer retention is agreed
- AI conversation history containing client context is cleared at the end of each work session

---

## Section 8: Security Review Requirement

Before beginning any engagement that involves:
- Client system architecture or integration design
- AI adoption within regulated industries (financial services, healthcare, government)
- Data platform design with PII or sensitive data flows
- Cloud migration or infrastructure decisions

The practitioner must confirm:
1. The appropriate tool tier for the engagement data classification
2. That no Confidential or Restricted data will enter public AI tools
3. That the engagement AI usage is disclosed to the client at kick-off

---

## Section 9: Limitations and Disclaimers

AI tools used in Velocity engagements:
- Do not have access to real-time data unless explicitly configured
- May produce plausible-sounding but incorrect information — practitioner verification is mandatory
- Are not certified for use in safety-critical decisions
- Do not carry professional indemnity — the practitioner's professional accountability applies

ZenCloud engagement outputs:
- Are architecture advisory, not legal, financial, or regulatory advice
- Are based on information provided by the client — accuracy of that information is the client's responsibility
- Should be reviewed by the client's own subject matter experts before implementation

---

## Section 10: Enterprise Deployment Considerations

For clients seeking to deploy the Velocity tool layer within their own environment:

- VAF Agentic AI can be configured to operate within the client's Azure tenancy
- Data processing remains within the client's environment
- The AI model API calls are governed by the applicable API provider's terms (Anthropic)
- Client data does not train or improve any AI model under current Anthropic enterprise terms (verify current terms at engagement commencement)
- The client's internal AI governance policy applies alongside this policy

Enterprise deployment requires a separate technical configuration discussion with ZenCloud.

---

## Acknowledgement

All practitioners operating under ZenCloud engagements must confirm they have read and understood this policy before beginning client delivery.

This policy is reviewed and updated at each major Velocity Framework version release.

---

*ZenCloud Global Consultants — Brisbane*  
*AI and Client Data Usage Policy Version 1.0 — May 2026*
