# Chapter 13: Wardley Mapping — Seeing What Moves

## Opening

Most architecture frameworks describe what exists. Wardley Mapping describes what is happening to what exists.

That is a different kind of thinking, and it produces a different kind of insight. A TOGAF Architecture Vision tells you where you want to get to. An ArchiMate diagram tells you what the current estate looks like. A Wardley Map tells you why certain parts of that estate are becoming a liability, which parts are about to become commodities, and where the strategic decisions actually sit.

You do not need to produce Wardley Maps to get value from this chapter. What you need is to be able to read one when it appears in a strategy conversation — and increasingly, it will. The tool has moved from the margins of technology thinking into mainstream use in cloud strategy, digital transformation, and government technology leadership. If you are in a room where someone is talking about **evolution** and **commodity** and **genesis**, this chapter is what makes that conversation legible.

---

## Where Wardley Mapping Came From

**Simon Wardley** developed the mapping approach in the mid-2000s while working as a CEO trying to make technology strategy decisions. He found that the tools available — strategy documents, technology roadmaps, vendor presentations — all described what existed but gave him no way of reasoning about how technology components evolve over time, and therefore no way of making genuinely informed decisions about where to invest, what to build, and what to buy.

He borrowed from two places. From military strategy he took the idea that a map showing the terrain is more useful than a list of positions. From economics he took the observation that technologies — like products and services — follow a predictable pattern of evolution from novel and uncertain to well-understood and commodity. Combining those two observations produced Wardley Mapping.

The approach was published openly, refined through years of practitioner use, and is now part of the UK Government Digital Service's strategy toolkit. It has no certification programme in the traditional sense, no standards body, and no official specification. It is a thinking tool, distributed freely, improved by a global community of practitioners.

That informality is deliberate and important. Wardley Mapping is not a framework in the sense that TOGAF or SABSA are frameworks. It is a practice — a way of seeing — and it is more useful the more honestly it is applied.

---

## The Two Axes

A Wardley Map is a two-dimensional chart. Understanding the two axes is all you need to start reading one.

The **vertical axis** is the value chain — the chain of components that delivers value to the user at the top. The user's need sits at the top of the map. Everything below it is something that exists to serve that need. Components higher on the vertical axis are closer to the user and more visible to them. Components lower on the axis are further from the user — infrastructure, platforms, enabling capabilities that the user never sees directly but that everything else depends on.

The **horizontal axis** is evolution. It runs from left to right across four stages:

**Genesis** — on the far left. The component is novel, poorly understood, and unstable. Nobody has worked out how to do this well yet. It is expensive, uncertain, and different every time. Early cloud computing was here in the mid-2000s. Early AI capabilities are here now for many use cases.

**Custom-built** — one step right. The component is better understood but still built specifically for each organisation that needs it. It works, but every implementation is bespoke. There is skill involved and significant variation between providers.

**Product** — moving right again. The component has been standardised enough that products and services exist to deliver it. You can buy it rather than build it. The variation between implementations is narrowing. VMware virtualisation was here for most of the 2000s and 2010s.

**Commodity** — on the far right. The component is so well understood, so standardised, and so widely available that differentiation is essentially impossible. Cost and reliability are what matters. Electricity is the classic example. Cloud compute is here now. Increasingly, basic virtualisation is here too.

*At Meridian, the VMware estate sits in the product-to-commodity transition on the horizontal axis. VMware was a differentiating product capability fifteen years ago — it gave organisations server consolidation and flexibility that was genuinely difficult to achieve otherwise. Today, every cloud provider offers equivalent or superior capability as a commodity. Meridian is paying for a product-era capability in a commodity-era world. That is not a technology problem. It is an evolution problem. The Wardley Map makes it visible in a way that a cost analysis or a technical assessment does not.*

---

## The Value Chain

The vertical axis is where Wardley Mapping connects to the business architecture thinking from Chapter 11.

You build the value chain by starting with the user and asking: what does this person need? Then asking: what capabilities do we need in order to deliver that? Then asking: what does each of those capabilities depend on? You keep going until you reach the infrastructure layer — the components that everything else ultimately rests on.

*Meridian's value chain for community nursing starts with the patient: the need to receive safe, coordinated care at home. To deliver that, the community nurse needs access to the patient's clinical record in the field. To provide that access, Meridian needs a mobile-capable clinical application. That application depends on the EPR. The EPR depends on the network infrastructure. The network infrastructure depends on the data centre. The data centre depends on the VMware estate. Every component in that chain is visible on a Wardley Map. When the VMware estate starts failing, the impact travels up the chain — all the way to the patient who does not receive the care that was planned because the nurse could not access the record.*

This is what Wardley Mapping does that impact assessments and risk registers often fail to do. It shows the dependency chain as a spatial object. The visual makes the consequences of a failure at any point immediately legible — you can trace the line from the broken component upward to the user and see exactly what stops working.

---

## Evolution and the Strategic Insight

The strategic power of Wardley Mapping comes from combining the value chain with evolution.

Once you have placed your components on the map — positioned by their value chain height and their evolutionary stage — you can ask questions that most strategy documents cannot answer:

**Where are we treating a commodity as if it were a product?** If a component is on the right of the horizontal axis — commodity territory — and you are still building or customising it, you are spending money that produces no competitive differentiation. That money should be redirected.

**Where are we building something we should be buying?** If competitors can purchase a capability as a product and you are still building it custom, you are carrying a cost disadvantage with no strategic benefit.

**Where is the next movement going to happen?** Components move left to right over time — from genesis toward commodity. Identifying which of your components are mid-evolution lets you anticipate where commoditisation will happen next and plan ahead rather than react.

**Where is genuine differentiation possible?** Differentiation only comes from components in the genesis and custom-built stages — the left side of the map. Everything to the right is table stakes. Investing in differentiation on the right side of the map is waste. Investing in differentiation on the left side is strategy.

> **Pull quote:** "A Wardley Map does not tell you what to do. It tells you where you are standing — and why some of the ground beneath you is shifting."

---

## What Wardley Mapping Is Not

Wardley Mapping is not a prediction tool. It shows the current position of components and their likely direction of movement — not exactly when a component will commoditise or what will replace it. The map is a reasoning aid, not a forecast.

It is also not a communication tool to reach for before doing the hard thinking. A map where components have been placed quickly to populate a slide is decorative, not analytical. The value is in the conversation the map provokes, and that conversation only happens when the people in the room know the territory well enough to argue about where components actually sit.

---

## How Wardley Mapping Connects to the Other Frameworks

Wardley Mapping sits alongside the other frameworks in Part 2 rather than replacing any of them. The connections are practical and specific.

**With TOGAF Phase A and Phase E:** Wardley Mapping is useful at the strategy and options stages of an ADM programme. Phase A asks what success looks like. A Wardley Map of the current estate and its evolutionary trajectory helps answer why the current state is unsustainable. Phase E produces options — a Wardley Map helps evaluate which options are moving with the direction of travel and which are fighting it.

**With capability maps:** A capability map from BIZBOK shows what the organisation can do. A Wardley Map shows the evolutionary position of the components that deliver those capabilities. Together they answer two questions: what can we do, and how exposed are we if the technology delivering it commoditises before we are ready?

**With application portfolio work:** The application portfolio, covered in Chapter 21, catalogues the estate and assesses each application against its fitness for purpose. Wardley Mapping adds the evolutionary dimension — not just whether an application is fit today, but whether the approach it represents is viable in three years' time.

*At Meridian, the EA uses a Wardley Map during the VMware exit programme to make a specific argument to the board. She places the VMware virtualisation layer on the horizontal axis — product territory, moving toward commodity. She places Meridian's cloud provider equivalents on the far right — commodity already. She places the EPR systems higher on the value chain — closer to the user — and shows their dependency on the virtualisation layer. The argument she makes is not about cost, though cost follows from it. The argument is about position: Meridian is paying product-era prices for commodity-era capabilities, and that money should move to the EPR consolidation problem, which is where genuine differentiation in patient care is still possible. The board approves the reallocation. The Wardley Map did not make that decision — but it made the decision possible in a twenty-minute conversation.*

---

## Reading a Wardley Map in the Room

When a Wardley Map appears in a strategy conversation, here is how to read it quickly.

Start with the vertical axis. Find the user at the top. Trace downward to understand what the organisation is trying to deliver and what it depends on. This tells you the scope of the conversation.

Move to the horizontal axis. Anything on the far left — genesis territory — is where uncertainty and potential differentiation sit. Anything on the far right — commodity territory — is where the answer to build-vs-buy is always buy.

Look for inconsistencies: a commodity being treated as a product, or an early-stage component being managed as if it were stable. Those are usually where the organisation's real problems sit.

Then ask the question the map is designed to generate: given where everything sits, what should we be doing differently?

---

## Translator Panel

> **Practitioners say:** "Wardley Mapping is a situational awareness tool that maps components of value delivery against their evolutionary stage, from genesis through commodity, to enable strategic positioning."
>
> **What that means:** A Wardley Map is a diagram that shows what your organisation depends on to deliver value, and how mature each of those dependencies is. Mature dependencies should be bought, not built. Immature ones are where genuine differentiation is possible. The map shows you which is which.

> **Practitioners say:** "Evolution describes the movement of components from novel and uncertain activities through increasing understanding toward commodity and utility."
>
> **What that means:** Technology matures over time. What starts as experimental becomes custom-built, then becomes a product you can buy off the shelf, then becomes a commodity like electricity that you simply consume without thinking. Wardley Mapping puts your components on that journey and asks: are you treating them appropriately for where they actually are?

---

## The Key Idea

Wardley Mapping adds the dimension that other frameworks leave out: time and direction. A map of your technology estate that does not show which components are evolving, commoditising, or becoming obsolete is a photograph when what you need is a weather forecast. Wardley Mapping is not a replacement for TOGAF or ArchiMate or a capability map. It is the tool that shows you which direction the ground is moving — so that the architecture you build is designed for where things are going, not where they have been.

**Next:** Chapter 14 moves to ITIL — the service management framework that governs how the estate that architecture designs actually runs day to day, and why the relationship between architecture and service management is one of the most important and most misunderstood in the profession.

---

## Further Reading

- **Simon Wardley — Wardley Maps** (medium.com/@swardley or learnwardleymapping.com): Wardley published the full approach openly and the online version is the most current. Start with the "Finding a path" series. Free and comprehensive.
- **UK Government Digital Service — Technology Code of Practice** (gov.uk): The GDS applies Wardley Mapping in government technology strategy. Their published guidance shows how the tool is used in practice at scale in a public sector context — directly relevant to anyone working in or with government.
- **Ben Mosior — Wardley Mapping for Product Teams**: A practitioner-focused introduction that grounds the approach in delivery team contexts rather than executive strategy. Useful if you want to see how the tool applies below the leadership layer.
- **Chris Daniel and Ben Mosior — Wardley Mapping, The Knowledge** (learnwardleymapping.com): A structured guide to building maps from scratch. The right next step once you have read this chapter and want to start producing rather than just reading.
