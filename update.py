#!/usr/bin/env python3
import os
import subprocess

def inject_lecture1_orientation():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target_lead = r'''            <div class="intro-lead">
                Welcome to Lecture 1. Here we explore the fundamental grammar of pure mathematics: gathering objects into sets, mapping them through functions, and constructing our counting numbers from scratch using Peano's axioms.
            </div>'''

    reassuring_intro = r'''
            <!-- STUDENT ORIENTATION & REASSURANCE -->
            <div style="margin: 2rem 0 2.25rem 0;">
                <h3 style="margin-top: 0; color: #0f172a; font-size: 1.25rem;">Finding Your Footing: Welcome to Pure Mathematics</h3>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                    If you are joining this unit from secondary school calculus or applied introductory algebra, your first encounter with real analysis can feel slightly disorienting. Up to this point, mathematics has likely centered around <em>calculating answers</em>—finding an unknown $x$, sketching a quadratic curve, or evaluating an integral. Here, we step behind the curtain to examine the structural machinery that makes those techniques work in the first place.
                </p>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                    At first glance, some of what we do in this lecture might even seem strangely pedantic. You might reasonably wonder: <em>"Why do we need five abstract axioms just to define counting on our fingers? Why spend lecture time proving properties of numbers we have used without issue since primary school?"</em>
                </p>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                    The reality is that intuitive arithmetic, while dependable for everyday calculation, breaks down the moment we push into infinite collections, limits, and continuous curves. Much like writing reliable software requires unambiguous syntax before compiling complex algorithms, pure analysis demands an airtight grammar. Once we establish precisely what a set is, how mappings function, and how the natural numbers lock together like an unbroken chain of dominoes, we build a bedrock foundation that will never give way beneath us.
                </p>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 0;">
                    Do not feel discouraged if the symbolic notation seems dense on your first pass. Mathematical symbols are not barriers designed to keep you out; they are simply concise shorthand for very straightforward ideas. Take your time, lean into the analogies, and give yourself permission to explore the concepts rather than rushing to compute a final number.
                </p>
            </div>'''

    if target_lead in content:
        # Check if already present to prevent duplicate injections
        if "Finding Your Footing: Welcome to Pure Mathematics" in content:
            print("Orientation text is already present in week1-lecture1.html.")
            return

        content = content.replace(target_lead, target_lead + '\n' + reassuring_intro, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully integrated student orientation into week1-lecture1.html.")
    else:
        print("Could not locate the welcome lead in week1-lecture1.html.")

def execute_git_sync():
    commit_message = (
        "Add reassuring introduction for beginning students to Lecture 1\n\n"
        "Integrated an unboxed, welcoming prose introduction directly below the\n"
        "welcome lead in week1-lecture1.html. Normalises the shift from applied\n"
        "calculation to pure analytical reasoning and reassures students on the\n"
        "role of formal rigor."
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
    inject_lecture1_orientation()
    execute_git_sync()
