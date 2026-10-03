#!/usr/bin/env python3
import os
import subprocess

def update_curriculum_index():
    if not os.path.exists('index.html'):
        print("index.html not found in current directory. Please run in root.")
        return

    # Unified Styling System (matches week1.html)
    updated_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MTHS120: Discrete Mathematics | UNE Curriculum Index</title>
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
            --font-ui: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
        body { font-family: var(--font-ui); background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 0; }
        .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }

        /* Unified Header/Header-Wrapper styling */
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; }
        .header h1 { color: #0f172a; font-family: var(--font-ui); margin-top: 0; }
        .header a { color: var(--accent); text-decoration: none; font-weight: 500; }
        .header a:hover { color: var(--accent-hover); text-decoration: underline; }

        /* Unified Card Styling */
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }
        .week-card { background: var(--card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border); margin-bottom: 1rem; }

        /* Welcoming Intro Lead (from week1.html) */
        .intro-lead { font-size: 1.1rem; color: #1e293b; line-height: 1.7; margin-bottom: 2rem; background: #f1f5f9; padding: 1.5rem; border-radius: 6px; border-left: 4px solid var(--accent); border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }

        /* Welcoming Feature Styling */
        .welcoming-feature {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-left: 5px solid var(--accent);
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2.5rem;
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 2rem;
            align-items: center;
        }
        .welcoming-feature h2 { color: #92400e; margin-top: 0; font-size: 1.75rem; }
        .welcoming-feature p { color: #b45309; margin-bottom: 0; }
        .welcome-image-wrapper {
            border: 1px solid #fed7aa;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        .welcome-image {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
        }

        /* Unified link styling */
        .module-link {
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 4px;
            font-weight: 600;
            margin-top: 1rem;
            text-decoration: none;
        }
        .module-link:hover {
            background: var(--accent-hover);
            text-decoration: none;
        }

        @media (max-width: 768px) {
            .welcoming-feature { grid-template-columns: 1fr; gap: 1rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Unified Top Header (back navigation for index) -->
        <div class="header">
            <h1>MTHS120 Curriculum Index</h1>
            <a href="https://une.edu.au" style="font-weight: 400;">&larr; Return to UNE Portal</a>
        </div>

        <div class="module-content">
            <!-- Welcoming Intro Lead -->
            <div class="intro-lead">
                Welcome to the official curriculum index for UNE MTHS120. This course bridges mathematical formalism with discrete computation, exploring the language, tools, and structures used to build our digital world. Navigate through our weekly modules using the links below.
            </div>

            <!-- New Welcoming Hero Feature (using welcome-mth120.jpeg) -->
            <div class="welcoming-feature">
                <div class="welcome-image-wrapper">
                    <img src="images/welcome-mth120.jpeg" alt="MTHS120 Welcoming Illustration" class="welcome-image">
                </div>
                <div>
                    <h2>Hello, Mathematicians!</h2>
                    <p>Mathematics isn't just about formulas; it's about seeing the fundamental structures that connect everything. In MTHS120, we learn to stare infinity in the eye, tame complexity, and map relationships across the algebraic plane.</p>
                </div>
            </div>

            <h3>Weekly Modules</h3>

            <!-- Week 1 (Active) -->
            <div class="week-card">
                <h4>Week 1: Sets, Numbers, and Sequences</h4>
                <p>Master the grammar of logic, explore algebraic closure, and construct the real line.</p>
                <a href="week1.html" class="module-link">View Module</a>
            </div>

            <!-- Week 2 (Placeholder) -->
            <div class="week-card" style="opacity: 0.65;">
                <h4>Week 2: Algebraic Structures</h4>
                <p>Dive deep into Groups, Rings, and Fields—the foundational building blocks of algebra.</p>
                <a href="#" class="module-link">Coming Soon...</a>
            </div>

            <!-- More weeks added as needed... -->

        </div>
    </div>
</body>
</html>
"""
    with open('index.html', 'w') as f:
        f.write(updated_content)

def execute_git_sync():
    commit_message = (
        "Integrate welcome hero image into index.html\n\n"
        "Created a dedicated .welcoming-feature grid component to display the "
        "images/welcome-mth120.jpeg illustration alongside a warm greeting."
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
    print("Updating index.html with welcoming image...")
    update_curriculum_index()
    print("Committing and pushing to GitHub...")
    execute_git_sync()
    print("Deployment complete.")
