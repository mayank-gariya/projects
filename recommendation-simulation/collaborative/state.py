import streamlit as st

def initialize_state():

    if "liked_movies" not in st.session_state:
        st.session_state.liked_movies = []

    if "skipped_movies" not in st.session_state:
        st.session_state.skipped_movies = []

    if "movie_index" not in st.session_state:
        st.session_state.movie_index = 0