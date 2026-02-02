import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Missed Diagnosis AI Safety Net", layout="wide")

st.title("🩺 Missed Diagnosis AI Safety Net")
st.markdown("AI-powered clinical decision support for doctors")

st.divider()

# ------------------ PATIENT INPUT ------------------
st.header("Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 0, 100, 30)
    fever = st.selectbox("Fever", ["No", "Yes"])
    chest_pain = st.selectbox("Chest Pain", ["No", "Yes"])
    fatigue = st.selectbox("Fatigue", ["No", "Yes"])

with col2:
    bp = st.slider("Blood Pressure (Systolic)", 80, 200, 120)
    heart_rate = st.slider("Heart Rate", 40, 150, 80)
    diabetes = st.selectbox("Diabetes History", ["No", "Yes"])

# Convert Yes/No to 1/0
fever = 1 if fever == "Yes" else 0
chest_pain = 1 if chest_pain == "Yes" else 0
fatigue = 1 if fatigue == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0

# ------------------ DUMMY ML MODEL ------------------
# Fake training data to simulate AI model
X_train = np.array([
    [25, 0, 0, 0, 120, 80, 0],
    [65, 1, 1, 1, 150, 110, 1],
    [45, 1, 0, 1, 140, 95, 0],
    [70, 1, 1, 1, 160, 120, 1],
    [30, 0, 0, 0, 118, 75, 0]
])

y_train = np.array([0, 1, 0, 1, 0])  # 1 = High Risk

model = LogisticRegression()
model.fit(X_train, y_train)

# ------------------ ANALYSIS BUTTON ------------------
if st.button("Run AI Safety Check"):
    
    patient_data = np.array([[age, fever, chest_pain, fatigue, bp, heart_rate, diabetes]])
    risk_prob = model.predict_proba(patient_data)[0][1]

    st.subheader("🔍 AI Risk Analysis")

    if risk_prob > 0.6:
        st.error("🚨 High Risk of Potentially Missed Serious Condition")
    elif risk_prob > 0.3:
        st.warning("⚠️ Moderate Risk — Consider Further Evaluation")
    else:
        st.success("✅ Low Immediate Risk")

    st.write(f"**Risk Score:** {round(risk_prob * 100, 2)}%")

    # ------------------ VISIT SUMMARY ------------------
    st.divider()
    st.subheader("📝 Visit Summary")

    summary = {
        "Age": age,
        "Fever": fever,
        "Chest Pain": chest_pain,
        "Fatigue": fatigue,
        "Blood Pressure": bp,
        "Heart Rate": heart_rate,
        "Diabetes History": diabetes,
        "AI Risk Score (%)": round(risk_prob * 100, 2)
    }

    summary_df = pd.DataFrame(summary.items(), columns=["Parameter", "Value"])
    st.table(summary_df)

    st.info("This AI system is a decision-support tool and does NOT replace clinical judgment.")
