import { Anthropic } from '@anthropic-ai/sdk';
import { EARequest, Artefact, VAFFramework } from '../types/index';
import { logger } from '../logger';

const client = new Anthropic();

export const rhythmAgent = {
  async generate(request: EARequest, framework: VAFFramework): Promise<Artefact> {
    const startTime = Date.now();
    const systemPrompt = buildSystemPrompt(framework);

    try {
      const response = await client.messages.create({
        model: 'claude-sonnet-4-6',
        max_tokens: 4096,
        system: systemPrompt,
        messages: [
          {
            role: 'user',
            content: `Generate a Pulse System (VP5) for the following engagement:

Topic: ${request.topic}

Context: ${request.context || 'No additional context provided.'}

Constraints: ${request.constraints?.join(', ') || 'No constraints provided.'}

Requirements:
1. Follow the VP5 Rhythm Viewpoint structure exactly
2. Generate a complete Pulse System: Configuration, Pulse Briefing, Pulse Board structure, Pulse Report, Escalation Protocol, and context-specific Anti-Patterns
3. Populate every field with content specific to the stated topic — no blank placeholders, no template variables
4. Determine the appropriate Pulse tier (1/2/3) based on the described context and justify the choice
5. Identify the open decisions and questions most likely to appear in the first Pulse session for this engagement
6. Name context-specific anti-patterns that this type of engagement is most vulnerable to
7. Use operational, directive tone — this is a working governance system, not a concept document
8. Format as valid Markdown
9. Do not include preamble or explanation; output the artefact only`,
          },
        ],
      });

      const content = response.content[0];
      if (content.type !== 'text') {
        throw new Error('Unexpected response type from Claude');
      }

      const artefact: Artefact = {
        id: `${request.id}-rhythm`,
        type: 'rhythm',
        content: content.text,
        metadata: {
          requestId: request.id,
          generatedBy: 'rhythm-agent',
          timestamp: new Date(),
          vafVersion: '2.0.0',
          tokensUsed: response.usage.input_tokens + response.usage.output_tokens,
          validationPassed: false,
        },
      };

      logger.info(
        { requestId: request.id, type: artefact.type, tokens: artefact.metadata.tokensUsed, durationMs: Date.now() - startTime },
        'Rhythm artefact generated'
      );

      return artefact;
    } catch (error) {
      logger.error(
        { requestId: request.id, error: error instanceof Error ? error.message : String(error) },
        'Rhythm artefact generation failed'
      );
      throw error;
    }
  },
};

function buildSystemPrompt(framework: VAFFramework): string {
  return `You are the Rhythm Agent for the Velocity Architecture Framework (VAF) v2.

Your role: Generate VP5 artefacts — the Pulse System — that establish the operating governance cadence for a specific engagement. The Pulse System ensures ambiguity has a lifespan, not a permanent residency.

## VAF Framework Context

### Framework Specification
${framework.spec.slice(0, 5000)}...

### Viewpoint 5: Rhythm (Operating Cadence)
${framework.viewpoints.vp5?.slice(0, 3000) || 'Not available'}...

### Correspondence Rules (Must Comply)
${framework.correspondenceRules.slice(0, 3000)}...

### Foundation Layer (Guiding Principles)
${framework.foundation.slice(0, 2000)}...

### Reference Instrument
${framework.examples.rhythm?.slice(0, 2000) || 'Not available'}...

## Your Constraints

1. **Tone:** Operational, directive. Not conceptual — a working system ready to deploy from day one.
2. **Structure:** Always generate all five components: Pulse Configuration, Pulse Briefing (populated), Pulse Board, Pulse Report, and Escalation Protocol.
3. **VAF Concepts:** Apply Pulse tiers, escalation compression (CR-E2), terminal conditions (CR-E3), two-cycle maximum (CR-E4), and Pulse anti-patterns.
4. **No blank fields:** Every field must be populated with content derived from the topic and context. No YYYY-MM-DD placeholders, no empty rows.
5. **Output:** Valid Markdown only. No preamble. The artefact is your output.
6. **Context specificity:** The Pulse must feel designed for this specific engagement — not a generic governance template. Name the actual decision domains, realistic participant roles, and the specific questions most likely to arise for this type of work.

## Generation Rules

- Choose the correct Pulse tier based on the engagement scale and decision authority described in the context. State why.
- Populate the Pulse Briefing with 2–3 plausible open decisions and 1–2 approaching-expiry questions that reflect the stated topic.
- Design the Pulse Board for a realistic first session — include one aging decision, one new decision, and one escalation scenario.
- Populate the Pulse Report as if the first Pulse session has just completed — show decisions made, escalations triggered, and questions deferred with new expiry dates.
- Name 2–3 anti-patterns this specific engagement type is most likely to encounter, and state the response to each.
- The escalation protocol must name the tier above, the compressing condition, and the terminal binding point for this engagement.
- If you cannot generate a compliant artefact, explain why and fail loudly.`;
}
