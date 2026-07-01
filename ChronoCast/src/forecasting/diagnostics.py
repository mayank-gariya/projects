import numpy as np
import pandas as pd
import plotly.graph_objects as go

from scipy.stats import jarque_bera
from statsmodels.graphics.tsaplots import acf, pacf
from statsmodels.stats.diagnostic import acorr_ljungbox

from scipy.stats import probplot

def residuals(actual: pd.Series, predicted: pd.Series):
    """
    Compute residuals.
    Residual = Actual - Prediction
    """

    return actual - predicted

def ljung_box_test(residual, lags=10):
    """Perform Ljung-Box test."""

    result = acorr_ljungbox(
        residual,
        lags=[lags],
        return_df=True
    )

    return result

def jarque_bera_test(residual):
    """Test whether residuals are normally distributed."""

    statistic, pvalue = jarque_bera(residual)

    return {
        "Statistic": round(statistic, 4),
        "P-value": round(pvalue, 4)
    }

def diagnostic_summary(actual, predicted):
    """
    Complete statistical diagnostics.
    """

    res = residuals(actual, predicted)
    jb = jarque_bera_test(res)
    lb = ljung_box_test(res)
    lb_p = float(lb["lb_pvalue"].iloc[0])

    return {
        
        "Residual Mean": round(res.mean(), 4),
        "Residual Std": round(res.std(), 4),
        "Jarque-Bera": jb["Statistic"],
        "JB P-value": jb["P-value"],
        "Ljung-Box P-value": round(lb_p, 4),

        "Residuals Normal":
            "Yes" if jb["P-value"] > 0.05 else "No",

        "White Noise":
            "Yes" if lb_p > 0.05 else "No",

    }
    

def residual_plot(actual, predicted):

    res = residuals(actual, predicted)

    fig = go.Figure()
    fig.add_trace(

        go.Scatter(
            x=res.index,
            y=res,
            mode="lines",
            name="Residual",
        )
    )

    fig.add_hline(
        y=0,
        line_dash="dash"
    )

    fig.update_layout(
        title="Residual Plot",
        template="plotly_white",
        height=500,
        xaxis_title="Date",
        yaxis_title="Residual",
    )

    return fig

def residual_histogram(actual, predicted):

    res = residuals(actual, predicted)
    fig = go.Figure()

    fig.add_histogram(
        x=res,
        nbinsx=40,
        name="Residual",
    )

    fig.update_layout(
        title="Residual Distribution",
        template="plotly_white",
        height=500,
        xaxis_title="Residual",
        yaxis_title="Frequency",
    )

    return fig

def qq_plot(actual, predicted):

    residual = actual - predicted
    residual = residual.dropna()

    # Compute theoretical and ordered sample quantiles
    (theoretical_quantiles, ordered_values), (slope, intercept, r) = probplot(
        residual,
        dist="norm",
        fit=True,
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=theoretical_quantiles,
            y=ordered_values,
            mode="markers",
            name="Residuals",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=theoretical_quantiles,
            y=slope * theoretical_quantiles + intercept,
            mode="lines",
            name="Reference Line",
        )
    )

    fig.update_layout(
        title=f"Q-Q Plot (Correlation = {r:.4f})",
        template="plotly_white",
        height=550,
        xaxis_title="Theoretical Quantiles",
        yaxis_title="Sample Quantiles",
        hovermode="closest",
    )

    return fig


def acf_plot(actual, predicted, nlags=30):

    res = residuals(actual, predicted)

    values = acf(
        res,
        nlags=nlags,
        fft=True,
    )

    fig = go.Figure()

    fig.add_trace(

        go.Bar(
            x=list(range(len(values))),
            y=values,
        )
    )

    fig.add_hline(y=0)

    fig.update_layout(
        title="Residual ACF",
        template="plotly_white",
        height=500,
        xaxis_title="Lag",
        yaxis_title="Correlation",
    )

    return fig

def pacf_plot(actual, predicted, nlags=30):

    res = residuals(actual, predicted)

    values = pacf(
        res,
        nlags=nlags,
    )

    fig = go.Figure()

    fig.add_trace(

        go.Bar(
            x=list(range(len(values))),
            y=values,
        )

    )

    fig.add_hline(y=0)

    fig.update_layout(
        title="Residual PACF",
        template="plotly_white",
        height=500,
        xaxis_title="Lag",
        yaxis_title="Correlation",

    )

    return fig


def model_recommendation(summary):

    text = []

    if summary["White Noise"] == "Yes":
        text.append("✅ Residuals behave like white noise.")
    else:
        text.append("⚠ Residuals still contain information.")

    if summary["Residuals Normal"] == "Yes":
        text.append("✅ Residuals are approximately normal.")
    else:
        text.append("⚠ Residuals are not normally distributed.")

    if summary["White Noise"] == "Yes" and summary["Residuals Normal"] == "Yes":
        text.append("🎯 Model diagnostics indicate a good statistical fit.")
    else:
        text.append("📈 Consider trying SARIMA, Prophet, or LSTM for improved performance.")

    return "\n".join(text)

