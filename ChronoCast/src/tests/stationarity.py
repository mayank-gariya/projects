import pandas as pd
from statsmodels.tsa.stattools import adfuller , kpss
import warnings
from statsmodels.tools.sm_exceptions import InterpolationWarning

warnings.filterwarnings(
    "ignore",
    category=InterpolationWarning,
)


def adf_test(series: pd.Series) -> dict:
    """
    Perform Augmented Dickey-Fuller Test.
    """
    
    result = adfuller(series.dropna())
    
    return {
        "Test Statistic": result[0],
        "p-value": result[1],
        "Lags Used": result[2],
        "Observations": result[3],
        "Critical Values": result[4],
    }

def kpss_test(series: pd.Series) -> dict:
    """
    Perform KPSS Test.
    """
    
    statistic, p_value, lags, critical = kpss(
        series.dropna(),
        regression="c",
        nlags="auto",
    )

    return {
        "Test Statistic": statistic,
        "p-value": p_value,
        "Lags Used": lags,
        "Critical Values": critical,
    }
    
def interpret_adf(result: dict) -> str:
    """
    Interpret ADF test.
    """

    if result["p-value"] < 0.05:
        return "✅ The series is stationary."

    return "❌ The series is non-stationary."

def interpret_kpss(result: dict) -> str:
    """
    Interpret KPSS test.
    """

    if result["p-value"] < 0.05:
        return "❌ The series is non-stationary."

    return "✅ The series is stationary."

    