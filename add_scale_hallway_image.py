#!/usr/bin/env python3
r"""
add_scale_hallway_image.py

Embeds 'images/scale-hallway.png' as Figure 5.2 into Section 5.1 of
week1-lecture3.html, completing the visual pair for sequence algebra operations.
"""

import sys
import subprocess
from pathlib import Path

SCALE_FIGURE_HTML = """            <!-- ILLUSTRATION: SCALE HALLWAY -->
            <div style="margin: 1.75rem 0 2rem 0; text-align: center;">
                <div style="border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); background: #ffffff;">
                    <img src="images/scale-hallway.png" alt="Scalar multiplication across an infinite locker hallway" style="width: 100%; height: auto; display: block;">
                </div>
                <p style="font-size: 0.88rem; color: #64748b; margin-top: 0.6rem; line-height: 1.5;">
                    <em>Figure 5.2:</em> Scalar multiplication on a sequence. Every slip of paper inside Hallway $A$ has its stored magnitude scaled by multiplier $\\lambda$ ($(\\lambda a)_n = \\lambda a_n$).
                </p>
            </div>"""

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def main() -> None:
    target = Path("week1-lecture3.html")
    if not target.exists():
        print(f"Error: {target.name} not found.", file=sys.stderr)
        sys.exit(1)

    content = target.read_text(encoding="utf-8")

    if "images/scale-hallway.png" in content:
        print(f"scale-hallway.png is already present in {target.name}.")
        return

    # Check if sum-hallway is present to place scale-hallway immediately after it
    sum_token = "images/sum-hallway.png"
    sum_pos = content.find(sum_token)

    if sum_pos != -1:
        # Locate the end of the sum-hallway figure block
        close_div = content.find("</div>", sum_pos)
        if close_div != -1:
            # Step past the outer wrapping div
            outer_close_div = content.find("</div>", close_div + len("</div>"))
            insert_idx = (outer_close_div + len("</div>")) if outer_close_div != -1 else (close_div + len("</div>"))
            updated_content = content[:insert_idx] + "\n\n" + SCALE_FIGURE_HTML + content[insert_idx:]
        else:
            print("Error: Could not find end of sum-hallway block.", file=sys.stderr)
            sys.exit(1)
    else:
        # Fallback: insert directly below Section 5.1 bullet list
        anchor = "Mathematicians describe this as <strong>pointwise</strong> or <strong>term-by-term</strong> arithmetic."
        pos = content.find(anchor)
        if pos == -1:
            print("Error: Could not locate Section 5.1 anchor.", file=sys.stderr)
            sys.exit(1)
        close_ul = content.find("</ul>", pos)
        insert_idx = close_ul + len("</ul>")
        updated_content = content[:insert_idx] + "\n\n" + SCALE_FIGURE_HTML + content[insert_idx:]

    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully added scale-hallway.png to {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Add Figure 5.2 scalar multiplication hallway illustration"
        commit_body = (
            "Embed images/scale-hallway.png into Section 5.1 of\n"
            "week1-lecture3.html to complete the visual pair for pointwise\n"
            "addition and scalar multiplication on sequences."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed Figure 5.2.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
