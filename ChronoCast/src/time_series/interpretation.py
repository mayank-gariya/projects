import pandas as pd


def generate_report(
    decomposition,
    adf_result,
    kpss_result,
    rolling_mean,
    rolling_std,
    residuals,
):
    """
    Generates an automated interpretation report
    from the time series analysis.
    """

    report = []

    # ----------------------------
    # Trend
    # ----------------------------

    trend = decomposition.trend.dropna()

    if trend.iloc[-1] > trend.iloc[0]:
        report.append(
            "📈 **Trend:** A long-term upward trend is observed, indicating that the stock has generally appreciated over the selected period."
        )
    else:
        report.append(
            "📉 **Trend:** The long-term trend is downward, suggesting a gradual decline in price."
        )

    seasonal_strength = decomposition.seasonal.std()

    if seasonal_strength > 1:
        report.append(
            "🔄 **Seasonality:** Repeating seasonal fluctuations are visible, indicating periodic market behaviour."
        )
    else:
        report.append(
            "🔄 **Seasonality:** Very weak seasonal behaviour is detected. Price movements are primarily trend-driven."
        )

    adf_p = adf_result["p-value"]
    kpss_p = kpss_result["p-value"]

    if adf_p < 0.05 and kpss_p > 0.05:
        report.append(
            "✅ **Stationarity:** Both ADF and KPSS tests indicate the series is stationary."
        )

    elif adf_p > 0.05 and kpss_p < 0.05:
        report.append(
            "❌ **Stationarity:** The series is non-stationary. Differencing is recommended before forecasting."
        )

    else:
        report.append(
            "⚠️ **Stationarity:** Statistical tests provide mixed evidence regarding stationarity."
        )

    mean_change = abs(
        rolling_mean.iloc[-1] - rolling_mean.iloc[0]
    )

    std_change = abs(
        rolling_std.iloc[-1] - rolling_std.iloc[0]
    )

    if mean_change > 1:
        report.append(
            "📊 **Rolling Mean:** The rolling mean changes noticeably over time, suggesting that the average price level is not constant."
        )
    else:
        report.append(
            "📊 **Rolling Mean:** The rolling mean remains relatively stable."
        )

    if std_change > 1:
        report.append(
            "📉 **Volatility:** Rolling standard deviation varies across time, indicating changing market volatility."
        )
    else:
        report.append(
            "📉 **Volatility:** Market volatility remains fairly stable throughout the selected period."
        )

    resid_std = residuals.std()

    if resid_std > 5:
        report.append(
            "⚡ **Residuals:** Residual fluctuations remain relatively high, suggesting unexplained movements are still present."
        )
    else:
        report.append(
            "⚡ **Residuals:** Residual component appears relatively small, indicating that trend and seasonality explain much of the variation."
        )

    report.append(
        "💡 **Recommendation:** Based on the observed characteristics, ARIMA-based forecasting is appropriate. If stronger seasonal behaviour is observed, SARIMA should also be considered."
    )

    return report