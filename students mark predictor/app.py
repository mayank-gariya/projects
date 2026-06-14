import streamlit as st
import pickle
import pandas as pd
import numpy as np 

# Set page config for a wider, cleaner layout
st.set_page_config(page_title="Student Score Predictor", page_icon="🎓", layout="wide")

# Load models and data
@st.cache_resource
def load_assets():
    pipe = pickle.load(open(r'data-models\model.pkl', 'rb'))
    data = pickle.load(open(r'data-models\df3.pkl', 'rb'))
    return pipe, data

pipe, data = load_assets()

# Title and Subtitle Styling
st.title('🎓 Student Score Predictor')
st.image('student-score.png',width=500)
st.markdown('Provide the student details below to instantly predict their academic performance score.')

# --- UPPER SIDE PREDICTION SLOTS ---
# These empty containers act as placeholders to display results at the top
result_status = st.empty()
result_metric = st.empty()

st.markdown('---')

# Define dropdown mapping dictionaries
diet_quality = {'Poor': 0, 'Fair': 1, 'Good': 2}
parental_education_level = {'High School' : 0, 'Bachelor' : 1, 'Master' : 2}
internet_quality  = {'Poor' : 0, 'Average' : 1, 'Good' : 2}
gender = {'Male': 1, 'Female': 0}
partime_job = {'Yes': 1, 'No': 0}
extracurricular_activity = {'Yes': 1, 'No': 0}

# Wrap inputs inside a form to prevent lag on input changes
with st.form("student_details_form"):
    
    # Section 1: Numerical/Daily Habits (Two Column Layout)
    st.subheader("📊 Numerical Metrics & Daily Habits")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider('Age of Student', min_value=12, max_value=25, value=17, step=1)
        study_hour = st.slider('Daily Study Hours', min_value=0, max_value=14, value=5, step=1)
        media_hours = st.slider('Social Media Usage (Hours)', min_value=0, max_value=20, value=2, step=1)
        attendence = st.slider('Attendance Percentage (%)', min_value=56, max_value=100, value=75, step=1)

    with col2:
        sleeping_hours = st.slider('Daily Sleep (Hours)', min_value=3, max_value=10, value=8, step=1)
        exercise_hours = st.slider('Exercise (Hours)', min_value=0, max_value=6, value=1, step=1)
        mental_health = st.slider('Mental Health Rating (0 = Poor, 10 = Excellent)', min_value=0, max_value=10, value=2, step=1)

    st.markdown('---')
    
    # Section 2: Categorical/Profile Details (Two Column Layout)
    st.subheader("👤 Student Profile & Environment")
    col3, col4 = st.columns(2)
    
    with col3:
        gender_val = st.selectbox('Gender', options=list(gender.keys()))
        parent_map_val = st.selectbox('Parental Education Level', options=list(parental_education_level.keys()))
        diet_map_val = st.selectbox('Diet Quality', options=list(diet_quality.keys()))

    with col4:
        internet_map_val = st.selectbox('Internet Quality', options=list(internet_quality.keys()))
        parttime_job_val = st.selectbox('Has Part-time Job?', options=list(partime_job.keys()))
        extra_val = st.selectbox('Engaged in Extracurricular Activities?', options=list(extracurricular_activity.keys()))

    # Form Submit Button
    st.markdown('<br>', unsafe_allow_html=True)
    submit_button = st.form_submit_button(label='🔮 Predict Score', use_container_width=True)

# Process prediction only after clicking the submit button
if submit_button:
    # Build feature array with correct mapped integers
    inputs = np.array([
        age, 
        study_hour, 
        media_hours, 
        attendence, 
        sleeping_hours, 
        exercise_hours, 
        diet_quality[diet_map_val], 
        mental_health, 
        parental_education_level[parent_map_val], 
        internet_quality[internet_map_val], 
        gender[gender_val], 
        partime_job[parttime_job_val], 
        extracurricular_activity[extra_val]
    ]).reshape(1, -1)
    
    # Run prediction model
    output = pipe.predict(inputs)[0]
    
    # Inject content back into the upper placeholders
    result_status.success("🎉 Prediction Completed Successfully!")
    result_metric.metric(label="Predicted Exam Score", value=f"{output:.2f}")
