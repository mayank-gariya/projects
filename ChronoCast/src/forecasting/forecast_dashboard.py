import streamlit as st
import pandas as pd


def forecast_dashboard(
    model_name: str,
    model_order: tuple,
    metrics: dict,
    forecast_days: int,
    current_price: float,
    predicted_price: float,
):
    """
    Professional Forecast Dashboard
    """

    st.subheader("📈 Forecast Dashboard")

    expected_return = (
        (predicted_price - current_price)
        / current_price
    ) * 100

    if expected_return > 5:
        trend = "📈 Strong Bullish"

    elif expected_return > 1:
        trend = "🟢 Bullish"

    elif expected_return < -5:
        trend = "📉 Strong Bearish"

    elif expected_return < -1:
        trend = "🔴 Bearish"

    else:
        trend = "➡ Sideways"

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Forecast Model",
            model_name
        )

        st.metric(
            "Forecast Horizon",
            f"{forecast_days} Days"
        )

        st.metric(
            "Model Order",
            str(model_order)
        )

    with col2:

        st.metric(
            "Current Price",
            f"${current_price:.2f}"
        )

        st.metric(
            "Forecast Price",
            f"${predicted_price:.2f}"
        )

        st.metric(
            "Expected Return",
            f"{expected_return:.2f}%"
        )

    with col3:

        st.metric(
            "Trend",
            trend
        )

        st.metric(
            "RMSE",
            metrics["RMSE"]
        )

        st.metric(
            "MAPE",
            f"{metrics['MAPE (%)']}%"
        )

    st.divider()

    report = pd.DataFrame({

        "Metric":[
            "MAE",
            "RMSE",
            "MAPE",
            "R²",
            "Forecast Horizon",
            "Current Price",
            "Forecast Price",
            "Expected Return",
            "Trend",
            "Model",
            "Order",
        ],

        "Value":[
            metrics["MAE"],
            metrics["RMSE"],
            metrics["MAPE (%)"],
            metrics["R² Score"],
            forecast_days,

            round(current_price,2),
            round(predicted_price,2),

            f"{expected_return:.2f}%",

            trend,
            model_name,
            str(model_order)
        ]

    })
    
    report["Value"] = report["Value"].astype(str)

    st.subheader("📄 Forecast Report")

    st.dataframe(
        report,
        width="stretch",
        hide_index=True
    )

    csv = report.to_csv(index=False).encode()

    st.download_button(
        "📥 Download Forecast Report",
        csv,
        "forecast_report.csv",
        "text/csv"
    )