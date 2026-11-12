# Ankonisaho Seabo | Data Analytics Portfolio
**Data Analytics • SQL • Python • Machine Learning • Energy Insights**

This portfolio contains three end-to-end demonstration projects:
1. Retail sales analysis (SQL, KPI summaries, charts and written findings)
2. Customer churn prediction (preprocessing, Random Forest, evaluation and limitations)
3. Energy demand analysis (hourly patterns, temperature relationship and recommendations)

> **Data transparency:** all included datasets are generated synthetically for portfolio practice. Findings and model metrics are illustrative and must not be presented as real company results.

## Skills demonstrated
- Python: pandas, NumPy, matplotlib, scikit-learn
- SQL: aggregation, grouping, date functions, analytical queries
- Data preparation, exploratory analysis, visualization, metrics interpretation
- Business writing, limitations, reproducibility and responsible modeling

## Project map
- `project_1_retail/` — CSV, SQL script, chart outputs, findings
- `project_2_churn/` — customer data, model training script, evaluation metrics, confusion matrix, feature importance
- `project_3_energy/` — hourly dataset, analysis script, charts, written findings

## Run locally
Python 3.10+ recommended.
```bash
pip install pandas numpy matplotlib scikit-learn
cd project_2_churn
python train_model.py
cd ../project_3_energy
python analysis.py
```
Retail SQL is SQLite-compatible; load `data/retail_sales.csv` into a table named `retail_sales`, then execute `analysis.sql`.

## Suggested GitHub presentation
Create a public repository named `ankonisaho-seabo-data-analytics-portfolio`, upload the folders, and pin this repository on your profile. Replace synthetic data with permitted real datasets as you gain experience, add dashboard versions (Power BI/Tableau), and document each project with screenshots and a short demo video.
