import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Customer Insights Dashboard")

df = pd.read_csv("Churn.csv")

# Churn Distribution
st.subheader("Customer Churn Distribution Overview")
st.bar_chart(df["Churn"].value_counts())
st.info("💡 Most customers do not churn, but a significant portion (~25%) do, indicating potential retention opportunities.")

# Tenure vs Churn
st.subheader("Tenure vs Churn")
fig, ax = plt.subplots()
sns.boxplot(x="Churn", y="tenure", data=df, ax=ax)
st.pyplot(fig)

# Monthly Charges vs Churn
st.subheader("Monthly Charges vs Churn")
fig, ax = plt.subplots()
sns.boxplot(x="Churn", y="MonthlyCharges", data=df, ax=ax)
st.pyplot(fig)