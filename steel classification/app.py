import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Steel Defects Detector",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Steel Plates Faults Detection Dashboard")
st.markdown("""
This application utilizes an **Ensemble Stacking Machine Learning model** (Random Forest + XGBoost) to predict manufacturing defects directly from steel plate dimensions.
""")

st.write("---")

# 2. Secure Artifact Loading (Using standard pickle to match your notebook execution)
MODEL_PATH = "models/steel_faults_ensemble.pkl"
SCALER_PATH = "models/scaler.pkl"
ENCODER_PATH = "models/label_encoder.pkl"

@st.cache_resource
def load_pipeline():
    """Loads and caches the model artifacts using standard pickle."""
    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH) and os.path.exists(ENCODER_PATH):
        try:
            with open(MODEL_PATH, "rb") as f:
                model = pkl.load(f)
            with open(SCALER_PATH, "rb") as f:
                scaler = pkl.load(f)
            with open(ENCODER_PATH, "rb") as f:
                label_encoder = pkl.load(f)
            return model, scaler, label_encoder
        except Exception as e:
            st.error(f"Error unpickling model weights: {e}")
            return None, None, None
    else:
        st.error("❌ Pipeline artifacts missing in 'models/' directory. Please ensure files are uploaded to GitHub!")
        return None, None, None

model, scaler, label_encoder = load_pipeline()

# 3. Form Input Grid
col1, col2, col3 = st.columns(3)

with col1:
    st.header("📐 Geometry & Coordinates")
    x_min = st.number_input("X Minimum Coordinate", value=42.0)
    x_max = st.number_input("X Maximum Coordinate", value=134.0)
    y_min = st.number_input("Y Minimum Coordinate", value=872000.0)
    y_max = st.number_input("Y Maximum Coordinate", value=872200.0)
    pixels_area = st.number_input("Pixels Area", value=500.0)
    x_perimeter = st.number_input("X Perimeter", value=35.0)
    y_perimeter = st.number_input("Y Perimeter", value=40.0)
    length_conveyer = st.number_input("Length of Conveyer", value=1350.0)

with col2:
    st.header("💡 Luminosity & Indexing")
    sum_luminosity = st.number_input("Sum of Luminosity", value=55000.0)
    min_luminosity = st.number_input("Minimum Luminosity", value=80.0)
    max_luminosity = st.number_input("Maximum Luminosity", value=145.0)
    steel_thickness = st.number_input("Steel Plate Thickness (mm)", value=40.0)
    edges_index = st.slider("Edges Index", 0.0, 1.0, 0.1)
    empty_index = st.slider("Empty Index", 0.0, 1.0, 0.3)
    square_index = st.slider("Square Index", 0.0, 1.0, 0.5)

with col3:
    st.header("📊 Logistical & Shape Ratios")
    outside_x_index = st.slider("Outside X Index", 0.0, 1.0, 0.02)
    edges_x_index = st.slider("Edges X Index", 0.0, 1.0, 0.6)
    edges_y_index = st.slider("Edges Y Index", 0.0, 1.0, 0.9)
    outside_global_index = st.selectbox("Outside Global Index", [0.0, 0.5, 1.0], index=1)
    log_areas = st.number_input("Log of Areas", value=2.7)
    log_x_index = st.number_input("Log X Index", value=1.3)
    log_y_index = st.number_input("Log Y Index", value=1.4)
    orientation_index = st.slider("Orientation Index", -1.0, 1.0, -0.2)
    luminosity_index = st.slider("Luminosity Index", -1.0, 1.0, -0.1)
    sigmoid_areas = st.slider("Sigmoid of Areas", 0.0, 1.0, 0.5)
    
    st.markdown("**Steel Type Designation:**")
    steel_a300 = st.checkbox("Type A300", value=True)
    steel_a400 = 0 if steel_a300 else 1

st.write("---")

# 4. Trigger Prediction Action
if st.button("🚀 Analyze Steel Plate Defect", use_container_width=True):
    if model is not None:
        with st.spinner("Processing features through Stacking Ensemble..."):
            try:
                # Features mapped explicitly to lowercase to match Colab transformations
                input_data = {
                    "x_minimum": x_min, "x_maximum": x_max, "y_minimum": y_min, "y_maximum": y_max,
                    "pixels_areas": pixels_area, "x_perimeter": x_perimeter, "y_perimeter": y_perimeter,
                    "sum_of_luminosity": sum_luminosity, "minimum_of_luminosity": min_luminosity,
                    "maximum_of_luminosity": max_luminosity, "length_of_conveyer": length_conveyer,
                    "typeofsteel_a300": int(steel_a300), "typeofsteel_a400": int(steel_a400),
                    "steel_plate_thickness": steel_thickness, "edges_index": edges_index, "empty_index": empty_index,
                    "square_index": square_index, "outside_x_index": outside_x_index, "edges_x_index": edges_x_index,
                    "edges_y_index": edges_y_index, "outside_global_index": outside_global_index, "logofareas": log_areas,
                    "log_x_index": log_x_index, "log_y_index": log_y_index, "orientation_index": orientation_index,
                    "luminosity_index": luminosity_index, "sigmoidofareas": sigmoid_areas
                }
                
                input_df = pd.DataFrame([input_data])
                
                # Replicating Colab feature engineering logic precisely
                input_df['fault_width'] = np.abs(input_df['x_maximum'] - input_df['x_minimum'])
                input_df['fault_length'] = np.abs(input_df['y_maximum'] - input_df['y_minimum'])
                input_df['fault_area_estimate'] = input_df['fault_width'] * input_df['fault_length']
                input_df['thickness'] = input_df['steel_plate_thickness'] / (input_df['pixels_areas'] + 1e-5)
                
                # Apply standard scaling transformations
                scaled_features = scaler.transform(input_df)
                
                # Run predictions and extract target mapping
                prediction_encoded = model.predict(scaled_features)
                probabilities = model.predict_proba(scaled_features)[0]
                
                # Revert encoding layer back to defect label
                predicted_class_name = label_encoder.inverse_transform(prediction_encoded)[0]
                prediction_label = predicted_class_name.upper().replace("_", " ")
                confidence = float(np.max(probabilities)) * 100
                
                # Render Results Metrics
                st.success("### Analysis Complete!")
                metric_col1, metric_col2 = st.columns(2)
                metric_col1.metric(label="Predicted Fault Category", value=prediction_label)
                metric_col2.metric(label="Ensemble Model Confidence", value=f"{confidence:.2f}%")
                
                # Conditional Warning flags
                if "SCATCH" in prediction_label or "SCRATCH" in prediction_label:
                    st.warning("⚠️ High structural risk. Inspect machine rollers for mechanical abrasive points.")
                elif "BUMPS" in prediction_label or "PASTRY" in prediction_label:
                    st.info("ℹ️ Surface irregularity detected. Check raw slab cooling rates.")
                    
            except Exception as e:
                st.error(f"Prediction failed inside Streamlit runtime: {str(e)}")
                st.info("💡 Note: If you encounter a shape mismatch error, make sure you retrain your model in Colab without leaving the binary fault leakage columns in your X features matrix.")
    else:
        st.error("Model engine failed to initialize. Check log alerts above.")