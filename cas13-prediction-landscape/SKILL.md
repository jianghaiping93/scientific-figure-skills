---
name: cas13-prediction-landscape
description: Generate round-level prediction landscape embeddings (e.g., round0 and round14) from mutant prediction tables with publication-grade styling.
---

# CAS13 Prediction Landscape

Use this skill for dimensionality-reduction landscape figures from round prediction files.

## Primary Script

- `/nas/jhp/projects/bioinformatics/scripts/cas13/build_round_prediction_landscape.py`

## Standard Run

```bash
python3 /nas/jhp/projects/bioinformatics/scripts/cas13/build_round_prediction_landscape.py
```

## Inputs

- `/nas/jhp/projects/bioinformatics/data/cas13/模拟迭代过程/cas12f/r16_ts20_cv5_cosine_mt20_ensemble_demo_ensemble/round0.csv`
- `/nas/jhp/projects/bioinformatics/data/cas13/模拟迭代过程/cas12f/r16_ts20_cv5_cosine_mt20_ensemble_demo_ensemble/round14.csv`

## Key Outputs

- `/nas/jhp/projects/bioinformatics/results/figures/cas13/fig_prediction_landscape_round0_round14/prediction_landscape_round0_round14.svg`
- `/nas/jhp/projects/bioinformatics/results/figures/cas13/fig_prediction_landscape_round0_round14/prediction_landscape_round0.svg`
- `/nas/jhp/projects/bioinformatics/results/figures/cas13/fig_prediction_landscape_round0_round14/prediction_landscape_round14.svg`
