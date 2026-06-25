import streamlit as st
import pandas as pd

@st.cache_data
def get_data():
    
    occupation_preferences = {
        "Student": {
            "Action": 0.4,
            "Comedy": 0.3,
            "Sci-Fi": 0.3
        },

        "Engineer": {
            "Sci-Fi": 0.5,
            "Documentary": 0.2,
            "Action": 0.3
        },

        "Teacher": {
            "Drama": 0.4,
            "Biography": 0.3,
            "Comedy": 0.3
        },

        "Doctor": {
            "Biography": 0.4,
            "Drama": 0.3,
            "Documentary": 0.3
        }
    }
    
    movies_by_genre = {
        "Action": [
            "Avengers",
            "John Wick",
            "Mad Max"
        ],

        "Sci-Fi": [
            "Interstellar",
            "The Matrix",
            "Inception"
        ],

        "Drama": [
            "The Shawshank Redemption",
            "Forrest Gump",
            "The Green Mile"
        ],

        "Comedy": [
            "The Hangover",
            "Superbad",
            "Free Guy"
        ],

        "Documentary": [
            "Inside Bill's Brain",
            "Planet Earth",
            "The Social Dilemma"
        ],

        "Biography": [
            "A Beautiful Mind",
            "Steve Jobs",
            "The Theory of Everything"
        ]
    }
    
    return occupation_preferences , movies_by_genre