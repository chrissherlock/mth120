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
            --bg: #f8fafc; --text: #0f172a; --card: #ffffff; --border: #cbd5e1;
            --accent: #d97706; --accent-hover: #b45309;
            --telemetry-bg: #0f172a; --telemetry-text: #fbbf24;
            --track1-bg: #fffbeb; --track2-bg: #fff7ed;
        }
        body { font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; }
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .intro-lead { font-size: 1.1rem; color: #1e293b; line-height: 1.7; margin-bottom: 1.5rem; background: #f1f5f9; padding: 1.5rem; border-radius: 6px; border-left: 4px solid var(--accent); border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }
        .intro-graphic { background: #090d16; border-radius: 8px; padding: 1.5rem; display: flex; justify-content: center; margin-bottom: 2.5rem; box-shadow: inset 0 2px 4px rgba(0,0,0,0.4); border: 1px solid #334155; }

        h2 { border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; margin-top: 2.5rem; color: #0f172a; }
        h3 { color: #1e293b; margin-top: 1.5rem; }

        /* Diagram Container Styles */
        .diagram-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0; }
        .diagram-card { background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; display: flex; flex-direction: column; align-items: center; min-width: 0; }
        .diagram-card h5 { margin: 0 0 0.75rem 0; color: #b45309; font-size: 0.95rem; text-align: center; white-space: nowrap; }

        /* Dual-Track Layout */
        .dual-track-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 1.5rem; margin-bottom: 2rem; }
        .track-card { padding: 1.5rem; border-radius: 6px; border: 1px solid var(--border); }
        .track-formal { background: var(--track1-bg); border-color: #fde68a; }
        .track-applied { background: var(--track2-bg); border-color: #fed7aa; }
        .track-card h4 { margin-top: 0; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; color: #b45309; }

        /* Interactive Simulator & Game Styles */
        .simulator, .game-box { border: 1px solid var(--border); border-radius: 8px; overflow: hidden; margin-top: 2rem; background: var(--card); box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
        .game-header { background: #0f172a; color: #fbbf24; padding: 1rem 1.5rem; font-family: monospace; font-size: 0.95rem; display: flex; justify-content: space-between; align-items: center; }
        .game-body { padding: 1.5rem; background: #f8fafc; display: flex; flex-direction: column; gap: 1rem; border-bottom: 1px solid var(--border); }
        .game-explainer { background: #fef3c7; border: 1px solid #fde68a; padding: 1.25rem; border-radius: 6px; font-size: 0.95rem; color: #92400e; margin-bottom: 0.5rem; line-height: 1.7; }
        .game-controls { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; }
        .game-btn { background: var(--accent); color: white; border: none; padding: 0.5rem 1rem; border-radius: 4px; cursor: pointer; font-weight: bold; transition: background 0.2s; }
        .game-btn:hover { background: var(--accent-hover); }
        .game-btn:disabled { background: #94a3b8; cursor: not-allowed; }
        .game-canvas-wrap { background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; display: flex; justify-content: center; }

        .telemetry { background: var(--telemetry-bg); color: var(--telemetry-text); padding: 0.75rem 1.5rem; font-family: monospace; display: flex; gap: 2rem; font-size: 0.9rem; align-items: center;}
        .canvas-container { padding: 2rem; background: #f1f5f9; display: flex; justify-content: center; border-bottom: 1px solid var(--border); }
        .controls-pane { display: flex; gap: 2rem; padding: 1.5rem; background: var(--card); border-bottom: 1px solid var(--border); align-items: flex-start; }
        .nav-buttons { display: flex; flex-direction: column; gap: 0.5rem; min-width: 120px; }
        button { background: var(--accent); color: white; border: none; padding: 0.5rem 1rem; border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%; transition: background 0.2s; }
        button:hover { background: var(--accent-hover); }
        button:disabled { background: #94a3b8; cursor: not-allowed; }
        .step-summary { flex-grow: 1; font-size: 0.95rem; color: #334155; line-height: 1.5; }
        .pane { background: var(--card); padding: 1.5rem; }
        .pane h4 { margin-top: 0; color: var(--accent); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem; }
        .pane p { margin: 0 0 0.75rem 0; }
        .pane p:last-child { margin-bottom: 0; }
        .toggle-group { min-width: 220px; }
        select { width: 100%; padding: 0.5rem; border-radius: 4px; border: 1px solid var(--border); font-family: system-ui, sans-serif; background: #fff; color: var(--text); }

        .definition-box { background: #f8fafc; border-left: 4px solid var(--accent); padding: 1rem 1.5rem; margin: 1rem 0; border-radius: 0 6px 6px 0; border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }
        .aside-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #b45309; padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .aside-box h4 { margin-top: 0; color: #b45309; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }
        .example-list li { margin-bottom: 0.75rem; }
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
                Welcome to Week 1 of MTHS120. Before we can analyze continuous change, accumulation, and rates of variation, we must first master the language used to construct the mathematical universe. This module bridges discrete foundational concepts—starting with set theory notation and the hierarchical expansion of our number systems—into the rigorous study of sequences and limits. By examining both abstract formal definitions and their practical numerical behaviors side by side, you will build the analytical intuition necessary to navigate real analysis with confidence.
            </div>

            <!-- DECORATIVE TOPIC ILLUSTRATION SVG -->
            <div class="intro-graphic">
                <svg width="700" height="140" viewBox="0 0 700 140">
                    <g transform="translate(30, 10)">
                        <rect x="0" y="0" width="180" height="120" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
                        <circle cx="70" cy="60" r="35" fill="#d97706" opacity="0.35"/>
                        <circle cx="110" cy="60" r="35" fill="#fbbf24" opacity="0.35"/>
                        <text x="50" y="65" font-family="sans-serif" font-size="11" fill="#ffffff" font-weight="bold">A</text>
                        <text x="120" y="65" font-family="sans-serif" font-size="11" fill="#ffffff" font-weight="bold">B</text>
                        <text x="90" y="105" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Set Theory (A ∪ B)</text>
                    </g>
                    <g transform="translate(240, 10)">
                        <rect x="0" y="0" width="200" height="120" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
                        <rect x="15" y="15" width="170" height="90" rx="6" fill="none" stroke="#fbbf24" stroke-dasharray="3"/>
                        <text x="25" y="30" font-family="sans-serif" font-size="10" fill="#fbbf24">ℝ (Real)</text>
                        <rect x="35" y="38" width="130" height="60" rx="4" fill="none" stroke="#d97706"/>
                        <text x="45" y="52" font-family="sans-serif" font-size="10" fill="#d97706">ℚ ⊃ ℤ ⊃ ℕ</text>
                        <circle cx="100" cy="78" r="14" fill="#d97706" opacity="0.45"/>
                        <text x="100" y="82" font-family="sans-serif" font-size="10" fill="#ffffff" font-weight="bold" text-anchor="middle">ℕ</text>
                        <text x="100" y="112" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Number Systems</text>
                    </g>
                    <g transform="translate(470, 10)">
                        <rect x="0" y="0" width="200" height="120" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
                        <line x1="20" y1="90" x2="180" y2="90" stroke="#64748b" stroke-width="1" stroke-dasharray="2"/>
                        <text x="175" y="86" font-family="sans-serif" font-size="9" fill="#fbbf24">L=0</text>
                        <circle cx="40" cy="40" r="4" fill="#d97706"/><line x1="40" y1="40" x2="70" y2="60" stroke="#d97706" stroke-width="1.5"/>
                        <circle cx="70" cy="60" r="4" fill="#d97706"/><line x1="70" y1="60" x2="100" y2="75" stroke="#d97706" stroke-width="1.5"/>
                        <circle cx="100" cy="75" r="4" fill="#d97706"/><line x1="100" y1="75" x2="130" y2="83" stroke="#d97706" stroke-width="1.5"/>
                        <circle cx="130" cy="83" r="4" fill="#10b981"/><line x1="130" y1="83" x2="160" y2="87" stroke="#10b981" stroke-width="1.5"/>
                        <circle cx="160" cy="87" r="5" fill="#10b981"/>
                        <text x="100" y="112" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Sequence Limits (aₙ → L)</text>
                    </g>
                </svg>
            </div>

            <h2>1. Set Theory Foundations</h2>
            <p>Before we can do calculus, we need a precise, unambiguous language to talk about collections of mathematical objects. A <strong>set</strong> is any well-defined collection of objects, called <em>elements</em> or <em>members</em>. If $x$ is an element of set $A$, we write $x \in A$; otherwise, $x \notin A$.</p>

            <div class="definition-box">
                <p><strong>Fundamental Ways to Specify Sets:</strong></p>
                <ul>
                    <li><strong>Roster Notation:</strong> Explicitly listing members within braces, e.g., $A = \{2, 3, 5, 7\}$ (the set of the first four prime numbers).</li>
                    <li><strong>Set-Builder Notation:</strong> Defining members by a logical predicate rule: $B = \{ x \in \mathbb{N} \mid x \text{ is prime and } x < 10 \}$.</li>
                </ul>
            </div>

            <h3>Subsets and Power Sets</h3>
            <p>Let $A$ and $B$ be sets. If every element of $A$ is also contained within $B$, we say $A$ is a <strong>subset</strong> of $B$, denoted $A \subseteq B$. If $A \subseteq B$ but $A \neq B$, $A$ is a <em>proper subset</em> ($A \subset B$). The <strong>power set</strong> of $A$, denoted $\mathcal{P}(A)$ or $2^A$, is the set of <em>all</em> subsets of $A$ (including the empty set $\emptyset$ and $A$ itself).</p>

            <div class="diagram-grid">
                <div class="diagram-card">
                    <h5>Subset Inclusion ($A \subseteq B$)</h5>
                    <svg width="240" height="110" viewBox="0 0 240 110">
                        <rect x="10" y="10" width="220" height="90" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
                        <text x="20" y="25" font-family="sans-serif" font-size="10" fill="#64748b">Universal Set U</text>
                        <ellipse cx="120" cy="60" rx="90" ry="35" fill="#fed7aa" opacity="0.4" stroke="#d97706" stroke-width="1.5"/>
                        <text x="185" y="70" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold">B</text>
                        <ellipse cx="90" cy="60" rx="45" ry="25" fill="#fde68a" opacity="0.6" stroke="#d97706" stroke-width="1.5"/>
                        <text x="85" y="64" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold">A</text>
                    </svg>
                </div>
                <div class="diagram-card">
                    <h5>Complement ($A^c = U \setminus A$)</h5>
                    <svg width="240" height="110" viewBox="0 0 240 110">
                        <rect x="10" y="10" width="220" height="90" rx="6" fill="#fef3c7" opacity="0.5" stroke="#cbd5e1" stroke-width="1.5"/>
                        <text x="20" y="25" font-family="sans-serif" font-size="10" fill="#92400e">Aᶜ (Complement Region)</text>
                        <circle cx="120" cy="60" r="32" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
                        <text x="115" y="64" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold">A</text>
                    </svg>
                </div>
            </div>

            <h3>Core Set Operations Visualized</h3>
            <p>Sets interact through algebra-like operations governed by rigorous logical connectives:</p>

            <div class="diagram-grid">
                <div class="diagram-card">
                    <h5>Union ($A \cup B$) &mdash; "Or"</h5>
                    <svg width="240" height="110" viewBox="0 0 240 110">
                        <rect x="10" y="10" width="220" height="90" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
                        <text x="20" y="25" font-family="sans-serif" font-size="10" fill="#64748b">Combined Elements</text>
                        <circle cx="95" cy="60" r="35" fill="#fed7aa" opacity="0.6" stroke="#d97706" stroke-width="1.5"/>
                        <circle cx="145" cy="60" r="35" fill="#fed7aa" opacity="0.6" stroke="#d97706" stroke-width="1.5"/>
                        <text x="85" y="64" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold">A</text>
                        <text x="150" y="64" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold">B</text>
                    </svg>
                </div>
                <div class="diagram-card">
                    <h5>Intersection ($A \cap B$) &mdash; "And"</h5>
                    <svg width="240" height="110" viewBox="0 0 240 110">
                        <rect x="10" y="10" width="220" height="90" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
                        <text x="20" y="25" font-family="sans-serif" font-size="10" fill="#64748b">Shared Overlap</text>
                        <circle cx="95" cy="60" r="35" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
                        <circle cx="145" cy="60" r="35" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
                        <path d="M 120 35 A 35 35 0 0 1 120 85 A 35 35 0 0 1 120 35 Z" fill="#d97706" opacity="0.6"/>
                        <text x="85" y="64" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold">A</text>
                        <text x="150" y="64" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold">B</text>
                    </svg>
                </div>
            </div>

            <h3>Cartesian Products ($A \times B$)</h3>
            <p>The Cartesian product pairs elements from two sets into ordered pairs:
            $$A \times B = \{ (a, b) \mid a \in A \text{ and } b \in B \}$$
            When $A = \mathbb{R}$ and $B = \mathbb{R}$, this operation constructs the familiar 2D coordinate plane $\mathbb{R}^2$.</p>

            <div class="diagram-card" style="margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
                <h5>Discrete Cartesian Grid ($A = \{1,2,3\} \times B = \{1,2\}$)</h5>
                <svg width="300" height="130" viewBox="0 0 300 130">
                    <line x1="50" y1="100" x2="270" y2="100" stroke="#64748b" stroke-width="1.5"/>
                    <line x1="70" y1="110" x2="70" y2="20" stroke="#64748b" stroke-width="1.5"/>
                    <text x="275" y="104" font-family="sans-serif" font-size="10" fill="#64748b">A</text>
                    <text x="65" y="15" font-family="sans-serif" font-size="10" fill="#64748b">B</text>
                    <circle cx="110" cy="80" r="5" fill="#d97706"/><text x="118" y="83" font-family="sans-serif" font-size="9" fill="#0f172a">(1,1)</text>
                    <circle cx="160" cy="80" r="5" fill="#d97706"/><text x="168" y="83" font-family="sans-serif" font-size="9" fill="#0f172a">(2,1)</text>
                    <circle cx="210" cy="80" r="5" fill="#d97706"/><text x="218" y="83" font-family="sans-serif" font-size="9" fill="#0f172a">(3,1)</text>
                    <circle cx="110" cy="45" r="5" fill="#d97706"/><text x="118" y="48" font-family="sans-serif" font-size="9" fill="#0f172a">(1,2)</text>
                    <circle cx="160" cy="45" r="5" fill="#d97706"/><text x="168" y="48" font-family="sans-serif" font-size="9" fill="#0f172a">(2,2)</text>
                    <circle cx="210" cy="45" r="5" fill="#d97706"/><text x="218" y="48" font-family="sans-serif" font-size="9" fill="#0f172a">(3,2)</text>
                </svg>
            </div>

            <h3>Anatomy of Set-Builder Notation</h3>
            <p>When dealing with infinite or continuous sets where listing elements is impossible, we use <strong>set-builder notation</strong>. This defines a set by stating the properties that its members must satisfy rather than listing them explicitly.</p>

            <div class="definition-box">
                <p><strong>Standard Structure:</strong></p>
                <p>$$A = \{ x \in S \mid P(x) \}$$</p>
                <ul>
                    <li><strong>$x$ (The Variable):</strong> Represents an arbitrary candidate element.</li>
                    <li><strong>$\in S$ (The Domain):</strong> The universal number system or set where candidates are drawn from (e.g., $x \in \mathbb{R}$).</li>
                    <li><strong>$\mid$ or $:$ (The Separator):</strong> Read aloud as <strong>"such that"</strong>. It acts as a strict logical filter.</li>
                    <li><strong>$P$ (The Predicate):</strong> The rule, equation, or inequality that $x$ must satisfy to gain membership.</li>
                </ul>
            </div>

            <h3>Step-by-Step Translation Examples</h3>
            <ul class="example-list">
                <li><strong>Finite Set (Even Numbers):</strong> <br>
                    $A = \{ n \in \mathbb{N} \mid n \text{ is even and } n < 10 \}$ <br>
                    <em>Translation:</em> "The set of all natural numbers $n$ such that $n$ is even and strictly less than 10" $\rightarrow \{2, 4, 6, 8\}$.</li>
                <li><strong>Continuous Interval (Inequalities):</strong> <br>
                    $B = \{ x \in \mathbb{R} \mid 1 \leq x < 5 \}$ <br>
                    <em>Translation:</em> "The set of all real numbers $x$ such that $x$ is greater than or equal to 1 and strictly less than 5" $\rightarrow [1, 5)$.</li>
                <li><strong>Transformed Elements:</strong> <br>
                    $C = \{ y \in \mathbb{R} \mid y = x^2 \text{ for some } x \in \mathbb{Z} \}$ <br>
                    <em>Translation:</em> "The set of all real numbers $y$ such that $y$ equals the square of some integer $x$" $\rightarrow \{0, 1, 4, 9, 16, \dots\}$.</li>
            </ul>

            <h3>Common Beginner Pitfalls</h3>
            <ul>
                <li><strong>Domain vs. Condition Confusion:</strong> The expression <em>before</em> the vertical bar tells you where you are looking (the pool of candidates); the expression <em>after</em> tells you who qualifies (the filter).</li>
                <li><strong>Redundant Restrictions:</strong> Writing $\{x \mid x \in \mathbb{R}\}$ is simply shorthand for the entire set of real numbers $\mathbb{R}$.</li>
            </ul>

            <h2>2. The Hierarchy of Number Systems</h2>
            <p>Mathematics constructs its universe of numbers step by step, algebraically expanding systems to solve equations and geometric problems that previous systems could not express. Each expansion resolves an <strong>algebraic closure failure</strong> of the previous system.</p>

            <div class="diagram-card" style="margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
                <h5>Nested Set Containment Hierarchy ($\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ )</h5>
                <svg width="520" height="150" viewBox="0 0 520 150">
                    <rect x="10" y="10" width="500" height="130" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
                    <text x="20" y="28" font-family="sans-serif" font-size="11" fill="#64748b" font-weight="bold">ℝ (Real Numbers: All terminating, repeating & non-repeating decimals)</text>

                    <rect x="35" y="38" width="450" height="92" rx="6" fill="#fffbeb" stroke="#fde68a" stroke-width="1.5"/>
                    <text x="45" y="54" font-family="sans-serif" font-size="10" fill="#92400e" font-weight="bold">ℚ (Rational Numbers: Fractions p/q)</text>

                    <rect x="65" y="62" width="390" height="60" rx="6" fill="#fef3c7" stroke="#fbbf24" stroke-width="1.5"/>
                    <text x="75" y="78" font-family="sans-serif" font-size="10" fill="#b45309" font-weight="bold">ℤ (Integers: Negatives, 0, Positives)</text>

                    <ellipse cx="260" cy="100" rx="140" ry="18" fill="#fed7aa" stroke="#d97706" stroke-width="1.5"/>
                    <text x="260" y="104" font-family="sans-serif" font-size="10" fill="#b45309" font-weight="bold" text-anchor="middle">ℕ (Natural Numbers: 1, 2, 3...)</text>
                </svg>
            </div>

            <!-- ALGEBRAIC STRUCTURES ASIDE -->
            <div class="aside-box">
                <h4>💡 Aside: What is a Group, Ring, and Field?</h4>
                <p>In abstract algebra, mathematicians classify number systems by the rules their operations obey:</p>
                <ul>
                    <li><strong>Additive Group ($\mathbb{Z}$):</strong> A set with an operation (addition) that is associative, has an identity element ($0$), and where every element has an opposite/inverse (e.g., $5 + (-5) = 0$).</li>
                    <li><strong>Commutative Ring ($\mathbb{Z}$):</strong> A system equipped with <em>two</em> operations (addition and multiplication). Addition forms a group, multiplication is associative and commutative ($a \times b = b \times a$), and multiplication distributes over addition ($a(b+c) = ab + ac$). However, multiplicative inverses (reciprocals) are not guaranteed (e.g., $3 \times x = 1$ has no integer solution).</li>
                    <li><strong>Field ($\mathbb{Q}, \mathbb{R}$):</strong> A ring where <em>every</em> non-zero element also possesses a multiplicative inverse (reciprocal), meaning you can freely divide by any non-zero number without escaping the system.</li>
                </ul>
                <p style="margin-top: 1rem;"><a href="algebraic_structures.html" style="color: var(--accent); font-weight: bold; text-decoration: none;">&rarr; Explore our Interactive Deep Dive on Groups, Rings, and Fields</a></p>
            </div>

            <h3>Natural Numbers ($\mathbb{N}$): The Counting Foundation</h3>
            <p>We begin with $\mathbb{N} = \{1, 2, 3, 4, \dots\}$ (sometimes including $0$). <strong>Algebraic Property:</strong> Closed under addition and multiplication (combining any two natural numbers always yields another natural number). <strong>Limitation:</strong> Not closed under subtraction. Attempting to solve $x + 5 = 2$ forces us outside $\mathbb{N}$ because negative numbers do not exist here.</p>

            <h3>Integers ($\mathbb{Z}$): Adding Inverses</h3>
            <p>To resolve subtraction failures, we adjoin additive inverses and zero, forming $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$. <strong>Algebraic Property:</strong> Forms an additive group and a commutative ring. <strong>Limitation:</strong> Not closed under division. Attempting to solve $2x = 3$ yields $x = \frac{3}{2}$, which has no solution inside $\mathbb{Z}$.</p>

            <div class="diagram-grid">
                <div class="diagram-card">
                    <h5>Algebraic Failure: Subtraction in $\mathbb{N}$</h5>
                    <svg width="240" height="120" viewBox="0 0 240 120">
                        <rect x="10" y="10" width="220" height="100" rx="6" fill="#fffbeb" stroke="#fde68a" stroke-width="1.5"/>
                        <text x="20" y="32" font-family="sans-serif" font-size="11" fill="#0f172a" font-weight="bold">1. Equation: x + 5 = 2</text>
                        <text x="20" y="55" font-family="sans-serif" font-size="11" fill="#0f172a">2. Isolate x: x = 2 - 5</text>
                        <text x="20" y="78" font-family="sans-serif" font-size="11" fill="#ef4444" font-weight="bold">3. Result: x = -3 ∉ ℕ</text>
                        <text x="20" y="100" font-family="sans-serif" font-size="10" fill="#b45309" font-weight="bold">→ Solution: Expand to ℤ</text>
                    </svg>
                </div>
                <div class="diagram-card">
                    <h5>Algebraic Failure: Division in $\mathbb{Z}$</h5>
                    <svg width="240" height="120" viewBox="0 0 240 120">
                        <rect x="10" y="10" width="220" height="100" rx="6" fill="#fffbeb" stroke="#fde68a" stroke-width="1.5"/>
                        <text x="20" y="32" font-family="sans-serif" font-size="11" fill="#0f172a" font-weight="bold">1. Equation: 2x = 3</text>
                        <text x="20" y="55" font-family="sans-serif" font-size="11" fill="#0f172a">2. Isolate x: x = 3 / 2</text>
                        <text x="20" y="78" font-family="sans-serif" font-size="11" fill="#ef4444" font-weight="bold">3. Result: x = 1.5 ∉ ℤ</text>
                        <text x="20" y="100" font-family="sans-serif" font-size="10" fill="#b45309" font-weight="bold">→ Solution: Expand to ℚ</text>
                    </svg>
                </div>
            </div>

            <h3>Rational Numbers ($\mathbb{Q}$): The Field of Ratios</h3>
            <p>We expand our universe to quotients of integers: $\mathbb{Q} = \{ \frac{p}{q} \mid p, q \in \mathbb{Z}, q \neq 0 \}$. <strong>Algebraic Property:</strong> Forms a <em>field</em>—fully closed under addition, subtraction, multiplication, and division (excluding division by zero). Every rational number has a decimal expansion that either terminates (e.g., $\frac{1}{4} = 0.25$) or repeats infinitely (e.g., $\frac{1}{3} = 0.333\dots$).</p>

            <h3>Real Numbers ($\mathbb{R}$): Filling the Geometric Gaps</h3>
            <p>Despite being dense (meaning between any two rational numbers, another rational always exists), $\mathbb{Q}$ contains massive structural "holes." For instance, applying the Pythagorean theorem to a right triangle with side lengths of 1 gives a hypotenuse of $\sqrt{2}$. Yet, <strong>Theorem:</strong> There is no rational number $p/q$ such that $(p/q)^2 = 2$.</p>

            <div class="diagram-card" style="margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
                <h5>The Geometric Gap: Constructing $\sqrt{2}$ on the Number Line</h5>
                <svg width="460" height="110" viewBox="0 0 460 110">
                    <line x1="30" y1="80" x2="430" y2="80" stroke="#64748b" stroke-width="2"/>
                    <circle cx="100" cy="80" r="4" fill="#64748b"/><text x="97" y="98" font-family="sans-serif" font-size="10" fill="#64748b">0</text>
                    <circle cx="240" cy="80" r="4" fill="#64748b"/><text x="235" y="98" font-family="sans-serif" font-size="10" fill="#64748b">1</text>
                    <circle cx="380" cy="80" r="4" fill="#64748b"/><text x="375" y="98" font-family="sans-serif" font-size="10" fill="#64748b">2</text>
                    <polygon points="100,80 240,80 240,40" fill="none" stroke="#d97706" stroke-width="1.5"/>
                    <text x="170" y="75" font-family="sans-serif" font-size="9" fill="#d97706">1</text>
                    <text x="245" y="62" font-family="sans-serif" font-size="9" fill="#d97706">1</text>
                    <path d="M 100 80 L 240 40" stroke="#ef4444" stroke-width="2"/>
                    <text x="155" y="50" font-family="sans-serif" font-size="10" fill="#ef4444" font-weight="bold">&radic;2 (&notin; &Qopf;)</text>
                    <path d="M 240 40 A 140 140 0 0 1 298 80" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3"/>
                </svg>
            </div>

            <div class="definition-box">
                <p><strong>The Completeness Property:</strong> To perform calculus, we require the real numbers ($\mathbb{R}$). $\mathbb{R}$ consists of all rationals combined with irrational numbers (non-repeating, non-terminating decimals like $\sqrt{2}$ or $\pi$). Crucially, $\mathbb{R}$ satisfies the <em>Least Upper Bound Property</em> (Completeness Axiom), ensuring there are no empty gaps on the number line. Without completeness, limits, suprema, and integrals could fall into nothingness.</p>
            </div>

            <h2>3. Sequences and the Limit Concept</h2>
            <p>With sets and real numbers established, we explore <strong>sequences</strong>—the fundamental bridge from discrete math to continuous calculus.</p>

            <h3>What Is a Sequence?</h3>
            <p><strong>In plain English:</strong> At its core, a sequence is simply an endless, ordered list of numbers. Think of it like a song playlist or a row of numbered parking spots stretching off forever toward infinity. Position is everything: there is a first term, a second term, a third term, and so on. Unlike a standard set (where order doesn't matter and items can't repeat), in a sequence you always know exactly which number comes next.</p>

            <p>Formally, a sequence is not merely a random string of numbers; it is a precisely defined mathematical function. Its domain is the set of natural numbers $\mathbb{N} = \{1, 2, 3, \dots\}$, and its codomain lies within the real numbers $\mathbb{R}$ (or any arbitrary set $S$). We write this mapping as:</p>
            <p>$$f: \mathbb{N} \rightarrow \mathbb{R}$$</p>
            <p>Instead of using standard function notation $f(n)$, mathematicians use subscript notation to denote the output at position index $n$:
            $$a_n = f(n)$$
            The entire infinite collection is expressed as $(a_n)_{n=1}^\infty = (a_1, a_2, a_3, \dots, a_n, \dots)$.</p>

            <div class="diagram-card" style="margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
                <h5>Sequence Mapping: Domain ($\mathbb{N}$) to Codomain ($\mathbb{R}$)</h5>
                <svg width="520" height="150" viewBox="0 0 520 150">
                    <!-- Domain Box -->
                    <rect x="20" y="20" width="140" height="110" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
                    <text x="90" y="38" font-family="sans-serif" font-size="11" fill="#475569" font-weight="bold" text-anchor="middle">Domain (ℕ)</text>
                    <circle cx="90" cy="55" r="12" fill="#fed7aa" stroke="#d97706"/><text x="90" y="59" font-family="sans-serif" font-size="10" fill="#92400e" font-weight="bold" text-anchor="middle">1</text>
                    <circle cx="90" cy="80" r="12" fill="#fed7aa" stroke="#d97706"/><text x="90" y="84" font-family="sans-serif" font-size="10" fill="#92400e" font-weight="bold" text-anchor="middle">2</text>
                    <circle cx="90" cy="105" r="12" fill="#fed7aa" stroke="#d97706"/><text x="90" y="109" font-family="sans-serif" font-size="10" fill="#92400e" font-weight="bold" text-anchor="middle">3</text>
                    <text x="90" y="125" font-family="sans-serif" font-size="10" fill="#64748b" text-anchor="middle">...</text>

                    <!-- Arrow Mapping -->
                    <path d="M 170 75 Q 235 45 300 75" fill="none" stroke="#d97706" stroke-width="2" marker-end="url(#arrow)"/>
                    <text x="235" y="50" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold" text-anchor="middle">f(n) = aₙ</text>

                    <!-- Codomain Box -->
                    <rect x="310" y="20" width="190" height="110" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
                    <text x="405" y="38" font-family="sans-serif" font-size="11" fill="#475569" font-weight="bold" text-anchor="middle">Codomain (ℝ)</text>
                    <circle cx="360" cy="55" r="12" fill="#fde68a" stroke="#d97706"/><text x="360" y="59" font-family="sans-serif" font-size="10" fill="#b45309" font-weight="bold" text-anchor="middle">a₁</text>
                    <circle cx="415" cy="80" r="12" fill="#fde68a" stroke="#d97706"/><text x="415" y="84" font-family="sans-serif" font-size="10" fill="#b45309" font-weight="bold" text-anchor="middle">a₂</text>
                    <circle cx="380" cy="110" r="12" fill="#fde68a" stroke="#d97706"/><text x="380" y="114" font-family="sans-serif" font-size="10" fill="#b45309" font-weight="bold" text-anchor="middle">a₃</text>
                </svg>
            </div>

            <div class="definition-box">
                <p><strong>Explicit vs. Recursive Formulations:</strong></p>
                <ul>
                    <li><strong>Explicit (Closed-Form) Formula:</strong> Provides a direct rule to compute the $n^{\text{th}}$ term instantly without needing prior terms. For example, $a_n = \frac{n}{n+1}$ allows us to jump straight to $a_{100} = \frac{100}{101}$.</li>
                    <li><strong>Recursive (Inductive) Definition:</strong> Defines terms relative to preceding terms. You must specify starting conditions (base cases) and a recurrence relation. A famous example is the Fibonacci sequence: $a_1 = 1, a_2 = 1$, and $a_n = a_{n-1} + a_{n-2}$ for $n \ge 3$.</li>
                </ul>
            </div>

            <h3>Core Behavioral Anatomy: Boundedness and Monotonicity</h3>
            <p>Before investigating whether a sequence converges to a limit, analysts examine two primary behavioral characteristics:</p>
            <ul>
                <li><strong>Monotonicity:</strong> A sequence is <em>monotonically increasing</em> if each term is greater than or equal to the last ($a_n \le a_{n+1}$ for all $n$), and <em>monotonically decreasing</em> if $a_n \ge a_{n+1}$. If it strictly alternates or wanders without a directional trend, it is non-monotonic.</li>
                <li><strong>Boundedness:</strong> A sequence is <em>bounded above</em> if there exists a real number $M$ such that $a_n \le M$ for all $n$, and <em>bounded below</em> if $a_n \ge m$ for all $n$. A sequence that is both bounded above and below is simply called bounded.</li>
            </ul>

            <div class="diagram-grid">
                <div class="diagram-card">
                    <h5>Boundedness (Upper & Lower Limits)</h5>
                    <svg width="240" height="120" viewBox="0 0 240 120">
                        <!-- Upper Bound M -->
                        <line x1="20" y1="25" x2="220" y2="25" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3"/>
                        <text x="25" y="20" font-family="sans-serif" font-size="9" fill="#ef4444">Upper Bound M</text>
                        <!-- Lower Bound m -->
                        <line x1="20" y1="95" x2="220" y2="95" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3"/>
                        <text x="25" y="110" font-family="sans-serif" font-size="9" fill="#3b82f6">Lower Bound m</text>
                        <!-- Sequence points trapped inside -->
                        <circle cx="40" cy="80" r="4" fill="#d97706"/>
                        <circle cx="80" cy="65" r="4" fill="#d97706"/>
                        <circle cx="120" cy="50" r="4" fill="#d97706"/>
                        <circle cx="160" cy="45" r="4" fill="#d97706"/>
                        <circle cx="200" cy="42" r="4" fill="#d97706"/>
                        <path d="M 40 80 L 80 65 L 120 50 L 160 45 L 200 42" fill="none" stroke="#d97706" stroke-width="1.5"/>
                    </svg>
                </div>
                <div class="diagram-card">
                    <h5>Monotonicity (Increasing Trend)</h5>
                    <svg width="240" height="120" viewBox="0 0 240 120">
                        <line x1="20" y1="100" x2="220" y2="100" stroke="#94a3b8" stroke-width="1"/>
                        <line x1="20" y1="100" x2="20" y2="15" stroke="#94a3b8" stroke-width="1"/>
                        <!-- Stepwise increasing points -->
                        <circle cx="50" cy="85" r="4" fill="#10b981"/>
                        <circle cx="90" cy="65" r="4" fill="#10b981"/>
                        <circle cx="130" cy="45" r="4" fill="#10b981"/>
                        <circle cx="170" cy="30" r="4" fill="#10b981"/>
                        <path d="M 50 85 L 90 65 L 130 45 L 170 30" fill="none" stroke="#10b981" stroke-width="1.5"/>
                        <text x="110" y="115" font-family="sans-serif" font-size="9" fill="#475569">aₙ ≤ aₙ₊₁ (Increasing)</text>
                    </svg>
                </div>
            </div>

            <h3>The Informal Idea of a Limit</h3>
            <p>When studying a sequence, our primary question is: <em>What value do the terms $a_n$ settle down toward as our index $n$ marches off toward infinity ($n \to \infty$)?</em></p>
            <p>Consider the sequence rule $a_n = \frac{1}{n}$. If we plug in successive index values for $n$:
            $$\text{For } n=1: a_1 = \frac{1}{1} = 1.0$$
            $$\text{For } n=2: a_2 = \frac{1}{2} = 0.5$$
            $$\text{For } n=3: a_3 = \frac{1}{3} \approx 0.333$$
            $$\text{For } n=10: a_{10} = \frac{1}{10} = 0.1$$
            As $n$ gets larger, the numbers shrink closer and closer to $0$. We say the limit is $0$, written as $\lim_{n\to\infty} \frac{1}{n} = 0$.</p>

            <h3>The $\epsilon-N$ Definition Decoded (The Challenge Game)</h3>
            <p>The formal definition of a limit is an interactive challenge between two players:</p>
            <ul>
                <li><strong>Your Role (The Skeptic / $\epsilon$):</strong> You pick an error tolerance budget ($\epsilon$). For example, you demand that all numbers in the sequence eventually land and stay within a narrow zone of $\pm 0.1$ around zero.</li>
                <li><strong>The System's Role ($N$):</strong> The system must find a specific cutoff position index ($N$). It wins the challenge if it can prove that *every single term* past that index ($n > N$) stays safely inside your error zone forever.</li>
            </ul>

            <div class="definition-box">
                <p><strong>Formal Definition of Convergence:</strong></p>
                <p>We say $\lim_{n\to\infty} a_n = L$ if:</p>
                <p>$$\forall \epsilon > 0, \quad \exists N \in \mathbb{N} \quad \text{such that} \quad \forall n > N, \quad |a_n - L| < \epsilon$$</p>
            </div>

            <!-- INTERACTIVE EPSILON CHALLENGE GAME -->
            <div class="game-box">
                <div class="game-header">
                    <span>🎮 INTERACTIVE CHALLENGE GAME: Test Your $\epsilon$</span>
                    <span>Sequence: $a_n = \frac{1}{n}$ (Target Limit $L = 0$)</span>
                </div>
                <div class="game-body">
                    <div class="game-explainer">
                        <strong>How This Game Works:</strong><br>
                        • <strong>The Sequence:</strong> We are testing $a_n = \frac{1}{n}$, which produces the shrinking list: $1, 0.5, 0.33, 0.25, 0.2, 0.16, \dots$ heading toward $0$.<br>
                        • <strong>Your Challenge:</strong> Click a tolerance button below to pick your error budget ($\epsilon$). You are demanding that the sequence be trapped within $\pm \epsilon$ of zero.<br>
                        • <strong>The System's Answer:</strong> The computer calculates the winning cutoff index ($N$) and renders the error zone on the diagram. Use the "Step Forward" button to manually verify that subsequent terms stay trapped inside the zone forever!
                    </div>

                    <p><strong>Choose Your Error Budget ($\epsilon$):</strong></p>
                    <div class="game-controls">
                        <button class="game-btn" onclick="startChallenge(0.2)">Test $\epsilon = 0.2$ (Wide)</button>
                        <button class="game-btn" onclick="startChallenge(0.1)">Test $\epsilon = 0.1$ (Medium)</button>
                        <button class="game-btn" onclick="startChallenge(0.05)">Test $\epsilon = 0.05$ (Tight)</button>
                    </div>

                    <div class="game-canvas-wrap">
                        <svg id="game-plot" width="560" height="160" viewBox="0 0 560 160">
                            <text x="180" y="85" font-family="sans-serif" font-size="13" fill="#64748b">Select an &epsilon; budget above to start the challenge.</text>
                        </svg>
                    </div>

                    <div class="game-controls" id="step-controls" style="display: none;">
                        <button class="game-btn" id="btn-challenge-next" onclick="advanceChallengeStep()">Step Forward ($n = N + 1$)</button>
                        <button class="game-btn" style="background-color: #64748b;" onclick="resetChallenge()">Reset Challenge</button>
                    </div>

                    <div id="game-output" style="font-family: monospace; background: #ffffff; padding: 1rem; border: 1px solid var(--border); border-radius: 4px; color: #0f172a;">
                        <em>Awaiting your $\epsilon$ selection above...</em>
                    </div>
                </div>
            </div>

            <p style="margin-top: 2rem;">To explore these mechanics further across multiple architectures, use the <strong>Dual-Track Simulator</strong> below:</p>

            <div class="dual-track-grid">
                <div class="track-card track-formal">
                    <h3>📐 Track 1: Abstract Formalism (Pure Theory)</h3>
                    <p>We say $\lim_{n\to\infty} a_n = L$ if:</p>
                    <p>$$\forall \epsilon > 0, \quad \exists N \in \mathbb{N} \quad \text{such that} \quad \forall n > N, \quad |a_n - L| < \epsilon$$</p>
                    <p>This universal-existential quantifier structure proves that points permanently enter and remain within an arbitrary neighborhood around $L$.</p>
                </div>
                <div class="track-card track-applied">
                    <h3>🎛 Track 2: Applied Mechanics (Numerical Analog)</h3>
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
                        <rect id="eps-band" x="40" y="132" width="540" height="28" fill="#fde68a" opacity="0.6"/>

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

                        <path d="M40 132 h-5" stroke="#d97706" fill="none"/>
                        <text x="12" y="136" font-family="sans-serif" font-size="10" fill="#d97706">&epsilon;=0.2</text>

                        <line id="n-threshold" x1="200" y1="20" x2="200" y2="160" stroke="#ef4444" stroke-width="2" stroke-dasharray="4" opacity="0"/>

                        <g id="points-group"></g>
                    </svg>
                </div>

                <div class="controls-pane">
                    <div class="nav-buttons">
                        <button id="btn-prev" onclick="step(-1)" disabled>Prev Step</button>
                        <button id="btn-next" onclick="step(1)">Next Step</button>
                        <button id="btn-reset" onclick="reset()" style="background-color: #64748b;">Reset</button>
                    </div>
                    <div class="step-summary" id="step-summary"></div>
                    <div class="toggle-group">
                        <label for="seq-toggle" style="font-size: 0.85rem; font-weight: bold; color: #475569; display: block; margin-bottom: 0.5rem;">COMPARE ARCHITECTURE:</label>
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
            if (challengeState.currentDisplayN > 14) {
                challengeState.currentDisplayN = 14;
            }
            updateChallengeUI();
        }

        function resetChallenge() {
            challengeState.active = false;
            document.getElementById('step-controls').style.display = 'none';
            document.getElementById('game-output').innerHTML = '<em>Challenge reset. Select an $\\epsilon$ budget above to start.</em>';
            document.getElementById('game-plot').innerHTML = '<text x="180" y="85" font-family="sans-serif" font-size="13" fill="#64748b">Select an &epsilon; budget above to start the challenge.</text>';
        }

        function updateChallengeUI() {
            const eps = challengeState.eps;
            const reqN = challengeState.reqN;
            const curN = challengeState.currentDisplayN;

            const output = document.getElementById('game-output');
            output.innerHTML = `<strong>Challenge Active ($\\epsilon = ${eps}$):</strong><br>` +
                `• System calculated required threshold: $N = \\lceil 1/${eps} \\rceil = ${reqN}$<br>` +
                `• Currently viewing up to position index $n = ${curN}$.<br>` +
                `• <strong>Status:</strong> All terms for $n > ${reqN}$ are safely trapped inside the $\\pm ${eps}$ error zone!`;

            if(window.renderMathInElement) {
                renderMathInElement(output, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ]
                });
            }
            renderGameSVG(eps, reqN, curN);
        }

        function renderGameSVG(eps, reqN, curN) {
            const svg = document.getElementById('game-plot');
            const maxN = 14;
            const width = 560;
            const height = 160;
            const originX = 40;
            const originY = 130;
            const maxXScale = 500;
            const maxYScale = 110;

            const topY = originY - (eps * maxYScale);
            const bottomY = originY + (eps * maxYScale);
            const bandHeight = bottomY - topY;
            const bandY = topY;

            let svgContent = `
                <rect x="${originX}" y="${bandY}" width="${maxXScale}" height="${bandHeight}" fill="#fef3c7" opacity="0.7"/>
                <line x1="${originX}" y1="${originY}" x2="${originX + maxXScale}" y2="${originY}" stroke="#64748b" stroke-width="2"/>
                <line x1="${originX}" y1="20" x2="${originX}" y2="${originY}" stroke="#64748b" stroke-width="2"/>
                <text x="5" y="${topY + 4}" font-family="sans-serif" font-size="9" fill="#d97706">+&epsilon;</text>
                <polyline points="32,${topY - 3} ${originX},${topY} 32,${topY + 3}" fill="none" stroke="#d97706" stroke-width="1.2"/>
                <line x1="22" y1="${topY}" x2="${originX}" y2="${topY}" stroke="#d97706" stroke-width="0.8" stroke-dasharray="2"/>
                <text x="5" y="${bottomY + 4}" font-family="sans-serif" font-size="9" fill="#d97706">-&epsilon;</text>
                <polyline points="32,${bottomY - 3} ${originX},${bottomY} 32,${bottomY + 3}" fill="none" stroke="#d97706" stroke-width="1.2"/>
                <line x1="22" y1="${bottomY}" x2="${originX}" y2="${bottomY}" stroke="#d97706" stroke-width="0.8" stroke-dasharray="2"/>
            `;

            for (let n = 1; n <= curN; n++) {
                const val = 1 / n;
                const cx = originX + (n * (maxXScale / maxN));
                const cy = originY - (val * maxYScale);

                svgContent += `<line x1="${cx}" y1="${originY}" x2="${cx}" y2="${originY + 4}" stroke="#64748b"/>`;
                svgContent += `<text x="${cx - 4}" y="${originY + 15}" font-family="sans-serif" font-size="9" fill="#475569">${n}</text>`;

                const inside = n > reqN;
                const fillColor = inside ? '#10b981' : '#d97706';
                const r = inside ? 6 : 4;

                svgContent += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fillColor}" />`;
            }

            const thresholdX = originX + (reqN * (maxXScale / maxN));
            svgContent += `
                <line x1="${thresholdX}" y1="15" x2="${thresholdX}" y2="${originY + 10}" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>
                <text x="${thresholdX + 5}" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ef4444">N = ${reqN} (Cutoff)</text>
            `;

            svg.innerHTML = svgContent;
        }

        const state = { step: 0, seq: 'reciprocal', eps: 0.2 };
        const data = {
            reciprocal: [1.0, 0.5, 0.333, 0.25, 0.2, 0.166, 0.142, 0.125],
            geometric: [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.0156, 0.0078]
        };

        const narratives = [
            {
                phase: "Initialization", n: 1, indexVal: 1,
                summary: "<strong>Goal:</strong> Initialize the sequence mapping $f: \\mathbb{N} \\rightarrow \\mathbb{R}$ and establish error bound constraints for our numerical iteration stream.",
                what: "<p><strong>Abstract Formalism:</strong> The sequence initializes at index $n=1$, yielding $a_1 = 1.0$ under the selected mapping rule.</p><p><strong>Applied Mechanics:</strong> Our iterative computation begins, defining a target limit $L=0$ and an acceptable residual tolerance $\\epsilon = 0.2$ (the yellow band).</p>",
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
                what: "<p><strong>Abstract Formalism:</strong> We evaluate $\vert{}a_n - 0\vert{} < 0.2$. For linear decay ($1/n$), this yields $n > 5$. For exponential decay ($2^{-n}$), it crosses at $n > 2$.</p><p><strong>Applied Mechanics:</strong> We set the threshold index $N$, rendering the red threshold boundary on our canvas to mark the computation latency required for target precision.</p>",
                why: "<p><strong>Formal Rationale:</strong> This operationalizes the existential quantifier $\\exists N$ in the formal definition.</p><p><strong>System Constraint:</strong> Establishes the exact execution latency required before the system certifies output stability.</p>"
            },
            {
                phase: "Convergence Verification", n: 8, indexVal: 8,
                summary: "<strong>Goal:</strong> Fulfill the universal quantifier condition to formally certify the limit.",
                what: "<p><strong>Abstract Formalism:</strong> For all subsequent indices $n > N$, terms remain strictly trapped within the $\\epsilon$ neighborhood.</p><p><strong>Applied Mechanics:</strong> The residual error remains flat and negligible across all further computation steps.</p>",
                why: "<p><strong>Formal Rationale:</strong> This satisfies $\\forall n > N$. Because this inequality holds for <em>any</i> arbitrary $\\epsilon > 0$, the limit $\\lim_{n\\to\\infty} a_n = L$ is verified.</p><p><strong>System Constraint:</strong> Guarantees long-term numerical stability against unexpected divergence.</p>"
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
                group.innerHTML += `<circle cx="${cx}" cy="${cy}" r="5" fill="#d97706" />`;
                if(idx > 0) {
                    const prevVal = data[state.seq][idx - 1];
                    const px = 80 + ((idx - 1) * 60);
                    const py = 160 - (prevVal * 140);
                    group.innerHTML += `<line x1="${px}" y1="${py}" x2="${cx}" y2="${cy}" stroke="#d97706" stroke-width="2" opacity="0.5"/>`;
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
</html>
"""
    with open('week1.html', 'w') as f:
        f.write(html_content)

def update_curriculum_index():
    if not os.path.exists('index.html'):
        print("index.html not found in current directory. Please run in root.")
        return

    with open('index.html', 'r') as f:
        content = f.read()

    target = '<a href="#" class="module-link">View Module</a>'
    replacement = '<a href="${item.week === 1 ? \'week1.html\' : \'#\'}" class="module-link">View Module</a>'

    updated_content = content.replace(target, replacement)

    with open('index.html', 'w') as f:
        f.write(updated_content)

def execute_git_sync():
    commit_message = (
        "Add pointer lines and arrows from epsilon labels to error band edges\n\n"
        "Updated renderGameSVG in week1.html to draw dynamic pointer lines and arrow "
        "chevrons connecting the +epsilon and -epsilon labels directly to the top and bottom "
        "boundaries of the tolerance band."
    )

    commands = [
        ['git', 'add', 'update.py', 'week1.html', 'index.html'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]

    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == "__main__":
    print("Writing Week 1 module with epsilon label pointer lines...")
    write_week1_module()
    print("Updating index.html routing...")
    update_curriculum_index()
    print("Committing and pushing to GitHub...")
    execute_git_sync()
    print("Deployment complete.")
