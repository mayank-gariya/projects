import streamlit as st


with st.expander(
        "🎯 What is Content-Based Filtering?",
        expanded=True
    ):

        st.markdown("""
        Content-Based Filtering recommends items that are
        similar to those a user already likes.

        Instead of using demographic information
        or ratings from other users,
        the system focuses on item features.

        Example:

        User likes:
        - Toy Story

        Features:
        - Animation
        - Comedy
        - Children

        Recommended:
        - Aladdin
        - Lion King
        - Beauty and the Beast
        """)

with st.expander(
        "⚙️ Recommendation Pipeline"
    ):

        st.code(
"""
User Selects Movie
        ↓
Extract Movie Features
        ↓
Create Feature Vector
        ↓
Calculate Similarity
        ↓
Rank Similar Movies
        ↓
Generate Recommendations
"""
        )

with st.expander(
        "📊 Example Walkthrough"
    ):

        st.markdown("""
### Example

Movie:

**Toy Story**

Genres:

- Animation
- Comedy
- Children

The system converts these genres into a numerical representation.

Then it compares this representation
with every other movie in the dataset.

Movies with similar genre patterns
receive higher similarity scores.

Finally, the most similar movies are recommended.
""")

with st.expander(
        "🆚 Demographic vs Content-Based"
    ):

        st.markdown("""
| Demographic Filtering | Content-Based Filtering |
|----------------------|------------------------|
| Uses Age | Uses Movie Features |
| Uses Gender | Uses Genres |
| Uses Occupation | Uses Item Attributes |
| Recommends based on Similar Users | Recommends based on Similar Movies |

Example:

Demographic:
24-year-old Engineer
→ Interstellar

Content-Based:
Likes Interstellar
→ The Matrix
→ Arrival
→ Blade Runner
""")

with st.expander(
        "✅ Advantages"
    ):

        st.markdown("""
- Easy to explain
- Personalized recommendations
- No need for other users
- Works well when item features are available
- Transparent recommendation process
""")

with st.expander(
        "⚠️ Limitations"
    ):

        st.markdown("""
- Can become too narrow
- May recommend very similar items repeatedly
- Difficult when item features are limited
- Cannot discover completely new interests
""")

st.success("""
Key Takeaways

• Content-Based Filtering recommends similar items.
• It uses movie features instead of user demographics.
• Similarity is calculated between items.
• Movie genres are commonly used as features.
• It is one of the most important recommendation techniques.
""")