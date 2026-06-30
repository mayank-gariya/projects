from typing import Tuple

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def train_arima(series: pd.Series,order: Tuple[int, int, int] = (5, 1, 0)):
    """
    Train an ARIMA model.

    Parameters
    ----------
    series : pd.Series Closing price series.
    order : tuple (p,d,q)
    
    Returns
    -------
    model_fit Trained ARIMA model.
    """
    series = series.asfreq("B").ffill()
    
    model = ARIMA(
        series,
        order=order,
    )

    model_fit = model.fit()

    return model_fit


def forecast_arima(model,periods: int = 30):
    """
    Forecast future prices.

    Parameters
    ----------
    model
        Trained ARIMA model.

    periods : int
        Number of future periods.

    Returns
    -------
    pd.Series
        Forecast values.
    """

    forecast = model.forecast(steps=periods)

    return forecast


def train_test_split_series(series: pd.Series,test_size: float = 0.2):
    
    """
    Split a time series into train and test sets.

    Parameters
    ----------
    series : pd.Series

    test_size : float

    Returns
    -------
    train, test
    """

    split_index = int(len(series) * (1 - test_size))

    train = series.iloc[:split_index]
    test = series.iloc[split_index:]
    
    train = train.asfreq("B").ffill()
    test = test.asfreq("B").ffill()

    return train, test


def fit_and_forecast(series: pd.Series,order=(5, 1, 0),test_size=0.2):
    """
    Train ARIMA and forecast on test data.

    Returns
    -------
    train
    test
    predictions
    model
    """

    train, test = train_test_split_series(
        series,
        test_size,
    )

    model = train_arima(
        train,
        order,
    )

    predictions = model.forecast(
        steps=len(test)
    )

    predictions.index = test.index

    return (
        train,
        test,
        predictions,
        model,
    )