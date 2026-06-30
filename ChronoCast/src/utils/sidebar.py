from datetime import date
import streamlit as st


def sidebar_inputs():

    st.sidebar.title("⏳ ChronoCast")

    st.sidebar.markdown(
        """
        Analyze financial time series,
        visualize trends, test stationarity,
        and forecast future prices.
        """
    )

    st.sidebar.divider()

    ticker = st.sidebar.selectbox(
        "📈 Stock",
        (
            "AAPL",
            "MSFT",
            "AMZN",
            "NVDA",
            "TSLA",
            "NFLX",
            'GOOGl'
        ),
    )

    start_date = st.sidebar.date_input(
        "📅 Start Date",
        value=date(2020, 1, 1),
    )

    end_date = st.sidebar.date_input(
        "📅 End Date",
        value=date.today(),
    )

    st.sidebar.divider()

    st.sidebar.caption("ChronoCast v1.0")

    return ticker, start_date, end_date