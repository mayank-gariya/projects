import streamlit as st
from recommendation-simulation.demographic.sythetic.helper import get_data
import pandas as pd

occupation_preferences , movies_data_genre = get_data()
#synthetic users 
synthetic_users = [
    {"age": 18, "gender": "M", "occupation": "Student"},
    {"age": 22, "gender": "F", "occupation": "Student"},
    {"age": 27, "gender": "M", "occupation": "Engineer"},
    {"age": 35, "gender": "F", "occupation": "Teacher"},
    {"age": 42, "gender": "M", "occupation": "Doctor"},
]

# weights
occupation_weights = {
    "Student": {
        "Action": 4,
        "Comedy": 3,
        "Sci-Fi": 3
    },
    "Engineer": {
        "Sci-Fi": 5,
        "Action": 3,
        "Documentary": 2
    },
    "Teacher": {
        "Drama": 4,
        "Biography": 3,
        "Comedy": 3
    },
    "Doctor": {
        "Biography": 4,
        "Drama": 3,
        "Documentary": 3
    }
}
    
age = st.slider(
    "Age",
    15,
    70,
    25
)

# age influence
if age <= 20:
    genre_bonus = {
        "Action": 2,
        "Comedy": 2
    }

elif age <= 35:
    genre_bonus = {
        "Sci-Fi": 2,
        "Action": 1
    }

else:
    genre_bonus = {
        "Drama": 2,
        "Biography": 2
    }
    
gender = st.selectbox(
    "Gender",
    ["M", "F"]
)

if gender == "M":
    gender_bonus = {
        "Action": 1,
        "Sci-Fi": 1
    }

else:
    gender_bonus = {
        "Drama": 1,
        "Comedy": 1
    }

occupation = st.selectbox(
    "Occupation",
    [
        "Student",
        "Engineer",
        "Teacher",
        "Doctor"
    ]
)


st.info(f"""
Recommendation Profile

Age: {age}
Gender: {gender}
Occupation: {occupation}

The system will use demographic rules
associated with {occupation}.
""")

pref_df = pd.DataFrame(
    occupation_preferences[occupation].items(),
    columns=["Genre","Weight"]
)

st.bar_chart(
    pref_df.set_index("Genre")
)

top_genre = max(
    occupation_preferences[occupation],
    key=occupation_preferences[occupation].get
)

recommendations = movies_data_genre[top_genre]

st.subheader("🎬 Recommended Movies")

genre_scores = {}

# occupation score
for genre, score in occupation_weights[occupation].items():
    genre_scores[genre] = score

# age score
for genre, score in genre_bonus.items():
    genre_scores[genre] = genre_scores.get(genre, 0) + score

# gender score
for genre, score in gender_bonus.items():
    genre_scores[genre] = genre_scores.get(genre, 0) + score
for movie in recommendations:
    st.write("✅", movie)

st.success(f"""
Recommendation Explanation

Occupation (Engineer)
→ Sci-Fi +5

Age (24)
→ Sci-Fi +2
→ Action +1

Gender (Male)
→ Sci-Fi +1
→ Action +1

Final Scores:

Sci-Fi = 8
Action = 2
Documentary = 2

Top Genre = Sci-Fi
""")

st.success(f"""
Why were these movies recommended?

Occupation: {occupation}

Preferred Genre: {top_genre}

The system assumes people with similar occupations
have similar interests and therefore recommends
movies from the {top_genre} genre.
""")
