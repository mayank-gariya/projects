import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Suppress the specific version warning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Customer Churn Prediction Dashboard")
st.write("Enter the customer details to predict churn risk.")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100)
        gender = st.selectbox("Gender", ["Male", "Female"])
        tenure = st.number_input("Tenure (months)", min_value=0)
        usage_freq = st.number_input("Usage Frequency", min_value=0)
        support_calls = st.number_input("Support Calls", min_value=0)
        
    with col2:
        payment_delay = st.number_input("Payment Delay (days)", min_value=0)
        sub_type = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
        contract_len = st.selectbox("Contract Length", ["Monthly", "Yearly"])
        total_spend = st.number_input("Total Spend", min_value=0.0)
        last_interaction = st.number_input("Days Since Last Interaction", min_value=0)

    submit = st.form_submit_button("Predict Churn")


input_data = np.array([
        age,gender,tenure, 
        usage_freq,support_calls, 
        payment_delay,sub_type, 
        contract_len ,total_spend,last_interaction
]).reshape(1,-1)
    
prediction = model.predict(input_data)

if prediction == 0 :
    st.text('no churn')
else:
    st.text('churn')