#!/usr/bin/env python3
"""
Write out the updated week2.html page with a grounded, empathetic introduction
and a clean, prose-driven roadmap without redundant cards.
"""

from pathlib import Path
import sys

TARGET_FILE = Path("week2.html")

HTML_CONTENT = r"""<!DOCTYPE html>
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
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .intro-lead { font-size: 1.05rem; color: #1e293b; line-height: 1.75; margin-bottom: 2rem; background: #f8fafc; padding: 1.75rem; border-radius: 8px; border: 1px solid var(--border); border-left: 5px solid var(--accent); }
        .intro-lead h3 { margin-top: 0; margin-bottom: 0.75rem; color: #0f172a; font-size: 1.25rem; }
        .intro-lead p { margin: 0 0 1rem 0; }
        .intro-lead p:last-child { margin-bottom: 0; }

        .orientation-section { margin: 2rem 0 2.5rem 0; color: #334155; line-height: 1.75; font-size: 1rem; }
        .orientation-section h3 { margin-top: 0; color: #0f172a; font-size: 1.25rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem; margin-bottom: 1rem; }
        .orientation-section p { margin-bottom: 1.15rem; }

        h2 { border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; margin-top: 2.5rem; color: #0f172a; font-family: var(--font-ui); scroll-margin-top: 2rem; }
        h3 { color: #1e293b; margin-top: 1.5rem; font-family: var(--font-ui); scroll-margin-top: 2rem; }

        .lecture-card { background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; transition: transform 0.15s ease, box-shadow 0.15s ease; }
        .lecture-card:hover { transform: translateY(-2px); box-shadow: 0 6px 12px -2px rgba(0,0,0,0.08); border-color: var(--accent); }
        .lecture-card h3 { margin-top: 0; color: #0f172a; }
        .lecture-badge { display: inline-block; background: var(--accent); color: white; padding: 0.2rem 0.55rem; border-radius: 4px; font-weight: 700; font-size: 0.8rem; text-transform: uppercase; margin-bottom: 0.5rem; }

        /* Mobile-first adjustments */
        @media (max-width: 768px) {
            .katex-display { overflow-x: auto !important; overflow-y: hidden !important; -webkit-overflow-scrolling: touch !important; max-width: 100% !important; padding: 0.25rem 0 !important; }
            body { background: #ffffff; padding: 1rem 0.75rem; }
            .container { max-width: 100%; margin: 0; }
            .module-content { background: transparent; padding: 0; border: none; border-radius: 0; box-shadow: none; margin-bottom: 1rem; }
            .header { padding-bottom: 0.75rem; margin-bottom: 1.25rem; }
            .header > div:last-child, .nav-btn-group { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; width: 100% !important; gap: 0.5rem !important; }
            .header > div:last-child a, .nav-btn-group a { flex: 1 1 0 !important; min-width: 0 !important; text-align: center !important; padding: 0.55rem 0.4rem !important; font-size: 0.82rem !important; white-space: nowrap !important; overflow: hidden !important; text-overflow: ellipsis !important; }
            p, div, li, blockquote { word-break: break-word; overflow-wrap: break-word; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- TOP NAVIGATION HEADER -->
        <div class="header" style="border-bottom: 2px solid var(--border); padding-bottom: 1.5rem; margin-bottom: 2rem; display: flex; flex-direction: column; align-items: center; gap: 1.25rem;">
            <div class="nav-btn-group" style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap; width: 100%;">
                <a href="week1.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&larr; Prev Week</a>
                <a href="index.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&#8962; Curriculum Index</a>
                <span style="background: #f1f5f9; color: #94a3b8; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; font-weight: 600; font-size: 0.88rem; cursor: not-allowed; text-align: center; white-space: nowrap;">Next Week &rarr;</span>
            </div>
            <div style="text-align: center; width: 100%; min-width: 0;">
                <h1 style="margin: 0; line-height: 1.3; font-size: 1.5rem;">Week 2 Overview Hub</h1>
            </div>
        </div>

        <div class="module-content">
            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter2-hero.jpg" alt="Week 2: Limits of Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <!-- EMPATHETIC ORIENTATION LEAD -->
            <div class="intro-lead">
                <h3>A Gentle Note Before You Begin: You Belong Here</h3>
                <p>
                    If opening this page brings a sudden wave of hesitation, pause and take a steady breath. The transition from introductory calculus to real analysis is notorious for making even dedicated students feel completely disoriented. In calculus, you learned how to compute answers with recipes and algebraic steps. Here, we suddenly ask you to defend <em>why</em> those answers are true, using Greek letters ($\epsilon$, $\delta$), nested quantifiers ($\forall$, $\exists$), and inequalities that can feel backwards at first glance.
                </p>
                <p>
                    Feeling friction right now does not mean you lack mathematical ability—it means your brain is being asked to think in an entirely new way. Nobody reads an $\epsilon\text{-}N$ proof for the first time and finds it obvious. Real mathematicians do not write these proofs in one neat pass; they make messy scratches on scrap paper, test guesses, and only polish the logic at the very end. Be kind to yourself this week, take breaks when your mind feels full, and trust that the intuition will click as you spend time with the pictures behind the symbols.
                </p>
            </div>

            <!-- PROSE-DRIVEN ROADMAP -->
            <div class="orientation-section">
                <h3>The Big Picture: Demystifying "Approaching Infinity"</h3>
                <p>
                    In earlier math courses, limits are usually introduced as an intuitive movie: <em>"as $n$ gets larger and larger, the terms $a_n$ move closer and closer to $L$."</em> That mental picture is a wonderful place to start, but pure mathematics asks a deeper, practical question: how do you guarantee that a sequence doesn't suddenly drift away when you look away?
                </p>
                <p>
                    The great breakthrough of analysis was replacing the slippery idea of "getting closer" with an ironclad guarantee of distance. Instead of watching motion, we establish a challenge: you specify any tiny tolerance window you like—no matter how microscopically narrow—and we show that after a certain point down the line, every single term remains trapped inside that window forever.
                </p>
                <p>
                    Across this week's three lectures, we unpack that single idea one step at a time:
                </p>
                <p>
                    We start in <strong>Lecture 4 (Formal $\epsilon\text{-}N$ Convergence and Limit Laws)</strong> by stripping the fear from the definition. We treat convergence like target practice: you name the tolerance $\epsilon$, and we find the cutoff locker index $N$ after which every term hits the target. Once that foundation is solid, we prove that convergent sequences can never wander off to infinity (they are bounded) and build reliable algebraic rules for combining limits.
                </p>
                <p>
                    In <strong>Lecture 5 (The Monotone Convergence Theorem and Squeeze Principle)</strong>, we ask what happens when a sequence only moves in one direction—always climbing or always falling—but runs straight into a solid boundary. Completeness guarantees that it must settle against that ceiling, giving us a powerful way to define numbers like $e$ without guessing. We then learn how to handle erratic, oscillating terms by trapping them between two well-behaved sequences in the Squeeze Principle.
                </p>
                <p>
                    Finally, in <strong>Lecture 6 (Recursive Sequences and Divergence to Infinity)</strong>, we investigate sequences generated by feedback loops, where each step depends on the previous one. We explore why calculating limits before proving they actually exist leads to subtle traps, and we establish the formal benchmark for when sequences refuse to settle down at all, breaking past every conceivable floor to $+\infty$.
                </p>
                <p style="background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid var(--accent); border-radius: 6px; padding: 1rem 1.25rem; font-size: 0.95rem; color: #92400e;">
                    <strong>Pacing Advice:</strong> Treat each lecture as an exploration, not a race. Read the intuitive explanations first, look at the visual diagrams, and let the formal definitions settle naturally before diving into algebraic proofs.
                </p>
            </div>

            <div style="margin: 2rem 0;">
                <h2 style="margin-top: 0;">Weekly Lecture Modules</h2>
                <p style="color: #475569; font-size: 1.05rem;">Select a lecture module below to begin:</p>
            </div>

            <!-- LECTURE 4 CARD -->
            <div class="lecture-card">
                <span class="lecture-badge">Lecture 4</span>
                <h3><a href="week2-lecture4.html" style="color: inherit; text-decoration: none;">Formal $\epsilon\text{-}N$ Convergence and Limit Laws &rarr;</a></h3>
                <p style="color: #334155; margin-bottom: 1rem;">
                    Master the formal $\epsilon\text{-}N$ definition of convergence through interactive archery simulators, explore quantifier order dependencies, prove sequence boundedness, and establish the algebraic limit laws for sums, products, and quotients.
                </p>
                <div>
                    <a href="week2-lecture4.html" style="background: var(--accent); color: white; padding: 0.45rem 0.9rem; border-radius: 5px; text-decoration: none; font-weight: 600; font-size: 0.88rem;">Open Lecture 4 &rarr;</a>
                </div>
            </div>

            <!-- LECTURE 5 CARD -->
            <div class="lecture-card">
                <span class="lecture-badge">Lecture 5</span>
                <h3><a href="week2-lecture5.html" style="color: inherit; text-decoration: none;">The Monotone Convergence Theorem and the Squeeze Principle &rarr;</a></h3>
                <p style="color: #334155; margin-bottom: 1rem;">
                    Connect sequence limits to suprema and real completeness. Study the full proof of the Monotone Convergence Theorem, trace Euler's number $e = \lim (1 + 1/n)^n$, explore the lottery thought experiment, and sandwich trigonometric sequences using the Squeeze Theorem.
                </p>
                <div>
                    <a href="week2-lecture5.html" style="background: var(--accent); color: white; padding: 0.45rem 0.9rem; border-radius: 5px; text-decoration: none; font-weight: 600; font-size: 0.88rem;">Open Lecture 5 &rarr;</a>
                </div>
            </div>

            <!-- LECTURE 6 CARD -->
            <div class="lecture-card">
                <span class="lecture-badge">Lecture 6</span>
                <h3><a href="week2-lecture6.html" style="color: inherit; text-decoration: none;">Recursive Sequences and Divergence to Infinity &rarr;</a></h3>
                <p style="color: #334155; margin-bottom: 1rem;">
                    Learn why blind algebraic substitution fails on recurrence relations, prove error contraction for continued fractions approximating $\sqrt{2}$, master the 4-step recursive strategy, and formalize divergence to infinity via the $M\text{-}N$ towering floor test.
                </p>
                <div>
                    <a href="week2-lecture6.html" style="background: var(--accent); color: white; padding: 0.45rem 0.9rem; border-radius: 5px; text-decoration: none; font-weight: 600; font-size: 0.88rem;">Open Lecture 6 &rarr;</a>
                </div>
            </div>

            <!-- FOOTER NAVIGATION -->
            <div class="footer-nav" style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: center; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
                <a href="week1.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&larr; Prev Week</a>
                <a href="index.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">&#8962; Curriculum Index</a>
                <span style="background: #f1f5f9; color: #94a3b8; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; font-weight: 600; font-size: 0.88rem; cursor: not-allowed; text-align: center; white-space: nowrap;">Next Week &rarr;</span>
            </div>
        </div>
    </div>
</body>
</html>
"""


def write_week2_hub(file_path: Path) -> None:
    file_path.write_text(HTML_CONTENT, encoding="utf-8")
    print(f"Successfully written to {file_path}")


if __name__ == "__main__":
    try:
        write_week2_hub(TARGET_FILE)
    except OSError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)
