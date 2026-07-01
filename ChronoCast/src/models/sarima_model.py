from datetime import timedelta, datetime

import pandas as pd
import streamlit as st

# SARIMA imports
from src.forecasting.sarima_model import (
    train_sarima,
    forecast_sarima,
    fit_and_forecast_sarima,
)

from src.data.utils import load_processed_data
from src.forecasting.evaluating import calculate_metrics, metrics_dataframe
from src.visualisations.forecast_charts import (
    actual_vs_predicted_chart,
    future_forecast_chart,
    confidence_interval_chart,
    residual_plot,
    residual_distribution,
    forecast_table,
)


def sarima_start_to_end():
    # ------------------------------------------------------------
    # Sidebar: Ticker & Date (local, with unique keys)
    # ------------------------------------------------------------
    ticker = st.sidebar.selectbox(
        "Select Ticker",
        options=["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", "META", "NFLX"],
        key="sarima_ticker"                     # unique key
    )

    start_date = st.sidebar.date_input(
        "Start Date",
        value=datetime.now() - timedelta(days=365),
        key="sarima_start"
    )

    end_date = st.sidebar.date_input(
        "End Date",
        value=datetime.now(),
        key="sarima_end"
    )

    # Load data
    data = load_processed_data(ticker, start_date, end_date)
    if data is None:
        st.error("Unable to load stock data.")
        st.stop()

    close = data["Close"]

    # ------------------------------------------------------------
    # Sidebar: Forecast Settings
    # ------------------------------------------------------------
    st.sidebar.header("Forecast Settings")

    forecast_days = st.sidebar.slider(
        "Forecast Horizon (Days)",
        min_value=7,
        max_value=180,
        value=30,
        key="sarima_forecast_days"
    )

    # ------------------------------------------------------------
    # Sidebar: SARIMA Parameters
    # ------------------------------------------------------------
    st.sidebar.subheader("SARIMA Parameters")

    # Non-seasonal order
    col1, col2, col3 = st.columns(3)
    with col1:
        p = st.sidebar.number_input(
            "p (AR)", min_value=0, max_value=10, value=1,
            key="sarima_p"
        )
    with col2:
        d = st.sidebar.number_input(
            "d (Differencing)", min_value=0, max_value=3, value=1,
            key="sarima_d"
        )
    with col3:
        q = st.sidebar.number_input(
            "q (MA)", min_value=0, max_value=10, value=1,
            key="sarima_q"
        )

    # Seasonal order
    st.sidebar.markdown("**Seasonal Order**")
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        P = st.sidebar.number_input(
            "P (seasonal AR)", min_value=0, max_value=5, value=1,
            key="sarima_P"
        )
    with col5:
        D = st.sidebar.number_input(
            "D (seasonal diff)", min_value=0, max_value=2, value=1,
            key="sarima_D"
        )
    with col6:
        Q = st.sidebar.number_input(
            "Q (seasonal MA)", min_value=0, max_value=5, value=1,
            key="sarima_Q"
        )
    with col7:
        s = st.sidebar.number_input(
            "S (seasonal period)", min_value=1, max_value=365, value=7,
            key="sarima_s"
        )

    # ------------------------------------------------------------
    # Main page: Title & model training
    # ------------------------------------------------------------
    st.header("📈 SARIMA Forecasting")

    with st.spinner("Training SARIMA model..."):
        train, test, prediction, model = fit_and_forecast_sarima(
            close,
            order=(p, d, q),
            seasonal_order=(P, D, Q, s),
            test_size=0.2,
        )

    # ------------------------------------------------------------
    # Model performance metrics
    # ------------------------------------------------------------
    metrics = calculate_metrics(test, prediction)

    st.subheader("📊 Model Performance")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("MAE", metrics["MAE"])
    with col2:
        st.metric("RMSE", metrics["RMSE"])
    with col3:
        st.metric("MAPE", f"{metrics['MAPE (%)']} %")
    with col4:
        st.metric("R² Score", metrics["R² Score"])

    with st.expander("View Complete Metrics"):
        st.dataframe(metrics_dataframe(metrics), width="stretch", hide_index=True)

    st.divider()

    # ------------------------------------------------------------
    # Future forecast with confidence intervals
    # ------------------------------------------------------------
    future_model = train_sarima(
        close,
        order=(p, d, q),
        seasonal_order=(P, D, Q, s),
    )

    future_forecast = forecast_sarima(future_model, periods=forecast_days)

    future_dates = pd.date_range(
        start=close.index[-1] + timedelta(days=1),
        periods=forecast_days,
        freq="B",
    )
    future_forecast.index = future_dates

    forecast_result = future_model.get_forecast(steps=forecast_days)
    conf_int = forecast_result.conf_int()
    conf_int.index = future_dates
    lower = conf_int.iloc[:, 0]
    upper = conf_int.iloc[:, 1]

    forecast_df = forecast_table(future_forecast)

    # ------------------------------------------------------------
    # Visualizations
    # ------------------------------------------------------------
    st.subheader("📈 Actual vs Predicted")
    st.plotly_chart(
        actual_vs_predicted_chart(
            train=train,
            test=test,
            prediction=prediction,
            model_name="SARIMA",
        ),
        width="stretch",
    )
    st.info(
        """
        **Interpretation**  
        • Blue = training data  
        • Orange = actual unseen prices  
        • Green = SARIMA predictions  
        A good model should follow the actual prices closely.
        """
    )

    st.divider()

    st.subheader("🔮 Future Forecast")
    st.plotly_chart(
        future_forecast_chart(
            historical=close,
            forecast=future_forecast,
            model_name="SARIMA",
        ),
        width="stretch",
    )

    st.divider()

    st.subheader("📊 Forecast Confidence Interval")
    st.plotly_chart(
        confidence_interval_chart(
            historical=close,
            forecast=future_forecast,
            lower=lower,
            upper=upper,
            model_name="SARIMA",
        ),
        width="stretch",
    )
    st.info(
        """
        The shaded region is the **95% confidence interval**.  
        Wider intervals indicate higher uncertainty.
        """
    )

    st.divider()

    st.subheader("📉 Residual Analysis")
    left, right = st.columns(2)
    with left:
        st.plotly_chart(residual_plot(actual=test, prediction=prediction), width="stretch")
    with right:
        st.plotly_chart(residual_distribution(actual=test, prediction=prediction), width="stretch")
    st.info(
        """
        Residuals should be randomly scattered around zero.  
        Patterns suggest the model missed some structure.
        """
    )

    st.divider()

    st.subheader("📄 Forecast Values")
    display_df = forecast_df.copy()
    display_df["Forecast"] = display_df["Forecast"].round(2)
    st.dataframe(display_df, width="stretch", hide_index=True)

    st.divider()

    csv = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name=f"{ticker}_sarima_forecast.csv",
        mime="text/csv",
        key="sarima_download",
    )

    st.divider()

    # ------------------------------------------------------------
    # Forecast summary
    # ------------------------------------------------------------
    st.subheader("📝 Forecast Summary")

    latest_price = float(close.iloc[-1])
    predicted_price = float(future_forecast.iloc[-1])
    change = predicted_price - latest_price
    change_pct = (change / latest_price) * 100

    if change_pct > 5:
        trend = "📈 Strong Bullish"
    elif change_pct > 1:
        trend = "📈 Mild Bullish"
    elif change_pct < -5:
        trend = "📉 Strong Bearish"
    elif change_pct < -1:
        trend = "📉 Mild Bearish"
    else:
        trend = "➡️ Sideways"

    summary_col1, summary_col2 = st.columns(2)
    with summary_col1:
        st.metric("Current Price", f"${latest_price:.2f}")
        st.metric("Forecast Price", f"${predicted_price:.2f}")
    with summary_col2:
        st.metric("Expected Change", f"{change_pct:.2f}%")
        st.metric("Trend", trend)

    st.success(
        f"""
### 📌 Model Interpretation

**Forecast Horizon:** {forecast_days} business days  
**Current Price:** ${latest_price:.2f}  
**Predicted Price:** ${predicted_price:.2f}  
**Expected Return:** {change_pct:.2f}%  
**Overall Trend:** {trend}

---
### Model Performance
- **MAE** : {metrics['MAE']}
- **RMSE** : {metrics['RMSE']}
- **MAPE** : {metrics['MAPE (%)']}%
- **R² Score** : {metrics['R² Score']}

Lower MAE, RMSE and MAPE indicate better performance; R² closer to 1 is better.
"""
    )
