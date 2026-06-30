from datetime import date
import plotly.graph_objects as go
import streamlit as st

from src.utils.metrics import calculate_metrics
from src.visualisations.charts import candel_chart , moving_average_chart , volume_chart , closing_price_chart , ohlc_range_chart
from src.utils.sidebar import sidebar_inputs
from src.data.utils import load_processed_data

from  src.visualisations.analysis_charts import  returns_distribution_chart , monthly_returns_heatmap

st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("📊 Data Explorer")

ticker, start_date, end_date = sidebar_inputs()
 
if ticker:
    
    data = load_processed_data(
        ticker,
        start_date,
        end_date,
    )

    if data is None or data.empty:
        st.error("Invalid ticker or no data found.")
        st.stop()

    metrices = calculate_metrics(data)
    
    volatility = data["Daily_Return"].std() * (252 ** 0.5) * 100
    trading_days = len(data)
    highest_volume = data["Volume"].max()
    lowest_price = data["Low"].min()
    
    
    def format_number(number):
        """
        Convert large numbers into human-readable form.
        """

        if number >= 1_000_000_000:
            return f"{number/1_000_000_000:.2f}B"

        if number >= 1_000_000:
            return f"{number/1_000_000:.2f}M"

        if number >= 1_000:
            return f"{number/1_000:.2f}K"

        return str(number)
    
    col1,col2,col3,col4,col5,col6 = st.columns(6)

    with col1:

        st.metric(
            "Current Price",
            f"${metrices['current_price']:.2f}",
            f"{metrices['daily_change_pct']:.2f}%"
        )

    with col2:

        st.metric(
            "52W High",
            f"${metrices['period_high']:.2f}"
        )

    with col3:

        st.metric(
            "52W Low",
            f"${lowest_price:.2f}"
        )

    with col4:

        st.metric(
            "Volatility",
            f"{volatility:.2f}%"
        )

    with col5:

        st.metric(
            "Trading Days",
            trading_days
        )

    with col6:

        st.metric(
            "Avg Volume",
            format_number(metrices["average_volume"])
        )
    
    st.divider()
    
    st.subheader("📈 Closing Price Trend")
    st.plotly_chart(
        closing_price_chart(
            data,
            ticker,
        ),
        width="stretch",
    )
    
    st.subheader("📈 Price Action")
    st.plotly_chart(
    candel_chart(data, ticker),
    width="stretch",
    )
    
    st.subheader("📉 Trend Analysis")
    st.plotly_chart(
        volume_chart(data),
        width="stretch",
    )
    
    st.subheader("📉 OHLC Trading Range")
    st.plotly_chart(
        ohlc_range_chart(
            data,
            ticker,
        ),
        width="stretch",
    )
            
    st.subheader("📊 Daily Returns Distribution")
    st.plotly_chart(
        returns_distribution_chart(data),
        width="stretch",
    )
    
    st.subheader("🔥 Monthly Returns Heatmap")
    st.plotly_chart(
        monthly_returns_heatmap(data),
        width="stretch",
    )

    st.divider()
    
    st.subheader("📄 Historical Dataset")
    
    st.subheader("📋 Dataset Info")

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric("Rows", len(data))

    with c2:
        st.metric("Columns", len(data.columns))

    with c3:
        st.metric(
            "Missing Values",
            int(data.isna().sum().sum())
        )

    with c4:
        st.metric(
            "Date Range",
            f"{len(data)} Days"
        )
    
    st.dataframe(
        data,
        width="stretch",
        height=400
    )

    csv = data.to_csv().encode("utf-8")

    st.download_button(
        "📥 Download CSV",
        data=csv,
        file_name=f"{ticker}.csv",
        mime="text/csv"
    )