from datetime import timedelta

import pandas as pd
import streamlit as st

from src.utils.sidebar import sidebar_inputs
from src.data.utils import load_processed_data

from src.forecasting.evaluating import (
    calculate_metrics,
    metrics_dataframe,
)

from src.visualisations.forecast_charts import (
    actual_vs_predicted_chart,
    future_forecast_chart,
    confidence_interval_chart,
    residual_plot,
    residual_distribution,
    forecast_table,
)

from src.forecasting.auto_arima import train_auto_arima , best_parameter , model_summary , get_aic , get_bic , Auto_fit_and_forecast , forecast_auto_arima 

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



def auto_arima_start_to_end():
    
    st.sidebar.header("Forecast Settings")

    forecast_days = st.sidebar.slider(
        "Forecast Horizon (Days)",
        min_value=7,
        max_value=180,
        value=30,
    )
    
    naive_model = train_auto_arima(close)
    
    st.header('AUTO ARIMA')
    
    with st.spinner("Training AUTO ARIMA model..."):
         AutoA_train, AutoA_test, AutoA_prediction, AutoA_model = Auto_fit_and_forecast(close)
    
    col1 , col2 , col3 = st.columns(3)
    
    with col1 : 
        st.metric(
            'Best parameters',
            f'{best_parameter(naive_model)}'
        )
    
    with col2 : 
        st.metric(
            'AIC',
            f'{get_aic(naive_model):.4f}'
        )
        
    with col3 :
        st.metric(
            'BIC',
            f'{get_bic(naive_model):.4f}'
        )
        
    st.divider()
    
    st.subheader('Modle summary')
    st.code(naive_model.summary().as_text(), language="text")
    
    st.divider()
    
    metrics = calculate_metrics(
        AutoA_test,
        AutoA_prediction,
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
    
    forecast, conf_int = naive_model.predict(
        n_periods=forecast_days,
        return_conf_int=True,
    )

    future_dates = pd.date_range(
        start=close.index[-1] + timedelta(days=1),
        periods=forecast_days,
        freq="B",
    )

    future_forecast = pd.Series(
        forecast,
        index=future_dates,
        name="Forecast",
    )

    lower = pd.Series(
        conf_int[:, 0],
        index=future_dates,
        name="Lower CI",
    )

    upper = pd.Series(
        conf_int[:, 1],
        index=future_dates,
        name="Upper CI",
    )

    forecast_df = forecast_table(future_forecast)
        
    st.subheader("📈 Actual vs Predicted")

    st.plotly_chart(
        actual_vs_predicted_chart(
            train=AutoA_train,
            test=AutoA_test,
            prediction=AutoA_prediction,
            model_name="AUTO ARIMA",
        ),
        width="stretch",
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
            model_name="AUTO ARIMA",
        ),
        width="stretch",
    )

    st.divider()

    st.subheader("📉 Residual Analysis")

    left, right = st.columns(2)

    with left:

        st.plotly_chart(
            residual_plot(
                actual=AutoA_test,
                prediction=AutoA_prediction,
            ),
            width="stretch",
        )

    with right:

        st.plotly_chart(
            residual_distribution(
                actual=AutoA_test,
                prediction=AutoA_prediction,
            ),
            width="stretch",
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


    csv = display_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name=f"{ticker}_forecast.csv",
        mime="text/csv",
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