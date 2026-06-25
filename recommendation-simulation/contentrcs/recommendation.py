import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from demographic.movielens.cache_data import load_movies_data

# get the data 
genre_cols = [
    "Action","Adventure","Animation",
    "Children","Comedy","Crime",
    "Documentary","Drama","Fantasy",
    "Film-Noir","Horror","Musical",
    "Mystery","Romance","Sci-Fi",
    "Thriller","War","Western"
]

users, ratings, movies = load_movies_data()

#get the movies features 

moveies_feature = movies[genre_cols]

# calculate the similarity
similarity_matrix = cosine_similarity(
    moveies_feature
)

# calculate the recommendation 

def get_recommendation(movie_title):
    
    idx = movies[
        movies['title'] == movie_title
    ].index[0]
    
    sim_scores = sorted(
        list(enumerate(similarity_matrix[idx])),
        key=lambda x: x[1],
        reverse=True
    )
    
    top_movies = sim_scores[1:11]
    
    top_movie_indices = [i[0] for i in top_movies]
    scores = [round(i[1],3) for i in top_movies]

    recommendations = movies.iloc[top_movie_indices][[
        "movie_id",
        "title",
        "release_date"
    ]].copy()

    recommendations["similarity_score"] = scores

    return recommendations