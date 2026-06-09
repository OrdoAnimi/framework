Part 2 · The Frameworks Explained
Chapter 5
Zachman — The Classification System

John Zachman did not invent enterprise architecture. He gave it a way to think about itself.

In 1987 Zachman was working at IBM. Large organisations were drowning in complexity. They had been building technology systems for two decades and each system had been built in isolation. A payroll system over here. A customer database over there. A claims processing platform. A financial reporting tool. Each built by a different team at a different moment to solve a different problem. Each one working perfectly on its own terms.

Together they were becoming unmanageable.

The problem was not that the systems were bad. The problem was that nobody had a way of describing them all together that made sense. Engineers described systems one way. Managers described them another. Executives needed something different again. Everyone was talking about the same estate and none of them was speaking the same language.

Imagine the situation at Meridian Health Partnership today. The clinical director describes the patient record system as a tool for delivering safe care. The IT manager describes it as a VMware virtual machine running on aging hardware. The project manager describes it as a dependency blocking the cloud migration. The CFO describes it as a cost line. They are all describing the same system. None of them is wrong. And none of them can have a useful conversation with the others because they have no shared framework for organising what they each know.

That is the problem Zachman was looking at in 1987. And the solution he proposed was not a new methodology. It was not a process. It was a classification system. A way of organising the different descriptions of an enterprise so that every type of description had a home and nothing important was confused with something else.


The grid

The Zachman Framework is a six-by-six matrix. Six rows. Six columns. Thirty-six cells. Each cell represents a distinct type of architecture description.

The rows represent different perspectives. Different audiences who need different things from the same organisation.


The columns represent the six interrogatives. Six questions that any complete description of an enterprise must be able to answer.


Every cell in the grid is the intersection of one row and one column. The cell at Row 3, Column 1 is the architect's view of what data exists. The cell at Row 2, Column 6 is the business manager's view of why the organisation exists. The cell at Row 5, Column 2 is the technician's view of how something actually runs.

None of these cells is more important than the others. None of them is the whole picture. All thirty-six together add up to a complete description of an enterprise. That is the Zachman Framework. Not a process. Not a methodology. A classification system that tells you where every type of description belongs.


The aeroplane and the building

Zachman used an analogy to explain the framework that still works thirty-nine years later.

Think about a commercial aeroplane. To build one you need many different types of description. The aeronautical engineer needs aerodynamic models. The structural engineer needs stress calculations. The systems engineer needs wiring diagrams. The interior designer needs spatial layouts. The pilot needs flight manuals. The maintenance technician needs service specifications.

Each of these is a complete and accurate description of the same aeroplane. None of them substitutes for another. The aerodynamic model does not tell you how to service the landing gear. The interior layout does not tell you how the engines work. They are different descriptions of the same object, each complete for its intended purpose, each belonging to a different cell in the grid.

At Meridian, the patient record system is exactly like that aeroplane. The clinical director's description of it as a care delivery tool is accurate and complete for her purposes. The infrastructure engineer's description of it as a virtual machine on VMware is accurate and complete for his purposes. The data governance lead's description of it as a repository of personally identifiable health information is accurate and complete for her purposes. All three are right. All three belong in different cells of the Zachman grid. The problem is not that any description is wrong. The problem is that Meridian has never organised them so people can find the right one when they need it.


Where you will encounter Zachman

Zachman is less commonly used as an active working tool than TOGAF or ArchiMate. Most organisations that work with Zachman use it as a reference model rather than a daily practice.

You will encounter it most often in three situations.

The first is in large government and defence organisations. Zachman's influence on FEAF and DODAF means its fingerprints are visible in government architecture frameworks globally. If you work in or with government IT you will see the row and column logic even when the Zachman name is not used.

The second is in academic and formal EA education. Zachman is a foundational framework in most enterprise architecture courses and certifications. Understanding it gives you the conceptual foundation that makes every other framework easier to learn. The ADM phases in TOGAF, the layers in ArchiMate, the domains in BDAT — all of them are easier to understand if you have first understood why classification matters.

The third is in organisations doing serious architecture documentation. When an organisation wants to ensure they have captured every type of architecture description they need, the Zachman grid is the completeness check. If you can populate every cell you have missed nothing.

Meridian's new enterprise architect uses the Zachman grid in her first month. Not to build a complete thirty-six cell model — that would take years. But to check completeness. She maps what documentation already exists at Meridian against the grid. Seven cells have reasonable content. Twenty-nine are empty. That tells her exactly where the gaps are before she starts planning. The grid did not tell her what to build. It told her what was missing.

What Zachman does well and where its limits are

Zachman does one thing exceptionally well. It provides a complete and logical classification of every type of architecture description an enterprise might need. Nothing is missing from the grid. Nothing is in the wrong place. As a completeness check and a shared vocabulary it is rigorous and elegant.

Its limits are equally clear.

It is not a methodology. The Zachman Framework tells you where descriptions belong. It does not tell you how to create them, in what sequence, or what to do when you have them. If you pick up the Zachman Framework hoping it will tell you how to run an architecture programme you will be disappointed. That is not what it is for.

It is also not a practical tool for most daily architecture work. Populating all thirty-six cells for a large organisation is a significant undertaking that takes years. Most organisations use a subset of the cells relevant to their current problem rather than attempting completeness.

And it does not address how architectures are developed, governed, or changed over time. For that you need TOGAF. For visual notation you need ArchiMate. Zachman provides the intellectual foundation. The other frameworks provide the working method.