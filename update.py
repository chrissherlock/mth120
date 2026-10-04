#!/usr/bin/env python3
import os
import subprocess

def update_russell_explanation():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacement block with beginner-friendly intuition and HTML &mdash; entity
    replacement_block = (
        '                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">\n'
        '                            <strong>The Shadow of Paradox:</strong> However, allowing any arbitrary property to define a set ("naive set theory") soon revealed cracks in paradise. In 1901, philosopher and logician Bertrand Russell formulated <strong><a href="https://en.wikipedia.org/wiki/Russell%27s_paradox" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; text-decoration: underline;">Russell\'s Paradox</a></strong> &mdash; the set of all sets that don\'t contain themselves &mdash; by considering the set $R$ of all such sets:\n'
        '                        </p>\n'
        '                        <div style="text-align: center; margin: 0.5rem 0;">\n'
        '                            $$R = \\{x \\mid x \\notin x\\}$$\n'
        '                        </div>\n'
        '                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">\n'
        '                            To see why this creates a crisis, ask a simple question: <em>Does $R$ contain itself?</em><br>\n'
        '                            &bull; If <strong>yes</strong>, it breaks its own rule and shouldn\'t be in $R$.<br>\n'
        '                            &bull; If <strong>no</strong>, its definition forces it to be included in $R$, meaning it <em>does</em> contain itself!<br>\n'
        '                            Either assumption blows up in our face, leading directly to the formal contradiction:\n'
        '                        </p>\n'
        '                        <div style="text-align: center; margin: 0.5rem 0;">\n'
        '                            $$R \\in R \\iff R \\notin R$$\n'
        '                        </div>\n'
        '                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">\n'
        '                            This stunning realization proved that set theory needed rigorous axiomatic guardrails&mdash;inspiring the modern Zermelo-Fraenkel foundations that keep our mathematical house standing today.\n'
        '                        </p>'
    )

    target_start = '<strong>The Shadow of Paradox:</strong>'
    if target_start in content:
        start_idx = content.find(target_start)
        p_end_idx = content.find('</p>', start_idx) + 4
        content = content[:start_idx] + replacement_block + content[p_end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Russell's Paradox explanation in week1-lecture1.html.")
        return True

    print("Error: Could not locate the target section in week1-lecture1.html.")
    return False

def synchronize_git_changes():
    commit_message = (
        "Add beginner-friendly explanation of Russell's Paradox to Cantor bio\n\n"
        "Enhanced the Russell's Paradox section in the Cantor biographical card in\n"
        "week1-lecture1.html by pairing the formal logical notation with an intuitive\n"
        "explanation of why the self-referential loop creates an inescapable contradiction."
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
    if update_russell_explanation():
        synchronize_git_changes()
