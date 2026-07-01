import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose


def decompose_series(
    series: pd.Series,
    model: str = "additive",
    period: int = 30,
):
    """
    Perform seasonal decomposition.

    Parameters
    ----------
    series : pd.Series
        Closing price series.

    model : str
        additive or multiplicative.

    period : int
        Seasonal period.
    """

    series = series.dropna()

    decomposition = seasonal_decompose(
        series,
        model=model,
        period=period,
        extrapolate_trend="freq",
    )

    return decomposition