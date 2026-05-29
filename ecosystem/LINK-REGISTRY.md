# Ecosystem Link Registry

Canonical URLs for all ZenCloud ecosystem repos. Source of truth for all cross-site links.

---

## Canonical URLs

| Repo | Canonical URL | Hosting | Status |
|------|--------------|---------|--------|
| velocity-architecture | `https://velocityarchitectureframework.com/` | Azure Container / Cloudflare | Live — custom domain |
| velocity-academy | `https://velocityarchitecture.com.au/` | GitHub Pages / Cloudflare | Live — custom domain |
| zencloud-advisory | `https://www.zencloud.com.au/` | Cloudflare Pages | Pending DNS cutover |
| studiosix | `https://studiosix.com.au/` | GitHub Pages / Cloudflare | Live — custom domain |
| ea-artefact-generator | `https://ea.velocityarchitecture.com.au/` | GitHub Pages / Cloudflare | Live — custom domain |
| vaf-sa | `https://zencloudau.github.io/vaf-sa/` | GitHub Pages | Live — GitHub Pages |
| vsf-match | `https://zencloudau.github.io/vsf-match/` | GitHub Pages | Live — GitHub Pages |
| vaf-python-zero-to-hero | `https://zencloudau.github.io/vaf-python-zero-to-hero/` | GitHub Pages | Live — GitHub Pages |
| vaf-typescript-zero-to-hero | `https://zencloudau.github.io/vaf-typescript-zero-to-hero/` | GitHub Pages | Live — GitHub Pages |
| AzureSACertification | `https://zencloudau.github.io/AzureSACertification/` | GitHub Pages | Live — GitHub Pages |
| SAPEACertification | `https://zencloudau.github.io/SAPEACertification/` | GitHub Pages | Live — GitHub Pages |
| CISSPCertification | `https://zencloudau.github.io/CISSPCertification/` | GitHub Pages | Live — GitHub Pages |
| learn-with-claude | `https://zencloudau.github.io/learn-with-claude/` | GitHub Pages | Live — GitHub Pages |
| trading-dashboard | `https://zencloudau.github.io/trading-dashboard/` | GitHub Pages | Live — GitHub Pages |
| pmi-portal | `https://zencloudau.github.io/pmi-portal/` | GitHub Pages | Live — GitHub Pages |

---

## VAF Agent Entry Point

The VAF Agentic Architect is accessed at:

```
https://velocityarchitectureframework.com/app/portal.html
```

All agent launch links (`Open agent ↗`, `VAF Agent ↗`, `Agentic Architect ↗`) must point to this URL — not the bare domain.

Site navigation back-links (`← VAF`, `VAF Framework ↗`, `Velocity Architecture Framework`) may link to the bare domain.

---

## Retired / Redirected URLs

These URLs are no longer canonical. Update all live links to the current canonical.

| Old URL | Redirects To |
|---------|-------------|
| `https://zencloudau.github.io/velocity-architecture/` | `https://velocityarchitectureframework.com/` |
| `https://zencloudau.github.io/velocity-academy/` | `https://velocityarchitecture.com.au/` |
| `https://velocity-academy.pages.dev/` | `https://velocityarchitecture.com.au/` |

---

## og: Meta Status

All public HTML entry points carry `og:url`, `og:title`, `og:description`.

| Repo | Entry Point | og:url | og:title | og:description |
|------|-------------|--------|----------|----------------|
| velocity-architecture | index.html | ✓ | ✓ | ✓ |
| velocity-academy | index.html | ✓ | ✓ | ✓ |
| zencloud-advisory | index.html | ✓ | ✓ | ✓ |
| studiosix | index.html | ✓ | ✓ | ✓ |
| ea-artefact-generator | index.html | ✓ | ✓ | ✓ |
| vaf-sa | index.html, toolkit.html, lexicon.html | ✓ | ✓ | ✓ |
| vsf-match | index.html, landing.html | ✓ | ✓ | ✓ |
| vaf-python-zero-to-hero | index.html, docs/index.html | ✓ | ✓ | ✓ |
| vaf-typescript-zero-to-hero | docs/index.html | ✓ | ✓ | ✓ |
| AzureSACertification | index.html | ✓ | ✓ | ✓ |
| SAPEACertification | index.html | ✓ | ✓ | ✓ |
| learn-with-claude | index.html | ✓ | ✓ | ✓ |
| trading-dashboard | index.html | ✓ | ✓ | ✓ |
| pmi-portal | index.html | ✓ | ✓ | ✓ |
| CISSPCertification | Jekyll — managed in _config.yml | — | — | — |

---

*Last audited: 2026-05-29. See CHANGE-PROTOCOL.md for update process.*
