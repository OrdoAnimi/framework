# Appendix B — Framework Comparison Table

*Reading the Map · Reference*

---

The frameworks and adjacent disciplines covered in the book, side by side. Use this to place any framework in context — what kind of thing it is, what it is for, and where its limits are. The frameworks are not competitors; they occupy different categories (see Chapter 21). The "type" column names the category.

---

## The Frameworks at a Glance

| Framework | Type | Origin | Primary purpose | Best used for | Known limitation |
|---|---|---|---|---|---|
| **Zachman** | Classification | John Zachman, IBM, 1987 | Classify the kinds of description an enterprise needs | Checking completeness; resolving "we're talking past each other" | Describes, does not tell you how to build; ceremonial if all 36 cells are populated |
| **TOGAF** | Method | The Open Group, 1995 | A repeatable method (the ADM) for developing architecture | A shared vocabulary and defensible sequence | Heavy if run in full; designed for large enterprises, not small fast ones |
| **ADM** | Method (within TOGAF) | The Open Group | The phase cycle: vision → domains → roadmap → governance | Structuring the thinking, selectively | Becomes ritual if every phase is performed regardless of need |
| **ArchiMate** | Notation | The Open Group, 2009 | A standard visual language across business, app, technology | Diagrams others can read; the vertical trace | Dense views become unreadable; needs the single-thread reading technique |
| **SABSA** | Domain (security) | Sherwood et al., 1990s | Trace security controls to business risk | Security architecture connected to business risk | Often absent; can be heavyweight for small organisations |
| **BIZBOK** | Domain (business) | Business Architecture Guild | Business architecture practice, incl. capability mapping | Capability maps, value streams, business-layer depth | Abstract; value depends on connecting it to real decisions |
| **SAP EA Framework** | Domain (vendor) | SAP | Architecture aligned to the SAP landscape | Organisations with a large SAP estate | Naturally centred on SAP's own technology |
| **Wardley Mapping** | Strategy / evolution | Simon Wardley, 2005 | Reason about evolution and what to build vs. buy | Strategic positioning; build/buy/commodity decisions | Subjective placement; takes practice to read and draw well |
| **ITIL** | Operating / service mgmt | UK Government (CCTA), 1989 | Manage IT services in operation | Running what architecture builds; incident/change | Downstream of architecture; can ossify into process for its own sake |
| **COBIT** | Governance | ISACA, 1996 | Govern the enterprise's use of IT | Control environment; audit alignment | Control-heavy; often invoked only at audit time |
| **Government/Defence (FEAF, DODAF, MODAF, NAF)** | Method/reference (sector) | US/UK governments, 1990s–2000s | Architecture for government and defence estates | Public-sector and defence contexts | Mandated detail can be disproportionate outside those sectors |

---

## How to Read This Table

**Match the category to the question.** The "type" column is the most useful. A strategy question reaches for Wardley; a method question for the ADM; a classification question for Zachman; a governance question for COBIT. Asking "which framework?" without first asking "which category of question?" is the category error of Chapter 21.

**No framework does everything.** Each is strong within its category and silent outside it. TOGAF gives you a method but not a notation; ArchiMate gives you a notation but not a method; Zachman gives you a taxonomy but neither. A working practice combines several.

**The limitation column matters as much as the purpose column.** Every framework has a characteristic failure mode — usually ceremony, heaviness, or being applied outside the context it was designed for. Knowing the limitation is knowing when *not* to reach for the framework.

**Certification ≠ capability.** Several of these frameworks have certification programmes (TOGAF and SABSA most prominently). A certificate demonstrates familiarity with the framework, not the ability to use it well in a real organisation — which is the skill this book argues actually matters.

---

## Certification Pathways (where they exist)

| Framework | Certification | Entry point |
|---|---|---|
| TOGAF | TOGAF Foundation, then Practitioner (The Open Group) | Self-study or accredited training; widely available |
| ArchiMate | ArchiMate 3 Foundation/Practitioner (The Open Group) | Often taken alongside TOGAF |
| SABSA | SABSA Foundation (SCF), then advanced (SABSA Institute) | Accredited training |
| ITIL | ITIL 4 Foundation, then specialist modules (PeopleCert/Axelos) | Foundation is the common entry point |
| COBIT | COBIT Foundation, then Design & Implementation (ISACA) | Often pursued by audit and governance professionals |
| BIZBOK | Certified Business Architect — CBA (Business Architecture Guild) | Guild membership and exam |

*Zachman, Wardley Mapping, and the government/defence frameworks are studied through their published material and communities rather than a single dominant certification — see Appendix E for the professional landscape.*

---

## The Honest Summary

If you take one thing from this table: the frameworks are a toolkit, not a shelf of competing products. The mature practitioner uses several — a method, a notation, domain depth where needed, a strategy lens, and a governance frame — selecting each for the question in front of them and resisting the pull to perform any of them ceremonially. The frameworks are a map (Chapter 54). This table is a guide to which map to unfold for which journey.
