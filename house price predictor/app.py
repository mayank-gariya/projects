import gradio as gr
import joblib
import pandas as pd
import numpy as np

# Load the saved model pipeline
loaded_pipeline = joblib.load('model.pkl')

# Define the feature columns as they were used during model training
# This list must match the order and names of features X_train was composed of.
FEATURE_COLUMNS = [
    'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
    'basement', 'hotwaterheating', 'airconditioning', 'parking',
    'prefarea', 'furnishingstatus'
]

# Define the prediction function that will be used by Gradio
def predict_price(
    area,
    bedrooms,
    bathrooms,
    stories,
    mainroad,
    guestroom,
    basement,
    hotwaterheating,
    airconditioning,
    parking,
    prefarea,
    furnishingstatus
):
    # Map 'Yes'/'No' inputs to 1/0 for binary categorical features
    mainroad_val = 1 if mainroad == 'Yes' else 0
    guestroom_val = 1 if guestroom == 'Yes' else 0
    basement_val = 1 if basement == 'Yes' else 0
    hotwaterheating_val = 1 if hotwaterheating == 'Yes' else 0
    airconditioning_val = 1 if airconditioning == 'Yes' else 0
    prefarea_val = 1 if prefarea == 'Yes' else 0

    # Map furnishingstatus to its encoded numerical value
    furnishing_map = {'furnished': 0, 'semi-furnished': 1, 'unfurnished': 2}
    furnishingstatus_val = furnishing_map.get(furnishingstatus, 2) # Default to 'unfurnished' if not found

    # Create a DataFrame from the inputs, ensuring correct column order
    input_data = pd.DataFrame([[area, bedrooms, bathrooms, stories, mainroad_val, guestroom_val,
                                  basement_val, hotwaterheating_val, airconditioning_val, parking,
                                  prefarea_val, furnishingstatus_val]],
                              columns=FEATURE_COLUMNS) # Use the defined FEATURE_COLUMNS

    # Make prediction using the loaded pipeline
    prediction = loaded_pipeline.predict(input_data)[0]

    return f"Predicted Price: {prediction:,.2f} INR"

# Define Gradio input components
inputs = [
    gr.Number(label="Area (sq ft)", value=5900),
    gr.Number(label="Bedrooms", value=4, precision=0),
    gr.Number(label="Bathrooms", value=2, precision=0),
    gr.Number(label="Stories", value=2, precision=0),
    gr.Radio(choices=["No", "Yes"], label="Main Road Access", value="No"),
    gr.Radio(choices=["No", "Yes"], label="Guest Room", value="No"),
    gr.Radio(choices=["No", "Yes"], label="Basement", value="Yes"),
    gr.Radio(choices=["No", "Yes"], label="Hot Water Heating", value="No"),
    gr.Radio(choices=["No", "Yes"], label="Air Conditioning", value="No"),
    gr.Number(label="Parking Spaces", value=1, precision=0),
    gr.Radio(choices=["No", "Yes"], label="Preferred Area", value="No"),
    gr.Dropdown(choices=["furnished", "semi-furnished", "unfurnished"], label="Furnishing Status", value="semi-furnished")
]

# Create the Gradio interface
interface = gr.Interface(
    fn=predict_price,
    inputs=inputs,
    outputs="text",
    title="House Price Prediction",
    description="Enter the features of the house to get a price prediction."
)

# Launch the app
if __name__ == "__main__":
    interface.launch(share=True)