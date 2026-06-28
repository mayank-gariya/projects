import streamlit as st
import pandas as pd
from demographic.movielens.cache_data import load_movies_data
from demographic.movielens.recommendation import demographic_recommendation
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "ml-100k"

st.set_page_config(layout='wide')

# getting data
users, ratings, movies = load_movies_data()

# ui
def ui():
    st.write(
        "MovieLens 100K Dataset Demo"
    )

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.metric("Users", len(users))

    with col2:
        st.metric("Movies", len(movies))

    with col3:
        st.metric("Ratings", len(ratings))

    with col4:    
        st.metric("Occupations", users["occupation"].nunique())

    with col5:
        df = pd.read_csv(
            DATA_DIR / "u.genre",
            sep="|",
            names=["Genre", "counts"]
        )
        st.metric(label="Total Genres", value=len(df))

    col1 , col2 ,col3 , col4= st.columns(4)

    with col1:
        st.subheader("Genres List")
        st.dataframe(df)

    with col2:
        occ_df = pd.read_csv(
            DATA_DIR / "u.occupation",
            names=["occupations"]
        )
        st.subheader('Occupations')
        st.dataframe(occ_df)

    with col3:
        st.subheader('Movies data')
        st.dataframe(movies,width="stretch")

    with col4:
        st.subheader('Users data')
        st.dataframe(users ,width="stretch")
        
    selected_user = st.selectbox(
        "Select User",
        users["user_id"].tolist()
    )

    user_info = users[
        users["user_id"] == selected_user
    ].iloc[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Age", user_info["age"])

    with col2:
        st.metric("Gender", user_info["gender"])

    with col3:
        st.metric("Occupation", user_info["occupation"])

    st.divider()

    if st.button("Generate Recommendations"):

        recs = demographic_recommendation(selected_user)

        if len(recs) == 0:
            st.warning("No recommendations found")

        else:
            st.subheader("Recommended Movies")

            st.dataframe(
                recs[
                    ["title", "avg_rating", "rating_count"]
                ],
                width="stretch"
            )
