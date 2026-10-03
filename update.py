#!/usr/bin/env python3
import os
import subprocess

def add_reciprocal_comparison_to_squeeze_example():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old Classic Example block
    old_classic_example = '''            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Classic Example: Applying the Squeeze Theorem</h4>
                <p>Consider evaluating $\lim_{n\to\infty} \frac{\sin(n)}{n}$. Because sine oscillates between $-1$ and $1$, we know:</p>
                <p style="text-align: center; margin: 0.75rem 0;">$$-\frac{1}{n} \le \frac{\sin(n)}{n} \le \frac{1}{n}$$</p>
                <p>Since $\lim_{n\to\infty} \left(-\frac{1}{n}\right) = 0$ and $\lim_{n\to\infty} \left(\frac{1}{n}\right) = 0$, the Squeeze Theorem forces our middle sequence to also converge:</p>
                <p style="text-align: center; margin-top: 0.75rem;">$$\lim_{n\to\infty} \frac{\sin(n)}{n} = 0$$</p>
            </div>'''

    # Expanded Classic Example block featuring both sin(n)/n and n/sin(n)
    expanded_classic_example = '''            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Classic Example: Applying the Squeeze Theorem</h4>
                <p>Consider evaluating $\lim_{n\to\infty} \frac{\sin(n)}{n}$. Because sine oscillates between $-1$ and $1$, we know:</p>
                <p style="text-align: center; margin: 0.75rem 0;">$$-\frac{1}{n} \le \frac{\sin(n)}{n} \le \frac{1}{n}$$</p>
                <p>Since $\lim_{n\to\infty} \left(-\frac{1}{n}\right) = 0$ and $\lim_{n\to\infty} \left(\frac{1}{n}\right) = 0$, the Squeeze Theorem forces our middle sequence to also converge:</p>
                <p style="text-align: center; margin-top: 0.75rem;">$$\lim_{n\to\infty} \frac{\sin(n)}{n} = 0$$</p>

                <hr style="border: none; border-top: 1px solid #fde68a; margin: 1.25rem 0;">

                <p><strong>Cautionary Contrast: What about the reciprocal $\frac{n}{\sin(n)}$?</strong></p>
                <p>It is easy to confuse $\frac{\sin(n)}{n}$ with its reciprocal $\frac{n}{\sin(n)}$. However, as $n$ grows while $\sin(n)$ periodically approaches $0$ near integer multiples of $\pi$, the ratio $\frac{n}{\sin(n)}$ shoots off toward $\pm\infty$ with wild, unbounded oscillations. Therefore, <strong>$\lim_{n\to\infty} \frac{n}{\sin(n)}$ diverges</strong> and the Squeeze Theorem cannot be applied here.</p>
            </div>'''

    if old_classic_example in content:
        content = content.replace(old_classic_example, expanded_classic_example)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added n/sin(n) comparison to Squeeze Theorem example in week2.html.")
    else:
        print("Classic Example block not found in week2.html.")

def execute_git_sync():
    commit_message = (
        "Add comparison for n / sin(n) divergence in Squeeze Theorem classic example\n\n"
        "Expanded the Squeeze Theorem classic example box in week2.html to contrast\n"
        "the convergent sin(n)/n with the divergent reciprocal n / sin(n)."
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
    add_reciprocal_comparison_to_squeeze_example()
    execute_git_sync()
