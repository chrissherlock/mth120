#!/usr/bin/env python3
import os
import re
import subprocess

def convert_orientation_to_unboxed_prose():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    unboxed_intro = r'''            <!-- ORIENTATION & ROADMAP -->
            <div style="margin: 2.25rem 0 2rem 0;">
                <h3 style="margin-top: 0; color: #0f172a;">Finding Your Footing in Pure Mathematics</h3>
                <p>If you are transitioning from high school calculus or introductory algebra, Week 1 can feel like stepping into unfamiliar territory. Up until now, mathematics has mostly focused on <em>calculating answers</em>—finding $x$, evaluating integrals, or graphing functions. Here, we step behind the scenes to examine <strong>the structural machinery itself</strong>.</p>
                <p>Think of this module as building the foundation across three main pillars:</p>
                <ul style="margin: 0.5rem 0 1rem 1.5rem; padding: 0;">
                    <li style="margin-bottom: 0.5rem;"><strong>Sets and Functions:</strong> The fundamental grammar of modern mathematics. Before analyzing numerical behavior, we need precise ways to gather objects together and establish mappings between them.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>Numbers and Completeness:</strong> Why fractions ($\mathbb{Q}$) leave tiny gaps on the number line, and how the real numbers ($\mathbb{R}$) form an unbroken continuum.</li>
                    <li><strong>Sequences and Sums:</strong> Your entry point into infinity. A sequence is an endless list progressing step by step, creating the bridge to limits and continuous analysis.</li>
                </ul>
                <p>Don't be intimidated by the formal symbols. Mathematical notation is simply concise shorthand for clear, intuitive concepts. Take each idea one step at a time.</p>
            </div>'''

    pattern_boxed = r'[ \t]*<!-- ORIENTATION & ROADMAP -->[\s\S]*?</div>[ \t]*(?=\n\s*<!-- SECTION 1 -->)'
    if re.search(pattern_boxed, content):
        # Using a callable bypasses replacement template escape parsing
        content = re.sub(pattern_boxed, lambda _: unboxed_intro.strip(), content)
        print("Replaced boxed orientation with unboxed prose in week1.html.")
    else:
        target = '<!-- SECTION 1 -->'
        if target in content:
            content = content.replace(target, unboxed_intro + '\n\n            <!-- SECTION 1 -->', 1)
            print("Inserted unboxed orientation before Section 1 in week1.html.")
        else:
            print("Target anchor '<!-- SECTION 1 -->' not found in week1.html.")
            return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def execute_git_sync():
    commit_message = (
        "Fix LaTeX escape crash and unbox orientation section in week1.html\n\n"
        "Resolved a re.PatternError caused by regex template evaluation of LaTeX\n"
        "macros (\\mathbb) by passing a callable to re.sub. Converted the boxed\n"
        "orientation section after the Table of Contents into unboxed prose."
    )
    commands = [
        ['git', 'add', 'week1.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    convert_orientation_to_unboxed_prose()
    execute_git_sync()
