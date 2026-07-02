# 📊 ChronoCast: Time Series Analysis & Forecasting Playground

A comprehensive, interactive web application for learning and experimenting with time series analysis and forecasting models. Built with Streamlit, this project transforms complex time series concepts into an intuitive, hands-on experience.

**Live Demo:** [https://projects-kjut26fcmmjcdsgawmgey2.streamlit.app/](https://projects-kjut26fcmmjcdsgawmgey2.streamlit.app/)

**GitHub Repository:** [mayank-gariya/projects/ChronoCast](https://github.com/mayank-gariya/projects/blob/main/ChronoCast)

---

## 🎯 Project Vision

The goal wasn't to predict stock prices perfectly (that's nearly impossible). Instead, I wanted to build a **sandbox where you can tweak parameters and instantly see how they affect forecasts** — making time series concepts tangible and interactive.

This project is a **learning-focused initiative** designed for understanding time series principles, not for production-level forecasting accuracy.

---

## 💡 Origin Story: From Idea to Implementation

### The Inspiration
While learning time series analysis, I realized that understanding concepts and seeing them in action are two different things. I wanted to create a platform where learners could:
- Visualize theoretical concepts in real-time
- Experiment with different models and parameters
- Understand what works and why

### The Approach
Rather than building another "black-box" forecasting tool, I decided to create an **interactive simulation project** where users can:
1. Select different forecasting models
2. Adjust parameters in real-time
3. Instantly compare results
4. Learn from visual feedback

This approach transforms passive learning into active experimentation.

---

## 🔍 What ChronoCast Does

### Core Features

#### 📈 **Data Exploration**
- Fetch live stock data via `yfinance`
- Interactive time series visualization
- Historical data analysis and trends

#### 🧪 **Statistical Testing**
- **ADF Test** (Augmented Dickey-Fuller) - Check stationarity
- **KPSS Test** - Alternative stationarity test
- **Ljung-Box Test** - Test for autocorrelation
- **ARCH Test** - Detect heteroscedasticity

#### 📊 **Time Series Decomposition**
- Visualize trend components
- Identify seasonal patterns
- Analyze residuals
- Interactive decomposition plots

#### 🔮 **Multi-Model Forecasting**
- **ARIMA** - Classical statistical model with manual (p,d,q) tuning
- **SARIMA** - ARIMA with seasonal components
- **Auto ARIMA** - Automated parameter selection
- **Prophet** - Facebook's robust forecasting model

#### 📉 **Performance Metrics**
- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)
- **MAPE** (Mean Absolute Percentage Error)
- **R²** (Coefficient of Determination)

#### ⚙️ **Interactive Parameter Tuning**
- Adjust (p,d,q) parameters for ARIMA
- Configure seasonality settings for Prophet
- Apply log-transformations
- Include/exclude holiday effects
- Real-time forecast updates

#### 📚 **Learning Hub**
- Short concept explanations
- Model descriptions
- Parameter guidance
- Statistical test interpretations

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Web Framework:** Streamlit
- **Data Sources:** yfinance (live stock data)
- **Time Series Libraries:**
  - `statsmodels` (ARIMA, SARIMA, statistical tests)
  - `prophet` (Facebook's Prophet)
  - `auto-arima` (Automated ARIMA selection)
- **Data Processing:** pandas, NumPy
- **Machine Learning:** scikit-learn
- **Statistics:** scipy

---

## 🚀 Features Overview

### 1. **Data Analysis & Visualization**
- Live stock price data fetching
- Interactive Plotly visualizations
- Time series decomposition charts
- Statistical test results display

### 2. **Stationarity Testing**
- Run multiple statistical tests in one click
- Understand p-values and test interpretations
- Guidance on when to difference the data

### 3. **Model Comparison**
- Side-by-side forecast comparisons
- Performance metrics dashboard
- Visual accuracy assessment

### 4. **Educational Component**
- Concept explanations for each test
- Model selection guidance
- Parameter tuning tips
- Common pitfalls and best practices

---

## 📂 Project Structure

```
ChronoCast/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── modules/
│   ├── data_fetcher.py      # yfinance integration
│   ├── statistical_tests.py  # ADF, KPSS, Ljung-Box, ARCH tests
│   ├── time_series_utils.py # Decomposition and preprocessing
│   ├── forecasting_models.py # ARIMA, SARIMA, Prophet implementations
│   └── visualization.py      # Plotly charts and UI components
├── docs/
│   └── concepts.md          # Learning materials
└── README.md                # This file
```

---

## 🎮 How to Use

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mayank-gariya/projects.git
   cd projects/ChronoCast
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   Navigate to `http://localhost:8501`

### Using the Live Demo
Simply visit: [https://projects-kjut26fcmmjcdsgawmgey2.streamlit.app/](https://projects-kjut26fcmmjcdsgawmgey2.streamlit.app/)

### Step-by-Step Workflow

1. **Select Stock Symbol** - Enter any valid ticker (AAPL, GOOGL, TSLA, etc.)
2. **Choose Date Range** - Pick your analysis period
3. **Run Statistical Tests** - Check if your data is stationary
4. **Visualize Decomposition** - See trend, seasonality, and residuals
5. **Select Models** - Choose forecasting models to compare
6. **Tune Parameters** - Adjust (p,d,q) for ARIMA or settings for Prophet
7. **Generate Forecast** - Create forecasts with your chosen model
8. **Compare Performance** - View metrics and accuracy

---

## ⚠️ Known Issues

### Current Bug
When opening the forecast page for the first time, you might encounter a "same ID error". 

**Solution:** Simply **reload the page** and everything will work smoothly.

This is a known issue we're actively working on and will be resolved in the next update.

---

## 🔮 Future Roadmap

This project is just the beginning! Planned enhancements include:

- **🤖 Machine Learning Models**
  - XGBoost for time series forecasting
  - Gradient Boosting methods

- **🧠 Deep Learning Models**
  - LSTM (Long Short-Term Memory)
  - GRU (Gated Recurrent Unit)
  - Transformer-based models

- **🔗 Hybrid Models**
  - ARIMA + Prophet ensemble
  - ARIMA + XGBoost combination
  - Weighted model averaging

- **⚡ AutoML**
  - Automated model selection
  - Hyperparameter optimization
  - Best model recommendation engine

- **📊 Advanced Analytics**
  - Confidence interval visualization
  - Anomaly detection
  - Multiple step-ahead forecasting

- **💾 Data Management**
  - Export forecasts to CSV
  - Save model configurations
  - User dashboard with history

---

## 🤝 Contributing

This project is **open-source** and welcomes contributions! 

### How to Contribute

1. **Find Issues** - Check GitHub Issues for bugs and feature requests
2. **Fork & Branch** - Create a new branch for your contribution
3. **Make Changes** - Implement your fix or feature
4. **Test Thoroughly** - Ensure your changes work as expected
5. **Submit PR** - Open a pull request with a clear description

### Contribution Areas
- 🐛 Bug fixes (especially the session ID error)
- ✨ New forecasting models
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- 📈 New statistical tests
- 🧪 Test coverage

---

## 📚 Resources & Articles

- **Medium Article:** [ChronoCast: The Time Series Project](https://medium.com/@mayankgariya482/chronocast-the-time-series-project-320f2e33fb71)
- **LinkedIn Post:** [Project Announcement](https://www.linkedin.com/posts/mayank-gariya-564124401_machinelearning-datascience-timeseries-share-7478425410137903104-c2AP/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGa2HBwBNh9dY-L-ZL5HInhV_NmnJH5J2vA)

---

## 📖 Learning Resources

### Time Series Concepts Covered
- **Stationarity** - What it is and why it matters
- **Differencing** - Making data stationary
- **Autocorrelation (ACF)** - Understanding data relationships
- **Partial Autocorrelation (PACF)** - Identifying ARIMA parameters
- **Seasonality** - Patterns that repeat over time
- **ARIMA Components** - AR, I, MA explained
- **Prophet Model** - Trend + seasonality + holidays approach

### Recommended Learning Path
1. Start with data exploration and visualization
2. Run stationarity tests to understand your data
3. Try decomposing the time series
4. Experiment with ARIMA using Auto ARIMA first
5. Compare with Prophet
6. Adjust parameters based on visual feedback

---

## 📊 Key Metrics & Performance

The application evaluates models using:
- **MAE** - Average prediction error (intuitive)
- **RMSE** - Penalizes larger errors (sensitive to outliers)
- **MAPE** - Percentage error (scale-independent)
- **R²** - Explained variance (0-1 scale)

*Note: These metrics are for comparison purposes. Real-world forecasting is more complex and requires domain expertise.*

---

## 💡 Disclaimer

This project is designed for **learning and experimentation purposes**. It should not be used for actual financial investment decisions. Time series forecasting is inherently uncertain, and past performance doesn't guarantee future results.

---

## 📝 License

This project is open-source and available under the MIT License.

---

## 👤 About the Creator

**Mayank Gariya**

Building data science projects with a focus on practical learning and interactive education.

- 🔗 LinkedIn: [linkedin.com/in/mayank-gariya](https://www.linkedin.com/in/mayank-gariya-564124401/)
- 📝 Medium: [@mayankgariya482](https://medium.com/@mayankgariya482)
- 💻 GitHub: [mayank-gariya](https://github.com/mayank-gariya)

---

## 🎓 What You'll Learn

By exploring ChronoCast, you'll understand:

✅ How to fetch and preprocess real-world time series data  
✅ How to test for stationarity and why it matters  
✅ How to decompose time series into components  
✅ How ARIMA models work and how to tune them  
✅ How Prophet handles trend and seasonality  
✅ How to evaluate and compare forecasting models  
✅ Best practices in time series analysis  
✅ Common pitfalls and how to avoid them  

---

## 🚀 Get Started

👉 **Try the live demo:** [https://projects-kjut26fcmmjcdsgawmgey2.streamlit.app/](https://projects-kjut26fcmmjcdsgawmgey2.streamlit.app/)

👉 **Contribute on GitHub:** [mayank-gariya/projects](https://github.com/mayank-gariya/projects)

---

**Made with ❤️ for the data science community**

*Last Updated: 2024*
