# SABSA — Security Architecture

*Part 2 · The Frameworks Explained*

Security is not an add-on to enterprise architecture. It is a dimension of every architecture decision.

Most organisations treat security as something that happens after the architecture is designed. The systems are built, the data flows are established, the integrations are wired up, and then the security team is asked to review it. This approach produces expensive rework, compliance failures, and systems that are structurally difficult to secure regardless of the controls placed on top of them.

SABSA takes a different approach. It starts with business risk, derives security requirements from that risk, and connects every security control to a specific business objective. The result is a security architecture that serves the organisation rather than one that protects the technology at the expense of the business.

Meridian handles patient data for 14,000 people across 180 sites. A community mental health patient’s record contains some of the most sensitive information a person can have. The consequences of a data breach are not just regulatory — they are human. Patients who discover their mental health history has been exposed face consequences in employment, relationships, and insurance that no financial penalty captures. For Meridian, security architecture is not a compliance exercise. It is a duty of care. SABSA gives the EA a framework for designing security around that duty rather than around a checklist.

## The SABSA matrix

SABSA uses a matrix similar in structure to Zachman. Six rows representing different perspectives on security architecture. Six columns representing the fundamental questions: What, Why, How, Who, Where, and When.

The rows move from the contextual perspective — the business context and risk — down through conceptual, logical, and physical design to the component level and finally the operational level. This layered approach ensures that security decisions made at the technical level can always be traced back to a business risk, and that business risks are always addressed by specific technical controls.

## How SABSA connects to TOGAF

SABSA and TOGAF are designed to work together. TOGAF provides the enterprise architecture development method. SABSA provides the security architecture layer within it.

In a TOGAF-led programme, SABSA contributes at specific phases. In Phase A, SABSA provides the security requirements that become architecture principles. In Phases C and D, SABSA provides the security architecture baseline alongside the application and technology baselines. In Phase E, SABSA provides the security assessment of each option. In Phase F, SABSA ensures that the migration sequence does not create security vulnerabilities in the transition states.

Meridian’s EA is not a security specialist. But she knows enough about SABSA to know when she needs one. When she maps the VMware migration options in Phase E, she applies a SABSA-informed question to each: does this transition state create a period where patient data is more exposed than it is today? Option A — lift and shift — creates a six-month period where authentication depends on both on-premises Active Directory and Entra ID simultaneously. That hybrid state is a security risk. The SABSA contextual layer question — what must be protected and why — makes that risk visible before it is built into the programme plan.

## SABSA and the security certifications

SABSA has its own certification pathway. Foundation, Practitioner, and Master levels. The certifications are rigorous and respected in the security architecture community. A CISSP — Certified Information Systems Security Professional — demonstrates broad security knowledge. A SABSA practitioner demonstrates specifically that they can design security architectures that are traceable to business requirements.

The certifications address different things. CISSP is the broader credential — it covers security domains from cryptography to physical security to legal and compliance. SABSA is the architecture-specific credential — it focuses on how security architecture is designed, not just what it contains. Many enterprise security architects hold both. A later chapter covers the full security certification landscape in detail.

## What SABSA does well and where its limits are

SABSA does one thing exceptionally well. It provides a rigorous method for tracing every security control back to a business risk and forward to a specific implementation. This traceability is invaluable in regulated environments — healthcare, financial services, government — where security architecture must be demonstrably connected to compliance requirements.

Its limits are real. SABSA is comprehensive and the full framework is dense. Most organisations do not apply the complete matrix. They apply the contextual and conceptual layers — the business risk and principles layers — and use the lower layers as a reference rather than a procedure.

SABSA also requires security architecture expertise to apply well. An enterprise architect without a security background can use SABSA principles to ask the right questions. Actually populating the SABSA matrix for a complex programme requires a security architect with specific domain knowledge.

---

## Translator Panel

> **Security architects say:** "We trace this control back to a business risk."
>
> **What that means:** The core SABSA move — every control justified by a risk it manages and a business requirement, not by a checklist. The traceability is the value, even if you never populate the full matrix.

> **People say:** "Isn't that just the security team's job?"
>
> **What that means:** SABSA's point is that security is an architecture domain, not a bolt-on. An enterprise architect without deep security expertise can still ask the SABSA question — what business risk does this control manage? — and that question alone improves most decisions.

---

## The Key Idea

SABSA is the domain framework for security architecture, and its defining contribution is traceability: every security control connected backward to a business risk and forward to a specific implementation, so security is justified by what it protects rather than by a compliance checklist. Like Zachman it is a layered model that few organisations populate in full; its everyday value is the habit of mind it instils — start from business risk, not from controls. That single discipline is usable by any architect, security specialist or not, and it is what keeps security architecture connected to the business rather than bolted on after the fact.

**Next:** Chapter 11 moves to the business layer and BIZBOK — what business architecture actually tells you.

---

## Further Reading

- **The SABSA Institute** (sabsa.org): The framework, the layered matrix, and the certification pathway from its source.
- **John Sherwood, Andrew Clark & David Lynas — Enterprise Security Architecture: A Business-Driven Approach**: The foundational SABSA text, and the clearest statement of the risk-to-control traceability idea.
- **(ISC)² — CISSP**: The broad security credential to set alongside SABSA's architecture-specific one, for understanding the wider security certification landscape.
