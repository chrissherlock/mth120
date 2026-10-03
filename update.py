#!/usr/bin/env python3
import os
import re
import subprocess
import sys

def restore_exact_friendly_intros():
    filepath = 'week1.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        sys.exit(1)

    # 1. Section 1 Infobox Intro
    sec1_intro_replacement = (
        '<!-- SECTION 1 NOTATION INFOBOX -->\n'
        '            <div class="infobox">\n'
        '                <h4>📖 Notation Reference: Set Theory</h4>\n'
        '                <div class="infobox-intro">\n'
        '                    <strong>Taking your first steps into set theory notation?</strong> '
        'It is completely normal if curly braces, union symbols ($\cup$), and intersections ($\cap$) '
        'look like a secret code at first. Think of them simply as the grammar and punctuation of '
        'logic—shorthand ways of talking about collections, memberships, and groupings.\n'
        '                </div>'
    )
    content = re.sub(
        r'<!-- SECTION 1 NOTATION INFOBOX -->[\s\S]*?<div class="infobox-intro">[\s\S]*?</div>(?=\s*<div class="notation-grid">)',
        lambda _: sec1_intro_replacement,
        content,
        count=1
    )

    # 2. Section 2 Infobox Intro
    sec2_intro_replacement = (
        '<!-- SECTION 2 NOTATION INFOBOX -->\n'
        '            <div class="infobox">\n'
        '                <h4>📖 Notation Reference: Number Systems</h4>\n'
        '                <div class="infobox-intro">\n'
        '                    <strong>Navigating the expanding universe of numbers?</strong> '
        'If moving from counting numbers ($\mathbb{N}$) all the way to reals ($\mathbb{R}$) '
        'feels like a whirlwind of blackboard letters, do not worry! Each letter simply represents '
        'a tool invented to solve a specific algebraic puzzle that the previous system could not handle.\n'
        '                </div>'
    )
    content = re.sub(
        r'<!-- SECTION 2 NOTATION INFOBOX -->[\s\S]*?<div class="infobox-intro">[\s\S]*?</div>(?=\s*<div class="notation-grid">)',
        lambda _: sec2_intro_replacement,
        content,
        count=1
    )

    # 3. Section 3 Infobox Intro & Header
    sec3_header_intro_replacement = (
        '<!-- SECTION 3 NOTATION INFOBOX -->\n'
        '            <div class="infobox">\n'
        '                <h4>📖 Notation Reference: Sequences, Limits &amp; Quantifiers</h4>\n\n'
        '                <div class="infobox-intro">\n'
        '                    <strong>Don\'t be intimidated by the symbols!</strong> '
        'If upside-down A\'s ($\forall$), backward E\'s ($\exists$), or little ceiling brackets ($\lceil \dots \\rceil$) '
        'look unfamiliar, that is completely normal. They are simply mathematicians\' shorthand for everyday concepts:\n'
        '                    <ul>\n'
        '                        <li><strong>$\\forall$ (For all):</strong> Read as <em>"No matter how tiny an error budget you pick..."</em></li>\n'
        '                        <li><strong>$\\exists$ (There exists):</strong> Read as <em>"We can always point to a specific cutoff position..."</em></li>\n'
        '                        <li><strong>$\\lceil x \\rceil$ (Ceiling):</strong> Means <em>"round up to the next integer"</em> (e.g., $\\lceil 4.2 \\rceil = 5$), because position indices must be whole counting numbers!</li>\n'
        '                    </ul>\n'
        '                </div>'
    )
    content = re.sub(
        r'<!-- SECTION 3 NOTATION INFOBOX -->[\s\S]*?<h4>📖 Notation Reference: Sequences[^<]*</h4>[\s\S]*?<div class="infobox-intro">[\s\S]*?</div>(?=\s*<div class="notation-grid">)',
        lambda _: sec3_header_intro_replacement,
        content,
        count=1
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully restored exact friendly intros in {filepath}.")

def execute_git_sync():
    commit_message = (
        "Restore original friendly infobox intro messages in week1.html\n\n"
        "Restored the exact friendly intro paragraphs from prior to commit\n"
        "d25c8e0c across all three notation infoboxes in week1.html."
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
    restore_exact_friendly_intros()
    execute_git_sync()
