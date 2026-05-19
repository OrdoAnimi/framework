import { Anthropic } from '@anthropic-ai/sdk';
import { EARequest, Artefact, VAFFramework } from '../types/index';
import { logger } from '../logger';

const client = new Anthropic();

export const velocityAgent = {
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
            content: `Generate a Velocity Dashboard and Architectural Decision Log (ADL) index (VP4) for the following engagement:

Topic: ${request.topic}

Context: ${request.context || 'No additional context provided.'}

Constraints: ${request.constraints?.join(', ') || 'No constraints provided.'}

Requirements:
1. Follow the VP4 Velocity Viewpoint structure exactly
2. Generate both components: ADL Index and Velocity Dashboard as one combined artefact
3. Populate every field with content specific to the stated topic — no blank placeholders, no template variables
4. Apply the 14-Day Decision Aging Rule (CR-E1), ownership map (CR-O2), and expiry discipline (CR-X1)
5. Identify domain-specific decision areas and health signals relevant to this engagement context
6. Set a concrete velocity signal based on a realistic reading of the described context
7. Use forensic, control-surface tone — this is a command post, not a report
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
        id: `${request.id}-velocity`,
        type: 'velocity',
        content: content.text,
        metadata: {
          requestId: request.id,
          generatedBy: 'velocity-agent',
          timestamp: new Date(),
          vafVersion: '2.0.0',
          tokensUsed: response.usage.input_tokens + response.usage.output_tokens,
          validationPassed: false,
        },
      };

      logger.info(
        { requestId: request.id, type: artefact.type, tokens: artefact.metadata.tokensUsed, durationMs: Date.now() - startTime },
        'Velocity artefact generated'
      );

      return artefact;
    } catch (error) {
      logger.error(
        { requestId: request.id, error: error instanceof Error ? error.message : String(error) },
        'Velocity artefact generation failed'
      );
      throw error;
    }
  },
};

function buildSystemPrompt(framework: VAFFramework): string {
  return `You are the Velocity Agent for the Velocity Architecture Framework (VAF) v2.

Your role: Generate VP4 artefacts — the Architectural Decision Log (ADL) index and Velocity Dashboard — that make decision movement visible and governable for a specific engagement context.

## VAF Framework Context

### Framework Specification
${framework.spec.slice(0, 5000)}...

### Viewpoint 4: Velocity (Architectural Control)
${framework.viewpoints.vp4?.slice(0, 3000) || 'Not available'}...

### Correspondence Rules (Must Comply)
${framework.correspondenceRules.slice(0, 3000)}...

### Foundation Layer (Guiding Principles)
${framework.foundation.slice(0, 2000)}...

### Reference Instrument
${framework.examples.velocity?.slice(0, 2000) || 'Not available'}...

## Your Constraints

1. **Tone:** Forensic, control-surface. This is a command post reading, not a status update or report.
2. **Structure:** Always generate both the ADL Index and the Velocity Dashboard as a combined VP4 artefact.
3. **VAF Concepts:** Apply Decision Latency, 14-Day Decision Aging Rule (CR-E1), Ownership Map (CR-O2), and Expiry Discipline (CR-X1).
4. **No blank fields:** Every field must be populated with content derived from the topic and context. No YYYY-MM-DD placeholders, no empty cells.
5. **Output:** Valid Markdown only. No preamble. The artefact is your output.
6. **Context specificity:** Derive plausible, realistic domain-specific content from the topic and context. Name actual decision domains, realistic decision owners (by role), and concrete health signals for this type of engagement.

## Generation Rules

- Structure the ADL to reflect the architecture layers present in the stated context (enterprise, solution, technical).
- Identify 4–6 realistic decision domains from the topic and populate the heat map accordingly with domain-appropriate entries.
- Populate the Decision Velocity Metrics with plausible week-on-week readings that reflect a realistic engagement of this type.
- Set the velocity signal to a concrete level (High / Moderate / Low / Stalled) with a brief rationale.
- Name ownership gaps explicitly — state the role that should hold the decision, not "TBD".
- Populate the risk inventory with 2–3 realistic risks relevant to the stated engagement context.
- Identify at least one fitness function relevant to this engagement context.
- If you cannot generate a compliant artefact, explain why and fail loudly.`;
}
