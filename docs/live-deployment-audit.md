# Live Deployment Audit

Date: 2026-05-28

## Scope

This audit records source-vs-live deployment freshness for the ZenCloudAU / Velocity Architecture estate.

No workflow, DNS, Cloudflare, application, or design changes were made as part of this audit.

## Findings

| Site | Source Status | Live Status | Finding | Action |
|---|---|---|---|---|
| velocity-academy | Source includes Explore courses CTA and Python / TypeScript course cards | Live page still shows older Explore learning paths CTA and does not expose the new course cards | Deployment freshness mismatch | Verify Cloudflare Pages production branch, build source, and latest deployment |
| velocity-academy/courses | Source includes Python Zero to Hero and TypeScript Zero to Hero course cards | Live route requires browser verification | Pending live verification | Verify after Cloudflare redeploy |
| vaf-python-zero-to-hero | Source is a static course site | Live route documented | Pending live verification | Verify GitHub Pages freshness |
| vaf-typescript-zero-to-hero | Source redirects root to docs and docs contains the course page | Live route documented | Pending live verification | Verify GitHub Pages freshness |
| vsf-match | Source uses GitHub Actions Pages deployment | Live route documented | Pending live verification | Verify GitHub Pages freshness and generated asset strategy |

## Confirmed Source Evidence

Velocity Academy source now links the hero CTA to `courses/index.html` and labels it `Explore courses`.

Velocity Academy source now includes `Python Zero to Hero` and `TypeScript Zero to Hero` cards.

Velocity Academy course source now includes both course cards and links them to the relevant GitHub Pages course sites.

## Deployment Risk Notes

1. The Academy source appears correct, but the live Cloudflare Pages site appears stale.
2. The likely causes are Cloudflare Pages deployment branch mismatch, stale production deployment, root/output directory mismatch, or cache.
3. Do not change DNS or custom domains before confirming Cloudflare Pages project settings.
4. Do not rewrite workflows during this audit stage.

## Next Action

Trigger or inspect Cloudflare Pages deployment for `velocity-academy` and confirm that the production deployment is sourced from the latest `main` branch commit.
