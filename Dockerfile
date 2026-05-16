FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY tsconfig.json ./
COPY app ./app

RUN npm run build

RUN cp app/portal.html dist/app/portal.html

RUN npm prune --production

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => { if (r.statusCode !== 200) throw new Error(r.statusCode) })"

EXPOSE 3000

CMD ["node", "dist/app/app.js"]
