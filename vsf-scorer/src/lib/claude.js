// Claude API Integration — VSF Scoring
// ZenCloud Global Consultants

import { SCORING_GUIDE } from './scoring.js';

/**
 * Build the VSF scoring prompt for Claude
 */
function buildScoringPrompt(cvText, candidateName) {
  return `You are a senior architecture career analyst using the Velocity Success Factor (VSF) framework developed by ZenCloud Global Consultants.

Analyse this CV and score each professional engagement across 5 dimensions (1-10 each):

DIMENSIONS:
1. Scale of Impact (25%): Geographic reach, users/seats/sites affected, financial consequence, program breadth
2. Complexity Governed (25%): M&A, regulated industries, multi-vendor, live operations, technical debt, concurrent programs
3. Authority Held (20%): Decision-making level, ARB/governance forum role, sign-off responsibility, design authority function
4. Outcome Integrity (20%): Delivery completion, zero-disruption delivery, client satisfaction, clean handover
5. Capability Transferred (10%): Reusable patterns, frameworks built, standards set, team uplift, documentation quality

SCORING GUIDE:
${Object.entries(SCORING_GUIDE).map(([k, v]) => `${k}: ${v}`).join('\n')}

INSTRUCTIONS:
- Extract each distinct professional engagement chronologically
- Score all 5 dimensions for each engagement based strictly on evidence in the CV
- Do not inflate scores — score what is evidenced, not what is claimed without evidence
- Provide a concise one-line evidence note explaining the dimension scores
- Skip sabbaticals, career breaks, or gaps — mark them with null scores

Return ONLY valid JSON in this exact format. No preamble. No markdown. No explanation:
{
  "candidate": "${candidateName}",
  "engagements": [
    {
      "period": "2020-2025",
      "role": "Exact Role Title from CV",
      "org": "Organisation Name",
      "scale": 7,
      "complexity": 8,
      "authority": 9,
      "outcome": 8,
      "capability": 7,
      "note": "One line: specific evidence from CV that explains these scores"
    }
  ],
  "overall_assessment": "Two sentences: career trajectory from VSF perspective, peak operating level, and honest aggregate assessment."
}

CV TO ANALYSE:
${cvText}`;
}

/**
 * Score a CV using Claude API
 */
export async function scoreCV(cvText, candidateName) {
  const apiKey = import.meta.env.VITE_ANTHROPIC_API_KEY;

  if (!apiKey) {
    throw new Error('VITE_ANTHROPIC_API_KEY not set. Add your Anthropic API key to .env');
  }

  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
      "anthropic-version": "2023-06-01"
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 1000,
      messages: [{ role: "user", content: buildScoringPrompt(cvText, candidateName) }]
    })
  });

  if (!response.ok) {
    const err = await response.json().catch(() => ({}));
    throw new Error(err.error?.message || `API error: ${response.status}`);
  }

  const data = await response.json();
  const text = data.content
    ?.filter(b => b.type === "text")
    .map(b => b.text)
    .join("") || "";

  const clean = text.replace(/```json|```/g, "").trim();

  try {
    return JSON.parse(clean);
  } catch {
    throw new Error("Failed to parse scoring response. Raw output: " + text.substring(0, 200));
  }
}
