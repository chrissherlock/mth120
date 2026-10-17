#!/usr/bin/env python3
"""Apply remaining structural, CSS scoping, and pedagogical fixes to week2-lecture4.html."""

from pathlib import Path
import re
import sys


def apply_exact_replacement(content: str, old: str, new: str, label: str) -> str:
    if old not in content:
        print(f"[WARN] Target block not found for: {label}", file=sys.stderr)
        return content
    count = content.count(old)
    if count > 1:
        print(f"[WARN] Multiple matches ({count}) for: {label}; replacing first occurrence.", file=sys.stderr)
    else:
        print(f"[OK] Patched: {label}")
    return content.replace(old, new, 1)


def patch_lecture_file(filepath: Path) -> None:
    text = filepath.read_text(encoding="utf-8")

    # 1. Close the Archery Game flex container before Figure 4 (Section 1.4)
    old_archery_fig4 = """                    <p style="margin: 0.75rem 0 0 0; color: #334155; font-size: 0.95rem;">
                        If you have a reliable rule to produce a valid $N$ for <em>any</em> positive $\\epsilon$ the skeptic throws at you, you win the game—and the sequence converges to $L$!
                    </p>
                </div>

                <!-- DIAGRAM 4: CHALLENGE-RESPONSE SHRINKAGE COMPARISON -->
                <figure style="margin: 1.25rem 0; padding: 1.25rem 1.5rem; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px;">"""

    new_archery_fig4 = """                    <p style="margin: 0.75rem 0 0 0; color: #334155; font-size: 0.95rem;">
                        If you have a reliable rule to produce a valid $N$ for <em>any</em> positive $\\epsilon$ the skeptic throws at you, you win the game—and the sequence converges to $L$!
                    </p>
                </div>
            </div>

            <!-- DIAGRAM 4: CHALLENGE-RESPONSE SHRINKAGE COMPARISON -->
            <figure style="margin: 1.25rem 0; padding: 1.25rem 1.5rem; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px;">"""

    old_fig4_end = """                    <p style="margin: 0.6rem 0 0 0; font-size: 0.88rem; color: #64748b; line-height: 1.5;">
                        <strong>Quantifier ordering in action:</strong> You must wait for the skeptic to name <code style="color:#b45309;">ϵ</code> <em>first</em> before you can commit to <code style="color:#ef4444;">N</code>. As <code style="color:#b45309;">ϵ → 0</code>, the required cutoff <code style="color:#ef4444;">N</code> is pushed arbitrarily far to the right.
                    </p>
                </figure>
            </div>"""

    new_fig4_end = """                    <p style="margin: 0.6rem 0 0 0; font-size: 0.88rem; color: #64748b; line-height: 1.5;">
                        <strong>Quantifier ordering in action:</strong> You must wait for the skeptic to name <code style="color:#b45309;">ϵ</code> <em>first</em> before you can commit to <code style="color:#ef4444;">N</code>. As <code style="color:#b45309;">ϵ → 0</code>, the required cutoff <code style="color:#ef4444;">N</code> is pushed arbitrarily far to the right.
                    </p>
            </figure>"""

    text = apply_exact_replacement(text, old_archery_fig4, new_archery_fig4, "Un-nest Figure 4 from Archery flex container (open)")
    text = apply_exact_replacement(text, old_fig4_end, new_fig4_end, "Un-nest Figure 4 from Archery flex container (close)")

    # 2. Add bridge note to Section 1.6 (#epsilon-delta-suite) connecting eps-delta & eps-N
    old_suite_intro = """                  <p style="margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
                    Every rigorous functional limit proof follows the four-word structural spine:
                    <strong style="color: #0284c7;">Given</strong>,
                    <strong style="color: #d97706;">Choose</strong>,
                    <strong style="color: #475569;">Suppose</strong>, and
                    <strong style="color: #047857;">Check</strong>.
                    Select an archetype below to explore the core algebraic obstacle and its formal resolution.
                  </p>"""

    new_suite_intro = """                  <p style="margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
                    Every rigorous limit proof—whether bounding continuous inputs ($0 &lt; |x - a| &lt; \\delta$) or discrete sequence tails ($n &gt; N$)—follows the exact same four-word structural spine:
                    <strong style="color: #0284c7;">Given</strong>,
                    <strong style="color: #d97706;">Choose</strong>,
                    <strong style="color: #475569;">Suppose</strong>, and
                    <strong style="color: #047857;">Check</strong>.
                    Select an archetype below to explore the core algebraic obstacle (conjugates, polynomial bounding, or reciprocal moats) and its formal resolution.
                  </p>"""

    text = apply_exact_replacement(text, old_suite_intro, new_suite_intro, "Add eps-delta / eps-N bridge note in Section 1.6")

    # 3. Fix TOC link 3.3 to jump to the 3D Guide heading instead of skipping to the WebGL box
    old_toc_33 = """<li><a href="#corridor-3d-section" style="color: #0284c7; text-decoration: none;">3.3 Guide: Visualizing Convergence in 3D (The $\\epsilon$-Tube) <span style="font-size: 0.72rem; color: #0284c7; font-weight: 600;">[3D WebGL]</span></a></li>"""
    new_toc_33 = """<li><a href="#guide-3d-tube" style="color: #0284c7; text-decoration: none;">3.3 Guide: Visualizing Convergence in 3D (The $\\epsilon$-Tube) <span style="font-size: 0.72rem; color: #0284c7; font-weight: 600;">[3D WebGL]</span></a></li>"""

    old_h3_33 = """                <h3 style="color: #0f172a; font-size: 1.35rem; font-weight: 700; margin: 0 0 0.35rem 0; line-height: 1.3;">
                    Guide: Visualizing Convergence in 3D (The $\\epsilon$-Tube)
                </h3>"""
    new_h3_33 = """                <h3 id="guide-3d-tube" style="color: #0f172a; font-size: 1.35rem; font-weight: 700; margin: 0 0 0.35rem 0; line-height: 1.3;">
                    Guide: Visualizing Convergence in 3D (The $\\epsilon$-Tube)
                </h3>"""

    text = apply_exact_replacement(text, old_toc_33, new_toc_33, "Point TOC 3.3 to #guide-3d-tube")
    text = apply_exact_replacement(text, old_h3_33, new_h3_33, "Add id='guide-3d-tube' to 3.3 heading")

    # 4. Fix Midway Checkpoint Tile 3 (replace premature Section 4.1 recap with Section 3 recap)
    old_checkpoint_tile3 = """                    <!-- Section 3 Anchor -->
                    <div style="background: #ffffff; padding: 1.2rem; border-radius: 8px; border: 1px solid #e2e8f0;">
                        <div style="font-weight: 700; color: #0369a1; font-size: 0.95rem; margin-bottom: 0.4rem;">
                            3. The Elbow Room Principle
                        </div>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin: 0;">
                            You discovered that limit uniqueness is not a rule of grammar, but a geometric gift of distance ($d = |L - M| > 0$). Because distinct numbers have space between them, we can draw non-touching bubbles that force an adversarial contradiction.
                        </p>
                    </div>"""

    new_checkpoint_tile3 = """                    <!-- Section 3 Anchor -->
                    <div style="background: #ffffff; padding: 1.2rem; border-radius: 8px; border: 1px solid #e2e8f0;">
                        <div style="font-weight: 700; color: #0369a1; font-size: 0.95rem; margin-bottom: 0.4rem;">
                            3. The Scratchpad &amp; Tail Lock-In
                        </div>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin: 0;">
                            You learned the analyst's trade secret: work backward from $|a_n - L| &lt; \\epsilon$ on scrap paper to isolate $n &gt; g(\\epsilon)$, then set $N = \\lceil g(\\epsilon) \\rceil$ to seal the infinite tail inside the 2D ribbon or 3D containment pipe.
                        </p>
                    </div>"""

    text = apply_exact_replacement(text, old_checkpoint_tile3, new_checkpoint_tile3, "Fix Midway Checkpoint Tile 3 to recap Section 3")

    # 5. Replace hardcoded KaTeX HTML dump in Elbow Room Figure (Section 4.1)
    katex_dump_pattern = re.compile(
        r"Because distinct limits <span><span class=\"katex\">.*?creates an impassable water-moat with hazard boundaries\.",
        re.DOTALL,
    )
    clean_elbow_caption = (
        r"Because distinct limits $L \ne M$ sit separated by positive distance "
        r"$d = |L - M| > 0$, setting tolerance $\epsilon < \frac{d}{2}$ "
        r"creates an impassable water-moat with hazard boundaries."
    )
    if katex_dump_pattern.search(text):
        text = katex_dump_pattern.sub(lambda _: clean_elbow_caption, text, count=1)
        print("[OK] Patched: Replace raw KaTeX HTML dump in Elbow Room figure caption")
    else:
        print("[WARN] Target block not found for: KaTeX HTML dump in Elbow Room figure", file=sys.stderr)

    # 6. Scope CSS in Tail Invariance Widget (Section 4.2) and add mobile nav-panel media query
    old_ti_widget = """            <!-- ================================================================= -->
            <!-- WIDGET: TAIL INVARIANCE & TRUNCATION (DIRECTED NARRATIVE STEPPER) -->
            <!-- ================================================================= -->
            <div class="widget-box" style="margin: 2.5rem 0; padding: 1.5rem; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
                <style>
                    .widget-box .widget-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.25rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.85rem; }
                    .widget-box .widget-title { margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; letter-spacing: -0.01em; }
                    .widget-box .dim-toggles { display: flex; gap: 0.5rem; }
                    .widget-box .dim-btn { padding: 0.4rem 0.85rem; font-size: 0.82rem; font-weight: 600; border-radius: 6px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; cursor: pointer; transition: all 0.2s ease; }
                    .widget-box .dim-btn.active { background: #0284c7; color: #ffffff; border-color: #0284c7; box-shadow: 0 1px 2px rgba(2, 132, 199, 0.2); }
                    .widget-box .telemetry-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 0.65rem; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.75rem; margin-bottom: 1.25rem; }
                    .widget-box .telemetry-cell { display: flex; flex-direction: column; gap: 0.2rem; }
                    .widget-box .telemetry-label { font-size: 0.72rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.04em; }
                    .widget-box .telemetry-val { font-size: 0.88rem; font-weight: 700; color: #0f172a; font-variant-numeric: tabular-nums; }
                    .widget-box .canvas-wrap { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.5rem; margin-bottom: 1.25rem; overflow: hidden; }

                    /* STRICT SIDE-BY-SIDE NAVIGATION PANEL */
                    .widget-box .nav-panel { display: grid; grid-template-columns: auto 1fr; align-items: center; gap: 1.25rem; background: #f1f5f9; border-radius: 8px; padding: 0.85rem 1.15rem; margin-bottom: 1.25rem; }
                    .widget-box .nav-buttons { display: flex; gap: 0.5rem; flex-shrink: 0; white-space: nowrap; }
                    .widget-box .ti-btn { padding: 0.45rem 0.9rem; font-size: 0.85rem; font-weight: 600; border-radius: 6px; border: 1px solid #cbd5e1; background: #ffffff; color: #334155; cursor: pointer; transition: all 0.15s ease; }
                    .widget-box .ti-btn:hover:not(:disabled) { background: #f8fafc; border-color: #94a3b8; }
                    .widget-box .ti-btn:disabled { opacity: 0.45; cursor: not-allowed; }
                    .widget-box .ti-btn-primary { background: #0284c7; color: #ffffff; border-color: #0284c7; }
                    .widget-box .ti-btn-primary:hover:not(:disabled) { background: #0369a1; border-color: #0369a1; }
                    .widget-box .preview-desc { margin: 0; font-size: 0.9rem; line-height: 1.5; color: #334155; min-width: 0; }

                    .widget-box .panes-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; }
                    .widget-box .ti-pane { border-radius: 8px; padding: 1rem; border: 1px solid #e2e8f0; }
                    .widget-box .ti-pane-what { background: #f0fdf4; border-color: #bbf7d0; border-left: 4px solid #16a34a; }
                    .widget-box .ti-pane-why { background: #eff6ff; border-color: #bfdbfe; border-left: 4px solid #2563eb; }
                    .widget-box .ti-pane h4 { margin: 0 0 0.4rem 0; font-size: 0.82rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; }
                    .widget-box .ti-pane-what h4 { color: #15803d; }
                    .widget-box .ti-pane-why h4 { color: #1d4ed8; }
                    .widget-box .ti-pane-body { font-size: 0.88rem; line-height: 1.6; color: #1e293b; }"""

    new_ti_widget = """            <!-- ================================================================= -->
            <!-- WIDGET: TAIL INVARIANCE & TRUNCATION (DIRECTED NARRATIVE STEPPER) -->
            <!-- ================================================================= -->
            <div class="widget-box" id="tail-invariance-widget" style="margin: 2.5rem 0; padding: 1.5rem; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
                <style>
                    #tail-invariance-widget .widget-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.25rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.85rem; }
                    #tail-invariance-widget .widget-title { margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; letter-spacing: -0.01em; }
                    #tail-invariance-widget .dim-toggles { display: flex; gap: 0.5rem; }
                    #tail-invariance-widget .dim-btn { padding: 0.4rem 0.85rem; font-size: 0.82rem; font-weight: 600; border-radius: 6px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; cursor: pointer; transition: all 0.2s ease; }
                    #tail-invariance-widget .dim-btn.active { background: #0284c7; color: #ffffff; border-color: #0284c7; box-shadow: 0 1px 2px rgba(2, 132, 199, 0.2); }
                    #tail-invariance-widget .telemetry-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 0.65rem; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.75rem; margin-bottom: 1.25rem; }
                    #tail-invariance-widget .telemetry-cell { display: flex; flex-direction: column; gap: 0.2rem; }
                    #tail-invariance-widget .telemetry-label { font-size: 0.72rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.04em; }
                    #tail-invariance-widget .telemetry-val { font-size: 0.88rem; font-weight: 700; color: #0f172a; font-variant-numeric: tabular-nums; }
                    #tail-invariance-widget .canvas-wrap { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.5rem; margin-bottom: 1.25rem; overflow: hidden; }

                    /* STRICT SIDE-BY-SIDE NAVIGATION PANEL */
                    #tail-invariance-widget .nav-panel { display: grid; grid-template-columns: auto 1fr; align-items: center; gap: 1.25rem; background: #f1f5f9; border-radius: 8px; padding: 0.85rem 1.15rem; margin-bottom: 1.25rem; }
                    @media (max-width: 680px) { #tail-invariance-widget .nav-panel { grid-template-columns: 1fr; } }
                    #tail-invariance-widget .nav-buttons { display: flex; gap: 0.5rem; flex-shrink: 0; white-space: nowrap; }
                    #tail-invariance-widget .ti-btn { padding: 0.45rem 0.9rem; font-size: 0.85rem; font-weight: 600; border-radius: 6px; border: 1px solid #cbd5e1; background: #ffffff; color: #334155; cursor: pointer; transition: all 0.15s ease; }
                    #tail-invariance-widget .ti-btn:hover:not(:disabled) { background: #f8fafc; border-color: #94a3b8; }
                    #tail-invariance-widget .ti-btn:disabled { opacity: 0.45; cursor: not-allowed; }
                    #tail-invariance-widget .ti-btn-primary { background: #0284c7; color: #ffffff; border-color: #0284c7; }
                    #tail-invariance-widget .ti-btn-primary:hover:not(:disabled) { background: #0369a1; border-color: #0369a1; }
                    #tail-invariance-widget .preview-desc { margin: 0; font-size: 0.9rem; line-height: 1.5; color: #334155; min-width: 0; }

                    #tail-invariance-widget .panes-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; }
                    #tail-invariance-widget .ti-pane { border-radius: 8px; padding: 1rem; border: 1px solid #e2e8f0; }
                    #tail-invariance-widget .ti-pane-what { background: #f0fdf4; border-color: #bbf7d0; border-left: 4px solid #16a34a; }
                    #tail-invariance-widget .ti-pane-why { background: #eff6ff; border-color: #bfdbfe; border-left: 4px solid #2563eb; }
                    #tail-invariance-widget .ti-pane h4 { margin: 0 0 0.4rem 0; font-size: 0.82rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; }
                    #tail-invariance-widget .ti-pane-what h4 { color: #15803d; }
                    #tail-invariance-widget .ti-pane-why h4 { color: #1d4ed8; }
                    #tail-invariance-widget .ti-pane-body { font-size: 0.88rem; line-height: 1.6; color: #1e293b; }"""

    text = apply_exact_replacement(text, old_ti_widget, new_ti_widget, "Scope Tail Invariance Widget CSS to #tail-invariance-widget")

    # Add mobile stacking for .nav-panel in the other 3 widgets (#order-preservation-widget, #sync-widget, #reciprocal-moat-widget)
    for wid in ("#order-preservation-widget", "#sync-widget", "#reciprocal-moat-widget"):
        target_rule = f"{wid} .nav-panel {{ display: grid; grid-template-columns: auto 1fr; align-items: center; gap: 1.25rem; background: #f1f5f9; border-radius: 8px; padding: 0.85rem 1.15rem; margin-bottom: 1.25rem; }}"
        replacement_rule = (
            target_rule
            + f"\n                    @media (max-width: 680px) {{ {wid} .nav-panel {{ grid-template-columns: 1fr; }} }}"
        )
        text = apply_exact_replacement(text, target_rule, replacement_rule, f"Add mobile breakpoint for {wid} .nav-panel")

    # 7. Fix invalid SVG attribute shadow="..." and invalid HTML attribute font-family="..."
    text = apply_exact_replacement(
        text,
        '<rect x="440" y="138" width="200" height="44" rx="6" fill="#dc2626" shadow="0 4px 6px rgba(0,0,0,0.1)"/>',
        '<rect x="440" y="138" width="200" height="44" rx="6" fill="#dc2626" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.1))"/>',
        "Replace invalid SVG shadow attribute with filter='drop-shadow(...)'",
    )

    text = apply_exact_replacement(
        text,
        '<div style="margin: 2rem 0; padding: 1.75rem 2rem; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);" font-family="system-ui, -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif">',
        '<div style="margin: 2rem 0; padding: 1.75rem 2rem; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); font-family: system-ui, -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif;">',
        "Move stray font-family HTML attribute into style attribute",
    )

    # 8. Align phrasing in Midpoint Moat Worked Example (Section 4.7)
    text = apply_exact_replacement(
        text,
        "<strong>Test terms sequence:</strong> Let's look at the trajectory beginning past N = 2:",
        "<strong>Test terms sequence:</strong> Let's inspect the trajectory from milestone $N = 2$ onward ($n \\ge 2$):",
        "Align Midpoint Moat bullet 3 phrasing with n >= 2 diagram",
    )

    # 9. Condense duplicate post-widget denominator paragraphs in Section 5.5
    old_quotient_outro = """            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Notice the danger lurking in the denominator: $|b_n|$. If terms $b_n$ were allowed to flirt with zero, the fraction $\\frac{1}{|b_n|}$ would blow up to infinity!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Here again, Section 4 comes to our rescue. By the <strong>Preservation of Sign property</strong>, because $L \\neq 0$, there exists an index $N_0$ past which $|b_n| > \\frac{|L|}{2}$. Inverting this inequality flips the direction:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\\frac{1}{|b_n|} < \\frac{2}{|L|}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The dangerous denominator is now securely capped by a fixed constant! We substitute this bound into our expression:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\\left|\\frac{1}{b_n} - \\frac{1}{L}\\right| < \\frac{2}{|L|^2} |b_n - L|$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Because $|b_n - L|$ can be made arbitrarily small, the entire distance collapses below $\\epsilon$. The Algebraic Limit Laws form an airtight, beautiful system: each theorem rests securely on the foundational properties we established in the sections before it.
            </p>"""

    new_quotient_outro = """            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Substituting the reciprocal ceiling $\\frac{1}{|b_n|} &lt; \\frac{2}{|L|}$ (valid for all $n &gt; N_0$) into our distance formula replaces the volatile denominator with a fixed constant:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\\left|\\frac{1}{b_n} - \\frac{1}{L}\\right| = \\frac{|b_n - L|}{|b_n| \\cdot |L|} &lt; \\frac{2}{|L|^2} |b_n - L|$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                By choosing a second cutoff $N_1$ so that $|b_n - L| &lt; \\frac{\\epsilon |L|^2}{2}$ and taking the master horizon $N = \\max(N_0, N_1)$, the entire distance collapses strictly below $\\epsilon$. Together with the Product Law, this completes the Quotient Law—showing how each algebraic theorem rests securely on the structural properties established in Section 4. $\\blacksquare$
            </p>"""

    text = apply_exact_replacement(text, old_quotient_outro, new_quotient_outro, "Condense duplicate post-widget paragraphs in Section 5.5")

    filepath.write_text(text, encoding="utf-8")
    print(f"\nSuccessfully updated {filepath}")


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("week2-lecture4.html")
    if not target.exists():
        print(f"Error: {target} not found.", file=sys.stderr)
        sys.exit(1)
    patch_lecture_file(target)
