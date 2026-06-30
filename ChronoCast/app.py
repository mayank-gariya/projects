import streamlit as st
from PIL import Image 

st.set_page_config(
    page_title="ChronoCast – Time Series Analysis",
    page_icon="⏳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <h1 style="font-size: 4rem; margin-bottom: 0;">⏳ ChronoCast</h1>
        <p style="font-size: 1.5rem; color: #888;">Time Series Analysis & Forecasting Toolkit</p>
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

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📌 What is ChronoCast?")
    st.write(
        """
        ChronoCast is an interactive time series analysis application designed for:
        - **Data Exploration** – load data from Yahoo Finance or upload your own CSV.
        - **Statistical Tests** – ADF, KPSS, Ljung‑Box, ARCH, and more.
        - **Decomposition** – break down series into trend, seasonal, and residual components.
        - **Forecasting** – ARIMA, SARIMA, ARIMAX, and automatic model selection.
        - **Learning Hub** – expandable explanations of core time series concepts.

        All powered by a clean Streamlit interface – no coding required.
        """
    )

with col2:
    st.image(
        'src/assits/streamlit image.png',
        width=300,
        caption="Powered by Streamlit"
    )
    st.caption("_Placeholder logo – replace with your own image_")


st.markdown("---")
st.subheader("🚀 Key Features")

features = st.columns(4)
features[0].markdown(
    """
    #### 📈 Data Explorer
    - Fetch live data from Yahoo Finance  
    - Upload CSV / Excel files  
    - Interactive plotting
    """
)
features[1].markdown(
    """
    #### 🔬 Statistical Tests
    - Stationarity (ADF, KPSS)  
    - Autocorrelation (Ljung‑Box)  
    - Heteroskedasticity (ARCH)
    """
)
features[2].markdown(
    """
    #### 🔮 Forecasting
    - ARIMA / SARIMA  
    - ARIMAX with exogenous variables  
    - Automated model selection
    """
)
features[3].markdown(
    """
    #### 📚 Learning Hub
    - Concept expanders  
    - Definitions, formulas, and examples  
    - Built‑in references
    """
)

st.markdown("---")
st.subheader("🛠️ Tech Stack")

tech = st.columns(5)
tech[0].markdown("**Python** 3.10+")
tech[1].markdown("**Streamlit**")
tech[2].markdown("**yfinance**")
tech[3].markdown("**statsmodels**")
tech[4].markdown("**pandas / numpy**")

st.markdown("---")
st.subheader("📂 Project Structure")

# If you have a screenshot of your folder structure, place it in the project root
# and uncomment the following lines:
#
# try:
#     img = Image.open("folder_structure.png")
#     st.image(img, caption="Project folder structure", use_column_width=True)
# except FileNotFoundError:
#     st.info("💡 Place a screenshot named `folder_structure.png` in the root directory to show your project structure.")

# As a fallback, show a text representation (like in your question)
st.code(
    """
    ChronoCast/
    ├── app.py                 # Home page (this file)
    ├── pages/
    │   ├── 1_Data_Explorer.py
    │   ├── 2_Time_Series_Analysis.py
    │   ├── 3_Statistical_Tests.py
    │   ├── 4_Forecasting.py
    │   └── 5_Learn.py
    ├── src/
    │   ├── data/              # data loading & processing
    │   ├── forecasting/       # model definitions
    │   ├── models/            # ARIMA, SARIMA wrappers
    │   ├── tests/             # statistical tests
    │   ├── time_series/       # decomposition, visualisation helpers
    │   ├── utils/             # helpers
    │   └── __pycache__/
    └── visualisations/        # plotting utilities
    """,
    language="text"
)

st.markdown("---")
st.markdown(
    f"""
    <div style="text-align: center; color: #888; padding: 1rem 0;">
        Made with ❤️ by <a href="https://github.com/mayank-gariya" target="_blank">Mayank Gariya</a> &nbsp;·&nbsp;
        <a href="https://github.com/mayank-gariya/ChronoCast" target="_blank">GitHub Repository</a>
    </div>
    """,
    unsafe_allow_html=True
)