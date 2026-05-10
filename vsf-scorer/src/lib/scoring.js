// Velocity Success Factor™ — Scoring Engine
// ZenCloud Global Consultants

export const WEIGHTS = {
  scale: 0.25,
  complexity: 0.25,
  authority: 0.20,
  outcome: 0.20,
  capability: 0.10
};

export const DIMENSIONS = [
  {
    key: "scale",
    label: "Scale of Impact",
    weight: "25%",
    description: "Geographic reach, users/seats/sites affected, financial consequence, program breadth"
  },
  {
    key: "complexity",
    label: "Complexity Governed",
    weight: "25%",
    description: "M&A, regulated industries, multi-vendor, live operations, technical debt, concurrent programs"
  },
  {
    key: "authority",
    label: "Authority Held",
    weight: "20%",
    description: "Decision-making level, ARB/governance forum role, sign-off responsibility, design authority function"
  },
  {
    key: "outcome",
    label: "Outcome Integrity",
    weight: "20%",
    description: "Delivery completion, zero-disruption delivery, client satisfaction, clean handover"
  },
  {
    key: "capability",
    label: "Capability Transferred",
    weight: "10%",
    description: "Reusable patterns, frameworks built, standards set, team uplift, documentation quality"
  }
];

export const BENCHMARKS = [
  { label: "Graduate / Junior EA", min: 0,   max: 4.5,  color: "#4a5568" },
  { label: "Mid-level SA",         min: 4.5,  max: 6.0,  color: "#2d6a9f" },
  { label: "Senior SA",            min: 6.0,  max: 7.5,  color: "#2d9f7a" },
  { label: "Principal / Lead EA",  min: 7.5,  max: 8.5,  color: "#9f7a2d" },
  { label: "Chief Architect",      min: 8.5,  max: 10.1, color: "#e85820" }
];

export const SCORING_GUIDE = {
  "1-2": "Entry level / no evidence",
  "3-4": "Mid-level practitioner",
  "5-6": "Senior practitioner",
  "7-8": "Principal / Lead level",
  "9-10": "Chief Architect / Global scale"
};

/**
 * Calculate VSF score for a single engagement
 */
export function calcVSF(scores) {
  return +(
    scores.scale    * WEIGHTS.scale +
    scores.complexity * WEIGHTS.complexity +
    scores.authority  * WEIGHTS.authority +
    scores.outcome    * WEIGHTS.outcome +
    scores.capability * WEIGHTS.capability
  ).toFixed(2);
}

/**
 * Get benchmark band for a VSF score
 */
export function getBenchmark(vsf) {
  return BENCHMARKS.find(b => vsf >= b.min && vsf < b.max) || BENCHMARKS[BENCHMARKS.length - 1];
}

/**
 * Calculate career aggregate VSF
 */
export function careerAggregate(engagements) {
  const valid = engagements.filter(e => e.vsf !== null && e.vsf !== undefined);
  if (!valid.length) return 0;
  return +(valid.reduce((s, e) => s + e.vsf, 0) / valid.length).toFixed(2);
}

/**
 * Find peak engagement
 */
export function peakEngagement(engagements) {
  const valid = engagements.filter(e => e.vsf !== null && e.vsf !== undefined);
  return valid.reduce((peak, e) => e.vsf > (peak?.vsf || 0) ? e : peak, null);
}
