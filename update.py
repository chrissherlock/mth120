#!/usr/bin/env python3
import os
import re
import subprocess

def strip_software_analogy():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the toggle-group HTML from the controls pane
    toggle_html_pattern = r'\s*<div class="toggle-group">[\s\S]*?</div>\s*(?=\n\s*</div>\s*\n\s*<div class="analysis-panes">)'
    content = re.sub(toggle_html_pattern, '\n', content)

    # 2. Replace the formulaClauses array and UI logic in the script block
    old_script_pattern = r'const formulaState = \{ step: 0, perspective: \'adversarial\' \};[\s\S]*?function updateFormulaCanvas\(step\)'

    new_script_block = r'''const formulaState = { step: 0 };
        const formulaClauses = [
            {
                clauseTitle: "1. The Challenge (∀ϵ > 0)", quantifier: "Universal (∀)", role: "Given tolerance", scope: "Arbitrary positive real",
                summary: "<strong>Step 1: Establishing tolerance.</strong> Consider any arbitrary positive distance $\\epsilon > 0$.",
                what: "<p>We are given an arbitrary positive distance $\\epsilon > 0$, forming a symmetric neighborhood $(L - \\epsilon, L + \\epsilon)$ around the target limit $L$.</p>",
                why: "<p>Demanding the condition holds for every $\\epsilon > 0$ ensures the sequence cannot settle at or bounce toward any other value.</p>"
            },
            {
                clauseTitle: "2. The Response (∃N ∈ ℕ)", quantifier: "Existential (∃)", role: "Cutoff index", scope: "Dependent on ϵ",
                summary: "<strong>Step 2: Identifying cutoff index N.</strong> An integer $N$ exists past which terms remain trapped.",
                what: "<p>We determine an integer index $N$ based on $\\epsilon$. For example, with $a_n = 1/n$, choosing $N = \\lceil 1/\\epsilon \\rceil$ ensures $1/N \\le \\epsilon$.</p>",
                why: "<p>Because $N$ is chosen after $\\epsilon$, it can push as far out down the sequence tail as necessary to satisfy tiny tolerances.</p>"
            },
            {
                clauseTitle: "3. The Tail Scope (∀n > N)", quantifier: "Universal (∀)", role: "Tail evaluation", scope: "All indices past N",
                summary: "<strong>Step 3: Examining all terms past N.</strong> Every subsequent index $n > N$ is evaluated.",
                what: "<p>We evaluate the infinite tail: all terms $a_n$ where $n \\in \\{N+1, N+2, N+3, \\dots\\}$.</p>",
                why: "<p>Convergence is strictly a long-term asymptotic property. A sequence may fluctuate wildy for early terms, provided the tail stays bounded.</p>"
            },
            {
                clauseTitle: "4. The Distance Condition (|aₙ - L| < ϵ)", quantifier: "Inequality (<)", role: "Proximity condition", scope: "Distance within band",
                summary: "<strong>Step 4: Confirming distance constraint.</strong> For all $n > N$, $\vert{}a_n - L\vert{} < \\epsilon$.",
                what: "<p>Every term $a_n$ with index $n > N$ lies strictly inside the open interval $(L - \\epsilon, L + \\epsilon)$.</p>",
                why: "<p>This guarantees that the entire infinite tail stays trapped within the tolerance window without ever escaping.</p>"
            }
        ];

        function setFormulaStep(stepIdx) { formulaState.step = stepIdx; updateFormulaUI(); }
        function stepFormula(dir) {
            formulaState.step += dir;
            if (formulaState.step < 0) formulaState.step = 0;
            if (formulaState.step > 3) formulaState.step = 3;
            updateFormulaUI();
        }
        function updateFormulaUI() {
            const idx = formulaState.step;
            const current = formulaClauses[idx];
            for (let i = 0; i < 4; i++) {
                const el = document.getElementById(`chunk-${i}`);
                el.classList.remove('active', 'completed');
                if (i === idx) el.classList.add('active');
                else if (i < idx) el.classList.add('completed');
            }
            document.getElementById('fw-tel-clause').innerText = current.clauseTitle;
            document.getElementById('fw-tel-quant').innerText = current.quantifier;
            document.getElementById('fw-tel-role').innerText = current.role;
            document.getElementById('fw-tel-scope').innerText = current.scope;
            document.getElementById('btn-fw-prev').disabled = (idx === 0);
            document.getElementById('btn-fw-next').disabled = (idx === 3);
            document.getElementById('fw-heading-what').innerText = "Mathematical Mechanics";
            document.getElementById('fw-heading-why').innerText = "Logical Rationale";
            document.getElementById('fw-step-summary').innerHTML = current.summary;
            document.getElementById('fw-pane-what').innerHTML = current.what;
            document.getElementById('fw-pane-why').innerHTML = current.why;
            if (window.renderMathInElement) {
                renderMathInElement(document.getElementById('definition-walkthrough'), { delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}] });
            }
            updateFormulaCanvas(idx);
        }
        function updateFormulaCanvas(step)'''

    if re.search(old_script_pattern, content):
        content = re.sub(old_script_pattern, new_script_block, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully removed software specification analogy from week2.html.")
    else:
        print("Could not locate script section to update in week2.html.")

def execute_git_sync():
    commit_message = (
        "Remove software specification analogy from definition stepper\n\n"
        "Removed the software specification perspective and toggle dropdown from\n"
        "the epsilon-N clause stepper in week2.html, focusing the telemetry,\n"
        "summary, and analytical panes strictly on mathematical mechanics."
    )
    commands = [
        ['git', 'add', 'week2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    strip_software_analogy()
    execute_git_sync()
