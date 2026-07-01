"""
Forecast Evaluation Module
--------------------------

Contains evaluation metrics used to compare forecasting models.
"""

import numpy as np
import pandas as pd

from sklearn.metrics import mean_absolute_error,mean_squared_error,mean_absolute_percentage_error,r2_score

def calculate_metrics(actual:pd.Series,predicted:pd.Series)->dict:
    """Calculate forecasting evaluation metrics."""
    
    actual = np.array(actual)
    predicted = np.array(predicted)
    
    mae = mean_absolute_error(actual,predicted)
    mse = mean_squared_error(actual,predicted)
    
    rmse = np.sqrt(mse)
    
    mape = mean_absolute_percentage_error(actual,predicted) * 100
    
    r2 = r2_score(actual,predicted)
    
    return {
        "MAE": round(mae, 4),
        "RMSE": round(rmse, 4),
        "MAPE (%)": round(mape, 2),
        "R² Score": round(r2, 4),
    }

def metrics_dataframe(metrics: dict) -> pd.DataFrame:
    """
    Convert metrics dictionary into a dataframe.
    """

    return pd.DataFrame(
        {
            "Metric": list(metrics.keys()),
            "Value": list(metrics.values()),
        }
    )
    
def compare_models(results: dict) -> pd.DataFrame:
    """Compare multiple forecasting models."""
    
    return (
        pd.DataFrame(results)
        .T
        .sort_values("RMSE")
        .reset_index()
        .rename(columns={"index": "Model"})
    )

def best_model(results: dict):
    """
    Return the best model based on RMSE.
    """

    comparison = compare_models(results)

    return comparison.iloc[0]