<!-- Project Header -->
<div align="center">
  <h1>🏠 Real Estate Price Prediction Model</h1>
  <p><strong>A Machine Learning Solution for Accurate Property Price Estimation</strong></p>
  
  ![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
  ![Python Version](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square)
  ![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
  
</div>

---

## 📋 About the Project

Welcome! This project is a sophisticated **real estate price prediction system** that leverages advanced machine learning techniques to estimate property values with impressive accuracy. Whether you're a real estate professional, investor, or someone curious about property valuation, this model provides data-driven insights into pricing dynamics.

The model takes various property characteristics—such as area, number of bedrooms, amenities, and location features—and outputs a predicted market price. It's built with production-ready code that's clean, scalable, and easy to integrate into your applications.

### ✨ Key Features

- **🎯 Intelligent Feature Engineering**: Polynomial features and derived metrics (area per bedroom ratio, etc.)
- **🔐 Robust Label Encoding**: Handles categorical variables with precision
- **📊 Professional Predictions**: Returns formatted price estimates in USD
- **⚡ Fast & Efficient**: Optimized preprocessing pipeline for real-time predictions
- **🛠️ Scikit-learn Integration**: Built on industry-standard libraries

---

## 🚀 Quick Start

### Prerequisites

Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/mayank-gariya/projects.git
cd projects/pro
```

2. **Install Dependencies**
```bash
pip install pandas numpy scikit-learn
```

3. **Verify Setup**
```python
python -c "import pandas; import numpy; import sklearn; print('✓ All dependencies installed!')"
```

### 🎮 Usage Example

```python
from app import predict_price

# Get a price prediction for a property
price = predict_price(
    area=5000,              # Square feet
    bedrooms=3,
    bathrooms=2,
    stories=2,
    mainroad=1,             # 1 = Yes, 0 = No
    guestroom=1,
    basement=1,
    hotwaterheating=1,
    airconditioning=1,
    parking=2,              # Number of parking spaces
    prefarea=1,
    furnishingstatus='furnished'  # 'furnished', 'semi-furnished', or 'unfurnished'
)

print(f"Estimated Price: {price}")
# Output: Estimated Price: $250,000.50
```

---

## 🧠 How It Works

### Feature Preprocessing Pipeline

The `FullFeaturePreprocessor` class handles the transformation journey:

1. **Label Encoding** - Converts categorical features (like furnishing status) into numerical values
2. **Polynomial Features** - Creates interaction terms to capture non-linear relationships
3. **Feature Engineering** - Generates meaningful derived features:
   - `area_per_bedroom`: Living space efficiency metric
   - `bathrooms_per_bedroom`: Bathroom-to-bedroom ratio

### Model Architecture

```
Input Features (12 parameters)
    ↓
Label Encoding (categorical → numerical)
    ↓
Polynomial Feature Expansion
    ↓
Feature Engineering
    ↓
Pre-trained ML Model
    ↓
Log-space Prediction
    ↓
Exponential Transform (inverse log)
    ↓
Final Price Estimate
```

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|-----------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Core Language |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data Manipulation & Analysis |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) | Numerical Computing |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) | Machine Learning |
| ![Jupyter](https://img.shields.io/badge/Jupyter-F37726?style=for-the-badge&logo=jupyter&logoColor=white) | Data Exploration & Analysis |

</div>

---

## 📁 Project Structure

```
pro/
├── app.py                      # Main application & prediction logic
├── models/
│   └── model.pkl              # Pre-trained ML model
└── README.md                  # This file
```

### File Descriptions

- **`app.py`** - Contains the `FullFeaturePreprocessor` class and `predict_price()` function for making predictions
- **`models/model.pkl`** - Serialized, trained machine learning model ready for inference

---

## 📊 Input Parameters Guide

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `area` | int | 1000-10000+ | Total property area in square feet |
| `bedrooms` | int | 1-6+ | Number of bedrooms |
| `bathrooms` | int | 1-4+ | Number of bathrooms |
| `stories` | int | 1-4 | Number of stories/floors |
| `mainroad` | int | 0-1 | Proximity to main road (1=Yes, 0=No) |
| `guestroom` | int | 0-1 | Has guest room (1=Yes, 0=No) |
| `basement` | int | 0-1 | Has basement (1=Yes, 0=No) |
| `hotwaterheating` | int | 0-1 | Has hot water heating (1=Yes, 0=No) |
| `airconditioning` | int | 0-1 | Has air conditioning (1=Yes, 0=No) |
| `parking` | int | 0-3+ | Number of parking spaces |
| `prefarea` | int | 0-1 | In preferred area (1=Yes, 0=No) |
| `furnishingstatus` | string | furnished, semi-furnished, unfurnished | Property furnishing status |

---

## 🎯 Use Cases

✅ **Real Estate Professionals** - Competitive market analysis and property valuation  
✅ **Property Investors** - Quick assessment of investment opportunities  
✅ **Homebuyers** - Fair market price estimation for negotiations  
✅ **Financial Institutions** - Automated property valuation for loan assessments  
✅ **Data Scientists** - Example of production-ready ML pipeline  

---

## 🔍 Model Performance Notes

The model uses **log-scale regression** for better prediction distribution, then transforms predictions back to actual prices. This approach:

- Reduces the impact of outliers
- Improves prediction accuracy for diverse price ranges
- Handles skewed price distributions effectively

---

## 🐛 Troubleshooting

### Issue: `FileNotFoundError: models/model.pkl`
**Solution:** Ensure the `models/model.pkl` file exists in the correct directory path relative to `app.py`

### Issue: `ValueError: Missing columns for polynomial transformation`
**Solution:** All required columns must be present in your input DataFrame. Check the parameter names match exactly.

### Issue: Division by zero in feature engineering
**Solution:** Bedrooms with value 0 are automatically handled (replaced with 1) to avoid division errors.

---

## 📈 Future Enhancements

🔮 **Planned Features:**
- Web API endpoint for cloud deployment
- Confidence intervals for predictions
- Model explainability (SHAP values)
- Real-time market trend analysis
- Multi-region model support

---

## 🤝 Contributing

I welcome contributions! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 💬 Get in Touch

I'd love to hear from you! Whether it's feedback, suggestions, or collaboration opportunities:

- **GitHub:** [@mayank-gariya](https://github.com/mayank-gariya)
- **Portfolio:** Check out my other projects on [GitHub](https://github.com/mayank-gariya)
- **Open to:** ML collaborations, real estate tech projects, data science discussions

---

<div align="center">

### Built with ❤️ by **Mayank Gariya**

*"Turning data into insights, one model at a time."*

⭐ If you found this helpful, please give it a star! 

![GitHub stars](https://img.shields.io/github/stars/mayank-gariya/projects?style=social)

</div>

---

## 📚 Resources & References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [NumPy Documentation](https://numpy.org/)
- [Real Estate Valuation Research](https://en.wikipedia.org/wiki/Real_estate_appraisal)

---

**Last Updated:** May 2026  
**Version:** 1.0.0
