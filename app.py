import streamlit as st
import joblib
import pandas as pd

# Load Trained Model
model = joblib.load("lead_scoring_model.pkl")

st.title("🚀 AI Lead Intelligence Engine")

st.write("Enter lead details below to predict conversion probability.")

# Input Fields
company_size = st.number_input("Company Size", min_value=1, max_value=5000, value=100)
industry = st.selectbox("Industry", ["SaaS", "FinTech", "Ecommerce", "Healthcare", "EdTech"])
website_visits = st.number_input("Website Visits", min_value=0, max_value=100, value=10)
email_opens = st.number_input("Email Opens", min_value=0, max_value=50, value=3)
budget = st.number_input("Budget", min_value=0, max_value=100000, value=10000)
decision_maker = st.selectbox("Decision Maker", ["No", "Yes"])

# Convert Yes/No to 0/1
decision_maker = 1 if decision_maker == "Yes" else 0

# Prediction
if st.button("Predict Lead Score"):

    input_data = pd.DataFrame([{
        "company_size": company_size,
        "industry": industry,
        "website_visits": website_visits,
        "email_opens": email_opens,
        "budget": budget,
        "decision_maker": decision_maker
    }])

    probability = model.predict_proba(input_data)[0][1]

    st.subheader(f"Lead Score: {probability:.2f}")

    if probability >= 0.7:
        st.success("🔥 High Intent Lead")
    elif probability >= 0.4:
        st.warning("⚠️ Medium Intent Lead")
    else:
        st.error("❌ Low Intent Lead")