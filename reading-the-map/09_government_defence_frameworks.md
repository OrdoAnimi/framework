# Government and Defence Frameworks

Not every organisation uses TOGAF. Government and defence organisations often have their own frameworks, mandated by regulation, procurement rules, or interoperability requirements.

If you work in or with government or defence you will encounter these frameworks by name and sometimes by requirement. If you do not, this chapter gives you enough to recognise them, understand why they exist, and navigate a conversation where they come up.

## Why government and defence needed their own frameworks

Government and defence organisations share three characteristics that make generic EA frameworks insufficient on their own.

The first is interoperability at scale. A defence system built by one contractor must be able to communicate with systems built by a dozen other contractors across multiple nations, sometimes in real-time, under operational conditions. The margin for integration failure is not a project delay. It is operational failure. Standard commercial EA frameworks were not designed with this constraint.

The second is procurement governance. Government procurement rules require that architecture descriptions meet specific standards before contracts are awarded. A supplier cannot simply produce a diagram in their preferred format. They must produce architecture artefacts that conform to the mandated framework so that government evaluators can compare them consistently.

The third is long-term programme management. Government programmes often run for ten to twenty years. The architecture frameworks that govern them must support continuity across changes in government, changes in contractors, and changes in technology. TOGAF's ADM can support this but government frameworks add the specific views and artefacts that long-running multi-contractor programmes need.

## FEAF — the US Federal Enterprise Architecture Framework

FEAF — the Federal Enterprise Architecture Framework — was published by the US federal government in 1999. It provides a common approach for US government agencies to develop enterprise architectures that support the integration of federal IT investments.

FEAF organises architecture around five reference models: Performance, Business, Data, Application, and Infrastructure. These map closely to BDAT with the addition of a Performance layer that explicitly connects architecture to government mission outcomes and budget accountability.

FEAF is used by US federal agencies and by contractors and consultants who work with them. If you are working on US government IT programmes you will encounter FEAF requirements in contract specifications and architecture review processes.

## DODAF — the US Department of Defense Architecture Framework

DODAF was published in 2003 and has been through several major versions since. It provides a standardised way of describing defence architectures so that systems built by different contractors can be evaluated, compared, and integrated.

DODAF organises architecture into viewpoints — specific perspectives that address specific concerns. The Operational Viewpoint describes how an operation works independently of the systems that support it. The Systems Viewpoint describes the systems. The Technical Standards Viewpoint defines the standards systems must conform to. Together these viewpoints give programme managers, contractors, and evaluators a common way of understanding and comparing architectures.

DODAF is mandatory for US defence programmes above a certain value threshold. If you work for a defence contractor, a systems integrator working with defence, or a consultancy with defence clients, you will encounter DODAF requirements directly.

## MODAF and NAF — UK and NATO equivalents

MODAF — the UK Ministry of Defence Architecture Framework — was developed as a UK equivalent to DODAF, adapted for UK procurement and programme management requirements. It shares DODAF’s viewpoint approach but reflects UK MoD governance structures and procurement rules.

NAF — the NATO Architecture Framework — was developed to support NATO’s multinational interoperability requirements. Where DODAF governs US systems and MODAF governs UK systems, NAF governs systems that must work together across NATO member nations. NAF has been progressively aligned with ArchiMate notation to improve readability and tool support.

Meridian is an NHS organisation, not a defence contractor. The EA will never directly use FEAF, DODAF, MODAF, or NAF. But she will encounter colleagues who have come from government or defence backgrounds who use vocabulary from these frameworks without realising not everyone shares it. Knowing what the frameworks are — and why they exist — makes those conversations easier and prevents the false assumption that everyone in the room is using the same mental model.
