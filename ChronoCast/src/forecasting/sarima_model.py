from typing import Tuple, Optional

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_test_split_series(series: pd.Series, test_size: float = 0.2):
    """
    Split a time series into train and test sets (preserving time order).

    Parameters
    ----------
    series : pd.Series
    test_size : float

    Returns
    -------
    train, test : pd.Series
    """
    split_index = int(len(series) * (1 - test_size))
    train = series.iloc[:split_index]
    test = series.iloc[split_index:]
    # ensure business-day frequency and fill missing
    train = train.asfreq("B").ffill()
    test = test.asfreq("B").ffill()
    return train, test

def train_sarima(
    series: pd.Series,
    order: Tuple[int, int, int] = (1, 1, 1),
    seasonal_order: Tuple[int, int, int, int] = (1, 1, 1, 7),
    enforce_stationarity: bool = False,
    enforce_invertibility: bool = False,
):
    """
    Train a SARIMA (Seasonal ARIMA) model using SARIMAX.

    Parameters
    ----------
    series : pd.Series
        Time series data.
    order : tuple (p,d,q) – non‑seasonal ARIMA order.
    seasonal_order : tuple (P,D,Q,s) – seasonal order and period.
    enforce_stationarity, enforce_invertibility : bool
        Passed to SARIMAX to relax constraints if needed.

    Returns
    -------
    model_fit : SARIMAXResultsWrapper
        Trained SARIMA model.
    """
    series = series.asfreq("B").ffill()

    model = SARIMAX(
        series,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=enforce_stationarity,
        enforce_invertibility=enforce_invertibility,
    )
    model_fit = model.fit(disp=False)
    return model_fit


def forecast_sarima(model, periods: int = 30) -> pd.Series:
    """
    Forecast future values from a trained SARIMA model.

    Parameters
    ----------
    model : SARIMAXResultsWrapper
        Trained SARIMA model.
    periods : int
        Number of future steps.

    Returns
    -------
    pd.Series
        Forecast values.
    """
    forecast = model.forecast(steps=periods)
    return forecast


def fit_and_forecast_sarima(
    series: pd.Series,
    order=(1, 1, 1),
    seasonal_order=(1, 1, 1, 7),
    test_size=0.2,
):
    """
    Train SARIMA on training set, forecast on test set.

    Returns
    -------
    train : pd.Series
    test : pd.Series
    predictions : pd.Series (aligned with test index)
    model : SARIMAXResultsWrapper
    """
    train, test = train_test_split_series(series, test_size)
    model = train_sarima(train, order, seasonal_order)
    predictions = model.forecast(steps=len(test))
    predictions.index = test.index
    return train, test, predictions, model