#!/usr/bin/env python3
import os
import subprocess

def relocate_peano_biography():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    start_box_token = '<!-- HISTORICAL CONTEXT: GIUSEPPE PEANO -->'
    end_box_token = '</div>\n            </div>'
    footer_token = '<!-- FOOTER NAVIGATION -->'

    peano_box_markup = r'''<!-- HISTORICAL CONTEXT: GIUSEPPE PEANO -->
            <div class="infobox" style="margin-top: 2rem; margin-bottom: 2rem;">
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

    # If the box is currently sitting at the top of Section 4, remove it first
    if start_box_token in content:
        start_idx = content.find(start_box_token)
        end_idx = content.find(end_box_token, start_idx)
        if start_idx != -1 and end_idx != -1:
            end_idx += len(end_box_token)
            content = content[:start_idx] + content[end_idx:].lstrip()

    # Re-insert the infobox right before the footer navigation
    footer_idx = content.find(footer_token)
    if footer_idx != -1:
        content = content[:footer_idx] + peano_box_markup + '\n\n            ' + content[footer_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully relocated Peano infobox to the bottom of Section 4.")
    else:
        print("Could not locate the footer navigation token in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Relocate Giuseppe Peano biographical infobox to bottom of Section 4\n\n"
        "Moved the historical infobox on Giuseppe Peano from the top of\n"
        "Section 4 to the conclusion of the section. This ensures students\n"
        "first engage with the mathematical mechanics of the five axioms and\n"
        "primitive recursive arithmetic before exploring the historical context\n"
        "and foundational crisis that motivated his work."
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
    relocate_peano_biography()
    synchronize_git_changes()
