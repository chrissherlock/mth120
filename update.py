#!/usr/bin/env python3
"""
Update week2-lecture4.html with unboxed, deeply detailed Section 1, 2, and 4,
stage both the HTML file and this script, commit, and push to the remote repo.
"""

from pathlib import Path
import subprocess
import sys

TARGET_FILE = Path("week2-lecture4.html")
SCRIPT_FILE = Path(__file__).resolve()

COMMIT_SUBJECT = (
    "Unbox and expand Proposition 5 sequence properties in Lecture 4"
)
COMMIT_BODY = (
    "Convert Section 4 of week2-lecture4.html from boxed cards into\n"
    "flowing, detailed prose. Explain absolute value stabilization,\n"
    "the prefix-tail splitting technique for boundedness, and the\n"
    "buffer-zone insulation intuition behind the preservation of sign."
)

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 2, Lecture 4: Formal Convergence and Limit Laws | MTHS120</title>
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
        *, *::before, *::after { box-sizing: border-box; }
        html, body { max-width: 100%; overflow-x: hidden; }
        body { font-family: var(--font-ui); background: var(--bg); color: var(--text); line-height: 1.65; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; width: 100%; }
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
        .module-content { background: var(--card); padding: 2.25rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .toc-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.75rem; margin: 2rem 0 2.5rem 0; }
        .toc-box h4 { margin: 0 0 0.75rem 0; color: #92400e; font-size: 1.05rem; }
        .toc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.5rem 1.5rem; margin: 0; padding-left: 1.25rem; }
        .toc-grid li { margin-bottom: 0.35rem; font-size: 0.95rem; }
        .toc-grid a { color: #b45309; text-decoration: none; font-weight: 500; }
        .toc-grid a:hover { text-decoration: underline; color: var(--accent-hover); }

        h2 { border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; margin-top: 3rem; color: #0f172a; font-family: var(--font-ui); scroll-margin-top: 2rem; }
        h3 { color: #1e293b; margin-top: 1.75rem; font-family: var(--font-ui); scroll-margin-top: 2rem; }
        h4 { color: #334155; margin-top: 1.25rem; font-family: var(--font-ui); }

        .widget-instructions { background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.5rem; margin: 2rem 0 1rem 0; }
        .widget-instructions h4 { margin: 0 0 0.65rem 0; color: #0f172a; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; }
        .widget-instructions ol { margin: 0.5rem 0 0.85rem 1.25rem; padding: 0; }
        .widget-instructions li { margin-bottom: 0.45rem; font-size: 0.95rem; color: #334155; }

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

        .worked-example-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 5px solid #10b981; padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .worked-example-box h4 { margin-top: 0; color: #047857; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }
        .worked-example-box p, .worked-example-box li { color: #0f172a !important; }

        .lecture-card { background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; transition: transform 0.15s ease, box-shadow 0.15s ease; }
        .lecture-card:hover { transform: translateY(-2px); box-shadow: 0 6px 12px -2px rgba(0,0,0,0.08); border-color: var(--accent); }
        .lecture-card h3 { margin-top: 0; color: #0f172a; }
        .lecture-badge { display: inline-block; background: var(--accent); color: white; padding: 0.2rem 0.55rem; border-radius: 4px; font-weight: 700; font-size: 0.8rem; text-transform: uppercase; margin-bottom: 0.5rem; }

        @media (max-width: 768px) {
            .katex-display {
                overflow-x: auto !important;
                overflow-y: hidden !important;
                -webkit-overflow-scrolling: touch !important;
                max-width: 100% !important;
                padding: 0.25rem 0 !important;
            }
            body { background: #ffffff; padding: 1rem 0.75rem; }
            .container { max-width: 100%; margin: 0; }
            .module-content { background: transparent; padding: 0; border: none; border-radius: 0; box-shadow: none; margin-bottom: 1rem; }
            .header { padding-bottom: 0.75rem; margin-bottom: 1.25rem; }
            ol, ul { padding-left: 1.25rem !important; margin-left: 0 !important; }
            .header > .nav-btn-group,
            .footer-nav {
                display: flex !important;
                flex-direction: row !important;
                flex-wrap: nowrap !important;
                width: 100% !important;
                gap: 0.5rem !important;
            }
            .header > .nav-btn-group a,
            .header > .nav-btn-group span,
            .footer-nav a,
            .footer-nav span {
                flex: 1 1 0 !important;
                min-width: 0 !important;
                text-align: center !important;
                padding: 0.55rem 0.4rem !important;
                font-size: 0.82rem !important;
                white-space: nowrap !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
            }
            p, div, li, blockquote { word-break: break-word; overflow-wrap: break-word; }
            .math-overflow-fix, div[style*="text-align: center"] { max-width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; }
            .analysis-panes { grid-template-columns: 1fr !important; }
            .controls-pane { flex-direction: column; }
            .telemetry-grid { grid-template-columns: 1fr 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- TOP NAVIGATION HEADER -->
        <div class="header" style="border-bottom: 2px solid var(--border); padding-bottom: 1.5rem; margin-bottom: 2rem; display: flex; flex-direction: column; align-items: center; gap: 1.25rem;">
            <div class="nav-btn-group" style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap; width: 100%;">
                <a href="week1-lecture3.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&larr; Lecture 3</a>
                <a href="week2.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&uarr; Week 2 Hub</a>
                <a href="week2-lecture5.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">Lecture 5 &rarr;</a>
            </div>
            <div style="text-align: center; width: 100%; min-width: 0;">
                <h1 style="margin: 0; line-height: 1.3; font-size: 1.5rem;">Week 2, Lecture 4: Formal Convergence and Limit Laws</h1>
            </div>
        </div>

        <div class="module-content">
            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter2-hero.jpg" alt="Week 2: Limits of Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <!-- UNBOXED FLOWING ORIENTATION -->
            <div style="margin: 2.25rem 0 2.5rem 0;">
                <h3 style="margin-top: 0; color: #0f172a; font-size: 1.3rem;">
                    Welcome to Lecture 4: Taking the Fear Out of $\epsilon\text{-}N$
                </h3>
                <p style="margin: 0 0 1.15rem 0; color: #334155; line-height: 1.75; font-size: 1rem;">
                    For almost every mathematics student, this lecture marks the exact moment where the landscape changes. Up until now, calculus has largely been about calculation: finding derivatives, computing integrals, or asking what number an expression "approaches." Today, we ask a fundamentally different question: <em>how do we construct an unshakeable logical guarantee that an infinite sequence arrives at its destination and stays there?</em>
                </p>
                <p style="margin: 0 0 1.15rem 0; color: #334155; line-height: 1.75; font-size: 1rem;">
                    When you first see the definition with its string of Greek letters and quantifiers—$\forall \epsilon > 0 \; \exists N \in \mathbb{N} \dots$—it can feel forbidding, cold, or backwards. That reaction is entirely normal. The secret is that this definition is not an obstacle course; it is simply a game of target practice between two players. Once you see the picture, the algebra becomes a predictable, step-by-step craft.
                </p>
                <p style="margin: 0 0 0.75rem 0; color: #334155; line-height: 1.75; font-size: 1rem;">
                    Here is the path we will walk together in this lecture:
                </p>
                <ul style="margin: 0 0 1.5rem 1.25rem; padding: 0; color: #334155; line-height: 1.7; font-size: 0.98rem;">
                    <li style="margin-bottom: 0.6rem;">
                        <strong>The Target Game (Sections 1 &amp; 3):</strong> We translate the formal $\epsilon\text{-}N$ definition into an intuitive two-player challenge. A skeptic hands you an arbitrarily tight error tolerance ($\epsilon$), and you demonstrate that beyond a certain cutoff point in the sequence ($N$), every single term lands safely inside that target window forever.
                    </li>
                    <li style="margin-bottom: 0.6rem;">
                        <strong>The Rules of the Game (Section 2):</strong> We inspect why the order of words and quantifiers matters so deeply. We will see why $N$ depends directly on $\epsilon$, and discover the comical catastrophe that happens if you accidentally swap their order.
                    </li>
                    <li style="margin-bottom: 0.6rem;">
                        <strong>The Scratchpad Method (Section 3):</strong> We share the practical trade secret of analysis proofs: how mathematicians work backwards on scrap paper to discover the cutoff $N$, and then write the final deductive proof cleanly forward.
                    </li>
                    <li style="margin-bottom: 0.6rem;">
                        <strong>Structural Guarantees (Sections 4 &amp; 5):</strong> We prove that any sequence that converges cannot escape to infinity (it is bounded), and build the algebraic limit laws—including the elegant "$\epsilon/2$" strategy—so you don't have to rebuild proofs from scratch every time.
                    </li>
                    <li>
                        <strong>When Things Fall Apart (Section 6):</strong> We learn how to formally prove that a sequence does <em>not</em> converge by carefully negating our definition and exposing persistent oscillation.
                    </li>
                </ul>
                <div style="background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid var(--accent); border-radius: 6px; padding: 0.85rem 1.15rem; font-size: 0.93rem; color: #92400e; line-height: 1.6;">
                    🌱 <strong>Advice for Today:</strong> Take your time. Don't worry if you need to read an argument twice or step away for a breath. Proving limits is a skill that builds muscle memory, and by the end of this lecture, you'll have the exact tools needed to construct these proofs with confidence.
                </div>
            </div>

            <!-- TABLE OF CONTENTS -->
            <div class="toc-box">
                <h4>📌 Lecture 4 Topics</h4>
                <ul class="toc-grid">
                    <li><a href="#section-epsilon-n">1. Formal $\epsilon\text{-}N$ Convergence</a></li>
                    <li><a href="#section-quantifiers">2. Quantifier Order, Scope, and Dependencies</a></li>
                    <li><a href="#section-interactive-widget">3. Interactive Epsilon Challenge Simulator</a></li>
                    <li><a href="#section-prop5">4. Properties of Convergent Sequences (Proposition 5)</a></li>
                    <li><a href="#section-theorems">5. Algebraic Limit Laws and Proofs (Theorem 1)</a></li>
                    <li><a href="#section-divergence-test">6. Proving Non-Existence of Limits</a></li>
                </ul>
            </div>

            <!-- SECTION 1: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
            <h2 id="section-epsilon-n">1. Formal $\epsilon\text{-}N$ Convergence</h2>

            <h3 style="color: #0f172a; margin-top: 1.5rem;">Why Calculus Intuition Leaves Us Wanting</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                In introductory calculus, we are taught to describe a limit with kinetic language: <em>"as $n$ gets larger and larger, the sequence terms $a_n$ get closer and closer to $L$."</em> For computing derivatives of basic functions, this image works well. But in pure mathematics, this informal description hides subtle logical cracks:
            </p>
            <ul style="margin: 0.5rem 0 1.25rem 1.25rem; color: #334155; line-height: 1.7; font-size: 0.98rem;">
                <li style="margin-bottom: 0.5rem;">
                    <strong>Does "closer and closer" mean terms must never move away?</strong> What if a sequence oscillates, jumping back and forth across $L$, or takes three steps closer and one step backward?
                </li>
                <li style="margin-bottom: 0.5rem;">
                    <strong>How close is close enough?</strong> If $a_n = 1 + 1/n$, the terms get closer and closer to $0$, but $0$ is certainly not the limit! They also get closer to $1/2$, but that isn't the limit either.
                </li>
                <li>
                    <strong>Can we prove uniqueness?</strong> Without an exact measurement of distance, we cannot defend why a sequence cannot converge to two different numbers simultaneously.
                </li>
            </ul>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                To resolve this ambiguity, nineteenth-century mathematicians replaced the fuzzy idea of motion with an ironclad guarantee of <strong>metric distance</strong>. Instead of asking how a sequence travels, we establish an exact distance test that must hold permanently.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Understanding Absolute Value as Physical Distance</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Before reading the formal sentence, remember what absolute value actually means geometrically. On the real number line, the distance between any two numbers $x$ and $y$ is simply $|x - y|$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                When we write $|a_n - L| < \epsilon$, we are making a very simple statement: <strong>the straight-line distance between the sequence value $a_n$ and the target number $L$ is strictly smaller than $\epsilon$</strong>. Expanding that inequality without absolute value bars reveals its spatial meaning:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$|a_n - L| < \epsilon \iff -\epsilon < a_n - L < \epsilon \iff L - \epsilon < a_n < L + \epsilon$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Geometrically, $|a_n - L| < \epsilon$ simply means that $a_n$ lands safely inside an open corridor of width $2\epsilon$ centered exactly at $L$.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">The Formal Definition</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Here is the definition that serves as the foundation of all real analysis. Don't rush past it—read every symbol slowly:
            </p>
            <div style="padding: 1.25rem 1.5rem; margin: 1.5rem 0; background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; text-align: center;">
                <span style="font-size: 1.1rem; color: #0f172a; font-weight: 600; display: block; margin-bottom: 0.5rem;">
                    Definition: Convergence of a Sequence
                </span>
                <span style="font-size: 1.15rem; color: #0f172a;">
                    A sequence $(a_n)_{n=0}^\infty$ converges to a real limit $L \in \mathbb{R}$ (written $\lim_{n\to\infty} a_n = L$ or $a_n \to L$) if and only if:
                </span>
                <p style="margin: 1rem 0 0.5rem 0; font-size: 1.25rem;">
                    $$\forall \epsilon > 0, \quad \exists N \in \mathbb{N} \quad \text{such that} \quad n > N \implies |a_n - L| < \epsilon$$
                </p>
            </div>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Breaking Down Every Piece of the Formula</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Let's unpack each component of this sentence so that nothing feels like a secret code:
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.85rem;">
                    <strong>$\forall \epsilon > 0$ ("For every epsilon greater than zero"):</strong><br>
                    The Greek letter $\epsilon$ (epsilon) is traditionally used because it stands for <em>error</em>. Think of $\epsilon$ as the challenge tolerance. The universal quantifier ($\forall$) means this test must hold for <em>any</em> positive tolerance anyone could ever name—whether they challenge you with $\epsilon = 1$, $\epsilon = 0.001$, or $\epsilon = 10^{-100}$. You cannot negotiate a larger error margin; you must be prepared to satisfy any tolerance, no matter how microscopically tight.
                </li>
                <li style="margin-bottom: 0.85rem;">
                    <strong>$\exists N \in \mathbb{N}$ ("There exists a natural number cutoff $N$"):</strong><br>
                    This is your response to the challenge. In response to the given $\epsilon$, you identify a specific milestone index $N$. Crucially, you get to inspect $\epsilon$ <em>first</em> before you choose $N$. If the skeptic gives you a loose tolerance ($\epsilon = 0.5$), you might only need $N = 2$. If they challenge you with an extremely tight tolerance ($\epsilon = 0.0001$), you will have to walk much further down the sequence to find a larger $N$.
                </li>
                <li style="margin-bottom: 0.85rem;">
                    <strong>$\forall n > N$ ("For all indices $n$ strictly past the cutoff"):</strong><br>
                    This defines the <em>infinite tail</em> of the sequence. Real analysis teaches us a liberating truth: <strong>initial terms do not matter</strong>. The first ten, hundred, or million terms of a sequence can jump around chaotically, take excursions into negative numbers, or violate the tolerance. What matters is that past your chosen milestone $N$, every single subsequent term settles down.
                </li>
                <li>
                    <strong>$\implies |a_n - L| < \epsilon$ ("The terms remain permanently trapped"):</strong><br>
                    Once you pass milestone $N$, every term $a_n$ is within distance $\epsilon$ of $L$. It is not enough for one term to enter the window and bounce back out. Once $n > N$, <em>no term is ever allowed to leave the target corridor again</em>.
                </li>
            </ul>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">The Mental Model: The Two-Player Archery Game</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                If you ever feel lost in the algebraic symbols, picture this scenario as a friendly game of archery between two people:
            </p>
            <div style="display: flex; gap: 2rem; align-items: center; margin: 1.5rem 0; flex-wrap: wrap;">
                <div style="flex: 0 0 280px; margin: 0 auto;">
                    <svg viewBox="0 0 260 160" style="width: 100%; height: auto; display: block;">
                        <circle cx="130" cy="80" r="68" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2.5"/>
                        <circle cx="130" cy="80" r="48" fill="#fef3c7" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="130" y="47" font-family="sans-serif" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">&plusmn;&epsilon; Tolerance</text>
                        <circle cx="130" cy="80" r="22" fill="#fee2e2" stroke="#ef4444" stroke-width="2.5"/>
                        <circle cx="130" cy="80" r="7" fill="#ef4444"/>
                        <text x="130" y="84" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">L</text>
                        <line x1="35" y1="22" x2="123" y2="74" stroke="#0f172a" stroke-width="3.5" stroke-linecap="round"/>
                        <polygon points="123,74 111,68 116,61" fill="#0f172a"/>
                        <line x1="35" y1="22" x2="25" y2="16" stroke="#b45309" stroke-width="2.5"/>
                        <line x1="41" y1="28" x2="31" y2="22" stroke="#b45309" stroke-width="2.5"/>
                    </svg>
                </div>
                <div style="flex: 1; min-width: 280px;">
                    <ol style="margin: 0; padding-left: 1.25rem; color: #334155; line-height: 1.7; font-size: 0.98rem;">
                        <li style="margin-bottom: 0.5rem;">
                            <strong>Player 1 (The Skeptic) sets the target:</strong> They paint a target ring of radius $\epsilon$ around the bullseye $L$. They can make this ring as impossibly tiny as they want.
                        </li>
                        <li style="margin-bottom: 0.5rem;">
                            <strong>Player 2 (You, the Defender) finds the cutoff:</strong> You inspect their ring and announce a milestone index $N$.
                        </li>
                        <li>
                            <strong>The Test:</strong> Every arrow shot after turn $N$ (that is, $a_{N+1}, a_{N+2}, a_{N+3}, \dots$) must land securely inside the target ring.
                        </li>
                    </ol>
                    <p style="margin: 0.75rem 0 0 0; color: #334155; font-size: 0.95rem;">
                        If you have a reliable rule to produce a valid $N$ for <em>any</em> positive $\epsilon$ the skeptic throws at you, you win the game—and the sequence converges to $L$!
                    </p>
                </div>
            </div>

            <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-top: 1.5rem;">
                Use the interactive tool below to step through each clause of this definition in order. Notice how the internal telemetry updates, the visual diagram highlights the active region, and the mechanical and logical explanations synchronize with each step:
            </p>

            <!-- CLAUSE STEPPER -->
            <div class="stepper-walkthrough" id="definition-walkthrough">
                <div class="telemetry-grid">
                    <div class="telemetry-card"><span class="telemetry-label">Active Clause</span><span class="telemetry-badge" id="fw-tel-clause" style="color: #b45309;">1. The Challenge (∀ϵ > 0)</span></div>
                    <div class="telemetry-card"><span class="telemetry-label">Quantifier</span><span class="telemetry-badge" id="fw-tel-quant" style="color: #0369a1;">Universal (∀)</span></div>
                    <div class="telemetry-card"><span class="telemetry-label">Logical Role</span><span class="telemetry-badge" id="fw-tel-role" style="color: #be185d;">Given tolerance</span></div>
                    <div class="telemetry-card"><span class="telemetry-label">Scope</span><span class="telemetry-badge" id="fw-tel-scope" style="color: #047857;">Arbitrary positive real</span></div>
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
                        <rect id="fw-svg-epsband" x="50" y="55" width="640" height="70" fill="#fde68a" opacity="0.35" stroke="#f59e0b" stroke-dasharray="4" stroke-width="1.2"/>
                        <text id="fw-svg-epslbl1" x="65" y="48" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#d97706" font-weight="bold">+ϵ</text>
                        <text id="fw-svg-epslbl2" x="65" y="142" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#d97706" font-weight="bold">-ϵ</text>
                        <line id="fw-svg-nline" x1="330" y1="20" x2="330" y2="160" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5" opacity="0.2"/>
                        <text id="fw-svg-nlbl" x="338" y="34" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#ef4444" font-weight="bold" opacity="0.2">Cutoff N</text>
                        <g id="fw-svg-pts">
                            <circle id="fw-pt-1" cx="120" cy="25" r="5" fill="#94a3b8" opacity="0.5"/>
                            <circle id="fw-pt-2" cx="190" cy="42" r="5" fill="#94a3b8" opacity="0.5"/>
                            <circle id="fw-pt-3" cx="260" cy="55" r="5" fill="#94a3b8" opacity="0.5"/>
                            <circle id="fw-pt-4" cx="330" cy="55" r="5" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
                            <circle id="fw-pt-5" cx="400" cy="74" r="6" fill="#10b981"/>
                            <circle id="fw-pt-6" cx="470" cy="84" r="6" fill="#10b981"/>
                            <circle id="fw-pt-7" cx="540" cy="88" r="6" fill="#10b981"/>
                            <circle id="fw-pt-8" cx="610" cy="89" r="6" fill="#10b981"/>
                        </g>
                    </svg>
                </div>

                <div class="controls-pane">
                    <div class="nav-buttons">
                        <button id="btn-fw-prev" onclick="stepFormula(-1)" disabled>Prev Clause</button>
                        <button id="btn-fw-next" onclick="stepFormula(1)">Next Clause</button>
                    </div>
                    <div class="step-summary" id="fw-step-summary"></div>
                </div>

                <div class="analysis-panes">
                    <div class="pane">
                        <h4>Mathematical Mechanics</h4>
                        <div id="fw-pane-what"></div>
                    </div>
                    <div class="pane">
                        <h4>Logical Rationale</h4>
                        <div id="fw-pane-why"></div>
                    </div>
                </div>
            </div>

            <!-- SECTION 2: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
            <h2 id="section-quantifiers">2. Quantifier Order, Scope, and Dependencies</h2>

            <h3 style="color: #0f172a; margin-top: 1.5rem;">The Grammar of Analysis: Why Order Matters</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                In everyday English, word order can be remarkably forgiving. You can say <em>"Everyone loves someone"</em> or <em>"There is someone whom everyone loves,"</em> and listeners usually piece together what you mean. But in formal mathematical analysis, the order of quantifiers is not stylistic—it is the entire logical backbone of the argument. Changing the order of two quantifiers doesn't tweak the sentence; it completely alters the reality being described.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                When you see a long chain of symbols like:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.2rem;">
                $$\forall \epsilon > 0 \quad \exists N \in \mathbb{N} \quad \forall n > N, \quad |a_n - L| < \epsilon$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                the golden rule is to <strong>read strictly from left to right</strong>. Each quantifier establishes a "turn" in a conversation or a nested scope in a computer program. A variable introduced further to the right is allowed to look back and depend on variables to its left, but variables to the left can never look ahead to what hasn't been chosen yet.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Lexical Scope: The "Who Knows What" Rule</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                To see why $N$ depends on $\epsilon$, let's trace the visibility of information through the three variables:
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.85rem;">
                    <strong>The Outer Scope ($\forall \epsilon > 0$):</strong><br>
                    $\epsilon$ is chosen first. Because it sits at the very outside of the statement, it is chosen in complete isolation. Whoever picks $\epsilon$ knows nothing about $N$ and doesn't care what $N$ will be. They can pick $\epsilon = 1$, $\epsilon = 0.05$, or $\epsilon = 10^{-12}$.
                </li>
                <li style="margin-bottom: 0.85rem;">
                    <strong>The Inner Scope ($\exists N \in \mathbb{N}$):</strong><br>
                    Now it is our turn to pick $N$. Because $\exists N$ is written <em>after</em> $\forall \epsilon$, $N$ is chosen with full knowledge of $\epsilon$. In other words, $N$ is mathematically a function of $\epsilon$: we write $N = N(\epsilon)$. If the challenger changes $\epsilon$ from $0.1$ to $0.001$, we are entirely free to change our choice of $N$ to a much larger integer.
                </li>
                <li>
                    <strong>The Innermost Scope ($\forall n > N$):</strong><br>
                    Finally, the index $n$ is tested. Because $n$ sits inside the scope of both $\epsilon$ and $N$, it evaluates only for indices that are strictly greater than the cutoff $N$ we just selected.
                </li>
            </ul>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">When Can You Swap Quantifiers? (The Commutativity Rule)</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                A helpful rule of thumb to keep in mind is:
            </p>
            <ul style="margin: 0.5rem 0 1.25rem 1.25rem; color: #334155; line-height: 1.7; font-size: 0.98rem;">
                <li style="margin-bottom: 0.5rem;">
                    <strong>Quantifiers of the same type always commute:</strong> You can safely swap two universal quantifiers ($\forall x \, \forall y \iff \forall y \, \forall x$) or two existential quantifiers ($\exists x \, \exists y \iff \exists y \, \exists x$) without changing the mathematical meaning.
                </li>
                <li>
                    <strong>Alternating quantifiers NEVER commute:</strong> Swapping a $\forall$ with an $\exists$ radically changes what the statement demands. In analysis, $\forall \epsilon \, \exists N$ and $\exists N \, \forall \epsilon$ describe two completely different universes.
                </li>
            </ul>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">The Fatal Quantifier Swap: Why $\exists N \; \forall \epsilon$ Breaks Mathematics</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                To see the power of quantifier order firsthand, let's conduct a thought experiment. What would happen if a student accidentally reversed the first two quantifiers in an exam and wrote:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem; color: #b91c1c;">
                $$\exists N \in \mathbb{N} \quad \forall \epsilon > 0 \quad \forall n > N, \quad |a_n - L| < \epsilon \quad \text{?}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Read it from left to right using our "who knows what" rule:
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The statement now opens with $\exists N \in \mathbb{N}$. That means a single milestone number $N$ must be chosen <em>first</em>, before anyone has named $\epsilon$. Then, that same fixed $N$ must satisfy $|a_n - L| < \epsilon$ for <strong>every single positive $\epsilon$ simultaneously</strong>!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Think about what that requires. If $|a_n - L| < \epsilon$ for every $\epsilon > 0$, what non-negative real number is strictly smaller than every positive number? Only zero! The only distance smaller than every positive tolerance is exactly zero:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$|a_n - L| = 0 \implies a_n = L \quad \text{for all } n > N$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                By accidentally swapping those two words, the definition no longer describes sequences that approach a limit. It only describes sequences that literally <strong>freeze and become permanently constant</strong> after step $N$ (like $3, 7, 2, 5, 5, 5, 5, \dots$). A sequence like $a_n = 1/n$, which never equals $0$ but clearly converges to $0$, would fail this broken test!
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">A Practical Mental Checklist for Reading Proofs</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Whenever you sit down to write or read an $\epsilon\text{-}N$ proof, keep this internal dialogue running:
            </p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    <strong>When you see $\forall \epsilon > 0$:</strong> Remind yourself, <em>"I do not choose $\epsilon$. Someone hands it to me. I must treat $\epsilon$ as an arbitrary positive constant throughout my proof."</em>
                </li>
                <li style="margin-bottom: 0.6rem;">
                    <strong>When you see $\exists N \in \mathbb{N}$:</strong> Say to yourself, <em>"Now it's my turn. I must find a formula for $N$ that uses $\epsilon$. It is completely fine if $N$ gets huge when $\epsilon$ is tiny."</em>
                </li>
                <li>
                    <strong>When you see $\forall n > N$:</strong> Say to yourself, <em>"Now I verify my work. I let $n$ be an arbitrary index past $N$ and prove that the distance inequality $|a_n - L| < \epsilon$ holds algebraically."</em>
                </li>
            </ol>

            <!-- SECTION 3 -->
            <h2 id="section-interactive-widget">3. Interactive Epsilon Challenge Simulator</h2>
            <div class="widget-instructions">
                <h4>📖 Guide: Exploring the &epsilon;–N Definition with $a_n = \frac{1}{n}$ ($L = 0$)</h4>
                <p>This widget illustrates how shrinking tolerance pushes cutoff $N$ further down the tail:</p>
                <ol>
                    <li><strong>Choose Tolerance ($\epsilon$):</strong> Test $\epsilon = 0.2$ ($N=5$), $\epsilon = 0.1$ ($N=10$), or $\epsilon = 0.05$ ($N=20$).</li>
                    <li><strong>Observe Cutoff ($N$):</strong> Marked by the red dashed line ($N = \lceil 1/\epsilon \rceil$).</li>
                    <li><strong>Step Forward:</strong> Watch terms turn green as they enter the safe interior past $N$.</li>
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
                        <button class="game-btn" style="background-color: #64748b;" onclick="resetChallenge()">Reset</button>
                    </div>
                </div>
            </div>

            <div class="worked-example-box" style="margin-top: 1.5rem;">
                <h4>🎯 Worked Example: The $\epsilon\text{-}N$ Scratchpad Method</h4>
                <p>Prove formally that $\lim_{n\to\infty} \frac{2n+1}{n} = 2$:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Step 1: The Scratchpad Analysis.</strong> Start with $|a_n - L| < \epsilon$:
                        $$\left|\frac{2n+1}{n} - 2\right| = \left|2 + \frac{1}{n} - 2\right| = \frac{1}{n} < \epsilon$$
                    </li>
                    <li style="margin-bottom: 0.4rem;"><strong>Step 2: Solving for $n$.</strong> Rearranging gives $n > \frac{1}{\epsilon}$.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Step 3: Choosing $N$.</strong> Pick any integer $N \ge \frac{1}{\epsilon}$ (explicitly $N = \lceil 1/\epsilon \rceil$).</li>
                    <li><strong>Step 4: Formal Proof Write-Up.</strong> Let $\epsilon > 0$ be given. Set $N = \lceil 1/\epsilon \rceil$. For any $n > N$, we have $n > \frac{1}{\epsilon} \implies \frac{1}{n} < \epsilon$, which guarantees $\left|\frac{2n+1}{n} - 2\right| < \epsilon$. $\blacksquare$</li>
                </ol>
            </div>

            <!-- SECTION 4: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
            <h2 id="section-prop5">4. Properties of Convergent Sequences (Proposition 5)</h2>

            <h3 style="color: #0f172a; margin-top: 1.5rem;">Structural Guarantees: The Free Gifts of Convergence</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Writing an $\epsilon\text{-}N$ proof from scratch every time you encounter a new sequence would be exhausting. Mathematicians don't rebuild every argument from raw definitions; instead, they prove <strong>structural theorems</strong>. These are universal guarantees: once you know a sequence converges, you automatically inherit three powerful properties for free, without ever needing to guess a cutoff index again.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                In the course curriculum, these three guarantees are collected together in <strong>Proposition 5</strong>. Let's explore each one carefully, unpack the intuition behind why it must be true, and see how mathematicians construct their proofs.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Property 1: Absolute Value Stabilization ($a_n \to L \implies \vert{}a_n\vert{} \to \vert{}L\vert{}$)</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The first property says that if a sequence of numbers settles down to a limit $L$, then taking the absolute values of those numbers causes them to settle down to $|L|$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>Why does this make intuitive sense?</strong> Remember our geometric picture: absolute value measures distance from the origin $0$. If the points $a_n$ are crowding closer and closer to $L$, their distance from zero must naturally crowd closer and closer to $L$'s distance from zero.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Rigorous Proof:</strong> The proof relies on a handy tool known as the <em>Reverse Triangle Inequality</em>, which states that for any real numbers $x$ and $y$:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\big| |x| - |y| \big| \le |x - y|$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Notice what this inequality tells us: the distance between $|a_n|$ and $|L|$ is <em>always smaller than or equal to</em> the distance between $a_n$ and $L$. Therefore, whenever we choose an index $N$ such that $|a_n - L| < \epsilon$, we automatically get:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\big| |a_n| - |L| \big| \le |a_n - L| < \epsilon$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The exact same cutoff index $N$ that worked for $a_n$ works immediately for $|a_n|$!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem; background: #fffbeb; border-left: 4px solid var(--accent); padding: 0.85rem 1.15rem; border-radius: 4px;">
                ⚠️ <strong>A Classic Beginner Trap (The Converse Fails!):</strong> Does $|a_n| \to |L|$ imply that $a_n \to L$? <em>No!</em> Consider the sequence $a_n = (-1)^n = (-1, 1, -1, 1, \dots)$. Taking absolute values gives $|a_n| = 1$, which obviously converges to $1$. But the sequence $a_n$ itself never converges because it permanently oscillates. The only exception where the converse works is when the limit is zero: $|a_n| \to 0 \iff a_n \to 0$.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Property 2: Convergence Implies Boundedness (The Prefix vs. Tail Strategy)</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The second property is one of the most celebrated cornerstones of analysis:
            </p>
            <p style="text-align: center; margin: 1rem 0; font-size: 1.15rem; font-weight: 600; color: #0f172a;">
                Every convergent sequence is bounded.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                That is, there exists some positive real number $M > 0$ such that $|a_n| \le M$ for every single index $n \in \mathbb{N}$. In other words, a sequence that converges can never run off to $+\infty$ or $-\infty$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Conceptual Dilemma:</strong> An infinite sequence has infinitely many terms. How could we possibly build a single finite fence $[-M, M]$ that holds infinitely many numbers, especially when earlier terms might have jumped around wildly?
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Proof Strategy (Divide and Conquer):</strong> Mathematicians solve this using a beautiful two-step technique: we split the sequence into a <em>finite prefix</em> and an <em>infinite tail</em>.
            </p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.75rem;">
                    <strong>Trapping the Infinite Tail:</strong> Because $a_n \to L$, we can choose <em>any</em> tolerance we like. Let's make our lives easy and simply pick $\epsilon = 1$. By the definition of convergence, there exists some cutoff index $N$ such that:
                    $$n > N \implies |a_n - L| < 1$$
                    Applying the triangle inequality gives $|a_n| = |(a_n - L) + L| \le |a_n - L| + |L| < 1 + |L|$. Look at what we've accomplished: <em>all infinitely many terms past index $N$ are trapped below the number $|L| + 1$!</em>
                </li>
                <li style="margin-bottom: 0.75rem;">
                    <strong>Checking the Finite Prefix:</strong> What about the terms before the cutoff: $\{a_0, a_1, a_2, \dots, a_N\}$? There are only finitely many of them! Any finite list of real numbers has a guaranteed largest absolute value.
                </li>
                <li>
                    <strong>Building the Global Fence ($M$):</strong> We simply take the maximum over the finite prefix and our tail bound:
                    $$M = \max\Big(|a_0|, |a_1|, |a_2|, \dots, |a_N|, |L| + 1\Big)$$
                    Because every term in the prefix is $\le M$ by definition of a maximum, and every term in the tail is $< |L| + 1 \le M$, the number $M$ bounds the entire infinite sequence. $\blacksquare$
                </li>
            </ol>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>Does the converse hold?</strong> Again, ask yourself: if a sequence is bounded, does it have to converge? No! Boundedness is a <em>necessary</em> condition for convergence, but not a <em>sufficient</em> one. The sequence $a_n = (-1)^n$ is safely trapped inside $[-1, 1]$, yet it never converges.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Property 3: Preservation of Sign (The Buffer Zone)</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The third property provides peace of mind when working with signs:
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                If a sequence converges to a strictly positive limit ($L > 0$), then eventually all of its terms must become strictly positive and stay bounded away from zero. Specifically, there is an index $N_0$ such that:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$a_n > \frac{L}{2} > 0 \quad \text{for all } n > N_0$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                (Likewise, if $L < 0$, then eventually $a_n < \frac{L}{2} < 0$).
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>Why do we care so much about this?</strong> Think ahead to the Algebraic Limit Laws in the next section. When we want to prove that $\lim \frac{a_n}{b_n} = \frac{K}{L}$, we need to divide by $b_n$. But you cannot divide by zero! Even worse, if the numbers $b_n$ got closer and closer to zero, $1/b_n$ would explode to infinity. The preservation of sign property guarantees that if $L \neq 0$, the terms $b_n$ eventually build an impenetrable moat of width $L/2$ between themselves and zero.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Geometric Proof:</strong> If $L > 0$, the distance from $L$ to zero is exactly $L$. Since we can choose any positive $\epsilon$ in the definition of convergence, let's deliberately choose a tolerance that doesn't reach zero: set $\epsilon = \frac{L}{2}$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                By the definition of convergence, there is an index $N_0$ such that for all $n > N_0$, we have $|a_n - L| < \frac{L}{2}$. Unpacking the absolute value bars:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$-\frac{L}{2} < a_n - L < \frac{L}{2} \implies L - \frac{L}{2} < a_n < L + \frac{L}{2} \implies \frac{L}{2} < a_n < \frac{3L}{2}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Look at the left-hand inequality: $a_n > \frac{L}{2}$. Because $L > 0$, $\frac{L}{2}$ is strictly positive. Every term in the tail is trapped above $\frac{L}{2}$ forever, completely insulated from zero!
            </p>

            <!-- SECTION 5 -->
            <h2 id="section-theorems">5. Algebraic Limit Laws and Proofs (Theorem 1)</h2>
            <p>Evaluating limits directly with $\epsilon\text{-}N$ proofs for every function is tedious. The Algebraic Limit Laws allow us to compute limits compositionally.</p>

            <div class="infobox" style="background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.5rem; margin: 1.25rem 0 1.75rem 0;">
                <h4 style="margin: 0 0 0.85rem 0; color: #0f172a; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem;">📐 Algebraic Limit Laws (Theorem 1)</h4>
                <div style="font-size: 0.93rem; color: #475569; line-height: 1.6; margin: 0 0 1.25rem 0; padding-bottom: 0.85rem; border-bottom: 1px solid #e2e8f0;">
                    Suppose $\lim_{n\to\infty} a_n = K$ and $\lim_{n\to\infty} b_n = L$, and let $c \in \mathbb{R}$ be a constant. Then:
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.95rem;">
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>1. Constant Rule:</strong> <span>$\lim_{n\to\infty} c = c$</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>2. Scalar Multiple:</strong> <span>$\lim_{n\to\infty} (c \cdot a_n) = c \cdot K$</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>3. Sum / Difference:</strong> <span>$\lim_{n\to\infty} (a_n \pm b_n) = K \pm L$</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>4. Product Rule:</strong> <span>$\lim_{n\to\infty} (a_n \cdot b_n) = K \cdot L$</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>5. Quotient Rule:</strong> <span>$\lim_{n\to\infty} \left(\frac{a_n}{b_n}\right) = \frac{K}{L}$, provided $L \neq 0$ and $b_n \neq 0$</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem;">
                        <strong>6. Power Rule:</strong> <span>$\lim_{n\to\infty} (a_n)^p = K^p$</span>
                    </div>
                </div>
            </div>

            <div class="worked-example-box">
                <h4>🎯 Rigorous Proof of the Sum Law</h4>
                <p>We prove that $\lim (a_n + b_n) = K + L$. Let $\epsilon > 0$.</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li>Since $a_n \to K$, $\exists N_1$ such that $n > N_1 \implies |a_n - K| < \frac{\epsilon}{2}$.</li>
                    <li>Since $b_n \to L$, $\exists N_2$ such that $n > N_2 \implies |b_n - L| < \frac{\epsilon}{2}$.</li>
                    <li>Let $N = \max(N_1, N_2)$. For any $n > N$, applying the Triangle Inequality yields:
                        $$|(a_n + b_n) - (K + L)| = |(a_n - K) + (b_n - L)| \le |a_n - K| + |b_n - L| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
                    </li>
                </ol>
            </div>

            <!-- SECTION 6 -->
            <h2 id="section-divergence-test">6. Proving Non-Existence of Limits</h2>
            <p>To show that a sequence $(a_n)$ does not converge to any limit, we must prove that every possible candidate $L \in \mathbb{R}$ fails the $\epsilon\text{-}N$ definition:</p>
            <div style="text-align: center; margin: 0.75rem 0;">
                $$\forall L \in \mathbb{R}, \quad \exists \epsilon > 0 \quad \text{such that} \quad \forall N \in \mathbb{N}, \quad \exists n > N \quad \text{with} \quad |a_n - L| \ge \epsilon$$
            </div>

            <div class="worked-example-box">
                <h4>🎯 Proof: $a_n = (-1)^n$ Has No Limit</h4>
                <p>Consider the alternating sequence $(1, -1, 1, -1, \dots)$. Fix any $L \in \mathbb{R}$ and set $\epsilon = 1$.</p>
                <ul style="margin: 0.35rem 0 0 1.25rem;">
                    <li><strong>Case 1 ($\vert{}L - 1\vert{} < 1$):</strong> In this case $L > 0$. For any odd index $n$, $a_n = -1$, giving $|a_n - L| = |-1 - L| = 1 + L > 1 = \epsilon$.</li>
                    <li><strong>Case 2 ($\vert{}L - 1\vert{} \ge 1$):</strong> For any even index $n$, $a_n = 1$, giving $|a_n - L| = |1 - L| \ge 1 = \epsilon$.</li>
                </ul>
                <p style="margin-top: 0.5rem; margin-bottom: 0;">In both cases, terms oscillate outside the $\epsilon = 1$ band for arbitrarily large $n$. Thus, no limit $L$ exists.</p>
            </div>

            <!-- FOOTER NAVIGATION -->
            <div class="footer-nav" style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: center; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
                <a href="week1-lecture3.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&larr; Lecture 3</a>
                <a href="week2.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&uarr; Week 2 Hub</a>
                <a href="week2-lecture5.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">Lecture 5 &rarr;</a>
            </div>
        </div>
    </div>

    <!-- INTERACTIVE SCRIPTS -->
    <script>
        // Definition Stepper Data Arc
        const formulaSteps = [
            {
                clause: "1. The Challenge (∀ϵ > 0)",
                quant: "Universal (∀)",
                role: "Given tolerance (Skeptic)",
                scope: "Arbitrary positive real ϵ",
                summary: "The skeptic challenges the sequence by selecting an arbitrarily small tolerance band around L. The sequence must meet any challenge, no matter how microscopically tight.",
                what: "The tolerance variable &epsilon; &gt; 0 enters the outermost scope. A symmetric horizontal corridor of half-width &epsilon; is drawn around target limit L.",
                why: "Requiring universal satisfaction for all &epsilon; &gt; 0 prevents declaring convergence prematurely. A valid limit must withstand any precision test.",
                epsOpacity: 0.35,
                nLineOpacity: 0.15,
                activePoints: [0, 1, 2, 3]
            },
            {
                clause: "2. The Response (∃N ∈ ℕ)",
                quant: "Existential (∃)",
                role: "Defender's cutoff index",
                scope: "Natural number N = N(ϵ)",
                summary: "In response to the chosen &epsilon;, we identify a discrete index N &isin; &naturals; beyond which the sequence permanently settles inside the corridor.",
                what: "We determine cutoff N &isin; &naturals; as a function of &epsilon;. The boundary x = N partitions indices into a transient prefix and a permanent tail.",
                why: "The existential quantifier gives us the move after inspecting &epsilon;. We are permitted to disregard any finite prefix of unruly initial terms.",
                epsOpacity: 0.35,
                nLineOpacity: 0.9,
                activePoints: [3]
            },
            {
                clause: "3. The Tail (∀n > N)",
                quant: "Universal (∀)",
                role: "Tail iteration",
                scope: "All indices n strictly past N",
                summary: "We inspect every single term strictly beyond cutoff N. Convergence demands that no subsequent term ever escapes the corridor again.",
                what: "The universal quantifier sweeps across all indices n &gt; N to infinity. The condition must hold universally across the entire infinite tail.",
                why: "Limits describe asymptotic inevitability. Permitting even a single escape past N would violate stability and introduce permanent error.",
                epsOpacity: 0.35,
                nLineOpacity: 0.9,
                activePoints: [4, 5, 6, 7]
            },
            {
                clause: "4. Proximity (|aₙ - L| < ϵ)",
                quant: "Predicate Test",
                role: "Metric containment",
                scope: "Distance condition in ℝ",
                summary: "Every term in the tail satisfies |a_n - L| < &epsilon;. The terms remain trapped within the target corridor forever.",
                what: "The distance |a_n - L| evaluates strictly less than &epsilon; for every n &gt; N. The green points lie securely inside the yellow target band.",
                why: "The absolute difference metric provides an unbiased distance test, ensuring convergence whether terms approach monotonically or oscillate.",
                epsOpacity: 0.45,
                nLineOpacity: 0.9,
                activePoints: [4, 5, 6, 7]
            }
        ];

        let currentFormulaStep = 0;

        function renderFormulaState(step) {
            currentFormulaStep = step;
            const data = formulaSteps[step];

            const clauseBadge = document.getElementById('fw-tel-clause');
            const quantBadge = document.getElementById('fw-tel-quant');
            const roleBadge = document.getElementById('fw-tel-role');
            const scopeBadge = document.getElementById('fw-tel-scope');
            const summaryBox = document.getElementById('fw-step-summary');
            const paneWhat = document.getElementById('fw-pane-what');
            const paneWhy = document.getElementById('fw-pane-why');

            if (clauseBadge) clauseBadge.textContent = data.clause;
            if (quantBadge) quantBadge.textContent = data.quant;
            if (roleBadge) roleBadge.textContent = data.role;
            if (scopeBadge) scopeBadge.textContent = data.scope;

            if (summaryBox) summaryBox.innerHTML = `<p style="margin:0;">${data.summary}</p>`;
            if (paneWhat) paneWhat.innerHTML = `<p>${data.what}</p>`;
            if (paneWhy) paneWhy.innerHTML = `<p>${data.why}</p>`;

            for (let i = 0; i < 4; i++) {
                const chunk = document.getElementById('chunk-' + i);
                if (!chunk) continue;
                chunk.classList.remove('active', 'completed');
                if (i === step) chunk.classList.add('active');
                else if (i < step) chunk.classList.add('completed');
            }

            const prevBtn = document.getElementById('btn-fw-prev');
            const nextBtn = document.getElementById('btn-fw-next');
            if (prevBtn) prevBtn.disabled = (step === 0);
            if (nextBtn) nextBtn.disabled = (step === formulaSteps.length - 1);

            const epsBand = document.getElementById('fw-svg-epsband');
            const nLine = document.getElementById('fw-svg-nline');
            const nLbl = document.getElementById('fw-svg-nlbl');
            if (epsBand) epsBand.setAttribute('opacity', data.epsOpacity);
            if (nLine) nLine.setAttribute('opacity', data.nLineOpacity);
            if (nLbl) nLbl.setAttribute('opacity', data.nLineOpacity);
        }

        function setFormulaStep(step) {
            if (step >= 0 && step < formulaSteps.length) {
                renderFormulaState(step);
            }
        }

        function stepFormula(delta) {
            const next = currentFormulaStep + delta;
            if (next >= 0 && next < formulaSteps.length) {
                renderFormulaState(next);
            }
        }

        // Interactive Epsilon Simulator Logic
        function renderChallengePlot(eps, nCutoff) {
            const svg = document.getElementById('game-plot');
            if (!svg) return;

            const width = 740;
            const height = 260;
            const padX = 50;
            const padY = 30;
            const plotW = width - padX - 40;
            const plotH = height - padY - 40;

            const maxN = 24;
            const xPos = (n) => padX + ((n - 1) / (maxN - 1)) * plotW;
            const yPos = (val) => padY + plotH - (val / 1.1) * plotH;

            const epsY = yPos(eps);
            const zeroY = yPos(0);
            const cutoffX = xPos(nCutoff);

            let svgMarkup = `
                <!-- Grid line and zero axis -->
                <line x1="${padX}" y1="${zeroY}" x2="${padX + plotW}" y2="${zeroY}" stroke="#94a3b8" stroke-width="1.5" />
                <text x="${padX + plotW + 8}" y="${zeroY + 4}" font-family="sans-serif" font-size="11" fill="#64748b" font-weight="bold">L = 0</text>

                <!-- Tolerance corridor -->
                <rect x="${padX}" y="${epsY}" width="${plotW}" height="${zeroY - epsY}" fill="#fef3c7" stroke="#f59e0b" stroke-dasharray="4" stroke-width="1.2" opacity="0.65" />
                <text x="${padX + 8}" y="${epsY - 6}" font-family="sans-serif" font-size="11" fill="#b45309" font-weight="bold">+ϵ = ${eps}</text>

                <!-- Cutoff threshold line -->
                <line x1="${cutoffX}" y1="${padY}" x2="${cutoffX}" y2="${padY + plotH}" stroke="#ef4444" stroke-width="2" stroke-dasharray="5" />
                <text x="${cutoffX + 6}" y="${padY + 16}" font-family="sans-serif" font-size="12" fill="#ef4444" font-weight="bold">N = ${nCutoff}</text>
            `;

            for (let n = 1; n <= maxN; n++) {
                const val = 1 / n;
                const cx = xPos(n);
                const cy = yPos(val);
                const isTail = n > nCutoff;
                const fillColor = isTail ? "#10b981" : "#94a3b8";
                const strokeColor = isTail ? "#047857" : "#64748b";
                const radius = isTail ? 5.5 : 4;

                svgMarkup += `
                    <circle cx="${cx}" cy="${cy}" r="${radius}" fill="${fillColor}" stroke="${strokeColor}" stroke-width="1.2">
                        <title>a_${n} = ${val.toFixed(3)}</title>
                    </circle>
                `;

                if (n === 1 || n === nCutoff || n === nCutoff + 1 || n === maxN) {
                    svgMarkup += `<text x="${cx}" y="${zeroY + 18}" font-family="sans-serif" font-size="10" fill="#64748b" text-anchor="middle">n=${n}</text>`;
                }
            }

            svg.innerHTML = svgMarkup;
        }

        function startChallenge(eps) {
            const nCutoff = Math.ceil(1 / eps);
            const nextVal = (1 / (nCutoff + 1)).toFixed(3);

            const epsBadge = document.getElementById('cg-tel-eps');
            const reqnBadge = document.getElementById('cg-tel-reqn');
            const valBadge = document.getElementById('cg-tel-val');
            const statusBadge = document.getElementById('cg-tel-status');
            const ctrlPanel = document.getElementById('step-controls');

            if (epsBadge) epsBadge.textContent = 'ϵ = ' + eps;
            if (reqnBadge) reqnBadge.textContent = 'N = ' + nCutoff;
            if (valBadge) valBadge.textContent = `a_${nCutoff + 1} = ${nextVal} < ${eps}`;
            if (statusBadge) {
                statusBadge.textContent = 'Target Secure';
                statusBadge.style.color = '#059669';
            }
            if (ctrlPanel) ctrlPanel.style.display = 'flex';

            renderChallengePlot(eps, nCutoff);
        }

        function resetChallenge() {
            const epsBadge = document.getElementById('cg-tel-eps');
            const reqnBadge = document.getElementById('cg-tel-reqn');
            const valBadge = document.getElementById('cg-tel-val');
            const statusBadge = document.getElementById('cg-tel-status');
            const ctrlPanel = document.getElementById('step-controls');
            const svg = document.getElementById('game-plot');

            if (epsBadge) epsBadge.textContent = 'Select below';
            if (reqnBadge) reqnBadge.textContent = '—';
            if (valBadge) valBadge.textContent = '—';
            if (statusBadge) {
                statusBadge.textContent = 'Standby';
                statusBadge.style.color = '#64748b';
            }
            if (ctrlPanel) ctrlPanel.style.display = 'none';

            if (svg) {
                svg.innerHTML = '<text x="260" y="130" font-family="ui-sans-serif, system-ui, sans-serif" font-size="14" fill="#64748b">Select an &epsilon; budget above to illustrate the sample.</text>';
            }
        }

        // Initialize state once KaTeX and DOM are ready
        window.addEventListener('DOMContentLoaded', () => {
            renderFormulaState(0);
        });
    </script>
</body>
</html>
"""


def write_lecture4_page(file_path: Path) -> None:
    file_path.write_text(HTML_CONTENT, encoding="utf-8")
    print(f"Successfully updated '{file_path}'.")


def check_staged_changes() -> bool:
    """Return True if changes exist in the git staging index."""
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return result.returncode != 0


def sync_git_repository(target_path: Path, script_path: Path) -> None:
    commit_message = f"{COMMIT_SUBJECT}\n\n{COMMIT_BODY}"

    print(f"Staging {target_path.name} and {script_path.name}...")
    subprocess.run(["git", "add", str(target_path), str(script_path)], check=True)

    if not check_staged_changes():
        print("Staged files are already identical to HEAD. Nothing to commit.")
        return

    print("Creating git commit...")
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    print("Pushing to remote repository...")
    subprocess.run(["git", "push"], check=True)
    print("Done! Changes pushed successfully.")


if __name__ == "__main__":
    try:
        write_lecture4_page(TARGET_FILE)
        sync_git_repository(TARGET_FILE, SCRIPT_FILE)
    except subprocess.CalledProcessError as git_err:
        print(f"Git execution error: {git_err}", file=sys.stderr)
        sys.exit(1)
    except OSError as err:
        print(f"File system error: {err}", file=sys.stderr)
        sys.exit(1)
