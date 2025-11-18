
# **Diversity Gap Analysis in Hiring Trends**

This project performs a complete **diversity bias audit** on hiring datasets using Python.
It detects demographic imbalance, evaluates hiring fairness, visualizes disparities, and generates an automatic written report.

The pipeline processes raw CSV data → cleans it → analyzes bias → generates charts → creates a final report.

---

## **📌 Project Objectives**

* Identify potential **biases** in hiring decisions
* Analyze hiring rates across **gender**, **race**, and other demographic attributes
* Visualize workforce representation and disparity patterns
* Generate a final **Diversity Gap Report** for stakeholders
* Provide a reproducible **end-to-end data science workflow**

---

## **📁 Project Structure**

```
├── data_ingest.py
├── bias_analysis.py
├── visualize_bias.py
├── report_generator.py
├── run_pipeline.py
├── raw_hiring.csv
├── cleaned_hiring.csv (auto-generated)
├── charts/ (auto-generated)
│   ├── dist_gender.png
│   ├── hire_gender.png
│   ├── disp_gender.png
│   └── ...
├── bias_* (auto-generated analysis CSVs)
└── report.txt
```

---

## **⚙️ Installation**

Clone the repository and install dependencies:

```
pip install pandas matplotlib
```

No additional libraries required.

---

## **📥 Input Dataset Format**

Your `raw_hiring.csv` must contain demographic & hiring outcome details like:

```
candidate_id,gender,race,education_level,experience_years,hired,salary_expected
1,Male,White,Bachelor,3,1,60000
2,Female,Asian,Master,2,0,55000
...
```

**Required columns:**

* `candidate_id`
* `gender`
* `race`
* `hired`

Additional columns are allowed.

---

## **🚀 How to Run the Project**

### **1) Run Complete Pipeline (Recommended)**

```
python run_pipeline.py --raw raw_hiring.csv
```

This automatically:

* Cleans the raw dataset
* Generates cleaned_hiring.csv
* Creates all bias analysis CSVs
* Produces visualizations in `/charts`
* Outputs `report.txt`

---

### **2) Run Each Step Manually**

#### **Step 1 — Clean Data**

```
python data_ingest.py --input raw_hiring.csv --output cleaned_hiring.csv
```

#### **Step 2 — Bias Analysis**

```
python bias_analysis.py --input cleaned_hiring.csv --outprefix bias
```

#### **Step 3 — Visualize Charts**

```
python visualize_bias.py --input cleaned_hiring.csv --outdir charts
```

#### **Step 4 — Generate Final Report**

```
python report_generator.py --input cleaned_hiring.csv --output report.txt
```

---

## **📊 Outputs**

### ✔️ **Bias Analysis CSVs**

* `bias_hiring_rate_gender.csv`
* `bias_hiring_rate_race.csv`
* `bias_distribution_gender.csv`
* `bias_disparity_race.csv`
* etc.

### ✔️ **Charts**

* Hiring rate charts
* Representation distribution
* Disparity index graphs

### ✔️ **Final Report (`report.txt`)**

Contains:

* Representation summary
* Hiring rate differences
* Relative disparity (0–1 scale)
* Potential red flags & gaps

---

## **🧠 Insights & Use Cases**

This project helps organizations:

* Detect hiring inequalities
* Improve diversity & inclusion strategies
* Understand demographic hiring patterns
* Make fair and transparent HR decisions

---

## **📜 License**

MIT License — free to use and modify.


