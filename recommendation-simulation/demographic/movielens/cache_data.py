import streamlit as st
import pandas as pd

@st.cache_data
def load_movies_data():
    """Loads and formats the official MovieLens demographic pipeline."""
    
    users = pd.read_csv(
        "ml-100k/u.user",
        sep="|",
        names=["user_id", "age", "gender", "occupation", "zip_code"],
        encoding="latin-1"
    )
    
    ratings = pd.read_csv(
        'ml-100k/u.data',
        sep='\t',
        names=['user_id','movie_id','rating','timestamp']
    )
    
    movie_cols = [
        "movie_id","title","release_date","video_release_date","IMDb_URL",
        "unknown","Action","Adventure","Animation","Children","Comedy",
        "Crime","Documentary","Drama","Fantasy","Film-Noir","Horror",
        "Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"
    ]
    
    movies = pd.read_csv(
        "ml-100k/u.item",
        sep="|",
        names=movie_cols,
        encoding="latin-1"
    )
    
    return users, ratings, movies