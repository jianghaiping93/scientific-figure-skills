#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def apply_publication_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "DejaVu Sans", "Liberation Sans"],
            "axes.linewidth": 0.8,
            "axes.facecolor": "white",
            "figure.facecolor": "white",
            "axes.labelsize": 9,
            "axes.titlesize": 10,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "svg.fonttype": "none",
        }
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build publication-grade figure from template family")
    p.add_argument("--input", required=True, help="input csv/tsv file")
    p.add_argument("--family", required=True, choices=["line", "bar", "scatter", "violin_box", "heatmap", "distribution"])
    p.add_argument("--x", required=True, help="x column")
    p.add_argument("--y", required=True, help="y column")
    p.add_argument("--group", default=None, help="optional grouping column")
    p.add_argument("--title", default="")
    p.add_argument("--xlabel", default=None)
    p.add_argument("--ylabel", default=None)
    p.add_argument("--out", required=True, help="output figure path (.svg/.pdf/.png)")
    p.add_argument("--sep", default=",", help="separator, default comma")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    apply_publication_style()

    path = Path(args.input)
    df = pd.read_csv(path, sep=args.sep)
    if args.x not in df.columns or args.y not in df.columns:
        raise ValueError(f"Missing required columns: {args.x}, {args.y}")

    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    palette = sns.color_palette("Blues", n_colors=8)

    if args.family == "line":
        if args.group and args.group in df.columns:
            sns.lineplot(data=df, x=args.x, y=args.y, hue=args.group, marker="o", linewidth=1.2, ax=ax)
        else:
            sns.lineplot(data=df, x=args.x, y=args.y, marker="o", color=palette[-2], linewidth=1.2, ax=ax)
    elif args.family == "bar":
        sns.barplot(data=df, x=args.x, y=args.y, hue=args.group if args.group in df.columns else None, palette="Blues", ax=ax)
    elif args.family == "scatter":
        sns.scatterplot(data=df, x=args.x, y=args.y, hue=args.group if args.group in df.columns else None, palette="viridis", s=24, edgecolor="black", linewidth=0.2, ax=ax)
    elif args.family == "violin_box":
        sns.violinplot(data=df, x=args.x, y=args.y, hue=args.group if args.group in df.columns else None, inner=None, linewidth=0.7, palette="Blues", ax=ax)
        sns.stripplot(data=df, x=args.x, y=args.y, hue=args.group if args.group in df.columns else None, dodge=True if args.group and args.group in df.columns else False, color="black", size=2.0, alpha=0.45, ax=ax)
    elif args.family == "heatmap":
        table = df.pivot_table(index=args.y, columns=args.x, values=args.group if args.group in df.columns else args.y, aggfunc="mean")
        sns.heatmap(table, cmap="RdBu_r", center=0, linewidths=0.25, linecolor="white", ax=ax, cbar_kws={"shrink": 0.65})
    elif args.family == "distribution":
        sns.histplot(data=df, x=args.y, hue=args.group if args.group in df.columns else None, bins=30, alpha=0.45, element="step", ax=ax)

    ax.set_title(args.title)
    ax.set_xlabel(args.xlabel if args.xlabel is not None else args.x)
    ax.set_ylabel(args.ylabel if args.ylabel is not None else args.y)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)


if __name__ == "__main__":
    main()
