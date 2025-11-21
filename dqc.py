import pandas as pd
import os

DATA_FILE = "data/international_matches.csv"
REPORT_FILE = "reports/data_quality_report.html"

df = pd.read_csv(DATA_FILE)
report = {}

report["missing_values"] = df.isnull().sum().to_dict()
report["duplicates"] = int(df.duplicated().sum())
report["dtypes"] = df.dtypes.astype(str).to_dict()
report["summary"] = df.describe(include="all").to_html()

html = f"""
<h1>Data Quality Report</h1>
<h2>Missing Values</h2><pre>{report['missing_values']}</pre>
<h2>Duplicates</h2><pre>{report['duplicates']}</pre>
<h2>Data Types</h2><pre>{report['dtypes']}</pre>
<h2>Summary Statistics</h2>{report['summary']}
"""
os.makedirs("reports", exist_ok=True)
with open(REPORT_FILE, "w") as f:
    f.write(html)

print(f"Report generated: {REPORT_FILE}")
