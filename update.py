#!/usr/bin/env python3

import re
import sys

def inject_toc_ids(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file '{file_path}'")
        return

    # Dictionary mapping the exact inner text of headings to their TOC IDs
    headers_to_ids = {
        "Why Calculus Intuition Leaves Us Wanting": "calculus-intuition",
        "Understanding Absolute Value as Physical Distance": "absolute-value-distance",
        "The Formal Definition": "formal-definition",
        "The Grammar of Analysis: Why Order Matters": "grammar-of-analysis",
        'The "Who Knows What" Rule: Order of Information': "who-knows-what",
        "When Can You Swap Quantifiers? (The Commutativity Rule)": "commutativity",
        r"The Fatal Quantifier Swap: Why $\exists N \; \forall \epsilon$ Breaks Mathematics": "fatal-swap",
        "A Practical Mental Checklist for Reading Proofs": "mental-checklist",
        r"Guide 1: The $\epsilon$-$N$ Challenge Game ($a_n = \frac{1}{n} \to 0$)": "guide1-adversarial",
        "Theorem: Uniqueness of Limits": "theorem-uniqueness",
        "Theorem: Tail Invariance (The Shift &amp; Truncation Theorem)": "theorem-tail-invariance",
        "Theorem: Order Limit Theorem (Preservation of Inequalities)": "theorem-order-limit",
        "Proposition 5: Fundamental Sequence Properties": "proposition-5",
        r"Property 1: Absolute Value Stabilization ($a_n \to L \implies |a_n| \to |L|$)": "prop5-abs",
        "Property 2: Convergence Implies Boundedness (The Prefix vs. Tail Strategy)": "prop5-bounded",
        "Property 3: Preservation of Sign (The Buffer Zone)": "prop5-sign",
        "The Architecture of Compositionality": "architecture-compositionality",
        "Theorem 1: The Algebraic Limit Laws": "theorem-limit-laws",
        r'The "$\epsilon/2$ Trick" and the Sum Law Proof': "epsilon-half-trick",
        'The "Add-and-Subtract Bridge": Proving the Product Law': "add-subtract-bridge",
        "Guarding the Denominator: The Quotient Law": "guarding-denominator",
        "The Flip Side: Defeating the Target Game": "flip-side-defeating",
        "The Anatomy of Negation: Flipping the Quantifiers": "anatomy-of-negation",
        r"Disproving Every Real Candidate at Once ($\forall L \in \mathbb{R}$)": "disproving-every-candidate",
        r"A Detailed Walkthrough: Proving That $a_n = (-1)^n$ Has No Limit": "walkthrough-divergence",
        "Summary Checklist: How to Disprove a Limit": "summary-checklist"
    }

    # 1. Update the H3 and H4 elements
    for text, dom_id in headers_to_ids.items():
        # Escape special characters, but replace escaped spaces with \s+ to handle HTML formatting/newlines
        escaped_text = re.escape(text).replace(r'\ ', r'\s+')

        # Regex breakdown:
        # Group 1: The opening tag up to the closing angle bracket (e.g., <h3 style="...">)
        # Group 2: The tag name itself (h3 or h4) - used for matching the closing tag
        # Group 3: The attributes inside the tag
        # Group 4: The angle bracket, inner text, and closing tag
        pattern = re.compile(rf'(<(h[34])([^>]*?))(>\s*{escaped_text}\s*</\2>)', re.IGNORECASE)

        def replacer(match):
            opening_tag = match.group(1)
            # Skip if the tag already contains an ID attribute to prevent duplication
            if 'id=' in opening_tag:
                return match.group(0)
            return f'{opening_tag} id="{dom_id}"{match.group(4)}'

        html_content = pattern.sub(replacer, html_content)

    # 2. Update the Worked Example div container
    div_target = r'<div class="worked-example-box" style="margin-top: 2rem;">'
    div_replacement = r'<div id="worked-example" class="worked-example-box" style="margin-top: 2rem;">'
    html_content = html_content.replace(div_target, div_replacement)

    # Write changes back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully injected TOC IDs into {file_path}")

if __name__ == "__main__":
    file_name = "week2-lecture4.html" if len(sys.argv) == 1 else sys.argv[1]
    inject_toc_ids(file_name)
