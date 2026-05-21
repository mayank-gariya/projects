import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from pathlib import Path

# Download NLTK resources
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))


def transform_text(text):
    text = text.lower()

    try:
        text = nltk.word_tokenize(text)
    except:
        return ""

    text = [word for word in text if word.isalnum()]

    text = [
        word for word in text
        if word not in stop_words
        and word not in string.punctuation
    ]

    text = [ps.stem(word) for word in text]

    return " ".join(text)


# Load files from model folder
MODEL_DIR = Path("model")

try:
    with open(MODEL_DIR / "vectorizer.pkl", "rb") as f:
        tfidf = pickle.load(f)

    with open(MODEL_DIR / "model.pkl", "rb") as f:
        model = pickle.load(f)

except Exception as e:
    st.error(f"Loading failed: {e}")
    st.stop()


st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📩"
)

st.title("📩 Email / SMS Spam Classifier")

input_sms = st.text_area(
    "Enter your message",
    placeholder="Type message here..."
)

if st.button("Predict"):

    if input_sms.strip() == "":
        st.warning("Please enter a message")

    else:
        transformed_sms = transform_text(input_sms)

        vector_input = tfidf.transform([transformed_sms])

        result = model.predict(vector_input)[0]

        if result == 1:
            st.error("🚨 Spam")
        else:
            st.success("✅ Not Spam")