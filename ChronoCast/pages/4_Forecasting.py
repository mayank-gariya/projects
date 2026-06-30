import pandas as pd
import streamlit as st

from src.models.arima_model import arima_start_to_end 
from src.models.auto_arima_model import auto_arima_start_to_end

st.set_page_config(
    page_title="Forecasting",
    page_icon="🔮",
    layout="wide",
)

st.title("🔮 Stock Price Forecasting")

st.markdown(
    """
Forecast future stock prices ,

This module trains an model,
evaluates its performance on unseen data,
and predicts future prices.
"""
)

tab1 , tab2 , tab3 , tab4 = st.tabs([
    'Arima',
    'Auto Arima',
    'Sarima',
    'other'
])

with tab1:
    arima_start_to_end()

with tab2 :
    auto_arima_start_to_end()