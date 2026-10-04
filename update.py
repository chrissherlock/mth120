#!/usr/bin/env python3
import os
import subprocess

def insert_set_operations_infobox():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    section2_anchor = '<h2 id="set-operations">2. Set Operations and Products</h2>'

    infobox_markup = r'''<h2 id="set-operations">2. Set Operations and Products</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Set Operations</h4>
                <div class="infobox-intro">
                    <strong>The algebra of collections:</strong> Just as arithmetic has addition and multiplication, set theory uses precise logical operations to combine, compare, and partition sets.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$A \cup B$</span><span class="notation-desc">Union: elements in $A$, in $B$, or in both ($\lor$)</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \cap B$</span><span class="notation-desc">Intersection: elements common to both $A$ and $B$ ($\land$)</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \setminus B$</span><span class="notation-desc">Difference: elements in $A$ that are not in $B$</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \times B$</span><span class="notation-desc">Cartesian product: set of all ordered pairs $(a, b)$</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \cap B = \emptyset$</span><span class="notation-desc">Disjoint sets: sets sharing no elements</span></div>
                    <div class="notation-item"><span class="notation-sym">$|A \times B|$</span><span class="notation-desc">Product cardinality: $|A| \cdot |B|$ total pairs</span></div>
                </div>
            </div>'''

    if section2_anchor in content:
        if "Notation Reference: Set Operations" in content:
            print("Notation reference is already present in Section 2.")
            return

        content = content.replace(section2_anchor, infobox_markup, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully restored the Set Operations notation infobox in week1-lecture1.html.")
    else:
        print("Could not find the Section 2 heading anchor in week1-lecture1.html.")

def execute_git_sync():
    commit_message = (
        "Restore set operations notation reference infobox to Lecture 1\n\n"
        "Reintroduced a dedicated notation reference infobox at the beginning\n"
        "of Section 2 in week1-lecture1.html. Summarizes symbols for union,\n"
        "intersection, relative complement, Cartesian product, and disjoint sets\n"
        "to match the reference layouts in Sections 1 and 3."
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
    insert_set_operations_infobox()
    execute_git_sync()
