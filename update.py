#!/usr/bin/env python3
import os
import subprocess

def insert_peano_biography_box():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    section4_heading = '<h2 id="peano-axioms">4. Peano\'s Axioms for Natural Numbers</h2>'

    peano_box_markup = r'''<h2 id="peano-axioms">4. Peano's Axioms for Natural Numbers</h2>

            <!-- HISTORICAL CONTEXT: GIUSEPPE PEANO -->
            <div class="infobox" style="margin-top: 1.5rem; margin-bottom: 2rem;">
                <h4>📖 Who was Giuseppe Peano?</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/peano.jpg" alt="Giuseppe Peano" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Giuseppe Peano<br>(1858–1932)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong>Giuseppe Peano</strong> was an Italian mathematician and logician at the University of Turin whose influence touches almost every page of modern mathematics. If you have ever written $\in$ for set membership, $\cup$ for union, or $\cap$ for intersection, you are using notation Peano personally invented to make mathematical arguments completely unambiguous.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>Why did he formulate these axioms?</strong> In the late nineteenth century, mathematics was undergoing a profound foundational crisis. For centuries, calculus and arithmetic had relied heavily on geometric sketches, physical intuition, and vague notions of "infinitesimals." But intuition began leading mathematicians into contradictions—Peano himself famously shocked the mathematical world by discovering a continuous curve that completely fills a two-dimensional square.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            Realizing that geometric intuition could no longer be trusted as proof, Peano set out to reconstruct arithmetic from the ground up. In his 1889 treatise <em>Arithmetices principia, nova methodo exposita</em>, he demonstrated that the entire infinite system of counting numbers, addition, and multiplication could be derived from just five simple, airtight logical rules.
                        </p>
                    </div>
                </div>
            </div>'''

    if section4_heading in content:
        if "Who was Giuseppe Peano?" in content:
            print("Peano biography infobox is already present in week1-lecture1.html.")
            return

        content = content.replace(section4_heading, peano_box_markup, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added Giuseppe Peano infobox to week1-lecture1.html.")
    else:
        print("Could not find the Section 4 heading in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Add historical biography infobox for Giuseppe Peano to Lecture 1\n\n"
        "Introduced an infobox under Section 4 of week1-lecture1.html detailing\n"
        "who Giuseppe Peano was and the historical motivation behind his axioms.\n"
        "Highlights the late 19th-century rigorization of analysis, his creation\n"
        "of standard set notation, and his drive to eliminate hidden assumptions\n"
        "from arithmetic."
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
    insert_peano_biography_box()
    synchronize_git_changes()
