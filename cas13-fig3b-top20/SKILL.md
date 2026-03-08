---
name: cas13-fig3b-top20
description: Reproduce and customize CAS13 fig3b-style top20 relative activity figures and prediction-vs-activity correlation figures from iterative round data.
---

# CAS13 Fig3b Top20

Use this skill for CAS13/Cas12f iterative optimization visualizations.

## Primary Script

- `/nas/jhp/projects/bioinformatics/scripts/cas13/build_fig3b_top20_relative_activity.py`

## Outputs

- `/nas/jhp/projects/bioinformatics/results/figures/cas13/fig3b_top20_relative_activity/`

## Standard Run

```bash
python3 /nas/jhp/projects/bioinformatics/scripts/cas13/build_fig3b_top20_relative_activity.py
```

## Notes

- Includes Top20 per-round relative activity to WT pipeline.
- Includes selected-round prediction vs activity scatter/correlation outputs.
- Prefer SVG/PDF outputs for publication editing.

## Quick Examples

```bash
# 中文：生成 fig3b top20 相关全部图
python3 /nas/jhp/projects/bioinformatics/scripts/cas13/build_fig3b_top20_relative_activity.py

# English: regenerate and inspect stats table
python3 /nas/jhp/projects/bioinformatics/scripts/cas13/build_fig3b_top20_relative_activity.py
cat /nas/jhp/projects/bioinformatics/results/figures/cas13/fig3b_top20_relative_activity/top20_prediction_vs_activity_selected_rounds_stats.csv
```
