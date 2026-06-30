import pandas as pd
from pmdarima import auto_arima


def train_auto_arima(
    series: pd.Series,
    seasonal: bool = False,
    stepwise: bool = True,
):
    """Train an Auto ARIMA model."""

    model = auto_arima(
        series,
        start_p=0,
        start_q=0,
        max_p=5,
        max_q=5,
        d=None,
        seasonal=seasonal,
        stepwise=stepwise,
        trace=False,
        error_action="ignore",
        suppress_warnings=True,
        information_criterion="aic",
        test="adf",
    )

    return model


def forecast_auto_arima(model, periods=30):
    """Forecast future values."""
    return model.predict(n_periods=periods)


def train_test_split_series(
    series: pd.Series,
    test_size: float =0.2,
):
    """Split a time series while preserving order."""

    split = int(len(series) * (1 - test_size))

    train = series.iloc[:split]
    test = series.iloc[split:]

    train = train.asfreq("B").ffill()
    test = test.asfreq("B").ffill()

    return train, test


def Auto_fit_and_forecast(
    series: pd.Series,
    test_size: float =0.2,
):
    """
    Split the series, fit Auto ARIMA on training data,
    and predict the test period.
    """

    train, test = train_test_split_series(series, test_size)

    model = train_auto_arima(train)

    predictions = model.predict(n_periods=len(test))

    predictions = pd.Series(
        predictions,
        index=test.index,
        name="Prediction",
    )

    return train, test, predictions, model

def best_parameter(model):
    '''returns the best value of p , q and d '''
    return model.order

def model_summary(model):
    '''returns the model summary '''
    return model.summary()

def get_aic(model):
    return model.aic()

def get_bic(model):
    return model.bic()