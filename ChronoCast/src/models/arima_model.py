import streamlit as st
import pandas as pd
from datetime import timedelta

from src.forecasting.evaluating import (
    calculate_metrics,
    metrics_dataframe,
)

from src.forecasting.arima_model import (
    train_arima,
    forecast_arima,
    fit_and_forecast,
)

from src.utils.sidebar import sidebar_inputs
from src.data.utils import load_processed_data

from src.visualisations.forecast_charts import (
    actual_vs_predicted_chart,
    future_forecast_chart,
    confidence_interval_chart,
    residual_plot,
    residual_distribution,
    forecast_table,
)

ticker, start_date, end_date = sidebar_inputs()

data = load_processed_data(
    ticker,
    start_date,
    end_date,
)

if data is None:
    st.error("Unable to load stock data.")
    st.stop()
    
close = data["Close"]

forecast_days = st.sidebar.slider(
    "Forecast Horizon (Days)",
    min_value=7,
    max_value=180,
    value=30,
)

def arima_start_to_end():
    st.sidebar.subheader("ARIMA Parameters")

    col1 , col2 ,col3 = st.columns(3)
    with col1 :
        p = st.sidebar.number_input(
            "p (Auto-Regressive)",
            min_value=0,
            max_value=10,
            value=5,
        )
    with col2 :
        d = st.sidebar.number_input(
            "d (Differencing)",
            min_value=0,
            max_value=3,
            value=1,
        )
    with col3 :
        q = st.sidebar.number_input(
            "q (Moving Average)",
            min_value=0,
            max_value=10,
            value=0,
        )

    with st.spinner("Training ARIMA model..."):

        train, test, prediction, model = fit_and_forecast(
            close,
            order=(p, d, q),
        )
        
    metrics = calculate_metrics(
        test,
        prediction,
    )

    st.subheader("📊 Model Performance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "MAE",
            metrics["MAE"],
        )

    with col2:
        st.metric(
            "RMSE",
            metrics["RMSE"],
        )

    with col3:
        st.metric(
            "MAPE",
            f"{metrics['MAPE (%)']} %",
        )

    with col4:
        st.metric(
            "R² Score",
            metrics["R² Score"],
        )

    with st.expander("View Complete Metrics"):

        st.dataframe(
            metrics_dataframe(metrics),
            width="stretch",
            hide_index=True,
        )
        
    st.divider()

    future_model = train_arima(
        close,
        order=(p, d, q),
    )

    future_forecast = forecast_arima(
        future_model,
        periods=forecast_days,
    )

    future_dates = pd.date_range(
        start=close.index[-1] + timedelta(days=1),
        periods=forecast_days,
        freq="B",
    )

    future_forecast.index = future_dates

    forecast_result = future_model.get_forecast(
        steps=forecast_days,
    )

    confidence_interval = forecast_result.conf_int()

    confidence_interval.index = future_dates

    lower = confidence_interval.iloc[:, 0]
    upper = confidence_interval.iloc[:, 1]

    forecast_df = forecast_table(
        future_forecast,
    )

    st.subheader("📈 Actual vs Predicted")

    st.plotly_chart(
        actual_vs_predicted_chart(
            train=train,
            test=test,
            prediction=prediction,
            model_name="ARIMA",
        ),
        width="stretch",
    )

    st.info(
        """
        **Interpretation**

        • Blue line represents the training data.

        • Orange line represents the actual unseen prices.

        • Green line represents ARIMA predictions.

        A good forecasting model should closely follow the actual prices.
        """
    )

    st.divider()

    st.subheader("🔮 Future Forecast")

    st.plotly_chart(
        future_forecast_chart(
            historical=close,
            forecast=future_forecast,
            model_name="ARIMA",
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
            model_name="ARIMA",
        ),
        width="stretch",
    )

    st.info(
        """
        The shaded region represents the **95% confidence interval**.

        Wider intervals indicate greater uncertainty in future predictions.
        """
    )

    st.divider()


    st.subheader("📉 Residual Analysis")

    left, right = st.columns(2)

    with left:

        st.plotly_chart(
            residual_plot(
                actual=test,
                prediction=prediction,
            ),
            width="stretch",
        )

    with right:

        st.plotly_chart(
            residual_distribution(
                actual=test,
                prediction=prediction,
            ),
            width="stretch",
        )

    st.info(
        """
        Residuals should ideally be randomly distributed around zero.

        If obvious patterns exist, the model may not have captured
        all information in the time series.
        """
    )

    st.divider()

    st.subheader("📄 Forecast Values")

    display_df = forecast_df.copy()

    display_df["Forecast"] = display_df["Forecast"].round(2)

    st.dataframe(
        display_df,
        width="stretch",
        hide_index=True,
    )

    st.divider()

    forecast_csv = display_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Forecast CSV",
        data=forecast_csv,
        file_name=f"{ticker}_forecast.csv",
        mime="text/csv",
        key='Arima forecast'
    )

    st.divider()


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

        st.metric(
            "Current Price",
            f"${latest_price:.2f}",
        )

        st.metric(
            "Forecast Price",
            f"${predicted_price:.2f}",
        )

    with summary_col2:

        st.metric(
            "Expected Change",
            f"{change_pct:.2f}%",
        )

        st.metric(
            "Trend",
            trend,
        )

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

    • MAE : {metrics['MAE']}

    • RMSE : {metrics['RMSE']}

    • MAPE : {metrics['MAPE (%)']}%

    • R² Score : {metrics['R² Score']}

    ---

    Lower MAE, RMSE and MAPE values indicate better forecasting performance,
    while an R² value closer to 1 indicates a stronger fit.
    """
    )