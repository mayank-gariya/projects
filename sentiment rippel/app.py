import gradio as gr
import joblib
import random
import time
import matplotlib.pyplot as plt
import io
from PIL import Image

# 1. Load your pre-trained pipeline
pipeline = joblib.load('logistic_regression_pipeline.pkl')

def create_minimal_viz(votes_a, votes_b):
    """Generates a clean, modern summary chart."""
    plt.figure(figsize=(5, 1.8), facecolor='white')
    categories = ['Agree', 'Reject']
    counts = [votes_a, votes_b]
    colors = ["#10c689", '#ef4444'] # Modern Green and Red
    
    plt.barh(categories, counts, color=colors, height=0.5)
    plt.title('Collective Decision Summary', fontsize=10, loc='left', color="#106CFF", pad=10)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().xaxis.set_visible(False)
    plt.tick_params(axis='y', which='both', length=0, labelsize=9)
    
    for i, v in enumerate(counts):
        plt.text(v + 0.1, i, str(v), color='#111827', va='center', fontweight='bold', fontsize=9)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return Image.open(buf)

def simulate_ripple(tweet, num_users, bias_strength, use_bias):
    if not tweet.strip():
        yield None, "<div style='text-align:center; color:#111827;'>Please enter a broadcast message.</div>"
        return

    # ML Sentiment Analysis
    probs = pipeline.predict_proba([tweet])[0]
    prob_pos = probs[1]
    
    active_global_bias = bias_strength if use_bias else 0
    user_data = []
    
    # Pre-calculate individual baselines and final outcomes to preserve structural integrity during the ripple
    for i in range(int(num_users)):
        # Generate a unique starting bias for each individual user (-0.2 to +0.2)
        individual_bias = random.uniform(-0.2, 0.2)
        total_bias_offset = active_global_bias + individual_bias
        
        # The final decision score combining message weight and unique background biases
        final_score = prob_pos + total_bias_offset
        is_agree = final_score > 0.5
        
        user_data.append({
            "ind_bias": individual_bias,
            "total_bias": total_bias_offset,
            "is_agree": is_agree
        })

    # ANIMATION LOOP: The Sequential Ripple Wave
    for wave in range(int(num_users) + 1):
        grid_html = "<div style='display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px;'>"
        
        current_a = 0
        current_b = 0

        for i in range(int(num_users)):
            data = user_data[i]
            
            if i < wave: # The ripple wave has reached this user node
                if data["is_agree"]:
                    bg, label = "#168ecf", "PATH: AGREE"
                    current_a += 1
                else:
                    bg, label = "#c83019", "PATH: REJECT"
                    current_b += 1
                
                # Render comprehensive bias metrics in solid black text
                bias_details = f"""
                <div style='color: #111827; font-size: 0.75em; text-align: left; margin-top: 6px; line-height: 1.3;'>
                    • Base Bias: {data["ind_bias"]:+.2f}<br>
                    • Net Bias: {data["total_bias"]:+.2f}<br>
                    • Impact Score: {prob_pos + data["total_bias"]:.2f}
                </div>
                <div style='color: #111827; font-size: 0.8em; font-weight: 900; margin-top: 6px;'>{label}</div>
                """
            else: # Node is still sleeping, waiting for the wave impact
                bg = "#bddeff"
                bias_details = """
                <div style='color: #9ca3af; font-size: 0.75em; text-align: left; margin-top: 6px; line-height: 1.3;'>
                    • Base Bias: Locked<br>
                    • Net Bias: Locked<br>
                    • Impact Score: Pending
                </div>
                <div style='color: #9ca3af; font-size: 0.8em; font-weight: bold; margin-top: 6px;'>WAITING...</div>
                """

            grid_html += f"""
            <div style='background-color: {bg}; padding: 12px; border-radius: 6px; 
                        border: 1px solid #e5e7eb; font-family: sans-serif; min-height: 100px;
                        display: flex; flex-direction: column; justify-content: space-between;'>
                <b style='font-size: 0.75em; color: #4b5563; opacity: 0.8;'>USER {i+1}</b>
                {bias_details}
            </div>"""
        
        grid_html += "</div>"
        
        # UI Top Header Progress
        header = f"""
        <div style='margin-bottom: 20px; font-family: sans-serif;'>
            <h2 style='margin:0; color:#ffffff; font-size: 1.1em;'>Wave Propagation: {int((wave/num_users)*100)}%</h2>
            <p style='margin:2px 0; color:#4b5563; font-size: 0.85em;'>Signal Intensity: {prob_pos:.2f} | Env Bias Layer: {active_global_bias:+.2f}</p>
        </div>"""

        # Generate and inject analytics visualization only at completion of full ripple sequence
        chart = create_minimal_viz(current_a, current_b) if wave == int(num_users) else None
        
        yield chart, header + grid_html
        time.sleep(0.12) # Velocity control for the physical ripple wave effect

# ==========================================
# UI CODE STRUCTURE (Preserved Exact Form Layout)
# ==========================================
with gr.Blocks(theme=gr.themes.Default(spacing_size="md", radius_size="lg")) as demo:
    gr.Markdown("## 🌊 Ripple & Visual Analytics")
    
    with gr.Row():
        # LEFT: CONTROLS
        with gr.Column(scale=1):
            with gr.Group():
                gr.Markdown("### ⚙️ Simulation Settings")
                msg = gr.Textbox(label="Message Content", placeholder="Enter text for the community...", lines=4)
                count = gr.Slider(1, 21, 11, step=2, label="Population Size")
                bias_on = gr.Checkbox(label="Enable Environmental Bias", value=True)
                bias_lvl = gr.Slider(-0.5, 0.5, -0.1, step=0.05, label="Bias Offset")
            
            btn = gr.Button("🚀 Start Broadcast", variant="primary")
            
        # RIGHT: ANALYTICS & GRID
        with gr.Column(scale=2):
            gr.Markdown("### 📈 Live Influence Tracking")
            viz_box = gr.Image(label="Voter Distribution", interactive=False)
            html_box = gr.HTML()

    btn.click(simulate_ripple, [msg, count, bias_lvl, bias_on], [viz_box, html_box])

if __name__ == "__main__":
    demo.launch()
