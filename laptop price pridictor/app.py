import gradio as gr
import pickle
import numpy as np
import os

# --- 1. System Setup: Load model and reference data ---
# We use try/except blocks to ensure the app doesn't crash if files are missing.
try:
    with open('pipe.pkl', 'rb') as f:
        pipe = pickle.load(f)
    with open('df.pkl', 'rb') as f:
        df = pickle.load(f)
except FileNotFoundError as e:
    print(f"Error: Required file not found. {e}")
    print("Ensure 'pipe.pkl' and 'df.pkl' are in the correct directory.")
    pipe = None
    df = None 

# Check for the specified laptop image
laptop_image_path = "image.png"
if not os.path.exists(laptop_image_path):
    print(f"Error: Required file '{laptop_image_path}' not found.")
    # Fallback to none, but in image, I must assume it exists as requested.
    laptop_image_path = None


# --- 2. Definition of UI Input Options ---
# These must match the data format the model was trained on.
if df is not None:
    BRAND_OPTIONS = list(df['Company'].unique())
    TYPE_OPTIONS = list(df['TypeName'].unique())
    CPU_OPTIONS = list(df['Cpu brand'].unique())
    GPU_OPTIONS = list(df['Gpu brand'].unique())
    OS_OPTIONS = list(df['os'].unique())
else:
    BRAND_OPTIONS = ["Model Not Loaded"]
    TYPE_OPTIONS = []
    CPU_OPTIONS = []
    GPU_OPTIONS = []
    OS_OPTIONS = []

# Fixed numerical/categorical options
RAM_OPTIONS = [2, 4, 6, 8, 12, 16, 24, 32, 64]
RESOLUTION_OPTIONS = [
    '1920x1080', '1366x768', '1600x900', '3840x2160',
    '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
]
HDD_OPTIONS = [0, 128, 256, 512, 1024, 2048]
SSD_OPTIONS = [0, 8, 128, 256, 512, 1024]
YES_NO_OPTIONS = ['Yes', 'No']


# --- 3. Core Prediction Logic ---
# This is a port of your Streamlit preprocessing logic.

def get_prediction(company, lap_type, ram, weight, touchscreen, ips, screen_size, resolution, cpu, hdd, ssd, gpu, os):
    if pipe is None:
        return "ERROR: The prediction model failed to load."

    try:
        # Preprocessing: Convert Yes/No strings to 1/0
        touchscreen_val = 1 if touchscreen == 'Yes' else 0
        ips_val = 1 if ips == 'Yes' else 0
        
        # Calculate PPI (Pixels Per Inch)
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        
        # Create input feature vector, ensuring 'object' dtype
        query = np.array([company, lap_type, ram, weight, touchscreen_val, ips_val, ppi, cpu, hdd, ssd, gpu, os], dtype=object)
        query = query.reshape(1, 12)
        
        # Execute prediction and format output (assume INR)
        prediction = pipe.predict(query)
        final_price = int(np.exp(prediction[0]))
        
        # Return the final stylized HTML output as a string.
        # This will be rendered inside the gr.HTML component.
        return f"""
        <div style="text-align: center; color: #121212;">
            <p style="font-size: 1.2rem; font-weight: 600; margin-bottom: 5px;">The Predicted Price of this configuration is</p>
            <p style="font-size: 3rem; font-weight: 800; color: #235B63; margin-top: 15px !important; margin-bottom: 5px !important;">₹ {final_price:,}</p>
            <p style="font-size: 0.9rem; color: #707070;">Estimated Market Value</p>
        </div>
        """
        
    except ValueError as e:
        print(f"Prediction Error (ValueError): {e}")
        return "<div style='color: red; text-align: center;'>ERROR: Model formatting issue. Check console.</div>"
    except Exception as e:
        print(f"Critical Runtime Error: {e}")
        return "<div style='color: red; text-align: center;'>CRITICAL ERROR. Check console.</div>"

# --- 4. Define Custom CSS for visual layout ---
# This applies the dark teal/charcoal styling and arranges inputs.
# Note: Since Gradio changes, custom classes may need adjustment.
theme_css = """
body, gr-app, gr-root {
    background-color: #FDFDFD !important; /* Off-white background */
}

/* General Layout spacing */
.gradio-container {
    max-width: 1300px !important;
}

/* Page Title Style */
.main_title h1 {
    font-weight: 700 !important;
    text-align: center;
    color: #121212;
    margin-bottom: 5px !important;
}
.main_subtitle p {
    text-align: center;
    color: #404040;
    margin-bottom: 30px !important;
    font-size: 1.1rem;
}

/* Header Text for Input Features */
.input_header h2 {
    font-size: 1.5rem !important;
    font-weight: 600 !important;
    color: #121212;
    margin-bottom: 10px !important;
}

/* Standard Widget Label Style */
.gr-form label {
    font-size: 1.0rem !important;
    font-weight: 500 !important;
    color: #121212 !important;
}

/* Dark Teal Styling for Action Buttons (Predict Button) */
.gr-button-primary {
    background: #235B63 !important; /* Main Dark Teal */
    border-color: #235B63 !important;
    color: white !important;
    border-radius: 20px !important; /* Rounded style */
    padding: 10px 25px !important;
    font-weight: 600 !important;
}
.gr-button-primary:hover {
    background: #184147 !important; /* Darker hover */
}

/* Styling for Yes/No Radio Buttons like Segmented Controls */
/* These often require more specific targets in newer Gradio */
.gr-radio-group {
    border-radius: 8px !important;
    overflow: hidden !important;
    border: 1px solid #D9D9D9 !important;
}
.gr-radio-group .gr-radio {
    border-radius: 0px !important;
    border: none !important;
}
/* Selected state */
.gr-radio-group .gr-radio[aria-checked="true"] {
    background-color: #235B63 !important; 
    color: white !important;
    border-radius: 0px !important;
}
.gr-radio-group .gr-radio[aria-checked="false"]:hover {
    background-color: #F0F0F0 !important;
}


/* Prediction Result Card Styling */
.result_card {
    background-color: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08); /* Soft shadow */
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
"""

# --- 5. Build the UI using Blocks ---
# This arranges components into the 3-column (Inputs/Inputs/Results) layout.

with gr.Blocks(theme=gr.themes.Default(primary_hue="teal"), css=theme_css) as demo:
    
    # 5a. Page Title Section
    gr.Markdown("# Laptop Price Predictor", elem_classes=["main_title"])
    gr.Markdown("Enter laptop specifications to get an instant estimate.", elem_classes=["main_subtitle"])
    
    # 5b. Define the main content container: Left Inputs, Right Result
    with gr.Row(equal_height=True):
        
        # --- LEFT: Input Features Container (Two columns) ---
        with gr.Column(scale=2):
            gr.Markdown("## Input Features", elem_classes=["input_header"])
            
            with gr.Row():
                # --- INPUT COLUMN 1 ---
                with gr.Column():
                    in_brand = gr.Dropdown(choices=BRAND_OPTIONS, label="Brand", value=BRAND_OPTIONS[0] if BRAND_OPTIONS else None)
                    in_type = gr.Dropdown(choices=TYPE_OPTIONS, label="Type")
                    in_ram = gr.Dropdown(choices=RAM_OPTIONS, label="RAM (in GB)")
                    in_weight = gr.Number(label="Weight of the Laptop (in kg)", value=1.5, precision=2)
                    in_touch = gr.Radio(choices=YES_NO_OPTIONS, label="Touchscreen", value='No')
                    in_ips = gr.Radio(choices=YES_NO_OPTIONS, label="IPS Panel", value='No')

                # --- INPUT COLUMN 2 ---
                with gr.Column():
                    in_screen_size = gr.Slider(minimum=10.0, maximum=18.0, step=0.1, value=13.3, label="Screen size in inches")
                    in_res = gr.Dropdown(choices=RESOLUTION_OPTIONS, label="Screen Resolution")
                    in_cpu = gr.Dropdown(choices=CPU_OPTIONS, label="CPU Brand")
                    in_hdd = gr.Dropdown(choices=HDD_OPTIONS, label="HDD (GB)")
                    in_ssd = gr.Dropdown(choices=SSD_OPTIONS, label="SSD (GB)")
                    in_gpu = gr.Dropdown(choices=GPU_OPTIONS, label="GPU Brand")
                    in_os = gr.Dropdown(choices=OS_OPTIONS, label="OS")
            
            # Action Button (Primary Teal), centered under inputs
            with gr.Row():
                with gr.Column(scale=1): gr.Markdown("") # Spacers for centering
                predict_btn = gr.Button("Predict Laptop Price", variant="primary", elem_id="predict_btn", scale=2)
                with gr.Column(scale=1): gr.Markdown("")

        # --- RIGHT: Prediction Results Container (Single Column Card) ---
        with gr.Column(scale=1):
            
            # The visually stylized output card
            with gr.Column(elem_classes=["result_card"]):
                if laptop_image_path:
                    # Using the specified laptop image 'image.png'
                    gr.Image(laptop_image_path, interactive=False, show_label=False, height=150)
                else:
                    # Optional: Fallback text if image missing (remove for clean look)
                    gr.Markdown("*(Laptop Image Not Found)*", elem_classes=["text-center"])
                
                # HTML output for complex text styling that Label cannot handle
                # Initialize with placeholder text that has proper card styling.
                out_html = gr.HTML(
                    value="""
                    <div style="text-align: center; color: #707070;">
                        <p style="font-size: 1.2rem; font-weight: 600; margin-bottom: 5px; color: #121212;">Predicted Price</p>
                        <p style="font-size: 3rem; font-weight: 800; color: #C0C0C0;">₹ --</p>
                        <p style="font-size: 0.9rem;">Configure options and click predict</p>
                    </div>
                    """
                )
    
    # 6. Event Handling: Wire the button to the prediction function
    # The 'inputs' order here MUST match the function definition at step 3.
    input_list = [
        in_brand, in_type, in_ram, in_weight, in_touch, 
        in_ips, in_screen_size, in_res, in_cpu, in_hdd, 
        in_ssd, in_gpu, in_os
    ]
    
    # The click event updates the 'value' of the HTML component.
    predict_btn.click(fn=get_prediction, inputs=input_list, outputs=out_html)

# 7. Launch the app
if __name__ == "__main__":
    demo.launch(share=True)