#!/usr/bin/env python3
import os
import subprocess

def update_curriculum_index():
    if not os.path.exists('index.html'):
        print("index.html not found in current directory.")
        return

    updated_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MTHS120: Calculus and Linear Algebra Notes</title>
    <!-- KaTeX Integration -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
    <style>
        :root {
            --bg: #f8fafc; --text: #0f172a; --card: #ffffff; --border: #cbd5e1;
            --accent: #d97706; --accent-hover: #b45309;
            --telemetry-bg: #f8fafc; --telemetry-text: #334155;
            --track1-bg: #fffbeb; --track2-bg: #fff7ed;
            --font-ui: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
        body { font-family: var(--font-ui); background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; }

        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; }
        .header h1 { color: #0f172a; margin-top: 0; font-size: 2rem; }
        .header p { color: #64748b; margin-bottom: 0; }

        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .intro-lead { font-size: 1.05rem; color: #1e293b; line-height: 1.7; margin-bottom: 2rem; background: #f1f5f9; padding: 1.5rem; border-radius: 6px; border-left: 4px solid var(--accent); border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }

        /* Hero Banner Component */
        .welcome-hero {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-left: 5px solid var(--accent);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 2.5rem;
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }
        .welcome-hero-image-wrap {
            width: 100%;
            border-radius: 6px;
            overflow: hidden;
            border: 1px solid #fed7aa;
            background: #ffffff;
        }
        .welcome-hero-image {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Modules Grid */
        .modules-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.25rem;
            margin-top: 1.5rem;
        }
        .week-card {
            background: var(--card);
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: border-color 0.2s, box-shadow 0.2s;
        }
        .week-card:hover {
            border-color: #94a3b8;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        }
        .week-card h4 {
            margin-top: 0;
            color: #0f172a;
            font-size: 1.1rem;
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }
        .week-badge {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            background: #f1f5f9;
            color: #475569;
        }
        .week-badge.active {
            background: #fef3c7;
            color: #92400e;
        }
        .week-card p {
            color: #475569;
            font-size: 0.95rem;
            line-height: 1.5;
            margin: 0.5rem 0 1.25rem 0;
            flex-grow: 1;
        }
        .module-link {
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: 0.55rem 1rem;
            border-radius: 4px;
            font-weight: 600;
            text-decoration: none;
            font-size: 0.9rem;
            text-align: center;
            transition: background 0.2s;
        }
        .module-link:hover {
            background: var(--accent-hover);
        }
        .module-link.disabled {
            background: #e2e8f0;
            color: #94a3b8;
            cursor: default;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>MTHS120: Study Notes & Interactive Modules</h1>
            <p>Personal reference notes, visualizations, and worked derivations for single-variable calculus and linear algebra.</p>
        </div>

        <div class="module-content">
            <div class="intro-lead">
                This site organizes core curriculum topics into self-contained interactive notes. Modules combine rigorous mathematical formalism, worked examples, and interactive step-throughs designed to build mechanical intuition for real analysis, rates of change, accumulation, and matrix systems.
            </div>

            <!-- Welcome Visual Banner -->
            <div class="welcome-hero">
                <div class="welcome-hero-image-wrap">
                    <img src="images/welcome-mth120.jpeg" alt="Overview of Course Mathematics" class="welcome-hero-image">
                </div>
            </div>

            <h3 style="margin-top: 1rem;">Course Modules</h3>

            <div class="modules-grid">
                <!-- Week 1 -->
                <div class="week-card">
                    <div>
                        <h4>Week 1 <span class="week-badge active">Available</span></h4>
                        <p><strong>Sets, Numbers, and Sequences:</strong> Set-builder notation, algebraic closures ($\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$), monotonicity, boundedness, and the formal $\epsilon-N$ sequence limit definition.</p>
                    </div>
                    <a href="week1.html" class="module-link">Open Module 1 &rarr;</a>
                </div>

                <!-- Week 2 -->
                <div class="week-card">
                    <div>
                        <h4>Week 2 <span class="week-badge">Planned</span></h4>
                        <p><strong>Functions and Continuity:</strong> Domain, codomain, function composition, $\epsilon-\delta$ definitions of continuity, and the Intermediate Value Theorem.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 3 -->
                <div class="week-card">
                    <div>
                        <h4>Week 3 <span class="week-badge">Planned</span></h4>
                        <p><strong>The Derivative:</strong> Difference quotients, instantaneous rates of change, tangent lines, and fundamental rules of differentiation.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 4 -->
                <div class="week-card">
                    <div>
                        <h4>Week 4 <span class="week-badge">Planned</span></h4>
                        <p><strong>Techniques of Differentiation:</strong> The Product Rule, Quotient Rule, Chain Rule, implicit differentiation, and higher-order derivatives.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 5 -->
                <div class="week-card">
                    <div>
                        <h4>Week 5 <span class="week-badge">Planned</span></h4>
                        <p><strong>Curve Sketching & Critical Points:</strong> First and second derivative tests, concavity, points of inflection, and local vs. global extrema.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 6 -->
                <div class="week-card">
                    <div>
                        <h4>Week 6 <span class="week-badge">Planned</span></h4>
                        <p><strong>One-Variable Optimization:</strong> Formulating applied rate models, physical constraints, boundary evaluation, and maximizing/minimizing continuous systems.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 7 -->
                <div class="week-card">
                    <div>
                        <h4>Week 7 <span class="week-badge">Planned</span></h4>
                        <p><strong>Anti-Derivatives & The Indefinite Integral:</strong> Reversing differentiation, initial value problems, and standard integration rules.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 8 -->
                <div class="week-card">
                    <div>
                        <h4>Week 8 <span class="week-badge">Planned</span></h4>
                        <p><strong>Riemann Sums & The Definite Integral:</strong> Partition limits, signed area, accumulation models, and the Fundamental Theorem of Calculus.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 9 -->
                <div class="week-card">
                    <div>
                        <h4>Week 9 <span class="week-badge">Planned</span></h4>
                        <p><strong>Integration Techniques & Applications:</strong> Change of variables (u-substitution), area between curves, volume by slicing, and accumulation from density functions.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 10 -->
                <div class="week-card">
                    <div>
                        <h4>Week 10 <span class="week-badge">Planned</span></h4>
                        <p><strong>Systems of Linear Equations:</strong> Linear combinations, augmented matrices, elementary row operations, and Gaussian elimination.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 11 -->
                <div class="week-card">
                    <div>
                        <h4>Week 11 <span class="week-badge">Planned</span></h4>
                        <p><strong>Row Echelon Form & Solution Spaces:</strong> Reduced row echelon form (RREF), rank, pivot columns, and parameterizing free variables.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>

                <!-- Week 12 -->
                <div class="week-card">
                    <div>
                        <h4>Week 12 <span class="week-badge">Planned</span></h4>
                        <p><strong>System Classification & Matrix Algebra:</strong> Uniquely determined, underdetermined, and overdetermined systems, homogeneous solutions, and matrix inverses.</p>
                    </div>
                    <a href="#" class="module-link disabled">Drafting</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""
    with open('index.html', 'w') as f:
        f.write(updated_content)

def execute_git_sync():
    commit_message = (
        "Restore full 12-week course scope and add hero banner to index.html\n\n"
        "Restructured index.html with the complete curriculum roadmap, integrated "
        "images/welcome-mth120.jpeg, and framed the content as personal study notes."
    )

    commands = [
        ['git', 'add', 'update.py', 'index.html'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]

    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == "__main__":
    print("Writing updated index.html with full 12-week layout...")
    update_curriculum_index()
    print("Committing and pushing to GitHub...")
    execute_git_sync()
    print("Deployment complete.")
