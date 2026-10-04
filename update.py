#!/usr/bin/env python3
import os
import subprocess

def update_density_section():
    filepath = 'week1-lecture2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old Section 1 block to replace
    old_section_1 = (
        '            <!-- SECTION 1 -->\n'
        '            <h2 id="density-rationals">1. Density of the Rational Numbers</h2>\n'
        '            <div class="infobox">\n'
        '                <h4>📖 Notation Reference: Number Sets &amp; Bounds</h4>\n'
        '                <div class="infobox-intro">\n'
        '                    <strong>The numbers we stand on:</strong> From counting numbers up to the unbroken real line, each extension repairs a specific structural limitation.\n'
        '                </div>\n'
        '                <div class="notation-grid">\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\mathbb{N}$</span><span class="notation-desc">Natural numbers $\\{0, 1, 2, \\dots\\}$</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\mathbb{Z}$</span><span class="notation-desc">Integers $\\{\\dots, -1, 0, 1, \\dots\\}$</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\mathbb{Q}$</span><span class="notation-desc">Rational numbers $\\{p/q \\mid p \\in \\mathbb{Z}, q \\in \\mathbb{Z}_+\\}$</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\mathbb{R}$</span><span class="notation-desc">Real numbers (complete ordered field)</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$|x|$</span><span class="notation-desc">Absolute value (distance to origin)</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\sup S$</span><span class="notation-desc">Supremum (least upper bound) of set $S$</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\inf S$</span><span class="notation-desc">Infimum (greatest lower bound) of set $S$</span></div>\n'
        '                </div>\n'
        '            </div>\n\n'
        '            <p>Fractions (rational numbers, $\\mathbb{Q}$) are packed incredibly tightly along the number line.</p>\n'
        '            <div class="definition-box">\n'
        '                <strong>Proposition 1 (Density of $\\mathbb{Q}$):</strong> For any two distinct rational numbers $a$ and $b$ with $a < b$, there exist infinitely many rational numbers strictly between them.\n'
        '            </div>\n'
        '            <p>\n'
        '                <em>Proof Construction:</em> The arithmetic midpoint $c_1 = \\frac{a+b}{2}$ is rational because $\\mathbb{Q}$ is closed under addition and division. Since $a < c_1 < b$, we can repeat this process on $a$ and $c_1$ to find $c_2 = \\frac{a+c_1}{2}$. Repeating this construction generates an infinite descending sequence of distinct rationals between $a$ and $b$:\n'
        '            </p>\n'
        '            <div style="text-align: center; margin: 1rem 0;">\n'
        '                $$b > c_1 > c_2 > c_3 > \\dots > a$$\n'
        '            </div>'
    )

    # Enhanced Section 1 block with warm, beginner-friendly explanations
    new_section_1 = (
        '            <!-- SECTION 1 -->\n'
        '            <h2 id="density-rationals">1. Density of the Rational Numbers</h2>\n'
        '            <div class="infobox">\n'
        '                <h4>📖 Notation Reference: Number Sets &amp; Bounds</h4>\n'
        '                <div class="infobox-intro">\n'
        '                    <strong>The numbers we stand on:</strong> From counting numbers up to the unbroken real line, each extension repairs a specific structural limitation.\n'
        '                </div>\n'
        '                <div class="notation-grid">\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\mathbb{N}$</span><span class="notation-desc">Natural numbers $\\{0, 1, 2, \\dots\\}$</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\mathbb{Z}$</span><span class="notation-desc">Integers $\\{\\dots, -1, 0, 1, \\dots\\}$</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\mathbb{Q}$</span><span class="notation-desc">Rational numbers $\\{p/q \\mid p \\in \\mathbb{Z}, q \\in \\mathbb{Z}_+\\}$</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\mathbb{R}$</span><span class="notation-desc">Real numbers (complete ordered field)</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$|x|$</span><span class="notation-desc">Absolute value (distance to origin)</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\sup S$</span><span class="notation-desc">Supremum (least upper bound) of set $S$</span></div>\n'
        '                    <div class="notation-item"><span class="notation-sym">$\\inf S$</span><span class="notation-desc">Infimum (greatest lower bound) of set $S$</span></div>\n'
        '                </div>\n'
        '            </div>\n\n'
        '            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">\n'
        '                At first glance, fractions (rational numbers, $\\mathbb{Q}$) feel like they fill up the number line entirely. If you pick any two fractions&mdash;say, $\\frac{1}{3}$ and $\\frac{1}{2}$&mdash;you can always find another one right between them (like their average, $\\frac{5}{12}$). In real analysis, this property is known as <strong>density</strong>.\n'
        '            </p>\n\n'
        '            <div class="definition-box">\n'
        '                <strong>Proposition 1 (Density of $\\mathbb{Q}$):</strong> For any two distinct rational numbers $a$ and $b$ with $a < b$, there exist infinitely many rational numbers strictly between them.\n'
        '            </div>\n\n'
        '            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;\">\n'
        '                <em>Building the Intuition:</em> How do we prove this rigorously without getting lost in an infinite loop? We use a constructive argument. If we take our two fractions $a$ and $b$, their arithmetic midpoint is guaranteed to sit safely halfway between them:\n'
        '            </p>\n\n'
        '            <div style="text-align: center; margin: 1.25rem 0; font-size: 1.05rem;">\n'
        '                $$c_1 = \\frac{a+b}{2}$$\n'
        '            </div>\n\n'
        '            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">\n'
        '                Because the rational numbers are closed under addition and division by non-zero integers, $c_1$ is guaranteed to be a rational number itself. Now, imagine zooming in on the left half of our interval, between $a$ and $c_1$. We can take their midpoint $c_2 = \\frac{a+c_1}{2}$. By repeating this zooming process endlessly, we generate an infinite descending sequence of unique rational numbers trapped between $a$ and $b$:\n'
        '            </p>\n\n'
        '            <div style="text-align: center; margin: 1rem 0;">\n'
        '                $$a < c_3 < c_2 < c_1 < b$$\n'
        '            </div>\n\n'
        '            <div class="aside-box">\n'
        '                <h4>💡 A Surprising Takeaway</h4>\n'
        '                <p style="margin-bottom: 0;">\n'
        '                    Even though $\\mathbb{Q}$ is packed so tightly that you can never find two fractions "touching" without another fraction between them, <strong>it is still full of invisible gaps</strong>. As we will see in the next section, these microscopic rational gaps are precisely where irrational numbers like $\\sqrt{2}$ live!\n'
        '                </p>\n'
        '            </div>'
    )

    if old_section_1 in content:
        content = content.replace(old_section_1, new_section_1, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Section 1 in week1-lecture2.html.")
        return True

    print("Error: Could not locate exact Section 1 match in week1-lecture2.html.")
    return False

def synchronize_git_changes():
    commit_message = (
        "Refine and explain Rational Density section in week1-lecture2.html\n\n"
        "Updated Section 1 of week1-lecture2.html to adopt a warm, intuitive\n"
        "pedagogical approach, breaking down the midpoint construction and\n"
        "highlighting the paradoxical gaps in the rational number line."
    )
    commands = [
        ['git', 'add', 'week1-lecture2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    if update_density_section():
        synchronize_git_changes()
