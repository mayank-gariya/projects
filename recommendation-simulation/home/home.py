import streamlit as st


st.markdown("""
    <style>
        /* Base Dark Canvas Layout */
        .stApp {
            background-color: #000000;
            color: #E0E0E0;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        
        /* Typography overrides */
        h1, h2, h3, h4 {
            color: #FFFFFF !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }
        
        /* Modernized Metric Display Canvas */
        div[data-testid="stMetric"] {
            background-color: #0A0A0A;
            border: 1px solid #1F1F1F;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }
        div[data-testid="stMetricValue"] {
            color: #E50914 !important;
            font-size: 2.2rem !important;
        }
        
        /* Callout Information Cards */
        .manifesto-card {
            background-color: #080808;
            border: 1px solid #1A1A1A;
            border-left: 4px solid #E50914;
            padding: 22px;
            border-radius: 8px;
            margin-bottom: 25px;
        }
        
        /* Sub-feature highlight badges */
        .feature-badge {
            color: #E50914;
            font-weight: bold;
            font-family: monospace;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER TITLE SECTION ---
st.markdown("""
# 🎬 RecSys: <span style='color: #E50914;'>Recommendation Engine</span> Simulator
""", unsafe_allow_html=True)
st.caption("Project Master Guide • System Architecture Overview • Version 1.0")
st.markdown("---")

# --- OVERVIEW METRICS ---
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="Algorithmic Pillars Evaluated", value="5 Frameworks")
with col_m2:
    st.metric(label="Primary Dataset Engine", value="MovieLens 100K")
with col_m3:
    st.metric(label="Simulation Interface Mode", value="Split Laboratory")

st.markdown("<br>", unsafe_allow_html=True)

# --- PROJECT MANIFESTO ---
st.markdown("""
<div class="manifesto-card">
    <h3>📖 Project Manifesto: What This System Does</h3>
    <p>
        This platform is an interactive testing suit built to demonstrate exactly how modern production digital platforms 
        (like Netflix, YouTube, or Amazon) analyze user traits and interaction history to predict what content they will watch next.
    </p>
    <p>
        To make this clear and easy to navigate, every algorithm tab in this project splits your workspace down the middle:
    </p>
    <ul>
        <li><strong>The Theoretical Laboratory (Left View):</strong> Breaks down real-world engineering failures (such as data sparsity, filter bubbles, and cold-starts) through clear concept lessons.</li>
        <li><strong>The Production Data Engine (Right View):</strong> Runs filtering pipelines against real user rating tables from the <strong>MovieLens 100K Dataset</strong> using live parameter controls.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- 5 ENGINE ARCHITECTURE OUTLINES ---
st.markdown("## 🗺️ The Five Algorithmic Pillars")
st.markdown("This project systematically builds up from basic metadata tracking to multi-dimensional recommendation networks:")

# Pillar 1
col1_left, col1_right = st.columns([1, 2])
with col1_left:
    st.markdown("<span class=\"feature-badge\">01 // Demographic</span>", unsafe_allow_html=True)
with col1_right:
    st.markdown("#### Demographic Filtering Engine")
    st.markdown("Groups users by traits like age or job to find shared tastes. This instantly solves the **User Cold-Start Problem** by generating baseline recommendations the moment a new user creates an account.")

st.markdown("---")

# Pillar 2
col2_left, col2_right = st.columns([1, 2])
with col2_left:
    st.markdown("<span class=\"feature-badge\">02 // Content-Based</span>", unsafe_allow_html=True)
with col2_right:
    st.markdown("#### Content-Based Filtering Engine")
    st.markdown("Builds profile vectors by tracking specific movie tags and genres a user has liked in the past. It explains the **Filter Bubble Dilemma**, showing how users can get trapped seeing only the same genres.")

st.markdown("---")

# Pillar 3
col3_left, col3_right = st.columns([1, 2])
with col3_left:
    st.markdown("<span class=\"feature-badge\">03 // Collaborative</span>", unsafe_allow_html=True)
with col3_right:
    st.markdown("#### Collaborative Filtering Hub")
    st.markdown("Ignores descriptive tags entirely, instead mapping overlapping customer habits to find hidden community patterns. It handles **Matrix Sparsity** challenges when dealing with millions of unfilled rating slots.")

st.markdown("---")

# Pillar 4
col4_left, col4_right = st.columns([1, 2])
with col4_left:
    st.markdown("<span class=\"feature-badge\">04 // Context-Aware</span>", unsafe_allow_html=True)
with col4_right:
    st.markdown("#### Context-Aware Streaming System")
    st.markdown("Expands standard user histories by adding real-time situational tracking, automatically adjusting recommendations based on **Time of Day, Active Device Type, or Current Location**.")

st.markdown("---")

# Pillar 5
col5_left, col5_right = st.columns([1, 2])
with col5_left:
    st.markdown("<span class=\"feature-badge\">05 // Hybrid Ensemble</span>", unsafe_allow_html=True)
with col5_right:
    st.markdown("#### Hybrid Ensemble Pipeline")
    st.markdown("Combines multiple separate recommendation models into a single pipeline. It uses dynamic weight controls to blend the quick initialization of demographic filters with the deep accuracy of collaborative systems.")
