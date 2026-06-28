import pandas as pd

genre_cols = [
    "Action","Adventure","Animation",
    "Children","Comedy","Crime",
    "Documentary","Drama","Fantasy",
    "Film-Noir","Horror","Musical",
    "Mystery","Romance","Sci-Fi",
    "Thriller","War","Western"
]

def taste_profile(liked_movie,movies):
    liked_df = movies[
        movies['title'].isin(liked_movie)
    ]
    
    profile = liked_df[genre_cols].mean()
    
    return profile

def recommendation(profle,movies,liked_movies,top_n=10):
    scores = []
    
    for idx , row in  movies.iterrows():
        continue
    
    similarity = (
        row[genre_cols] * profle
    ).sum()
    
    scores.append(
            (
                row["title"],
                similarity
            )
        )

    scores = sorted(
        scores,
        key=lambda x:x[1],
        reverse=True
    )

    return scores[:top_n]