---
name: cas13-proteingym-sparsity
description: Build publication-grade ProteinGym and non-ProteinGym sparsity landscape figures, tables, and type-stratified summaries for CAS13 project.
---

# CAS13 Protein Sparsity

Use this skill for sparsity analysis and figure generation across ProteinGym/non-ProteinGym datasets.

## Primary Script

- `/nas/jhp/projects/bioinformatics/docs/references/蛋白稀疏度_ref/build_non_proteingym_sparsity_analysis.py`

## Standard Run

```bash
python3 /nas/jhp/projects/bioinformatics/docs/references/蛋白稀疏度_ref/build_non_proteingym_sparsity_analysis.py
```

## Key Outputs

- `/nas/jhp/projects/bioinformatics/results/figures/cas13/proteingym/non_proteingym_sparsity_vs_mutant_count_by_type.svg`
- `/nas/jhp/projects/bioinformatics/results/figures/cas13/proteingym/non_proteingym_sparsity_vs_mutant_count_data.csv`
- `/nas/jhp/projects/bioinformatics/results/figures/cas13/proteingym/non_proteingym_dataset_fetch_status.csv`

## Notes

- Style targets restrained Science-like palette, white background, vector-first export.

## Quick Examples

```bash
# 中文：重建 non-ProteinGym 稀疏度图和统计表
python3 /nas/jhp/projects/bioinformatics/docs/references/蛋白稀疏度_ref/build_non_proteingym_sparsity_analysis.py

# English: build and view integrated protein table
python3 /nas/jhp/projects/bioinformatics/docs/references/蛋白稀疏度_ref/build_non_proteingym_sparsity_analysis.py
cat /nas/jhp/projects/bioinformatics/results/figures/cas13/proteingym/non_proteingym_all_proteins_integrated_table.csv | head
```
