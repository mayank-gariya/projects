import numpy as np
import pandas as pd
from statsmodels.stats.diagnostic import acorr_ljungbox , het_arch , het_breuschpagan
import statsmodels.api as sm 
from pmdarima.arima import nsdiffs
import streamlit as st


def test_show_correlation_result(ticker,df):
        
    df = df.copy()

    df["Returns"] = np.log(df["Close"] / df["Close"].shift(1))
    df = df.dropna()

    X = sm.add_constant(np.arange(len(df)))
    y = df["Returns"].values
    model = sm.OLS(y, X).fit()
    residuals = model.resid

    st.subheader(f"\n--- DIAGNOSTIC TESTS FOR {ticker} DAILY RETURNS --- \n")


    st.subheader("[1] Ljung-Box Test (Testing for Serial Correlation)")

    lb_results = acorr_ljungbox(residuals, lags=[10], return_df=True)
    p_val_lb = lb_results["lb_pvalue"].values[0]

    st.metric(
        label="Ljung-Box Statistic (Lag 10)",
        value=f"{lb_results['lb_stat'].values[0]:.4f}"
    )

    st.metric(
        label="p-value",
        value=f"{p_val_lb}"
    )
    
    if p_val_lb < 0.05:
        st.info("Result: Reject H0. Significant autocorrelation detected (Returns are predictable).\n")
    else:
        st.info(
            "Result: Fail to reject H0. No significant autocorrelation (Market is efficient/random).\n"
        )


    st.subheader("[2] Breusch-Pagan Test (Testing for Linear Heteroskedasticity)")
    bp_test = het_breuschpagan(residuals, X)
    bp_pvalue = bp_test[1]
    
    st.metric(
        label="LM Statistic",
        value=f"{bp_test[0]:.4f}"
    )

    st.metric(
        label="p-value",
        value=f"{bp_pvalue:.4f}"
    )
    
    if bp_pvalue < 0.05:
        st.info("Result: Reject H0. Linear heteroskedasticity is present.\n")
    else:
        st.info("Result: Fail to reject H0. Variance is stable over time.\n")


    st.subheader(
        "[3] Engle's ARCH-LM Test (Testing for Volatility Clustering / ARCH Effects)"
    )

    arch_test = het_arch(residuals, maxlag=5)
    arch_pvalue = arch_test[1]
    
    st.metric(
        label="LM Statistic",
        value=f"{arch_test[0]:.4f}"
    )

    st.metric(
        label="p-value",
        value=f"{arch_pvalue:.4f}"
    )
    
    if arch_pvalue < 0.05:
        st.info(
            "Result: Reject H0. ARCH effects detected. You must use a GARCH model for volatility forecasting.\n"
        )
    else:
        st.info("Result: Fail to reject H0. No volatility clustering detected.\n")


    st.subheader("[4] OCSB Test for Seasonality (Proxy for Canova-Hansen)")
 
    # m=5 implies a weekly pattern for business days
    seasonal_diffs_needed = nsdiffs(df["Returns"], m=5, test="ocsb")
    st.info(f"OCSB Seasonal Differencing Steps Required: {seasonal_diffs_needed}")
    
    if seasonal_diffs_needed > 0:
        st.info("Result: Identifiable trading-week seasonality detected.")
    else:
        st.info("Result: No calendar seasonal patterns found in returns.")


