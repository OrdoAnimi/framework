# ArchiMate — The Visual Language

Architecture diagrams are only useful if people can read them. ArchiMate is the standard that makes that possible.

Most architecture diagrams are drawn in PowerPoint or Visio using whatever shapes the author felt like using that day. The result looks different from every architect who produces it. A diagram produced by one team cannot be read reliably by another. ArchiMate solves this by providing a standardised visual language — specific shapes, specific meanings, specific rules for how they connect. Two architects using ArchiMate produce diagrams that any third architect can read without being told what the shapes mean.

Meridian’s current architecture diagrams are spread across 47 PowerPoint files. Each one uses different shapes, different colours, and different conventions. The new EA cannot read one diagram and transfer what she learned to the next. Every diagram requires its own orientation. When she starts producing ArchiMate views the change is immediate. Anyone on the architecture team can read any diagram from the first line. The investment in learning the notation pays back on the first shared diagram.

## The three layers

ArchiMate is organised into three layers. Each layer corresponds to one of the BDAT domains covered in Part 3. The layers are always drawn in the same order: Business at the top, Application in the middle, Technology at the bottom. This is not arbitrary. Business depends on Application. Application depends on Technology. The visual hierarchy reflects the dependency.

## The three aspects

Within each layer, ArchiMate elements are classified by aspect. The aspect tells you what role an element plays.

## The relationships

ArchiMate elements connect through relationships. The relationships are as standardised as the elements. Each type of relationship means something specific.

## ArchiMate versus UML

ArchiMate and UML — the Unified Modelling Language — are both visual languages for describing systems. They are not competitors. They are designed for different purposes and the right choice depends on what you are trying to show.

## How to start reading ArchiMate

You do not need to memorise all of this before you can read an ArchiMate diagram. You need four things.

First, identify which layer you are looking at. Business, Application, or Technology. The colour convention in most tools makes this visible immediately. Second, identify the element types. Rounded rectangles are typically active structure elements. Plain rectangles are typically passive structure. Third, read the relationships as directional. An arrow from A to B means A connects to or depends on B in some way. Fourth, look for the label on the relationship. Serving, realisation, triggering, composition. The label tells you the type of dependency.

The first ArchiMate diagram Meridian’s new EA shares with the clinical director is the current state technology layer. Two VMware nodes. Active Directory. The MPLS network. The EA walks the clinical director through it in ten minutes using just four questions: what are these boxes, what do the arrows mean, what is missing from this picture, and what happens if the bottom layer fails. The clinical director leaves understanding for the first time why a VMware licensing problem is her problem. ArchiMate made the connection visible. The conversation did the rest.
