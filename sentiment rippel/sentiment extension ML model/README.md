# 🌊 Sentiment Ripple - AI-Powered Chrome Extension

<div align="center">
  
![Sentiment Ripple](https://img.shields.io/badge/Sentiment%20Analysis-Chrome%20Extension-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=for-the-badge&logo=python)
![Machine%20Learning](https://img.shields.io/badge/Machine%20Learning-NLP-brightgreen?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi)
![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-grey?style=for-the-badge&logo=google-chrome)

A cutting-edge Chrome extension that analyzes sentiment in real-time using machine learning. Understand how public opinion ripples through communities with visual analytics and predictive bias modeling.

</div>

---

## 📺 Demo Video

Watch the sentiment analyzer in action:

[![Sentiment Ripple Demo](https://img.shields.io/badge/Watch%20Demo-Click%20Here-red?style=for-the-badge&logo=youtube)](https://github.com/mayank-gariya/projects/blob/main/sentiment%20rippel/sentiment%20extension%20ML%20model/negative%20reviews%20-%20Google%20Search%20-%20Google%20Chrome%202026-06-04%2020-51-40.mp4)

---

## 🎯 Project Overview

**Sentiment Ripple** is a comprehensive sentiment analysis system that combines:
- 🔍 Real-time text sentiment detection
- 🌊 Social influence ripple effect visualization
- 🤖 Machine Learning-powered predictions
- 📊 Interactive bias modeling and analytics

This project demonstrates how machine learning models can predict emotional responses and model how sentiments propagate through user populations.

---

## 🏗️ Architecture Overview

```
┌────────────────────────────────────────────────────────────┐
│                   Chrome Extension (Frontend)              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  popup.html / popup.js / background.js               │  │
│  │  - User Interface                                    │  │
│  │  - DOM Content Scraping                              │  │
│  │  - Message Passing                                   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────┬──────────────────────────────────────────┘
                  │ HTTP/CORS
                  
┌────────────────────────────────────────────────────────────┐
│              FastAPI Backend Server (Port 8000)            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  main.py                                             │  │
│  │  - FastAPI application                               │  │
│  │  - CORS middleware                                   │  │
│  │  - POST /predict endpoint                            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────┬──────────────────────────────────────────┘
                  │
                  ▼
┌────────────────────────────────────────────────────────────┐
│         ML Sentiment Prediction Pipeline                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  predictor.py                                        │  │
│  │  - Logistic Regression Model (trained)               │  │
│  │  - TF-IDF Vectorization                              │  │
│  │  - Sentiment Classification (Positive/Negative)      │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### **Frontend (Chrome Extension)**
| Technology | Purpose | Version |
|-----------|---------|---------|
| ![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black) | Extension Logic & DOM Interaction | ES6+ |
| ![HTML5](https://img.shields.io/badge/HTML5-Markup-E34C26?logo=html5&logoColor=white) | UI Structure | 5 |
| ![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3&logoColor=white) | Extension Styling | 3 |
| Chrome APIs | Content & Background Scripts | MV3 |

**Note on JavaScript Implementation:** 
> The JavaScript code (popup.js, background.js) was generated using Gemini AI assistant to handle Chrome extension messaging and DOM manipulation. I'm committed to learning JavaScript fundamentals deeply and will rebuild this component from scratch in future iterations to ensure complete code ownership and optimization. Currently, I have comprehensive understanding of the ML pipeline and backend architecture.

### **Backend (ML & API)**
| Technology | Purpose | Version |
|-----------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white) | Core Language | 3.9+ |
| ![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white) | REST API Framework | 0.100+ |
| ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8.0-F7931E?logo=scikit-learn) | Machine Learning | 1.8.0 |
| ![NLTK](https://img.shields.io/badge/NLTK-3.9.4-006633) | NLP Preprocessing | 3.9.4 |
| ![joblib](https://img.shields.io/badge/joblib-Model%20Serialization-009E73) | Model Persistence | Latest |
| ![Pandas](https://img.shields.io/badge/Pandas-2.3.3-150458?logo=pandas) | Data Processing | 2.3.3 |
| ![NumPy](https://img.shields.io/badge/NumPy-2.3.3-013243?logo=numpy) | Numerical Computing | 2.3.3 |

### **Data Visualization**
| Technology | Purpose | Version |
|-----------|---------|---------|
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.8-11557C) | Static Charts | 3.10.8 |
| ![Plotly](https://img.shields.io/badge/Plotly-6.7.0-3F4F75) | Interactive Plots | 6.7.0 |
| ![Gradio](https://img.shields.io/badge/Gradio-6.14.0-FF6B35) | Web Interface | 6.14.0 |

---

## 🔄 How It Works

### **Phase 1: Model Training**
1. **Data Preparation**: NLTK tokenization and text preprocessing
2. **Feature Extraction**: TF-IDF vectorization from training corpus
3. **Model Training**: Logistic Regression on sentiment-labeled dataset
4. **Serialization**: Model pipeline saved as `logistic_regression_pipeline.pkl`

### **Phase 2: Sentiment Analysis**
```
User Input Text
       ↓
┌─────────────────────────────────┐
│  Chrome Extension (Frontend)    │
│  - Extract/Scrape page content  │
│  - Send to backend              │
└─────────────────────────────────┘
       ↓
┌─────────────────────────────────┐
│  FastAPI Backend Server         │
│  - Receive text via POST /predict
│  - Pass to ML Pipeline          │
└─────────────────────────────────┘
       ↓
┌─────────────────────────────────┐
│  ML Prediction Pipeline         │
│  - TF-IDF Transform             │
│  - Logistic Regression Predict  │
│  - Return probability score     │
└─────────────────────────────────┘
       ↓
Display Results (Positive/Negative Sentiment Score)
```

### **Phase 3: Ripple Simulation & Analytics**
The system models how sentiment ripples through a population:

1. **Sentiment Foundation**: Initial sentiment score from ML model (0-1)
2. **Individual Biases**: Each user has unique bias offset (-0.2 to +0.2)
3. **Environmental Bias**: Global bias layer affecting entire population
4. **Decision Making**: `final_score = sentiment_score + individual_bias + env_bias`
5. **Visual Propagation**: Animated wave showing influence spreading through population
6. **Analytics Output**: Bar chart showing agreement vs. rejection distribution

---

## 📦 Installation & Setup

### **Prerequisites**
- Python 3.9 or higher
- Google Chrome/Chromium
- pip package manager

### **Backend Setup**

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Verify model file exists
ls backend/logistic_regression_pipeline.pkl

# 3. Start FastAPI server
cd backend
python main.py

# Output should show:
# Uvicorn running on http://127.0.0.1:8000
```

### **Chrome Extension Setup**

```bash
# 1. Open Chrome Extensions
# Go to: chrome://extensions/

# 2. Enable Developer Mode (top-right toggle)

# 3. Click "Load unpacked"

# 4. Navigate to: sentiment rippel/sentiment extension ML model/analyser_extension/

# 5. Extension is now active!
```

---

## 🎮 Usage Guide

### **Using the Chrome Extension**

1. **Navigate to any webpage** with text content
2. **Click the Sentiment Ripple extension icon** in Chrome toolbar
3. **Select text or use the "Analyze Page" button**
4. **View sentiment result**:
   - 🟢 **Positive**: Text expresses positive sentiment
   - 🔴 **Negative**: Text expresses negative sentiment
5. **View confidence score** (0-100%)

### **Using the Gradio Web Interface**

```bash
# Run the interactive demo
cd sentiment rippel
python app.py

# Opens at: http://127.0.0.1:7860
```

**Features in Gradio UI**:
- 📝 Enter broadcast message
- 👥 Set population size (1-21 users)
- ⚙️ Configure environmental bias
- 🚀 Start simulation
- 📊 Watch ripple effect animation
- 📈 See final analytics chart

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Model Type | Logistic Regression |
| Feature Extraction | TF-IDF Vectorization |
| Training Data | ~10,000 labeled reviews |
| Positive Class | 1 |
| Negative Class | 0 |
| Pipeline Accuracy | 85%+ |

---

## 📁 Project Structure

```
sentiment rippel/
├── sentiment extension ML model/
│   ├── analyser_extension/          # Chrome Extension
│   │   ├── manifest.json            # Extension configuration
│   │   ├── popup.html               # UI popup template
│   │   ├── popup.js                 # Frontend logic (Gemini-assisted)
│   │   └── background.js            # Background worker script
│   ├── backend/                     # Python Backend
│   │   ├── main.py                  # FastAPI server
│   │   ├── predictor.py             # ML prediction logic
│   │   └── logistic_regression_pipeline.pkl  # Trained model
│   └── negative reviews - Google Search.mp4  # Demo video
├── app.py                           # Gradio interactive demo
├── requirements.txt                 # Python dependencies
└── logistic_regression_pipeline.pkl # ML model
```

---

## 🚀 Future Improvements

### **Short Term**
- [ ] Rebuild JavaScript code from scratch (learning JS fundamentals)
- [ ] Add confidence thresholds
- [ ] Implement multi-language support
- [ ] Add review history tracking

### **Medium Term**
- [ ] Upgrade to BERT/Transformer-based models
- [ ] Real-time batch processing
- [ ] User preference customization
- [ ] Export sentiment analytics as CSV/JSON

### **Long Term**
- [ ] Sentiment emotion classification (joy, anger, fear, etc.)
- [ ] Sarcasm detection
- [ ] Domain-specific fine-tuning
- [ ] Mobile app version
- [ ] Cloud deployment with API scaling

---

## 🤝 Technical Notes

### **Why Logistic Regression?**
- ✅ Fast inference (ideal for extension)
- ✅ Interpretable predictions
- ✅ Low resource consumption
- ✅ Proven performance on binary classification
- ❓ Future: Plan to implement BERT for better accuracy

### **Architecture Decisions**
- **FastAPI**: Async support + automatic documentation
- **Uvicorn**: ASGI server for production performance
- **CORS Middleware**: Enable extension-to-backend communication
- **joblib**: Efficient ML model serialization

---

## ⚖️ Disclaimer & Learning Journey

**JavaScript Implementation Acknowledgment:**

The JavaScript code (popup.js, background.js) in this project was initially generated using Gemini AI assistant. While I understand the complete architecture and how the extension works, I acknowledge that:

- ✅ I have deep knowledge of the ML pipeline and Python backend
- ✅ I understand the Chrome Extension API concepts
- ✅ I understand async communication and CORS
- ❌ I am still learning JavaScript fundamentals (ES6+, async/await patterns, DOM manipulation)

**My Commitment:**
In future iterations, I will:
1. Learn JavaScript deeply (vanilla JS, async patterns, modern frameworks)
2. Rewrite the extension code from scratch
3. Optimize performance with better practices
4. Maintain complete code ownership

This project represents my journey from understanding AI/ML concepts to building end-to-end applications, and I'm committed to mastery in all technical areas.

---

## 📝 Requirements & Dependencies

```txt
gradio==6.14.0           # Web interface for demos
matplotlib==3.10.8       # Data visualization
matplotlib-inline==0.1.7 # Inline plotting
nltk==3.9.4             # NLP preprocessing
numpy==2.3.3            # Numerical computing
pandas==2.3.3           # Data manipulation
scikit-learn==1.8.0     # ML algorithms
plotly==6.7.0           # Interactive charts
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔗 Useful Resources

- [Chrome Extension Documentation](https://developer.chrome.com/docs/extensions/)
- [FastAPI Official Guide](https://fastapi.tiangolo.com/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [NLTK Tutorials](https://www.nltk.org/book/)
- [Gradio Documentation](https://www.gradio.app/)

---

## 📧 Contact & Support

For questions or suggestions about this project:

**Developer:** Mayank Gariya  
**Portfolio:** [GitHub Profile](https://github.com/mayank-gariya)  
**Project:** [Sentiment Ripple Repository](https://github.com/mayank-gariya/projects)

---

<div align="center">

### ⭐ If you find this project helpful, please star the repository!

**Built with ❤️ by Mayank Gariya**

*Last Updated: June 2026*

</div>

---

## 📜 License

This project is open source and available under the MIT License.

```
MIT License

Copyright (c) 2026 Mayank Gariya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🎓 Learning Resources Created

This project also serves as a learning resource for:
- Building Chrome Extensions from scratch
- Integrating Machine Learning with web applications
- RESTful API design with FastAPI
- NLP and Sentiment Analysis techniques
- Production-ready Python packaging

Feel free to fork and experiment!

