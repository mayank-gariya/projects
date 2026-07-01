import plotly.graph_objects as go
from plotly.subplots import make_subplots


def decomposition_chart(result):
    """
    Plot Trend, Seasonality and Residuals.
    """

    fig = make_subplots(
        rows=4,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.04,
        subplot_titles=(
            "Original Series",
            "Trend",
            "Seasonality",
            "Residuals",
        ),
    )

    fig.add_trace(
        go.Scatter(
            x=result.observed.index,
            y=result.observed,
            mode="lines",
            name="Observed",
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=result.trend.index,
            y=result.trend,
            mode="lines",
            name="Trend",
        ),
        row=2,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=result.seasonal.index,
            y=result.seasonal,
            mode="lines",
            name="Seasonality",
        ),
        row=3,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=result.resid.index,
            y=result.resid,
            mode="lines",
            name="Residual",
        ),
        row=4,
        col=1,
    )

    fig.update_layout(
        template="plotly_dark",
        height=900,
        showlegend=False,
        title="Time Series Decomposition",
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    return fig