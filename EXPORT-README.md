# ZAF Master Export — Thread 1 Complete
## ZenCloud Architecture Framework™ — Version 1

**Exported:** May 2026
**Thread:** 1 of 2 — Foundation, Research, Tools, Studio, Portal
**Next thread:** Version 2 — VAF Agentic Architect

---

## CURRENT REPO STATE — NOTHING FROM THIS THREAD IS UPLOADED YET

GitHub repo: github.com/ZenCloudAU/velocity-architecture
Commits: 18 (original content only)

The repo contains only original pre-thread content. Everything in this zip is new.

---

## UPLOAD CHECKLIST — WORK THROUGH IN ORDER

### Step 1 — Fix the licence

Repo shows "Unknown, Unknown licenses found". Two actions in GitHub browser:

Action A: Open LICENSE → pencil → replace entire contents with MIT text from repository/LICENSE in this zip → commit.

Action B: Open LICENSE.md → pencil → change filename to USAGE-AND-TERMS.md → replace contents with repository/USAGE-AND-TERMS.md from this zip → commit.

Result: MIT badge appears. Unknown warning gone.

---

### Step 2 — Upload repository content

In GitHub Desktop, copy from repository/ in this zip into the repo root:

  research/           4 research papers + bibliography
  frameworks/         3 framework documents
  guides/             plain language guide + practitioner manual (MD + docx)
  tools/              18 templates (MD + docx) + compression map
  assets/             licence terms
  spec/ additions     3 new ISO 42010 conformance documents

Also copy repository/README.md to replace existing README.md.
Also copy repository/CHANGELOG.md to repo root.

Commit: "Add VAF research, frameworks, guides, templates and conformance docs — May 2026"
Push.

---

### Step 3 — Upload studio and portal

CRITICAL: Before committing, open studio/index.html in a text editor.
Find CONFIG block at top. Change:
  practitionerKey: 'ZAF-2026',
to your actual key. Write it down offline.

Copy:
  studio/index.html  →  velocity-architecture/studio/index.html
  portal/index.html  →  velocity-architecture/portal/index.html

Commit: "Add ZAF Studio v2 and Client Portal"
Push.

URLs after upload:
  velocityarchitectureframework.com/studio/   Practitioner Studio
  velocityarchitectureframework.com/portal/   Client Portal

---

### Step 4 — Upload website files to repo root

Copy from website/ in this zip:
  landing-page.html  →  rename to index.html in repo root
  _config.yml        →  repo root
  CNAME              →  repo root

Do NOT upload zaf-page-squarespace.html or zaf-page-standalone.html to repo.
These are for zencloud.com.au when trademark clears.

Commit: "Update GitHub Pages landing page"
Push.

---

### Step 5 — Update CITATION.cff

In GitHub, open CITATION.cff → pencil → update version and date to May 2026 → commit.

---

## FILE INVENTORY

ZAF-Master-Export/
├── EXPORT-README.md                      this file
├── repository/
│   ├── README.md                         updated repo README
│   ├── LICENSE                           MIT licence
│   ├── USAGE-AND-TERMS.md               replaces LICENSE.md
│   ├── CHANGELOG.md                      NEW — Series versioning
│   ├── research/                         4 papers
│   ├── frameworks/                       3 documents
│   ├── guides/                           3 files
│   ├── tools/                            4 files
│   ├── spec/                             3 NEW ISO 42010 conformance docs
│   └── assets/                           1 file
├── studio/
│   └── index.html                        ZAF Studio v2 — CHANGE KEY FIRST
├── portal/
│   └── index.html                        ZAF Client Portal
├── website/
│   ├── landing-page.html                 rename to index.html for repo
│   ├── _config.yml
│   ├── CNAME
│   ├── zaf-page-squarespace.html         hold for zencloud.com.au
│   └── zaf-page-standalone.html
└── documents/
    ├── VAF_Practitioner_Operating_Manual.docx
    └── VAF_EA_Artefact_Templates.docx

---

## VERSION 2 — OPEN NEXT THREAD WITH THIS PROMPT

"We are building Version 2 of the ZenCloud Architecture Framework toolkit.
This is the VAF Agentic Architect — a Claude-powered agentic EA that connects
to github.com/ZenCloudAU/velocity-architecture, operates from the VAF knowledge
base, and produces EA artefacts autonomously. Version 1 is complete and in the
master export. Build the architecture for Version 2. Also build: three ISO 42010
conformance documents (conformance statement, viewpoint catalogue, correspondence
matrix), CHANGELOG.md, and SAP Activate / ZAF mapping module."

---

ZenCloud Global Consultants · ZenCloud Architecture Framework™ · May 2026
Thread 1 closed.
