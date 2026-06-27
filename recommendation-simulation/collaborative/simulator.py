import streamlit as st
import pandas as pd
from recommendation-simulation.demographic.movielens.cache_data import load_movies_data
from recommendation-simulation.collaborative.state import initialize_state
from recommendation-simulation.collaborative.engine import taste_profile, recommendation


# 1. Page Configuration
st.set_page_config(
    page_title="Netflix Recommendation Simulator",
    page_icon="🎬",
    layout="wide"
)

# 2. State & Data Loader
initialize_state()
users, ratings, movies = load_movies_data()

genre_cols = [
    "Action", "Adventure", "Animation", "Children", "Comedy", "Crime",
    "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical",
    "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
]

# 3. Premium Dark/Red UI Theme Stylesheet
st.markdown("""
    <style>
    /* Global Background and Typography Overrides */
    .stApp {
        background-color: #0c0c0e;
        color: #f3f4f6;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #f3f4f6 !important;
    }
    
    /* Elegant Clean Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track {
        background: #0c0c0e;
    }
    ::-webkit-scrollbar-thumb {
        background: #27272a;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #e50914;
    }

    /* Target Streamlit Tabs to match cinematic color palette */
    button[data-baseweb="tab"] {
        color: #a1a1aa !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        background-color: transparent !important;
        transition: all 0.3s ease;
    }
    button[data-baseweb="tab"]:hover {
        color: #ffffff !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #e50914 !important;
        border-bottom-color: #e50914 !important;
        font-weight: 700 !important;
    }
    div[data-styled-with-variants="true"] {
        border-bottom: 1px solid #1f2937;
    }

    /* Customizing Native Streamlit Progress Bars */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #e50914 0%, #b91c1c 100%);
        border-radius: 4px;
    }
    .stProgress > div > div {
        background-color: #27272a;
        height: 8px;
    }

    /* Customizing Primary Button styling */
    .stButton > button[kind="primary"] {
        background-color: #e50914 !important;
        border: none !important;
        color: white !important;
        font-weight: 600 !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 12px rgba(229, 9, 20, 0.2);
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #f43f5e !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.4);
    }

    /* Customizing Secondary Button styling */
    .stButton > button[kind="secondary"] {
        background-color: #1f2937 !important;
        border: 1px solid #374151 !important;
        color: #e5e7eb !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton > button[kind="secondary"]:hover {
        border-color: #9ca3af !important;
        color: #ffffff !important;
        background-color: #27272a !important;
    }

    /* Native Alert styling adjustments */
    div[data-testid="stNotification"] {
        background-color: #111827 !important;
        border: 1px solid #374151 !important;
        border-left: 5px solid #e50914 !important;
    }
    
    hr {
        border-color: #1f2937 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 4. Header Section
st.title("🎬 Netflix Recommendation Simulator")
st.caption("Explore movies, train your taste engine, and generate tailored recommendations instantly.")
st.markdown("---")

# 5. Tab Layout Architecture
tab1, tab2, tab3 = st.tabs([
    "🎯 Discover Movies",
    "✨ Personal Recommendations",
    "🧠 System Insights"
])

# ================= TAB 1: DISCOVER MOVIES =================
with tab1:
    current_movie = movies.iloc[st.session_state.movie_index % len(movies)]
    genres = [col for col in genre_cols if current_movie[col] == 1]
    genres_text = " • ".join(genres)

    # Main Movie Showcase Card
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(145deg, #141416, #050505);
            padding: 40px;
            border-radius: 16px;
            border: 1px solid #27272a;
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
        ">
            <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #e50914;"></div>
            <span style="background-color: #e50914; color: white; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px;">Now Showing</span>
            <h1 style="margin-top: 15px; margin-bottom: 8px; color: #ffffff; font-size: 2.8rem; font-weight: 800; letter-spacing: -0.5px;">{current_movie['title']}</h1>
            <p style="font-size: 15px; color: #a1a1aa; margin-bottom: 24px; display: flex; align-items: center; gap: 6px;">
                <span>📅 Released:</span> <strong style="color: #e5e7eb;">{current_movie['release_date']}</strong>
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span style="background: #1f2937; border: 1px solid #374151; padding: 8px 16px; border-radius: 6px; font-size: 14px; color: #f3f4f6; font-weight: 600; letter-spacing: 0.3px;">🎭 {genres_text}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Progress Section
    progress_val = min(len(st.session_state.liked_movies) / 10, 1.0)
    st.progress(progress_val)
    st.markdown(f"🍿 **Profile Strength:** `{len(st.session_state.liked_movies)}` movies liked — <span style='color: #e50914; font-weight: bold;'>Goal: 10</span>", unsafe_allow_html=True)
    st.write("")

    # Interaction Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("❤️ Like Movie", use_container_width=True, type="primary"):
            st.session_state.liked_movies.append(current_movie["title"])
            st.session_state.movie_index += 1
            st.rerun()
            
    with col2:
        if st.button("⏭️ Skip Next", use_container_width=True, type="secondary"):
            st.session_state.movie_index += 1
            st.rerun()

    st.markdown("---")

    # Dynamic Taste Profile
    if len(st.session_state.liked_movies) > 0:
        st.subheader("📊 Your Evolving Taste Profile")
        profile = taste_profile(st.session_state.liked_movies, movies)
        top_genres = profile.sort_values(ascending=False).head(5)
        st.bar_chart(top_genres, color="#e50914")

# ================= TAB 2: PERSONAL RECOMMENDATIONS =================
with tab2:
    if len(st.session_state.liked_movies) < 3:
        st.warning("🔒 **Recommendations Locked:** Please like at least **3 movies** in the Discover tab to build your engine baseline.")
    else:
        profile = taste_profile(st.session_state.liked_movies, movies)
        recommendations = recommendation(profile, movies, st.session_state.liked_movies)
        
        rec_df = pd.DataFrame(recommendations, columns=["Movie", "Score"])
        
        st.subheader("✨ Top Picks Tailored For You")
        st.write("")
                
        top_5_recs = rec_df.head(5)
        chunk_size = 3

        for i in range(0, len(top_5_recs), chunk_size):
            chunk = top_5_recs.iloc[i : i + chunk_size]

            cols = st.columns(len(chunk))

            for chunk_idx, (idx, row) in enumerate(chunk.iterrows()):
                with cols[chunk_idx]:
                    st.markdown(
                        f"""
                        <div style="
                            background: #111113;
                            border: 1px solid #232326;
                            border-top: 4px solid #e50914;
                            border-radius: 10px;
                            padding: 24px;
                            height: 200px;
                            display: flex;
                            flex-direction: column;
                            justify-content: space-between;
                            box-shadow: 0 10px 20px rgba(0,0,0,0.4);
                        ">
                            <div>
                                <h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 700; line-height: 1.4; max-height: 65px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">🍿 {row['Movie']}</h4>
                            </div>
                            <div>
                                <p style="margin: 0 0 6px 0; font-size: 11px; color: #71717a; text-transform: uppercase; font-weight: 700; letter-spacing: 1px;">Match Affinity</p>
                                <h3 style="margin: 0; color: #e50914; font-size: 1.8rem; font-weight: 800; letter-spacing: -0.5px;">{row['Score']*100:.1f}%</h3>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            
            st.write("") 

        st.markdown("---")
        st.subheader("📈 Recommendation Strength Comparison")
        chart_df = rec_df.head(10).set_index("Movie")
        st.bar_chart(chart_df["Score"], color="#b91c1c")


# ================= TAB 3: SYSTEM INSIGHTS =================
with tab3:
    st.header("🧠 How Collaborative Recommendations Work")
    
    st.markdown("""
    This application simulates a production-grade **Collaborative Filtering** algorithmic architecture. 
    Rather than looking purely at item-level descriptive attributes, it uncovers hidden affinities by analyzing patterns 
    and shared behaviors across the collective **User-Item Interaction Matrix**.
    """)
    st.write("")

    col_step1, col_step2, col_step3 = st.columns(3)
    with col_step1:
        st.markdown(
            """
            <div style="background: #111113; border: 1px solid #232326; padding: 24px; border-radius: 8px; min-height: 200px;">
                <h3 style="color: #e50914 !important; font-size: 1.25rem; font-weight:700; margin-top:0;">1. Matrix Construction</h3>
                <p style="color: #a1a1aa; font-size: 14px; margin: 0; line-height:1.6;">Your explicitly logged movie <strong>Likes</strong> are ingested into a sparse interaction grid alongside historical ratings from thousands of streaming profiles.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col_step2:
        st.markdown(
            """
            <div style="background: #111113; border: 1px solid #232326; padding: 24px; border-radius: 8px; min-height: 200px;">
                <h3 style="color: #e50914 !important; font-size: 1.25rem; font-weight:700; margin-top:0;">2. Latent Embeddings</h3>
                <p style="color: #a1a1aa; font-size: 14px; margin: 0; line-height:1.6;">The algorithmic system processes dense vector dimensions, identifying complex co-occurrence clusters and underlying content relationships hidden from raw text features.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col_step3:
        st.markdown(
            """
            <div style="background: #111113; border: 1px solid #232326; padding: 24px; border-radius: 8px; min-height: 200px;">
                <h3 style="color: #e50914 !important; font-size: 1.25rem; font-weight:700; margin-top:0;">3. Neighbor Similarity</h3>
                <p style="color: #a1a1aa; font-size: 14px; margin: 0; line-height:1.6;">Using high-performance mathematical comparisons (such as Cosine or Dot-Product similarity), the engine routes titles preferred by your lookalike demographic vectors straight to your feed.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    st.write("")
    st.info("💡 **Pro-Tip:** True collaborative systems rely heavily on collective data densities. As you log more unique interaction entries, your neighborhood coordinates continuously adapt to prioritize unexpected hidden gems.")
