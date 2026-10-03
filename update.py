#!/usr/bin/env python3
import os
import subprocess

def write_clean_modules():
    # Write Week 1 Module (Sections 1-3, strictly citation-free)
    week1_content = r"""<!DOCTYPE html>
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
            --bg: #f8fafc; --text: #0f172a; --card: #ffffff; --border: #cbd5e1;
            --accent: #d97706; --accent-hover: #b45309;
            --font-ui: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
        body { font-family: var(--font-ui); background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; }
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .intro-lead { font-size: 1.1rem; color: #1e293b; line-height: 1.7; margin-bottom: 1.5rem; background: #f1f5f9; padding: 1.5rem; border-radius: 6px; border-left: 4px solid var(--accent); border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }
        .toc-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.75rem; margin: 1.75rem 0 2.5rem 0; }
        .toc-box h4 { margin: 0 0 0.75rem 0; color: #92400e; font-size: 1.05rem; }
        .toc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.5rem 1.5rem; margin: 0; padding-left: 1.25rem; }
        .toc-grid li { margin-bottom: 0.35rem; font-size: 0.95rem; }
        .toc-grid a { color: #b45309; text-decoration: none; font-weight: 500; }
        .toc-grid a:hover { text-decoration: underline; color: var(--accent-hover); }

        h2 { border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; margin-top: 2.5rem; color: #0f172a; font-family: var(--font-ui); scroll-margin-top: 2rem; }
        h3 { color: #1e293b; margin-top: 1.5rem; font-family: var(--font-ui); scroll-margin-top: 2rem; }

        .infobox { background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.5rem; margin: 1.25rem 0 1.75rem 0; }
        .infobox h4 { margin: 0 0 0.85rem 0; color: #0f172a; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-ui); }
        .notation-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 0.85rem 1.75rem; font-size: 0.95rem; }
        .notation-item { display: grid; grid-template-columns: minmax(130px, max-content) 1fr; gap: 0.75rem; align-items: center; }
        .notation-sym { font-weight: 600; color: var(--accent); white-space: nowrap; display: flex; justify-content: center; align-items: center; text-align: center; }
        .notation-desc { min-width: 0; word-break: break-word; line-height: 1.5; color: #334155; }
        .infobox-intro { font-size: 0.93rem; color: #475569; line-height: 1.6; margin: 0 0 1.25rem 0; padding-bottom: 0.85rem; border-bottom: 1px solid #e2e8f0; }

        .definition-box { background: #f8fafc; border-left: 4px solid var(--accent); padding: 1rem 1.5rem; margin: 1rem 0; border-radius: 0 6px 6px 0; border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }
        .aside-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #b45309; padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .aside-box h4 { margin-top: 0; color: #b45309; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Week 1: Sets, Numbers, and Sequences</h1>
            <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Curriculum Index</a>
        </div>

        <div class="module-content">
            <div class="intro-lead">
                Welcome to Week 1 of MTHS120. In accordance with Topic 1 of the official lecture notes (Sections 1, 2, and 3), this module establishes set theory foundations, functions, Peano's axioms for natural numbers, real number completeness, and sequence mechanics including derived sequences and partial sums.
            </div>

            <div class="toc-box">
                <h4>📌 Module Table of Contents</h4>
                <ul class="toc-grid">
                    <li><a href="#section-sets">1. Sets and Functions (§1)</a></li>
                    <li><a href="#section-numbers">2. Number Systems and Completeness (§2)</a></li>
                    <li><a href="#section-sequences">3. Sequences, Derived Sequences, and Partial Sums (§3)</a></li>
                </ul>
            </div>

            <h2 id="section-sets">1. Sets and Functions (§1)</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Sets &amp; Functions</h4>
                <div class="infobox-intro">
                    <strong>The language of science:</strong> Set theory provides the foundational grammar for modern mathematics. Functions map inputs from a domain to outputs in a codomain.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$x \in A$</span><span class="notation-desc">$x$ is an element of set $A$</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \subseteq B$</span><span class="notation-desc">$A$ is a subset of $B$</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \cup B$</span><span class="notation-desc">Union of sets $A$ and $B$</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \cap B$</span><span class="notation-desc">Intersection of sets $A$ and $B$</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \setminus B$</span><span class="notation-desc">Set difference (relative complement)</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \times B$</span><span class="notation-desc">Cartesian product of sets</span></div>
                    <div class="notation-item"><span class="notation-sym">$f: X \to Y$</span><span class="notation-desc">Function $f$ with domain $X$ and codomain $Y$</span></div>
                    <div class="notation-item"><span class="notation-sym">$f^{-1}(y)$</span><span class="notation-desc">Preimage of element $y$</span></div>
                    <div class="notation-item"><span class="notation-sym">$g \circ f$</span><span class="notation-desc">Function composition ("f followed by g")</span></div>
                    <div class="notation-item"><span class="notation-sym">$f^{-1}$</span><span class="notation-desc">Inverse function (exists iff $f$ is bijective)</span></div>
                </div>
            </div>

            <p>A <strong>set</strong> is a collection of distinct elements. New sets are formed via union ($A \cup B$), intersection ($A \cap B$), difference ($A \setminus B$), and Cartesian product ($A \times B$).</p>

            <h3>Functions and Mappings</h3>
            <p>A <strong>function</strong> $f: X \to Y$ assigns to each element $x \in X$ (domain) one and only one value $y = f(x) \in Y$ (codomain).</p>
            <ul>
                <li><strong>Range:</strong> The subset of the codomain consisting of actual output values $R = \{f(x) \mid x \in X\}$.</li>
                <li><strong>Surjective (Onto):</strong> Range equals codomain ($R = Y$), meaning every element in $Y$ has at least one preimage.</li>
                <li><strong>Injective (1-to-1):</strong> Distinct inputs produce distinct outputs: $a \neq b \implies f(a) \neq f(b)$.</li>
                <li><strong>Bijective:</strong> Both injective and surjective, which is the exact necessary and sufficient condition for an <strong>inverse function</strong> $f^{-1}: Y \to X$ to exist.</li>
                <li><strong>Composition:</strong> For $f: X \to Y$ and $g: Y \to Z$, the composition $g \circ f: X \to Z$ maps $x \mapsto g(f(x))$.</li>
            </ul>

            <h2 id="section-numbers">2. Number Systems and Completeness (§2)</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Numbers &amp; Bounds</h4>
                <div class="infobox-intro">
                    <strong>Number systems and real analysis:</strong> Building from Peano's axioms for $\mathbb{N}$ to the completeness of $\mathbb{R}$.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$\mathbb{N}$</span><span class="notation-desc">Natural numbers $\{0, 1, 2, \dots\}$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\mathbb{Z}$</span><span class="notation-desc">Integers $\{\dots, -1, 0, 1, \dots\}$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\mathbb{Q}$</span><span class="notation-desc">Rational numbers $\{p/q \mid p \in \mathbb{Z}, q \in \mathbb{Z}_+\}$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\mathbb{R}$</span><span class="notation-desc">Real numbers (complete ordered field)</span></div>
                    <div class="notation-item"><span class="notation-sym">$|x|$</span><span class="notation-desc">Absolute value (distance to origin)</span></div>
                    <div class="notation-item"><span class="notation-sym">$\sup S$</span><span class="notation-desc">Supremum (least upper bound) of set $S$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\inf S$</span><span class="notation-desc">Infimum (greatest lower bound) of set $S$</span></div>
                </div>
            </div>

            <h3>Peano's Axioms for $\mathbb{N}$</h3>
            <p>Natural numbers are defined by Peano's axioms: $0 \in \mathbb{N}$, each number has a unique successor, $0$ is not a successor of any number (no loops, no branching, connected graph rooted at 0), and mathematical induction holds.</p>

            <h3>Completeness and the Least Upper Bound Property</h3>
            <p>While rationals $\mathbb{Q}$ are dense, they contain gaps (e.g., $x^2 = 2$ has no rational solution). The real numbers $\mathbb{R}$ extend $\mathbb{Q}$ and satisfy the <strong>Axiom of Completeness</strong>: Any non-empty subset $S \subseteq \mathbb{R}$ that is bounded above has a supremum ($\sup S$) in $\mathbb{R}$. The <strong>Archimedean Axiom</strong> ensures that for any positive real numbers $x, y$, there is an $n \in \mathbb{N}$ such that $nx > y$.</p>

            <h2 id="section-sequences">3. Sequences, Derived Sequences, and Partial Sums (§3)</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Sequence Mechanics</h4>
                <div class="infobox-intro">
                    <strong>Discrete modeling:</strong> Sequences are functions $f: \mathbb{N} \to \mathbb{R}$ mapping indices to real values.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$(a_n)$</span><span class="notation-desc">Sequence $(a_0, a_1, a_2, \dots)$</span></div>
                    <div class="notation-item"><span class="notation-sym">$a_n'$</span><span class="notation-desc">Derived sequence $a_{n+1} - a_n$</span></div>
                    <div class="notation-item"><span class="notation-sym">$s_n$</span><span class="notation-desc">Partial sum $\sum_{\nu=0}^n b_\nu$</span></div>
                    <div class="notation-item"><span class="notation-sym">$an + b$</span><span class="notation-desc">Arithmetic progression</span></div>
                    <div class="notation-item"><span class="notation-sym">$aq^n$</span><span class="notation-desc">Geometric progression</span></div>
                </div>
            </div>

            <h3>Derived Sequences and Partial Sums</h3>
            <p>The <strong>derived sequence</strong> of $(a_n)$ is defined by consecutive differences $a_n' = a_{n+1} - a_n$. A sequence is constant, increasing, or decreasing if and only if its derived sequence is identically zero, non-negative, or non-positive. Conversely, summing terms yields <strong>partial sums</strong> $s_n = \sum_{\nu=0}^n b_\nu$. For example, the partial sums of the geometric progression $q^n$ give the closed-form sum:</p>
            <p>$$\sum_{\nu=0}^{n-1} q^\nu = \frac{1 - q^n}{1 - q}$$</p>
        </div>
    </div>
</body>
</html>
"""
    with open('week1.html', 'w') as f:
        f.write(week1_content)

    # Write Week 2 Module (Sections 4-6, strictly citation-free)
    week2_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 2: Limits of Sequences | MTHS120</title>
    <!-- KaTeX Integration -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
    <style>
        :root {
            --bg: #f8fafc; --text: #0f172a; --card: #ffffff; --border: #cbd5e1;
            --accent: #d97706; --accent-hover: #b45309;
            --font-ui: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
        body { font-family: var(--font-ui); background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; }
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .intro-lead { font-size: 1.1rem; color: #1e293b; line-height: 1.7; margin-bottom: 1.5rem; background: #f1f5f9; padding: 1.5rem; border-radius: 6px; border-left: 4px solid var(--accent); border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }
        .toc-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.75rem; margin: 1.75rem 0 2.5rem 0; }
        .toc-box h4 { margin: 0 0 0.75rem 0; color: #92400e; font-size: 1.05rem; }
        .toc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.5rem 1.5rem; margin: 0; padding-left: 1.25rem; }
        .toc-grid li { margin-bottom: 0.35rem; font-size: 0.95rem; }
        .toc-grid a { color: #b45309; text-decoration: none; font-weight: 500; }
        .toc-grid a:hover { text-decoration: underline; color: var(--accent-hover); }

        h2 { border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; margin-top: 2.5rem; color: #0f172a; font-family: var(--font-ui); scroll-margin-top: 2rem; }
        h3 { color: #1e293b; margin-top: 1.5rem; font-family: var(--font-ui); scroll-margin-top: 2rem; }

        .infobox { background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.5rem; margin: 1.25rem 0 1.75rem 0; }
        .infobox h4 { margin: 0 0 0.85rem 0; color: #0f172a; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-ui); }
        .notation-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 0.85rem 1.75rem; font-size: 0.95rem; }
        .notation-item { display: grid; grid-template-columns: minmax(130px, max-content) 1fr; gap: 0.75rem; align-items: center; }
        .notation-sym { font-weight: 600; color: var(--accent); white-space: nowrap; display: flex; justify-content: center; align-items: center; text-align: center; }
        .notation-desc { min-width: 0; word-break: break-word; line-height: 1.5; color: #334155; }
        .infobox-intro { font-size: 0.93rem; color: #475569; line-height: 1.6; margin: 0 0 1.25rem 0; padding-bottom: 0.85rem; border-bottom: 1px solid #e2e8f0; }

        .scoping-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.5rem; margin: 1.75rem 0; }
        .scoping-box h4 { margin-top: 0; color: #92400e; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; }
        .scoping-table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.92rem; }
        .scoping-table th, .scoping-table td { border: 1px solid #fed7aa; padding: 0.6rem 0.85rem; text-align: left; }
        .scoping-table th { background: #fef3c7; color: #92400e; font-weight: 600; }
        .scoping-table td { background: #ffffff; color: #1e293b; }
        .swap-card-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin: 1rem 0; }
        .swap-card { background: #ffffff; border: 1px solid #fed7aa; border-radius: 6px; padding: 1rem; }
        .swap-card h5 { margin: 0 0 0.5rem 0; font-size: 0.95rem; }

        .widget-instructions { background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.5rem; margin: 2rem 0 1rem 0; }
        .widget-instructions h4 { margin: 0 0 0.65rem 0; color: #0f172a; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; }
        .widget-instructions ol { margin: 0.5rem 0 0.85rem 1.25rem; padding: 0; }
        .widget-instructions li { margin-bottom: 0.45rem; font-size: 0.95rem; color: #334155; }
        .widget-instructions ul { margin: 0.35rem 0 0.5rem 1.25rem; padding: 0; }
        .widget-instructions ul li { margin-bottom: 0.3rem; font-size: 0.92rem; color: #475569; }

        .game-box, .stepper-walkthrough { border: 1px solid var(--border); border-radius: 8px; overflow: hidden; margin-top: 1.5rem; background: var(--card); box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
        .telemetry-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 0.75rem; padding: 0.85rem 1.25rem; background: #f8fafc; border-bottom: 1px solid var(--border); }
        .telemetry-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.55rem 0.85rem; display: flex; flex-direction: column; gap: 0.25rem; min-width: 0; }
        .telemetry-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: #64748b; }
        .telemetry-badge { font-size: 0.92rem; font-weight: 600; line-height: 1.3; font-variant-numeric: tabular-nums; }

        .game-header { background: #f8fafc; color: #b45309; padding: 1rem 1.5rem; font-size: 0.92rem; font-weight: 700; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); }
        .game-body { padding: 1.5rem; background: #ffffff; display: flex; flex-direction: column; gap: 1rem; border-bottom: 1px solid var(--border); }
        .game-controls { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; }
        .game-btn { background: var(--accent); color: white; border: none; padding: 0.55rem 1.1rem; border-radius: 4px; cursor: pointer; font-weight: 600; font-size: 0.92rem; transition: background 0.2s; }
        .game-btn:hover { background: var(--accent-hover); }
        .game-canvas-wrap { background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 1.75rem; display: flex; justify-content: center; }
        .game-canvas-wrap svg { width: 100%; height: auto; display: block; }

        .formula-stage-wrap { background: #f8fafc; padding: 1.25rem; border-bottom: 1px solid var(--border); display: flex; justify-content: center; }
        .formula-display { display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; justify-content: center; font-size: 1.25rem; font-weight: 500; }
        .formula-chunk { padding: 0.45rem 0.85rem; border-radius: 6px; border: 2px solid #e2e8f0; color: #475569; background: #ffffff; transition: all 0.3s ease; cursor: pointer; user-select: none; white-space: nowrap; }
        .formula-chunk.active { border-color: #d97706; background: #fef3c7; color: #92400e; transform: translateY(-2px); }
        .formula-chunk.completed { border-color: #059669; color: #065f46; background: #ecfdf5; }
        .formula-sep { color: #64748b; font-weight: 400; white-space: nowrap; }

        .canvas-container { padding: 2rem; background: #f1f5f9; display: flex; justify-content: center; border-bottom: 1px solid var(--border); }
        .canvas-container svg { width: 100%; height: auto; display: block; }

        .controls-pane { display: flex; gap: 2rem; padding: 1.5rem; background: var(--card); border-bottom: 1px solid var(--border); align-items: flex-start; }
        .nav-buttons { display: flex; flex-direction: column; gap: 0.5rem; min-width: 140px; }
        button { background: var(--accent); color: white; border: none; padding: 0.55rem 1rem; border-radius: 4px; cursor: pointer; font-weight: 600; width: 100%; transition: background 0.2s; font-size: 0.92rem; }
        button:hover { background: var(--accent-hover); }
        button:disabled { background: #94a3b8; cursor: not-allowed; }
        .step-summary { flex-grow: 1; font-size: 0.97rem; color: #334155; line-height: 1.6; }
        .analysis-panes { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: var(--border); }
        .pane { background: var(--card); padding: 1.5rem; }
        .pane h4 { margin-top: 0; color: var(--accent); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem; font-weight: 700; }
        .pane p { margin: 0 0 0.75rem 0; line-height: 1.6; font-size: 0.95rem; }
        .pane p:last-child { margin-bottom: 0; }
        .toggle-group { min-width: 250px; }
        select { width: 100%; padding: 0.55rem; border-radius: 4px; border: 1px solid var(--border); background: #fff; color: var(--text); font-size: 0.92rem; }

        .definition-box { background: #f8fafc; border-left: 4px solid var(--accent); padding: 1rem 1.5rem; margin: 1rem 0; border-radius: 0 6px 6px 0; border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }
        .aside-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #b45309; padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .aside-box h4 { margin-top: 0; color: #b45309; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Week 2: Limits of Sequences | MTHS120</h1>
            <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Curriculum Index</a>
        </div>

        <div class="module-content">
            <div class="intro-lead">
                Welcome to Week 2 of MTHS120. In accordance with Topic 2 of the official lecture notes (Sections 4, 5, and 6), this module formalizes infinity and sequence convergence via the rigorous $\epsilon\text{-}N$ definition, limit arithmetic, the Squeeze Theorem, monotonic convergence to the supremum, and infinite limits.
            </div>

            <div class="toc-box">
                <h4>📌 Module Table of Contents</h4>
                <ul class="toc-grid">
                    <li><a href="#section-limits">1. Formal $\epsilon\text{–}N$ Convergence (§4)</a></li>
                    <li><a href="#section-theorems">2. Limit Theorems &amp; Arithmetic (§4)</a></li>
                    <li><a href="#section-supremum">3. Limits and Supremum (§5)</a></li>
                    <li><a href="#section-infinity">4. Infinity as a Limit (§6)</a></li>
                </ul>
            </div>

            <h2 id="section-limits">1. Formal $\epsilon\text{–}N$ Convergence (§4)</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Sequences &amp; Limits</h4>
                <div class="infobox-intro">
                    <strong>Don't be intimidated by the symbols!</strong> If upside-down A's ($\forall$), backward E's ($\exists$), or little ceiling brackets ($\lceil \dots \rceil$) look unfamiliar, that is completely normal. They are simply mathematicians' shorthand for everyday concepts.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$\forall$</span><span class="notation-desc">Universal quantifier: "for all" or "for every"</span></div>
                    <div class="notation-item"><span class="notation-sym">$\exists$</span><span class="notation-desc">Existential quantifier: "there exists"</span></div>
                    <div class="notation-item"><span class="notation-sym">$(a_n)$</span><span class="notation-desc">Sequence: an ordered list $(a_1, a_2, a_3, \dots)$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\lim_{n\to\infty} a_n = L$</span><span class="notation-desc">The sequence $a_n$ converges to limit $L$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\epsilon > 0$</span><span class="notation-desc">Arbitrary positive distance tolerance</span></div>
                    <div class="notation-item"><span class="notation-sym">$N \in \mathbb{N}$</span><span class="notation-desc">Cutoff index past which $|a_n - L| < \epsilon$</span></div>
                </div>
            </div>

            <p>A sequence $(a_n)$ converges to a limit $L$, written $\lim_{n\to\infty} a_n = L$, if:</p>
            <div class="definition-box">
                <p>$$\forall \epsilon > 0, \quad \exists N \in \mathbb{N} \quad \text{such that} \quad \forall n > N, \quad |a_n - L| < \epsilon$$</p>
            </div>

            <!-- CLAUSE STEPPER -->
            <div class="stepper-walkthrough" id="definition-walkthrough">
                <div class="telemetry-grid">
                    <div class="telemetry-card">
                        <span class="telemetry-label">Active Clause</span>
                        <span class="telemetry-badge" id="fw-tel-clause" style="color: #b45309;">1. The Challenge (∀ϵ > 0)</span>
                    </div>
                    <div class="telemetry-card">
                        <span class="telemetry-label">Quantifier</span>
                        <span class="telemetry-badge" id="fw-tel-quant" style="color: #0369a1;">Universal (∀)</span>
                    </div>
                    <div class="telemetry-card">
                        <span class="telemetry-label">Logical Role</span>
                        <span class="telemetry-badge" id="fw-tel-role" style="color: #be185d;">Given tolerance</span>
                    </div>
                    <div class="telemetry-card">
                        <span class="telemetry-label">Scope</span>
                        <span class="telemetry-badge" id="fw-tel-scope" style="color: #047857;">Arbitrary positive real</span>
                    </div>
                </div>

                <div class="formula-stage-wrap">
                    <div class="formula-display">
                        <div class="formula-chunk active" id="chunk-0" onclick="setFormulaStep(0)">$\forall \epsilon > 0$</div>
                        <span class="formula-sep">,</span>
                        <div class="formula-chunk" id="chunk-1" onclick="setFormulaStep(1)">$\exists N \in \mathbb{N}$</div>
                        <span class="formula-sep" style="font-size: 0.95rem; margin: 0 0.2rem;">such that</span>
                        <div class="formula-chunk" id="chunk-2" onclick="setFormulaStep(2)">$\forall n > N$</div>
                        <span class="formula-sep">,</span>
                        <div class="formula-chunk" id="chunk-3" onclick="setFormulaStep(3)">$|a_n - L| < \epsilon$</div>
                    </div>
                </div>

                <div class="canvas-container">
                    <svg id="fw-canvas" viewBox="0 0 740 180">
                        <line x1="50" y1="90" x2="690" y2="90" stroke="#94a3b8" stroke-dasharray="3" stroke-width="1.2"/>
                        <text x="700" y="94" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#64748b" font-weight="700">L</text>

                        <rect id="fw-svg-epsband" x="50" y="55" width="640" height="70" fill="#fde68a" opacity="0.3" stroke="#f59e0b" stroke-dasharray="4" stroke-width="1.2"/>
                        <text id="fw-svg-epslbl1" x="65" y="48" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#d97706" font-weight="bold">+ϵ</text>
                        <text id="fw-svg-epslbl2" x="65" y="142" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#d97706" font-weight="bold">-ϵ</text>

                        <line id="fw-svg-nline" x1="330" y1="20" x2="330" y2="160" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5" opacity="0.2"/>
                        <text id="fw-svg-nlbl" x="338" y="34" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#ef4444" font-weight="bold" opacity="0.2">Cutoff N</text>

                        <g id="fw-svg-pts">
                            <circle cx="120" cy="25" r="5" fill="#94a3b8" opacity="0.5"/>
                            <circle cx="190" cy="42" r="5" fill="#94a3b8" opacity="0.5"/>
                            <circle cx="260" cy="55" r="5" fill="#94a3b8" opacity="0.5"/>
                            <circle cx="330" cy="55" r="5" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
                            <circle cx="400" cy="74" r="6" fill="#10b981" id="pt-trapped-1"/>
                            <circle cx="470" cy="84" r="6" fill="#10b981" id="pt-trapped-2"/>
                            <circle cx="540" cy="88" r="6" fill="#10b981" id="pt-trapped-3"/>
                            <circle cx="610" cy="89" r="6" fill="#10b981" id="pt-trapped-4"/>
                        </g>
                    </svg>
                </div>

                <div class="controls-pane">
                    <div class="nav-buttons">
                        <button id="btn-fw-prev" onclick="stepFormula(-1)" disabled>Prev Clause</button>
                        <button id="btn-fw-next" onclick="stepFormula(1)">Next Clause</button>
                    </div>
                    <div class="step-summary" id="fw-step-summary"></div>
                    <div class="toggle-group">
                        <label for="fw-dimension-toggle" style="font-size: 0.85rem; font-weight: 700; color: #475569; display: block; margin-bottom: 0.5rem;">FRAMEWORK VIEW:</label>
                        <select id="fw-dimension-toggle" onchange="changeFormulaPerspective()">
                            <option value="adversarial">Adversarial Game (Skeptic vs. Prover)</option>
                            <option value="verification">Analogy: Software Specification</option>
                        </select>
                    </div>
                </div>

                <div class="analysis-panes">
                    <div class="pane">
                        <h4 id="fw-heading-what">Mathematical Mechanics</h4>
                        <div id="fw-pane-what"></div>
                    </div>
                    <div class="pane">
                        <h4 id="fw-heading-why">Logical Rationale</h4>
                        <div id="fw-pane-why"></div>
                    </div>
                </div>
            </div>

            <!-- QUANTIFIER ORDER & SCOPING -->
            <div class="scoping-box">
                <h4>💡 Quantifier Order and Dependency</h4>
                <p>Quantifiers are read from left to right, creating a clear dependency chain:</p>
                <table class="scoping-table">
                    <thead>
                        <tr><th>Variable</th><th>Scope</th><th>Dependency Rule</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>$\epsilon$</strong></td><td>$\forall \epsilon > 0$</td><td>Arbitrary positive tolerance, chosen independently of $N$.</td></tr>
                        <tr><td><strong>$N$</strong></td><td>$\exists N \in \mathbb{N}$</td><td>Chosen <em>after</em> inspecting $\epsilon$ ($N = N(\epsilon)$).</td></tr>
                        <tr><td><strong>$n$</strong></td><td>$\forall n > N$</td><td>Runs over all indices strictly past cutoff $N$.</td></tr>
                    </tbody>
                </table>
            </div>

            <div class="widget-instructions">
                <h4>📖 Guide: Exploring the &epsilon;–N Definition with $a_n = \frac{1}{n}$</h4>
                <p>This widget illustrates convergence for $\lim_{n\to\infty} \frac{1}{n} = 0$:</p>
                <ol>
                    <li><strong>Choose Tolerance ($\epsilon$):</strong> $\epsilon = 0.2$ ($N=5$), $\epsilon = 0.1$ ($N=10$), or $\epsilon = 0.05$ ($N=20$).</li>
                    <li><strong>Observe Cutoff ($N$):</strong> Marked by the red dashed line ($N = \lceil 1/\epsilon \rceil$).</li>
                    <li><strong>Step Forward:</strong> Trace terms entering the green interior past $N$.</li>
                </ol>
            </div>

            <!-- EPSILON CHALLENGE WIDGET -->
            <div class="game-box">
                <div class="game-header">
                    <span>Illustrating the Definition: $a_n = \frac{1}{n}$ ($L = 0$)</span>
                    <span>Finite Sample Visualization</span>
                </div>
                <div class="telemetry-grid" id="game-telemetry">
                    <div class="telemetry-card"><span class="telemetry-label">Sequence</span><span class="telemetry-badge" style="color: #0369a1;">$a_n = 1/n$ ($L = 0$)</span></div>
                    <div class="telemetry-card"><span class="telemetry-label">Tolerance (ϵ)</span><span class="telemetry-badge" id="cg-tel-eps" style="color: #b45309;">Select below</span></div>
                    <div class="telemetry-card"><span class="telemetry-label">Suitable Cutoff (N)</span><span class="telemetry-badge" id="cg-tel-reqn" style="color: #be185d;">—</span></div>
                    <div class="telemetry-card"><span class="telemetry-label">Term Displayed</span><span class="telemetry-badge" id="cg-tel-val" style="color: #334155;">—</span></div>
                    <div class="telemetry-card"><span class="telemetry-label">Status</span><span class="telemetry-badge" id="cg-tel-status" style="color: #64748b;">Standby</span></div>
                </div>
                <div class="game-body">
                    <div class="game-controls">
                        <button class="game-btn" onclick="startChallenge(0.2)">Test $\epsilon = 0.2$</button>
                        <button class="game-btn" onclick="startChallenge(0.1)">Test $\epsilon = 0.1$</button>
                        <button class="game-btn" onclick="startChallenge(0.05)">Test $\epsilon = 0.05$</button>
                    </div>
                    <div class="game-canvas-wrap">
                        <svg id="game-plot" viewBox="0 0 740 260">
                            <text x="260" y="130" font-family="ui-sans-serif, system-ui, sans-serif" font-size="14" fill="#64748b">Select an &epsilon; budget above to illustrate the sample.</text>
                        </svg>
                    </div>
                    <div class="game-controls" id="step-controls" style="display: none;">
                        <button class="game-btn" id="btn-challenge-next" onclick="advanceChallengeStep()">Step Forward ($n = N + 1$)</button>
                        <button class="game-btn" style="background-color: #64748b;" onclick="resetChallenge()">Reset</button>
                    </div>
                </div>
            </div>

            <h2 id="section-theorems">2. Limit Theorems &amp; Arithmetic (§4)</h2>
            <p>Theorem 1 establishes that if $(a_n) \to K$ and $(b_n) \to L$, then sums ($K \pm L$), scalar multiples ($cK$), products ($KL$), and quotients ($K/L$ for $L \neq 0$) converge accordingly. The <strong>Squeeze Theorem</strong> (Theorem 4) proves that if $a_n \le b_n \le c_n$ and $\lim a_n = \lim c_n = L$, then $\lim b_n = L$.</p>

            <h2 id="section-supremum">3. Limits and Supremum (§5)</h2>
            <p>Theorem 2 establishes the Monotone Convergence Theorem: Any increasing sequence that is bounded above converges, and its limit equals its supremum ($\lim a_n = \sup\{a_n\}$). This connects set completeness directly to analysis.</p>

            <h2 id="section-infinity">4. Infinity as a Limit (§6)</h2>
            <p>A sequence tends to infinity ($\lim a_n = \infty$) if for any large $M$, all terms past some index $N$ satisfy $a_n > M$. Unbounded increasing sequences diverge to infinity (Proposition 7).</p>
        </div>
    </div>

    <script>
        const formulaState = { step: 0, perspective: 'adversarial' };
        const formulaClauses = [
            {
                clauseTitle: "1. The Challenge (∀ϵ > 0)", quantifier: "Universal (∀)", advRole: "Given tolerance", advScope: "Arbitrary positive real",
                advSummary: "<strong>Step 1: Establishing tolerance.</strong> Consider any arbitrary positive distance $\\epsilon > 0$.",
                advWhat: "<p>We are given an arbitrary number $\\epsilon > 0$, forming a neighborhood $(L - \\epsilon, L + \\epsilon)$ around the limit.</p>",
                advWhy: "<p>Requiring the condition to hold for all positive $\\epsilon$ prevents oscillations away from $L$.</p>",
                verRole: "Test constraint", verScope: "Parameter specification", verSummary: "Analogy parameter.",
                verWhat: "<p>Input accuracy specification.</p>", verWhy: "<p>Stable systems satisfy arbitrary tolerances.</p>"
            },
            {
                clauseTitle: "2. The Response (∃N ∈ ℕ)", quantifier: "Existential (∃)", advRole: "Finding a witness index", advScope: "Dependent on ϵ",
                advSummary: "<strong>Step 2: Identifying cutoff index N.</strong> An integer $N$ exists past which terms stay within tolerance.",
                advWhat: "<p>For $a_n = 1/n$, one convenient choice is $N = \\lceil 1/\\epsilon \\rceil$.</p>",
                advWhy: "<p>Allows $N$ to depend directly on $\\epsilon$.</p>",
                verRole: "Bound synthesis", verScope: "Latency cutoff", verSummary: "Analogy cutoff.",
                verWhat: "<p>Execution cycle cutoff.</p>", verWhy: "<p>Ensures compliance.</p>"
            },
            {
                clauseTitle: "3. The Tail Scope (∀n > N)", quantifier: "Universal (∀)", advRole: "Evaluation of the tail", advScope: "All subsequent indices",
                advSummary: "<strong>Step 3: Examining all terms past N.</strong> Every term with index $n > N$ satisfies the distance condition.",
                advWhat: "<p>We evaluate all indices strictly past $N$ ($n = N+1, N+2, \dots$).</p>",
                advWhy: "<p>Convergence is a property of the long-term tail.</p>",
                verRole: "Suffix invariant", verScope: "Steady-state", verSummary: "Analogy tail check.",
                verWhat: "<p>Checking steady-state execution.</p>", verWhy: "<p>Initial transients do not affect convergence.</p>"
            },
            {
                clauseTitle: "4. The Distance Condition (|aₙ - L| < ϵ)", quantifier: "Inequality (<)", advRole: "Proximity condition", advScope: "Distance inside band",
                advSummary: "<strong>Step 4: Confirming distance constraint.</strong> For all $n > N$, $|a_n - L| < \\epsilon$.",
                advWhat: "<p>Each term $a_n$ with $n > N$ sits strictly within $(L - \\epsilon, L + \\epsilon)$.</p>",
                advWhy: "<p>Proves mathematically that $\\lim a_n = L$.</p>",
                verRole: "Invariant assertion", verScope: "Safety check", verSummary: "Analogy assertion.",
                verWhat: "<p>Assertion check evaluated on outputs.</p>", verWhy: "<p>Metric distance provides proximity.</p>"
            }
        ];

        function setFormulaStep(stepIdx) { formulaState.step = stepIdx; updateFormulaUI(); }
        function stepFormula(dir) {
            formulaState.step += dir;
            if (formulaState.step < 0) formulaState.step = 0;
            if (formulaState.step > 3) formulaState.step = 3;
            updateFormulaUI();
        }
        function changeFormulaPerspective() {
            formulaState.perspective = document.getElementById('fw-dimension-toggle').value;
            updateFormulaUI();
        }
        function updateFormulaUI() {
            const idx = formulaState.step;
            const current = formulaClauses[idx];
            const isAdv = (formulaState.perspective === 'adversarial');
            for (let i = 0; i < 4; i++) {
                const el = document.getElementById(`chunk-${i}`);
                el.classList.remove('active', 'completed');
                if (i === idx) el.classList.add('active');
                else if (i < idx) el.classList.add('completed');
            }
            document.getElementById('fw-tel-clause').innerText = current.clauseTitle;
            document.getElementById('fw-tel-quant').innerText = current.quantifier;
            document.getElementById('fw-tel-role').innerText = isAdv ? current.advRole : current.verRole;
            document.getElementById('fw-tel-scope').innerText = isAdv ? current.advScope : current.verScope;
            document.getElementById('btn-fw-prev').disabled = (idx === 0);
            document.getElementById('btn-fw-next').disabled = (idx === 3);
            document.getElementById('fw-heading-what').innerText = isAdv ? "Mathematical Mechanics" : "Software Analogy Mechanics";
            document.getElementById('fw-heading-why').innerText = isAdv ? "Logical Rationale" : "Analogy Context";
            document.getElementById('fw-step-summary').innerHTML = isAdv ? current.advSummary : current.verSummary;
            document.getElementById('fw-pane-what').innerHTML = isAdv ? current.advWhat : current.verWhat;
            document.getElementById('fw-pane-why').innerHTML = isAdv ? current.advWhy : current.verWhy;
            if (window.renderMathInElement) {
                renderMathInElement(document.getElementById('definition-walkthrough'), { delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}] });
            }
            updateFormulaCanvas(idx);
        }
        function updateFormulaCanvas(step) {
            const epsBand = document.getElementById('fw-svg-epsband');
            const nLine = document.getElementById('fw-svg-nline');
            const nLbl = document.getElementById('fw-svg-nlbl');
            epsBand.setAttribute('opacity', step === 0 ? '0.6' : '0.35');
            nLine.setAttribute('opacity', step >= 1 ? '1' : '0.2');
            nLbl.setAttribute('opacity', step >= 1 ? '1' : '0.2');
        }

        const challengeState = { active: false, eps: 0.2, reqN: 5, currentDisplayN: 5 };
        function startChallenge(eps) {
            challengeState.active = true;
            challengeState.eps = eps;
            challengeState.reqN = Math.ceil(1 / eps);
            challengeState.currentDisplayN = challengeState.reqN;
            document.getElementById('step-controls').style.display = 'flex';
            updateChallengeUI();
        }
        function advanceChallengeStep() {
            challengeState.currentDisplayN++;
            if (challengeState.currentDisplayN > 30) challengeState.currentDisplayN = 30;
            updateChallengeUI();
        }
        function resetChallenge() {
            challengeState.active = false;
            document.getElementById('step-controls').style.display = 'none';
            document.getElementById('cg-tel-eps').innerText = 'Select below';
            document.getElementById('cg-tel-reqn').innerText = '—';
            document.getElementById('cg-tel-val').innerText = '—';
            document.getElementById('cg-tel-status').innerText = 'Standby';
            renderGameSVG(null, 0, 0);
        }
        function updateChallengeUI() {
            const eps = challengeState.eps;
            const reqN = challengeState.reqN;
            const curN = challengeState.currentDisplayN;
            const atTerm = (1 / curN);
            document.getElementById('cg-tel-eps').innerHTML = `$${eps}$`;
            document.getElementById('cg-tel-reqn').innerHTML = `$N = ${reqN}$`;
            document.getElementById('cg-tel-val').innerHTML = `$a_{${curN}} = ${atTerm.toFixed(3)}$`;
            document.getElementById('cg-tel-status').innerHTML = curN > reqN ? `Inside (+${(eps - atTerm).toFixed(3)})` : `Boundary/Outside`;
            if(window.renderMathInElement) {
                renderMathInElement(document.getElementById('game-telemetry'), { delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}] });
            }
            renderGameSVG(eps, reqN, curN);
        }
        function renderGameSVG(eps, reqN, curN) {
            const svg = document.getElementById('game-plot');
            const originX = 90, originY = 130, maxXScale = 610;
            let svgContent = `<line x1="${originX}" y1="${originY}" x2="${originX + maxXScale}" y2="${originY}" stroke="#64748b" stroke-width="1.0"/><text x="${originX - 35}" y="${originY + 5}" font-family="sans-serif" font-size="12" font-weight="700" fill="#64748b">L=0</text><line x1="${originX}" y1="240" x2="${originX}" y2="25" stroke="#64748b" stroke-width="1.0"/><line x1="${originX}" y1="${originY}" x2="715" y2="${originY}" stroke="#64748b" stroke-width="1.0"/>`;
            if (eps === null) {
                svg.innerHTML = svgContent + `<text x="260" y="130" font-family="sans-serif" font-size="14" fill="#64748b">Select an &epsilon; budget above.</text>`;
                return;
            }
            const maxN = Math.max(14, reqN + 4);
            const scaleFactor = eps <= 0.05 ? 900 : (eps <= 0.1 ? 550 : 220);
            const topY = originY - (eps * scaleFactor), bottomY = originY + (eps * scaleFactor);
            svgContent += `<rect x="${originX}" y="${topY}" width="${maxXScale}" height="${bottomY - topY}" fill="#fef3c7" opacity="0.8"/><line x1="${originX}" y1="${topY}" x2="${originX + maxXScale}" y2="${topY}" stroke="#d97706" stroke-dasharray="4"/><line x1="${originX}" y1="${bottomY}" x2="${originX + maxXScale}" y2="${bottomY}" stroke="#d97706" stroke-dasharray="4"/>`;
            for (let n = 1; n <= curN; n++) {
                const val = 1 / n, cx = originX + (n * (maxXScale / maxN)), cy = originY - (val * scaleFactor);
                const inside = n > reqN;
                svgContent += `<circle cx="${cx}" cy="${cy}" r="${inside ? 7 : 5}" fill="${inside ? '#10b981' : '#d97706'}"/>`;
            }
            const thresholdX = originX + (reqN * (maxXScale / maxN));
            svgContent += `<line x1="${thresholdX}" y1="20" x2="${thresholdX}" y2="240" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="4"/><text x="${thresholdX + 6}" y="32" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ef4444">N = ${reqN}</text>`;
            svg.innerHTML = svgContent;
        }

        setFormulaStep(0);
        renderGameSVG(null, 0, 0);
    </script>
</body>
</html>
"""
    with open('week2.html', 'w') as f:
        f.write(week2_content)

def update_index():
    if not os.path.exists('index.html'):
        return
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_week2 = """<!-- Week 2 -->
                <div class="week-card">
                    <div>
                        <h4>Week 2 <span class="week-badge">Planned</span></h4>
                        <div class="week-meta">Topic 2 &bull; Sections 4, 5, 6</div>
                        <p><strong>Limits of Sequences:</strong> The formal $\\epsilon\\text{–}N$ definition of sequence limits, limit arithmetic, the Squeeze Theorem, convergence to the supremum, and infinite limits ($n \\to \\infty$).</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>"""

    new_week2 = """<!-- Week 2 -->
                <div class="week-card">
                    <div>
                        <h4>Week 2 <span class="week-badge active">Available</span></h4>
                        <div class="week-meta">Topic 2 &bull; Sections 4, 5, 6</div>
                        <p><strong>Limits of Sequences:</strong> The formal $\\epsilon\\text{–}N$ definition of sequence limits, limit arithmetic, the Squeeze Theorem, convergence to the supremum, and infinite limits ($n \\to \\infty$).</p>
                    </div>
                    <a href="week2.html" class="module-link">Open Module 2 &rarr;</a>
                </div>"""

    if old_week2 in content:
        content = content.replace(old_week2, new_week2)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)

def execute_git_sync():
    commit_message = (
        "Remove citation markers from course web pages and scripts\n\n"
        "Stripped out all reference tags from week1.html, week2.html,\n"
        "and update.py to maintain clean coursework material formatting."
    )
    commands = [
        ['git', 'add', 'week1.html', 'week2.html', 'index.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    write_clean_modules()
    update_index()
    execute_git_sync()
