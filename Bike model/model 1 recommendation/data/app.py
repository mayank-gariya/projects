import gradio as gr
import pickle
import pandas as pd

# Load data
df = pickle.load(open('df.pkl', 'rb'))
simailarity = pickle.load(open('simailarity.pkl', 'rb'))

# Recommendation Function
def get_recomendations(bike_model):
    if bike_model not in df['model'].values:
        return "❌ Bike not found"

    bike_index = df[df['model'] == bike_model].index[0]

    distances = simailarity[bike_index]

    bike_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    markdown_output = "# 🚀 Recommended Bikes For You\n\n"

    for i in bike_list:
        model_name = df.iloc[i[0]].model
        price = df.iloc[i[0]].price
        year = df.iloc[i[0]].year

        markdown_output += f"""
### 🏍️ {model_name}

💰 **Price:** ₹{price:,.0f}

📅 **Year:** {year}

---
"""

    return markdown_output


bike_name = sorted(df['model'].unique().tolist())

# Custom CSS
custom_css = """
.gradio-container {
    max-width: 1100px !important;
    margin: auto;
}

#title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 10px;
}

#subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 25px;
}

footer {
    visibility: hidden;
}
"""

# Modern Theme
theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
)

with gr.Blocks(theme=theme, css=custom_css) as iface:

    gr.HTML("""
        <div id='title'>
            🏍️ Bike Recommendation System
        </div>

        <div id='subtitle'>
            Find similar bikes based on your selected model
        </div>
    """)

    with gr.Row():
        bike_dropdown = gr.Dropdown(
            choices=bike_name,
            label="Select Bike Model",
            info="Choose a bike to get recommendations",
            scale=3
        )

    recommend_btn = gr.Button(
        "🔍 Get Recommendations",
        variant="primary",
        size="lg"
    )

    output = gr.Markdown()

    recommend_btn.click(
        fn=get_recomendations,
        inputs=bike_dropdown,
        outputs=output
    )

iface.launch(debug=True)