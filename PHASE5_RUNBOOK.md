# Phase 5.1 — Port 80 + HTTPS via Cloudflare
## Runbook

---

### Step 1 — Deploy the code changes

Commit and push to main:
- `Dockerfile` (nginx added, ports 80 + 3000 exposed)
- `nginx.conf` (reverse proxy 80 → localhost:3000)
- `start.sh` (boots nginx then node)
- `.github/workflows/deploy.yml` (port 80 added to ACI)

GitHub Actions will rebuild and redeploy automatically.
Confirm container is up:
```
az container show --resource-group vaf-rg --name vaf-agentic-architect --query "instanceView.state" -o tsv
```
Test port 80 directly before touching DNS:
```
curl -I http://20.190.118.105
```
Expected: HTTP 200 from nginx.

---

### Step 2 — Add site to Cloudflare

1. Go to https://dash.cloudflare.com → Add a Site
2. Enter: `velocityarchitectureframework.com`
3. Select plan: **Free**
4. Cloudflare will scan existing DNS records — it will find the A record pointing to `20.190.118.105`
5. Confirm the A record is present and **orange-cloud (Proxied)** is enabled
6. Note the two Cloudflare nameservers assigned (e.g. `aria.ns.cloudflare.com`, `bob.ns.cloudflare.com`)

---

### Step 3 — Update GoDaddy nameservers

1. Log in to GoDaddy → My Products → velocityarchitectureframework.com → DNS
2. Scroll to **Nameservers** → Change → Custom
3. Enter both Cloudflare nameservers from Step 2
4. Save

Propagation: 5–30 minutes. Cloudflare dashboard will confirm when active.

---

### Step 4 — Cloudflare DNS record (confirm)

In Cloudflare dashboard → DNS → Records:

| Type | Name | Content        | Proxy status |
|------|------|----------------|--------------|
| A    | @    | 20.190.118.105 | Proxied ✅   |

If the record is showing Unproxied (grey cloud), click edit and toggle to Proxied.

---

### Step 5 — SSL/TLS settings

Cloudflare dashboard → SSL/TLS → Overview:
- Set encryption mode to **Flexible** (origin is HTTP only, no cert on ACI)

Cloudflare dashboard → SSL/TLS → Edge Certificates:
- **Always Use HTTPS**: ON
- **Minimum TLS Version**: TLS 1.2
- **Automatic HTTPS Rewrites**: ON

---

### Step 6 — Verify

```
curl -I https://velocityarchitectureframework.com
```
Expected:
- HTTP/2 200
- `server: cloudflare`
- No port suffix in URL

Portal accessible at:
- https://velocityarchitectureframework.com (Cloudflare SSL, proxied)
- http://20.190.118.105 (direct, still works for admin/debug)
- http://20.190.118.105:3000 (Express direct, internal — can be locked down in Phase 5.2)

---

### Notes

- Port 3000 on the Azure IP remains accessible directly. Lock it down in Phase 5.2 (auth) or via Azure NSG rule.
- Cloudflare proxied mode hides the origin IP — standard DDoS and bot protection included on free plan.
- Do not add an HTTPS origin cert until Phase 5 advanced (origin pull cert or Azure App Gateway). Flexible SSL is correct for this topology.
