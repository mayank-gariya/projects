import streamlit as st
import yfinance as yf
import pandas as pd

@st.cache_data
def get_stock_data(ticker, start_date, end_date):

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
        group_by="column",
    )

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Remove duplicate columns if any
    data = data.loc[:, ~data.columns.duplicated()]
    
    if not data.empty:
        data.index = pd.to_datetime(data.index)
        data = data.sort_index()
        data = data.asfreq("B").ffill()

    return data
