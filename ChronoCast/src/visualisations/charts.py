import plotly.graph_objects as go
import plotly.express as px


def candel_chart(df,ticker):
    '''cretes the candel chart'''
    
    fig = go.Figure()
    
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name=ticker,
        )
    )
    
    fig.update_layout(
        title=f"{ticker} Price Movement",
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False,
        template="plotly_white",
        height=650,
    )
    
    return fig

def volume_chart(df):
    """
    Plot trading volume.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["Volume"],
            name="Volume",
        )
    )

    fig.update_layout(
        title="Trading Volume",
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white",
        height=350,
    )

    return fig


def moving_average_chart(df, ticker):
    """
    Plot Close price with moving averages.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Close Price",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["SMA_20"],
            mode="lines",
            name="SMA 20",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["SMA_50"],
            mode="lines",
            name="SMA 50",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["EMA_20"],
            mode="lines",
            name="EMA 20",
        )
    )

    fig.update_layout(
        title=f"{ticker} Moving Averages",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white",
        height=600,
    )

    return fig

def rolling_statistics_chart(df, ticker):
    """
    Plot Close Price, Rolling Mean and Rolling STD.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Close Price",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Rolling_Mean"],
            mode="lines",
            name="30-Day Rolling Mean",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Rolling_STD"],
            mode="lines",
            name="30-Day Rolling Std",
            line=dict(dash="dot"),
        )
    )

    fig.update_layout(
        title=f"{ticker} Rolling Statistics",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white",
        height=600,
    )

    return fig

def daily_returns_chart(df):
    """
    Plot daily returns over time.
    """

    fig = px.line(
        df,
        x=df.index,
        y="Daily_Return",
        title="Daily Returns"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        xaxis_title="Date",
        yaxis_title="Daily Return",
    )

    return fig

def return_distribution_chart(df):
    """
    Histogram of daily returns.
    """

    fig = px.histogram(
        df,
        x="Daily_Return",
        nbins=50,
        title="Distribution of Daily Returns",
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
    )

    return fig

def volatility_chart(df):
    """
    Plot rolling volatility.
    """

    fig = px.line(
        df,
        x=df.index,
        y="Rolling_Volatility",
        title="Rolling Volatility",
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        xaxis_title="Date",
        yaxis_title="Volatility",
    )

    return fig

def boxplot_returns(df):
    """
    Box plot of daily returns.
    """

    fig = px.box(
        df,
        y="Daily_Return",
        title="Daily Return Box Plot",
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
    )

    return fig

def closing_price_chart(df, ticker):
    """
    Line chart of closing prices over time.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Close Price",
            line=dict(width=3),
        )
    )

    fig.update_layout(
        title=f"{ticker} Closing Price",
        template="plotly_dark",
        height=550,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    return fig

def ohlc_range_chart(df, ticker):
    """
    OHLC Range Chart

    Shows the daily High-Low trading range with
    the Closing Price overlaid.
    """

    fig = go.Figure()

    # High Price
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["High"],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
            hoverinfo="skip",
        )
    )

    # Low Price (creates filled area)
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Low"],
            mode="lines",
            fill="tonexty",
            fillcolor="rgba(0,176,246,0.25)",
            line=dict(width=0),
            name="Daily Range",
        )
    )

    # Closing Price
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Close",
            line=dict(width=2),
        )
    )

    fig.update_layout(
        title=f"{ticker} OHLC Daily Trading Range",
        template="plotly_dark",
        height=550,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        legend=dict(
            orientation="h",
            y=1.02,
            x=1,
            xanchor="right",
        ),
    )

    return fig