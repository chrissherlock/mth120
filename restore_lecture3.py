#!/usr/bin/env python3
r"""
restore_lecture3.py

Writes the completely repaired, uncorrupted, and fully responsive
week1-lecture3.html file to disk and commits the change to git.
"""

import sys
import subprocess
from pathlib import Path

CLEAN_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 1, Lecture 3: Sequences and Discrete Calculus</title>
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
        body { font-family: var(--font-ui); background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; width: 100%; }
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1.5rem; margin-bottom: 2rem; display: flex; flex-direction: column; align-items: center; gap: 1.25rem; }
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .intro-lead { font-size: 1.1rem; color: #1e293b; line-height: 1.7; margin-bottom: 1.5rem; background: #f1f5f9; padding: 1.5rem; border-radius: 6px; border: 1px solid var(--border); border-left: 4px solid var(--accent); }
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

        .definition-box { background: #f8fafc; border: 1px solid var(--border); border-left: 4px solid var(--accent); padding: 1rem 1.5rem; margin: 1rem 0; border-radius: 0 6px 6px 0; }
        .aside-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #b45309; padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .aside-box h4 { margin-top: 0; color: #b45309; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }

        .worked-example-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 5px solid #10b981; padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .worked-example-box h4 { margin-top: 0; color: #047857; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }
        .worked-example-box p, .worked-example-box li { color: #0f172a !important; }

        .biography-box { background: #f5f3ff; border: 1px solid #ddd6fe; border-left: 5px solid #6366f1; padding: 1.25rem 1.5rem; margin: 2rem 0; border-radius: 0 6px 6px 0; }
        .biography-box h4 { margin-top: 0; color: #3730a3; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; }
        .biography-box p, .biography-box li { color: #0f172a !important; }

        .nobr { white-space: nowrap !important; word-break: keep-all !important; display: inline; }
        .katex { white-space: nowrap !important; }

        /* Responsive stepping table components */
        .stepping-table-container { margin: 1.5rem 0 2rem 0; }
        .desktop-stepping-table { width: 100%; border-collapse: collapse; font-size: 0.95rem; text-align: center; }
        .mobile-stepping-cards { display: none; flex-direction: column; gap: 0.85rem; }
        .stepping-card { background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1rem 1.15rem; box-shadow: 0 1px 3px rgba(0,0,0,0.04); }
        .stepping-card.plateau { background: #f0fdf4; border-color: #bbf7d0; }
        .stepping-card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem; padding-bottom: 0.4rem; border-bottom: 1px solid #e2e8f0; }
        .stepping-card-math { display: grid; grid-template-columns: repeat(3, 1fr) auto; align-items: center; gap: 0.5rem; font-size: 0.98rem; font-weight: 600; text-align: center; margin-bottom: 0.5rem; }

        @media (max-width: 768px) {
            body { background: #ffffff !important; padding: 1rem 0.75rem !important; margin: 0 !important; max-width: 100vw !important; overflow-x: hidden !important; }
            .container { max-width: 100% !important; margin: 0 !important; padding: 0 !important; }
            .module-content { background: transparent !important; padding: 0 !important; border: none !important; border-radius: 0 !important; box-shadow: none !important; margin-bottom: 1rem !important; }
            .header { padding-bottom: 0.75rem !important; margin-bottom: 1.25rem !important; }
            ol, ul { padding-left: 1.25rem !important; margin-left: 0 !important; }
            .header > div:last-child, .nav-btn-group, .footer-nav { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; width: 100% !important; gap: 0.5rem !important; }
            .header > div:last-child a, .nav-btn-group a, .footer-nav a { flex: 1 1 0 !important; min-width: 0 !important; text-align: center !important; padding: 0.55rem 0.4rem !important; font-size: 0.84rem !important; white-space: nowrap !important; overflow: hidden !important; text-overflow: ellipsis !important; }
            p, li, .definition-box { overflow-wrap: anywhere; word-break: normal; }
            .katex-display { overflow-x: auto !important; overflow-y: hidden !important; -webkit-overflow-scrolling: touch !important; max-width: 100% !important; padding: 0.25rem 0 !important; margin: 0.5rem 0 !important; }
            .stepper-nav-grid, .stepper-analytical-grid { grid-template-columns: 1fr !important; }

            /* Full-width responsive biography cards on mobile */
            .biography-box { padding: 1.25rem 1rem !important; }
            .biography-box > div { flex-direction: column !important; align-items: stretch !important; gap: 1.25rem !important; }
            .biography-box > div > div:first-child { flex: 0 0 100% !important; width: 100% !important; max-width: 100% !important; margin: 0 0 0.5rem 0 !important; }
            .biography-box > div > div:first-child img { width: 100% !important; max-height: 380px !important; object-fit: cover !important; border-radius: 6px !important; display: block !important; }
            .biography-box > div > div:last-child { width: 100% !important; min-width: 0 !important; }
        }

        @media (max-width: 640px) {
            .desktop-stepping-table { display: none !important; }
            .mobile-stepping-cards { display: flex !important; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- TOP NAVIGATION HEADER -->
        <div class="header">
            <div class="nav-btn-group" style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap; width: 100%;">
                <a href="week1-lecture2.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&larr; Lecture 2</a>
                <a href="week1.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&uarr; Week 1 Hub</a>
                <a href="week2-lecture4.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">Lecture 4 &rarr;</a>
            </div>
            <div style="text-align: center; width: 100%; min-width: 0;">
                <h1 style="margin: 0; line-height: 1.3; font-size: 1.5rem;">Week 1, Lecture 3: Sequences and Discrete Calculus</h1>
            </div>
        </div>

        <div class="module-content">
            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter1-hero.jpg" alt="Week 1: Sets, Numbers, and Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <div class="intro-lead">
                Welcome to Lecture 3. Having built the grammatical machinery of sets and functions (Lecture 1) and solidified the continuous real line $\mathbb{R}$ with completeness (Lecture 2), we now introduce motion into our universe. Here we study <strong>sequences</strong>—the fundamental vehicles of convergence, approximation, and discrete calculus.
            </div>

            <!-- UNBOXED FLOWING ORIENTATION -->
            <div style="margin: 2.25rem 0 2.5rem 0;">
                <h3 style="margin-top: 0; color: #0f172a; font-size: 1.25rem;">Finding Your Footing: Welcome to Discrete Dynamics</h3>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                    If you have studied calculus in secondary school, functions have almost always meant continuous curves: drawing a parabola $y = x^2$ with an unbroken pencil line, sliding along a smooth curve, or taking the tangent line at any arbitrary decimal value like $x = 1.414$. In that continuous universe, numbers flow into one another without gaps, and change happens smoothly and instantaneously.
                </p>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                    In this lecture, we step back from smooth slides and instead examine <strong>stepping stones</strong>. Rather than gliding across all real numbers, we take discrete integer steps: step 0, step 1, step 2, step 3... This is the world of <strong>sequences</strong>. Instead of asking what happens at $x = 1.414$, we ask what happens at the 100th locker, or how an infinite list of numbers behaves as our step counter marches toward infinity.
                </p>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                    At first glance, undergraduate analysis notation—subscripts <span class="nobr">$a_n$,</span> index ranges <span class="nobr">$(a_n)_{n=0}^\infty$,</span> and difference operators <span class="nobr">$a_n'$</span>—can look intimidatingly formal. Rest assured: every symbol in this lecture is simply a clean, precise way to label an item in an infinite list. You already intuitively understand these patterns from everyday life (such as monthly bank balances or compounding interest).
                </p>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 0;">
                    Take your time as we walk down the infinite locker corridor. See how arithmetic strides and geometric zoom factors govern discrete growth, notice how taking differences gives us a "discrete derivative," and enjoy seeing how discrete arithmetic lays the unshakable foundation for the limits and convergence theorems awaiting us in Week 2!
                </p>
            </div>

            <!-- TABLE OF CONTENTS -->
            <div class="toc-box">
                <h4>📌 Lecture 3 Topics</h4>
                <ul class="toc-grid">
                    <li><a href="#sequences-intro">1. What is a Sequence? (From Numbered Lockers to Formal Mappings)</a></li>
                    <li><a href="#catalogue-sequences">2. A Gallery of Fundamental Sequences</a></li>
                    <li><a href="#arithmetic-geometric">3. Arithmetic and Geometric Progressions (Deep Dive)</a></li>
                    <li><a href="#sequence-properties">4. Classifying Behavior: Monotonicity and Bounds</a></li>
                    <li><a href="#algebra-of-sequences">5. The Algebra of Sequences (Scaling and Sums)</a></li>
                    <li><a href="#derived-sequences">6. Discrete Calculus: The Derived Sequence (<span class="nobr">$a_n'$</span>)</a></li>
                    <li><a href="#discrete-integration">7. Reversing the Difference: Partial Sums and Series</a></li>
                    <li><a href="#grand-arc">8. The Grand Arc: From Discrete Rungs to the Continuum</a></li>
                </ul>
            </div>

            <!-- SECTION 1 -->
            <h2 id="sequences-intro">1. What is a Sequence? (From Numbered Lockers to Formal Mappings)</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Sequences &amp; Index Notation</h4>
                <div class="infobox-intro">
                    <strong>Lists through functional eyes:</strong> Instead of writing inputs inside parentheses like <span class="nobr">$f(n)$,</span> sequences use subscript notation <span class="nobr">$a_n$</span> to represent the $n$-th value in the list.
                </div>
                <div class="notation-grid">
                    <div class="notation-item">
                        <span class="notation-sym"><span class="nobr">$a_n$</span></span>
                        <span class="notation-desc">The $n$-th term of the sequence (the value stored at position $n$)</span>
                    </div>
                    <div class="notation-item">
                        <span class="notation-sym"><span class="nobr">$(a_n)_{n=0}^\infty$</span></span>
                        <span class="notation-desc">The complete infinite ordered sequence $(a_0, a_1, a_2, a_3, \dots)$</span>
                    </div>
                    <div class="notation-item">
                        <span class="notation-sym"><span class="nobr">$(a_n)_{n=1}^\infty$</span></span>
                        <span class="notation-desc">Sequence starting at index $1$ when $n=0$ is undefined (e.g. <span class="nobr">$a_n = 1/n$</span>)</span>
                    </div>
                    <div class="notation-item">
                        <span class="notation-sym"><span class="nobr">$a: \mathbb{N} \to \mathbb{R}$</span></span>
                        <span class="notation-desc">Formal definition: a function assigning each natural index $n$ to a real number $a_n$</span>
                    </div>
                </div>
            </div>

            <h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.25rem;">The Intuitive Picture: An Infinite Hallway of Numbered Lockers</h3>
            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">
                Before writing down any abstract symbols, think of a sequence as an infinite hallway lined with numbered school lockers:
            </p>
            <ul style="font-size: 0.98rem; line-height: 1.7; color: #334155; padding-left: 1.25rem; margin-bottom: 1.25rem;">
                <li>The <strong>locker door</strong> is labeled with a natural counting number: Locker $0$, Locker $1$, Locker $2$, Locker $3$, and so on. We call this whole number the <strong>index</strong> <span class="nobr">($n \in \mathbb{N}$).</span></li>
                <li>When you open door $n$, there is a slip of paper inside with an actual real number written on it. We call that stored number the <strong>$n$-th term</strong> <span class="nobr">($a_n \in \mathbb{R}$).</span></li>
            </ul>

            <!-- ILLUSTRATION: INFINITE LOCKERS PERSPECTIVE -->
            <div style="margin: 1.75rem 0 2rem 0; text-align: center;">
                <div style="border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); background: #ffffff;">
                    <img src="images/infinite-lockers.png" alt="Mathematical Sequence as an Infinite Locker Corridor" style="width: 100%; height: auto; display: block;">
                </div>
                <p style="font-size: 0.88rem; color: #64748b; margin-top: 0.6rem; line-height: 1.5;">
                    <em>Figure 3.1:</em> The sequence mapping <span class="nobr">$a: \mathbb{N} \to \mathbb{R}$</span> visualized as an infinite corridor. Each discrete locker door represents the natural index <span class="nobr">($n \in \mathbb{N}$),</span> while the contents inside reveal the corresponding real term <span class="nobr">($a_n \in \mathbb{R}$).</span>
                </p>
            </div>

            <div style="text-align: center; margin: 1.25rem 0; font-size: 1.1rem; background: #f8fafc; padding: 1rem; border-radius: 6px; border: 1px solid var(--border);">
                $$(a_n)_{n=0}^\infty = \Big(\underbrace{a_0}_{\text{Locker } 0}, \; \underbrace{a_1}_{\text{Locker } 1}, \; \underbrace{a_2}_{\text{Locker } 2}, \; \underbrace{a_3}_{\text{Locker } 3}, \; \dots, \; \underbrace{a_n}_{\text{Locker } n}, \; \dots\Big)$$
            </div>

            <h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.75rem;">The Aha! Moment: Why a Sequence is Actually a Function</h3>
            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">
                Why do pure mathematicians insist on calling this simple list of lockers a <strong>function</strong>?
            </p>
            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">
                Think back to our definition of a function in Lecture 1: a rule that takes every input from a starting set (the domain) and assigns it to exactly one output in a target set (the codomain). That is <em>exactly</em> what our locker hallway does!
            </p>
            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">
                You give the system a locker number <span class="nobr">($n \in \mathbb{N}$),</span> and it returns the single real number inside that locker <span class="nobr">($a_n \in \mathbb{R}$).</span> Therefore:
            </p>

            <div class="definition-box">
                <strong>Formal Definition of a Real Sequence:</strong><br>
                A <strong>sequence of real numbers</strong> is a function <span class="nobr">$a: \mathbb{N} \to \mathbb{R}$</span> whose domain is the set of natural numbers $\mathbb{N}$ <span class="nobr">(or $\mathbb{N} \setminus \{0\} = \{1, 2, 3, \dots\}$)</span> and whose codomain is the set of real numbers $\mathbb{R}$.<br><br>
                Instead of writing function parentheses like <span class="nobr">$a(n)$,</span> we write the input as a lower subscript:
                <div style="text-align: center; margin: 0.5rem 0; font-size: 1.05rem;">
                    $$\text{Function notation: } a(n) \quad\Longleftrightarrow\quad \text{Index notation: } a_n$$
                </div>
            </div>

            <div class="aside-box">
                <h4>💡 Does Indexing Start at $0$ or $1$?</h4>
                <p style="margin-top: 0; margin-bottom: 0.5rem;">
                    In mathematics, whether the natural numbers $\mathbb{N}$ include $0$ depends on context and convenience:
                </p>
                <ul style="margin: 0; padding-left: 1.25rem;">
                    <li>When modeling sets, counting dominoes, or building polynomial terms ($c_0 + c_1 x + \dots$), starting at $n=0$ is standard.</li>
                    <li>When dealing with fractions like $a_n = \frac{1}{n}$, dividing by zero is undefined, so we start at $n=1$.</li>
                </ul>
                <p style="margin: 0.5rem 0 0 0;">
                    Neither choice is "wrong." Always check the bottom bound on the index notation <span class="nobr">$(a_n)_{n=0}^\infty$</span> versus <span class="nobr">$(a_n)_{n=1}^\infty$.</span>
                </p>
            </div>

            <!-- SECTION 2 -->
            <h2 id="catalogue-sequences">2. A Gallery of Fundamental Sequences</h2>
            <div style="margin-bottom: 1.5rem;">
                <h3 style="margin-top: 0; color: #0f172a; font-size: 1.15rem;">How Do We Specify What Goes Inside Each Locker?</h3>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                    When constructing a sequence, there are two primary ways to describe the contents of every locker along the infinite corridor:
                </p>
                <ul style="font-size: 0.98rem; line-height: 1.75; color: #334155; padding-left: 1.25rem; margin-bottom: 1rem;">
                    <li style="margin-bottom: 0.5rem;">
                        <strong>An Explicit Formula (Direct Calculation):</strong> A direct algebraic equation that lets you calculate the value inside locker $n$ immediately. For example, if <span class="nobr">$a_n = n^2$,</span> finding the contents of the $100\text{th}$ locker requires no intermediate work: <span class="nobr">$a_{100} = 100^2 = 10{,}000$.</span>
                    </li>
                    <li>
                        <strong>A Descriptive or Structural Rule (Pattern-Based):</strong> A well-defined rule that uniquely determines what number belongs at step $n$, even if there is no high-school algebraic formula to jump there directly. For instance, "let <span class="nobr">$p_n$</span> be the $n\text{th}$ prime number" is completely rigorous because every natural index $n$ pairs with a single, unambiguous prime.
                    </li>
                </ul>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 0;">
                    Below are four foundational prototypes encountered throughout real analysis:
                </p>
            </div>

            <!-- UNBOXED FLOWING EXAMPLES LIST -->
            <div style="margin: 1.5rem 0 2rem 0;">
                <h4 style="color: #0f172a; font-size: 1.1rem; margin-bottom: 0.75rem;">Prototypes of Fundamental Sequences</h4>
                <ol style="margin: 0 0 0 1.25rem; font-size: 1.02rem; line-height: 1.8; color: #334155;">
                    <li style="margin-bottom: 0.85rem;">
                        <strong>The Sequence of Perfect Squares:</strong> <span class="nobr">$a_n = n^2$</span> <span class="nobr">(for $n \ge 0$).</span><br>
                        <em>Explicit terms:</em> <span class="nobr">$a_0 = 0,$</span> <span class="nobr">$a_1 = 1,$</span> <span class="nobr">$a_2 = 4,$</span> <span class="nobr">$a_3 = 9,$</span> <span class="nobr">$a_4 = 16,$</span> $\dots$<br>
                        <em>Behavior:</em> Grows without bound as <span class="nobr">$n \to \infty$.</span>
                    </li>
                    <li style="margin-bottom: 0.85rem;">
                        <strong>The Harmonic Sequence:</strong> <span class="nobr">$a_n = \frac{1}{n}$</span> <span class="nobr">(for $n \ge 1$).</span><br>
                        <em>Explicit terms:</em> <span class="nobr">$a_1 = 1,$</span> <span class="nobr">$a_2 = \frac{1}{2},$</span> <span class="nobr">$a_3 = \frac{1}{3},$</span> <span class="nobr">$a_4 = \frac{1}{4},$</span> $\dots$<br>
                        <em>Behavior:</em> Values grow progressively smaller and closer to $0$, illustrating convergence.
                    </li>
                    <li style="margin-bottom: 0.85rem;">
                        <strong>The Alternating Sequence:</strong> <span class="nobr">$a_n = (-1)^n$</span> <span class="nobr">(for $n \ge 0$).</span><br>
                        <em>Explicit terms:</em> <span class="nobr">$a_0 = 1,$</span> <span class="nobr">$a_1 = -1,$</span> <span class="nobr">$a_2 = 1,$</span> <span class="nobr">$a_3 = -1,$</span> <span class="nobr">$a_4 = 1,$</span> $\dots$<br>
                        <em>Behavior:</em> Bounces infinitely back and forth between $1$ and $-1$. It never settles down to a single number!
                    </li>
                    <li>
                        <strong>The Prime Sequence:</strong> <span class="nobr">$p_n$</span> where $p_n$ is the $n$-th prime number <span class="nobr">($n \ge 1$).</span><br>
                        <em>Explicit terms:</em> <span class="nobr">$p_1 = 2,$</span> <span class="nobr">$p_2 = 3,$</span> <span class="nobr">$p_3 = 5,$</span> <span class="nobr">$p_4 = 7,$</span> <span class="nobr">$p_5 = 11,$</span> $\dots$<br>
                        <em>Behavior:</em> This sequence has no simple algebraic formula, yet it is completely well-defined because every natural index $n$ determines a unique prime.
                    </li>
                </ol>
            </div>

            <!-- SECTION 3 -->
            <h2 id="arithmetic-geometric">3. Arithmetic and Geometric Progressions (Deep Dive)</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Progression Parameters</h4>
                <div class="infobox-intro">
                    <strong>Notice the parameter names:</strong> In these formulas, $a, b,$ and $q$ are fixed numbers that define the rule, while $n$ is simply the locker door counter <span class="nobr">($0, 1, 2, 3, \dots$).</span>
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$c_n = an + b$</span></span><span class="notation-desc">Arithmetic formula: start at baseline $b$, take $n$ strides of size $a$</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$c_{n+1} - c_n = a$</span></span><span class="notation-desc">Common difference: the fixed stride size added at every single step</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$c_n = a \cdot q^n$</span></span><span class="notation-desc">Geometric formula: start at scale factor $a$, multiply $n$ times by ratio $q$</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$\frac{c_{n+1}}{c_n} = q$</span></span><span class="notation-desc">Common ratio: the constant scaling factor between adjacent terms</span></div>
                </div>
            </div>

            <h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.25rem;">1. Unpacking the Two Great Motions: Strides vs. Zoom</h3>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                In reality, arithmetic and geometric progressions describe two distinct, tangible physical motions along our infinite locker corridor. Let us examine each in detail to see why their algebraic structures take the shapes they do.
            </p>

            <h4 style="color: #1e293b; margin-top: 1.5rem;">The Arithmetic Progression: Walking with Constant Strides</h4>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                Imagine standing at position <span class="nobr">$b$</span> right in front of Locker 0. To travel down the corridor, you decide that every single time you move from one locker to the next, you will take a rigid, identical stride forward of length <span class="nobr">$a$.</span>
            </p>
            <ul style="font-size: 0.98rem; line-height: 1.75; color: #334155; padding-left: 1.25rem; margin-bottom: 1.25rem;">
                <li>At <strong>Locker 0</strong>, you haven't taken any steps yet, so your position is just your starting baseline: <span class="nobr">$c_0 = b$.</span></li>
                <li>At <strong>Locker 1</strong>, you have taken 1 stride forward: <span class="nobr">$c_1 = b + a$.</span></li>
                <li>At <strong>Locker 2</strong>, you have taken 2 strides forward: <span class="nobr">$c_2 = b + a + a = b + 2a$.</span></li>
                <li>At <strong>Locker $n$</strong>, you have taken $n$ identical strides forward from your baseline: <span class="nobr">$c_n = an + b$.</span></li>
            </ul>

            <div class="definition-box">
                <strong>Formal Definition: Arithmetic Progression</strong><br>
                A sequence $(c_n)_{n=0}^\infty$ is an <strong>arithmetic progression</strong> if each term is obtained by adding a constant difference $a$ to the preceding term:
                <div style="text-align: center; margin: 0.5rem 0; font-size: 1.05rem;">
                    $$c_{n+1} - c_n = a \quad \text{for all } n \ge 0$$
                </div>
                Its explicit closed-form formula for any index $n$ is:
                <div style="text-align: center; margin: 0.5rem 0; font-size: 1.05rem; font-weight: 600; color: #0284c7;">
                    $$c_n = an + b$$
                </div>
                where $b = c_0$ is the initial baseline value at Locker 0, and $a$ is the common difference.
            </div>

            <h4 style="color: #1e293b; margin-top: 1.75rem;">The Geometric Progression: The Exponential Multiplier</h4>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                Now imagine a completely different mode of travel along the locker corridor. Instead of taking additive strides, suppose Locker 0 starts with an initial seed quantity <span class="nobr">$a$,</span> and every single time you cross from one locker to the next, your current holdings are <em>multiplied</em> by a zoom factor <span class="nobr">$q$.</span>
            </p>
            <div class="definition-box" style="border-left-color: #10b981;">
                <strong>Formal Definition: Geometric Progression</strong><br>
                A sequence $(c_n)_{n=0}^\infty$ is a <strong>geometric progression</strong> if each term is obtained by multiplying the preceding term by a constant ratio $q$:
                <div style="text-align: center; margin: 0.5rem 0; font-size: 1.05rem;">
                    $$\frac{c_{n+1}}{c_n} = q \quad \text{for all } n \ge 0 \quad (c_n \ne 0)$$
                </div>
                Its explicit closed-form formula for any index $n$ is:
                <div style="text-align: center; margin: 0.5rem 0; font-size: 1.05rem; font-weight: 600; color: #047857;">
                    $$c_n = a \cdot q^n$$
                </div>
                where $a = c_0$ is the starting scale factor at Locker 0, and $q$ is the common ratio.
            </div>

            <!-- INTERACTIVE PEDAGOGICAL AID: PROGRESSION STEPPING SIMULATOR -->
            <div id="progression-stepper-widget" style="margin: 2.25rem 0; background: #ffffff; border: 1px solid var(--border); border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); overflow: hidden;">
                <div style="background: #f8fafc; border-bottom: 1px solid var(--border); padding: 1rem 1.25rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
                    <div>
                        <span style="font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--accent); display: block;">Interactive Stepper</span>
                        <strong style="color: #0f172a; font-size: 1.05rem;">The Stepping Dynamics Simulator: Strides vs. Zoom</strong>
                    </div>
                    <div style="display: flex; gap: 0.4rem; background: #e2e8f0; padding: 0.25rem; border-radius: 6px;">
                        <button id="toggle-arithmetic" onclick="setMode('arithmetic')" style="padding: 0.35rem 0.75rem; border: none; border-radius: 4px; font-size: 0.82rem; font-weight: 600; cursor: pointer; background: #ffffff; color: #0284c7; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">Arithmetic (+3)</button>
                        <button id="toggle-geom-growth" onclick="setMode('geom_growth')" style="padding: 0.35rem 0.75rem; border: none; border-radius: 4px; font-size: 0.82rem; font-weight: 600; cursor: pointer; background: transparent; color: #475569;">Geometric (&times;2)</button>
                        <button id="toggle-geom-decay" onclick="setMode('geom_decay')" style="padding: 0.35rem 0.75rem; border: none; border-radius: 4px; font-size: 0.82rem; font-weight: 600; cursor: pointer; background: transparent; color: #475569;">Geometric (&times;0.5)</button>
                    </div>
                </div>

                <div style="background: #0f172a; color: #f8fafc; padding: 0.75rem 1.25rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 0.75rem; font-size: 0.82rem; font-family: ui-monospace, monospace; border-bottom: 1px solid #1e293b;">
                    <div><span style="color: #94a3b8; display: block; font-size: 0.72rem; text-transform: uppercase;">Locker Index (n)</span><strong id="telem-n" style="font-size: 1.05rem; color: #38bdf8;">0</strong></div>
                    <div><span style="color: #94a3b8; display: block; font-size: 0.72rem; text-transform: uppercase;">Stored Value (cₙ)</span><strong id="telem-val" style="font-size: 1.05rem; color: #34d399;">2</strong></div>
                    <div><span style="color: #94a3b8; display: block; font-size: 0.72rem; text-transform: uppercase;">Transition Step</span><strong id="telem-op" style="font-size: 1.05rem; color: #fbbf24;">Baseline Initializer</strong></div>
                    <div><span style="color: #94a3b8; display: block; font-size: 0.72rem; text-transform: uppercase;">Formula Expansion</span><strong id="telem-formula" style="font-size: 0.95rem; color: #cbd5e1;">b = 2</strong></div>
                </div>

                <div style="padding: 1.5rem 1.25rem; background: #ffffff; text-align: center; border-bottom: 1px solid var(--border);">
                    <svg id="stepper-canvas" viewBox="0 0 760 140" style="width: 100%; max-width: 740px; height: auto; display: inline-block; overflow: visible;"></svg>
                </div>

                <div class="stepper-nav-grid" style="padding: 1.25rem; background: #f8fafc; border-bottom: 1px solid var(--border); display: grid; grid-template-columns: 220px 1fr; gap: 1.25rem; align-items: center;">
                    <div style="display: flex; gap: 0.5rem; align-items: center;">
                        <button id="btn-prev" onclick="stepPrev()" style="flex: 1; padding: 0.6rem 0.8rem; background: #ffffff; border: 1px solid var(--border); border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer; color: #475569;">&larr; Prev</button>
                        <button id="btn-next" onclick="stepNext()" style="flex: 1; padding: 0.6rem 0.8rem; background: var(--accent); border: none; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer; color: #ffffff;">Next &rarr;</button>
                        <button id="btn-reset" onclick="resetStepper()" style="padding: 0.6rem 0.75rem; background: #e2e8f0; border: none; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer; color: #475569;" title="Reset to Locker 0">&#8635;</button>
                    </div>
                    <div style="background: #ffffff; border: 1px solid var(--border); border-left: 4px solid var(--accent); border-radius: 6px; padding: 0.6rem 0.9rem;">
                        <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #64748b; display: block;">Step Walkthrough Preview</span>
                        <p id="inline-preview-text" style="margin: 0; font-size: 0.88rem; line-height: 1.45; color: #1e293b;">Standing in front of Locker 0. Inspecting the baseline contents before any steps are taken.</p>
                    </div>
                </div>

                <div class="stepper-analytical-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; padding: 1.25rem; background: #ffffff;">
                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 1rem;">
                        <h5 style="margin: 0 0 0.4rem 0; font-size: 0.88rem; text-transform: uppercase; letter-spacing: 0.04em; color: #166534; display: flex; align-items: center; gap: 0.4rem;">
                            <span>⚙</span> What Is Happening (Mechanics)
                        </h5>
                        <div id="pane-what" style="font-size: 0.9rem; line-height: 1.55; color: #14532d;">The index pointer is stationed at Locker 0. The value is initialized to the base constant b = 2.</div>
                    </div>
                    <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 6px; padding: 1rem;">
                        <h5 style="margin: 0 0 0.4rem 0; font-size: 0.88rem; text-transform: uppercase; letter-spacing: 0.04em; color: #1e40af; display: flex; align-items: center; gap: 0.4rem;">
                            <span>💡</span> Why The System Does This (Rationale)
                        </h5>
                        <div id="pane-why" style="font-size: 0.9rem; line-height: 1.55; color: #1e3a8a;">Locker 0 represents the state before iteration begins. Because no step difference has been added yet, the step counter is n = 0, leaving only the pure baseline b.</div>
                    </div>
                </div>
            </div>

            <!-- SECTION 4 -->
            <h2 id="sequence-properties">4. Classifying Behavior: Monotonicity and Bounds</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Monotonicity &amp; Boundedness</h4>
                <div class="infobox-intro">
                    <strong>Describing directional motion:</strong> Sequences are classified by whether their terms march in one direction (monotonicity) or remain trapped between physical barriers (boundedness).
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$a_{n+1} \ge a_n$</span></span><span class="notation-desc">Increasing sequence: each term is greater than or equal to the predecessor</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$a_{n+1} > a_n$</span></span><span class="notation-desc">Strictly increasing: every new step climbs strictly higher</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$a_{n+1} \le a_n$</span></span><span class="notation-desc">Decreasing sequence: each term is less than or equal to the predecessor</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$a_{n+1} < a_n$</span></span><span class="notation-desc">Strictly decreasing: every new step falls strictly lower</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$m \le a_n \le M$</span></span><span class="notation-desc">Bounded sequence: trapped between lower bound $m$ and upper bound $M$</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$|a_n| \le K$</span></span><span class="notation-desc">Equivalent compact boundedness: trapped in symmetric interval $[-K, K]$</span></div>
                </div>
            </div>

            <h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.75rem;">1. The Geometry of Monotonicity: Preserving Direction</h3>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                A sequence is monotonic if it picks a single direction along the real line and commits to it forever. Look at the four discrete profiles below:
            </p>

            <!-- 4-PANEL RESPONSIVE VISUALIZATION FOR MONOTONICITY -->
            <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin: 1.75rem 0; text-align: center;">
                <p style="font-size: 1.05rem; font-weight: 700; color: #1e293b; margin-top: 0; margin-bottom: 0.35rem;">
                    VISUALIZING MONOTONICITY: Directional Profiles in the Discrete Plane
                </p>
                <p style="font-size: 0.92rem; color: #64748b; margin-top: 0; margin-bottom: 1.5rem; max-width: 780px; display: inline-block; line-height: 1.6;">
                    Monotonicity means committing to a direction along the real line and never reversing course. Notice that weak monotonicity permits flat horizontal rests, but strictly forbids a step backward.
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; text-align: left;">
                    <!-- PANEL 1: STRICTLY INCREASING -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #0284c7; display: block; margin-bottom: 0.2rem;">
                            1. Strictly Increasing: aₙ₊₁ > aₙ
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 0.75rem;">
                            Climbs at every single step (never pauses or dips)
                        </span>
                        <svg viewBox="0 0 380 220" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="45" y1="180" x2="355" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="50" y1="185" x2="50" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="360" y="185" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="50" y="25" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="80" y1="180" x2="80" y2="155" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="80" cy="155" r="5.5" fill="#0284c7" />
                            <text x="80" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <line x1="140" y1="180" x2="140" y2="130" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="140" cy="130" r="5.5" fill="#0284c7" />
                            <text x="140" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <line x1="200" y1="180" x2="200" y2="105" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="200" cy="105" r="5.5" fill="#0284c7" />
                            <text x="200" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <line x1="260" y1="180" x2="260" y2="78" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="260" cy="78" r="5.5" fill="#0284c7" />
                            <text x="260" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <line x1="320" y1="180" x2="320" y2="52" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="320" cy="52" r="5.5" fill="#0284c7" />
                            <text x="320" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 80 155 L 140 130 L 200 105 L 260 78 L 320 52" fill="none" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4" opacity="0.5" />
                        </svg>
                    </div>

                    <!-- PANEL 2: WEAKLY INCREASING -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #059669; display: block; margin-bottom: 0.2rem;">
                            2. Increasing (Weak): aₙ₊₁ &ge; aₙ
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 0.75rem;">
                            Never steps backward, flat plateaus permitted
                        </span>
                        <svg viewBox="0 0 380 220" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="45" y1="180" x2="355" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="50" y1="185" x2="50" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="360" y="185" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="50" y="25" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="80" y1="180" x2="80" y2="150" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="80" cy="150" r="5.5" fill="#059669" />
                            <text x="80" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <line x1="140" y1="180" x2="140" y2="115" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="140" cy="115" r="5.5" fill="#059669" />
                            <text x="140" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <line x1="200" y1="180" x2="200" y2="115" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="200" cy="115" r="5.5" fill="#059669" />
                            <text x="200" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <line x1="140" y1="115" x2="200" y2="115" stroke="#10b981" stroke-width="3" />
                            <text x="170" y="103" font-size="11.5" font-weight="bold" fill="#047857" text-anchor="middle">Plateau: a₁ = a₂</text>

                            <line x1="260" y1="180" x2="260" y2="80" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="260" cy="80" r="5.5" fill="#059669" />
                            <text x="260" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <line x1="320" y1="180" x2="320" y2="52" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="320" cy="52" r="5.5" fill="#059669" />
                            <text x="320" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 80 150 L 140 115 L 200 115 L 260 80 L 320 52" fill="none" stroke="#059669" stroke-width="2" stroke-dasharray="4,4" opacity="0.5" />
                        </svg>
                    </div>

                    <!-- PANEL 3: STRICTLY DECREASING -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #d97706; display: block; margin-bottom: 0.2rem;">
                            3. Strictly Decreasing: aₙ₊₁ &lt; aₙ
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 0.75rem;">
                            Cascades downward at each step (always drops)
                        </span>
                        <svg viewBox="0 0 380 220" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="45" y1="180" x2="355" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="50" y1="185" x2="50" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="360" y="185" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="50" y="25" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="80" y1="180" x2="80" y2="55" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="80" cy="55" r="5.5" fill="#d97706" />
                            <text x="80" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <line x1="140" y1="180" x2="140" y2="85" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="140" cy="85" r="5.5" fill="#d97706" />
                            <text x="140" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <line x1="200" y1="180" x2="200" y2="115" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="200" cy="115" r="5.5" fill="#d97706" />
                            <text x="200" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <line x1="260" y1="180" x2="260" y2="140" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="260" cy="140" r="5.5" fill="#d97706" />
                            <text x="260" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <line x1="320" y1="180" x2="320" y2="160" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="320" cy="160" r="5.5" fill="#d97706" />
                            <text x="320" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 80 55 L 140 85 L 200 115 L 260 140 L 320 160" fill="none" stroke="#d97706" stroke-width="2" stroke-dasharray="4,4" opacity="0.5" />
                        </svg>
                    </div>

                    <!-- PANEL 4: NON-MONOTONIC -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #dc2626; display: block; margin-bottom: 0.2rem;">
                            4. Non-Monotonic: Direction Changes
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 0.75rem;">
                            Zigzags up and down (fails single direction test)
                        </span>
                        <svg viewBox="0 0 380 220" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="45" y1="180" x2="355" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="50" y1="185" x2="50" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="360" y="185" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="50" y="25" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="80" y1="180" x2="80" y2="140" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="80" cy="140" r="5.5" fill="#ef4444" />
                            <text x="80" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <line x1="140" y1="180" x2="140" y2="70" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="140" cy="70" r="5.5" fill="#ef4444" />
                            <text x="140" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <line x1="200" y1="180" x2="200" y2="155" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="200" cy="155" r="5.5" fill="#ef4444" />
                            <text x="200" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <line x1="260" y1="180" x2="260" y2="85" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="260" cy="85" r="5.5" fill="#ef4444" />
                            <text x="260" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <line x1="320" y1="180" x2="320" y2="135" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="320" cy="135" r="5.5" fill="#ef4444" />
                            <text x="320" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 80 140 L 140 70 L 200 155 L 260 85 L 320 135" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4" opacity="0.6" />
                        </svg>
                    </div>
                </div>
            </div>

            <!-- SUBSECTION 3: BOUNDEDNESS -->
            <h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.75rem;">3. Boundedness: Building Fences Around the Infinite List</h3>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                A sequence is bounded if all infinitely many terms live trapped between an impenetrable floor $m$ and ceiling $M$:
            </p>

            <div class="definition-box">
                <strong>Formal Definitions of Bounds:</strong>
                <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.95rem; line-height: 1.75;">
                    <li><strong>Bounded Above:</strong> There exists a real number $M$ such that <span class="nobr">$a_n \le M$</span> for all <span class="nobr">$n \in \mathbb{N}$.</span></li>
                    <li><strong>Bounded Below:</strong> There exists a real number $m$ such that <span class="nobr">$a_n \ge m$</span> for all <span class="nobr">$n \in \mathbb{N}$.</span></li>
                    <li><strong>Bounded:</strong> A sequence is bounded if it is bounded <em>both</em> above and below: <span class="nobr">$$m \le a_n \le M \quad \forall n \in \mathbb{N}$$</span>
                    Equivalently, taking <span class="nobr">$K = \max(|m|, |M|)$,</span> all terms lie trapped in the symmetric interval: <span class="nobr">$|a_n| \le K$.</span></li>
                </ul>
            </div>

            <!-- 2-PANEL RESPONSIVE VISUALIZATION FOR BOUNDEDNESS -->
            <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin: 1.75rem 0; text-align: center;">
                <p style="font-size: 1.05rem; font-weight: 700; color: #1e293b; margin-top: 0; margin-bottom: 0.35rem;">
                    VISUALIZING BOUNDS: Shaded Corridors vs. Unbounded Escapes
                </p>
                <p style="font-size: 0.92rem; color: #64748b; margin-top: 0; margin-bottom: 1.5rem; max-width: 780px; display: inline-block; line-height: 1.6;">
                    A sequence is bounded if all infinitely many terms live trapped inside a horizontal corridor between ceiling $M$ and floor $m$. If terms eventually punch through every horizontal ceiling, the sequence is unbounded.
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; text-align: left;">
                    <!-- PANEL 1: BOUNDED CORRIDOR -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #047857; display: block; margin-bottom: 0.2rem;">
                            1. Bounded Sequence: m &le; aₙ &le; M
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 1rem;">
                            Trapped forever inside a horizontal corridor
                        </span>
                        <svg viewBox="0 0 420 240" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <rect x="75" y="70" width="315" height="95" fill="#ecfdf5" rx="4" opacity="0.9" />
                            <line x1="70" y1="205" x2="395" y2="205" stroke="#0f172a" stroke-width="2" />
                            <line x1="75" y1="210" x2="75" y2="45" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="210" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="75" y="35" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="75" y1="70" x2="390" y2="70" stroke="#059669" stroke-width="2" stroke-dasharray="5,4" />
                            <text x="68" y="75" font-size="13" font-weight="bold" fill="#047857" text-anchor="end">Ceiling M</text>

                            <line x1="75" y1="165" x2="390" y2="165" stroke="#059669" stroke-width="2" stroke-dasharray="5,4" />
                            <text x="68" y="170" font-size="13" font-weight="bold" fill="#047857" text-anchor="end">Floor m</text>

                            <circle cx="110" cy="145" r="5.5" fill="#059669" />
                            <circle cx="150" cy="85" r="5.5" fill="#059669" />
                            <circle cx="190" cy="135" r="5.5" fill="#059669" />
                            <circle cx="230" cy="100" r="5.5" fill="#059669" />
                            <circle cx="270" cy="130" r="5.5" fill="#059669" />
                            <circle cx="310" cy="110" r="5.5" fill="#059669" />
                            <circle cx="350" cy="120" r="5.5" fill="#059669" />

                            <text x="235" y="118" font-size="12" font-weight="bold" fill="#065f46" text-anchor="middle">|aₙ| &le; K (Trapped inside corridor)</text>
                        </svg>
                    </div>

                    <!-- PANEL 2: UNBOUNDED ESCAPE -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #b91c1c; display: block; margin-bottom: 0.2rem;">
                            2. Unbounded Sequence (Escape)
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 1rem;">
                            Punches through any proposed ceiling M
                        </span>
                        <svg viewBox="0 0 420 240" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="70" y1="205" x2="395" y2="205" stroke="#0f172a" stroke-width="2" />
                            <line x1="75" y1="210" x2="75" y2="45" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="210" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="75" y="35" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="75" y1="125" x2="390" y2="125" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4" />
                            <text x="68" y="130" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="end">Ceiling M</text>

                            <circle cx="105" cy="190" r="5.5" fill="#dc2626" />
                            <circle cx="145" cy="170" r="5.5" fill="#dc2626" />
                            <circle cx="195" cy="145" r="5.5" fill="#dc2626" />
                            <circle cx="245" cy="120" r="5.5" fill="#dc2626" />
                            <circle cx="295" cy="85" r="6.5" fill="#dc2626" stroke="#991b1b" stroke-width="2" />
                            <circle cx="345" cy="45" r="6.5" fill="#dc2626" stroke="#991b1b" stroke-width="2" />

                            <line x1="295" y1="115" x2="295" y2="95" stroke="#dc2626" stroke-width="1.8" />
                            <text x="305" y="105" font-size="11.5" font-weight="bold" fill="#b91c1c">Breaks ceiling!</text>
                        </svg>
                    </div>
                </div>
            </div>

            <!-- SECTION 5 -->
            <h2 id="algebra-of-sequences">5. The Algebra of Sequences (Scaling and Sums)</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Sequence Operations &amp; Linear Combinations</h4>
                <div class="infobox-intro">
                    <strong>Locker-by-locker arithmetic:</strong> Algebraic operations on sequences are performed term-by-term. Each new sequence is built by evaluating the operation independently at each index <span class="nobr">$n \in \mathbb{N}$.</span>
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$(\lambda a)_n = \lambda a_n$</span></span><span class="notation-desc">Scalar multiplication: every stored locker value is scaled by real number $\lambda$</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$(a + b)_n = a_n + b_n$</span></span><span class="notation-desc">Sum sequence: locker $n$ contains the sum of terms at matching door index $n$</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$(a \cdot b)_n = a_n b_n$</span></span><span class="notation-desc">Product sequence: term-by-term multiplication at matching door index $n$</span></div>
                    <div class="notation-item"><span class="notation-sym"><span class="nobr">$(a / b)_n = a_n / b_n$</span></span><span class="notation-desc">Quotient sequence: term-by-term division (valid when <span class="nobr">$b_n \ne 0$</span> for all $n$)</span></div>
                </div>
            </div>

            <h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.75rem;">1. Pointwise Operations: Hallways in Parallel</h3>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                In sequence algebra, we are not summing across the lockers of a single hallway. Instead, picture <strong>two parallel locker hallways running side-by-side</strong>: Hallway $A$ and Hallway $B$. Operations happen index-by-index in complete independence.
            </p>

            <h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.75rem;">2. Combining Simple Sequences to Create New Patterns</h3>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                Adding the linear climb $a_n = 2n + 1$ term-by-term to the alternating oscillation $b_n = (-1)^n$ synthesizes an emergent staircase featuring resting plateaus:
            </p>

            <!-- RESPONSIVE COMPARATIVE STEPPING DISPLAY -->
            <div class="stepping-table-container">
                <!-- DESKTOP TABLE -->
                <div style="overflow-x: auto; -webkit-overflow-scrolling: touch;">
                    <table class="desktop-stepping-table">
                        <thead>
                            <tr style="background: #f1f5f9; border-bottom: 2px solid var(--border);">
                                <th style="padding: 0.65rem 0.75rem; color: #475569; font-weight: 600;">Locker $n$</th>
                                <th style="padding: 0.65rem 0.75rem; color: #0284c7; font-weight: 600;">Climb: $a_n = 2n + 1$</th>
                                <th style="padding: 0.65rem 0.75rem; color: #d97706; font-weight: 600;">Bounce: $b_n = (-1)^n$</th>
                                <th style="padding: 0.65rem 0.75rem; color: #059669; font-weight: 600;">Sum: $c_n = a_n + b_n$</th>
                                <th style="padding: 0.65rem 0.75rem; color: #0f172a; font-weight: 600; text-align: left;">Stepping Motion</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 0$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$1$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$+1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$2$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Baseline starting point</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0; background: #f0fdf4;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 1$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$3$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$-1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$2$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: $-1$ cancels climb ($c_1 = c_0$)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 2$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$5$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$+1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$6$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Steps forward by $+4$</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0; background: #f0fdf4;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 3$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$7$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$-1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$6$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: $-1$ cancels climb ($c_3 = c_2$)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 4$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$9$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$+1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$10$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Steps forward by $+4$</td>
                            </tr>
                            <tr>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 5$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$11$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$-1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$10$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: $-1$ cancels climb ($c_5 = c_4$)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- MOBILE STACKED CARDS -->
                <div class="mobile-stepping-cards">
                    <div class="stepping-card">
                        <div class="stepping-card-header">
                            <strong style="color: #0f172a;">Locker n = 0</strong>
                            <span style="font-size: 0.75rem; background: #f1f5f9; padding: 0.2rem 0.5rem; border-radius: 4px; color: #475569; font-weight: 600;">Baseline</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₀)</span>1</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₀)</span>+1</div>
                            <div style="border-left: 2px solid #cbd5e1; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #059669; display: block;">Sum (c₀)</span>
                                <span style="color: #059669; font-size: 1.1rem;">2</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #64748b;">Starting baseline value</p>
                    </div>

                    <div class="stepping-card plateau">
                        <div class="stepping-card-header">
                            <strong style="color: #14532d;">Locker n = 1</strong>
                            <span style="font-size: 0.75rem; background: #dcfce7; color: #166534; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 700;">⏸ Flat Plateau</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₁)</span>3</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₁)</span>-1</div>
                            <div style="border-left: 2px solid #86efac; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #047857; display: block;">Sum (c₁)</span>
                                <span style="color: #047857; font-size: 1.1rem;">2</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #15803d; font-weight: 500;">-1 cancels the +2 climb &rarr; remains at 2 (c₁ = c₀)</p>
                    </div>

                    <div class="stepping-card">
                        <div class="stepping-card-header">
                            <strong style="color: #0f172a;">Locker n = 2</strong>
                            <span style="font-size: 0.75rem; background: #e0f2fe; color: #0369a1; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 600;">+4 Leap</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₂)</span>5</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₂)</span>+1</div>
                            <div style="border-left: 2px solid #cbd5e1; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #059669; display: block;">Sum (c₂)</span>
                                <span style="color: #059669; font-size: 1.1rem;">6</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #64748b;">Advances forward from 2 to 6</p>
                    </div>

                    <div class="stepping-card plateau">
                        <div class="stepping-card-header">
                            <strong style="color: #14532d;">Locker n = 3</strong>
                            <span style="font-size: 0.75rem; background: #dcfce7; color: #166534; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 700;">⏸ Flat Plateau</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₃)</span>7</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₃)</span>-1</div>
                            <div style="border-left: 2px solid #86efac; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #047857; display: block;">Sum (c₃)</span>
                                <span style="color: #047857; font-size: 1.1rem;">6</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #15803d; font-weight: 500;">-1 cancels the +2 climb &rarr; remains at 6 (c₃ = c₂)</p>
                    </div>

                    <div class="stepping-card">
                        <div class="stepping-card-header">
                            <strong style="color: #0f172a;">Locker n = 4</strong>
                            <span style="font-size: 0.75rem; background: #e0f2fe; color: #0369a1; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 600;">+4 Leap</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₄)</span>9</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₄)</span>+1</div>
                            <div style="border-left: 2px solid #cbd5e1; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #059669; display: block;">Sum (c₄)</span>
                                <span style="color: #059669; font-size: 1.1rem;">10</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #64748b;">Advances forward from 6 to 10</p>
                    </div>

                    <div class="stepping-card plateau">
                        <div class="stepping-card-header">
                            <strong style="color: #14532d;">Locker n = 5</strong>
                            <span style="font-size: 0.75rem; background: #dcfce7; color: #166534; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 700;">⏸ Flat Plateau</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₅)</span>11</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₅)</span>-1</div>
                            <div style="border-left: 2px solid #86efac; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #047857; display: block;">Sum (c₅)</span>
                                <span style="color: #047857; font-size: 1.1rem;">10</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #15803d; font-weight: 500;">-1 cancels the +2 climb &rarr; remains at 10 (c₅ = c₄)</p>
                    </div>
                </div>
            </div>

            <!-- SECTION 6 -->
            <h2 id="derived-sequences">6. Discrete Calculus: The Derived Sequence (<span class="nobr">$a_n'$</span>)</h2>
            <!-- HISTORICAL PROFILE: BROOK TAYLOR -->
            <div class="biography-box" style="margin-top: 2rem;">
                <div style="display: flex; flex-direction: row; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/taylor.jpg" alt="Brook Taylor portrait" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: block; margin-bottom: 0.5rem;">
                        <span style="font-weight: 700; font-size: 0.85rem; color: #0f172a; display: block; text-align: center;">Brook Taylor</span>
                        <span style="font-size: 0.75rem; color: #64748b; display: block; text-align: center;">(1685–1731)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #3730a3; font-size: 1.05rem;">
                            Historical Profile: The Pioneer of Finite Differences
                        </h4>
                        <p style="font-size: 0.92rem; line-height: 1.65; color: #334155; margin-bottom: 0.75rem;">
                            <strong>Background:</strong> An English mathematician and Secretary of the Royal Society, Brook Taylor approached change through discrete increments.
                        </p>
                        <ul style="font-size: 0.9rem; line-height: 1.6; color: #334155; margin: 0 0 0.75rem 1.25rem; padding: 0;">
                            <li>Published <em>Methodus Incrementorum Directa et Inversa</em> (1715), formally inaugurating the <strong>calculus of finite differences</strong>.</li>
                            <li>Formulated Taylor's Theorem as the natural limiting case when discrete step sizes approach zero.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="definition-box">
                <strong>Formal Definition: The Derived Sequence (<span class="nobr">$a_n'$</span>):</strong><br>
                Given a sequence <span class="nobr">$(a_n)_{n=0}^\infty$,</span> the <strong>derived sequence</strong> is defined by neighbor subtraction:
                <div style="text-align: center; margin: 0.5rem 0; font-size: 1.05rem;">
                    $$a_n' = a_{n+1} - a_n \quad (n \ge 0)$$
                </div>
            </div>

            <!-- SECTION 7 -->
            <h2 id="discrete-integration">7. Reversing the Difference: Partial Sums and Series</h2>
            <!-- HISTORICAL PROFILE: CARL FRIEDRICH GAUSS -->
            <div class="biography-box" style="margin-top: 2rem;">
                <div style="display: flex; flex-direction: row; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/gauss.jpg" alt="Carl Friedrich Gauss portrait" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: block; margin-bottom: 0.5rem;">
                        <span style="font-weight: 700; font-size: 0.85rem; color: #0f172a; display: block; text-align: center;">Carl Friedrich Gauss</span>
                        <span style="font-size: 0.75rem; color: #64748b; display: block; text-align: center;">(1777–1855)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #3730a3; font-size: 1.05rem;">
                            Historical Profile: The Prince of Mathematicians
                        </h4>
                        <p style="font-size: 0.92rem; line-height: 1.65; color: #334155; margin-bottom: 0.75rem;">
                            <strong>Background:</strong> Widely regarded as the <em>Princeps mathematicorum</em>, Gauss discovered the summation formula for consecutive integers at age nine by pairing terms from opposite ends.
                        </p>
                        <ul style="font-size: 0.9rem; line-height: 1.6; color: #334155; margin: 0 0 0.75rem 1.25rem; padding: 0;">
                            <li>Published <em>Disquisitiones Arithmeticae</em> (1801), founding modern number theory.</li>
                            <li>Formalized the famous summation identity: <span class="nobr">$\sum_{k=1}^n k = \frac{n(n+1)}{2}$.</span></li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="definition-box" style="border-left-color: #0284c7;">
                <strong>The Discrete Fundamental Theorem of Calculus (Telescoping Identity):</strong><br>
                For any sequence <span class="nobr">$(a_n)_{n=0}^\infty$,</span> the sum of consecutive differences collapses to the net change:
                <div style="text-align: center; margin: 0.65rem 0; font-size: 1.15rem; font-weight: 600; color: #0369a1;">
                    $$\sum_{k=0}^{n-1} a_k' = \sum_{k=0}^{n-1} (a_{k+1} - a_k) = a_n - a_0$$
                </div>
                Reconstructing any future term from its steps:
                <div style="text-align: center; margin: 0.5rem 0; font-size: 1.1rem; color: #047857;">
                    $$a_n = a_0 + \sum_{k=0}^{n-1} a_k'$$
                </div>
            </div>

            <!-- SECTION 8 -->
            <h2 id="grand-arc">8. The Grand Arc: From Discrete Rungs to the Infinite Horizon</h2>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1.25rem;">
                As we close out Week 1, our first three lectures form an interconnected narrative designed to handle infinity rigorously:
            </p>
            <ol style="margin: 0 0 1.5rem 1.5rem; font-size: 0.98rem; line-height: 1.75; color: #334155;">
                <li style="margin-bottom: 0.75rem;"><strong>Lecture 1 (Grammar):</strong> Sets, Cartesian products, rigorous mappings, and induction.</li>
                <li style="margin-bottom: 0.75rem;"><strong>Lecture 2 (Continuum):</strong> Density gaps, absolute value metrics, and the Completeness Axiom.</li>
                <li style="margin-bottom: 0.75rem;"><strong>Lecture 3 (Discrete Motion):</strong> Sequences, difference operators, and telescoping summation.</li>
            </ol>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 2rem;">
                In <strong>Week 2</strong>, armed with our complete real line and bounded sequences, we enter the beating heart of analysis: <strong>Limits and Convergence</strong> (<span class="nobr">$\lim_{n \to \infty} a_n = L$</span>). Congratulations on completing Week 1!
            </p>

            <!-- FOOTER NAVIGATION -->
            <div class="footer-nav" style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: center; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
                <a href="week1-lecture2.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&larr; Lecture 2</a>
                <a href="week1.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&uarr; Week 1 Hub</a>
                <a href="week2-lecture4.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">Lecture 4 &rarr;</a>
            </div>
        </div>
    </div>

    <!-- SCRIPT FOR PROGRESSION STEPPING SIMULATOR -->
    <script>
    (function() {
        const config = {
            arithmetic: {
                title: "Arithmetic Progression (a = 3, b = 2)",
                color: "#0284c7",
                minVal: 0,
                maxVal: 20,
                steps: [
                    { n: 0, val: 2, op: "Initial Base", formula: "b = 2", preview: "Standing in front of Locker 0. Reading baseline parameter b before any strides are taken.", what: "The sequence initializes at position c₀ = 2. Zero strides of size a = 3 have occurred.", why: "In an arithmetic model cₙ = an + b, the term an vanishes when n = 0, leaving pure baseline b." },
                    { n: 1, val: 5, op: "Added +3", formula: "2 + 3 = 5", preview: "Taking first stride. Advancing from Locker 0 to Locker 1 by adding fixed difference a = 3.", what: "The value moves from 2 to 5 by adding stride a = 3. One step executed.", why: "Discrete stepping advances by constant addition: c₁ = c₀ + a = 2 + 3." },
                    { n: 2, val: 8, op: "Added +3", formula: "2 + 3(2) = 8", preview: "Taking second stride. Stacking another stride of size 3 to reach Locker 2.", what: "The position advances to 8. Two strides of size 3 have now accumulated.", why: "Repeated addition compresses into multiplication by index n: 2 + 3 + 3 = 2 + 3(2)." },
                    { n: 3, val: 11, op: "Added +3", formula: "2 + 3(3) = 11", preview: "Taking third stride. Marching along the line at an exact steady, rhythmic pace.", what: "The position advances to 11. Stride length remains identically 3 units.", why: "Notice the rate of change is constant: cₙ' = cₙ₊₁ - cₙ = 3 everywhere." },
                    { n: 4, val: 14, op: "Added +3", formula: "2 + 3(4) = 14", preview: "Taking fourth stride. Leaping directly forward without changing stride width.", what: "The position advances to 14. Four identical intervals of 3 have been traversed.", why: "Direct calculation c₄ = 3(4) + 2 = 14 matches the 4-step walk identically." },
                    { n: 5, val: 17, op: "Added +3", formula: "2 + 3(5) = 17", preview: "Reaching fifth waypoint. Verifying linear progression along the locker corridor.", what: "We arrive at Locker 5 with c₅ = 17. Total distance gained is 5 × 3 = 15 units.", why: "Linear growth has no surprises: every single gap across the corridor is congruent." }
                ]
            },
            geom_growth: {
                title: "Geometric Growth (a = 2, q = 2)",
                color: "#059669",
                minVal: 0,
                maxVal: 68,
                steps: [
                    { n: 0, val: 2, op: "Initial Base", formula: "a · q⁰ = 2", preview: "Standing in front of Locker 0. Base scale factor initialized to a = 2.", what: "Quantity starts at c₀ = 2. Zero zoom multiplications have taken place.", why: "Because q⁰ = 1 for any non-zero ratio, c₀ = a · 1 = a." },
                    { n: 1, val: 4, op: "Scaled ×2", formula: "2 · 2¹ = 4", preview: "Applying first scaling factor. Doubling contents of Locker 0 to fill Locker 1.", what: "Current value 2 is multiplied by common ratio q = 2, reaching 4.", why: "Geometric steps advance by ratio multiplication: c₁ = c₀ · q = 2 · 2." },
                    { n: 2, val: 8, op: "Scaled ×2", formula: "2 · 2² = 8", preview: "Applying second doubling. Stride length between lockers visibly doubles.", what: "Value jumps from 4 to 8. Notice the jump distance (4) is already twice the first jump (2).", why: "Repeated multiplication creates exponents: c₂ = a · q · q = a · q²." },
                    { n: 3, val: 16, op: "Scaled ×2", formula: "2 · 2³ = 16", preview: "Third doubling step. Observe the stride beginning to stretch aggressively across the canvas.", what: "Value jumps from 8 to 16. Jump span is 8 units.", why: "Each step difference is itself growing: cₙ' = a(q - 1)qⁿ = 2(1)2ⁿ = cₙ." },
                    { n: 4, val: 32, op: "Scaled ×2", formula: "2 · 2⁴ = 32", preview: "Fourth doubling step. The gap expands past all previous milestones combined.", what: "Value grows from 16 to 32. One single jump covers more ground than the whole prior journey.", why: "Exponential acceleration: powers of 2 outpace any linear stride after few steps." },
                    { n: 5, val: 64, op: "Scaled ×2", formula: "2 · 2⁵ = 64", preview: "Final station reached. Total magnification reaches 32-fold over Locker 0.", what: "We reach Locker 5 with c₅ = 64. Initial quantity 2 has multiplied by 2⁵ = 32.", why: "In geometric growth, index n determines how many times ratio q multiplies itself." }
                ]
            },
            geom_decay: {
                title: "Geometric Decay (a = 64, q = 0.5)",
                color: "#d97706",
                minVal: 0,
                maxVal: 68,
                steps: [
                    { n: 0, val: 64, op: "Initial Base", formula: "64 · (½)⁰ = 64", preview: "Standing in front of Locker 0. Initial level starting at 64.", what: "Sample starts at magnitude c₀ = 64. Zero decay intervals elapsed.", why: "Initial term corresponds to zero multiplications: c₀ = 64 · 1 = 64." },
                    { n: 1, val: 32, op: "Scaled ×0.5", formula: "64 · (½)¹ = 32", preview: "First half-step interval. Halving value from 64 down to 32.", what: "Value drops by 32 units, arriving at position 32.", why: "Ratio q = ½ causes contraction: c₁ = 64 · ½ = 32." },
                    { n: 2, val: 16, op: "Scaled ×0.5", formula: "64 · (½)² = 16", preview: "Second half-step interval. Stride drops to 16 units as values contract.", what: "Value drops from 32 to 16. The step size itself has been cut in half.", why: "Successive steps compress: c₂ = 64 · (½)² = 64 · 1/4 = 16." },
                    { n: 3, val: 8, op: "Scaled ×0.5", formula: "64 · (½)³ = 8", preview: "Third interval. Steps grow progressively tighter as value nears zero floor.", what: "Value contracts to 8. Jump size is now only 8 units.", why: "Differences become smaller and smaller: decay naturally decelerates toward zero." },
                    { n: 4, val: 4, op: "Scaled ×0.5", formula: "64 · (½)⁴ = 4", preview: "Fourth interval. Approaching zero asymptotically without crossing it.", what: "Value drops to 4. All terms remain strictly positive (cₙ > 0).", why: "Multiplying positive numbers by positive fractions can never produce a negative." },
                    { n: 5, val: 2, op: "Scaled ×0.5", formula: "64 · (½)⁵ = 2", preview: "Fifth interval. Initial value has reduced to a small fraction of baseline.", what: "We reach Locker 5 with c₅ = 2. The value has shrunk by a factor of (½)⁵ = 1/32.", why: "Geometric decay models half-life, depreciation, and asymptotic convergence." }
                ]
            }
        };

        let activeMode = 'arithmetic';
        let currentStep = 0;

        function renderCanvas() {
            const svg = document.getElementById('stepper-canvas');
            if (!svg) return;
            const mode = config[activeMode];
            const stepData = mode.steps[currentStep];
            const minV = mode.minVal;
            const maxV = mode.maxVal;

            const leftX = 50;
            const rightX = 710;
            const axisY = 100;

            function scaleX(val) {
                return leftX + ((val - minV) / (maxV - minV)) * (rightX - leftX);
            }

            let html = '';
            html += `<line x1="${leftX - 15}" y1="${axisY}" x2="${rightX + 25}" y2="${axisY}" stroke="#0f172a" stroke-width="2" />`;
            html += `<polygon points="${rightX + 32},${axisY} ${rightX + 22},${axisY - 4} ${rightX + 22},${axisY + 4}" fill="#0f172a" />`;
            html += `<text x="${rightX + 35}" y="${axisY + 4}" font-size="11" font-weight="bold" fill="#0f172a">val</text>`;

            mode.steps.forEach((s, idx) => {
                const sx = scaleX(s.val);
                const isPassed = idx <= currentStep;
                const isCurrent = idx === currentStep;

                html += `<line x1="${sx}" y1="${axisY - 5}" x2="${sx}" y2="${axisY + 5}" stroke="${isPassed ? mode.color : '#94a3b8'}" stroke-width="${isCurrent ? '2.5' : '1.5'}" />`;
                html += `<text x="${sx}" y="${axisY + 20}" font-size="10.5" font-family="monospace" font-weight="${isCurrent ? 'bold' : 'normal'}" fill="${isCurrent ? mode.color : '#64748b'}" text-anchor="middle">${s.val}</text>`;
                html += `<text x="${sx}" y="${axisY + 34}" font-size="9" fill="${isCurrent ? '#0f172a' : '#94a3b8'}" text-anchor="middle">n=${s.n}</text>`;
            });

            for (let i = 0; i < currentStep; i++) {
                const startX = scaleX(mode.steps[i].val);
                const endX = scaleX(mode.steps[i + 1].val);
                const midX = (startX + endX) / 2;
                const hopHeight = Math.min(60, Math.max(25, Math.abs(endX - startX) * 0.35));
                const controlY = axisY - hopHeight;

                const isLastHop = (i === currentStep - 1);
                const strokeColor = isLastHop ? mode.color : '#cbd5e1';
                const strokeWidth = isLastHop ? 2.5 : 1.5;

                html += `<path d="M ${startX} ${axisY} Q ${midX} ${controlY} ${endX} ${axisY}" fill="none" stroke="${strokeColor}" stroke-width="${strokeWidth}" stroke-dasharray="${isLastHop ? 'none' : '3,3'}" />`;

                if (isLastHop) {
                    const badgeText = activeMode === 'arithmetic' ? '+3' : (activeMode === 'geom_growth' ? '×2' : '×0.5');
                    html += `<rect x="${midX - 16}" y="${controlY - 14}" width="32" height="16" rx="4" fill="${mode.color}" />`;
                    html += `<text x="${midX}" y="${controlY - 2}" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">${badgeText}</text>`;
                }
            }

            const curX = scaleX(stepData.val);
            html += `<circle cx="${curX}" cy="${axisY}" r="7" fill="${mode.color}" stroke="#ffffff" stroke-width="2.5" />`;
            html += `<circle cx="${curX}" cy="${axisY}" r="13" fill="${mode.color}" opacity="0.25" />`;

            svg.innerHTML = html;
        }

        function renderTelemetry() {
            const mode = config[activeMode];
            const stepData = mode.steps[currentStep];

            document.getElementById('telem-n').textContent = stepData.n;
            document.getElementById('telem-val').textContent = stepData.val;
            document.getElementById('telem-op').textContent = stepData.op;
            document.getElementById('telem-formula').textContent = stepData.formula;
        }

        function renderPanels() {
            const mode = config[activeMode];
            const stepData = mode.steps[currentStep];

            document.getElementById('inline-preview-text').textContent = stepData.preview;
            document.getElementById('pane-what').textContent = stepData.what;
            document.getElementById('pane-why').textContent = stepData.why;

            const btnPrev = document.getElementById('btn-prev');
            const btnNext = document.getElementById('btn-next');
            btnPrev.disabled = (currentStep === 0);
            btnNext.disabled = (currentStep === mode.steps.length - 1);
            btnPrev.style.opacity = (currentStep === 0) ? '0.5' : '1';
            btnNext.style.opacity = (currentStep === mode.steps.length - 1) ? '0.5' : '1';
        }

        function updateDisplay() {
            renderCanvas();
            renderTelemetry();
            renderPanels();
        }

        window.setMode = function(modeKey) {
            activeMode = modeKey;
            currentStep = 0;

            ['arithmetic', 'geom_growth', 'geom_decay'].forEach(k => {
                const btn = document.getElementById('toggle-' + k.replace('_', '-'));
                if (k === modeKey) {
                    btn.style.background = '#ffffff';
                    btn.style.color = config[k].color;
                    btn.style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
                } else {
                    btn.style.background = 'transparent';
                    btn.style.color = '#475569';
                    btn.style.boxShadow = 'none';
                }
            });

            updateDisplay();
        };

        window.stepNext = function() {
            if (currentStep < config[activeMode].steps.length - 1) {
                currentStep++;
                updateDisplay();
            }
        };

        window.stepPrev = function() {
            if (currentStep > 0) {
                currentStep--;
                updateDisplay();
            }
        };

        window.resetStepper = function() {
            currentStep = 0;
            updateDisplay();
        };

        document.addEventListener('DOMContentLoaded', updateDisplay);
        if (document.readyState === 'complete' || document.readyState === 'interactive') {
            updateDisplay();
        }
    })();
    </script>
</body>
</html>
"""

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def main() -> None:
    target = Path("week1-lecture3.html")
    target.write_text(CLEAN_HTML.strip() + "\n", encoding="utf-8")
    print(f"Successfully regenerated clean {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Regenerate clean, fully responsive Week 1 Lecture 3"
        commit_body = (
            "Restore complete week1-lecture3.html document. Resolves broken\n"
            "DOM boundaries, fixes duplicate style blocks, standardizes\n"
            "biography cards, and restores legible mobile SVG diagrams."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed regenerated lecture document.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
