import pandas as pd
import argparse
import matplotlib.pyplot as plt

def load(path):
    return pd.read_csv(path)

def plot_distribution(df, column, outpath):
    counts = df[column].value_counts()
    plt.figure(figsize=(6,4))
    counts.plot(kind="bar")
    plt.title(f"Distribution: {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def plot_hiring_rate(df, group_col, target_col, outpath):
    rates = df.groupby(group_col)[target_col].mean()
    plt.figure(figsize=(6,4))
    rates.plot(kind="bar")
    plt.title(f"Hiring Rate by {group_col}")
    plt.xlabel(group_col)
    plt.ylabel("Hiring Rate")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def plot_disparity(df, group_col, target_col, outpath):
    rates = df.groupby(group_col)[target_col].mean()
    base = rates.max()
    rel = rates / base
    plt.figure(figsize=(6,4))
    rel.plot(kind="bar")
    plt.title(f"Relative Disparity: {group_col}")
    plt.xlabel(group_col)
    plt.ylabel("Relative to Highest Hiring Rate")
    plt.ylim(0,1.2)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--groups", nargs="*", default=["gender","race"])
    parser.add_argument("--target", default="hired")
    parser.add_argument("--outdir", default="charts")
    args = parser.parse_args()
    import os
    os.makedirs(args.outdir, exist_ok=True)
    df = load(args.input)
    for g in args.groups:
        plot_distribution(df, g, f"{args.outdir}/dist_{g}.png")
        plot_hiring_rate(df, g, args.target, f"{args.outdir}/hire_{g}.png")
        plot_disparity(df, g, args.target, f"{args.outdir}/disp_{g}.png")
    print("charts generated in:", args.outdir)

if __name__ == "__main__":
    main()
