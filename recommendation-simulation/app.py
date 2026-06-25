import streamlit as st


st.set_page_config(
    page_title="RecSys Simulator Pro",
    page_icon="🎛️",
    layout="wide"
)

pg = st.navigation([
    st.Page('home/home.py',title='Home'),
    st.Page("demographic/main.py", title="Demographic"),
    st.Page("contentrcs/content.py", title="Content Based"),
    st.Page("collaborative/simulator.py", title="Collaborative Rec"),
    st.Page('hybrid/hybrid.py',title='Hybrid Rec')
], position="top")

pg.run()
