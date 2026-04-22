import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Get correct feature order from model
feature_order = model.feature_names_in_

# Title
st.title("Customer Churn Prediction")

# Inputs
age = st.number_input("Age", 18, 100)
services = st.number_input("Services Opted", 1, 10)

frequent = st.selectbox("Frequent Flyer", ["Yes", "No"])
income = st.selectbox("Income Class", ["Low Income", "Middle Income"])
social = st.selectbox("Social Media", ["Yes", "No"])

# Convert input to model format
data = {
    "Age": age,
    "ServicesOpted": services,

    # Only include columns used in training
    "FrequentFlyer_Yes": 1 if frequent == "Yes" else 0,
    "FrequentFlyer_No Record": 0,

    "AnnualIncomeClass_Low Income": 1 if income == "Low Income" else 0,
    "AnnualIncomeClass_Middle Income": 1 if income == "Middle Income" else 0,

    "AccountSyncedToSocialMedia_Yes": 1 if social == "Yes" else 0,

    "BookedHotelOrNot_Yes": 0
}

# Create dataframe
df = pd.DataFrame([data])

# Ensure correct column order
df = df[feature_order]

# Predict button
if st.button("Predict"):
    prediction = model.predict(df)

    if prediction[0] == 1:
        st.error("Customer will Churn ❌")
    else:
        st.success("Customer will NOT Churn ✅")