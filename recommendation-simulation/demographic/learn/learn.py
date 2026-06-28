import streamlit as st

def learn():
    with st.expander("🎯 What is Demographic Filtering?", expanded=True):

        st.markdown("""
        ```

        ### Definition

        Demographic filtering is a recommendation technique that groups users
        based on demographic characteristics such as:

        * Age
        * Gender
        * Occupation
        * Location
        * Education

        The assumption is:

        > People with similar demographic profiles tend to have similar preferences.

        For example:

        | User Profile | Possible Recommendation |
        | ------------ | ----------------------- |
        | Student      | Action Movies           |
        | Engineer     | Science Fiction Movies  |
        | Teacher      | Inspirational Movies    |
        | Teenager     | Superhero Movies        |

        Instead of analyzing individual behavior,
        the system uses demographic information to make recommendations.
        """)


    with st.expander("🧪 Synthetic Demographic Example"):

        st.markdown("""
        ```

        ### Scenario

        Suppose we create a simple rule:

        * Student → Action Movies
        * Engineer → Sci-Fi Movies
        * Teacher → Drama Movies

        User Profile:

        * Age: 24
        * Gender: Male
        * Occupation: Engineer

        Recommendations:

        * Interstellar
        * The Matrix
        * Inception

        ### Pipeline

        User Profile
        ↓
        Occupation = Engineer
        ↓
        Rule Matching
        ↓
        Sci-Fi Category
        ↓
        Recommendations

        This approach is called a **Rule-Based Demographic Recommender**.
        """)


    with st.expander("🎬 MovieLens Demographic Recommendation"):

        st.markdown("""
        ```

        ### Real Data Approach

        Unlike synthetic recommendations,
        MovieLens uses ratings from real users.

        Example:

        Target User:

        * Age: 24
        * Gender: Male
        * Occupation: Technician

        The system:

        1. Finds similar users.
        2. Collects movies they rated highly.
        3. Removes movies already watched.
        4. Recommends the highest-rated unseen movies.

        ### Pipeline

        Target User
        ↓
        Find Similar Demographic Users
        ↓
        Collect Ratings
        ↓
        Aggregate Scores
        ↓
        Rank Movies
        ↓
        Recommendations
        """)

    # ---------------------------------------------------

    # Visual Pipeline

    # ---------------------------------------------------

    with st.expander("⚙️ Recommendation Pipeline"):

        st.code(
        """
        SYNTHETIC ENGINE

        User Profile
        ↓
        Rule Matching
        ↓
        Movie Category
        ↓
        Recommendation

        MOVIELENS ENGINE

        Target User
        ↓
        Find Similar Users
        ↓
        Collect Ratings
        ↓
        Average Scores
        ↓
        Rank Movies
        ↓
        Recommendation
        """
        )

    with st.expander("✅ Advantages"):

        st.markdown("""
        ```

        ### Why use demographic filtering?

        * Easy to implement
        * No complex machine learning required
        * Works even for new users
        * Fast recommendation generation
        * Easy to explain to stakeholders

        This is often used as a baseline recommendation approach.
        """)


    with st.expander("⚠️ Limitations"):

        st.markdown("""
        ```

        ### Challenges

        Two users with the same demographics
        may still have completely different tastes.

        Example:

        User A:

        * 25 years old
        * Male
        * Engineer

        Likes:

        * Horror Movies

        User B:

        * 25 years old
        * Male
        * Engineer

        Likes:

        * Romantic Movies

        A demographic system may treat them as identical.

        This limitation is known as:

        ### Over-Generalization

        """)


    with st.expander("📊 Demographic vs Other Recommendation Systems"):


        st.markdown("""
        ```

        | Method                  | Uses Demographics | Uses User Ratings | Personalization |
        | ----------------------- | ----------------- | ----------------- | --------------- |
        | Demographic Filtering   | ✅                | ❌               | Low             |
        | Content-Based Filtering | ❌                | Partial           | Medium          |
        | Collaborative Filtering | ❌                | ✅               | High            |
        | Hybrid Systems          | ✅                | ✅               | Very High       |

        ### Industry Trend

        Modern platforms such as Netflix, Amazon, Spotify, and YouTube
        rarely rely on demographic filtering alone.

        Instead, demographic information is often combined with:

        * User behavior
        * Viewing history
        * Search history
        * Similar user interactions

        to build hybrid recommendation systems.
        """)


    st.success("""
    Key Takeaways

    • Demographic filtering groups users by shared characteristics.
    • Synthetic systems use predefined rules.
    • MovieLens demonstrates demographic filtering using real user ratings.
    • Demographic filtering is simple and explainable.
    • Modern recommendation systems usually combine multiple approaches.
    """)
