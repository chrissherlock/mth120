#!/usr/bin/env python3
import os
import subprocess

def add_mathematicians_biographies():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    descartes_box = r'''            <!-- HISTORICAL CONTEXT: RENE DESCARTES -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ Who was René Descartes?</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/decartes.jpg" alt="René Descartes" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">René Descartes<br>(1596–1650)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong><a href="https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; text-decoration: underline;">René Descartes</a></strong> was a French philosopher, scientist, and mathematician whose Latinized name, <em>Renatus Cartesius</em>, gives us the term <strong>Cartesian</strong>.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>Why do ordered pairs bear his name?</strong> Prior to Descartes, algebra and geometry were studied as completely disconnected subjects. In his 1637 work <em><a href="https://en.wikipedia.org/wiki/La_G%C3%A9om%C3%A9trie" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; font-style: italic; text-decoration: underline;">La Géométrie</a></em>, Descartes introduced the revolutionary idea of specifying the position of a point using an ordered pair of numbers $(x, y)$ measured along perpendicular axes.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            By constructing the Cartesian product of the real line with itself ($\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$), geometric curves could be analyzed through algebraic equations, and algebraic formulas could be visualized geometrically. This conceptual bridge between numbers and geometry is the ground upon which all of calculus and modern analysis stands.
                        </p>
                    </div>
                </div>
            </div>
'''

    cantor_box = r'''            <!-- HISTORICAL CONTEXT: GEORG CANTOR -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ Who was Georg Cantor?</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/cantor.jpg" alt="Georg Cantor" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Georg Cantor<br>(1845–1918)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong><a href="https://en.wikipedia.org/wiki/Georg_Cantor" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; text-decoration: underline;">Georg Cantor</a></strong> was a German mathematician and the principal architect of modern set theory. During the 1870s, his investigations into Fourier series led him to ask fundamental questions about the nature of infinite collections.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>The Power of Bijections:</strong> In Section 3.2, we defined a <strong>bijection</strong> as a one-to-one and onto mapping. Cantor realized that bijections provided an exact, unambiguous way to measure the size (or <em>cardinality</em>) of sets without counting them element-by-element: two sets have the exact same size if and only if there exists a bijection between them.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            Applying this insight to infinite sets yielded a conclusion that unsettled 19th-century mathematics: infinity is not monolithic. Cantor proved that while natural numbers $\mathbb{N}$ and rational numbers $\mathbb{Q}$ share the same cardinality, the continuum of real numbers $\mathbb{R}$ is strictly larger—no bijection between $\mathbb{N}$ and $\mathbb{R}$ can ever exist. Though fiercely opposed by contemporaries like Leopold Kronecker, his work became the foundation of modern analysis, prompting David Hilbert to declare: <em>"No one shall expel us from the paradise that Cantor has created."</em>
                        </p>
                    </div>
                </div>
            </div>
'''

    # Insert Descartes before <!-- SECTION 3 -->
    sec3_delim = '<!-- SECTION 3 -->'
    if sec3_delim in content and "Who was René Descartes?" not in content:
        sec3_idx = content.find(sec3_delim)
        content = content[:sec3_idx] + descartes_box + '\n            ' + content[sec3_idx:]
        print("Inserted René Descartes biography into Section 2.")
    else:
        print("Skipped Descartes insertion (already present or delimiter missing).")

    # Insert Cantor before <!-- SECTION 4 -->
    sec4_delim = '<!-- SECTION 4 -->'
    if sec4_delim in content and "Who was Georg Cantor?" not in content:
        sec4_idx = content.find(sec4_delim)
        content = content[:sec4_idx] + cantor_box + '\n            ' + content[sec4_idx:]
        print("Inserted Georg Cantor biography into Section 3.")
    else:
        print("Skipped Cantor insertion (already present or delimiter missing).")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def synchronize_git_changes():
    commit_message = (
        "Add biographical profiles for Descartes and Cantor to Lecture 1\n\n"
        "Added .biography-box profiles for René Descartes at the end of Section 2\n"
        "and Georg Cantor at the end of Section 3 in week1-lecture1.html. Connects\n"
        "Cartesian products to Descartes' unification of algebra and geometry,\n"
        "and bijective mappings to Cantor's cardinality of infinite sets."
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
    add_mathematicians_biographies()
    synchronize_git_changes()
