#!/usr/bin/env python3
import os
import subprocess

def expand_section_4_infinity():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # New expanded Section 4 block
    new_section_4 = r'''            <!-- SECTION 4 -->
            <h2 id="section-infinity">4. Infinity as a Limit (Divergence to Infinity)</h2>
            <p>Not all divergent sequences bounce around chaotically like $\frac{n}{\sin(n)}$ or alternate forever like $(-1)^n$. Many sequences grow steadily larger and larger, marching off toward infinity. While these sequences do not converge to a finite number $L$ (and thus technically <em>diverge</em>), we assign a special classification: they <strong>diverge to infinity</strong>.</p>

            <div class="definition-box">
                <p><strong>Formal Definition: Divergence to Infinity ($M\text{-}N$ Definition)</strong></p>
                <p>A sequence $(a_n)$ tends to infinity, written $\lim_{n\to\infty} a_n = \infty$, if:</p>
                <p style="text-align: center; margin: 0.75rem 0;">$$\forall M > 0, \quad \exists N \in \mathbb{N} \quad \text{such that} \quad \forall n > N, \quad a_n > M$$</p>
                <p>Similarly, a sequence tends to negative infinity ($\lim_{n\to\infty} a_n = -\infty$) if for every negative threshold $M < 0$, there exists an index $N$ such that $a_n < M$ for all $n > N$.</p>
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>💡 Intuition: The Towering Floor Game ($M\text{-}N$ Game)</h4>
                <p>Compare this to our $\epsilon\text{-}N$ archery game for finite limits:</p>
                <ul style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Finite Limit ($\lim a_n = L$):</strong> Your opponent gives you a tiny tolerance $\epsilon > 0$ to trap the sequence in a narrow neighborhood.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Infinite Limit ($\lim a_n = \infty$):</strong> Your opponent hands you an astronomically high threshold $M$ (e.g., $M = 1,000,000$).</li>
                    <li><strong>Your Goal ($N$):</strong> You must find a cutoff index $N$ such that every term past $N$ towers <em>above</em> $M$ and never drops back down. If you can always find such an $N$ no matter how absurdly large your opponent makes $M$, the sequence diverges to infinity.</li>
                </ul>
            </div>

            <!-- EMBEDDED SVG DIAGRAM FOR INFINITY LIMIT -->
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
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Worked Example: Proving $\lim_{n\to\infty} \sqrt{n} = \infty$</h4>
                <p>Let's use the formal $M\text{-}N$ definition to prove that the sequence $a_n = \sqrt{n}$ diverges to infinity:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>The Challenge:</strong> Given any arbitrary real number $M > 0$ (assume $M$ is large), we want to find an integer $N$ such that if $n > N$, then $\sqrt{n} > M$.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Working Backwards:</strong> Solve the inequality $\sqrt{n} > M$ for $n$. Squaring both sides gives $n > M^2$.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Choosing $N$:</strong> Choose any integer $N$ such that $N \ge M^2$ (or explicitly $N = \lceil M^2 \rceil$).</li>
                    <li><strong>Conclusion:</strong> For any $n > N$, we have $n > M^2$, which implies $\sqrt{n} > \sqrt{M^2} = M$. Thus, by definition, $\lim_{n\to\infty} \sqrt{n} = \infty$.</li>
                </ol>
            </div>'''

    # Anchor markers to replace Section 4
    old_sec_4_marker = '<!-- SECTION 4 -->'
    footer_marker = '<!-- BOTTOM NAVIGATION FOOTER -->'

    if old_sec_4_marker in content and footer_marker in content:
        parts = content.split('<!-- SECTION 4 -->')
        header_part = parts[0]
        rest_part = parts[1].split('<!-- BOTTOM NAVIGATION FOOTER -->')[1]

        updated_content = header_part + new_section_4 + '\n\n            <!-- BOTTOM NAVIGATION FOOTER -->' + rest_part
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully expanded Section 4 in week2.html.")
    else:
        print("Section 4 anchors not found in week2.html.")

def execute_git_sync():
    commit_message = (
        "Expand and update Section 4: Infinity as a Limit in week2.html\n\n"
        "Added formal M-N definition, towering floor intuition, an SVG threshold\n"
        "diagram, and a formal worked proof for week2.html."
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
    expand_section_4_infinity()
    execute_git_sync()
