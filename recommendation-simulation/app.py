import streamlit as st


st.set_page_config(
    page_title="RecSys Simulator Pro",
    page_icon="🎛️",
    layout="wide"
)

pg = st.navigation([
    st.Page('recommendation-simulation/home/home.py',title='Home'),
    st.Page("recommendation-simulatio/demographic/main.py", title="Demographic"),
    st.Page("recommendation-simulatio/contentrcs/content.py", title="Content Based"),
    st.Page("recommendation-simulatio/collaborative/simulator.py", title="Collaborative Rec"),
    st.Page('recommendation-simulatio/hybrid/hybrid.py',title='Hybrid Rec')
], position="top")

pg.run()
