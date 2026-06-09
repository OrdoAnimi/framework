# Chapter 1 — A Short Honest History

Every discipline has an origin story. Enterprise Architecture has several, depending on who is telling it. The official version tends to start with a framework. The honest version starts with a problem.

The problem was scale.

By the mid-1980s, large organisations — banks, governments, defence agencies, insurance companies — had been building technology systems for two decades. Each system had been built to solve a specific problem at a specific moment. A payroll system here. A customer database there. A claims processing platform. A financial reporting tool. Each one built by a different team, often using different technology, rarely designed to connect to anything else.

By itself, each system worked. Together, they were becoming unmanageable.

Data lived in multiple places and said different things. Changing one system broke something in another. New requirements cost ten times more than they should have because nobody had mapped the dependencies. The same information was being maintained in four different places by four different teams who did not know about each other.

The problem was not that the technology was bad. The problem was that nobody had a picture of the whole.

## 1987 — The Zachman Framework

In 1987, John Zachman, working at IBM, published a paper in the IBM Systems Journal titled A Framework for Information Systems Architecture. It was not a methodology. It was not a process. It was a classification system — a way of organising the different descriptions of an enterprise so that nothing was missed and nothing was confused with something else.

Zachman observed that complex objects — aeroplanes, buildings, industrial machines — required multiple different kinds of descriptions to be understood fully. An architect's drawing of a building is not the same as an electrical engineer's schematic. Both describe the same building. Neither one is complete by itself. Both are necessary. And neither one substitutes for the other.

He applied the same logic to information systems. A complete description of an enterprise required multiple perspectives — the owner's perspective, the designer's perspective, the builder's perspective, the user's perspective. And it required multiple interrogatives — what the system does, how it does it, where it runs, who operates it, when things happen, and why they exist.

The result was a six-by-six matrix. Six rows representing six perspectives on the enterprise. Six columns representing six interrogatives. Thirty-six cells, each representing a distinct type of architecture description.

Zachman's paper did not immediately change the industry. It planted a seed. It gave the emerging discipline of enterprise architecture a structural foundation that said: describing a complex organisation requires multiple types of description, and confusing one type with another is the source of much avoidable complexity.

That insight is still true. Thirty-nine years later, most architecture problems can be traced back to someone treating one type of description as if it were another. Treating a technical blueprint as if it were a business strategy. Treating a system diagram as if it were an application portfolio. Treating a governance model as if it were a delivery plan.

Zachman gave the profession its first taxonomy. Every framework that came after built on the same basic recognition: to understand an enterprise you need more than one perspective, and knowing which perspective you are using at any given moment matters.

## 1995 — TOGAF arrives

The Open Group Architecture Framework — TOGAF — was first published in 1995. It was derived from the United States Department of Defense Technical Architecture Framework for Information Management, known as TAFIM. The US government had developed TAFIM to address the same scale problem Zachman had identified — large, complex technology estates that needed a structured approach to development and governance.

The Open Group, a technology industry consortium, took TAFIM as a starting point and developed it into a methodology that any large organisation could apply. Where Zachman had given the profession a classification system, TOGAF gave it a process. The Architecture Development Method — the ADM — provided a cycle of phases for developing enterprise architectures from initial vision through to ongoing governance.

TOGAF was not prescriptive about what the architecture should look like. It was prescriptive about how to develop it. That distinction matters. TOGAF does not tell you to use Azure or AWS. It does not tell you to buy SAP or Oracle. It gives you a structured way of thinking through the decision.

TOGAF grew. Version by version, it expanded. New sections were added. The content framework grew more detailed. The certification programme was introduced. By the 2000s, TOGAF had become the most widely used enterprise architecture framework in the world. Today it is estimated that over one hundred thousand architects hold TOGAF certifications globally.

That reach has been both its strength and its challenge. Its strength because it gave the profession a common vocabulary. Its challenge because a framework designed for large defence and government enterprises does not always translate cleanly to a fifty-person technology company or a fast-moving digital organisation. TOGAF applied ceremonially — run in full regardless of whether each phase is warranted — produces more process than value. Applied selectively, as a thinking structure rather than a procedure, it remains genuinely useful.

## The 2000s — the consulting boom

The 2000s saw enterprise architecture become a commercial proposition. The major consulting firms built EA practices. A new generation of practitioners was certified. Architecture frameworks multiplied. FEAF was published for the US federal government. DODAF for defence. MODAF for the UK Ministry of Defence. SABSA for security architecture. The Business Architecture Guild published BIZBOK for business architecture. SAP developed its own EA framework aligned to its technology landscape.

The era produced genuine progress. The profession developed shared language. Modelling standards emerged. The Open Group published ArchiMate, a visual notation standard that gave architects a common way to draw enterprise architecture diagrams. Tools were built. Methods were refined.

It also produced something less useful. As EA became a profession with certifications and career paths, it accumulated the behaviours of any professionalising discipline. Credentials became a filter. Jargon became a signal of belonging. Governance processes were sometimes designed more to demonstrate the function's value than to produce decisions that helped organisations move. The frameworks themselves grew dense and self-referential.

A pattern appeared in research and in practice. EA functions that focused on documentation, compliance, and process often struggled to demonstrate business impact. EA functions that stayed close to real decisions, real programmes, and real business problems tended to produce outcomes their organisations valued.

## The 2010s — the maturity question

By the 2010s, the profession had matured enough to ask itself hard questions. Research consistently showed mixed results from enterprise architecture programmes. Some organisations pointed to EA as a source of genuine strategic value. Others had invested significantly and struggled to articulate what they had received in return.

Serious practitioners began to name the failure modes. Architecture Theatre was the term that emerged for governance processes that looked rigorous but did not produce binding decisions. Decision latency — the gap between when a question became visible and when it was answered — was identified as a primary cause of organisational dysfunction that architecture was supposed to address but sometimes made worse.

Thinkers like Niek de Visscher argued that EA had drifted toward control and away from connection. The discipline at its best, he argued, connected strategy to execution, ambition to reality, today's decisions to tomorrow's outcomes. Where it went wrong, it substituted documentation for those connections.

Vince Dooher made the argument that architecture was a teaching profession in disguise. The intent gap — the distance between what an architect intended and what an organisation understood — was the primary cause of architecture failure. Closing it required education, not better diagrams.

These arguments were not rejections of enterprise architecture. They were calls for a more honest practice. A practice that measured itself by the quality of the decisions it enabled rather than the volume of the documents it produced.

## The 2020s — acceleration and disruption

The pace of change accelerated in the 2020s in ways that put pressure on traditional EA cycles. Cloud computing matured and became the default for most new technology investment. Agile and DevOps moved delivery cycles from months to weeks. AI emerged as a genuine first-class participant in business processes rather than a tool used by humans.

Each of these shifts created challenges for an enterprise architecture practice designed around longer planning horizons. The frameworks responded. TOGAF published its tenth edition in 2022, incorporating more flexibility and explicit acknowledgement of agile delivery contexts. SAP published its enterprise architecture framework aligned to cloud-native and AI-augmented landscapes. New voices in the community argued for architectural approaches that were lighter, faster, and more connected to delivery teams.

Graham Davis articulated what many practitioners were experiencing: AI was not just another technology component to be modelled in the application layer. It disrupted the foundational assumptions of the People-Process-Technology model that had underpinned most capability thinking. AI capable of performing tasks that had previously required human judgement needed to be designed for explicitly — with clear human-machine boundaries, explicit governance, and architecture that could evolve as AI capability itself evolved.

The profession is still working through these challenges. The frameworks are more mature than they have ever been. The conversations about what EA is for are more honest than they have ever been. And the territory — the actual enterprise landscapes that architects are asked to navigate — is more complex and more rapidly changing than it has ever been.

## The timeline in brief