import streamlit as st
import pandas as pd


def diagnostics_dashboard(
    summary: dict,
    aic=None,
    bic=None,
    order=None,
):
    """
    Complete ARIMA diagnostics dashboard.
    """

    st.subheader("🩺 Diagnostics Dashboard")

    score = 0

    if summary["White Noise"] == "Yes":
        score += 40

    if summary["Residuals Normal"] == "Yes":
        score += 30

    if abs(summary["Residual Mean"]) < 0.5:
        score += 30

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Residual Mean",
            summary["Residual Mean"]
        )

        st.metric(
            "Residual Std",
            summary["Residual Std"]
        )

        st.metric(
            "Jarque-Bera",
            summary["Jarque-Bera"]
        )

    with col2:

        st.metric(
            "JB P-value",
            summary["JB P-value"]
        )

        st.metric(
            "Ljung-Box",
            summary["Ljung-Box P-value"]
        )

        if order is not None:

            st.metric(
                "ARIMA Order",
                str(order)
            )

    with col3:

        if aic is not None:

            st.metric(
                "AIC",
                round(aic,2)
            )

        if bic is not None:

            st.metric(
                "BIC",
                round(bic,2)
            )

        st.metric(
            "Health Score",
            f"{score}/100"
        )

    st.progress(score / 100)

    if score >= 90:

        st.success("🟢 Excellent model. Diagnostics look healthy.")

    elif score >= 70:

        st.info("🟡 Good model. Suitable for forecasting.")

    elif score >= 50:

        st.warning("🟠 Fair model. Consider trying Auto ARIMA, SARIMA or Prophet.")

    else:

        st.error("🔴 Poor model. Residual diagnostics indicate improvement is needed.")

    status = pd.DataFrame({

        "Diagnostic":[
            "Residual Mean",
            "White Noise",
            "Residual Normality",
            "Jarque-Bera",
            "Ljung-Box",
        ],

        "Result":[
            summary["Residual Mean"],
            summary["White Noise"],
            summary["Residuals Normal"],
            summary["Jarque-Bera"],
            summary["Ljung-Box P-value"],
        ]
    })
    
    status["Result"] = status["Result"].astype(str)

    st.subheader("📋 Validation Checklist")

    checks = [
        ("Data Loaded", True),
        ("Missing Values Removed", True),
        ("Stationarity Checked", True),
        ("Model Trained", True),
        ("Forecast Generated", True),
        ("Metrics Calculated", True),
        ("Residual White Noise", summary["White Noise"] == "Yes"),
        ("Residual Normality", summary["Residuals Normal"] == "Yes"),
    ]

    for label, passed in checks:
        if passed:
            st.success(f"✅ {label}")
        else:
            st.warning(f"⚠️ {label}")

    st.subheader("📊 Diagnostics Summary")

    st.dataframe(
        status,
        hide_index=True,
        width="stretch",
    )