// VSF Scorer — Main Component
// Velocity Success Factor™ by ZenCloud Global Consultants

import { useState } from "react";
import { scoreCV } from "./lib/claude.js";
import { calcVSF, getBenchmark, careerAggregate, peakEngagement, DIMENSIONS, BENCHMARKS } from "./lib/scoring.js";

const SAMPLE_CV = `Senior Solution Architect — 18 years experience

Principal Enterprise Architect | Global Technology Firm | 2021-2025
Led enterprise architecture governance across a portfolio of cloud transformation and legacy modernisation programs. Design Authority for a multi-vendor delivery environment. Presented to executive and board-level stakeholders. Governed architecture review board. Produced investment-grade artefacts through governance forums.

Lead Solution Architect | National Government Agency | 2018-2021
Lead architect for a state-wide digital transformation program. Designed target-state and transition architectures. Governed multi-agency delivery. Aligned to whole-of-government standards and frameworks.

Senior Solution Architect | Global Consulting Firm | 2014-2018
Senior architect across financial services, utilities, and mining clients. Led COTS platform evaluations, vendor governance, and architecture assurance. Delivered cloud migration programs across Azure and AWS. Mentored junior architects.

Solution Architect | Regional Technology Provider | 2010-2014
Solution architecture for mid-market clients. Cloud adoption, Microsoft 365 migrations, infrastructure modernisation. Led client workshops and produced architecture artefacts.

Systems Engineer | Government IT Department | 2006-2010
Senior systems engineer across government infrastructure. Led network and server upgrade programs. Technical lead for data centre consolidation.`;

export default function VSFScorer() {
  const [cvText, setCvText]           = useState(SAMPLE_CV);
  const [candidateName, setName]      = useState("Sample Candidate");
  const [results, setResults]         = useState(null);
  const [loading, setLoading]         = useState(false);
  const [error, setError]             = useState(null);
  const [selected, setSelected]       = useState(null);
  const [activeTab, setActiveTab]     = useState("heatmap");

  async function handleScore() {
    setLoading(true);
    setError(null);
    setResults(null);
    try {
      const raw = await scoreCV(cvText, candidateName);
      const engagements = raw.engagements.map(e => ({
        ...e,
        vsf: calcVSF({ scale: e.scale, complexity: e.complexity, authority: e.authority, outcome: e.outcome, capability: e.capability })
      }));
      const avg  = careerAggregate(engagements);
      const peak = peakEngagement(engagements);
      setResults({ ...raw, engagements, careerAvg: avg, peakEngagement: peak });
      setSelected(null);
      setActiveTab("heatmap");
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  function reset() { setResults(null); setSelected(null); setError(null); }

  const bm = results ? getBenchmark(results.careerAvg) : null;

  return (
    <div style={{ fontFamily: "'Georgia', serif", background: "#0a0d14", minHeight: "100vh", color: "#e8e4dc" }}>

      {/* Header */}
      <div style={{ background: "linear-gradient(135deg, #0d1929, #0a0d14)", borderBottom: "1px solid #2a3040", padding: "24px 40px" }}>
        <div style={{ fontSize: "10px", letterSpacing: "4px", color: "#e85820", marginBottom: "6px", fontFamily: "monospace" }}>
          ZENCLOUD GLOBAL CONSULTANTS
        </div>
        <h1 style={{ fontSize: "24px", fontWeight: "normal", margin: "0 0 4px", letterSpacing: "1px" }}>
          Velocity Success Factor™
        </h1>
        <div style={{ fontSize: "12px", color: "#8a9ab0" }}>
          Career value intelligence — score any CV across 5 dimensions of verified architectural value
        </div>
      </div>

      <div style={{ padding: "32px 40px", maxWidth: "1100px", margin: "0 auto" }}>

        {/* INPUT STATE */}
        {!results && (
          <div>
            <div style={{ display: "flex", gap: "16px", marginBottom: "16px", flexWrap: "wrap" }}>
              <div style={{ flex: "0 0 300px" }}>
                <label style={{ fontSize: "10px", letterSpacing: "2px", color: "#6a7a8a", display: "block", marginBottom: "6px" }}>
                  CANDIDATE NAME
                </label>
                <input value={candidateName} onChange={e => setName(e.target.value)}
                  style={{ width: "100%", background: "#0d1218", border: "1px solid #2a3040", color: "#e8e4dc", padding: "10px 14px", fontSize: "14px", fontFamily: "Georgia, serif", outline: "none", boxSizing: "border-box" }} />
              </div>
            </div>

            <label style={{ fontSize: "10px", letterSpacing: "2px", color: "#6a7a8a", display: "block", marginBottom: "6px" }}>
              PASTE CV TEXT
            </label>
            <textarea value={cvText} onChange={e => setCvText(e.target.value)} rows={14}
              style={{ width: "100%", background: "#0d1218", border: "1px solid #2a3040", color: "#e8e4dc", padding: "14px", fontSize: "13px", fontFamily: "monospace", outline: "none", resize: "vertical", lineHeight: "1.6", boxSizing: "border-box", marginBottom: "16px" }} />

            <div style={{ display: "flex", gap: "12px", alignItems: "center", marginBottom: "32px" }}>
              <button onClick={handleScore} disabled={loading || !cvText.trim()}
                style={{ background: loading ? "#2a3040" : "#e85820", color: "#fff", border: "none", padding: "14px 32px", fontSize: "11px", letterSpacing: "2px", cursor: loading ? "not-allowed" : "pointer", fontFamily: "monospace" }}>
                {loading ? "SCORING..." : "SCORE THIS CV"}
              </button>
              {loading && <span style={{ fontSize: "12px", color: "#6a7a8a" }}>Analysing engagements across 5 dimensions...</span>}
            </div>

            {error && <div style={{ color: "#e85820", fontSize: "13px", fontFamily: "monospace", marginBottom: "24px" }}>Error: {error}</div>}

            {/* Dimension cards */}
            <div style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: "10px" }}>
              {DIMENSIONS.map(d => (
                <div key={d.key} style={{ background: "#0d1218", border: "1px solid #2a3040", padding: "14px" }}>
                  <div style={{ fontSize: "9px", color: "#e85820", letterSpacing: "1px", marginBottom: "6px" }}>{d.weight} WEIGHT</div>
                  <div style={{ fontSize: "12px", color: "#e8e4dc", marginBottom: "4px" }}>{d.label}</div>
                  <div style={{ fontSize: "10px", color: "#6a7a8a" }}>{d.description}</div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* RESULTS STATE */}
        {results && (
          <div>
            {/* Summary */}
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: "20px" }}>
              <div>
                <div style={{ fontSize: "10px", color: "#e85820", letterSpacing: "3px", marginBottom: "6px", fontFamily: "monospace" }}>VSF PROFILE COMPLETE</div>
                <div style={{ fontSize: "22px", marginBottom: "6px" }}>{results.candidate}</div>
                <div style={{ fontSize: "13px", color: "#8a9ab0", maxWidth: "580px", lineHeight: "1.7" }}>{results.overall_assessment}</div>
              </div>
              <div style={{ textAlign: "right" }}>
                <div style={{ fontSize: "10px", color: "#8a9ab0", letterSpacing: "2px", marginBottom: "4px" }}>CAREER VSF</div>
                <div style={{ fontSize: "52px", fontWeight: "bold", color: "#e8a020", lineHeight: 1 }}>{results.careerAvg}</div>
                <div style={{ fontSize: "10px", color: "#6a7a8a" }}>/ 10.0</div>
                <div style={{ marginTop: "8px", fontSize: "10px", letterSpacing: "1px", color: bm.color, border: `1px solid ${bm.color}`, padding: "3px 10px", display: "inline-block" }}>
                  {bm.label.toUpperCase()}
                </div>
              </div>
            </div>

            {/* Stats */}
            <div style={{ display: "flex", gap: "24px", marginBottom: "20px", padding: "16px", background: "#0d1218", border: "1px solid #2a3040" }}>
              {[
                { label: "Peak VSF", value: results.peakEngagement?.vsf },
                { label: "Engagements Scored", value: results.engagements.length },
                { label: "Peak Role", value: results.peakEngagement?.role?.substring(0, 32) + "..." }
              ].map((s, i) => (
                <div key={i} style={{ borderLeft: i > 0 ? "1px solid #2a3040" : "none", paddingLeft: i > 0 ? "24px" : "0" }}>
                  <div style={{ fontSize: "18px", color: "#e8e4dc", fontWeight: "bold" }}>{s.value}</div>
                  <div style={{ fontSize: "10px", color: "#e85820", letterSpacing: "2px" }}>{s.label.toUpperCase()}</div>
                </div>
              ))}
            </div>

            {/* Tabs */}
            <div style={{ display: "flex", borderBottom: "1px solid #2a3040", marginBottom: "20px" }}>
              {[["heatmap","HEAT MAP"],["timeline","TIMELINE"],["detail","DETAIL"]].map(([v,l]) => (
                <button key={v} onClick={() => setActiveTab(v)}
                  style={{ background: activeTab===v?"#1a2535":"transparent", color: activeTab===v?"#e8a020":"#6a7a8a", border:"none", borderBottom: activeTab===v?"2px solid #e85820":"2px solid transparent", padding:"12px 20px", fontSize:"10px", letterSpacing:"2px", cursor:"pointer", fontFamily:"monospace" }}>
                  {l}
                </button>
              ))}
            </div>

            {/* Heat map */}
            {activeTab === "heatmap" && (
              <div>
                <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "8px" }}>
                  {results.engagements.map((e, i) => {
                    const intensity = e.vsf / 10;
                    const bg = `rgba(232,${Math.round(88+intensity*120)},${Math.round(32+intensity*40)},${0.1+intensity*0.6})`;
                    const isSel = selected === i;
                    return (
                      <div key={i} onClick={() => setSelected(isSel?null:i)}
                        style={{ background:bg, border: isSel?"2px solid #e85820":"1px solid #2a3040", padding:"14px", cursor:"pointer", borderRadius:"2px", minHeight:"80px" }}>
                        <div style={{ fontSize:"9px", color:"#8a9ab0", fontFamily:"monospace", marginBottom:"4px" }}>{e.period}</div>
                        <div style={{ fontSize:"26px", fontWeight:"bold", color:"#e8e4dc", lineHeight:1 }}>{e.vsf}</div>
                        <div style={{ fontSize:"9px", color:"#6a7a8a" }}>/ 10</div>
                        <div style={{ fontSize:"10px", color:"#8a9ab0", marginTop:"6px" }}>{e.role?.substring(0,28)}</div>
                      </div>
                    );
                  })}
                </div>

                {selected !== null && results.engagements[selected] && (() => {
                  const e = results.engagements[selected];
                  const eb = getBenchmark(e.vsf);
                  return (
                    <div style={{ marginTop:"16px", background:"#0d1929", border:"1px solid #2a3040", borderLeft:"4px solid #e85820", padding:"20px" }}>
                      <div style={{ display:"flex", justifyContent:"space-between", marginBottom:"12px" }}>
                        <div>
                          <div style={{ fontSize:"10px", color:"#e85820", fontFamily:"monospace", marginBottom:"4px" }}>{e.period}</div>
                          <div style={{ fontSize:"16px", marginBottom:"2px" }}>{e.role}</div>
                          <div style={{ fontSize:"12px", color:"#8a9ab0" }}>{e.org}</div>
                        </div>
                        <div style={{ textAlign:"right" }}>
                          <div style={{ fontSize:"36px", fontWeight:"bold", color:"#e8a020" }}>{e.vsf}</div>
                          <div style={{ fontSize:"10px", color:eb.color }}>{eb.label.toUpperCase()}</div>
                        </div>
                      </div>
                      <div style={{ display:"grid", gridTemplateColumns:"repeat(5,1fr)", gap:"8px", marginBottom:"12px" }}>
                        {DIMENSIONS.map(d => (
                          <div key={d.key} style={{ background:"#0a0d14", padding:"10px", textAlign:"center" }}>
                            <div style={{ fontSize:"8px", color:"#6a7a8a", marginBottom:"4px" }}>{d.label.substring(0,10).toUpperCase()}</div>
                            <div style={{ fontSize:"20px", fontWeight:"bold", color:"#e8e4dc" }}>{e[d.key]}</div>
                            <div style={{ height:"3px", background:"#1a2535", marginTop:"6px" }}>
                              <div style={{ height:"100%", width:`${e[d.key]*10}%`, background:"#e85820" }} />
                            </div>
                          </div>
                        ))}
                      </div>
                      <div style={{ fontSize:"12px", color:"#8a9ab0", fontStyle:"italic" }}>"{e.note}"</div>
                    </div>
                  );
                })()}
              </div>
            )}

            {/* Timeline */}
            {activeTab === "timeline" && (
              <div>
                {results.engagements.map((e, i) => {
                  const eb = getBenchmark(e.vsf);
                  return (
                    <div key={i} style={{ display:"flex", gap:"16px", marginBottom:"10px", alignItems:"center" }}>
                      <div style={{ width:"80px", fontSize:"10px", color:"#6a7a8a", fontFamily:"monospace", textAlign:"right", flexShrink:0 }}>{e.period}</div>
                      <div style={{ width:"10px", height:"10px", borderRadius:"50%", background:"#e85820", flexShrink:0 }} />
                      <div style={{ flex:1 }}>
                        <div style={{ display:"flex", alignItems:"center", gap:"10px" }}>
                          <div style={{ height:"22px", width:`${e.vsf*10}%`, minWidth:"40px", background:"linear-gradient(90deg,#e8582022,#e85820)", display:"flex", alignItems:"center", justifyContent:"flex-end", paddingRight:"8px" }}>
                            <span style={{ fontSize:"11px", fontWeight:"bold", color:"#e8e4dc" }}>{e.vsf}</span>
                          </div>
                          <span style={{ fontSize:"12px", color:"#8a9ab0" }}>{e.role}</span>
                        </div>
                        <div style={{ fontSize:"10px", color:"#4a5a6a", marginTop:"2px" }}>{e.org}</div>
                      </div>
                      <div style={{ fontSize:"9px", color:eb.color, width:"110px", textAlign:"right", flexShrink:0 }}>{eb.label.toUpperCase()}</div>
                    </div>
                  );
                })}
              </div>
            )}

            {/* Detail */}
            {activeTab === "detail" && (
              <div style={{ overflowX:"auto" }}>
                <table style={{ width:"100%", borderCollapse:"collapse", fontSize:"12px" }}>
                  <thead>
                    <tr>
                      {["Period / Role","VSF","Scale","Complexity","Authority","Outcome","Capability","Band"].map(h => (
                        <th key={h} style={{ background:"#0d1218", padding:"8px 10px", fontSize:"9px", color:"#6a7a8a", letterSpacing:"1px", textAlign:"left", border:"1px solid #2a3040" }}>{h.toUpperCase()}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {results.engagements.map((e, i) => {
                      const eb = getBenchmark(e.vsf);
                      return (
                        <tr key={i} style={{ background: i%2===0?"#0a0d14":"#0d1218" }}>
                          <td style={{ padding:"8px 10px", border:"1px solid #1a2535" }}>
                            <div style={{ fontSize:"9px", color:"#e85820", fontFamily:"monospace" }}>{e.period}</div>
                            <div style={{ fontSize:"11px", color:"#e8e4dc" }}>{e.role?.substring(0,28)}</div>
                          </td>
                          <td style={{ padding:"8px 10px", border:"1px solid #1a2535", textAlign:"center" }}>
                            <span style={{ fontSize:"16px", fontWeight:"bold", color:"#e8a020" }}>{e.vsf}</span>
                          </td>
                          {DIMENSIONS.map(d => (
                            <td key={d.key} style={{ padding:"8px 10px", border:"1px solid #1a2535", textAlign:"center" }}>
                              <div style={{ fontSize:"14px", color:"#e8e4dc" }}>{e[d.key]}</div>
                              <div style={{ height:"2px", background:"#1a2535", marginTop:"4px" }}>
                                <div style={{ height:"100%", width:`${e[d.key]*10}%`, background:"#e85820" }} />
                              </div>
                            </td>
                          ))}
                          <td style={{ padding:"8px 10px", border:"1px solid #1a2535" }}>
                            <span style={{ fontSize:"9px", color:eb.color }}>{eb.label.toUpperCase()}</span>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}

            {/* Benchmark bar */}
            <div style={{ marginTop:"24px", padding:"16px", background:"#0d1218", border:"1px solid #2a3040" }}>
              <div style={{ fontSize:"9px", color:"#6a7a8a", letterSpacing:"2px", marginBottom:"10px" }}>BENCHMARK SCALE</div>
              <div style={{ display:"flex", height:"12px", borderRadius:"2px", overflow:"hidden", marginBottom:"8px" }}>
                {BENCHMARKS.map((b,i) => <div key={i} style={{ flex:b.max-b.min, background:b.color, opacity:0.6 }} />)}
              </div>
              <div style={{ display:"flex" }}>
                {BENCHMARKS.map((b,i) => <div key={i} style={{ flex:b.max-b.min, fontSize:"8px", color:b.color }}>{b.label}</div>)}
              </div>
              <div style={{ marginTop:"10px", fontSize:"11px", color:"#8a9ab0" }}>
                Career average <span style={{ color:"#e8a020", fontWeight:"bold" }}>{results.careerAvg}</span> — <span style={{ color:bm.color }}>{bm.label}</span>
              </div>
            </div>

            <button onClick={reset}
              style={{ marginTop:"16px", background:"transparent", color:"#6a7a8a", border:"1px solid #2a3040", padding:"10px 20px", fontSize:"10px", letterSpacing:"2px", cursor:"pointer", fontFamily:"monospace" }}>
              ← SCORE ANOTHER CV
            </button>
          </div>
        )}
      </div>

      {/* Footer */}
      <div style={{ borderTop:"1px solid #2a3040", padding:"16px 40px", marginTop:"40px", display:"flex", justifyContent:"space-between", alignItems:"center" }}>
        <div style={{ fontSize:"10px", color:"#4a5a6a" }}>Velocity Success Factor™ is a ZenCloud Global Consultants framework.</div>
        <div style={{ fontSize:"10px", color:"#4a5a6a" }}>zencloud.com.au</div>
      </div>
    </div>
  );
}
