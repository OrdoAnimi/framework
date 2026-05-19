import { Anthropic } from '@anthropic-ai/sdk';
import { EARequest, Artefact, VAFFramework } from '../types/index';
import { logger } from '../logger';

const client = new Anthropic();

export const practitionerAgent = {
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
            content: `Generate an Integrity Arc assessment (VP6) for the practitioner operating in the following engagement:

Topic: ${request.topic}

Context: ${request.context || 'No additional context provided.'}

Constraints: ${request.constraints?.join(', ') || 'No constraints provided.'}

Requirements:
1. Follow the VP6 Practitioner Viewpoint structure exactly
2. Generate the complete Integrity Arc: all five positions assessed, Sacred Cows Register, Analytic Tests, and Velocity Signal
3. Assess each position (Authorship, Boundaries, Refusal, Staying, Exit) in the context of this specific engagement — state clearly what is present, what is absent, and what the conditions are
4. Populate the Sacred Cows Register with 2–4 beliefs specific to this type of engagement that protect dysfunction over clarity
5. Answer every Analytic Test question with a concrete, context-specific reading
6. Set the Velocity Signal to a specific level with a one-sentence rationale drawn from the engagement description
7. Use honest, direct, practitioner-to-practitioner tone — no hedging, no performance of professionalism
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
        id: `${request.id}-practitioner`,
        type: 'practitioner',
        content: content.text,
        metadata: {
          requestId: request.id,
          generatedBy: 'practitioner-agent',
          timestamp: new Date(),
          vafVersion: '2.0.0',
          tokensUsed: response.usage.input_tokens + response.usage.output_tokens,
          validationPassed: false,
        },
      };

      logger.info(
        { requestId: request.id, type: artefact.type, tokens: artefact.metadata.tokensUsed, durationMs: Date.now() - startTime },
        'Practitioner artefact generated'
      );

      return artefact;
    } catch (error) {
      logger.error(
        { requestId: request.id, error: error instanceof Error ? error.message : String(error) },
        'Practitioner artefact generation failed'
      );
      throw error;
    }
  },
};

function buildSystemPrompt(framework: VAFFramework): string {
  return `You are the Practitioner Agent for the Velocity Architecture Framework (VAF) v2.

Your role: Generate VP6 artefacts — the Integrity Arc — that assess the practitioner's position and establish what they are and are not accountable for in a specific engagement. This is the human layer of the framework.

## VAF Framework Context

### Framework Specification
${framework.spec.slice(0, 5000)}...

### Viewpoint 6: Practitioner (Human Layer)
${framework.viewpoints.vp6?.slice(0, 3000) || 'Not available'}...

### Correspondence Rules (Must Comply)
${framework.correspondenceRules.slice(0, 3000)}...

### Foundation Layer (Guiding Principles)
${framework.foundation.slice(0, 2000)}...

### Reference Instrument
${framework.examples.practitioner?.slice(0, 2000) || 'Not available'}...

## Your Constraints

1. **Tone:** Honest, direct, practitioner-to-practitioner. No hedging. No performance of professionalism. State what is true.
2. **Structure:** Always generate all sections: Engagement Context, all five arc positions assessed, Sacred Cows Register, Analytic Tests, and Velocity Signal.
3. **VAF Concepts:** Apply Authorship vs facilitation, Boundaries as written declarations, Refusal as a precise act, Staying as provisional assessment, Exit as a clean architectural decision.
4. **No blank fields:** Every field must be populated with content specific to the engagement. No "TBD" or template placeholders.
5. **Output:** Valid Markdown only. No preamble. The artefact is your output.
6. **Context specificity:** The assessment must read as specific to this type of engagement — not a generic integrity framework. Name the actual conditions, pressures, and sacred cows present in this kind of work.

## Generation Rules

- For each arc position, state clearly whether it is present or absent in this engagement context, and name the specific condition that determines this.
- For Authorship: identify whether the described context creates conditions for it or structurally prevents it, and state why.
- For Boundaries: write the scope declaration as if you are the practitioner — what you will and will not own.
- For Refusal: identify at least one specific piece of work this engagement is likely to demand that the practitioner should not produce without a prior decision.
- For Staying: assess the staying conditions honestly based on the engagement description. If the conditions for meaningful work are absent, say so.
- For Exit: assess whether exit conditions are approaching, reached, or not yet relevant. Do not soften this assessment.
- Sacred Cows Register: name the specific organisational beliefs in this type of engagement that will resist clarity. Be direct — these are the beliefs that protect dysfunction.
- Analytic Tests: answer each question with a concrete reading, not a neutral observation.
- Velocity Signal: set it to one of the four levels (High / Moderate / Low / Stalled) with a one-sentence rationale.
- If you cannot generate a compliant artefact, explain why and fail loudly.`;
}
