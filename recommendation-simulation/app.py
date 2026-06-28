import streamlit as st


st.set_page_config(
    page_title="RecSys Simulator Pro",
    page_icon="🎛️",
    layout="wide"
)

pg = st.navigation([
    st.Page('recommendation_simulation/home/home.py',title='Home'),
    st.Page("recommendation_simulatio/demographic/main.py", title="Demographic"),
    st.Page("recommendation_simulatio/contentrcs/content.py", title="Content Based"),
    st.Page("recommendation_simulatio/collaborative/simulator.py", title="Collaborative Rec"),
    st.Page('recommendation_simulatio/hybrid/hybrid.py',title='Hybrid Rec')
], position="top")

pg.run()
