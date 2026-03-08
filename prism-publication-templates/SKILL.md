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
