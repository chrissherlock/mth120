#!/usr/bin/env python3
import json
import os
import subprocess

# 1. Define the Stepper HTML Template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MTHS120 Interactive Stepper: Week 1 Lecture 3</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

    <style>
        :root {
            --bg: #f8fafc; --text: #0f172a; --card: #ffffff; --border: #cbd5e1;
            --accent: #d97706; --accent-hover: #b45309; --accent-light: #fef3c7;
            --success: #10b981; --success-bg: #d1fae5;
            --danger: #ef4444; --danger-bg: #fee2e2;
            --info: #3b82f6; --info-bg: #dbeafe;
            --font-ui: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }

        body { font-family: var(--font-ui); background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 900px; margin: 0 auto; }

        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
        .back-link { background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; transition: background 0.2s; white-space: nowrap; }
        .back-link:hover { background: #e2e8f0; color: #0f172a; }

        .telemetry-bar { background: var(--card); border: 1px solid var(--border); padding: 1rem; border-radius: 8px; display: flex; gap: 1.5rem; margin-bottom: 2rem; font-size: 0.9rem; font-family: monospace; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
        .tel-stat { display: flex; flex-direction: column; }
        .tel-label { color: #64748b; font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.75rem; }
        .tel-val { font-weight: bold; color: var(--accent); font-size: 1.1rem; }

        .stage-container { background: var(--card); border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 8px; padding: 2rem; margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
        .scenario-title { font-size: 1.25rem; font-weight: bold; color: #1e293b; margin-top: 0; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.75rem; }
        .scenario-context { font-size: 1.05rem; color: #334155; margin-bottom: 1.5rem; }

        .options-grid { display: grid; gap: 0.75rem; margin-bottom: 1.5rem; }
        .option-btn { background: #f1f5f9; border: 1px solid var(--border); border-radius: 6px; padding: 1rem 1.25rem; text-align: left; font-size: 1rem; cursor: pointer; transition: all 0.2s; font-family: var(--font-ui); color: var(--text); }
        .option-btn:hover { background: var(--accent-light); border-color: var(--accent); }
        .option-btn.selected { background: var(--accent-light); border-color: var(--accent); box-shadow: 0 0 0 2px var(--accent); }
        .option-btn.correct { background: var(--success-bg); border-color: var(--success); color: #065f46; }
        .option-btn.wrong { background: var(--danger-bg); border-color: var(--danger); color: #991b1b; }

        .analysis-container { display: none; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 2rem; border-top: 2px dashed #e2e8f0; padding-top: 1.5rem; animation: fadeIn 0.4s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .pane { padding: 1.25rem; border-radius: 6px; border: 1px solid; }
        .pane-what { background: #f0fdf4; border-color: #bbf7d0; border-left: 4px solid var(--success); }
        .pane-why { background: #eff6ff; border-color: #bfdbfe; border-left: 4px solid var(--info); }
        .pane h4 { margin: 0 0 0.75rem 0; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.05em; }
        .pane-what h4 { color: #047857; }
        .pane-why h4 { color: #1d4ed8; }
        .pane p { margin: 0; font-size: 0.95rem; line-height: 1.5; color: #334155; }

        .stepper-controls { display: flex; justify-content: space-between; align-items: center; margin-top: 1.5rem; }
        .action-btn { background: var(--accent); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 6px; font-weight: bold; font-size: 1rem; cursor: pointer; transition: background 0.2s; }
        .action-btn:hover { background: var(--accent-hover); }
        .action-btn:disabled { background: #cbd5e1; cursor: not-allowed; }
        .nav-btn { background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.75rem 1.25rem; border-radius: 6px; font-weight: bold; cursor: pointer; }
        .nav-btn:hover:not(:disabled) { background: #e2e8f0; }
        .nav-btn:disabled { opacity: 0.5; cursor: not-allowed; }

        @media (max-width: 640px) {
            .analysis-container { grid-template-columns: 1fr; }
            .telemetry-bar { flex-wrap: wrap; }
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <div>
            <h1 style="margin:0; font-size:1.75rem; color:#0f172a;">MTHS120 Interactive Stepper</h1>
            <p style="margin:0.25rem 0 0 0; color:#475569;">Week 1 Lecture 3: Sequences and Discrete Calculus</p>
        </div>
        <div>
            <a href="week1-lecture3.html" class="back-link">&larr; Back to Lecture 3</a>
        </div>
    </div>

    <div class="telemetry-bar">
        <div class="tel-stat">
            <span class="tel-label">Active Phase</span>
            <span class="tel-val" id="tel-phase">1 / 5</span>
        </div>
        <div class="tel-stat">
            <span class="tel-label">Current Mode</span>
            <span class="tel-val" id="tel-mode">Awaiting Input</span>
        </div>
        <div class="tel-stat">
            <span class="tel-label">Score</span>
            <span class="tel-val" id="tel-score">0</span>
        </div>
    </div>

    <div class="stage-container">
        <h2 class="scenario-title" id="stage-title">Loading...</h2>
        <div class="scenario-context" id="stage-context"></div>

        <div class="options-grid" id="options-container"></div>

        <div class="analysis-container" id="analysis-panes">
            <div class="pane pane-what">
                <h4>What Is Happening</h4>
                <p id="text-what"></p>
            </div>
            <div class="pane pane-why">
                <h4>Why The System Does This</h4>
                <p id="text-why"></p>
            </div>
        </div>

        <div class="stepper-controls">
            <button class="nav-btn" id="btn-prev" onclick="stepPrevious()" disabled>Prev</button>
            <button class="action-btn" id="btn-submit" onclick="evaluateSelection()">Submit Verification</button>
            <button class="nav-btn" id="btn-next" onclick="stepNext()" style="display:none;">Next Step ➔</button>
        </div>
    </div>
</div>

<script>
    const courseData = {course_data_json};

    let currentIndex = 0;
    let selectedOption = null;
    let phaseScore = 0;
    let hasAnsweredCurrent = false;

    const elTitle = document.getElementById("stage-title");
    const elContext = document.getElementById("stage-context");
    const elOptions = document.getElementById("options-container");
    const elPanes = document.getElementById("analysis-panes");
    const elWhat = document.getElementById("text-what");
    const elWhy = document.getElementById("text-why");
    const elBtnSubmit = document.getElementById("btn-submit");
    const elBtnNext = document.getElementById("btn-next");
    const elBtnPrev = document.getElementById("btn-prev");

    const telPhase = document.getElementById("tel-phase");
    const telMode = document.getElementById("tel-mode");
    const telScore = document.getElementById("tel-score");

    function renderMath() {
        if (typeof renderMathInElement !== 'undefined') {
            renderMathInElement(document.body, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false}
                ],
                throwOnError: false
            });
        }
    }

    function buildStep() {
        const data = courseData[currentIndex];

        elTitle.innerHTML = data.title;
        elContext.innerHTML = data.context;

        elOptions.innerHTML = "";
        data.options.forEach((opt, idx) => {
            const btn = document.createElement("button");
            btn.className = "option-btn";
            btn.innerHTML = opt;
            btn.onclick = () => selectOption(idx, btn);
            elOptions.appendChild(btn);
        });

        elPanes.style.display = "none";
        elBtnSubmit.style.display = "block";
        elBtnNext.style.display = "none";
        elBtnSubmit.disabled = true;

        selectedOption = null;
        hasAnsweredCurrent = false;

        telPhase.innerText = `${currentIndex + 1} / ${courseData.length}`;
        telMode.innerText = "Awaiting Input";
        telMode.style.color = "var(--text)";

        elBtnPrev.disabled = currentIndex === 0;

        renderMath();
    }

    function selectOption(idx, btnNode) {
        if (hasAnsweredCurrent) return;

        const buttons = elOptions.querySelectorAll(".option-btn");
        buttons.forEach(b => b.classList.remove("selected"));

        btnNode.classList.add("selected");
        selectedOption = idx;
        elBtnSubmit.disabled = false;
    }

    function evaluateSelection() {
        if (selectedOption === null || hasAnsweredCurrent) return;

        const data = courseData[currentIndex];
        const buttons = elOptions.querySelectorAll(".option-btn");

        hasAnsweredCurrent = true;
        elBtnSubmit.style.display = "none";
        elBtnNext.style.display = "block";
        elBtnNext.innerText = currentIndex === courseData.length - 1 ? "Complete Verification" : "Next Step ➔";

        if (selectedOption === data.correct) {
            buttons[selectedOption].classList.add("correct");
            phaseScore++;
            telScore.innerText = phaseScore;
            telMode.innerText = "Verified Valid";
            telMode.style.color = "var(--success)";
        } else {
            buttons[selectedOption].classList.add("wrong");
            buttons[data.correct].classList.add("correct");
            telMode.innerText = "Structural Error";
            telMode.style.color = "var(--danger)";
        }

        elWhat.innerHTML = data.what;
        elWhy.innerHTML = data.why;
        elPanes.style.display = "grid";

        renderMath();
    }

    function stepNext() {
        if (currentIndex < courseData.length - 1) {
            currentIndex++;
            buildStep();
        } else {
            elTitle.innerHTML = "System Verified: Diagnostics Complete";
            elContext.innerHTML = `<strong>Final Diagnostic Score: ${phaseScore} / ${courseData.length}</strong><br><br>You have successfully analyzed discrete sequences. From distinguishing monotonic profiles to reversing discrete step derivatives with telescoping sums, your foundation for formal convergence in Week 2 is fully assembled.`;
            elOptions.innerHTML = "";
            elPanes.style.display = "none";
            elBtnNext.style.display = "none";
            elBtnPrev.style.display = "none";

            telMode.innerText = "Simulation Ended";
            telMode.style.color = "var(--info)";
        }
    }

    function stepPrevious() {
        if (currentIndex > 0) {
            currentIndex--;
            buildStep();
        }
    }

    window.addEventListener('DOMContentLoaded', () => {
        buildStep();
    });
</script>

</body>
</html>"""

# 2. Define the Lecture 3 Course Data
course_data = [
    {
        "title": "Phase 1: Diagnosing Monotonicity",
        "context": "<strong>Scenario:</strong> You are evaluating a system state sequence represented by $a_n = \\frac{1}{n^2}$ for $n \\ge 1$. Which algebraic condition correctly proves this sequence is strictly decreasing?",
        "options": [
            "$$a_{n+1} - a_n = \\frac{1}{(n+1)^2} - \\frac{1}{n^2} < 0$$ for all $n \\ge 1$",
            "$$\\frac{a_{n+1}}{a_n} = \\frac{n^2}{(n+1)^2} > 1$$ for all $n \\ge 1$",
            "$$a_{n+1} - a_n = \\frac{1}{n+1} - \\frac{1}{n} \\le 0$$ for all $n \\ge 1$",
            "By checking the first three terms: $1 > \\frac{1}{4} > \\frac{1}{9}$"
        ],
        "correct": 0,
        "what": "The Difference Test demands we evaluate $a_{n+1} - a_n$. Since $(n+1)^2 > n^2$ for $n \\ge 1$, the fraction $\\frac{1}{(n+1)^2}$ is strictly smaller than $\\frac{1}{n^2}$, forcing their difference to be strictly negative.",
        "why": "A sequence is strictly decreasing if and only if every forward step results in a net drop (a negative derived difference). The finite observation trap (checking only the first few terms) is never a rigorous proof in analysis."
    },
    {
        "title": "Phase 2: Pointwise Algebra and Oscillations",
        "context": "<strong>Scenario:</strong> The sequence $c_n$ is formed by adding an arithmetic climb to a negative oscillation: $c_n = 2n + (-1)^n$. What is the behavior of the derived sequence $c_n'$?",
        "options": [
            "It remains constant at $c_n' = 2$.",
            "It alternates signs continuously, causing $c_n$ to lose all monotonic properties.",
            "It evaluates to $0$ on even steps and $+4$ on odd steps, proving $c_n$ is weakly increasing with flat plateaus.",
            "It evaluates to $-2$ everywhere, proving $c_n$ is strictly decreasing."
        ],
        "correct": 2,
        "what": "The derived difference of the linear term $2n$ is constantly $+2$. The derived difference of $(-1)^n$ alternates between $+2$ and $-2$. Adding them pointwise gives a derived sequence that hits $0$ then jumps to $+4$.",
        "why": "Pointwise addition of a constant difference and an alternating difference creates a periodic wave of differences. When the oscillation perfectly cancels the linear climb ($2 - 2 = 0$), the sequence hits a flat plateau, making it weakly (not strictly) increasing."
    },
    {
        "title": "Phase 3: The Discrete Derivative",
        "context": "<strong>Scenario:</strong> You need to compute the derived sequence $a_n' = a_{n+1} - a_n$ for the geometric progression $a_n = 5 \\cdot (3)^n$. What is the resulting sequence?",
        "options": [
            "$$a_n' = 15 \\cdot (3)^{n-1}$$",
            "$$a_n' = 10 \\cdot (3)^n$$",
            "$$a_n' = 5 \\cdot (2)^n$$",
            "$$a_n' = 5 \\cdot (3)^n$$"
        ],
        "correct": 1,
        "what": "Substitute into the definition: $a_n' = 5 \\cdot 3^{n+1} - 5 \\cdot 3^n = 5 \\cdot 3^n(3 - 1) = 5 \\cdot 3^n(2) = 10 \\cdot 3^n$.",
        "why": "The derived sequence of a geometric progression $aq^n$ is another geometric progression $a(q-1)q^n$. The scaling factor $(q-1)$ emerges naturally from factoring out the common ratio."
    },
    {
        "title": "Phase 4: Telescoping Sums",
        "context": "<strong>Scenario:</strong> You are evaluating the sum of the derived sequence $\\sum_{k=0}^{n-1} a_k'$ where $a_k = \\frac{1}{k+1}$. According to the Discrete Fundamental Theorem of Calculus (Telescoping Identity), what does this sum collapse to?",
        "options": [
            "$$\\frac{1}{n+1} - 1$$",
            "$$\\frac{1}{n+1}$$",
            "$$1 - \\frac{1}{n+1}$$",
            "$$0$$"
        ],
        "correct": 0,
        "what": "The Telescoping Identity states that $\\sum_{k=0}^{n-1} a_k' = a_n - a_0$. Substituting the terms gives $a_n = \\frac{1}{n+1}$ and $a_0 = \\frac{1}{1} = 1$. The result is strictly $\\frac{1}{n+1} - 1$.",
        "why": "A sum of consecutive differences always collapses inward, canceling every intermediate locker state. Only the final destination boundary ($a_n$) and the initial starting boundary ($-a_0$) survive the accumulation."
    },
    {
        "title": "Phase 5: Boundedness vs. Limits",
        "context": "<strong>Scenario:</strong> An analysis engine evaluates the alternating sequence $d_n = (-1)^n$. It logs that the sequence is strictly bounded. Does this guarantee the sequence has a convergent limit?",
        "options": [
            "Yes. The Axiom of Completeness guarantees bounded sequences always converge to their supremum.",
            "No. Boundedness only guarantees the sequence is trapped within a horizontal corridor (e.g., between -1 and 1), but it may oscillate forever without settling on a single destination.",
            "Yes, because the bounds $-1$ and $1$ eventually cancel each other out to zero.",
            "No, because the sequence is not bounded; it oscillates infinitely."
        ],
        "correct": 1,
        "what": "The sequence is bounded because $|d_n| \\le 1$ for all $n$. However, it diverges by oscillation, never approaching a single numerical limit.",
        "why": "Boundedness is a geometric fence; convergence is a destination. While convergence requires boundedness, boundedness alone does not guarantee convergence. A sequence can bounce infinitely between walls without ever coming to rest."
    }
]

# 3. Write the Stepper HTML File
final_stepper_html = html_template.replace("{course_data_json}", json.dumps(course_data, indent=4))
stepper_filename = "week1-lecture3-interactive-stepper.html"

with open(stepper_filename, "w", encoding="utf-8") as f:
    f.write(final_stepper_html)
print(f"Created: {stepper_filename}")

# 4. Patch week1-lecture3.html
lecture_filename = "week1-lecture3.html"

# HTML Snippets for Injection
nav_target = '<a href="week2-lecture4.html" style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">Lecture 4 &rarr;</a>'

nav_replacement = """<a href="week1-lecture3-interactive-stepper.html" style="background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;">✎ Practice Problems</a>
                """ + nav_target

cta_target = "<!-- FOOTER NAVIGATION -->"

cta_replacement = """<!-- INTERACTIVE STEPPER CTA -->
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 5px solid #10b981; padding: 1.75rem; margin-bottom: 2.5rem; border-radius: 6px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <h4 style="margin: 0 0 0.75rem 0; color: #047857; font-size: 1.15rem;">Ready to test your understanding?</h4>
                <p style="margin: 0 0 1.25rem 0; color: #334155; font-size: 1.02rem;">Work through the progressive interactive problems to lock in these foundational concepts before moving on to Week 2.</p>
                <a href="week1-lecture3-interactive-stepper.html" style="display: inline-block; background: #10b981; color: white; padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 1rem; transition: background 0.2s;">
                    Launch Interactive Problem Stepper ➔
                </a>
            </div>

            <!-- FOOTER NAVIGATION -->"""

if os.path.exists(lecture_filename):
    with open(lecture_filename, "r", encoding="utf-8") as f:
        lecture_html = f.read()

    # Idempotency check: Only patch if the links don't already exist
    if "week1-lecture3-interactive-stepper.html" not in lecture_html:
        # Inject Nav Link
        lecture_html = lecture_html.replace(nav_target, nav_replacement)

        # Inject CTA
        lecture_html = lecture_html.replace(cta_target, cta_replacement)

        with open(lecture_filename, "w", encoding="utf-8") as f:
            f.write(lecture_html)
        print(f"Patched: {lecture_filename} (Navigation and CTA injected)")
    else:
        print(f"Skipped: {lecture_filename} (Already contains the practice problem links)")
else:
    print(f"Error: {lecture_filename} not found in the current directory.")

# 5. Execute Git Commands Automatically
print("\\nExecuting Git commands...")
try:
    subprocess.run(["git", "add", "update.py", "week1-lecture3-interactive-stepper.html", "week1-lecture3.html"], check=True)
    subprocess.run(["git", "commit", "-m", "Add interactive stepper to Week 1 Lecture 3\\n\\nGenerate week1-lecture3-interactive-stepper.html and automatically patch week1-lecture3.html to include navigational and call-to-action links to the newly generated problems."], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Git operations completed successfully.")
except Exception as e:
    print(f"Git operations failed. Please run them manually. Error: {e}")
