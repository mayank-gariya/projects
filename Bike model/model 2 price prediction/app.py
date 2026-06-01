import gradio as gr
import pickle
import pandas as pd
import sys
import sklearn

# 1. Load the data and model outside the function
try:
    with open('bike_price_prediction.pkl', 'rb') as f:
        pipe = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    print(f"CRITICAL ERROR: Could not load the model: {e}")
    sys.exit(1) # Stop the script if the model is missing

try:
    with open('clean_df.pkl', 'rb') as f:
        df = pickle.load(f)
except Exception as e:
    print(f"CRITICAL ERROR: Could not load the dataframe: {e}")
    sys.exit(1)

# 2. Use 'global' keyword if needed, though usually not required for reading
def predict_price(state, brand, engine_capacity, fuel_type, mileage, owner_type, insurance_status, seller_type, resale_price, city_tier):
    # Ensure pipe is accessible
    global pipe 
    
    test_df = pd.DataFrame({
        'state': [state],
        'brand': [brand],
        'engine_capacity': [engine_capacity],
        'fuel_type': [fuel_type],
        'mileage': [mileage],
        'owner_type': [owner_type],
        'insurance_status': [insurance_status],
        'seller_type': [seller_type],
        'resale_price': [resale_price],
        'city_tier': [city_tier]
    })
    
    prediction = pipe.predict(test_df)[0]
    return f"Predicted Price: INR {float(prediction):,.2f}"


state_options = df['state'].unique().tolist()
brand_options = df['brand'].unique().tolist()
fuel_type_options = df['fuel_type'].unique().tolist()
owner_type_options = df['owner_type'].unique().tolist()
insurance_status_options = df['insurance_status'].unique().tolist()
seller_type_options = df['seller_type'].unique().tolist()
city_tier_options = df['city_tier'].unique().tolist()

# Define Gradio interface inputs
inputs = [
    gr.Dropdown(state_options, label="State"),
    gr.Dropdown(brand_options, label="Brand"),
    gr.Slider(
        float(df['engine_capacity'].min()), 
        float(df['engine_capacity'].max()), 
        value=float(df['engine_capacity'].mean()), 
        step=1, label="Engine Capacity (cc)"
    ),
    gr.Dropdown(fuel_type_options, label="Fuel Type"),
    gr.Slider(
        float(df['mileage'].min()), 
        float(df['mileage'].max()), 
        value=float(df['mileage'].mean()), 
        step=0.01, label="Mileage (km/l)"
    ),
    gr.Dropdown(owner_type_options, label="Owner Type"),
    gr.Dropdown(insurance_status_options, label="Insurance Status"),
    gr.Dropdown(seller_type_options, label="Seller Type"),
    gr.Slider(
        float(df['resale_price'].min()), 
        float(df['resale_price'].max()), 
        value=float(df['resale_price'].mean()), 
        step=0.01, label="Resale Price (INR)"
    ),
    gr.Dropdown(city_tier_options, label="City Tier")
]

# Create and launch the Gradio interface
iface = gr.Interface(fn=predict_price, inputs=inputs, outputs="text", title="Bike Price Prediction")
iface.launch(debug=True)
