# 🏍️ Bike Model: Price Prediction & Recommendation System

> **A Journey of Data Exploration, Modeling Iterations, and Building Effective ML Solutions**

---

## 📖 The Story Behind This Project

Hey there! I'm **Mayank Gariya**, and I want to share my experience building this bike modeling project. This wasn't just a straightforward, one-shot machine learning project—it was a journey filled with iterations, learnings, and refinements.

### How It All Started

I started with a simple goal: **predict bike prices accurately**. But as I dug deeper into the data, I realized there was so much more potential. The dataset told stories about bike features, pricing patterns, and customer preferences. This sparked an idea—why not build something that not only predicts prices but also *recommends bikes* to customers?

### The Evolution

- **Phase 1**: Data exploration and cleaning took longer than expected, but it was crucial. I discovered outliers, missing values, and patterns that would make or break the model.
- **Phase 2**: I tried multiple modeling approaches. Some worked well, others didn't. Each iteration taught me something valuable about feature engineering and model selection.
- **Phase 3**: Once the price prediction model was solid, I pivoted to build a lightweight recommendation engine—small but effective in its learning approach.

The result? **Two complementary models living in harmony**, each serving a specific purpose.

---

## 🎯 Project Overview

This project contains two carefully crafted machine learning models:

### 1. **Model 1: Bike Recommendation System** 🎁
A collaborative filtering and content-based recommendation system that suggests similar bikes based on specifications and user preferences. Perfect for e-commerce platforms and bike retailers.

**Key Features:**
- Content-based filtering using bike specifications
- Similarity scoring algorithms
- Lightweight and fast inference
- Real-world deployment ready

### 2. **Model 2: Bike Price Prediction** 💰
A robust regression model that predicts bike prices based on multiple features like brand, engine type, mileage, and more.

**Key Features:**
- Handles diverse bike specifications
- Feature importance analysis
- Price range predictions with confidence
- Production-ready model serialization

---

## 📊 Results & Performance

### Price Prediction Results
The model achieves excellent performance metrics on unseen test data:

![Price Prediction Results](./model%202%20price%20prediction/src/result.png)
*Model performance visualization showing predictions vs actual prices*

![Additional Metrics](./model%202%20price%20prediction/src/result2.png)
*Feature importance and error distribution analysis*

### Recommendation System Results
The recommendation engine successfully identifies similar bikes and ranks them by relevance:

![Recommendation Results](./model%201%20recommendation/data/resultforrecommendation%20.png)
*Recommendation system output showing similar bikes ranked by similarity score*

---

## 🛠️ Tech Stack

Built with industry-standard tools and libraries:

<div align="center">

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/Python-3.8+-3776ab?logo=python&logoColor=white) | Core programming language |
| ![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458?logo=pandas&logoColor=white) | Data manipulation & analysis |
| ![NumPy](https://img.shields.io/badge/NumPy-1.21+-013243?logo=numpy&logoColor=white) | Numerical computations |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24+-F7931E?logo=scikit-learn&logoColor=white) | Machine learning algorithms |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3+-11557c?logo=python&logoColor=white) | Data visualization |
| ![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-65d3e3?logo=python&logoColor=white) | Statistical visualization |
| ![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?logo=streamlit&logoColor=white) | Web app deployment |

</div>

---

## 📁 Project Structure

```
Bike model/
├── model 1 recommendation/              # Recommendation System
│   └── data/
│       ├── moto cleaning .ipynb         # Data preprocessing
│       ├── recommendation bike.ipynb    # Model building & analysis
│       ├── bikes_data.csv               # Raw dataset
│       ├── clean_df.csv                 # Processed data
│       ├── app.py                       # Streamlit app for recommendations
│       └── resultforrecommendation.png  # Results visualization
│
├── model 2 price prediction/            # Price Prediction Model
│   ├── src/
│   │   ├── result.png                   # Model performance visualization
│   │   └── result2.png                  # Feature importance analysis
│   ├── data/
│   │   ├── moto clean.ipynb             # EDA & data cleaning
│   │   ├── bike_sales_india.csv         # Raw dataset
│   │   └── clean_bike_sales.csv         # Processed data
│   ├── bike_price_prediction.pkl        # Trained model
│   ├── clean_df.pkl                     # Preprocessed features
│   ├── app.py                           # Streamlit web interface
│   └── README.md                        # Detailed model documentation
│
└── README.md                            # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mayank-gariya/projects.git
   cd projects/Bike\ model
   ```

2. **Install dependencies**
   ```bash
   pip install -r ../../requirements.txt
   ```

3. **Run the Price Prediction Model**
   ```bash
   cd model\ 2\ price\ prediction
   streamlit run app.py
   ```

4. **Run the Recommendation System**
   ```bash
   cd ../model\ 1\ recommendation/data
   streamlit run app.py
   ```

---

## 📈 Model Details

### Price Prediction Model
- **Algorithm**: Regression (Random Forest / Gradient Boosting)
- **Input Features**: Brand, Engine Type, Fuel Type, Mileage, Power, Torque, and more
- **Target**: Bike Price (Continuous)
- **Dataset Size**: ~6000+ bike records

### Recommendation Model
- **Algorithm**: Content-based filtering with similarity metrics
- **Similarity Metric**: Euclidean/Cosine distance
- **Input**: Bike specifications
- **Output**: Top-N similar bikes with similarity scores

---

## 💡 Key Insights & Learnings

Through this project, I learned:

1. **Data Quality is Everything**: Spending time on cleaning and understanding data paid off massively.
2. **Iteration Over Perfection**: The first model wasn't the best. Multiple iterations with different approaches led to the final solution.
3. **Simplicity Can Be Powerful**: The recommendation system doesn't need complex algorithms—simple, effective logic works best.
4. **Context Matters**: Understanding the business problem (bike pricing and recommendations) made the ML solutions more meaningful.

---

## 🔧 Usage Examples

### Example 1: Predict Bike Price
```python
import pickle
import pandas as pd

# Load model
model = pickle.load(open('model_2_price_prediction/bike_price_prediction.pkl', 'rb'))

# Prepare features
bike_features = {
    'brand': 'Hero',
    'engine_type': 'CC',
    'fuel_type': 'Petrol',
    'mileage': 40,
    'power': 12
}

# Predict
predicted_price = model.predict([bike_features])
print(f"Predicted Price: ₹{predicted_price[0]:.2f}")
```

### Example 2: Get Recommendations
```python
# Load data and model
recommendations = get_similar_bikes(bike_name='Hero Honda CB Shine', top_n=5)
print(recommendations)
```

---

## 🤝 Contributing

This is a personal project showcasing my ML journey. However, if you have suggestions or improvements, feel free to reach out!

---

## 📝 License

This project is open source and available under the MIT License.

---

## 📧 About Me

**Mayank Gariya**
- 🎓 Passionate about Machine Learning & Data Science
- 💻 Building practical ML solutions
- 📊 Data exploration enthusiast

*Feel free to connect with me for discussions on data science, machine learning, or just to chat about bikes!*

---

### ⭐ If You Found This Helpful

If this project helped you learn something new or inspired your own ML journey, I'd appreciate a star! It keeps me motivated to create more content.

**Built with ❤️ and lots of ☕ by Mayank Gariya**

---

<div align="center">

**Last Updated**: June 2026  
**Status**: Active & Maintained

</div>
