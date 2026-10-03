#!/usr/bin/env python3
import os
import subprocess

def write_week1_module():
    if os.path.exists('week1.html'):
        os.remove('week1.html')

    html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 1: Sets, Numbers, and Sequences | MTHS120</title>
    <!-- KaTeX Integration -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
    <style>
        :root {
            --bg: #f8fafc; --text: #1e293b; --card: #ffffff; --border: #e2e8f0;
            --accent: #0ea5e9; --telemetry-bg: #1e293b; --telemetry-text: #38bdf8;
            --track1-bg: #f0f9ff; --track2-bg: #fdf4ff;
        }
        body { font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; }
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 2rem; }

        h2 { border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; margin-top: 2.5rem; color: #0f172a; }
        h3 { color: #334155; margin-top: 1.5rem; }

        /* Dual-Track Layout */
        .dual-track-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 1.5rem; margin-bottom: 2rem; }
        .track-card { padding: 1.5rem; border-radius: 6px; border: 1px solid var(--border); }
        .track-formal { background: var(--track1-bg); border-color: #bae6fd; }
        .track-applied { background: var(--track2-bg); border-color: #f5d0fe; }
        .track-card h4 { margin-top: 0; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; color: #0369a1; }

        /* Interactive Simulator Styles */
        .simulator { border: 1px solid var(--border); border-radius: 8px; overflow: hidden; margin-top: 2rem; }
        .telemetry { background: var(--telemetry-bg); color: var(--telemetry-text); padding: 0.75rem 1.5rem; font-family: monospace; display: flex; gap: 2rem; font-size: 0.9rem; align-items: center;}
        .canvas-container { padding: 2rem; background: #f1f5f9; display: flex; justify-content: center; border-bottom: 1px solid var(--border); }
        .controls-pane { display: flex; gap: 2rem; padding: 1.5rem; background: var(--card); border-bottom: 1px solid var(--border); align-items: flex-start; }
        .nav-buttons { display: flex; flex-direction: column; gap: 0.5rem; min-width: 120px; }
        button { background: var(--accent); color: white; border: none; padding: 0.5rem 1rem; border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%; }
        button:disabled { background: var(--border); cursor: not-allowed; }
        .step-summary { flex-grow: 1; font-size: 0.95rem; color: #475569; line-height: 1.5; }
        .pane { background: var(--card); padding: 1.5rem; }
        .pane h4 { margin-top: 0; color: var(--accent); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem; }
        .pane p { margin: 0 0 0.75rem 0; }
        .pane p:last-child { margin-bottom: 0; }
        .toggle-group { min-width: 220px; }
        select { width: 100%; padding: 0.5rem; border-radius: 4px; border: 1px solid var(--border); font-family: system-ui, sans-serif; }

        .definition-box { background: #f8fafc; border-left: 4px solid var(--accent); padding: 1rem 1.5rem; margin: 1rem 0; border-radius: 0 6px 6px 0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Week 1: Sets, Numbers, and Sequences</h1>
            <a href="index.html" style="color: var(--accent); text-decoration: none;">&larr; Back to Curriculum Index</a>
        </div>

        <div class="module-content">
            <h2>1. Set Theory Foundations</h2>
            <p>Before we can do calculus, we need a precise language to talk about collections of objects. A <strong>set</strong> is any well-defined collection of objects, called <em>elements</em> or <em>members</em>.</p>

            <div class="definition-box">
                <p><strong>Notation Examples:</strong></p>
                <ul>
                    <li><strong>Roster Notation:</strong> Listing elements explicitly, e.g., $A = \{1, 2, 3, 4\}$.</li>
                    <li><strong>Set-Builder Notation:</strong> Defining elements by a property, e.g., $B = \{x \in \mathbb{R} \mid x^2 > 4\}$. Read: "The set of all $x$ in $\mathbb{R}$ such that $x^2$ is strictly greater than 4."</li>
                    <li><strong>Membership:</strong> $x \in A$ means "$x$ is an element of $A$". $x \notin A$ means it is not.</li>
                </ul>
            </div>

            <h3>Core Set Operations</h3>
            <p>We combine and manipulate sets using fundamental logic operations:</p>
            <ul>
                <li><strong>Union ($A \cup B$):</strong> Elements in $A$, or in $B$, or in both. ($\{1, 2\} \cup \{2, 3\} = \{1, 2, 3\}$)</li>
                <li><strong>Intersection ($A \cap B$):</strong> Elements belonging to <em>both</em> $A$ and $B$. ($\{1, 2\} \cap \{2, 3\} = \{2\}$)</li>
                <li><strong>Complement ($A^c$ or $U \setminus A$):</strong> Elements in the universal set $U$ that are <em>not</em> in $A$.</li>
                <li><strong>Cartesian Product ($A \times B$):</strong> The set of all ordered pairs $(a, b)$ where $a \in A$ and $b \in B$. (This is how we construct the 2D coordinate plane $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$).</li>
            </ul>

            <h2>2. The Hierarchy of Number Systems</h2>
            <p>Mathematics builds its universe of numbers step by step, expanding systems to solve equations that previous systems couldn't handle.</p>

            <ul>
                <li><strong>Natural Numbers ($\mathbb{N}$):</strong> $\{1, 2, 3, 4, \dots\}$ (sometimes including $0$). Used for counting. <em>Limitation:</em> You cannot subtract larger from smaller without breaking out of the set.</li>
                <li><strong>Integers ($\mathbb{Z}$):</strong> $\{\dots, -2, -1, 0, 1, 2, \dots\}$. Includes negatives and zero. <em>Limitation:</em> You cannot divide ($3 \div 2$) and stay inside $\mathbb{Z}$.</li>
                <li><strong>Rational Numbers ($\mathbb{Q}$):</strong> Numbers expressible as a fraction $\frac{p}{q}$ where $p, q \in \mathbb{Z}$ and $q \neq 0$. Includes terminating and repeating decimals.</li>
                <li><strong>Real Numbers ($\mathbb{R}$):</strong> All rational numbers <em>plus</em> irrational numbers (like $\sqrt{2}$ or $\pi$) whose decimals never terminate or repeat. $\mathbb{R}$ fills all the "gaps" on the number line.</li>
            </ul>

            <div class="definition-box">
                <p><strong>Why Real Analysis Matters:</strong> The rational numbers ($\mathbb{Q}$) have "holes" (e.g., no rational number squared equals $2$). Calculus requires the <em>Completeness Property</em> of the Real Numbers ($\mathbb{R}$) to guarantee that limits, suprema, and integrals don't fall into empty space.</p>
            </div>

            <h2>3. Sequences and the Limit Concept</h2>
            <p>With sets and real numbers established, we can define <strong>sequences</strong>—the core bridge to calculus.</p>
            <p>A sequence is formally a function whose domain is the natural numbers $\mathbb{N}$ and whose codomain is the real numbers $\mathbb{R}$:</p>
            <p>$$f: \mathbb{N} \rightarrow \mathbb{R}, \quad \text{denoted as } (a_n)_{n=1}^\infty \text{ or } a_1, a_2, a_3, \dots, a_n$$</p>

            <p>When studying sequences, our primary question is: <em>As $n$ grows infinitely large ($n \to \infty$), do the terms $a_n$ settle down toward a specific target value $L$?</em></p>

            <p>To explore this rigorously, use the <strong>Dual-Track Simulator</strong> below, which maps the abstract formal definition of a limit against a concrete numerical iteration stream.</p>

            <div class="dual-track-grid">
                <div class="track-card track-formal">
                    <h3>📐 Track 1: Abstract Formalism (Pure Theory)</h3>
                    <p>We say $\lim_{n\to\infty} a_n = L$ if:</p>
                    <p>$$\forall \epsilon > 0, \quad \exists N \in \mathbb{N} \quad \text{such that} \quad \forall n > N, \quad |a_n - L| < \epsilon$$</p>
                    <p>This universal-existential quantifier structure proves that points permanently enter and remain within an arbitrary neighborhood around $L$.</p>
                </div>
                <div class="track-card track-applied">
                    <h3>🎛️ Track 2: Applied Mechanics (Numerical Analog)</h3>
                    <p>Imagine tracking a numerical error-correction stream where successive approximation residuals represent our sequence ($a_n$).</p>
                    <p>We want total error eradication ($L=0$), but operational performance requires proving the recurrence relation reliably drops residuals beneath an acceptable tolerance threshold ($\epsilon = 0.2$) past a specific execution index ($N$).</p>
                </div>
            </div>

            <div class="simulator">
                <div class="telemetry">
                    <span>PHASE: <span id="tel-phase">Initialization</span></span>
                    <span>ARCHITECTURE: <span id="tel-seq">$a_n = \frac{1}{n}$</span></span>
                    <span>INDEX ($n$) = <span id="tel-n">1</span></span>
                    <span>VALUE ($a_n$) = <span id="tel-val">$1.000$</span></span>
                    <span>TOLERANCE ($\epsilon$) = <span id="tel-eps">$0.2$</span></span>
                </div>

                <div class="canvas-container">
                    <svg id="plot" width="600" height="200" viewBox="0 0 600 200">
                        <rect id="eps-band" x="40" y="132" width="540" height="28" fill="#bae6fd" opacity="0.5"/>

                        <line x1="40" y1="160" x2="580" y2="160" stroke="#94a3b8" stroke-width="2"/>
                        <line x1="40" y1="20" x2="40" y2="160" stroke="#94a3b8" stroke-width="2"/>

                        <text x="585" y="155" font-family="serif" font-style="italic" font-size="14" fill="#64748b">n</text>
                        <text x="15" y="12" font-family="serif" font-style="italic" font-size="14" fill="#64748b">a<tspan dy="4" font-size="10">n</tspan></text>

                        <path d="M80 160 v5 M140 160 v5 M200 160 v5 M260 160 v5 M320 160 v5 M380 160 v5 M440 160 v5 M500 160 v5" stroke="#94a3b8" fill="none"/>
                        <text x="76" y="180" font-family="sans-serif" font-size="10" fill="#64748b">1</text>
                        <text x="136" y="180" font-family="sans-serif" font-size="10" fill="#64748b">2</text>
                        <text x="196" y="180" font-family="sans-serif" font-size="10" fill="#64748b">3</text>
                        <text x="256" y="180" font-family="sans-serif" font-size="10" fill="#64748b">4</text>
                        <text x="316" y="180" font-family="sans-serif" font-size="10" fill="#64748b">5</text>
                        <text x="376" y="180" font-family="sans-serif" font-size="10" fill="#64748b">6</text>
                        <text x="436" y="180" font-family="sans-serif" font-size="10" fill="#64748b">7</text>
                        <text x="496" y="180" font-family="sans-serif" font-size="10" fill="#64748b">8</text>

                        <path d="M40 20 h-5 M40 90 h-5" stroke="#94a3b8" fill="none"/>
                        <text x="25" y="165" font-family="sans-serif" font-size="10" fill="#64748b">0</text>
                        <text x="15" y="94" font-family="sans-serif" font-size="10" fill="#64748b">0.5</text>
                        <text x="15" y="24" font-family="sans-serif" font-size="10" fill="#64748b">1.0</text>

                        <path d="M40 132 h-5" stroke="#0284c7" fill="none"/>
                        <text x="12" y="136" font-family="sans-serif" font-size="10" fill="#0284c7">&epsilon;=0.2</text>

                        <line id="n-threshold" x1="200" y1="20" x2="200" y2="160" stroke="#ef4444" stroke-width="2" stroke-dasharray="4" opacity="0"/>

                        <g id="points-group"></g>
                    </svg>
                </div>

                <div class="controls-pane">
                    <div class="nav-buttons">
                        <button id="btn-prev" onclick="step(-1)" disabled>Prev Step</button>
                        <button id="btn-next" onclick="step(1)">Next Step</button>
                        <button id="btn-reset" onclick="reset()" style="background-color: var(--text-muted);">Reset</button>
                    </div>
                    <div class="step-summary" id="step-summary"></div>
                    <div class="toggle-group">
                        <label for="seq-toggle" style="font-size: 0.85rem; font-weight: bold; color: var(--text-muted); display: block; margin-bottom: 0.5rem;">COMPARE ARCHITECTURE:</label>
                        <select id="seq-toggle" onchange="changeSeq()">
                            <option value="reciprocal">Linear Attenuator (a_n = 1/n)</option>
                            <option value="geometric">Exponential Decay (a_n = 2^-n)</option>
                        </select>
                    </div>
                </div>

                <div class="analysis-panes">
                    <div class="pane">
                        <h4>What Is Happening (Mechanics)</h4>
                        <div id="pane-what"></div>
                    </div>
                    <div class="pane">
                        <h4>Why The System Does This (Rationale)</h4>
                        <div id="pane-why"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const state = { step: 0, seq: 'reciprocal', eps: 0.2 };
        const data = {
            reciprocal: [1.0, 0.5, 0.333, 0.25, 0.2, 0.166, 0.142, 0.125],
            geometric: [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.0156, 0.0078]
        };

        const narratives = [
            {
                phase: "Initialization", n: 1, indexVal: 1,
                summary: "<strong>Goal:</strong> Initialize the sequence mapping $f: \\mathbb{N} \\rightarrow \\mathbb{R}$ and establish error bound constraints for our numerical iteration stream.",
                what: "<p><strong>Abstract Formalism:</strong> The sequence initializes at index $n=1$, yielding $a_1 = 1.0$ under the selected mapping rule.</p><p><strong>Applied Mechanics:</strong> Our iterative computation begins, defining a target limit $L=0$ and an acceptable residual tolerance $\\epsilon = 0.2$ (the blue band).</p>",
                why: "<p><strong>Formal Rationale:</strong> Under real analysis axioms, we cannot rely on loose intuition. We must establish that the sequence domain maps to a bounded codomain where arbitrary $\\epsilon$-neighborhoods can be tested.</p><p><strong>System Constraint:</strong> Defining $\\epsilon$ upfront ensures convergence bounds are specified before executing subsequent steps.</p>"
            },
            {
                phase: "Iteration", n: 3, indexVal: 3,
                summary: "<strong>Goal:</strong> Evaluate intermediate terms as the sequence progresses through preliminary index steps.",
                what: "<p><strong>Abstract Formalism:</strong> The system computes $a_2$ and $a_3$. The terms decrease monotonically.</p><p><strong>Applied Mechanics:</strong> The recurrence relation actively dampens residual error across steps $n=2$ and $n=3$, bringing the value down toward the target limit.</p>",
                why: "<p><strong>Formal Rationale:</strong> Monotonic decrease guarantees downward motion, but does not yet satisfy convergence bounds.</p><p><strong>System Constraint:</strong> Lowering the value is insufficient; we must locate the exact index where terms permanently cross into tolerance.</p>"
            },
            {
                phase: "Threshold Discovery", n: 5, indexVal: 5,
                summary: "<strong>Goal:</strong> Algebraically solve for the critical threshold index $N$ dictated by the $\\epsilon-N$ definition.",
                what: "<p><strong>Abstract Formalism:</strong> We evaluate $|a_n - 0| < 0.2$. For linear decay ($1/n$), this yields $n > 5$. For exponential decay ($2^{-n}$), it crosses at $n > 2$.</p><p><strong>Applied Mechanics:</strong> We set the threshold index $N$, rendering the red threshold boundary on our canvas to mark the computation latency required for target precision.</p>",
                why: "<p><strong>Formal Rationale:</strong> This operationalizes the existential quantifier $\\exists N$ in the formal definition.</p><p><strong>System Constraint:</strong> Establishes the exact execution latency required before the system certifies output stability.</p>"
            },
            {
                phase: "Convergence Verification", n: 8, indexVal: 8,
                summary: "<strong>Goal:</strong> Fulfill the universal quantifier condition to formally certify the limit.",
                what: "<p><strong>Abstract Formalism:</strong> For all subsequent indices $n > N$, terms remain strictly trapped within the $\\epsilon$ neighborhood.</p><p><strong>Applied Mechanics:</strong> The residual error remains flat and negligible across all further computation steps.</p>",
                why: "<p><strong>Formal Rationale:</strong> This satisfies $\\forall n > N$. Because this inequality holds for <em>any</em> arbitrary $\\epsilon > 0$, the limit $\\lim_{n\\to\\infty} a_n = L$ is verified.</p><p><strong>System Constraint:</strong> Guarantees long-term numerical stability against unexpected divergence.</p>"
            }
        ];

        function changeSeq() {
            state.seq = document.getElementById('seq-toggle').value;
            updateUI();
        }

        function step(dir) {
            state.step += dir;
            document.getElementById('btn-prev').disabled = state.step === 0;
            document.getElementById('btn-next').disabled = state.step === 3;
            updateUI();
        }

        function reset() { state.step = 0; step(0); }

        function updateUI() {
            const current = narratives[state.step];

            const seqMath = state.seq === 'reciprocal' ? '$a_n = \\frac{1}{n}$' : '$a_n = 2^{-n}$';
            document.getElementById('tel-seq').innerHTML = seqMath;
            document.getElementById('tel-val').innerHTML = '$' + data[state.seq][current.indexVal - 1].toFixed(3) + '$';

            document.getElementById('tel-phase').innerText = current.phase;
            document.getElementById('tel-n').innerText = current.indexVal;

            document.getElementById('step-summary').innerHTML = current.summary;
            document.getElementById('pane-what').innerHTML = current.what;
            document.getElementById('pane-why').innerHTML = current.why;

            if(window.renderMathInElement) {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ]
                });
            }
            renderCanvas();
        }

        function renderCanvas() {
            const group = document.getElementById('points-group');
            const threshold = document.getElementById('n-threshold');
            group.innerHTML = '';

            const current = narratives[state.step];
            const pointsToDraw = data[state.seq].slice(0, current.indexVal);

            pointsToDraw.forEach((val, idx) => {
                const cx = 80 + (idx * 60);
                const cy = 160 - (val * 140);
                group.innerHTML += `<circle cx="${cx}" cy="${cy}" r="5" fill="#0ea5e9" />`;
                if(idx > 0) {
                    const prevVal = data[state.seq][idx - 1];
                    const px = 80 + ((idx - 1) * 60);
                    const py = 160 - (prevVal * 140);
                    group.innerHTML += `<line x1="${px}" y1="${py}" x2="${cx}" y2="${cy}" stroke="#0ea5e9" stroke-width="2" opacity="0.5"/>`;
                }
            });

            if (state.step >= 2) {
                const nIndex = state.seq === 'reciprocal' ? 5 : 3;
                threshold.setAttribute('x1', 80 + (nIndex-1)*60);
                threshold.setAttribute('x2', 80 + (nIndex-1)*60);
                threshold.setAttribute('opacity', '1');
            } else {
                threshold.setAttribute('opacity', '0');
            }
        }

        reset();
    </script>
</body>
</html>"""
    with open('week1.html', 'w') as f:
        f.write(html_content)

def execute_git_sync():
    commit_message = (
        "Expand Week 1 module to include Sets and Number Systems theory\n\n"
        "Added comprehensive foundational sections covering Set Theory notation and \n"
        "operations, the hierarchy of Number Systems (N, Z, Q, R) and their gaps, \n"
        "and formal sequence definitions prior to the interactive epsilon-N simulator."
    )

    commands = [
        ['git', 'add', 'update.py', 'week1.html'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]

    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == "__main__":
    print("Writing Week 1 module...")
    write_week1_module()
    print("Committing and pushing to GitHub...")
    execute_git_sync()
    print("Deployment complete.")
