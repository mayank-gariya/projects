import streamlit as st
import numpy as np 
from datetime import date
from src.utils.sidebar import sidebar_inputs
from src.data.utils import load_processed_data
from src.time_series.decompostion import decompose_series

from src.time_series.decompostion_charts import (
    decomposition_chart,
)

from src.time_series.autocorrelation import (
    generate_acf,
    generate_pacf,
)

from src.visualisations.charts import (
    rolling_statistics_chart,
    daily_returns_chart,
    return_distribution_chart,
    volatility_chart,
    boxplot_returns,
)

from src.utils.analysis import (
    rolling_statistics,
    annualized_volatility,
    trend_strength,
    return_statistics,
    summary_statistics,
)
from src.tests.stationarity import (
    adf_test,
    kpss_test,
    interpret_adf,
    interpret_kpss,
)

from src.time_series.interpretation import generate_report


st.set_page_config(page_title="Time Series Analysis", layout="wide")

st.title("📈 Time Series Analysis")

ticker, start_date, end_date = sidebar_inputs()

data = load_processed_data(ticker,start_date,end_date)

if data is None or data.empty:
    st.error("Invalid ticker or no data found.")
    st.stop()

data = rolling_statistics(data)
close = data["Close"]

st.sidebar.subheader("Decomposition Settings")

decomposition_model = st.sidebar.selectbox(
    "Model",
    ["additive", "multiplicative"],
)

seasonal_period = st.sidebar.slider(
    "Seasonal Period",
    min_value=5,
    max_value=365,
    value=30,
)
decomposition = decompose_series(
    close,
    model=decomposition_model,
    period=seasonal_period,
)

st.subheader("📊 Time Series Decomposition")

st.plotly_chart(
    decomposition_chart(decomposition),
    width="stretch",
)

st.divider()

lags = st.sidebar.slider(
    "Number of Lags",
    min_value=10,
    max_value=100,
    value=40,
)

st.subheader("📊 Autocorrelation Analysis")

left, right = st.columns(2)

with left:
    st.pyplot(
        generate_acf(
            close,
            lags,
        )
    )

with right:
    st.pyplot(
        generate_pacf(
            close,
            lags,
        )
    )
    
st.header("📈 Rolling Statistics")
st.plotly_chart(
    rolling_statistics_chart(data, ticker),
    width="stretch",
)

st.header("📉 Daily Returns")
st.plotly_chart(
    daily_returns_chart(data),
    width="stretch",
)

st.header("📊 Return Distribution")
st.plotly_chart(
    return_distribution_chart(data),
   width="stretch",
)

st.header("📈 Rolling Volatility")
st.plotly_chart(
    volatility_chart(data),
    width="stretch",
)

st.header("📦 Outlier Detection")
st.plotly_chart(
    boxplot_returns(data),
    width="stretch",
)

kpss_result = kpss_test(data["Close"])
adf_result = adf_test(data["Close"])

rolling_mean = data['Close'].rolling(window=3).mean()

report = generate_report(
    decomposition=decomposition,
    adf_result=adf_result,
    kpss_result=kpss_result,
    rolling_mean=data['Rolling_Mean'].dropna(),
    rolling_std=data['Rolling_Volatility'].dropna(),
    residuals=decomposition.resid.dropna(),
)

st.divider()

st.subheader("📝 Automated Time Series Interpretation")

st.success(
    """
The following observations have been generated automatically
from the statistical analysis and visualizations above.
"""
)

for point in report:
    st.markdown(point)
    
report_text = "\n\n".join(report)

st.download_button(
    label="📥 Download Analysis Report",
    data=report_text,
    file_name="time_series_report.txt",
    mime="text/plain",
)