📊 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a customer is likely to churn, combined with an interactive multi-page Streamlit dashboard for real-time predictions and business insights.

🚀 Live Demo

https://churn-prediction-webapp-gjcx3jqthea2zauf7vznfw.streamlit.app/

🎯 Problem Statement

Customer churn is a major challenge for subscription-based businesses.
The goal of this project is to:

1. Predict whether a customer will churn
2. Identify key factors influencing churn
3. Help businesses take proactive retention actions

🧠 Project Overview

This project covers the complete ML lifecycle:

1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. eature Engineering
4 Model Training & Evaluation
5. Model Optimization (threshold tuning)
6. Interactive UI Development
7. Deployment on Streamlit Cloud

⚙️ Tech Stack

1. Python
2. Pandas, NumPy
3. Scikit-learn
4. Matplotlib, Seaborn
5. Streamlit
6. GitHub + Streamlit Cloud (Deployment)

📂 Project Structure

churn-project/
│
├── Prediction.py           # Main prediction UI
├── model.pkl               # Trained ML model
├── scaler.pkl              # Feature scaler
├── churn.csv               # Dataset
├── requirements.txt        # Dependencies
│
├── pages/
│   └── Insights Dashboard.py       # Insights dashboard

🤖 Model Details

1. Model Used: Logistic Regression
2. Class imbalance handled using:
c3. lass_weight="balanced"
4. Threshold tuned from 0.5 → 0.4 to improve recall

📊 Model Performance

1. Accuracy: ~75–82%
2. Recall (Churn): ~88% 🔥
3. Focus: Maximizing churn detection (business priority)

💡 Key Insights

1. Customers with low tenure are more likely to churn
2. Fiber optic users show higher churn rates
3. Month-to-month contracts have highest churn
4. Customers using electronic check payments are more likely to leave
5. Higher monthly charges correlate with increased churn

🖥️ Features

🔹 Prediction Page
1. User-friendly input form
2. Real-time churn prediction
3. Probability score + visual indicator
4. Smart recommendation messages
🔹 Insights Dashboard
1. Churn distribution visualization
2. Tenure Vs Churn
3. Monthly charges Vs churn
4. Customer behavior analysis
5. Business-focused insights

🧪 How to Run Locally

git clone https://github.com/Khushitomar14205/churn-prediction-app.git
cd churn-prediction-app

pip install -r requirements.txt
streamlit run app.py

📈 Future Improvements

1. Add advanced models (Random Forest, XGBoost)
2. Integrate SHAP for explainability
3. Add real-time data integration
4. Improve UI with advanced visualizations

