import argparse
import os
import pandas as pd
import numpy as np

def load_csv(path):
    return pd.read_csv(path)

def basic_clean(df):
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    df.replace({np.nan: None}, inplace=True)
    df = df.drop_duplicates()
    return df

def infer_column_types(df):
    numeric = df.select_dtypes(include=["number"]).columns.tolist()
    object_cols = [c for c in df.columns if c not in numeric]
    return numeric, object_cols

def impute_missing(df, numeric_cols, categorical_cols):
    for c in numeric_cols:
        median = df[c].median()
        df[c] = df[c].fillna(median)
    for c in categorical_cols:
        df[c] = df[c].fillna("Unknown")
    return df

def standardize_columns(df):
    col_map = {}
    for c in df.columns:
        low = c.lower()
        low = low.replace(" ", "_")
        col_map[c] = low
    df.rename(columns=col_map, inplace=True)
    return df

def add_basic_metadata(df, source_path):
    df["_source_file"] = os.path.basename(source_path)
    df["_rows"] = len(df)
    return df

def validate_required_columns(df, required):
    missing = [c for c in required if c not in df.columns]
    return missing

def process_file(input_path, output_path, required_columns):
    df = load_csv(input_path)
    df = basic_clean(df)
    df = standardize_columns(df)
    numeric_cols, categorical_cols = infer_column_types(df)
    df = impute_missing(df, numeric_cols, categorical_cols)
    df = add_basic_metadata(df, input_path)
    missing = validate_required_columns(df, required_columns)
    result = {"cleaned_path": output_path, "missing_required_columns": missing}
    df.to_csv(output_path, index=False)
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--required", nargs="*", default=["candidate_id","gender","race","hired"])
    args = parser.parse_args()
    res = process_file(args.input, args.output, args.required)
    print("cleaned_file:", res["cleaned_path"])
    if res["missing_required_columns"]:
        print("missing_required_columns:", ",".join(res["missing_required_columns"]))
    else:
        print("all required columns present")

if __name__ == "__main__":
    main()
