import streamlit as st
import pandas as pd
from demographic.movielens.demographic import ui
from demographic.learn.learn import learn

st.set_page_config(
    page_title="Demographic Recommendation Simulator", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        /* Global Background & Text Customization */
        .stApp {
            background-color: #000000;
            color: #E0E0E0;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        
        /* Sidebar Restyling */
        [data-testid="stSidebar"] {
            background-color: #090909;
            border-right: 1px solid #1C1C1C;
        }
        
        /* Typography overrides */
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }
        
        /* Styled Metric Cards */
        div[data-testid="stMetric"] {
            background-color: #111111;
            border: 1px solid #222222;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        div[data-testid="stMetricValue"] {
            color: #E50914 !important;
            font-size: 2rem !important;
            font-weight: 700 !important;
        }
        div[data-testid="stMetricLabel"] {
            color: #AAAAAA !important;
            font-size: 0.9rem !important;
        }
        
        /* Custom Modern Alert Boxes */
        .stAlert {
            background-color: #141414 !important;
            border: 1px solid #262626 !important;
            border-left: 4px solid #E50914 !important;
            color: #FFFFFF !important;
            border-radius: 6px;
        }

        /* Navigation Tabs Header Customization */
        button[data-baseweb="tab"] {
            color: #888888 !important;
            font-size: 1.05rem;
            padding: 12px 24px;
            background-color: transparent !important;
            transition: all 0.3s ease;
        }
        button[data-baseweb="tab"]:hover {
            color: #FFFFFF !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #E50914 !important;
            border-bottom: 3px solid #E50914 !important;
            font-weight: bold;
        }
        
        /* Tab separator line override */
        div[data-testid="stTabBar"] {
            border-bottom: 1px solid #222222;
        }
        
        /* Premium Canvas Card for Executed Code Outputs */
        .execution-container {
            background-color: #0A0A0A;
            padding: 28px;
            border-radius: 12px;
            border: 1px solid #1F1F1F;
            margin-top: 20px;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
        }

        /* Highlight text info badge */
        .info-badge {
            background-color: #141414; 
            padding: 20px; 
            border-radius: 8px; 
            border-left: 4px solid #E50914;
            margin-bottom: 20px;
            border-top: 1px solid #1F1F1F;
            border-right: 1px solid #1F1F1F;
            border-bottom: 1px solid #1F1F1F;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
# 🎬 <span style='color: #E50914;'>Demographic</span> Recommendation Simulator
""", unsafe_allow_html=True)
st.markdown("A multi-tier sandbox environment for exploring Demographic Filtering model architectures.")
st.markdown("---")

# --- Tabs Setup ---
tab_movielens, tab_learn = st.tabs([
    "🍿 MovieLens Production Engine", 
    "📖 Core Concepts"
])

# --- Tab 2: MovieLens Production Engine ---
with tab_movielens:
    st.subheader("🎬 MovieLens Dataset Live Engine")
    st.markdown("Evaluates real consumer streaming telemetry and processes recommendation loops against compiled demographic profiles.")
    
    st.markdown('<div class="execution-container">', unsafe_allow_html=True)
    
    try:
        ui()        
    except FileNotFoundError:
        st.error("❌ Component Missing: MovieLens pipeline definition could not be located.")
        st.info("Please verify the file path remains intact: `demographic/movielens/demographic.py`")    
    st.markdown('</div>', unsafe_allow_html=True)

# --- Tab 3: Learning Module ---
with tab_learn:
    st.subheader("📜 Architectural Blueprint")
    
    col_info, col_spacer = st.columns([2, 1], gap="large")
    
    with col_info:
        st.markdown('''
        Welcome to the conceptual guide. This section breaks down how demographic-driven 
        systems function, highlighting their placement inside commercial streaming pipelines.
        ''')
        
        st.markdown("""
        <div class="info-badge">
            <strong style="color: #FFFFFF; font-size: 1.1rem;">Core Heuristic Matrix:</strong><br>
            <span style="color: #CCCCCC; font-size: 0.95rem; display: inline-block; margin-top: 5px;">
            Demographic filtering correlates a user's inherent attributes (e.g., age bracket, location metadata, occupational clusters) 
            to generate immediate baselines. It operates under the premise that cohorts sharing key socio-demographic features 
            exhibit highly correlated consuming trends.
            </span>
        </div>
        """, unsafe_allow_html=True)
        
        st.caption("💡 Highly effective for mitigating Cold Start issues when fresh users join a platform.")

    st.markdown('<div class="execution-container">', unsafe_allow_html=True)
    
    try:
        learn()
        
    except FileNotFoundError:
        st.error("❌ Component Missing: Interactive conceptual component missing.")
        st.info("Please verify the file path remains intact: `demographic/learn/learn.py`") 
           
    st.markdown('</div>', unsafe_allow_html=True)