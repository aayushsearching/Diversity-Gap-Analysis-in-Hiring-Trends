import pandas as pd
import argparse

def load_data(path):
    return pd.read_csv(path)

def compute_group_stats(df, group_cols, target_col):
    tables = {}
    for g in group_cols:
        t = df.groupby(g)[target_col].mean().reset_index()
        t.columns = [g, "hiring_rate"]
        tables[g] = t
    return tables

def count_distribution(df, group_cols):
    dist = {}
    for g in group_cols:
        d = df[g].value_counts(normalize=True).reset_index()
        d.columns = [g, "percentage"]
        dist[g] = d
    return dist

def disparity_index(rate_a, rate_b):
    if rate_b == 0:
        return None
    return round(rate_a / rate_b, 3)

def compute_disparity(df, group_cols, target_col):
    results = {}
    for g in group_cols:
        t = df.groupby(g)[target_col].mean()
        base_group = t.idxmax()
        base_rate = t.max()
        out = []
        for grp, rate in t.items():
            d = disparity_index(rate, base_rate)
            out.append({"group": grp, "hiring_rate": round(rate, 3),"relative_to_best": d})
        results[g] = pd.DataFrame(out)
    return results

def export_results(tables, path_prefix):
    for name, table in tables.items():
        out = f"{path_prefix}_{name}.csv"
        table.to_csv(out, index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--target", default="hired")
    parser.add_argument("--groups", nargs="*", default=["gender","race"])
    parser.add_argument("--outprefix", default="analysis")
    args = parser.parse_args()
    df = load_data(args.input)
    hire_stats = compute_group_stats(df, args.groups, args.target)
    dist = count_distribution(df, args.groups)
    disp = compute_disparity(df, args.groups, args.target)
    all_tables = {}
    all_tables.update({f"hiring_rate_{k}": v for k, v in hire_stats.items()})
    all_tables.update({f"distribution_{k}": v for k, v in dist.items()})
    all_tables.update({f"disparity_{k}": v for k, v in disp.items()})
    export_results(all_tables, args.outprefix)
    print("generated:", len(all_tables), "files")

if __name__ == "__main__":
    main()
