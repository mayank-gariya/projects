import streamlit as st


st.set_page_config(
    page_title="RecSys Simulator Pro",
    page_icon="🎛️",
    layout="wide"
)

pg = st.navigation([
    st.Page('recommendation-simulation/home/home.py',title='Home'),
    st.Page("recommendation-simulation/demographic/main.py", title="Demographic"),
    st.Page("recommendation-simulation/contentrcs/content.py", title="Content Based"),
    st.Page("recommendation-simulation/collaborative/simulator.py", title="Collaborative Rec"),
    st.Page('recommendation-simulation/hybrid/hybrid.py',title='Hybrid Rec')
], position="top")

pg.run()
