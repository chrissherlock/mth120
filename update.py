#!/usr/bin/env python3
"""
Update week1-lecture3.html to implement a responsive table layout with a sticky
index column, touch acceleration, and mobile swipe telemetry.
"""

from pathlib import Path
import subprocess
import sys

TARGET_FILE = Path("week1-lecture3.html")
SCRIPT_FILE = Path(__file__).resolve()

COMMIT_SUBJECT = (
    "Make comparative sequence table responsive with sticky index column"
)
COMMIT_BODY = (
    "Enforce a 600px min-width on the Section 5 comparative sequence table\n"
    "to prevent column cramping on mobile viewports. Make the Locker index\n"
    "column sticky so row context is preserved during horizontal scroll.\n"
    "Add touch momentum scrolling and a responsive swipe indicator banner."
)


def inject_responsive_table_styles(content: str) -> str:
    """Inject CSS rules for the sticky table layout and mobile banner."""
    table_css = """
        /* Responsive Stepping Table Styles */
        .table-scroll-hint {
            display: none;
            font-size: 0.76rem;
            font-weight: 700;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.4rem;
            text-align: right;
        }
        .stepping-table-wrap {
            width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            margin: 1.25rem 0 1.75rem 0;
            border: 1px solid var(--border);
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
            background: #ffffff;
        }
        .stepping-table {
            width: 100%;
            min-width: 600px;
            border-collapse: collapse;
            font-size: 0.92rem;
            text-align: center;
        }
        .stepping-table th {
            background: #f1f5f9;
            padding: 0.65rem 0.75rem;
            color: #475569;
            font-weight: 600;
            border-bottom: 2px solid var(--border);
        }
        .stepping-table td {
            padding: 0.6rem 0.75rem;
            border-bottom: 1px solid #e2e8f0;
        }
        .stepping-table tr:last-child td {
            border-bottom: none;
        }
        .stepping-table tr.row-plateau {
            background: #f0fdf4;
        }
        /* Sticky Leftmost Column (Locker Index) */
        .stepping-table th:first-child,
        .stepping-table td:first-child {
            position: sticky;
            left: 0;
            z-index: 2;
            background: #ffffff;
            box-shadow: 2px 0 5px -2px rgba(0,0,0,0.12);
        }
        .stepping-table th:first-child {
            background: #f1f5f9;
            z-index: 3;
        }
        .stepping-table tr.row-plateau td:first-child {
            background: #f0fdf4;
        }
    """

    content = content.replace("</style>", f"{table_css}\n    </style>", 1)

    mobile_media_rule = (
        "@media (max-width: 768px) {\n"
        "            .table-scroll-hint { display: block !important; }\n"
        "            .stepping-table td, .stepping-table th { "
        "font-size: 0.85rem !important; padding: 0.5rem 0.6rem !important; }\n"
    )
    return content.replace("@media (max-width: 768px) {\n", mobile_media_rule, 1)


def upgrade_stepping_table_markup(content: str) -> str:
    """Replace inline-styled table with responsive classes and sticky columns."""
    old_table_snippet = """            <!-- BEGINNER-FRIENDLY COMPARATIVE STEPPING TABLE -->
            <div style="overflow-x: auto; margin: 1.25rem 0;">
                <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; text-align: center;">
                    <thead>
                        <tr style="background: #f1f5f9; border-bottom: 2px solid var(--border);">
                            <th style="padding: 0.65rem 0.75rem; color: #475569; font-weight: 600;">Locker <span class="nobr">$n$</span></th>
                            <th style="padding: 0.65rem 0.75rem; color: #0284c7; font-weight: 600;">Climb: <span class="nobr">$a_n = 2n + 1$</span></th>
                            <th style="padding: 0.65rem 0.75rem; color: #d97706; font-weight: 600;">Bounce: <span class="nobr">$b_n = (-1)^n$</span></th>
                            <th style="padding: 0.65rem 0.75rem; color: #059669; font-weight: 600;">Sum: <span class="nobr">$c_n = a_n + b_n$</span></th>
                            <th style="padding: 0.65rem 0.75rem; color: #0f172a; font-weight: 600; text-align: left;">Stepping Motion</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;"><span class="nobr">$n = 0$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #0369a1;"><span class="nobr">$1$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #b45309;"><span class="nobr">$+1$</span></td>
                            <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;"><span class="nobr">$2$</span></td>
                            <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Baseline starting point</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #f0fdf4;">
                            <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;"><span class="nobr">$n = 1$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #0369a1;"><span class="nobr">$3$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #b45309;"><span class="nobr">$-1$</span></td>
                            <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;"><span class="nobr">$2$</span></td>
                            <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: <span class="nobr">$-1$</span> cancels climb (<span class="nobr">$c_1 = c_0$</span>)</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;"><span class="nobr">$n = 2$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #0369a1;"><span class="nobr">$5$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #b45309;"><span class="nobr">$+1$</span></td>
                            <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;"><span class="nobr">$6$</span></td>
                            <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Steps forward by <span class="nobr">$+4$</span></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #f0fdf4;">
                            <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;"><span class="nobr">$n = 3$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #0369a1;"><span class="nobr">$7$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #b45309;"><span class="nobr">$-1$</span></td>
                            <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;"><span class="nobr">$6$</span></td>
                            <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: <span class="nobr">$-1$</span> cancels climb (<span class="nobr">$c_3 = c_2$</span>)</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;"><span class="nobr">$n = 4$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #0369a1;"><span class="nobr">$9$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #b45309;"><span class="nobr">$+1$</span></td>
                            <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;"><span class="nobr">$10$</span></td>
                            <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Steps forward by <span class="nobr">$+4$</span></td>
                        </tr>
                        <tr>
                            <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;"><span class="nobr">$n = 5$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #0369a1;"><span class="nobr">$11$</span></td>
                            <td style="padding: 0.6rem 0.75rem; color: #b45309;"><span class="nobr">$-1$</span></td>
                            <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;"><span class="nobr">$10$</span></td>
                            <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: <span class="nobr">$-1$</span> cancels climb (<span class="nobr">$c_5 = c_4$</span>)</td>
                        </tr>
                    </tbody>
                </table>
            </div>"""

    new_table_snippet = """            <!-- BEGINNER-FRIENDLY COMPARATIVE STEPPING TABLE -->
            <div class="table-scroll-hint">↔ Swipe horizontally to inspect values</div>
            <div class="stepping-table-wrap">
                <table class="stepping-table">
                    <thead>
                        <tr>
                            <th>Locker <span class="nobr">$n$</span></th>
                            <th style="color: #0284c7;">Climb: <span class="nobr">$a_n = 2n + 1$</span></th>
                            <th style="color: #d97706;">Bounce: <span class="nobr">$b_n = (-1)^n$</span></th>
                            <th style="color: #059669;">Sum: <span class="nobr">$c_n = a_n + b_n$</span></th>
                            <th style="text-align: left;">Stepping Motion</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><span class="nobr">$n = 0$</span></td>
                            <td style="color: #0369a1;"><span class="nobr">$1$</span></td>
                            <td style="color: #b45309;"><span class="nobr">$+1$</span></td>
                            <td style="font-weight: 700; color: #047857;"><span class="nobr">$2$</span></td>
                            <td style="text-align: left; color: #475569;">Baseline starting point</td>
                        </tr>
                        <tr class="row-plateau">
                            <td><span class="nobr">$n = 1$</span></td>
                            <td style="color: #0369a1;"><span class="nobr">$3$</span></td>
                            <td style="color: #b45309;"><span class="nobr">$-1$</span></td>
                            <td style="font-weight: 700; color: #047857;"><span class="nobr">$2$</span></td>
                            <td style="text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: <span class="nobr">$-1$</span> cancels climb (<span class="nobr">$c_1 = c_0$</span>)</td>
                        </tr>
                        <tr>
                            <td><span class="nobr">$n = 2$</span></td>
                            <td style="color: #0369a1;"><span class="nobr">$5$</span></td>
                            <td style="color: #b45309;"><span class="nobr">$+1$</span></td>
                            <td style="font-weight: 700; color: #047857;"><span class="nobr">$6$</span></td>
                            <td style="text-align: left; color: #475569;">Steps forward by <span class="nobr">$+4$</span></td>
                        </tr>
                        <tr class="row-plateau">
                            <td><span class="nobr">$n = 3$</span></td>
                            <td style="color: #0369a1;"><span class="nobr">$7$</span></td>
                            <td style="color: #b45309;"><span class="nobr">$-1$</span></td>
                            <td style="font-weight: 700; color: #047857;"><span class="nobr">$6$</span></td>
                            <td style="text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: <span class="nobr">$-1$</span> cancels climb (<span class="nobr">$c_3 = c_2$</span>)</td>
                        </tr>
                        <tr>
                            <td><span class="nobr">$n = 4$</span></td>
                            <td style="color: #0369a1;"><span class="nobr">$9$</span></td>
                            <td style="color: #b45309;"><span class="nobr">$+1$</span></td>
                            <td style="font-weight: 700; color: #047857;"><span class="nobr">$10$</span></td>
                            <td style="text-align: left; color: #475569;">Steps forward by <span class="nobr">$+4$</span></td>
                        </tr>
                        <tr class="row-plateau">
                            <td><span class="nobr">$n = 5$</span></td>
                            <td style="color: #0369a1;"><span class="nobr">$11$</span></td>
                            <td style="color: #b45309;"><span class="nobr">$-1$</span></td>
                            <td style="font-weight: 700; color: #047857;"><span class="nobr">$10$</span></td>
                            <td style="text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: <span class="nobr">$-1$</span> cancels climb (<span class="nobr">$c_5 = c_4$</span>)</td>
                        </tr>
                    </tbody>
                </table>
            </div>"""

    return content.replace(old_table_snippet, new_table_snippet, 1)


def check_staged_changes() -> bool:
    """Return True if uncommitted changes exist in the git staging index."""
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return result.returncode != 0


def sync_git_repository(target_path: Path, script_path: Path) -> None:
    """Stage files, create the git commit, and push upstream."""
    commit_message = f"{COMMIT_SUBJECT}\n\n{COMMIT_BODY}"

    print(f"Staging {target_path.name} and {script_path.name}...")
    subprocess.run(["git", "add", str(target_path), str(script_path)], check=True)

    if not check_staged_changes():
        print("Staged files are already identical to HEAD. Nothing to commit.")
        return

    print("Creating git commit...")
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    print("Pushing to remote repository...")
    subprocess.run(["git", "push"], check=True)
    print("Done! Changes pushed successfully.")


if __name__ == "__main__":
    try:
        raw_html = TARGET_FILE.read_text(encoding="utf-8")
        html_with_styles = inject_responsive_table_styles(raw_html)
        final_html = upgrade_stepping_table_markup(html_with_styles)

        TARGET_FILE.write_text(final_html, encoding="utf-8")
        print(f"Successfully updated '{TARGET_FILE}'.")

        sync_git_repository(TARGET_FILE, SCRIPT_FILE)
    except subprocess.CalledProcessError as git_err:
        print(f"Git execution error: {git_err}", file=sys.stderr)
        sys.exit(1)
    except OSError as err:
        print(f"File system error: {err}", file=sys.stderr)
        sys.exit(1)
