# Velocity Success Factor™ (VSF) Scorer

**A ZenCloud Global Consultants product.**

> *"Recruiters are selling bodies. VSF measures what architects actually did — not what they were called."*

---

## What is VSF?

The Velocity Success Factor is a career value intelligence framework that scores professional engagements across five dimensions of verified architectural value — replacing keyword and title matching with evidence-based capability assessment.

Every existing ATS scores on keywords, titles, and years of experience. VSF scores on value delivered, complexity governed, and authority held. A candidate with 8 years and a 9.2 VSF outranks a candidate with 20 years and a 6.1 VSF. That is a fundamentally different hiring signal.

---

## The Five Dimensions

| Dimension | Weight | What it measures |
|---|---|---|
| **Scale of Impact** | 25% | Geographic reach, users/seats/sites affected, financial consequence |
| **Complexity Governed** | 25% | M&A, regulated industries, multi-vendor, live operations, technical debt |
| **Authority Held** | 20% | Decision-making level, ARB/governance forum role, sign-off responsibility |
| **Outcome Integrity** | 20% | Delivery completion, zero-disruption, client satisfaction, clean handover |
| **Capability Transferred** | 10% | Reusable patterns, frameworks built, standards set, team uplift |

---

## Benchmark Bands

| VSF Score | Benchmark |
|---|---|
| 3.0 – 4.5 | Graduate / Junior EA |
| 4.5 – 6.0 | Mid-level Solution Architect |
| 6.0 – 7.5 | Senior Solution Architect |
| 7.5 – 8.5 | Principal / Lead EA |
| 8.5 – 10.0 | Chief Architect |

---

## How it Works

1. Paste any CV or LinkedIn profile text into the scorer
2. Claude AI parses each professional engagement chronologically
3. Each engagement is scored across all five dimensions automatically
4. A VSF heat map, timeline, and dimension breakdown are generated
5. The candidate is benchmarked against the five standard bands

**Scoring happens in under 60 seconds per CV.**

---

## Use Cases

**For hiring managers and CIOs** tired of title-based recruitment — understand actual capability before the interview.

**For architecture practice leads** building teams — compare candidates on verified value, not years.

**For recruiters** who want to differentiate — stop selling bodies, start selling evidence.

**For architects** assessing their own trajectory — understand where you have operated and where you are heading.

---

## Tech Stack

- React (functional components, hooks)
- Anthropic Claude API (`claude-sonnet-4-20250514`)
- CSS-in-JS styling
- No external UI libraries

---

## Setup

### Prerequisites
- Node.js 18+
- Anthropic API key

### Install

```bash
git clone https://github.com/zencloud/vsf-scorer.git
cd vsf-scorer
npm install
```

### Configure

Create a `.env` file in the root:

```env
VITE_ANTHROPIC_API_KEY=your_api_key_here
```

> **Note:** The Claude API call is made client-side in the demo. For production deployment, proxy the API call through a backend to protect your API key.

### Run

```bash
npm run dev
```

---

## Project Structure

```
vsf-scorer/
├── src/
│   ├── App.jsx              # Root component
│   ├── VSFScorer.jsx        # Main scorer interface
│   ├── components/
│   │   ├── HeatMap.jsx      # Heat map view
│   │   ├── Timeline.jsx     # Timeline view
│   │   ├── DetailTable.jsx  # Dimension detail table
│   │   └── BenchmarkBar.jsx # Benchmark positioning
│   ├── lib/
│   │   ├── scoring.js       # VSF calculation engine
│   │   ├── benchmarks.js    # Benchmark band definitions
│   │   └── claude.js        # Claude API integration
│   └── styles/
│       └── theme.js         # Design tokens
├── public/
│   └── index.html
├── .env.example
├── package.json
├── vite.config.js
└── README.md
```

---

## API Usage

The scorer uses the Anthropic Messages API with a structured prompt that extracts engagements from CV text and scores each across the five VSF dimensions. The prompt returns JSON that is parsed and rendered directly.

```javascript
// lib/claude.js
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    messages: [{ role: "user", content: scoringPrompt(cvText, candidateName) }]
  })
});
```

---

## Scoring Prompt Design

The scoring prompt instructs Claude to:
1. Parse each professional engagement chronologically
2. Score each across all five dimensions (1–10)
3. Provide a one-line evidence note explaining the scores
4. Return structured JSON only — no preamble, no markdown

See `lib/claude.js` for the full prompt specification.

---

## Roadmap

- [ ] PDF upload support (CV parsing from file)
- [ ] Multi-candidate comparison view
- [ ] Side-by-side heat map overlay
- [ ] Export to PDF report
- [ ] Backend API proxy for production key security
- [ ] LinkedIn profile URL import
- [ ] Team/cohort scoring dashboard
- [ ] VSF trend analysis over time

---

## Contributing

VSF is a ZenCloud Global Consultants framework. Contributions, issues, and feature requests are welcome.

---

## Licence

MIT — see `LICENSE` for details.

---

## About ZenCloud Global Consultants

ZenCloud Global Consultants provides enterprise architecture advisory, governance frameworks, and hiring intelligence tools for organisations navigating complex technology transformation.

**zencloud.com.au** | **zencloud.com.au/writing**

---

*Velocity Success Factor™ is a ZenCloud Global Consultants framework.*
