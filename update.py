#!/usr/bin/env python3
import os
import subprocess

def update_infinity_svg():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_svg_block = r'''            <!-- EMBEDDED SVG DIAGRAM FOR INFINITY LIMIT -->
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem; margin-top: 1.5rem; margin-bottom: 1.5rem;">
                <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.75rem; text-align: center;">VISUALIZATION: The $M\text{-}N$ Threshold Test for $\lim_{n\to\infty} \sqrt{n} = \infty$</p>
                <svg viewBox="0 0 800 280" style="width: 100%; height: auto; display: block;">
                    <!-- Axes -->
                    <line x1="60" y1="220" x2="760" y2="220" stroke="#cbd5e1" stroke-width="2"/>
                    <line x1="60" y1="20" x2="60" y2="240" stroke="#cbd5e1" stroke-width="2"/>
                    <text x="710" y="235" font-size="11" font-weight="bold" fill="#64748b">n (index)</text>
                    <text x="20" y="35" font-size="11" font-weight="bold" fill="#64748b">Value</text>

                    <!-- Massive Threshold Line M -->
                    <line x1="60" y1="90" x2="760" y2="90" stroke="#ef4444" stroke-width="2" stroke-dasharray="6"/>
                    <text x="70" y="82" font-size="12" font-weight="bold" fill="#ef4444">Threshold M (e.g., 100)</text>

                    <!-- Cutoff Line N -->
                    <line x1="520" y1="20" x2="520" y2="240" stroke="#d97706" stroke-width="2" stroke-dasharray="4"/>
                    <text x="528" y="45" font-size="12" font-weight="bold" fill="#b45309">Cutoff Index N</text>

                    <!-- Sequence Curve an = sqrt(n) (scaled for view) -->
                    <path d="M 70,215 Q 200,180 350,140 T 520,95 T 750,50" fill="none" stroke="#0284c7" stroke-width="3"/>

                    <!-- Highlight Region Above Threshold Past N -->
                    <rect x="520" y="20" width="240" height="70" fill="#fef3c7" opacity="0.4"/>
                    <text x="580" y="60" font-size="11" font-weight="bold" fill="#92400e">All terms $a_n > M$ for $n > N$</text>
                </svg>
            </div>'''

    new_svg_block = r'''            <!-- EMBEDDED SVG DIAGRAM FOR INFINITY LIMIT -->
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

    if old_svg_block in content:
        content = content.replace(old_svg_block, new_svg_block)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated M-N threshold SVG visualization in week2.html.")
    else:
        print("Old SVG block not found.")

def execute_git_sync():
    commit_message = (
        "Update M-N threshold SVG visualization in week2.html\n\n"
        "Refined the SVG diagram for Section 4 with discrete sequence points,\n"
        "grid lines, and clearer threshold and cutoff index callouts."
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
    update_infinity_svg()
    execute_git_sync()
