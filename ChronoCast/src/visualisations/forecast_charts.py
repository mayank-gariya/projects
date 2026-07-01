import plotly.graph_objects as go
import pandas as pd


def actual_vs_predicted_chart(train: pd.Series,test: pd.Series,prediction: pd.Series,model_name: str = "ARIMA",):
    """
    Plot Train, Test and Predicted values.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=train.index,
            y=train,
            mode="lines",
            name="Train",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=test.index,
            y=test,
            mode="lines",
            name="Actual",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=prediction.index,
            y=prediction,
            mode="lines",
            name="Prediction",
        )
    )
    
    fig.update_layout(
        title=f"{model_name} : Actual vs Prediction",
        template="plotly_white",
        height=650,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Price",
    )

    return fig


def future_forecast_chart(historical: pd.Series,forecast: pd.Series,model_name="ARIMA"):
    """
    Plot historical prices with future forecast.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=historical.index,
            y=historical,
            mode="lines",
            name="Historical",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast,
            mode="lines",
            name="Forecast",
        )
    )

    fig.update_layout(
        title=f"{model_name} Future Forecast",
        template="plotly_white",
        height=650,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Price",
    )

    return fig


def residual_plot(actual: pd.Series,prediction: pd.Series):
    """
    Residual Error Plot.
    """

    residual = actual - prediction

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=residual.index,
            y=residual,
            mode="markers",
            name="Residual",
        )
    )

    fig.add_hline(
        y=0,
        line_dash="dash",
    )

    fig.update_layout(
        title="Residual Errors",
        template="plotly_white",
        height=500,
        xaxis_title="Date",
        yaxis_title="Error",
    )

    return fig


def residual_distribution(actual: pd.Series,prediction: pd.Series):
    """
    Distribution of residuals.
    """

    residual = actual - prediction

    fig = go.Figure()

    fig.add_histogram(
        x=residual,
        nbinsx=40,
        name="Residual Distribution",
    )

    fig.update_layout(
        title="Residual Distribution",
        template="plotly_white",
        height=500,
        xaxis_title="Residual",
        yaxis_title="Frequency",
    )

    return fig


def confidence_interval_chart(historical: pd.Series,forecast: pd.Series,lower,upper,model_name="ARIMA"):
    """
    Forecast with confidence interval.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=historical.index,
            y=historical,
            mode="lines",
            name="Historical",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast,
            mode="lines",
            name="Forecast",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=upper.index,
            y=upper,
            line=dict(width=0),
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=lower.index,
            y=lower,
            fill="tonexty",
            name="Confidence Interval",
            line=dict(width=0),
        )
    )

    fig.update_layout(
        title=f"{model_name} Forecast with Confidence Interval",
        template="plotly_white",
        height=650,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Price",
    )

    return fig


def forecast_table(forecast: pd.Series):
    """
    Convert forecast to dataframe.
    """

    df = pd.DataFrame()

    df["Date"] = forecast.index
    df["Forecast"] = forecast.values

    return df