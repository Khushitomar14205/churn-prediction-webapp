📊 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a customer is likely to churn, combined with an interactive multi-page Streamlit dashboard for real-time predictions and business insights.

🚀 Live Demo

https://churn-prediction-webapp-gjcx3jqthea2zauf7vznfw.streamlit.app/

🎯 Problem Statement

Customer churn is a major challenge for subscription-based businesses.
The goal of this project is to:

Predict whether a customer will churn
Identify key factors influencing churn
Help businesses take proactive retention actions

🧠 Project Overview

This project covers the complete ML lifecycle:

Data Cleaning & Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Model Training & Evaluation
Model Optimization (threshold tuning)
Interactive UI Development
Deployment on Streamlit Cloud

⚙️ Tech Stack

Python
Pandas, NumPy
Scikit-learn
Matplotlib, Seaborn
Streamlit
GitHub + Streamlit Cloud (Deployment)

📂 Project Structure

churn-project/
│
├── Prediction.py                  # Main prediction UI
├── model.pkl               # Trained ML model
├── scaler.pkl              # Feature scaler
├── churn.csv               # Dataset
├── requirements.txt        # Dependencies
│
├── pages/
│   └── Insights Dashboard.py       # Insights dashboard

🤖 Model Details

Model Used: Logistic Regression
Class imbalance handled using:
class_weight="balanced"
Threshold tuned from 0.5 → 0.4 to improve recall

📊 Model Performance

Accuracy: ~75–82%
Recall (Churn): ~88% 🔥
Focus: Maximizing churn detection (business priority)

💡 Key Insights

Customers with low tenure are more likely to churn
Fiber optic users show higher churn rates
Month-to-month contracts have highest churn
Customers using electronic check payments are more likely to leave
Higher monthly charges correlate with increased churn

🖥️ Features

🔹 Prediction Page
User-friendly input form
Real-time churn prediction
Probability score + visual indicator
Smart recommendation messages
🔹 Insights Dashboard
Churn distribution visualization
Customer behavior analysis
Business-focused insights

🧪 How to Run Locally

git clone https://github.com/Khushitomar14205/churn-prediction-app.git
cd churn-prediction-app

pip install -r requirements.txt
streamlit run app.py

📈 Future Improvements

Add advanced models (Random Forest, XGBoost)
Integrate SHAP for explainability
Add real-time data integration
Improve UI with advanced visualizations

