import { Anthropic } from '@anthropic-ai/sdk';
import { EARequest, TaskPlan, OrchestratorState, Artefact, VAFFramework } from './types/index';
import { governanceAgent } from './agents/governance-agent';
import { strategyAgent } from './agents/strategy-agent';
import { designAgent } from './agents/design-agent';
import { velocityAgent } from './agents/velocity-agent';
import { rhythmAgent } from './agents/rhythm-agent';
import { practitionerAgent } from './agents/practitioner-agent';
import { validationAgent } from './agents/validation-agent';
import { actionEngine } from './action-engine';
import { loadVAFFramework } from './kb-loader';
import { logger } from './logger';

class Orchestrator {
  private client = new Anthropic();
  private framework: VAFFramework | null = null;

  async execute(request: EARequest): Promise<OrchestratorState> {
    const state: OrchestratorState = {
      requestId: request.id,
      phase: 'planning',
      artefacts: [],
      errors: [],
      startTime: new Date(),
    };

    try {
      logger.info({ requestId: request.id }, 'Phase: Loading VAF Framework');
      if (!this.framework) {
        this.framework = await loadVAFFramework();
      }

      logger.info({ requestId: request.id }, 'Phase: Planning');
      state.phase = 'planning';
      const plan = await this.createPlan(request);

      if (!plan || !plan.artefactsNeeded || plan.artefactsNeeded.length === 0) {
        state.errors.push('Planning failed: no artefacts identified');
        state.phase = 'failed';
        return state;
      }

      logger.info({ requestId: request.id, artefactsNeeded: plan.artefactsNeeded }, 'Phase: Generation');
      state.phase = 'generation';

      const results = await Promise.all(
        plan.artefactsNeeded.map(async (artefactType) => {
          try {
            return await this.generateArtefact(request, artefactType);
          } catch (error) {
            state.errors.push(`Generation failed for ${artefactType}: ${error instanceof Error ? error.message : String(error)}`);
            return null;
          }
        })
      );
      state.artefacts = results.filter((a): a is NonNullable<typeof a> => a !== null);

      if (state.artefacts.length === 0) {
        state.phase = 'failed';
        return state;
      }

      logger.info({ requestId: request.id, artefactCount: state.artefacts.length }, 'Phase: Validation');
      state.phase = 'validation';

      for (const artefact of state.artefacts) {
        try {
          const isValid = await validationAgent.validate(artefact, this.framework, state.artefacts);
          if (!isValid) {
            state.errors.push(`Validation failed for ${artefact.type}`);
          }
        } catch (error) {
          state.errors.push(`Validation error for ${artefact.type}: ${error instanceof Error ? error.message : String(error)}`);
        }
      }

      logger.info({ requestId: request.id, artefactCount: state.artefacts.length }, 'Phase: Publishing');
      state.phase = 'publishing';

      for (const artefact of state.artefacts) {
        try {
          const result = await actionEngine.commitArtefact(request.id, artefact);
          logger.info(
            { requestId: request.id, type: artefact.type, sha: result.sha, url: result.url },
            'Artefact committed to GitHub'
          );
        } catch (error) {
          state.errors.push(`Commit failed for ${artefact.type}: ${error instanceof Error ? error.message : String(error)}`);
        }
      }

      state.phase = 'complete';
      state.endTime = new Date();
      state.duration = state.endTime.getTime() - state.startTime.getTime();

      logger.info(
        { requestId: request.id, artefactCount: state.artefacts.length, durationMs: state.duration, errors: state.errors.length },
        'Request complete'
      );

      return state;
    } catch (error) {
      state.phase = 'failed';
      state.errors.push(`Orchestration failed: ${error instanceof Error ? error.message : String(error)}`);
      state.endTime = new Date();
      state.duration = state.endTime.getTime() - state.startTime.getTime();
      logger.error({ requestId: request.id, error, duration: state.duration }, 'Request failed');
      return state;
    }
  }

  private async createPlan(request: EARequest): Promise<TaskPlan> {
    try {
      const requestedArtefacts = request.requestedArtefacts || ['governance', 'strategy', 'design', 'velocity', 'rhythm', 'practitioner'];
      const plan: TaskPlan = {
        requestId: request.id,
        artefactsNeeded: requestedArtefacts,
        validationRules: ['structure', 'tone', 'alignment', 'vaf-concepts'],
        sequenceOrder: ['governance', 'strategy', 'design', 'velocity', 'rhythm', 'practitioner'],
      };
      return plan;
    } catch (error) {
      logger.error({ error }, 'Plan creation failed');
      throw error;
    }
  }

  private async generateArtefact(request: EARequest, type: string): Promise<Artefact | null> {
    if (!this.framework) throw new Error('VAF framework not loaded');

    switch (type) {
      case 'governance':   return governanceAgent.generate(request, this.framework);
      case 'strategy':     return strategyAgent.generate(request, this.framework);
      case 'design':       return designAgent.generate(request, this.framework);
      case 'velocity':     return velocityAgent.generate(request, this.framework);
      case 'rhythm':       return rhythmAgent.generate(request, this.framework);
      case 'practitioner': return practitionerAgent.generate(request, this.framework);
      default:
        logger.warn({ type }, 'Unknown artefact type');
        return null;
    }
  }
}

export const orchestrator = new Orchestrator();
