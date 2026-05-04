import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ---------------- TITLE ----------------
st.set_page_config(page_title="Churn Predictor", layout="centered")

st.title("📊 Customer Churn Prediction System")
st.markdown("Predict whether a customer is likely to churn based on their service usage and billing details.")

# ---------------- INPUT SECTIONS ----------------

st.subheader("👤 Customer Information")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen?", [0, 1])
    Partner = st.selectbox("Has Partner?", ["Yes", "No"])

with col2:
    Dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72)
    PhoneService = st.selectbox("Phone Service?", ["Yes", "No"])

# ---------------- SERVICES ----------------

st.subheader("📞 Services")

col3, col4 = st.columns(2)

with col3:
    MultipleLines = st.selectbox("Multiple Lines?", ["Yes", "No"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security?", ["Yes", "No"])
    OnlineBackup = st.selectbox("Online Backup?", ["Yes", "No"])

with col4:
    DeviceProtection = st.selectbox("Device Protection?", ["Yes", "No"])
    TechSupport = st.selectbox("Tech Support?", ["Yes", "No"])
    StreamingTV = st.selectbox("Streaming TV?", ["Yes", "No"])
    StreamingMovies = st.selectbox("Streaming Movies?", ["Yes", "No"])

# ---------------- BILLING ----------------

st.subheader("💳 Billing Information")

col5, col6 = st.columns(2)

with col5:
    Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing?", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])

with col6:
    MonthlyCharges = st.number_input("Monthly Charges", value=50.0)
    TotalCharges = st.number_input("Total Charges", value=1000.0)

# ---------------- PREPROCESS ----------------

def preprocess():
    data = {
        'gender': 1 if gender == "Male" else 0,
        'SeniorCitizen': SeniorCitizen,
        'Partner': 1 if Partner == "Yes" else 0,
        'Dependents': 1 if Dependents == "Yes" else 0,
        'tenure': tenure,
        'PhoneService': 1 if PhoneService == "Yes" else 0,
        'MultipleLines': 1 if MultipleLines == "Yes" else 0,
        'OnlineSecurity': 1 if OnlineSecurity == "Yes" else 0,
        'OnlineBackup': 1 if OnlineBackup == "Yes" else 0,
        'DeviceProtection': 1 if DeviceProtection == "Yes" else 0,
        'TechSupport': 1 if TechSupport == "Yes" else 0,
        'StreamingTV': 1 if StreamingTV == "Yes" else 0,
        'StreamingMovies': 1 if StreamingMovies == "Yes" else 0,
        'PaperlessBilling': 1 if PaperlessBilling == "Yes" else 0,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,

        'InternetService_Fiber optic': 1 if InternetService == "Fiber optic" else 0,
        'InternetService_No': 1 if InternetService == "No" else 0,

        'Contract_One year': 1 if Contract == "One year" else 0,
        'Contract_Two year': 1 if Contract == "Two year" else 0,

        'PaymentMethod_Credit card (automatic)': 1 if PaymentMethod == "Credit card (automatic)" else 0,
        'PaymentMethod_Electronic check': 1 if PaymentMethod == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if PaymentMethod == "Mailed check" else 0,
    }

    return pd.DataFrame([data])

# ---------------- PREDICTION ----------------

if st.button("🔍 Predict Churn"):
    input_df = preprocess()
    input_scaled = scaler.transform(input_df)

    prob = model.predict_proba(input_scaled)[0][1]

    st.subheader("📈 Prediction Result")

    # Probability bar
    st.progress(int(prob * 100))
    
    if MonthlyCharges <= 0 or TotalCharges <= 0:
      st.warning("⚠️ Charges should be greater than 0 for valid prediction.")
      st.stop()

    if prob > 0.4:
        st.error(f"⚠️ High Risk of Churn ({prob:.2f})")
        st.warning("💡 Suggestion: Offer discounts, better plans, or customer support.")
    else:
        st.success(f"✅ Low Risk of Churn ({prob:.2f})")
        st.info("💡 Customer is likely satisfied. Maintain engagement.")

# ---------------- OPTIONAL CHARTS ----------------

st.subheader("📊 Sample Insights")

# Example chart (static demo)
chart_data = pd.DataFrame({
    "Feature": ["Tenure", "MonthlyCharges", "Fiber Internet"],
    "Impact": [0.8, 0.7, 0.9]
})

st.bar_chart(chart_data.set_index("Feature"))

st.markdown("---")
st.caption("Developed by KHUSHI TOMAR | Machine Learning Project")