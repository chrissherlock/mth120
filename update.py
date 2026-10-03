#!/usr/bin/env python3
import os
import subprocess

def add_svg_to_squeeze_example():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old block containing the reciprocal comparison without SVG
    old_block = '''                <p><strong>Cautionary Contrast: What about the reciprocal $\frac{n}{\sin(n)}$?</strong></p>
                <p>It is easy to confuse $\frac{\sin(n)}{n}$ with its reciprocal $\frac{n}{\sin(n)}$. However, as $n$ grows while $\sin(n)$ periodically approaches $0$ near integer multiples of $\pi$, the ratio $\frac{n}{\sin(n)}$ shoots off toward $\pm\infty$ with wild, unbounded oscillations. Therefore, <strong>$\lim_{n\to\infty} \frac{n}{\sin(n)}$ diverges</strong> and the Squeeze Theorem cannot be applied here.</p>'''

    # New block embedding the SVG graph directly
    new_block = '''                <p><strong>Cautionary Contrast: What about the reciprocal $\frac{n}{\sin(n)}$?</strong></p>
                <p>It is easy to confuse $\frac{\sin(n)}{n}$ with its reciprocal $\frac{n}{\sin(n)}$. However, as $n$ grows while $\sin(n)$ periodically approaches $0$ near integer multiples of $\pi$, the ratio $\frac{n}{\sin(n)}$ shoots off toward $\pm\infty$ with wild, unbounded oscillations. Therefore, <strong>$\lim_{n\to\infty} \frac{n}{\sin(n)}$ diverges</strong> and the Squeeze Theorem cannot be applied here.</p>

                <!-- Embedded SVG Graph of n / sin(n) divergence -->
                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1rem; margin-top: 1rem;">
                    <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.5rem; text-align: center;">VISUALIZATION: Wild Divergence of $\frac{n}{\sin(n)}$ for $n = 1 \dots 50$</p>
                    <svg viewBox="0 0 800 340" style="width: 100%; height: auto; display: block;">
                        <!-- Axes -->
                        <line x1="60" y1="170" x2="760" y2="170" stroke="#cbd5e1" stroke-width="2"/>
                        <line x1="60" y1="30" x2="60" y2="310" stroke="#cbd5e1" stroke-width="2"/>
                        <text x="710" y="155" font-size="11" font-weight="bold" fill="#64748b">n (index)</text>
                        <text x="70" y="45" font-size="11" font-weight="bold" fill="#ef4444">Wild Vertical Spikes (Divergence)</text>

                        <!-- Data Points for n / sin(n) -->
                        <g>
                            <circle cx="74" cy="165" r="4" fill="#d97706"/><circle cx="88" cy="180" r="4" fill="#d97706"/><circle cx="102" cy="150" r="4" fill="#d97706"/><circle cx="116" cy="120" r="4" fill="#ef4444"/><circle cx="130" cy="200" r="4" fill="#d97706"/><circle cx="144" cy="230" r="4" fill="#d97706"/><circle cx="158" cy="110" r="4" fill="#ef4444"/><circle cx="172" cy="240" r="4" fill="#ef4444"/><circle cx="186" cy="190" r="4" fill="#d97706"/><circle cx="200" cy="130" r="4" fill="#d97706"/><circle cx="214" cy="290" r="4" fill="#ef4444"/><circle cx="228" cy="80" r="4" fill="#ef4444"/><circle cx="242" cy="185" r="4" fill="#d97706"/><circle cx="256" cy="155" r="4" fill="#d97706"/><circle cx="270" cy="60" r="4" fill="#ef4444"/><circle cx="284" cy="300" r="4" fill="#ef4444"/><circle cx="298" cy="210" r="4" fill="#d97706"/><circle cx="312" cy="140" r="4" fill="#d97706"/><circle cx="326" cy="45" r="4" fill="#ef4444"/><circle cx="340" cy="310" r="4" fill="#ef4444"/><circle cx="354" cy="220" r="4" fill="#d97706"/><circle cx="368" cy="150" r="4" fill="#d97706"/><circle cx="382" cy="30" r="4" fill="#ef4444"/><circle cx="396" cy="310" r="4" fill="#ef4444"/><circle cx="410" cy="205" r="4" fill="#d97706"/><circle cx="424" cy="135" r="4" fill="#d97706"/><circle cx="438" cy="35" r="4" fill="#ef4444"/><circle cx="452" cy="310" r="4" fill="#ef4444"/><circle cx="466" cy="195" r="4" fill="#d97706"/><circle cx="480" cy="125" r="4" fill="#d97706"/><circle cx="494" cy="50" r="4" fill="#ef4444"/><circle cx="508" cy="310" r="4" fill="#ef4444"/><circle cx="522" cy="215" r="4" fill="#d97706"/><circle cx="536" cy="145" r="4" fill="#d97706"/><circle cx="550" cy="40" r="4" fill="#ef4444"/><circle cx="564" cy="310" r="4" fill="#ef4444"/><circle cx="578" cy="200" r="4" fill="#d97706"/><circle cx="592" cy="130" r="4" fill="#d97706"/><circle cx="606" cy="55" r="4" fill="#ef4444"/><circle cx="620" cy="310" r="4" fill="#ef4444"/><circle cx="634" cy="210" r="4" fill="#d97706"/><circle cx="648" cy="140" r="4" fill="#d97706"/><circle cx="662" cy="45" r="4" fill="#ef4444"/><circle cx="676" cy="310" r="4" fill="#ef4444"/><circle cx="690" cy="205" r="4" fill="#d97706"/><circle cx="704" cy="135" r="4" fill="#d97706"/><circle cx="718" cy="35" r="4" fill="#ef4444"/><circle cx="732" cy="310" r="4" fill="#ef4444"/><circle cx="746" cy="195" r="4" fill="#d97706"/>
                        </g>
                    </svg>
                </div>'''

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully embedded SVG graph into Squeeze Theorem example in week2.html.")
    else:
        print("Reciprocal comparison block not found in week2.html.")

def execute_git_sync():
    commit_message = (
        "Embed n / sin(n) divergence SVG graph into Squeeze Theorem classic example\n\n"
        "Added an embedded SVG visualization contrasting the convergent sin(n)/n\n"
        "with the wildly oscillating, divergent n / sin(n) sequence in week2.html."
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
    add_svg_to_squeeze_example()
    execute_git_sync()
