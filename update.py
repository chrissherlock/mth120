#!/usr/bin/env python3
import os
import subprocess

def inject_friendly_intro():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    welcome_box = r'''            <!-- ORIENTATION & ROADMAP -->
            <div class="aside-box" style="background: #f8fafc; border-left: 4px solid var(--accent); border-color: #cbd5e1; margin: 2rem 0;">
                <h4 style="color: #0f172a;">🌱 Finding Your Footing in Pure Mathematics</h4>
                <p>If you are transitioning from high school calculus or applied algebra, Week 1 can feel like stepping into a whole new world. Up until now, mathematics has mostly been about <em>calculating answers</em>—finding $x$, taking a derivative, or plotting curves. Here, we step behind the curtain to examine <strong>the structural machinery itself</strong>.</p>
                <p style="margin-bottom: 0.5rem;">Think of this week as laying the bedrock across three core ideas:</p>
                <ul style="margin: 0 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Sets and Functions:</strong> The fundamental grammar and nouns of modern mathematics. Before we can talk about numbers doing things, we need a precise way to collect them and describe how they interact.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Numbers and Completeness:</strong> Why fractions ($\mathbb{Q}$) alone leave microscopic gaps on the ruler, and how the real numbers ($\mathbb{R}$) form a seamless continuum.</li>
                    <li><strong>Sequences and Sums:</strong> Your entry point into infinity. A sequence is an endless list marching forward step by step, setting the stage for limits and continuous analysis.</li>
                </ul>
                <p style="margin-top: 0.75rem; margin-bottom: 0;">Don't let the formal notation intimidate you. Every strange symbol you encounter is just shorthand for a clear, intuitive idea. Take it one line at a time!</p>
            </div>'''

    target = '            <!-- SECTION 1 -->'
    replacement = welcome_box + '\n\n' + target

    if '🌱 Finding Your Footing in Pure Mathematics' in content:
        print("Orientation section already present in week1.html.")
        return

    if target in content:
        content = content.replace(target, replacement, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully injected friendly orientation into week1.html.")
    else:
        print("Target anchor '<!-- SECTION 1 -->' not found in week1.html.")

def execute_git_sync():
    commit_message = (
        "Add friendly orientation section after TOC in week1.html\n\n"
        "Inserted an accessible roadmap and orientation guide beneath the Table\n"
        "of Contents to bridge the transition to pure mathematical thinking."
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
    inject_friendly_intro()
    execute_git_sync()
