# Velocity Research Publishing Workflow

This folder uses a source-backed publishing model.

## Principle

Markdown is the source of truth. Public readers should see rendered HTML.

Do not publish raw GitHub Markdown links on LinkedIn unless the intent is to show the source file. Publish the rendered research reader URL instead.

## Current publishing pattern

1. Add the paper as a Markdown file in `research/`.
2. Add it to the rendered research library in `research/index.html`.
3. Publish the rendered reader URL, not the raw Markdown URL.

Example:

```text
Source file:
research/zencloud-it-governance-working-paper-may-2026.md

Reader page:
https://zencloudau.github.io/velocity-architecture/research/

Featured article page:
https://zencloudau.github.io/velocity-architecture/research/it-governance-frameworks-australian-public-sector-2025-2026/
```

## Reader experience standard

Every research paper must provide:

- Readable HTML rendering.
- Top navigation back to the framework, research library, ZenCloud, StudioSix, Academy, and GitHub.
- Footer links back into the ecosystem.
- A GitHub source link for audit/source-of-truth purposes.
- No dead-end article pages.

## Scalable target state

For hundreds of policy papers, cloud patterns, architecture patterns, and research articles, the target workflow should become:

```text
1. Add Markdown file to /research/
2. Add metadata entry to a paper registry
3. The research library lists it automatically
4. A reusable reader route renders it automatically
5. LinkedIn points to the rendered reader URL
```

The preferred target URL shape is:

```text
https://zencloudau.github.io/velocity-architecture/research/reader/?file=research/example-paper.md
```

or, after registry support:

```text
https://zencloudau.github.io/velocity-architecture/research/paper/example-paper/
```

## Recommended metadata fields

Each paper should eventually have:

```text
title
subtitle
slug
type
published_date
tags
source_file
author
status
```

## Do not duplicate content

Do not manually recreate the same paper as separate HTML content unless it is a special featured article.

Use Markdown once. Render it everywhere.

## Publishing rule

If the paper is for LinkedIn or public sharing, the link must open a styled HTML reader, not raw GitHub text.
