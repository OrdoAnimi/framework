# ── Stage 1: Build ──────────────────────────────────────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci --prefer-offline

COPY . .
RUN npm run build

# Copy non-TS assets that tsc doesn't move
RUN cp app/portal.html dist/app/portal.html

# ── Stage 2: Runtime ─────────────────────────────────────────────────────────
FROM node:20-alpine

# Install nginx
RUN apk add --no-cache nginx

WORKDIR /app

# Copy compiled app and production deps
COPY --from=builder /app/dist       ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./

# nginx config
COPY nginx.conf /etc/nginx/http.d/default.conf

# Entrypoint
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80 3000

CMD ["/start.sh"]