import pandas as pd

from statsmodels.graphics.tsaplots import (
    plot_acf,
    plot_pacf,
)

import matplotlib.pyplot as plt

def generate_acf(series: pd.Series, lags: int = 40):

    fig, ax = plt.subplots(figsize=(12, 4))

    plot_acf(
        series.dropna(),
        lags=lags,
        ax=ax,
        alpha=0.05,
    )

    ax.set_title("Autocorrelation Function (ACF)")

    return fig


def generate_pacf(series: pd.Series, lags: int = 40):

    fig, ax = plt.subplots(figsize=(12, 4))

    plot_pacf(
        series.dropna(),
        lags=lags,
        ax=ax,
        alpha=0.05,
        method="ywm",
    )

    ax.set_title("Partial Autocorrelation Function (PACF)")

    return fig