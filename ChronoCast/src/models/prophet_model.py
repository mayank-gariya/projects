from datetime import timedelta, datetime
import pandas as pd
import streamlit as st
import numpy as np
from prophet import Prophet
import holidays

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


def prophet_start_to_end():
    # ------------------------------------------------------------
    # Sidebar: Ticker & Date
    # ------------------------------------------------------------
    ticker = st.sidebar.selectbox(
        "Select Ticker",
        options=["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", "META", "NFLX"],
        key="prophet_ticker"
    )

    start_date = st.sidebar.date_input(
        "Start Date",
        value=datetime.now() - timedelta(days=365 * 2),
        key="prophet_start"
    )

    end_date = st.sidebar.date_input(
        "End Date",
        value=datetime.now(),
        key="prophet_end"
    )

    data = load_processed_data(ticker, start_date, end_date)
    if data is None:
        st.error("Unable to load stock data.")
        st.stop()

    close = data["Close"]

    # Clean numeric data
    close = pd.to_numeric(close, errors="coerce").dropna()
    if close.empty:
        st.error("No valid price data available after cleaning.")
        st.stop()

    # ------------------------------------------------------------
    # Sidebar: Forecast Settings
    # ------------------------------------------------------------
    st.sidebar.header("Forecast Settings")

    forecast_days = st.sidebar.slider(
        "Forecast Horizon (Days)",
        min_value=7,
        max_value=180,
        value=30,
        key="prophet_forecast_days"
    )

    st.sidebar.subheader("Prophet Options")
    changepoint_prior_scale = st.sidebar.slider(
        "Changepoint Prior Scale",
        min_value=0.01,
        max_value=5.0,
        value=0.5,
        step=0.01,
        key="prophet_changepoint"
    )
    seasonality_prior_scale = st.sidebar.slider(
        "Seasonality Prior Scale",
        min_value=0.01,
        max_value=20.0,
        value=10.0,
        step=0.5,
        key="prophet_seasonality"
    )
    seasonality_mode = st.sidebar.selectbox(
        "Seasonality Mode",
        options=["additive", "multiplicative"],
        index=0,
        key="prophet_seasonality_mode"
    )
    add_weekly = st.sidebar.checkbox("Weekly Seasonality", value=True, key="prophet_weekly")
    add_yearly = st.sidebar.checkbox("Yearly Seasonality", value=False, key="prophet_yearly")
    use_holidays = st.sidebar.checkbox("Include US Holidays", value=True, key="prophet_holidays")
    use_log = st.sidebar.checkbox("Log‑transform target", value=True, key="prophet_log")

    # ------------------------------------------------------------
    # Prepare data for Prophet
    # ------------------------------------------------------------
    df = close.reset_index()
    df.columns = ["ds", "y"]

    if use_log:
        df["y"] = np.log(df["y"])

    # Train/Test split (80/20)
    split_index = int(len(df) * 0.8)
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]

    # ------------------------------------------------------------
    # Build holidays DataFrame if needed
    # ------------------------------------------------------------
    if use_holidays:
        start_year = start_date.year
        end_year = end_date.year + 1
        us_holidays = holidays.US(years=range(start_year, end_year + 1))
        holidays_df = pd.DataFrame(list(us_holidays.items()), columns=["ds", "holiday"])
        holidays_df["ds"] = pd.to_datetime(holidays_df["ds"])
    else:
        holidays_df = None

    # ------------------------------------------------------------
    # Train Prophet model
    # ------------------------------------------------------------
    with st.spinner("Training Prophet model..."):
        model = Prophet(
            changepoint_prior_scale=changepoint_prior_scale,
            seasonality_prior_scale=seasonality_prior_scale,
            seasonality_mode=seasonality_mode,
            weekly_seasonality=add_weekly,
            yearly_seasonality=add_yearly,
            daily_seasonality=False,
            holidays=holidays_df,                
            holidays_prior_scale=10.0,          
        )
        model.fit(train_df)

    # ------------------------------------------------------------
    # Predict on test set
    # ------------------------------------------------------------
    future_test = test_df[["ds"]]
    forecast_test = model.predict(future_test)

    pred_test_df = forecast_test[["ds", "yhat"]].merge(test_df[["ds"]], on="ds", how="inner")
    pred_test = pred_test_df.set_index("ds")["yhat"]

    if use_log:
        train_series = np.exp(train_df.set_index("ds")["y"])
        test_series = np.exp(test_df.set_index("ds")["y"])
        pred_test = np.exp(pred_test)
    else:
        train_series = train_df.set_index("ds")["y"]
        test_series = test_df.set_index("ds")["y"]

    # ------------------------------------------------------------
    # Metrics
    # ------------------------------------------------------------
    metrics = calculate_metrics(test_series, pred_test)

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
    # Future forecast
    # ------------------------------------------------------------
    last_date = close.index[-1]
    future_dates = pd.date_range(
        start=last_date + timedelta(days=1),
        periods=forecast_days,
        freq="B"
    )
    future_df = pd.DataFrame({"ds": future_dates})
    future_forecast_all = model.predict(future_df)

    if use_log:
        future_forecast = np.exp(future_forecast_all.set_index("ds")["yhat"])
        lower = np.exp(future_forecast_all.set_index("ds")["yhat_lower"])
        upper = np.exp(future_forecast_all.set_index("ds")["yhat_upper"])
    else:
        future_forecast = future_forecast_all.set_index("ds")["yhat"]
        lower = future_forecast_all.set_index("ds")["yhat_lower"]
        upper = future_forecast_all.set_index("ds")["yhat_upper"]

    # Clean forecast
    future_forecast = pd.to_numeric(future_forecast, errors="coerce").dropna()
    if future_forecast.empty:
        st.error("Forecast contains only invalid values. Please adjust parameters.")
        st.stop()

    lower = pd.to_numeric(lower, errors="coerce")
    upper = pd.to_numeric(upper, errors="coerce")

    forecast_df = forecast_table(future_forecast)

    # ------------------------------------------------------------
    # Visualizations
    # ------------------------------------------------------------
    st.subheader("📈 Actual vs Predicted (Test Set)")
    st.plotly_chart(
        actual_vs_predicted_chart(
            train=train_series,
            test=test_series,
            prediction=pred_test,
            model_name="Prophet",
        ),
        width="stretch",
    )
    st.info(
        """
        **Interpretation**  
        • Blue = training data  
        • Orange = actual unseen prices  
        • Green = Prophet predictions  
        A good model should follow the actual prices closely.
        """
    )

    st.divider()

    st.subheader("🔮 Future Forecast")
    st.plotly_chart(
        future_forecast_chart(
            historical=close,
            forecast=future_forecast,
            model_name="Prophet",
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
            model_name="Prophet",
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

    # ------------------------------------------------------------
    # Residual Analysis
    # ------------------------------------------------------------
    st.subheader("📉 Residual Analysis")
    left, right = st.columns(2)
    with left:
        st.plotly_chart(residual_plot(actual=test_series, prediction=pred_test), width="stretch")
    with right:
        st.plotly_chart(residual_distribution(actual=test_series, prediction=pred_test), width="stretch")
    st.info(
        """
        Residuals should be randomly scattered around zero.  
        Patterns suggest the model missed some structure.
        """
    )

    st.divider()

    # ------------------------------------------------------------
    # Forecast Values Table & Download
    # ------------------------------------------------------------
    st.subheader("📄 Forecast Values")
    display_df = forecast_df.copy()
    display_df["Forecast"] = display_df["Forecast"].round(2)
    st.dataframe(display_df, width="stretch", hide_index=True)

    st.divider()

    csv = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name=f"{ticker}_prophet_forecast.csv",
        mime="text/csv",
        key="prophet_download",
    )

    st.divider()

    # ------------------------------------------------------------
    # Forecast Summary with bulletproof numeric extraction
    # ------------------------------------------------------------
    st.subheader("📝 Forecast Summary")

    # Safely get latest price
    try:
        latest_price = float(close.iloc[-1])
    except (TypeError, ValueError):
        st.error("Latest price is invalid (non‑numeric or None).")
        st.stop()

    # Safely get predicted price
    try:
        predicted_val = future_forecast.iloc[-1]
        if pd.isna(predicted_val):
            raise ValueError("Predicted price is NaN")
        predicted_price = float(predicted_val)
    except (TypeError, ValueError, IndexError):
        st.error("Predicted price is invalid (non‑numeric or missing).")
        st.stop()

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