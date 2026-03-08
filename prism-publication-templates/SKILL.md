---
name: prism-publication-templates
description: Convert Prism template families (1-111 templates) into vibe-coding figure workflows. Use this when user provides tabular data and needs publication-grade line/bar/scatter/violin/heatmap/distribution figures consistent with Prism-style layouts.
---

# Prism Publication Templates

Use this skill when the request is: "给我一个高标准发表图" and the user provides CSV/TSV data.

## Workflow

1. Inspect template catalog: `references/prism_template_catalog.csv`.
2. Pick template family: `line`, `bar`, `scatter`, `violin_box`, `heatmap`, `distribution`.
3. Build figure with `scripts/plot_from_template_family.py`.
4. Prefer SVG/PDF output for editing and publication.

## Command

```bash
python3 skills/high-standard-figure-skills/prism-publication-templates/scripts/plot_from_template_family.py \
  --input <data.csv> \
  --family <line|bar|scatter|violin_box|heatmap|distribution> \
  --x <x_col> \
  --y <y_col> \
  --group <optional_group_col> \
  --title "<title>" \
  --xlabel "<x label>" \
  --ylabel "<y label>" \
  --out <output.svg>
```

## Template Source

- Extracted Prism templates are in:
  - `/nas/jhp/projects/bioinformatics/docs/references/1-111号模板/1-111号模板`
- The `references/prism_template_catalog.csv` maps template id/title to family.

## Quick Examples

```bash
# 中文：按模板家族快速作图（柱状图）
python3 /nas/jhp/projects/bioinformatics/skills/high-standard-figure-skills/prism-publication-templates/scripts/plot_from_template_family.py \
  --input /nas/jhp/projects/bioinformatics/results/figures/cas13/proteingym/non_proteingym_sparsity_vs_mutant_count_data.csv \
  --family bar \
  --x protein_type \
  --y total_mutations \
  --out /nas/jhp/projects/bioinformatics/results/figures/cas13/proteingym/example_bar.svg

# English: scatter with group
python3 /nas/jhp/projects/bioinformatics/skills/high-standard-figure-skills/prism-publication-templates/scripts/plot_from_template_family.py \
  --input /nas/jhp/projects/bioinformatics/results/figures/cas13/proteingym/non_proteingym_sparsity_vs_mutant_count_data.csv \
  --family scatter \
  --x sparse_fitness \
  --y total_mutations \
  --group protein_type \
  --xlabel "Sparsity" \
  --ylabel "Mutant count" \
  --out /nas/jhp/projects/bioinformatics/results/figures/cas13/proteingym/example_scatter.svg
```
