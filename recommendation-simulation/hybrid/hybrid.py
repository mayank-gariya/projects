import streamlit as st
import pandas as pd

from recommendation-simulation.demographic.movielens.cache_data import load_movies_data
from recommendation-simulation.contentrcs.recommendation import get_recommendation
from recommendation-simulation.collaborative.engine import taste_profile, recommendation

st.set_page_config(page_title="Hybrid Recommender", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
        /* Main application background override */
        .stApp, [data-testid="stAppViewContainer"] {
            background-color: #0b0b0c !important;
            color: #f1f1f1 !important;
        }
        
        /* Headers and Typography */
        h1, h2, h3, h4, h5, h6, label {
            color: #ffffff !important;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        
        /* Global Accent Elements & Active Sliders */
        .stSlider [data-baseweb="slider"] [role="slider"] {
            background-color: #E50914 !important;
        }
        
        /* Action Buttons */
        div.stButton > button:first-child {
            background-color: #E50914 !important;
            color: white !important;
            border: none !important;
            font-weight: 600 !important;
            transition: all 0.3s ease;
            box-shadow: 0px 4px 15px rgba(229, 9, 20, 0.3);
        }
        div.stButton > button:first-child:hover {
            background-color: #ff1f29 !important;
            transform: translateY(-1px);
            box-shadow: 0px 6px 20px rgba(229, 9, 20, 0.5);
        }
        
        /* Custom UI Info Boxes */
        div[data-testid="stNotification"] {
            background-color: #16161a !important;
            border-left: 4px solid #E50914 !important;
            border-radius: 4px;
        }
        
        /* Interactive Tabs Customization */
        button[data-baseweb="tab"] {
            color: #8c8c8c !important;
            font-size: 16px !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #E50914 !important;
            border-bottom-color: #E50914 !important;
            font-weight: bold !important;
        }
        
        /* Selectboxes and Input Fields styling */
        div[data-baseweb="select"] > div {
            background-color: #16161a !important;
            color: white !important;
            border-color: #333333 !important;
        }
        
        /* Dataframes & Tables */
        div[data-testid="stDataFrame"] {
            background-color: #16161a !important;
            border-radius: 8px;
            padding: 5px;
        }
        
        hr {
            border-top: 1px solid #222222 !important;
        }
    </style>
""", unsafe_allow_html=True)


st.title("🚀 Hybrid Recommendation System")

users, ratings, movies = load_movies_data()

tab1, tab2 = st.tabs([
    "🎬 Hybrid Demo",
    "📚 Learn"
])

with tab1:
    st.subheader("⚖️ Hybrid Weight Settings")

    movie_name = st.selectbox(
        "Select a movie",
        sorted(movies["title"])
    )

    weight = st.slider(
        "Content-Based Weight",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1
    )

    st.info(
        f"""
        **Content Weight:** {weight:.1f}  |  **Collaborative Weight:** {1-weight:.1f}
        """
    )

    generate_btn = st.button(
        "🎯 Generate Hybrid Recommendations",
        use_container_width=True
    )

    if generate_btn:
        # CONTENT RECOMMENDATIONS
        content_df = get_recommendation(movie_name)

        content_df = content_df.rename(
            columns={
                "title": "Movie",
                "similarity_score": "Content Score"
            }
        )[["Movie", "Content Score"]]
        
        # COLLABORATIVE RECOMMENDATIONS
        if (
            "liked_movies" not in st.session_state
            or len(st.session_state.liked_movies) < 3
        ):
            st.warning(
                "⚠️ Please like at least 3 movies in the Collaborative Simulator first."
            )

        else:
            profile = taste_profile(
                st.session_state.liked_movies,
                movies
            )

            collab_recs = recommendation(
                profile,
                movies,
                st.session_state.liked_movies
            )

            collab_df = pd.DataFrame(
                collab_recs,
                columns=["Movie", "Collaborative Score"]
            )

            hybrid_df = pd.merge(
                content_df,
                collab_df,
                on="Movie",
                how="outer"
            ).fillna(0)

            hybrid_df["Hybrid Score"] = (
                weight * hybrid_df["Content Score"]
                +
                (1 - weight) * hybrid_df["Collaborative Score"]
            )

            hybrid_df = hybrid_df.sort_values(
                "Hybrid Score",
                ascending=False
            )

            st.subheader("🎯 Top Recommendations For You")

            st.dataframe(
                hybrid_df.head(10),
                use_container_width=True,
                hide_index=True
            )

            st.bar_chart(
                hybrid_df.head(10).set_index("Movie")["Hybrid Score"]
            )

with tab2:
    st.header("📚 Quick Guide: Hybrid Recommenders")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🔍 What is it?
        A **Hybrid System** merges two distinct data perspectives to find your next favorite movie:
        
        * **Content-Based Filtering:** Analyzes item properties (genres, directors, keywords). *e.g., If you watch Iron Man, you get Thor.*
        * **Collaborative Filtering:** Analyzes community behavior (patterns from lookalike users). *e.g., Users who liked what you liked also watched Inception.*
        """)
        
    with col2:
        st.markdown("""
        ### 🚀 Why use it?
        * **No "Cold Start" Glitches:** Brand new movies with no ratings can still be suggested via metadata tags.
        * **Maximized Accuracy:** Seamlessly balances specific personal taste profiles with dynamic global trends.
        * **The Standard:** The core strategy deployed across **Netflix, Spotify, and YouTube**.
        """)

    st.markdown("---")
    st.markdown("### 🧮 How It's Calculated")
    
    st.latex(r"\text{Hybrid Score} = (W \times S_{\text{content}}) + ((1 - W) \times S_{\text{collab}})")
    
    st.markdown("""
    > 💡 **Where:**
    > * $W$ = Content Weight (controlled by your slider input)
    > * $S_{\text{content}}$ = Matching features score between your selections.
    > * $S_{\text{collab}}$ = Match frequency score generated from similar user profiles.
    """)
