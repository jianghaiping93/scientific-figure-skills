---
name: scientific-figure-router
description: Route figure requests to the best available publication-grade plotting workflow (Prism family templates or CAS13-specific pipelines) based on data schema and user intent.
---

# Scientific Figure Router

Use this skill as the single entry point.

## Routing Rules

1. If request mentions `cas13`, `top20`, `relative activity`, `fig3b`:
   - Route to `cas13-fig3b-top20`.
2. If request mentions `sparsity`, `proteingym`, `non-proteingym`, `mutant count`:
   - Route to `cas13-proteingym-sparsity`.
3. If request mentions `round0`, `round14`, `embedding`, `landscape`, `dimensionality reduction`:
   - Route to `cas13-prediction-landscape`.
4. Otherwise:
   - Route to `prism-publication-templates`, select family by chart intent:
     - trend/timecourse -> `line`
     - categorical comparison -> `bar`
     - relationship/correlation -> `scatter`
     - distribution by groups -> `violin_box` or `distribution`
     - matrix/tolerance map -> `heatmap`

## Output Policy

- Default output: SVG + PDF.
- Fonts: prefer Arial-compatible sans-serif stack.
- White background, restrained colors, editable vector text.

## Quick Examples

```bash
# 中文：以统一入口调用 fig3b 流程（实际由路由判定）
python3 /nas/jhp/projects/bioinformatics/scripts/cas13/build_fig3b_top20_relative_activity.py

# English: generic data-driven route to Prism family plotting
python3 /nas/jhp/projects/bioinformatics/skills/high-standard-figure-skills/prism-publication-templates/scripts/plot_from_template_family.py \
  --input <data.csv> --family <scatter> --x <x_col> --y <y_col> --out <output.svg>
```
