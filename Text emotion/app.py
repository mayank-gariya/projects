import spaces
import re
import joblib
import gradio as gr
import spacy
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from spacy.lang.en.stop_words import STOP_WORDS

# 1. Setup NLTK and SpaCy dependencies
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
    nltk.download('wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('wordnet')
    
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

lemmatizer = WordNetLemmatizer()

logistic_regression_tfidf_model = joblib.load('logistic_regression_bow.pkl')
tfidf_vectorizer = joblib.load('vectorizer_tfidf.pkl')

# Extract feature names at startup for word mapping
feature_names = np.array(tfidf_vectorizer.get_feature_names_out())

# 3. Label mapping
label_mapping = {
    0: 'sadness',
    1: 'joy',
    2: 'love',
    3: 'anger',
    4: 'fear',
    5: 'surprise'
}

# 4. Include the text cleaning functions from your notebook (Kept identical)
def basic_cleaning(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = text.lower()
    return text

def fully_cleaned(text):
    cleaned = basic_cleaning(text)
    doc = nlp(cleaned)
    tokens = [token.text for token in doc]
    tokens = [token for token in tokens if token not in STOP_WORDS]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

# 5. Prediction & Interpretation function
@spaces.GPU
def predict_emotion_with_interpretation(text):
    if not text.strip():
        return "Unknown", []
        
    cleaned_text = fully_cleaned(text)
    text_tfidf = tfidf_vectorizer.transform([cleaned_text])
    
    # Get the predicted class index
    prediction = logistic_regression_tfidf_model.predict(text_tfidf)[0]
    predicted_emotion = label_mapping.get(prediction, "Unknown")
    
    # --- Interpretation Logic ---
    word_weights = {}
    if hasattr(logistic_regression_tfidf_model, "coef_"):
        # Get the coefficients assigned to features for the predicted class
        coefs = logistic_regression_tfidf_model.coef_[prediction]
        
        # Identify features present in the user's input string
        _, present_word_indices = text_tfidf.nonzero()
        
        for idx in present_word_indices:
            word = feature_names[idx]
            weight = coefs[idx]
            if weight > 0:  # Only look at words that positively correlate with this class
                word_weights[word] = weight

    # Break original text into words to build the highlight tuples for Gradio
    words = text.split()
    highlighted_output = []
    
    for word in words:
        # Match back using the exact basic cleaning and lemmatization logic
        clean_w = lemmatizer.lemmatize(basic_cleaning(word).strip())
        
        if clean_w in word_weights:
            # Append word with the classification label to highlight it
            highlighted_output.append((word + " ", predicted_emotion))
        else:
            highlighted_output.append((word + " ", None))
            
    return predicted_emotion, highlighted_output

# 6. Gradio Interface (Updated layout structure to present the interpretation)
with gr.Blocks(title="Emotion Classifier") as demo:
    gr.Markdown("# Emotion Classifier")
    gr.Markdown("Enter a sentence to classify its emotion and instantly see which words contributed to the prediction.")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(lines=5, placeholder="Enter text here...", label="Input Text")
            submit_btn = gr.Button("Classify Emotion")
            
        with gr.Column():
            output_label = gr.Textbox(label="Predicted Emotion")
            output_highlights = gr.HighlightedText(
                label="Word Contribution Interpretation",
                combine_adjacent=False,
                show_legend=True
            )
            
    submit_btn.click(
        fn=predict_emotion_with_interpretation,
        inputs=input_text,
        outputs=[output_label, output_highlights]
    )

# Launch the interface
if __name__ == "__main__":
    demo.launch()
