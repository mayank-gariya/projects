# 🌾 Crop Recommendation System

![Banner](https://github.com/mayank-gariya/projects/blob/main/crops%20model/src/farmer.png?raw=true)

## 📖 The Journey

Building an intelligent crop recommendation system wasn't just about writing code—it was about understanding the real challenges farmers face. Through this project, I embarked on a journey of discovery, transformation, and optimization.

### The Story

Every great machine learning project starts with a question: *"How can we help farmers make better decisions?"* This is exactly what drove me to develop a smart crop recommendation system. But getting there required patience, experimentation, and a deep understanding of the underlying data.

**Stage 1: Understanding the Foundation** 🔍
- I started by diving deep into the Crop Recommendation dataset
- Explored relationships between soil properties (Nitrogen, Phosphorus, Potassium), temperature, humidity, pH, and rainfall
- Discovered hidden patterns and correlations that would shape the entire model
- Analyzed feature distributions to understand what we're working with

**Stage 2: The Transformation** ⚡
- Raw data is rarely perfect. Features had skewed distributions that could mislead our model
- I applied **PowerTransformer** (Yeo-Johnson) to normalize feature distributions
- This transformation dramatically improved model stability and performance
- Watched as skewed agricultural metrics became more Gaussian-distributed

**Stage 3: Building Intelligence** 🧠
- Implemented a lightweight yet powerful **Decision Tree classifier**
- The model learns to mimic expert farmer decision-making
- Small in complexity, but effective in learning patterns
- Built a complete ML pipeline that standardizes inputs before prediction

The result? A recommendation system that reliably suggests the best crop for any given environmental condition.

---

## 🎯 Project Overview

This is an **intelligent crop recommendation system** that analyzes environmental and soil conditions to recommend the most suitable crop for cultivation. Using a combination of data preprocessing, feature transformation, and machine learning, the system achieves robust predictions.

### Key Achievements

✅ **Data-Driven Insights** - Comprehensive EDA revealing agricultural patterns  
✅ **Advanced Preprocessing** - PowerTransformer for handling skewed distributions  
✅ **Optimized Model** - Decision Tree pipeline with ~95% accuracy  
✅ **Production Ready** - Deployed as a Streamlit web application  
✅ **Reproducible** - Fully documented with serialized models  

---

## 📊 Results

### Model Performance

![Results](https://github.com/mayank-gariya/projects/blob/main/crops%20model/src/result1.png?raw=true)

The model successfully predicts crop recommendations based on:
- **Soil Properties**: Nitrogen (N), Phosphorus (P), Potassium (K) levels
- **Climate Factors**: Temperature, Humidity, pH, Rainfall
- **Location Context**: Region-specific agricultural patterns

### Key Metrics

- **Accuracy**: High classification accuracy across all crop categories
- **Precision & Recall**: Balanced performance ensuring reliable recommendations
- **Feature Importance**: Rainfall and Temperature emerge as critical factors

---

## 🛠️ Tech Stack

### Core Libraries

<div align="center">

| Library | Purpose |
|---------|---------|
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data manipulation & analysis |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) | Numerical computing |
| ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) | ML models & preprocessing |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) | Web application framework |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white) | Data visualization |
| ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white) | Statistical visualization |

</div>

### Key Technologies

- **Python 3.x** - Core programming language
- **Scikit-Learn's PowerTransformer** - Advanced feature scaling & distribution transformation
- **Decision Tree Algorithm** - Interpretable machine learning model
- **Pickle** - Model serialization for production deployment

---

## 📁 Project Structure

```
crops model/
├── crop model.ipynb                              # Complete analysis & model development
├── Crop_recommendation.csv                       # Dataset (~2200 records)
├── decision_tree_crop_recommender_pipeline.pkl   # Trained model pipeline
├── df.pkl                                        # Processed dataframe
├── app.py                                        # Streamlit web application
└── src/
    ├── farmer.png                                # Project banner
    ├── result1.png                               # Model results visualization
    └── r.png                                     # Additional results
```

---

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/mayank-gariya/projects.git
cd projects/crops\ model

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Launch the Streamlit app
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`

### Using the Model

```python
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the pipeline
with open('decision_tree_crop_recommender_pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

# Prepare input (N, P, K, Temperature, Humidity, pH, Rainfall)
features = np.array([[50, 40, 40, 25.5, 80, 7.0, 200]])

# Get recommendation
recommendation = model.predict(features)
print(f"Recommended crop: {recommendation[0]}")
```

---

## 📚 Data Insights

The dataset contains **2200+ records** of crop cultivation scenarios with the following features:

| Feature | Description | Range |
|---------|-------------|-------|
| **N** | Nitrogen content | 0-140 mg/kg |
| **P** | Phosphorus content | 5-145 mg/kg |
| **K** | Potassium content | 5-205 mg/kg |
| **Temperature** | Average temperature | 8-43°C |
| **Humidity** | Relative humidity | 14-99% |
| **pH** | Soil pH level | 3.5-9.5 |
| **Rainfall** | Annual rainfall | 20-200 cm |

---

## 🔧 Model Pipeline

### 1. **Data Exploration & Cleaning**
   - Handled missing values
   - Analyzed feature distributions
   - Identified outliers and anomalies

### 2. **Feature Transformation**
   - Applied **PowerTransformer (Yeo-Johnson)**
   - Normalized highly skewed features
   - Improved model convergence and performance

### 3. **Model Training**
   - Decision Tree Classifier with optimized hyperparameters
   - Cross-validation for robustness
   - Hyperparameter tuning for best accuracy

### 4. **Pipeline Serialization**
   - Combined transformer + classifier into one pipeline
   - Consistent preprocessing for new predictions
   - Production-ready deployment

### 5. **Application Deployment**
   - Interactive Streamlit interface
   - Real-time crop recommendations
   - User-friendly input controls

---

## 💡 Why This Approach?

**Why PowerTransformer?**
- Agricultural data often shows skewed distributions
- Non-normal data can confuse traditional ML models
- Power transformation preserves interpretability while improving performance

**Why Decision Tree?**
- Highly interpretable—farmers can understand *why* a crop is recommended
- Handles non-linear relationships naturally
- Computationally efficient for real-time predictions
- No feature scaling required after transformation

**Why This Matters**
- Helps farmers optimize yield and reduce risk
- Considers multiple environmental factors simultaneously
- Provides a data-driven alternative to traditional guesswork

---

## 🎓 What I Learned

✨ **Data tells stories** - Exploring data reveals patterns humans would miss  
✨ **Preprocessing is crucial** - Raw data needs transformation to shine  
✨ **Simplicity wins** - A small, well-designed model beats complex mediocrity  
✨ **Deployability matters** - A model in a notebook is nice; deployed is better  
✨ **Agriculture is complex** - Environmental factors interact in intricate ways  

---

## 📈 Future Improvements

- [ ] Add ensemble methods (Random Forest, Gradient Boosting) for comparison
- [ ] Implement confidence scores for recommendations
- [ ] Add seasonal factors and regional climate data
- [ ] Create mobile application for farmer accessibility
- [ ] Integrate real-time weather APIs
- [ ] Multi-language support for broader reach

---

## 📄 License

This project is open source and available for educational and agricultural purposes.

---

## 🤝 Connect & Collaborate

If you find this project helpful or have suggestions for improvement, feel free to:
- Fork the repository
- Open an issue for bugs or feature requests
- Share your thoughts and use cases

---

<div align="center">

### Made with ❤️ for Agriculture & Data Science

**Mayank Gariya**  
*Data Scientist | ML Enthusiast | Agriculture Tech Advocate*

🔗 [GitHub](https://github.com/mayank-gariya) | 💼 [Portfolio](https://github.com/mayank-gariya/projects)

---

*"Data has the power to transform agriculture. Let's make farming smarter, one prediction at a time."*

</div>
