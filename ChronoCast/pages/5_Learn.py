import streamlit as st

# Set page config
st.set_page_config(page_title="Time Series Learning Hub", layout="wide")


st.markdown(
    """
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <h1 style="font-size: 4rem; margin-bottom: 0;">🏫 Learning Hub</h1>
        <p style="font-size: 1.5rem; color: #888;">Time Series Analysis & Forecasting Learning</p>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto;">
            Built with <strong>Streamlit</strong>, <strong>yfinance</strong>, and <strong>statsmodels</strong> – 
            explore, test, and forecast your data with ease.
        </p>
        <br>
        <a href="https://github.com/mayank-gariya" target="_blank" style="text-decoration: none;">
            <img src="https://img.shields.io/badge/GitHub-mayank--gariya-181717?style=for-the-badge&logo=github" alt="GitHub">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

concepts = {
    "Definition": r"""
    **Time Series** is a sequence of data points collected or recorded at successive equally spaced points in time.  
    Examples: daily stock prices, hourly temperatures, monthly sales, annual GDP.  
    Key characteristics: temporal ordering, dependence between observations, and potential patterns.
    """,
    
    "Examples": r"""
    - **Financial**: Stock prices, exchange rates, trading volumes.
    - **Economic**: GDP, inflation, unemployment rates.
    - **Environmental**: Temperature, rainfall, air quality.
    - **Business**: Sales, website traffic, customer churn.
    - **Healthcare**: Heart rate, blood pressure, daily step counts.
    """,
    
    "Potential (Why analyze time series?)": r"""
    - **Forecasting**: Predict future values (e.g., sales next month).
    - **Monitoring**: Detect anomalies or changes in behavior.
    - **Understanding**: Uncover underlying patterns (trend, seasonality).
    - **Control**: Adjust processes based on predictions (e.g., inventory management).
    - **Signal Processing**: Extract meaningful signals from noise.
    """,
    
    "Decomposition": r"""
    **Time Series Decomposition** breaks a series into its constituent components:  
    - **Trend** (\(T_t\)): Long-term direction (upward/downward).  
    - **Seasonal** (\(S_t\)): Regular periodic fluctuations (e.g., weekly, yearly).  
    - **Cyclic** (\(C_t\)): Long-term oscillations without fixed period (often merged with trend).  
    - **Residual/Irregular** (\(R_t\)): Random noise left after removing T, S, C.  

    Additive: \(Y_t = T_t + S_t + C_t + R_t\)  
    Multiplicative: \(Y_t = T_t \times S_t \times C_t \times R_t\)  

    *Implementation*: Use `statsmodels.tsa.seasonal.seasonal_decompose`.
    """,
    
    "Trend, Seasonality, Residuals, Cyclicity": r"""
    - **Trend**: Persistent increase or decrease over time (e.g., population growth).  
    - **Seasonality**: Fixed periodic patterns (e.g., ice cream sales peak in summer).  
    - **Residuals**: What remains after removing trend and seasonality; should be white noise for a good model.  
    - **Cyclicity**: Fluctuations lasting more than one year, often linked to economic cycles (boom/bust). Unlike seasonality, cycles do not have a fixed period.
    """,
    
    "Stationarity (Weak & Strong)": r"""
    **Weak Stationarity** (or covariance stationary):  
    - Mean is constant over time.  
    - Variance is constant over time.  
    - Covariance between two time points depends only on the lag, not on the actual time.  

    **Strong Stationarity** (strict stationarity):  
    - The joint distribution of any set of observations is invariant to time shifts.  
    - Implies weak stationarity (if second moments exist).  

    Most time series models require at least weak stationarity.
    """,
    
    "Different Tests for Different Things": r"""
    - **Stationarity Tests**:  
      - **ADF (Augmented Dickey-Fuller)**: Tests for unit root (non-stationarity).  
      - **KPSS**: Tests for stationarity (opposite null).  
    - **White Noise / Independence**:  
      - **Ljung-Box** (portmanteau): Tests if autocorrelations are jointly zero.  
    - **Normality**: Shapiro-Wilk, Jarque-Bera.  
    - **Heteroskedasticity**: ARCH-LM test.  
    - **Causality**: Granger causality test (helps in forecasting with exogenous variables).
    """,
    
    "Problem with Stationarity": r"""
    **Why non-stationarity is problematic?**  
    - Model coefficients become unreliable (spurious regression).  
    - Forecasts are unstable and inefficient.  
    - Many statistical properties (like variance) are not finite.  
    - Most classical models (AR, MA, ARIMA) assume stationarity.  

    *Consequence*: You often need to transform the series to achieve stationarity before modeling.
    """,
    
    "Methods to Remove Non-Stationarity": r"""
    Common techniques to make a series stationary:  
    - **Differencing**: \(Y'_t = Y_t - Y_{t-1}\) (first difference). If needed, second difference.  
    - **Log Transformation**: Stabilises variance and can linearise exponential growth.  
    - **Detrending**: Fit a trend line (e.g., polynomial) and subtract it.  
    - **Seasonal Adjustment**: Subtract seasonal component (e.g., using STL or moving averages).  
    - **Box-Cox Transformation**: General power transformation to stabilise variance.
    """,
    
    "Visualisations": r"""
    Essential visual tools for time series:  
    - **Line plot**: Shows overall pattern (trend, seasonality, outliers).  
    - **Seasonal subseries plot**: Compares same season across years.  
    - **ACF (Autocorrelation Function)**: Correlation of series with its own lags. Helps identify MA order.  
    - **PACF (Partial Autocorrelation Function)**: Correlation after removing intermediate lags. Helps identify AR order.  
    - **Decomposition plots**: Show trend, seasonal, residual separately.  
    - **Histogram / Q-Q plot**: Check distribution of residuals.
    """,
    
    "What is AR (Autoregressive)?": r"""
    **AR(p)**: A model where the current value depends on its own previous values.  
    Formula: \(Y_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_p Y_{t-p} + \varepsilon_t\)  
    - \(\phi\) are coefficients, \(\varepsilon_t\) is white noise.  
    - Order \(p\) is the number of lags.  
    - Stationarity requires roots of characteristic polynomial to be outside the unit circle.  
    - PACF cuts off after lag p.
    """,
    
    "What is MA (Moving Average)?": r"""
    **MA(q)**: A model where the current value depends on past forecast errors.  
    Formula: \(Y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q}\)  
    - \(\theta\) are coefficients, \(\varepsilon_t\) is white noise.  
    - Invertibility requires roots to be outside unit circle.  
    - ACF cuts off after lag q.
    """,
    
    "ARIMA (and the 'I')": r"""
    **ARIMA(p,d,q)** combines AR, differencing (I), and MA:  
    - **p**: AR order.  
    - **d**: number of differences to achieve stationarity.  
    - **q**: MA order.  
    Model: \((1 - \sum_{i=1}^p \phi_i L^i)(1-L)^d Y_t = c + (1 + \sum_{j=1}^q \theta_j L^j)\varepsilon_t\)  
    - **I** stands for Integrated (the differencing part).  
    - ARIMA is suitable for non‑seasonal data. For seasonal data, use SARIMA.
    """,
    
    "ARIMAX (Exogenous Variables)": r"""
    **ARIMAX** extends ARIMA by including external (exogenous) variables.  
    Formula: \(Y_t = \alpha_1 X_{1t} + \dots + \alpha_k X_{kt} + \text{ARIMA errors}\)  
    - The exogenous part can be any external regressor (e.g., temperature, promotions).  
    - Useful when the target series is influenced by other factors.  
    - Also called **regression with ARIMA errors**.
    """,
    
    "Tests: ADF, KPSS, Ljung-Box": r"""
    - **ADF (Augmented Dickey-Fuller)**:  
      - Null hypothesis: series has a unit root (non-stationary).  
      - If p-value < 0.05, reject null → series is stationary.  
    - **KPSS (Kwiatkowski-Phillips-Schmidt-Shin)**:  
      - Null: series is stationary (around a deterministic trend).  
      - If p-value < 0.05, reject null → series is non-stationary.  
    - **Ljung-Box Test**:  
      - Null: autocorrelations up to lag k are zero (white noise).  
      - If p-value < 0.05, reject → significant autocorrelation remains (model may be incomplete).  
    """,
    
    "Other Important Tests": r"""
    - **White Noise**: Check with Ljung-Box or Box-Pierce.  
    - **Normality**: Shapiro-Wilk (for small samples) or Jarque-Bera.  
    - **Heteroskedasticity**: ARCH-LM (tests for conditional heteroskedasticity).  
    - **Granger Causality**: Tests if one time series helps predict another.  
    - **Structural Breaks**: Chow test, CUSUM, or Bai-Perron.
    """
}

for idx, (title, content) in enumerate(concepts.items()):
    with st.expander(f"📌 {title}", expanded=(idx == 0)):
        st.markdown(content)

st.markdown("---")
st.info("💡 **Tip**: Use these concepts together. For example, first visualize, then test stationarity, apply transformations if needed, and finally fit ARIMA/ARIMAX.")
st.caption("Made with ❤️ consider liking it ")
