import streamlit as st

st.set_page_config(
    page_title='ChronoCast',
    page_icon='📈',
    layout='wide'
)

st.title("📈 ChronoCast")

st.markdown("""
### Time Series Analysis & Forecasting Studio

Analyze stocks, identify trends, test stationarity,
and forecast future prices using advanced time series models.
""")

st.info(
    "Select Data Explorer from the sidebar to begin."
)