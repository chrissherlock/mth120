#!/usr/bin/env python3
import os
import subprocess

def streamline_composition_section():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_section_3_3 = r'''            <!-- SUBSECTION 3.3: COMPOSITION AND INVERTIBILITY -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">3.3 Composition and Invertibility</h3>
                    <span style="font-weight: 700; color: var(--accent); font-size: 0.92rem;">Pipelines &amp; Reverse Paths</span>
                </div>

                <h4 style="margin: 0 0 0.5rem 0; color: #0f172a; font-size: 1.02rem;">1. Composition ($g \circ f$): Chaining Actions in Series</h4>
                <p style="margin: 0 0 0.75rem 0; color: #334155; line-height: 1.65;">
                    Composition connects two functions like links in a pipeline: the output of the first function feeds directly as the input into the second. If $f: X \to Y$ and $g: Y \to Z$, their composite $g \circ f: X \to Z$ creates a single direct leap from $X$ to $Z$:
                </p>
                <div class="definition-box" style="margin: 0.75rem 0;">
                    $$(g \circ f)(x) = g(f(x))$$
                </div>
                <p style="color: #334155; line-height: 1.65; margin-bottom: 1.25rem;">
                    <strong>Read from right to left:</strong> Although $g$ is written on the left, $f$ acts on $x$ first. Think of $(g \circ f)(x)$ as saying: <em>"evaluate $f(x)$ first, then pass that output into $g$."</em>
                </p>

                <h4 style="margin: 1.25rem 0 0.5rem 0; color: #0f172a; font-size: 1.02rem; border-top: 1px solid #f1f5f9; padding-top: 1rem;">2. Inverses ($f^{-1}$): The "Undo" Operation</h4>
                <p style="margin: 0 0 0.75rem 0; color: #334155; line-height: 1.65;">
                    An <strong>inverse function</strong> $f^{-1}: Y \to X$ simply undoes what $f$ did. Composing a function with its inverse brings you right back to your starting point:
                </p>
                <div style="text-align: center; margin: 0.75rem 0; font-size: 1.05rem;">
                    $$(f^{-1} \circ f)(x) = x \quad \text{and} \quad (f \circ f^{-1})(y) = y$$
                </div>
                <p style="color: #334155; line-height: 1.65; margin-bottom: 0.5rem;">
                    Why must a function be <strong>bijective</strong> to have an inverse? It comes down to what happens when you try to walk the arrows backward:
                </p>
                <ul style="margin: 0.25rem 0 0.75rem 1.25rem; padding: 0; color: #334155; font-size: 0.95rem; line-height: 1.65;">
                    <li><strong>Must be Injective (No Ambiguity):</strong> If two inputs merged to the same output, walking backward leaves you at a fork with no unique answer for where you came from.</li>
                    <li><strong>Must be Surjective (No Dead Ends):</strong> If an element in $Y$ was never hit by an arrow, the reverse path is undefined for that point.</li>
                </ul>
                <div class="definition-box" style="margin-top: 0.75rem; margin-bottom: 0;">
                    <strong>Core Takeaway:</strong> A mapping $f: X \to Y$ has a two-sided inverse $f^{-1}: Y \to X$ <strong>if and only if</strong> it is bijective.
                </div>
            </div>'''

    start_delim = '<!-- SUBSECTION 3.3: INVERTIBILITY AND COMPOSITION -->'
    if start_delim not in content:
        start_delim = '<!-- SUBSECTION 3.3: COMPOSITION AND INVERTIBILITY -->'
    end_delim = '<!-- SECTION 4 -->'

    start_idx = content.find(start_delim)
    end_idx = content.find(end_delim)

    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + new_section_3_3 + '\n\n            ' + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully streamlined Section 3.3 in week1-lecture1.html.")
    else:
        print("Could not locate boundaries for Section 3.3 in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Streamline composition and invertibility to clarify conceptual flow\n\n"
        "Reordered Section 3.3 in week1-lecture1.html so function composition is\n"
        "introduced before invertibility. Clarified the right-to-left evaluation\n"
        "order of composite functions and simplified the rationale for why\n"
        "bijectivity is required to reverse a mapping without ambiguity."
    )
    commands = [
        ['git', 'add', 'week1-lecture1.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    streamline_composition_section()
    synchronize_git_changes()
