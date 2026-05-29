# Ecosystem Change Protocol

Process for making cross-site URL changes and maintaining ecosystem link integrity.

---

## When to Use This Protocol

Use this protocol for any change that affects a canonical URL or cross-site link:

- Migrating a repo from GitHub Pages to a custom domain
- Changing a domain name
- Restructuring a site's URL paths
- Adding or renaming a public page

---

## Step 1 — Update LINK-REGISTRY.md

Before touching any file, update `ecosystem/LINK-REGISTRY.md`:

1. Change the canonical URL in the **Canonical URLs** table
2. If retiring an old URL, add it to the **Retired / Redirected URLs** table
3. Update the **Status** column

---

## Step 2 — Grep All Repos

Run a cross-repo search for the old URL before changing it:

```bash
grep -r "OLD-URL" /path/to/GitHub/ --include="*.html" --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.md" -l
```

Do not commit any file changes until you have a complete list of affected files.

---

## Step 3 — Apply Changes in One Pass

Fix all occurrences across all affected repos in a single session. Do not fix one repo and leave others stale.

Priority order:
1. Live HTML files (`.html`) — user-facing, highest impact
2. React/TypeScript component files (`.tsx`, `.jsx`) — build outputs affected
3. Instruction files (`CLAUDE.md`, `AGENTS.md`) — affects AI guidance
4. Living documentation (coherence standards, control matrices)
5. Historical records (`legacy-url-redirect-map.md`, runbooks) — may intentionally retain old URLs

---

## Step 4 — Verify og: Meta Tags

After a domain change, verify the `og:url` tags in all affected HTML entry points match the new canonical URL. See `LINK-REGISTRY.md` for the current og: status across all repos.

---

## Step 5 — Update LINK-REGISTRY.md og: Table

Update the og: Meta Status table in `LINK-REGISTRY.md` to reflect any changes.

---

## Step 6 — Commit All Repos

Commit all repos affected by the change in a single round. Suggested commit message format:

```
Update canonical URL: OLD-DOMAIN → NEW-DOMAIN

Affects: [list repos]
```

---

## Domain Migration Checklist

When migrating a repo to a custom domain:

- [ ] Confirm DNS is live and returning 200
- [ ] Update `LINK-REGISTRY.md` canonical URL and status
- [ ] Grep all repos for old `zencloudau.github.io/REPO` URL
- [ ] Update `og:url` in all HTML entry points
- [ ] Update all cross-site nav links pointing to this repo
- [ ] Update `CLAUDE.md` / `AGENTS.md` instruction files in all repos
- [ ] Update any living documentation (coherence standards, repo control matrix)
- [ ] Verify all agent launch links still point to `/app/portal.html` where applicable
- [ ] Run ecosystem-link-check workflow to confirm all URLs return 200
- [ ] Update LINK-REGISTRY.md og: Meta Status table

---

## Agent Launch Link Rule

The VAF Agentic Architect entry point is:

```
https://velocityarchitectureframework.com/app/portal.html
```

Agent launch links (buttons or CTAs labelled "Open agent ↗", "VAF Agent ↗", "Agentic Architect ↗") **must** link to `/app/portal.html`, not the bare domain. This is enforced in the link-integrity workflow.

Site navigation back-links (`← VAF`, `VAF Framework ↗`, etc.) may link to the bare domain — these are site references, not agent launch points.

---

*See LINK-REGISTRY.md for current canonical URL state.*
