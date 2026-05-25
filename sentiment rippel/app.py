import gradio as gr
import joblib
import random

# 1. Load your pre-trained pipeline
pipeline = joblib.load('logistic_regression_pipeline.pkl')

def simulate_ripple(tweet, num_users, bias_strength, use_bias):
    if not tweet.strip():
        return "<div style='text-align:center; padding:20px;'>Please enter a message to begin the simulation.</div>"
    
    # Analyze Sentiment
    probs = pipeline.predict_proba([tweet])[0]
    prob_pos = probs[1]
    
    votes_for_a = 0
    votes_for_b = 0
    user_grid_html = "<div style='display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; margin-top: 20px;'>"
    
    for i in range(1, int(num_users) + 1):
        # Base random noise for individuality
        individual_noise = random.uniform(-0.1, 0.1)
        
        # Apply Global Bias if checkbox is checked
        # bias_strength is mapped from -1 to 1
        active_bias = bias_strength if use_bias else 0
        
        # Final Decision Score Calculation
        decision_score = prob_pos + individual_noise + active_bias
        
        if decision_score > 0.5:
            path_text = "PATH: AGREE"
            bg_color = "#1fbe59" # Green
            text_color = "#000000"
            votes_for_a += 1
        else:
            path_text = "PATH: REJECT"
            bg_color = "#f64a4a" # Red
            text_color = "#000000" # Dark Red Text
            votes_for_b += 1

        user_grid_html += f"""
        <div style='background-color: {bg_color}; color: {text_color}; padding: 12px; border-radius: 8px; text-align: center; border: 2px solid rgba(0,0,0,0.1);'>
            <span style='font-size: 0.8em; font-weight: bold;'>USER {i}</span><br>
            <b style='font-size: 1em;'>{path_text}</b>
        </div>
        """
    
    user_grid_html += "</div>"
    
    # 2. Collective Decision Logic
    winner = "COMMUNITY AGREES" if votes_for_a > votes_for_b else "COMMUNITY REJECTS"
    consensus_color = "#22c55e" if winner == "COMMUNITY AGREES" else "#ef4444"
    
    summary_html = f"""
    <div style='background-color: #1e293b; color: white; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 20px;'>
        <h2 style='margin: 0; color: {consensus_color};'>{winner}</h2>
        <div style='display: flex; justify-content: space-around; margin-top: 15px;'>
            <div><b style='font-size: 1.5em;'>{votes_for_a}</b><br><small>AGREE VOTES</small></div>
            <div><b style='font-size: 1.5em;'>{votes_for_b}</b><br><small>REJECT VOTES</small></div>
        </div>
    </div>
    """
    
    return summary_html + user_grid_html

# ==========================================
# 3. INTERFACE DESIGN (Preserving Last Version UI)
# ==========================================
with gr.Blocks(theme=gr.themes.Default(primary_hue="blue")) as demo:
    gr.Markdown("# 🎇📊 Community Ripple & Voting Simulator")
    
    with gr.Row():
        # LEFT: CONTROLS
        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ Simulation Controls")
            user_slider = gr.Slider(minimum=1, maximum=21, step=2, value=7, label="Community Size")
            
            with gr.Group():
                gr.Markdown("**Community Bias Settings**")
                use_bias_checkbox = gr.Checkbox(label="Enable Global Bias", value=False)
                bias_slider = gr.Slider(
                    minimum=-0.5, 
                    maximum=0.5, 
                    step=0.05, 
                    value=0, 
                    label="Bias Level (Left=Negative, Right=Positive)"
                )
            
            input_text = gr.Textbox(label="Your Message ( The ripple )", placeholder="e.g. I found this university so bad , i just hate it ", lines=4)
            send_btn = gr.Button("🚀 Broadcast & Vote", variant="primary")
            
        # RIGHT: OUTCOMES
        with gr.Column(scale=2):
            gr.Markdown("### 📊 Live Voting & Individual Pathways")
            output_area = gr.HTML()

    # Event Listener
    send_btn.click(
        fn=simulate_ripple,
        inputs=[input_text, user_slider, bias_slider, use_bias_checkbox],
        outputs=output_area
    )

if __name__ == "__main__":
    demo.launch()