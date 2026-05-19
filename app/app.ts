import dotenv from 'dotenv';
dotenv.config();

import express, { Express, Request, Response, NextFunction } from 'express';
import path from 'path';
import { orchestrator } from './orchestrator';
import { logger } from './logger';
import { EARequest } from './types/index';

const app: Express = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.use((req: Request, res: Response, next: NextFunction) => {
  logger.info({ method: req.method, path: req.path }, 'Incoming request');
  next();
});

// Serve portal at root
app.get('/', (req: Request, res: Response) => {
  res.sendFile(path.join(__dirname, 'portal.html'));
});

// Health check
app.get('/health', (req: Request, res: Response) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString(), version: '2.0.0' });
});

// Status
app.get('/status', (req: Request, res: Response) => {
  res.json({ status: 'operational', version: '2.0.0', environment: process.env.NODE_ENV || 'development', timestamp: new Date().toISOString() });
});

// Generate EA artefacts
app.post('/artefacts/generate', async (req: Request, res: Response) => {
  try {
    const { topic, context, constraints, requestedArtefacts, userId } = req.body;

    if (!topic) {
      res.status(400).json({ error: 'topic is required' });
      return;
    }

    const requestId = `req-${Date.now()}-${Math.random().toString(36).substring(7)}`;
    logger.info({ requestId, topic, userId: userId || 'anonymous' }, 'EA generation requested');

    const eaRequest: EARequest = {
      id: requestId,
      topic,
      context,
      constraints,
      requestedArtefacts: requestedArtefacts || ['governance', 'strategy', 'design', 'velocity', 'rhythm', 'practitioner'],
      userId: userId || 'anonymous',
      timestamp: new Date(),
    };

    const result = await orchestrator.execute(eaRequest);

    res.json({
      requestId: result.requestId,
      phase: result.phase,
      artefactCount: result.artefacts.length,
      artefacts: result.artefacts.map(a => ({
        id: a.id,
        type: a.type,
        metadata: a.metadata,
        contentPreview: a.content.slice(0, 1000),
        contentLength: a.content.length,
      })),
      errors: result.errors,
      duration: result.duration,
      timestamp: new Date().toISOString(),
    });
  } catch (error) {
    logger.error({ error }, 'Generation request failed');
    res.status(500).json({ error: 'Generation failed', message: error instanceof Error ? error.message : String(error) });
  }
});

// Retrieve artefact
app.get('/artefacts/:id', async (req: Request, res: Response) => {
  res.status(501).json({ error: 'Not implemented', message: 'Retrieve from GitHub directly' });
});

// 404
app.use((req: Request, res: Response) => {
  res.status(404).json({ error: 'Not found', path: req.path });
});

const server = app.listen(port, () => {
  logger.info({ port }, 'VAF Agentic Architect v2 listening');
});

process.on('SIGTERM', () => { server.close(() => process.exit(0)); });
process.on('SIGINT', () => { server.close(() => process.exit(0)); });

export default app;
