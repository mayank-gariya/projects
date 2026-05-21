# 📩 Email & SMS Spam Classifier

A powerful machine learning application that classifies emails and SMS messages as spam or legitimate using advanced NLP techniques and a trained classification model.

---

## 🎯 Overview

This project implements a sophisticated spam detection system that uses **TF-IDF vectorization** combined with **machine learning classification** to identify unwanted messages with high accuracy. Whether you're protecting your inbox or analyzing message patterns, this classifier provides real-time spam detection capabilities.

### Key Features
✨ **Real-time Classification** - Instantly identify spam messages  
🔐 **Robust NLP Pipeline** - Advanced text preprocessing and stemming  
🎨 **User-friendly Interface** - Interactive web interface built with Streamlit  
⚡ **Fast Performance** - Optimized model inference  
📊 **Scalable Architecture** - Easily deployable and maintainable  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mayank-gariya/projects.git
   cd projects/sms_classifier
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download required NLTK data**
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will launch at `http://localhost:8501` in your default browser.

---

## 📊 How It Works

### Text Processing Pipeline

The classifier employs a comprehensive text preprocessing pipeline:

1. **Lowercase Conversion** - Normalize text case
2. **Tokenization** - Break text into individual words using NLTK
3. **Alphanumeric Filtering** - Remove special characters and punctuation
4. **Stop Word Removal** - Eliminate common words like "the", "is", "and"
5. **Stemming** - Reduce words to their root form using Porter Stemmer
6. **Vectorization** - Convert text to TF-IDF feature vectors

### Model Architecture

```
Input Text
    ↓
Text Preprocessing (Cleaning, Tokenization, Stemming)
    ↓
TF-IDF Vectorization
    ↓
Machine Learning Classifier
    ↓
Output (Spam / Not Spam)
```

---

## 🛠️ Tech Stack

<div align="center">

### Core Libraries

| **Library** | **Purpose** |
|:---:|:---:|
| ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) | Machine Learning & Classification |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) | Numerical Computing |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data Manipulation |
| ![NLTK](https://img.shields.io/badge/NLTK-154F5B?style=for-the-badge&logo=python&logoColor=white) | Natural Language Processing |
| ![SciPy](https://img.shields.io/badge/SciPy-0C55A7?style=for-the-badge&logo=scipy&logoColor=white) | Scientific Computing |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) | Web Interface |

### Versions
```
streamlit==1.45.1
scikit-learn==1.6.1
numpy==2.2.6
pandas==2.2.3
nltk==3.9.1
scipy==1.15.3
joblib==1.5.1
threadpoolctl==3.6.0
```

</div>

---

## 📁 Project Structure

```
sms_classifier/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── model/
│   ├── model.pkl          # Trained classifier model
│   └── vectorizer.pkl     # TF-IDF vectorizer
├── data/
│   └── [training datasets]
└── README.md              # This file
```

---

## 💡 Usage Examples

### Example 1: Legitimate Message
```
Input:  "Hi! Can we meet tomorrow at 3 PM?"
Output: ✅ Not Spam
```

### Example 2: Spam Message
```
Input:  "Congratulations! You've won $1,000,000. Click here to claim now!"
Output: 🚨 Spam
```

---

## 📈 Performance

The model achieves strong classification performance through:
- **TF-IDF Feature Engineering** - Captures the importance of words in documents
- **Optimized Preprocessing** - Removes noise while preserving signal
- **Trained Classification Model** - Learned patterns from labeled spam/ham data

---

## 🔧 Development

### Making Improvements

To enhance the classifier:

1. **Update the training data** in the `data/` folder
2. **Retrain the model** with improved preprocessing logic
3. **Experiment with different algorithms** (SVM, Naive Bayes, etc.)
4. **Optimize hyperparameters** for better accuracy
5. **Add new features** for enhanced detection

### Contributing

Feel free to fork this repository and submit pull requests with improvements!

---

## 📝 Model Details

- **Algorithm**: Naive Bayes Classifier
- **Feature Extraction**: TF-IDF Vectorization
- **Training Approach**: Supervised Learning
- **Input**: Raw text messages
- **Output**: Binary classification (Spam / Not Spam)

---

## ⚠️ Limitations & Future Enhancements

### Current Limitations
- Binary classification (Spam vs. Not Spam)
- Requires model retraining for domain-specific datasets
- May not catch sophisticated phishing attempts

### Future Improvements
- 🔮 Multi-language support
- 🔮 Deep learning models (LSTM, Transformers)
- 🔮 Real-time model updates
- 🔮 Confidence score display
- 🔮 Multi-class classification (Spam, Phishing, Legitimate, Promotional)

---

## 📜 License

This project is open source and available under the MIT License.

---

## 🤝 Connect With Me

Feel free to reach out and connect on various platforms:

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mayank-gariya)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/mayank-gariya)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/mayank_gariya)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your-email@example.com)

</div>

---

## 📧 Questions & Support

Have questions or need help? Feel free to:
- Open an issue on GitHub
- Check existing discussions
- Reach out directly

---

<div align="center">

**Made with ❤️ by [Mayank Gariya](https://github.com/mayank-gariya)**

*If you found this project helpful, please consider giving it a ⭐!*

</div>

---

### Version History
- **v1.0.0** (May 2026) - Initial release with core spam classification functionality

