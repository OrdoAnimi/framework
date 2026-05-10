# Velocity Success Factor™ (VSF) Scorer

**A ZenCloud Global Consultants product.**

> *"Recruiters are selling bodies. VSF measures what architects actually did — not what they were called."*

---

## What Does This Do?

Paste any CV or LinkedIn profile into the VSF Scorer and it will:

1. Read every professional role chronologically
2. Score each role across 5 dimensions of real architectural value (1–10 each)
3. Generate a heat map of career performance over time
4. Benchmark the candidate against 5 standard levels — from Graduate through to Chief Architect
5. Produce a career aggregate score and peak operating level

**The result:** a factual, evidence-based profile that tells you what someone actually did — not what title they held.

---

## Why Does This Exist?

Traditional recruitment filters on:
- Job titles ("has EA in the title")
- Years of experience ("10+ years required")
- Keywords ("TOGAF, Azure, TOGAF, Azure")

None of these measure whether someone actually governed a $35M program, presented to a board, or delivered zero-disruption across 14 data centres on four continents.

VSF does.

---

## The Five Dimensions

| # | Dimension | Weight | What it measures |
|---|---|---|---|
| 1 | **Scale of Impact** | 25% | How far did their work reach? Users, sites, countries, financial consequence |
| 2 | **Complexity Governed** | 25% | How hard was the environment? M&A, regulation, live operations, multi-vendor |
| 3 | **Authority Held** | 20% | What level did they actually operate at? ARB chair, Design Authority, sign-off |
| 4 | **Outcome Integrity** | 20% | Did the work land? Delivered, zero-disruption, clean handover |
| 5 | **Capability Transferred** | 10% | What did they leave behind? Frameworks, patterns, team uplift |

---

## Benchmark Bands

| VSF Score | What it means |
|---|---|
| 3.0 – 4.5 | Graduate / Junior EA |
| 4.5 – 6.0 | Mid-level Solution Architect |
| 6.0 – 7.5 | Senior Solution Architect |
| 7.5 – 8.5 | Principal / Lead EA |
| 8.5 – 10.0 | Chief Architect |

---

## Before You Start — What You Need

You need two things:

### 1. Node.js (free)

Node.js is the software that runs this application on your computer.

- Go to **https://nodejs.org**
- Download the version labelled **LTS** (Long Term Support)
- Install it like any normal application
- To check it worked: open Terminal (Mac) or Command Prompt (Windows), type `node --version` and press Enter — you should see a number like `v20.x.x`

### 2. An Anthropic API Key (pay per use — approx $0.01–0.03 per CV scored)

The scorer uses Claude AI to read and score CVs. You need an API key from Anthropic.

- Go to **https://console.anthropic.com**
- Create a free account
- Go to **API Keys** in the left menu
- Click **Create Key** — name it anything (e.g. "VSF Scorer")
- Copy the key — it starts with `sk-ant-...`
- **Keep it safe — treat it like a password. Do not share it or push it to GitHub.**

**Cost:** Each CV scored costs approximately $0.01–0.03 USD in API usage. There is no subscription — you only pay for what you use. Anthropic provides $5 of free credit when you sign up, which covers 150–500 CV scores.

---

## Installation — Step by Step

### Step 1 — Download the code

**Option A — Using Git:**
```bash
git clone https://github.com/zencloud/vsf-scorer.git
cd vsf-scorer
```

**Option B — Download ZIP:**
Click the green **Code** button at the top of this GitHub page → **Download ZIP** → unzip the file → open the `vsf-scorer` folder.

---

### Step 2 — Open a terminal in the project folder

**Mac:** Right-click the `vsf-scorer` folder → **New Terminal at Folder**

**Windows:** Open the `vsf-scorer` folder in File Explorer → click the address bar at the top → type `cmd` → press Enter

---

### Step 3 — Install dependencies

In your terminal, type exactly:

```bash
npm install
```

Wait for it to finish. You will see a lot of text scroll by — that is normal. It ends when you see your cursor again.

---

### Step 4 — Add your API key

In the `vsf-scorer` folder, find the file called `.env.example`.

- Make a copy of it
- Rename the copy to `.env` (remove the `.example` part)
- Open `.env` in any text editor (Notepad, TextEdit, VS Code)
- Replace `your_api_key_here` with your actual Anthropic API key

It should look exactly like this (with your real key):
```
VITE_ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxx
```

Save the file and close it.

> **Note:** The `.env` file is protected by `.gitignore` — it will never be uploaded to GitHub. Your API key stays on your machine only.

---

### Step 5 — Run the application

In your terminal:

```bash
npm run dev
```

You will see output like:
```
  VITE v5.x.x  ready in 300ms
  ➜  Local:   http://localhost:5173/
```

Leave this terminal window open while you use the application.

---

### Step 6 — Open in your browser

Go to **http://localhost:5173** in Chrome, Safari, Firefox, or Edge.

The VSF Scorer will load. A sample CV is pre-loaded — click **SCORE THIS CV** to test that everything is working.

---

## How to Use It

1. **Paste a CV** into the large text area — plain text works best. Copy and paste from Word, PDF, or a LinkedIn profile.
2. **Enter the candidate's name** in the name field at the top
3. **Click SCORE THIS CV**
4. Wait 10–30 seconds while Claude reads and scores the CV
5. View the results:
   - **Heat Map** — visual grid of VSF scores by engagement. Click any cell to see the full dimension breakdown.
   - **Timeline** — bar chart showing career trajectory over time
   - **Detail** — complete dimension scores in a table
6. Click **← Score Another CV** to start again with a new CV

---

## What Makes a Good CV Input?

The scorer works best with CV text that includes:

- Clear role title and organisation for each position
- Dates (years are sufficient — exact months not required)
- What the person actually delivered — not just a list of responsibilities
- Scale indicators — team sizes, number of users, countries, financial figures
- Authority indicators — who they reported to, what governance forums they chaired, what they signed off

The more outcome-oriented detail in the CV, the more accurate the VSF scores.

---

## Stopping the Application

When you are finished, go back to your terminal and press **Ctrl + C** to stop the server.

To start it again next time, open your terminal in the `vsf-scorer` folder and run `npm run dev` again.

---

## Troubleshooting

**"npm: command not found"**
Node.js is not installed or not recognised. Reinstall from https://nodejs.org and restart your terminal completely before trying again.

**"VITE_ANTHROPIC_API_KEY not set"**
Your `.env` file is missing or named incorrectly. Make sure the file is called exactly `.env` (not `.env.example`, not `.env.txt`) and is saved inside the `vsf-scorer` folder.

**"API error: 401"**
Your API key is invalid or has been revoked. Generate a new one at https://console.anthropic.com and update your `.env` file.

**"API error: 429"**
You have hit Anthropic's rate limit. Wait 60 seconds and try again.

**"Failed to parse scoring response"**
The CV text may be too short or too vague for Claude to extract engagements from. Try adding more detail — role titles, organisations, dates, and what was delivered.

**Blank screen when I open the browser**
Make sure you are visiting `http://localhost:5173` (not `https://`) and that `npm run dev` is still running in your terminal.

**Nothing happens when I click Score This CV**
Check your terminal window — there may be an error message there. Most commonly this is an API key issue.

---

## Security — Important

**Never deploy this application publicly with your API key exposed.**

The `.env` file is excluded from GitHub by `.gitignore`. Your key stays local.

If you want to deploy VSF Scorer as a public web application for others to use, you must route the Claude API call through a backend server that holds the API key securely. Contact ZenCloud for guidance on production deployment.

---

## Project Structure

For developers who want to understand or extend the codebase:

```
vsf-scorer/
├── src/
│   ├── App.jsx              # Root component
│   ├── VSFScorer.jsx        # Main scorer interface and all views
│   ├── main.jsx             # React entry point
│   └── lib/
│       ├── scoring.js       # VSF calculation engine, dimension definitions, benchmark bands
│       └── claude.js        # Claude API call and scoring prompt construction
├── public/
│   └── index.html           # HTML shell
├── .env.example             # API key template — copy to .env and add your key
├── .gitignore               # Keeps .env out of GitHub
├── package.json             # Project metadata and dependencies
├── vite.config.js           # Vite build configuration
├── LICENSE                  # MIT licence
└── README.md                # This file
```

---

## Roadmap

- [ ] PDF and DOCX upload — drag and drop a CV file directly
- [ ] Multi-candidate comparison — score two CVs side by side
- [ ] Export to PDF — one-page candidate VSF summary report
- [ ] LinkedIn profile URL import
- [ ] Team cohort dashboard — score and rank a shortlist
- [ ] Backend proxy for safe public deployment

---

## Contributing

Issues, ideas, and pull requests are welcome via GitHub.

---

## Licence

MIT — see `LICENSE` for details.

Velocity Success Factor™ is a trademark of ZenCloud Global Consultants.

---

## About ZenCloud Global Consultants

ZenCloud Global Consultants provides enterprise architecture advisory, governance frameworks, and hiring intelligence tools for organisations navigating complex technology transformation.

**zencloud.com.au** | **zencloud.com.au/writing**

---

*© 2026 ZenCloud Global Consultants. Velocity Success Factor™ is a ZenCloud trademark.*
