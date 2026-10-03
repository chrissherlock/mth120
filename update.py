#!/usr/bin/env python3
import os
import subprocess

def add_infinity_diagram_explanation():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The SVG visualization block as it currently exists
    svg_block = r'''            <!-- EMBEDDED SVG DIAGRAM FOR INFINITY LIMIT -->
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem; margin-top: 1.5rem; margin-bottom: 1.5rem;">
                <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.75rem; text-align: center;">VISUALIZATION: The $M\text{-}N$ Threshold Test for $\lim_{n\to\infty} \sqrt{n} = \infty$</p>
                <svg viewBox="0 0 800 300" style="width: 100%; height: auto; display: block;">
                    <!-- Grid Lines -->
                    <line x1="80" y1="240" x2="760" y2="240" stroke="#e2e8f0" stroke-width="1"/>
                    <line x1="80" y1="180" x2="760" y2="180" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3"/>
                    <line x1="80" y1="120" x2="760" y2="120" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3"/>
                    <line x1="80" y1="60" x2="760" y2="60" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3"/>

                    <!-- Axes -->
                    <line x1="80" y1="240" x2="760" y2="240" stroke="#0f172a" stroke-width="2"/>
                    <line x1="80" y1="20" x2="80" y2="260" stroke="#0f172a" stroke-width="2"/>
                    <text x="710" y="260" font-size="11" font-weight="bold" fill="#64748b">Index n</text>
                    <text x="40" y="30" font-size="11" font-weight="bold" fill="#64748b">a_n</text>

                    <!-- Massive Threshold Line M -->
                    <line x1="80" y1="120" x2="760" y2="120" stroke="#ef4444" stroke-width="2" stroke-dasharray="6"/>
                    <text x="95" y="112" font-size="12" font-weight="bold" fill="#ef4444">Threshold Level M</text>

                    <!-- Cutoff Line N -->
                    <line x1="500" y1="30" x2="500" y2="260" stroke="#d97706" stroke-width="2.5" stroke-dasharray="4"/>
                    <text x="510" y="48" font-size="12" font-weight="bold" fill="#b45309">Cutoff Index N</text>

                    <!-- Shaded Region Above Threshold Past N -->
                    <rect x="500" y="35" width="240" height="85" fill="#fef3c7" opacity="0.5" rx="4"/>
                    <text x="525" y="75" font-size="11" font-weight="bold" fill="#92400e">Region where $a_n > M$</text>
                    <text x="525" y="92" font-size="10" font-weight="600" fill="#b45309">Guaranteed for all $n > N$</text>

                    <!-- Sequence Data Points (Discrete Dots for sqrt(n)) -->
                    <g>
                        <circle cx="100" cy="225" r="4" fill="#0284c7"/><circle cx="125" cy="215" r="4" fill="#0284c7"/>
                        <circle cx="150" cy="207" r="4" fill="#0284c7"/><circle cx="175" cy="200" r="4" fill="#0284c7"/>
                        <circle cx="200" cy="193" r="4" fill="#0284c7"/><circle cx="225" cy="186" r="4" fill="#0284c7"/>
                        <circle cx="250" cy="180" r="4" fill="#0284c7"/><circle cx="275" cy="174" r="4" fill="#0284c7"/>
                        <circle cx="300" cy="168" r="4" fill="#0284c7"/><circle cx="325" cy="162" r="4" fill="#0284c7"/>
                        <circle cx="350" cy="157" r="4" fill="#0284c7"/><circle cx="375" cy="151" r="4" fill="#0284c7"/>
                        <circle cx="400" cy="146" r="4" fill="#0284c7"/><circle cx="425" cy="141" r="4" fill="#0284c7"/>
                        <circle cx="450" cy="136" r="4" fill="#0284c7"/><circle cx="475" cy="131" r="4" fill="#0284c7"/>
                        <!-- Past Cutoff N (Highlighted Green/Teal) -->
                        <circle cx="500" cy="126" r="5.5" fill="#10b981"/><circle cx="525" cy="116" r="5.5" fill="#10b981"/>
                        <circle cx="550" cy="107" r="5.5" fill="#10b981"/><circle cx="575" cy="98" r="5.5" fill="#10b981"/>
                        <circle cx="600" cy="89" r="5.5" fill="#10b981"/><circle cx="625" cy="80" r="5.5" fill="#10b981"/>
                        <circle cx="650" cy="71" r="5.5" fill="#10b981"/><circle cx="675" cy="62" r="5.5" fill="#10b981"/>
                        <circle cx="700" cy="53" r="5.5" fill="#10b981"/>
                    </g>
                    <text x="95" y="258" font-size="10" fill="#64748b">n=1</text>
                    <text x="492" y="275" font-size="10" font-weight="bold" fill="#d97706">N</text>
                    <text x="690" y="258" font-size="10" fill="#64748b">n increases</text>
                </svg>
            </div>'''

    # The explanatory caption block to append right below the SVG
    caption_block = r'''            <!-- EXPLANATION CAPTION UNDERNEATH VISUALIZATION -->
            <div class="aside-box" style="margin-top: 1rem; margin-bottom: 1.5rem;">
                <h4>📖 How to Read This Diagram</h4>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.3rem;"><strong>The Threshold Level ($M$):</strong> The dashed red line represents your opponent's arbitrary high demand $M$.</li>
                    <li style="margin-bottom: 0.3rem;"><strong>The Cutoff Index ($N$):</strong> The orange dashed line marks the boundary $N$. Everything to the left is initial transient behavior; everything to the right is the long-term tail.</li>
                    <li><strong>The Green Points ($a_n > M$):</strong> Notice how every single blue point eventually crosses above the red threshold at index $N$, turning green and staying safely in the yellow shaded zone forever.</li>
                </ol>
            </div>'''

    target = svg_block
    replacement = svg_block + '\n\n' + caption_block

    if target in content and 'How to Read This Diagram' not in content:
        content = content.replace(target, replacement, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added explanation caption beneath SVG visualization in week2.html.")
    else:
        print("SVG block not found or caption already present.")

def execute_git_sync():
    commit_message = (
        "Add explanatory caption beneath M-N threshold visualization in week2.html\n\n"
        "Inserted a scannable breakdown explaining the threshold level M, cutoff index N,\n"
        "and permanent tail property for Section 4 in week2.html."
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
    add_infinity_diagram_explanation()
    execute_git_sync()
