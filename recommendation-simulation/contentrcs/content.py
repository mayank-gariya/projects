import streamlit as st
from recommendation_simulation.demographic.movielens.cache_data import load_movies_data
from recommendation_simulation.contentrcs.recommendation import get_recommendation
import pandas as pd

st.set_page_config(page_title="Content-Based Recommendation System", page_icon="🎭", layout="wide")

st.markdown("""
    <style>
        /* Main background and text */
        .stApp {
            background-color: #0b0c10;
            color: #c5c6c7;
        }
        
        /* Headers and Titles */
        h1, h2, h3, h4, h5, h6, .st-emotion-cache-10trblm {
            color: #ffffff !important;
            font-weight: 700 !important;
        }
        
        /* Highlight Accent (Red) */
        .red-text {
            color: #e50914;
        }
        
        /* Primary Buttons */
        div.stButton > button:first-child {
            background-color: #e50914;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        div.stButton > button:first-child:hover {
            background-color: #b20710;
            color: white;
            box-shadow: 0 0 10px rgba(229, 9, 20, 0.5);
        }
        
        /* Metrics styling */
        div[data-testid="stMetricValue"] {
            color: #e50914 !important;
            font-size: 2rem;
            font-weight: bold;
        }
        
        /* Info/Success/Warning boxes custom styling */
        .stAlert {
            background-color: #1f2833 !important;
            border-left: 5px solid #e50914 !important;
            color: #ffffff !important;
        }
        
        /* Tabs styling */
        button[data-baseweb="tab"] {
            color: #c5c6c7 !important;
            font-size: 1.1rem;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #e50914 !important;
            border-bottom-color: #e50914 !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- App Header ---
st.markdown("<h1 style='margin-bottom: 0;'>🎭 <span style='color: #e50914;'>Content-Based</span> Recommendation System</h1>", unsafe_allow_html=True)
st.caption("Discover movies similar to your favorites using movie features and genres.")
st.markdown("---")

# --- Load Data ---
users, ratings, movies = load_movies_data()

# --- Tabs Setup ---
tab1, tab2 = st.tabs([
    "🎬 Recommendation Demo",
    "📖 Learn"
])

with tab1:
    # Key Metrics Display wrapped in a clean container
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Movies Available", f"{len(movies):,}")
        with col2:
            st.metric("Active Users", f"{len(users):,}")
        with col3:
            st.metric("Total Ratings", f"{len(ratings):,}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Interactive Columns
    left_col, right_col = st.columns([1, 1], gap="large")

    with left_col:
        st.subheader("🔍 Find Your Movie")
        movie_name = st.selectbox(
            "Select a Movie from the database:",
            sorted(movies["title"]),
            label_visibility="collapsed"
        )

        selected_movie = movies[movies["title"] == movie_name].iloc[0]

        genre_cols = [
            "Action","Adventure","Animation",
            "Children","Comedy","Crime",
            "Documentary","Drama","Fantasy",
            "Film-Noir","Horror","Musical",
            "Mystery","Romance","Sci-Fi",
            "Thriller","War","Western"
        ]

        genres = [genre for genre in genre_cols if selected_movie[genre] == 1]

        # Display Selected Movie Metadata
        st.markdown(
            f"""
            <div style="background-color: #141414; padding: 20px; border-radius: 8px; border: 1px solid #282828; margin-top: 10px;">
                <p style="margin: 0; color: #8c8c8c; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Selected Movie</p>
                <h3 style="margin: 5px 0 15px 0; color: #ffffff;">{movie_name}</h3>
                <p style="margin: 0 0 5px 0; color: #8c8c8c; font-weight: bold;">Genres:</p>
                <span style="color: #e50914; font-weight: 500;">{" • ".join(genres)}</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Action Button
        generate_btn = st.button("Generate Similar Movies", use_container_width=True)

    with right_col:
        st.subheader("💡 Concept Guide")
        st.info("""
        **Content-Based Filtering** focuses heavily on the item's DNA.
        
        Instead of tracking what *other* users like, it maps similarities entirely on metadata:
        
        • **Genres & Categories**
        • **Plot Keywords**
        • **Directorial & Cast Attributes**
        
        If you enjoy a specific title, the algorithm instantly isolates candidates sharing the closest matching feature vectors.
        """)

    st.markdown("---")

    # --- Recommendations Output Area ---
    if generate_btn:
        recommendations = get_recommendation(movie_name)

        st.markdown("### 🎯 Recommended For You")
        
        # Display recommendations table
        st.dataframe(
            recommendations,
            use_container_width=True,
            hide_index=True
        )

        st.success(
            f"""
            **Why these recommendations?**

            The engine mapped the feature landscape of **{movie_name}** against the database catalog to output the closest mathematical matches based on its genre fingerprints.
            """
        )

with tab2:
    st.markdown("## 📖 Understanding Content-Based Filtering")
    st.markdown("Below is the structural breakdown execution for this content-based approach.")
    
    try:
        with open("recommendation_simulation/contentrcs/learn.py", "r", encoding="utf-8") as f:
            demographic_code = f.read()
            
        exec(demographic_code)
        
    except FileNotFoundError:
        st.error("❌ Could not find the system learning asset file (`contexrec/learn.py`).")
