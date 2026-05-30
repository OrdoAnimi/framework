# ZenCloudAU Deployment Map

This document defines the deployment model for the ZenCloudAU / Velocity Architecture ecosystem.

## Deployment Principles

1. Source files and generated build files should be kept separate where practical.
2. Cloudflare Pages is used for commercial or primary brand surfaces.
3. GitHub Pages is used for static learning assets, tools, demos, and public reference sites.
4. Each repo should declare:
   - purpose
   - source of truth
   - deployment target
   - production URL
   - build command
   - output directory
   - owner role in ecosystem

## Cloudflare Pages Sites

| Repo | Role | Production URL | Build Command | Output | Status |
|---|---|---|---|---|---|
| zencloud-advisory | Commercial advisory site | https://www.zencloud.com.au/ | npm run build | dist | Active main-dev project |
| velocity-academy | Learning hub | https://velocity-academy.pages.dev/ | Static / Cloudflare Pages | root | Source updated; verify live deployment freshness |
| studiosix | Product/media studio | https://studiosix.com.au/ | npm run build | dist | Active |
| pmi-portal | PMO / delivery governance workspace | TBD | npm run build | dist | Confirm production URL |
| ea-artefact-generator | EA artefact tooling | https://ea.velocityarchitecture.com.au/ | npm run build | dist | Active |

## GitHub Pages Sites

| Repo | Role | Production URL | Deployment Model | Status |
|---|---|---|---|---|
| velocity-architecture | Framework authority | https://zencloudau.github.io/velocity-architecture/ | GitHub Pages static | Active |
| vaf-sa | Solution architecture method | https://zencloudau.github.io/vaf-sa/ | GitHub Pages static | Active |
| vsf-match | Career readiness tool | https://zencloudau.github.io/vsf-match/ | GitHub Actions Pages | Active; review generated asset strategy |
| trading-dashboard | Personal / educational trading lab | https://zencloudau.github.io/trading-dashboard/ | GitHub Pages static | Active lab asset |
| vaf-python-zero-to-hero | Python course | https://zencloudau.github.io/vaf-python-zero-to-hero/ | GitHub Pages static | Active course |
| vaf-typescript-zero-to-hero | TypeScript course | https://zencloudau.github.io/vaf-typescript-zero-to-hero/ | GitHub Pages / docs redirect | Active course |
| learn-with-claude | AI-assisted coding learning path | https://zencloudau.github.io/learn-with-claude/ | GitHub Pages static | Active |
| SAPEACertification | SAP EA certification study hub | https://zencloudau.github.io/SAPEACertification/ | GitHub Pages static | Active |
| AzureSACertification | Azure SA certification study hub | https://zencloudau.github.io/AzureSACertification/ | GitHub Pages static | Active |
| CISSPCertification | CISSP certification study hub | https://zencloudau.github.io/CISSPCertification/ | GitHub Pages static | Active |
| agentic-cert | Agentic AI certification hub | https://zencloudau.github.io/agentic-cert/ | GitHub Pages static | Active |

## Deployment Health Checks

For every repo:

- README has live URL
- GitHub About section has website URL
- repo description exists
- deployment model is known
- main branch is source of truth unless repo uses master
- no accidental node_modules committed
- no secrets committed
- no local-only Claude settings committed unless intentionally tracked
- generated build assets are either intentionally committed or excluded

## Known Follow-up Items

1. Confirm Cloudflare Pages production branch for velocity-academy.
2. Confirm whether velocity-academy deploys from root or build output.
3. Decide whether vsf-match should continue committing generated assets back to repo.
4. Standardise README deployment blocks across all repos.
5. Add consistent footer routing across public sites.
6. Confirm production URL and deployment target for pmi-portal.
7. Confirm Cloudflare build settings for zencloud-advisory before replacing the primary ZenCloud site.

## Execution Rule

Automation-first. Do not perform manual local edits unless explicitly requested. Deployment and workflow changes require a confidence threshold of at least 90%; otherwise pause and request verification.
