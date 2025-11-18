import pandas as pd
import argparse

def load(path):
    return pd.read_csv(path)

def summarize_distribution(df, col):
    dist = df[col].value_counts(normalize=True) * 100
    txt = []
    for g, p in dist.items():
        txt.append(f"{g}: {p:.2f}%")
    return "\n".join(txt)

def summarize_hiring_rates(df, group, target):
    rates = df.groupby(group)[target].mean()
    txt = []
    for g, r in rates.items():
        txt.append(f"{g}: {r:.3f}")
    return "\n".join(txt)

def summarize_disparity(df, group, target):
    rates = df.groupby(group)[target].mean()
    base = rates.max()
    txt = []
    for g, r in rates.items():
        rel = r / base if base != 0 else 0
        txt.append(f"{g}: {rel:.3f}")
    return "\n".join(txt)

def generate_report(df, groups, target):
    lines = []
    lines.append("DIVERSITY GAP ANALYSIS REPORT")
    lines.append("----------------------------------")
    for g in groups:
        lines.append(f"\nDistribution for {g}:")
        lines.append(summarize_distribution(df, g))
        lines.append(f"\nHiring Rates for {g}:")
        lines.append(summarize_hiring_rates(df, g, target))
        lines.append(f"\nDisparity Levels for {g}:")
        lines.append(summarize_disparity(df, g, target))
        lines.append("\n----------------------------------")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--groups", nargs="*", default=["gender","race"])
    parser.add_argument("--target", default="hired")
    parser.add_argument("--output", default="report.txt")
    args = parser.parse_args()
    df = load(args.input)
    report = generate_report(df, args.groups, args.target)
    with open(args.output, "w") as f:
        f.write(report)
    print("report saved to:", args.output)

if __name__ == "__main__":
    main()
