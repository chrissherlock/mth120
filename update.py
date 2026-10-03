#!/usr/bin/env python3
import os
import re
import subprocess

def enlarge_archery_svg():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<div class="aside-box"[^>]*>\s*<h4>\s*💡 Plain-English Breakdown: What is this formula actually saying\?</h4>)([\s\S]*?)(</div>\s*</div>)'

    enlarged_svg_layout = r'''
                <div style="margin-top: 0.75rem; display: flex; align-items: center; gap: 2rem; flex-wrap: nowrap;">
                    <!-- LEFT COLUMN: Larger SVG Graphic -->
                    <div style="flex: 0 0 240px; background: #ffffff; border: 1px solid #fde68a; border-radius: 8px; padding: 1rem; box-sizing: border-box; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                        <svg viewBox="0 0 220 140" style="width: 100%; height: auto; display: block;">
                            <!-- Target Board Outer Ring -->
                            <circle cx="110" cy="70" r="55" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
                            <!-- Epsilon Tolerance Band -->
                            <circle cx="110" cy="70" r="38" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
                            <text x="110" y="42" font-family="sans-serif" font-size="9" font-weight="bold" fill="#d97706" text-anchor="middle">±ε Tolerance</text>
                            <!-- Bullseye (Limit L) -->
                            <circle cx="110" cy="70" r="18" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
                            <circle cx="110" cy="70" r="6" fill="#ef4444"/>
                            <text x="110" y="66" font-family="sans-serif" font-size="8" font-weight="bold" fill="#991b1b" text-anchor="middle">L</text>

                            <!-- Arrow Shaft & Feathers (Diagonal Accent) -->
                            <line x1="30" y1="20" x2="105" y2="65" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
                            <polygon points="105,65 95,60 100,55" fill="#0f172a"/>
                            <!-- Feather tail -->
                            <line x1="30" y1="20" x2="22" y2="15" stroke="#b45309" stroke-width="2"/>
                            <line x1="35" y1="25" x2="27" y2="20" stroke="#b45309" stroke-width="2"/>
                        </svg>
                    </div>
                    <!-- RIGHT COLUMN: Explanation Text -->
                    <div style="flex: 1; min-width: 0;">
                        <p style="margin-top: 0;">If looking at $\forall \epsilon > 0, \ \exists N \in \mathbb{N} \ \text{such that} \ \forall n > N, \ |a_n - L| < \epsilon$ makes your head spin, think of it as an <strong>archery challenge</strong> or a <strong>game between two players</strong>:</p>
                        <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                            <li style="margin-bottom: 0.4rem;"><strong>1. The Challenger sets tolerance ($\epsilon$):</strong> Your opponent hands you a tiny positive distance $\epsilon$, drawing a narrow target band around $L$.</li>
                            <li style="margin-bottom: 0.4rem;"><strong>2. You find a cutoff step ($N$):</strong> You determine how far down the list to walk—past index $N$—so everything settles inside the band.</li>
                            <li style="margin-bottom: 0.4rem;"><strong>3. The Tail Test ($|a_n - L| < \epsilon$):</strong> The absolute distance between $a_n$ and $L$ stays smaller than $\epsilon$ for <em>every step</em> past $N$.</li>
                        </ol>
                        <p style="margin-top: 0.5rem; margin-bottom: 0;">If you win no matter how small your opponent makes $\epsilon$, the sequence converges to $L$!</p>
                    </div>
                </div>'''

    def replacer(match):
        return match.group(1) + enlarged_svg_layout + match.group(3)

    new_content, count = re.subn(pattern, replacer, content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully enlarged archery SVG in week2.html.")
    else:
        print("Error: Plain-English Breakdown section pattern not matched.")

def execute_git_sync():
    commit_message = (
        "Enlarge archery target SVG graphic in week2.html\n\n"
        "Increased the width of the left-hand flex container and SVG viewbox\n"
        "to make the archery target illustration larger and more prominent."
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
    enlarge_archery_svg()
    execute_git_sync()
