# Customer Churn Prediction

A compact Streamlit dashboard to predict whether a customer is likely to churn using a pre-trained scikit-learn model.

## What this is
- Simple web UI (Streamlit) to enter customer attributes and get a churn prediction.
- Model and example dataset included:
  - model.pkl — trained Pipeline (StandardScaler + LogisticRegression)
  - customer_churn_dataset-testing-master.csv — sample dataset used for development

## Features
- Quick, form-based input for common customer fields (age, gender, tenure, usage, payments, subscription type, etc.)
- Instant prediction: "churn" or "no churn"
- Portable: single-file app (app.py) + model.pkl

## Requirements
- Python 3.8+
- Recommended packages:
  - streamlit
  - scikit-learn
  - pandas
  - numpy
- (Install via pip) Example:
  pip install streamlit scikit-learn pandas numpy

## Quick start
1. Clone the repo or download the `customer churn prediction` folder.
2. Ensure `model.pkl` is in the same folder as `app.py`.
3. Run the app:
   streamlit run "customer churn prediction/app.py"
4. Open the local URL shown in the terminal, fill the form and click "Predict Churn".

## Notes & tips
- The app expects the model input order to match the pipeline used to train `model.pkl`. Do not change field order without retraining.
- The current UI is minimal — consider adding input validation, clearer labels, and probability output for more actionable insights.
- If you plan to deploy, include a requirements.txt and pin package versions for reproducibility.

## Data & model
- Sample dataset: `customer_churn_dataset-testing-master.csv`
- Trained model: `model.pkl` (scikit-learn Pipeline)

## License & contact
- Add your preferred license file (e.g., MIT) if you want to share this publicly.
- Questions or improvements: open an issue or contact the repository owner.
