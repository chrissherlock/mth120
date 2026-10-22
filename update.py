#!/usr/bin/env python3
import sys

def apply_patch():
    try:
        with open("week2-lecture5.html", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: week2-lecture5.html not found.")
        sys.exit(1)

    old_section = """            <!-- SECTION 1 -->
            <h2 id="section-mct">1. The Monotone Convergence Theorem</h2>
            <p>While the formal $\\epsilon\\text{-}N$ definition lets us <em>verify</em> a limit when we already know its value, how do we prove a limit exists when the value is unknown? The answer lies in monotonic behavior.</p>

            <div class="definition-box">
                <strong>Proposition 6:</strong> Let $S \\subset \\mathbb{R}$ be a non-empty bounded set and $\\alpha = \\sup S$. Then there exists an increasing sequence $(a_n)$ of elements in $S$ that converges to $\\alpha$.<br>
                <em>Proof:</em> For each $n \\ge 1$, $\\alpha - \\frac{1}{n} < \\alpha$. Since $\\alpha$ is the least upper bound, $\\alpha - \\frac{1}{n}$ cannot be an upper bound for $S$. Hence, there exists $a_n \\in S$ such that $\\alpha - \\frac{1}{n} < a_n \\le \\alpha$. As $n \\to \\infty$, the Squeeze Theorem yields $a_n \\to \\alpha$.
            </div>

            <div class="infobox" style="margin-top: 1.5rem;">
                <h4>📈 Theorem 2: The Monotone Convergence Theorem (MCT)</h4>
                <div class="infobox-intro">
                    Every bounded monotonic sequence of real numbers converges.
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.95rem;">
                    <div style="padding-bottom: 0.5rem; border-bottom: 1px solid #e2e8f0;">
                        <strong>1. Non-Decreasing:</strong> If $(a_n)$ is non-decreasing ($a_n \\le a_{n+1}$) and bounded above, then $(a_n)$ converges, and:
                        <p style="text-align: center; margin: 0.5rem 0;">$$\\lim_{n\\to\\infty} a_n = \\sup \\{a_n : n \\in \\mathbb{N}\\}$$</p>
                    </div>
                    <div>
                        <strong>2. Non-Increasing:</strong> If $(a_n)$ is non-increasing ($a_n \\ge a_{n+1}$) and bounded below, then $(a_n)$ converges, and:
                        <p style="text-align: center; margin: 0.5rem 0;">$$\\lim_{n\\to\\infty} a_n = \\inf \\{a_n : n \\in \\mathbb{N}\\}$$</p>
                    </div>
                </div>
            </div>

            <div class="worked-example-box">
                <h4>🎯 Formal Proof of the Monotone Convergence Theorem</h4>
                <p>Let $(a_n)$ be increasing and bounded above. Define the set of values $S = \\{a_n : n \\ge 1\\}$.</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li>By the Completeness Axiom of $\\mathbb{R}$, $S$ possesses a supremum: $\\alpha = \\sup S$.</li>
                    <li>Let $\\epsilon > 0$. Then $\\alpha - \\epsilon < \\alpha$, so $\\alpha - \\epsilon$ is not an upper bound of $S$.</li>
                    <li>Thus, there exists an index $N$ such that $\\alpha - \\epsilon < a_N \\le \\alpha$.</li>
                    <li>Because $(a_n)$ is increasing, for any $n > N$ we have $a_n \\ge a_N$. Hence:
                        $$\\alpha - \\epsilon < a_N \\le a_n \\le \\alpha < \\alpha + \\epsilon \\implies |a_n - \\alpha| < \\epsilon$$
                    </li>
                    <li>Therefore, $\\lim_{n\\to\\infty} a_n = \\alpha = \\sup \\{a_n\\}$. $\\blacksquare$</li>
                </ol>
            </div>"""

    new_section = """            <!-- SECTION 1: THE MONOTONE CONVERGENCE THEOREM -->
            <h2 id="section-mct">1. The Monotone Convergence Theorem (The Escape Hatch)</h2>

            <h3 style="color: #0f172a; margin-top: 1.5rem;">Why We Need It: Proving Convergence Blind</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                In Lecture 4, you mastered the $\\epsilon\\text{-}N$ game. But that game has a glaring prerequisite: <strong>you must already know the exact value of the limit $L$ before you can prove it</strong>. You can't set up the distance $|a_n - L| < \\epsilon$ if $L$ is a mystery.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                What happens when you encounter a sequence defined by a bizarre recursive formula or an infinite sum, and you have absolutely no idea what number it approaches? This is where the <strong>Monotone Convergence Theorem (MCT)</strong> acts as your mathematical escape hatch. It allows you to definitively prove a sequence converges <em>without ever knowing what it converges to</em>.
            </p>

            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #0284c7; border-radius: 8px; padding: 1.25rem 1.5rem; margin: 1.5rem 0;">
                <div style="color: #0284c7; margin: 0 0 0.5rem 0; font-size: 0.92rem; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700;">
                    The Physical Intuition: Two Opposing Forces
                </div>
                <p style="margin: 0; color: #334155; line-height: 1.6;">
                    Imagine a sequence as a machine operating under two strict physical laws:
                </p>
                <ul style="padding-left: 1.25rem; margin: 0.5rem 0 0 0; color: #334155; line-height: 1.7;">
                    <li style="margin-bottom: 0.5rem;">
                        <strong>The Engine (Monotonicity):</strong> The sequence is strictly <em>increasing</em>. Every new term steps higher than the last. It never reverses direction.
                    </li>
                    <li>
                        <strong>The Glass Ceiling (Boundedness):</strong> There is a hard, impenetrable ceiling (an upper bound $M$) that the sequence is mathematically forbidden from crossing.
                    </li>
                </ul>
                <p style="margin: 1rem 0 0 0; color: #334155; line-height: 1.6;">
                    If an engine pushes upward forever, but is physically trapped beneath a ceiling, it cannot escape to infinity, and it cannot retreat. It has only one option: it must eventually crush flat against a final barrier.
                </p>
            </div>

            <div class="infobox" style="margin-top: 2rem;">
                <h4>📈 Theorem 2: The Monotone Convergence Theorem (MCT)</h4>
                <div class="infobox-intro">
                    Every bounded monotonic sequence of real numbers converges.
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.95rem;">
                    <div style="padding-bottom: 0.5rem; border-bottom: 1px solid #e2e8f0;">
                        <strong>1. Non-Decreasing:</strong> If $(a_n)$ is non-decreasing ($a_n \\le a_{n+1}$) and bounded above, then $(a_n)$ converges to the <em>least upper bound</em> (supremum) of its terms:
                        <p style="text-align: center; margin: 0.75rem 0; font-size: 1.15rem;">$$\\lim_{n\\to\\infty} a_n = \\sup \\{a_n : n \\in \\mathbb{N}\\}$$</p>
                    </div>
                    <div>
                        <strong>2. Non-Increasing:</strong> If $(a_n)$ is non-increasing ($a_n \\ge a_{n+1}$) and bounded below, then $(a_n)$ converges to the <em>greatest lower bound</em> (infimum) of its terms:
                        <p style="text-align: center; margin: 0.75rem 0; font-size: 1.15rem;">$$\\lim_{n\\to\\infty} a_n = \\inf \\{a_n : n \\in \\mathbb{N}\\}$$</p>
                    </div>
                </div>
            </div>

            <!-- ================================================================= -->
            <!-- INTERACTIVE WIDGET: THE MONOTONE CONVERGENCE THEOREM PROOF        -->
            <!-- ================================================================= -->
            <div class="widget-box" id="mct-proof-widget" style="margin: 2.5rem 0; padding: 1.5rem; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
                <style>
                    #mct-proof-widget .widget-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.25rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.85rem; }
                    #mct-proof-widget .widget-title { margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; letter-spacing: -0.01em; }

                    #mct-proof-widget .telemetry-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.65rem; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.75rem; margin-bottom: 1.25rem; }
                    #mct-proof-widget .telemetry-cell { display: flex; flex-direction: column; gap: 0.2rem; }
                    #mct-proof-widget .telemetry-label { font-size: 0.72rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.04em; }
                    #mct-proof-widget .telemetry-val { font-size: 0.88rem; font-weight: 700; color: #0f172a; font-variant-numeric: tabular-nums; }

                    #mct-proof-widget .canvas-wrap { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.5rem; margin-bottom: 1.25rem; overflow: hidden; position: relative; }
                    #mct-proof-widget svg { display: block; width: 100%; height: auto; }

                    /* Navigation & Inline Preview */
                    #mct-proof-widget .nav-panel { display: grid; grid-template-columns: auto 1fr; align-items: center; gap: 1.25rem; background: #f1f5f9; border-radius: 8px; padding: 0.85rem 1.15rem; margin-bottom: 1.25rem; }
                    @media (max-width: 680px) { #mct-proof-widget .nav-panel { grid-template-columns: 1fr; } }
                    #mct-proof-widget .nav-buttons { display: flex; gap: 0.5rem; flex-shrink: 0; white-space: nowrap; }
                    #mct-proof-widget .mct-btn { padding: 0.45rem 0.9rem; font-size: 0.85rem; font-weight: 600; border-radius: 6px; border: 1px solid #cbd5e1; background: #ffffff; color: #334155; cursor: pointer; transition: all 0.15s ease; }
                    #mct-proof-widget .mct-btn:hover:not(:disabled) { background: #f8fafc; border-color: #94a3b8; }
                    #mct-proof-widget .mct-btn:disabled { opacity: 0.45; cursor: not-allowed; }
                    #mct-proof-widget .mct-btn-primary { background: #0284c7; color: #ffffff; border-color: #0284c7; }
                    #mct-proof-widget .mct-btn-primary:hover:not(:disabled) { background: #0369a1; border-color: #0369a1; }
                    #mct-proof-widget .preview-desc { margin: 0; font-size: 0.9rem; line-height: 1.5; color: #334155; min-width: 0; border-left: 3px solid #0284c7; padding-left: 0.85rem; }

                    /* Paired Analytical Panes */
                    #mct-proof-widget .panes-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; }
                    #mct-proof-widget .mct-pane { border-radius: 8px; padding: 1rem; border: 1px solid #e2e8f0; }
                    #mct-proof-widget .mct-pane-what { background: #f0fdf4; border-color: #bbf7d0; border-left: 4px solid #16a34a; }
                    #mct-proof-widget .mct-pane-why { background: #eff6ff; border-color: #bfdbfe; border-left: 4px solid #2563eb; }
                    #mct-proof-widget .mct-pane h4 { margin: 0 0 0.4rem 0; font-size: 0.82rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; }
                    #mct-proof-widget .mct-pane-what h4 { color: #15803d; }
                    #mct-proof-widget .mct-pane-why h4 { color: #1d4ed8; }
                    #mct-proof-widget .mct-pane-body { font-size: 0.88rem; line-height: 1.6; color: #1e293b; min-height: 4.5rem; }

                    /* SVG Animation Classes */
                    .mct-anim { transition: opacity 0.4s ease, transform 0.4s ease; }
                    .mct-hidden { opacity: 0; pointer-events: none; }
                    .mct-visible { opacity: 1; pointer-events: auto; }
                </style>

                <div class="widget-header">
                    <h3 class="widget-title">Interactive Proof: Trapping the Supremum</h3>
                </div>

                <!-- LIVE STATE TELEMETRY -->
                <div class="telemetry-grid">
                    <div class="telemetry-cell">
                        <span class="telemetry-label">Active Phase</span>
                        <span id="mct-tel-phase" class="telemetry-val">0: The Physical Setup</span>
                    </div>
                    <div class="telemetry-cell">
                        <span class="telemetry-label">Supremum Boundary</span>
                        <span id="mct-tel-sup" class="telemetry-val" style="color: #0284c7;">α = sup(S)</span>
                    </div>
                    <div class="telemetry-cell">
                        <span class="telemetry-label">Challenge Corridor</span>
                        <span id="mct-tel-eps" class="telemetry-val" style="color: #d97706;">Pending</span>
                    </div>
                    <div class="telemetry-cell">
                        <span class="telemetry-label">Milestone Target</span>
                        <span id="mct-tel-n" class="telemetry-val" style="color: #0f172a;">Pending</span>
                    </div>
                    <div class="telemetry-cell">
                        <span class="telemetry-label">Tail Status</span>
                        <span id="mct-tel-status" class="telemetry-val" style="color: #64748b;">Bounded &amp; Rising</span>
                    </div>
                </div>

                <!-- SYNCHRONIZED VISUAL CANVAS (SVG) -->
                <div class="canvas-wrap">
                    <svg id="mct-svg" viewBox="0 0 800 340">
                        <defs>
                            <marker id="mct-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto-start-reverse">
                                <path d="M 0 2 L 7 5 L 0 8 z" fill="#64748b"/>
                            </marker>
                            <pattern id="mct-hatch-red" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
                                <line x1="0" y1="0" x2="0" y2="8" stroke="#f87171" stroke-width="1.5" stroke-opacity="0.6" />
                            </pattern>
                        </defs>

                        <!-- Background Grid -->
                        <g stroke="#f1f5f9" stroke-width="1">
                            <line x1="80" y1="40" x2="720" y2="40"/>
                            <line x1="80" y1="90" x2="720" y2="90"/>
                            <line x1="80" y1="140" x2="720" y2="140"/>
                            <line x1="80" y1="190" x2="720" y2="190"/>
                            <line x1="80" y1="240" x2="720" y2="240"/>
                            <line x1="120" y1="20" x2="120" y2="280"/>
                            <line x1="200" y1="20" x2="200" y2="280"/>
                            <line x1="280" y1="20" x2="280" y2="280"/>
                            <line x1="360" y1="20" x2="360" y2="280"/>
                            <line x1="440" y1="20" x2="440" y2="280"/>
                            <line x1="520" y1="20" x2="520" y2="280"/>
                            <line x1="600" y1="20" x2="600" y2="280"/>
                            <line x1="680" y1="20" x2="680" y2="280"/>
                        </g>

                        <!-- Axes -->
                        <line x1="80" y1="280" x2="740" y2="280" stroke="#94a3b8" stroke-width="1.2" marker-end="url(#mct-arr)"/>
                        <text x="750" y="284" font-size="10" font-weight="700" fill="#475569">Index n</text>
                        <line x1="80" y1="280" x2="80" y2="20" stroke="#94a3b8" stroke-width="1.2" marker-end="url(#mct-arr)"/>
                        <text x="45" y="20" font-size="10" font-weight="700" fill="#475569">Value</text>

                        <!-- LAYER 0: The Setup (Ceiling and Sequence) -->
                        <g id="mct-layer-setup">
                            <!-- Upper Bound M (Higher than supremum) -->
                            <line x1="80" y1="40" x2="720" y2="40" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 3"/>
                            <text x="730" y="44" font-size="10" font-weight="600" fill="#64748b">Bound M</text>

                            <!-- Supremum Line α (The TRUE ceiling) -->
                            <line x1="80" y1="70" x2="720" y2="70" stroke="#0284c7" stroke-width="2"/>
                            <text x="730" y="74" font-size="11.5" font-weight="800" fill="#0284c7">Supremum α</text>

                            <!-- Monotonic Sequence Points -->
                            <!-- Values curve asymptotically toward y=70 from y=240 -->
                            <polyline points="120,240 180,180 240,140 300,115 360,100 420,90 480,83 540,78 600,75 660,73" fill="none" stroke="#93c5fd" stroke-width="1.5"/>

                            <g id="mct-pts" fill="#0284c7" stroke="#ffffff" stroke-width="1">
                                <circle cx="120" cy="240" r="4.5"/>
                                <circle cx="180" cy="180" r="4.5"/>
                                <circle cx="240" cy="140" r="4.5"/>
                                <circle cx="300" cy="115" r="4.5"/>
                                <circle cx="360" cy="100" r="4.5"/>
                                <circle cx="420" cy="90" r="4.5"/>
                                <circle cx="480" cy="83" r="4.5"/>
                                <circle cx="540" cy="78" r="4.5"/>
                                <circle cx="600" cy="75" r="4.5"/>
                                <circle cx="660" cy="73" r="4.5"/>
                            </g>
                        </g>

                        <!-- LAYER 1: The Challenge (Epsilon Corridor) -->
                        <g id="mct-layer-eps" class="mct-anim mct-hidden">
                            <!-- Corridor Background -->
                            <rect x="80" y="70" width="640" height="50" fill="#fef3c7" fill-opacity="0.6"/>
                            <!-- Epsilon Floor Line (α - ε) -->
                            <line x1="80" y1="120" x2="720" y2="120" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4 2"/>
                            <text x="730" y="124" font-size="10.5" font-weight="800" fill="#d97706">Floor: α − ε</text>

                            <!-- Epsilon Bracket -->
                            <path d="M 75 70 Q 65 70 65 95 T 55 120 Q 65 120 65 95 T 75 70" fill="none" stroke="#b45309" stroke-width="1.2"/>
                            <text x="45" y="99" font-size="10" font-weight="700" fill="#b45309" text-anchor="end">Width ε</text>
                        </g>

                        <!-- LAYER 2: The Breakthrough Point (a_N) -->
                        <g id="mct-layer-break" class="mct-anim mct-hidden">
                            <!-- Highlight the specific point that breaks the floor -->
                            <circle cx="300" cy="115" r="7" fill="none" stroke="#ef4444" stroke-width="2"/>
                            <path d="M 300 145 L 300 128" fill="none" stroke="#ef4444" stroke-width="1.5" marker-end="url(#mct-arr)"/>
                            <text x="300" y="160" font-size="10" font-weight="800" fill="#e11d48" text-anchor="middle">Milestone Term a_N</text>

                            <!-- Red shading below floor to show it's not an upper bound -->
                            <rect x="80" y="120" width="220" height="160" fill="url(#mct-hatch-red)"/>
                        </g>

                        <!-- LAYER 3: The Tail Lock-In -->
                        <g id="mct-layer-tail" class="mct-anim mct-hidden">
                            <!-- Master Cutoff Line -->
                            <line x1="300" y1="40" x2="300" y2="280" stroke="#059669" stroke-width="2" stroke-dasharray="5 3"/>
                            <rect x="260" y="285" width="80" height="20" rx="4" fill="#059669"/>
                            <text x="300" y="299" font-size="9" font-weight="800" fill="#ffffff" text-anchor="middle">Cutoff N</text>

                            <!-- Green Tail Shading in the Corridor -->
                            <rect x="300" y="70" width="420" height="50" fill="#dcfce7" fill-opacity="0.8"/>

                            <!-- Highlight Tail Points in Green -->
                            <g fill="#10b981" stroke="#ffffff" stroke-width="1.5">
                                <circle cx="360" cy="100" r="5"/>
                                <circle cx="420" cy="90" r="5"/>
                                <circle cx="480" cy="83" r="5"/>
                                <circle cx="540" cy="78" r="5"/>
                                <circle cx="600" cy="75" r="5"/>
                                <circle cx="660" cy="73" r="5"/>
                            </g>
                            <text x="480" y="55" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">Infinite Tail Locked in Corridor</text>
                        </g>
                    </svg>
                </div>

                <!-- NAVIGATION & INLINE PREVIEW -->
                <div class="nav-panel">
                    <div class="nav-buttons">
                        <button id="mct-btn-prev" class="mct-btn" onclick="advanceMCT(-1)" disabled>Previous</button>
                        <button id="mct-btn-next" class="mct-btn mct-btn-primary" onclick="advanceMCT(1)">Next Step</button>
                        <button id="mct-btn-reset" class="mct-btn" onclick="resetMCT()">Reset</button>
                    </div>
                    <p id="mct-preview-text" class="preview-desc">
                        We begin with an increasing sequence bounded above. By the Completeness Axiom, the set of sequence values must have a tightest possible ceiling: the supremum α.
                    </p>
                </div>

                <!-- PAIRED ANALYTICAL PANES -->
                <div class="panes-grid">
                    <div class="mct-pane mct-pane-what">
                        <h4>What Is Happening</h4>
                        <div id="mct-pane-what" class="mct-pane-body">
                            The sequence aₙ marches upward. It is trapped beneath some upper bound M, meaning it cannot escape to infinity. Because the real numbers are complete, there is a lowest possible ceiling, denoted α = sup(S).
                        </div>
                    </div>
                    <div class="mct-pane mct-pane-why">
                        <h4>Why The System Does This</h4>
                        <div id="mct-pane-why" class="mct-pane-body">
                            The Supremum. We suspect the sequence will crash into this exact ceiling α. To prove lim aₙ = α, we must show that the infinite tail eventually enters and stays within any arbitrary ε-corridor drawn below α.
                        </div>
                    </div>
                </div>
            </div>

            <script>
            (function() {
                let mctStep = 0;

                const mctData = [
                    {
                        phase: "0: The Physical Setup",
                        eps: "Pending", n: "Pending",
                        status: "Bounded & Rising", statusColor: "#64748b",
                        summary: "We begin with an increasing sequence bounded above. By the Completeness Axiom, the set of sequence values must have a tightest possible ceiling: the supremum α.",
                        what: "The sequence aₙ marches upward. It is trapped beneath some upper bound M, meaning it cannot escape to infinity. Because the real numbers are complete, there is a lowest possible ceiling, denoted α = sup(S).",
                        why: "The Supremum. We suspect the sequence will crash into this exact ceiling α. To prove lim aₙ = α, we must show that the infinite tail eventually enters and stays within any arbitrary ε-corridor drawn below α.",
                        l_eps: false, l_break: false, l_tail: false
                    },
                    {
                        phase: "1: The Epsilon Challenge",
                        eps: "ε > 0 Chosen", n: "Pending",
                        status: "Testing the Floor", statusColor: "#b45309",
                        summary: "The Skeptic issues a challenge tolerance ε. We draw an open corridor spanning from the ceiling α down to a floor at α - ε.",
                        what: "An amber corridor of width ε is drawn directly below the supremum ceiling. The lower boundary forms a new barrier at α - ε.",
                        why: "The ε-N Game. We are asserting that α is the true limit. Therefore, the sequence must eventually be able to penetrate and survive inside this tiny margin, no matter how small ε is.",
                        l_eps: true, l_break: false, l_tail: false
                    },
                    {
                        phase: "2: The Breakthrough Point",
                        eps: "ε > 0", n: "Term a_N Found",
                        status: "Floor Breached", statusColor: "#e11d48",
                        summary: "Because α is the LOWEST possible ceiling, dropping the floor down by ε means α - ε is no longer a valid upper bound. Therefore, at least one sequence term MUST exist above it.",
                        what: "We identify a specific term a_N that has broken through the floor α - ε. (If no such term existed, the floor would be an upper bound smaller than the supremum, which is a logical contradiction).",
                        why: "The Supremum Property. This is the pure magic of the proof. We don't have to calculate N algebraically. The definition of the supremum mathematically guarantees that a breakthrough term a_N must exist.",
                        l_eps: true, l_break: true, l_tail: false
                    },
                    {
                        phase: "3: The Monotonic Lock-In",
                        eps: "ε > 0", n: "Master Cutoff N",
                        status: "Tail Captured ✓", statusColor: "#059669",
                        summary: "Because the sequence only moves upward, every term after a_N is pushed even higher. The entire infinite tail is now crushed between the breakthrough floor and the supremum ceiling.",
                        what: "The master cutoff N drops. For every index n > N, we know aₙ ≥ a_N (because it is increasing). Therefore: α - ε < a_N ≤ aₙ ≤ α. The tail is locked inside the green corridor.",
                        why: "The Engine Meets the Ceiling. Monotonicity acts like a ratchet—the sequence cannot fall back down below the floor. The combination of the supremum and monotonicity completes the limit proof.",
                        l_eps: true, l_break: true, l_tail: true
                    }
                ];

                function renderMCT() {
                    const data = mctData[mctStep];

                    document.getElementById('mct-tel-phase').textContent = data.phase;
                    document.getElementById('mct-tel-eps').textContent = data.eps;
                    document.getElementById('mct-tel-n').textContent = data.n;
                    document.getElementById('mct-tel-status').textContent = data.status;
                    document.getElementById('mct-tel-status').style.color = data.statusColor;

                    document.getElementById('mct-preview-text').textContent = data.summary;
                    document.getElementById('mct-pane-what').textContent = data.what;
                    document.getElementById('mct-pane-why').textContent = data.why;

                    document.getElementById('mct-btn-prev').disabled = (mctStep === 0);
                    document.getElementById('mct-btn-next').disabled = (mctStep === mctData.length - 1);

                    const setVis = (id, show) => {
                        const el = document.getElementById(id);
                        if (show) { el.classList.remove('mct-hidden'); el.classList.add('mct-visible'); }
                        else { el.classList.remove('mct-visible'); el.classList.add('mct-hidden'); }
                    };

                    setVis('mct-layer-eps', data.l_eps);
                    setVis('mct-layer-break', data.l_break);
                    setVis('mct-layer-tail', data.l_tail);
                }

                window.advanceMCT = function(delta) {
                    mctStep = Math.max(0, Math.min(mctData.length - 1, mctStep + delta));
                    renderMCT();
                };

                window.resetMCT = function() {
                    mctStep = 0;
                    renderMCT();
                };

                document.addEventListener('DOMContentLoaded', renderMCT);
            })();
            </script>"""

    if old_section in content:
        content = content.replace(old_section, new_section)
        with open("week2-lecture5.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully updated Section 1 (Monotone Convergence Theorem) in week2-lecture5.html.")
    else:
        print("Error: Could not find the target section to replace.")

if __name__ == "__main__":
    apply_patch()
