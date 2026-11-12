# Customer Churn Prediction — Evaluation
Model: Random Forest classifier; 75/25 stratified train/test split; class weighting; fixed random seed 42.
Dataset: 1,800 synthetic customers. Target prevalence: 13.6%.

| Metric | Test result |
|---|---:|
| Accuracy | 0.789 |
| Precision | 0.282 |
| Recall | 0.361 |
| F1 | 0.317 |
| ROC-AUC | 0.694 |

## Interpretation
Accuracy is not sufficient by itself; precision and recall describe the trade-off in identifying customers who churn. ROC-AUC measures ranking discrimination. The confusion matrix and class report are included in outputs.

## Limitations & responsible use
- This is a synthetic demonstration dataset with intentionally generated relationships; metrics are not evidence of performance on a real company's customers.
- Validate with a real, time-based holdout and compare against a baseline before deployment.
- Use predictions to prioritize supportive retention offers, not to deny service or make unfair decisions.
- Monitor drift, calibration, and subgroup performance.
