FROM node:20-alpine

WORKDIR /app

# Copy package files and install ALL dependencies (including devDependencies for build)
COPY package*.json ./
RUN npm ci

# Copy source
COPY tsconfig.json ./
COPY app ./app

# Build TypeScript
RUN npm run build

# Remove devDependencies after build
RUN npm prune --production

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => { if (r.statusCode !== 200) throw new Error(r.statusCode) })"

EXPOSE 3000

CMD ["node", "dist/app/app.js"]
