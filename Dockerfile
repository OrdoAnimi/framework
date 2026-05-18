# ── Stage 1: Build ──────────────────────────────────────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci --prefer-offline

COPY . .
RUN npm run build

# ── Stage 2: Runtime ─────────────────────────────────────────────────────────
FROM node:20-alpine

# Install nginx
RUN apk add --no-cache nginx

WORKDIR /app

# Copy compiled app and production deps
COPY --from=builder /app/dist       ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./

# nginx config — replaces Alpine default
COPY nginx.conf /etc/nginx/http.d/default.conf

# Remove Alpine's default nginx server block if present
RUN rm -f /etc/nginx/http.d/default.conf.bak 2>/dev/null || true

# Entrypoint
COPY start.sh /start.sh
RUN chmod +x /start.sh

# 80  — nginx (public, Cloudflare-proxied)
# 3000 — Express (internal only)
EXPOSE 80 3000

CMD ["/start.sh"]
