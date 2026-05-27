import gradio as gr
import pandas as pd
import joblib
import time
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

ps = PorterStemmer()

resources = ['punkt', 'punkt_tab', 'stopwords']
for res in resources:
    try:
        nltk.download(res, quiet=True)
    except Exception as e:
        print(f"Error downloading {res}: {e}")
        

def transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [ps.stem(i) for i in text if i.isalnum() and i not in stopwords.words('english')]
    return " ".join(y)

try:
    loaded_pipe = joblib.load('multinomial_nb_model.pkl')
    loaded_le = joblib.load('label_encoder.pkl')

except:
    loaded_pipe = None

def next_step():
    return gr.update(visible=False), gr.update(visible=True)

def final_predict(p, g, d, e, m, s, i, a):
    time.sleep(2.0)  # Simulated thinking time for suspense
    if loaded_pipe:
        sample_data = pd.DataFrame([{
            'power': transform(p), 'gender': g, 'description': transform(d),
            'in_endgame': e, 'movies_in': m, 'strength': s, 
            'intelligence': i, 'agility': a
        }])
        pred = loaded_pipe.predict(sample_data)
        res = loaded_le.inverse_transform(pred)[0]
        return f"## 🎯 Result: {res.upper()}"
    return "## 🎯 Result: Iron Man (Demo Mode)"

# --- UI Layout ---
with gr.Blocks() as demo:
    gr.Markdown("# 🦸‍♂️ Avenger Identity Quest")
    
    with gr.Row():
        # ================= LEFT COLUMN =================
        with gr.Column(scale=1):
            # Banner/Intro Image Placeholder
            gr.Image(value="src/avengers.png",height=200) 
            
            # Rules of the Game
            with gr.Group():
                gr.Markdown("### 📜 Game Rules")
                gr.Markdown("""
                1. Think of one of the 5 core Avengers listed on the right panel.
                2. Answer each character question honestly, one step at a time.
                3. Use the **Hero Stat Cards** on the right to calibrate your sliders.
                4. Press 'Reveal' at the end and see if the AI can read your mind!
                """)
            
            gr.Markdown("---")
            gr.Markdown("### 📝 AVengers Quiz")
            
            # Interactive Quiz Steps
            with gr.Column(visible=True) as step1:
                p_in = gr.Textbox(label="Describe their unique power:")
                btn1 = gr.Button("Next ➔")

            with gr.Column(visible=False) as step2:
                g_in = gr.Radio(["Male", "Female"], label="Gender")
                btn2 = gr.Button("Next ➔")

            with gr.Column(visible=False) as step3:
                d_in = gr.Textbox(label="General Description (Personality/Looks)")
                btn3 = gr.Button("Next ➔")

            with gr.Column(visible=False) as step4:
                e_in = gr.Checkbox(label="Was in Endgame?")
                btn4 = gr.Button("Next ➔")

            with gr.Column(visible=False) as step5:
                m_in = gr.Slider(1, 10, step=1, label="Movies Count",value=5)
                s_in = gr.Slider(0, 100, label="Strength")
                i_in = gr.Slider(0, 100, label="Intelligence")
                a_in = gr.Slider(0, 100, label="Agility" ,value=70)
                btn_final = gr.Button("REVEAL MY AVENGER", variant="primary")

            result_out = gr.Markdown("")

        # ================= RIGHT COLUMN =================
        with gr.Column(scale=1):
            gr.Markdown("### 📊 Hero Stat Cards (Side-by-Side Reference)")
        
            avengers_list = ["hulk", "iron", "spider", "widow", "captain"]
            
            for avenger in avengers_list:
                with gr.Accordion(f"Hero Reference: {avenger.upper()}", open=True):
                    with gr.Row():
                        # Left side: Strength Image
                        gr.Image(
                            value=f"src/{avenger}strength.png", 
                            label="Strength Matrix", 
                            show_label=True, 
                            height=150
                        )
                        # Right side: Intelligence Image
                        gr.Image(
                            value=f"src/{avenger}inteli.png", 
                            label="Intelligence Matrix", 
                            show_label=True, 
                            height=150
                        )

    # --- Quiz Navigation Logic ---
    btn1.click(next_step, None, [step1, step2])
    btn2.click(next_step, None, [step2, step3])
    btn3.click(next_step, None, [step3, step4])
    btn4.click(next_step, None, [step4, step5])
    
    btn_final.click(
        final_predict, 
        inputs=[p_in, g_in, d_in, e_in, m_in, s_in, i_in, a_in], 
        outputs=result_out
    )

demo.launch(debug=True ,theme=gr.themes.Soft())
