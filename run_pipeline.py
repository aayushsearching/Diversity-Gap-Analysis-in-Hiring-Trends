import os
import argparse

def run_clean(input_path, cleaned_path):
    cmd = f"python data_ingest.py --input \"{input_path}\" --output \"{cleaned_path}\""
    os.system(cmd)

def run_analysis(cleaned_path, prefix):
    cmd = f"python bias_analysis.py --input \"{cleaned_path}\" --outprefix \"{prefix}\""
    os.system(cmd)

def run_visuals(cleaned_path, outdir):
    cmd = f"python visualize_bias.py --input \"{cleaned_path}\" --outdir \"{outdir}\""
    os.system(cmd)

def run_report(cleaned_path, output):
    cmd = f"python report_generator.py --input \"{cleaned_path}\" --output \"{output}\""
    os.system(cmd)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", required=True)
    parser.add_argument("--cleaned", default="cleaned_hiring.csv")
    parser.add_argument("--charts", default="charts")
    parser.add_argument("--analysis_prefix", default="bias")
    parser.add_argument("--report", default="report.txt")
    args = parser.parse_args()
    run_clean(args.raw, args.cleaned)
    run_analysis(args.cleaned, args.analysis_prefix)
    run_visuals(args.cleaned, args.charts)
    run_report(args.cleaned, args.report)
    print("pipeline completed")

if __name__ == "__main__":
    main()
