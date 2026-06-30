from datetime import date

import streamlit as st

from src.data.data_loader import get_stock_data
from src.tests.stationarity import (
    adf_test,
    kpss_test,
    interpret_adf,
    interpret_kpss,
)
from src.tests.transform import (
    first_difference,
    second_difference,
    log_transform,
)

from src.tests.stats_charts import first_differencing_chart , second_differencing_chart , log_differencing_chart , without_difference
from src.utils.sidebar import sidebar_inputs

from src.tests.correlation_test import test_show_correlation_result
st.set_page_config(
    page_title="Statistical Tests",
    layout="wide",
)

st.title("📊 Statistical Tests")

col1, col2, col3 = st.columns(3)

ticker, start_date, end_date = sidebar_inputs()


if ticker:

    data = get_stock_data(
        ticker,
        start_date,
        end_date,
    )

    if data is None or data.empty:
        st.error("No data found.")
        st.stop()

    if data.columns.nlevels > 1:
        data.columns = data.columns.get_level_values(0)
    
    col1 , col2 = st.columns(2)
    
    with col1 :
        st.subheader("📈 Augmented Dickey-Fuller (ADF) Test")

        adf_result = adf_test(data["Close"])

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "ADF Statistic",
                f"{adf_result['Test Statistic']:.4f}",
            )

        with c2:
            st.metric(
                "P-value",
                f"{adf_result['p-value']:.5f}",
            )

        st.info(interpret_adf(adf_result))

        st.write("### Critical Values")

        st.json(adf_result["Critical Values"])

    with col2 : 
        st.subheader("📉Kwiatkowski-Phillips-Schmidt-Shin KPSS Test")

        kpss_result = kpss_test(data["Close"])

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "KPSS Statistic",
                f"{kpss_result['Test Statistic']:.4f}",
            )

        with c2:
            st.metric(
                "P-value",
                f"{kpss_result['p-value']:.5f}",
            )

        st.info(interpret_kpss(kpss_result))

        st.write("### Critical Values")

        st.json(kpss_result["Critical Values"])

    st.divider()

    st.header("🔄 Data Transformations")

    diff_df = first_difference(data)
    second_diff_df = second_difference(data)
    log_df = log_transform(data)
    
    st.plotly_chart(
        without_difference(data['Close']),
        width='stretch'
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "First Difference",
            "Second Difference",
            "Log Transform",
        ]
    )

    with tab1:
        
        st.plotly_chart(
            first_differencing_chart(diff_df),
            width="stretch",
        )

        st.dataframe(
            diff_df[
                [
                    "Close",
                    "Differenced",
                ]
            ]
        )
        
        st.divider()
        
        st.header('Test after first order difference')
        
        col1 , col2 = st.columns(2)
        
        with col1 : 
            st.subheader('ADF test')
            adf_result = adf_test(diff_df['Differenced'])
            
            st.metric(
                "ADF Statistic",
                f"{adf_result['Test Statistic']:.4f}",
            )
            st.metric(
                "P-value",
                f"{adf_result['p-value']:.5f}",
            )
            st.info(interpret_adf(adf_result))
            
        with col2 :
            st.subheader('KPSS test')
            kpss_result = kpss_test(diff_df['Differenced'])
            
            st.metric(
                "ADF Statistic",
                f"{kpss_result['Test Statistic']:.4f}",
            )
            st.metric(
                "P-value",
                f"{kpss_result['p-value']:.5f}",
            )
            
            st.info(interpret_adf(kpss_result))  
            
    with tab2:
        
        st.plotly_chart(
            second_differencing_chart(second_diff_df),
            width="stretch",
        )

        st.dataframe(
            second_diff_df[
                [
                    "Close",
                    "Second_Difference",
                ]
            ]
        )
        st.divider()
        
        st.header('Test after second order difference')
        
        col1 , col2 = st.columns(2)
        
        with col1 : 
            st.subheader('ADF test')
            adf_result = adf_test(second_diff_df['Second_Difference'])
            
            st.metric(
                "ADF Statistic",
                f"{adf_result['Test Statistic']:.4f}",
            )
            st.metric(
                "P-value",
                f"{adf_result['p-value']:.5f}",
            )
            st.info(interpret_adf(adf_result))
            
        with col2 :
            
            st.subheader('KPSS test')
            kpss_result = kpss_test(second_diff_df['Second_Difference'])
            
            st.metric(
                "ADF Statistic",
                f"{kpss_result['Test Statistic']:.4f}",
            )
            st.metric(
                "P-value",
                f"{kpss_result['p-value']:.5f}",
            )
            
            st.info(interpret_adf(kpss_result))  
            
    with tab3:
                
        st.plotly_chart(
            log_differencing_chart(log_df),
            width="stretch",
        )

        st.dataframe(
            log_df[
                [
                    "Close",
                    "Log_Close",
                ]
            ]
        )
        
        st.divider()
        
        st.header('Test after Log order difference')
        
        col1 , col2 = st.columns(2)
        
        with col1 : 
            st.subheader('ADF test')
            adf_result = adf_test(log_df['Log_Close'])
            
            st.metric(
                "ADF Statistic",
                f"{adf_result['Test Statistic']:.4f}",
            )
            st.metric(
                "P-value",
                f"{adf_result['p-value']:.5f}",
            )
            st.info(interpret_adf(adf_result))
            
        with col2 :
            st.subheader('KPSS test')
            kpss_result = kpss_test(log_df['Log_Close'])
            
            st.metric(
                "ADF Statistic",
                f"{kpss_result['Test Statistic']:.4f}",
            )
            st.metric(
                "P-value",
                f"{kpss_result['p-value']:.5f}",
            )
            
            st.info(interpret_adf(kpss_result))  

    st.divider()
    
    test_show_correlation_result(ticker,data)

    st.header("📋 Stationarity Report")

    adf_stationary = adf_result["p-value"] < 0.05
    kpss_stationary = kpss_result["p-value"] > 0.05

with st.expander('report'):
    
    if adf_stationary and kpss_stationary:

        st.success(
            """
            ✅ Final Verdict

            Both ADF and KPSS indicate that the time series is stationary.

            This dataset is suitable for models such as ARIMA.
            """
        )

    else:

        st.warning(
            """
            ⚠️ Final Verdict

            The time series appears to be non-stationary.

            Apply differencing or other transformations before forecasting.
            
            here adf and kpss tests suggest about time-series refer those 
            """
        )