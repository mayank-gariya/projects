import plotly.graph_objects as go
import plotly.express as px


def cumulative_return_chart(df, ticker):
    """
    Plot cumulative returns over time.

    Shows how $1 invested on the first trading day
    would have grown over the selected period.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Cumulative_Return"],
            mode="lines",
            name="Cumulative Returns",
            line=dict(width=3),
        )
    )

    fig.update_layout(
        title=f"{ticker} - Cumulative Returns",
        template="plotly_dark",
        height=550,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Growth of $1 Investment",
        legend=dict(
            orientation="h",
            y=1.02,
            x=1,
            xanchor="right",
        ),
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    fig.update_yaxes(
        tickformat=".2f"
    )

    return fig

def returns_distribution_chart(df):
    """
    Histogram of daily returns.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=df["Daily_Return"] * 100,
            nbinsx=50,
            name="Daily Returns",
            opacity=0.85,
        )
    )

    fig.update_layout(
        title="Daily Returns Distribution",
        template="plotly_dark",
        height=500,
        hovermode="x unified",
        xaxis_title="Daily Return (%)",
        yaxis_title="Frequency",
        bargap=0.05,
    )

    return fig

def monthly_returns_heatmap(df):
    """
    Monthly Returns Heatmap.
    """
    returns = df["Close"].resample("ME").last().pct_change() * 100

    heatmap = returns.to_frame(name="Return")

    heatmap["Year"] = heatmap.index.year
    heatmap["Month"] = heatmap.index.strftime("%b")

    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    pivot = heatmap.pivot(
        index="Year",
        columns="Month",
        values="Return"
    )

    pivot = pivot.reindex(columns=month_order)

    fig = px.imshow(
        pivot,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale="RdYlGn",
        labels=dict(
            color="Return (%)"
        ),
    )

    fig.update_layout(
        title="Monthly Returns Heatmap",
        template="plotly_dark",
        height=500,
        xaxis_title="Month",
        yaxis_title="Year",
    )

    return fig