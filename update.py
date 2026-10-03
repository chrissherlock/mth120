#!/usr/bin/env python3
import os
import subprocess

def align_archery_svg_left():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old block to replace
    old_block = r'''            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>💡 Plain-English Breakdown: What is this formula actually saying?</h4>
                <div style="display: flex; justify-content: center; margin: 1.25rem 0 0.5rem 0;">
                    <svg viewBox="0 0 220 140" style="max-width: 200px; height: auto;">
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
                <p>If looking at $\forall \epsilon > 0, \ \exists N \in \mathbb{N} \ \text{such that} \ \forall n > N, \ |a_n - L| < \epsilon$ makes your head spin, think of it as an <strong>archery challenge</strong> or a <strong>game between two players</strong>:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.5rem;"><strong>1. The Challenger sets a tiny tolerance ($\epsilon$):</strong> Your opponent hands you a tiny positive distance $\epsilon$ (like $0.01$). They draw a narrow target band around the limit $L$: from $L - \epsilon$ up to $L + \epsilon$. They are daring you to find a point where the sequence stays inside forever.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>2. You find a cutoff step ($N$):</strong> You look at the sequence and figure out how far down the list you need to walk—past some index $N$—so that everything after it settles down inside the target band.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>3. The Tail Test ($|a_n - L| < \epsilon$):</strong> The absolute distance between your sequence term $a_n$ and the limit $L$ is smaller than your opponent's tolerance $\epsilon$ for <em>every single step</em> past $N$.</li>
                </ol>
                <p style="margin-top: 0.75rem; margin-bottom: 0;">If you can successfully win this game no matter how ridiculously small your opponent makes $\epsilon$, then the sequence truly converges to $L$!</p>
            </div>'''

    new_block = r'''            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>💡 Plain-English Breakdown: What is this formula actually saying?</h4>
                <div style="display: flex; align-items: center; gap: 1.75rem; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex-shrink: 0; display: flex; justify-content: center; width: 180px;">
                        <svg viewBox="0 0 220 140" style="width: 100%; height: auto;">
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
                    <div style="flex-grow: 1; min-width: 280px;">
                        <p style="margin-top: 0;">If looking at $\forall \epsilon > 0, \ \exists N \in \mathbb{N} \ \text{such that} \ \forall n > N, \ |a_n - L| < \epsilon$ makes your head spin, think of it as an <strong>archery challenge</strong> or a <strong>game between two players</strong>:</p>
                        <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                            <li style="margin-bottom: 0.4rem;"><strong>1. The Challenger sets tolerance ($\epsilon$):</strong> Your opponent hands you a tiny positive distance $\epsilon$, drawing a narrow target band around $L$.</li>
                            <li style="margin-bottom: 0.4rem;"><strong>2. You find a cutoff step ($N$):</strong> You determine how far down the list to walk—past index $N$—so everything settles inside the band.</li>
                            <li style="margin-bottom: 0.4rem;"><strong>3. The Tail Test ($|a_n - L| < \epsilon$):</strong> The absolute distance between $a_n$ and $L$ stays smaller than $\epsilon$ for <em>every step</em> past $N$.</li>
                        </ol>
                        <p style="margin-top: 0.5rem; margin-bottom: 0;">If you win no matter how small your opponent makes $\epsilon$, the sequence converges to $L$!</p>
                    </div>
                </div>
            </div>'''

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully aligned archery SVG to the left in week2.html.")
    else:
        print("Warning: old block exact match not found. Attempting replacement via regex or alternative check.")

def execute_git_sync():
    commit_message = (
        "Align archery target SVG to the left of epsilon-N explanation box\n\n"
        "Wrapped the content of the plain-English breakdown in week2.html into\n"
        "a flexbox layout so the archery graphic sits cleanly on the left side."
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
    align_archery_svg_left()
    execute_git_sync()
