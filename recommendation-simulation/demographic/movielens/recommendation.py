import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd
from recommendation_simulation.demographic.movielens.cache_data import load_movies_data

users, ratings, movies = load_movies_data()

def age_group(age):
    if age <= 18:
        return "Teen"

    elif age <= 35:
        return "Young Adult"

    elif age <= 50:
        return "Adult"

    else:
        return "Senior"

users["age_group"] = users["age"].apply(age_group)

def demographic_recommendation(user_id,top_n=10):
    target_user = users[users['user_id']==user_id]
    
    if len(target_user) == 0 :
        return pd.DataFrame()
    
    target_age_group = target_user.iloc[0]['age_group']
    target_gender = target_user.iloc[0]['gender']
    target_occupation = target_user.iloc[0]['occupation']
    
    #get the similar users
    similar_user = users[
        (users['age_group']==target_age_group)&
        (users['gender']==target_gender)&
        (users['occupation']==target_occupation)
    ]['user_id']
    
    # get similar ratings
    similar_ratings = ratings[
        ratings['user_id'].isin(similar_user)
    ]
    
    # Movies already watched
    watched_movies = ratings[
        ratings["user_id"] == user_id
    ]["movie_id"]
    
    # average move raitngs
    movie_scores = (
            similar_ratings
            .groupby("movie_id")["rating"]
            .agg(["mean", "count"])
            .reset_index()
        )
    
    movie_scores.columns = [
        "movie_id",
        "avg_rating",
        "rating_count"
    ]
    
    # Minimum popularity filter
    movie_scores = movie_scores[
        movie_scores["rating_count"] >= 5
    ]
    
    # Remove watched movies
    movie_scores = movie_scores[
        ~movie_scores["movie_id"].isin(watched_movies)
    ]
    
    # Score
    movie_scores = movie_scores.sort_values(
        by=["avg_rating", "rating_count"],
        ascending=False
    )

    recommendations = movie_scores.merge(
        movies[["movie_id", "title"]],
        on="movie_id"
    )

    return recommendations.head(top_n)
