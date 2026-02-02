🚨 Problem

In high-pressure healthcare environments, doctors often handle large patient volumes with limited consultation time. This can lead to unintentional missed diagnoses, which may delay treatment and affect patient outcomes.

There is a need for an intelligent safety layer that assists — not replaces — doctors in detecting hidden risk patterns.

💡 Proposed Solution

Missed Diagnosis AI Safety Net acts as a second clinical reviewer.
It analyzes patient symptoms, vital signs, and medical history to:

Detect high-risk combinations

Alert doctors to possible overlooked conditions

Provide explainable reasoning behind alerts

Generate structured visit summaries

This system supports clinical decision-making while keeping doctors in control.

⚙️ Features

✅ Doctor-friendly web interface
✅ AI-based risk prediction model
✅ Risk level alerts (Low / Moderate / High)
✅ 🧠 Explainable AI — “Why This Alert?” panel
✅ Automatic Visit Summary
✅ Decision-support disclaimer for ethical use

🧠 How It Works

Doctor enters patient data (age, symptoms, vitals, history)

Data is processed by a Machine Learning model (Logistic Regression)

The system calculates a risk probability

Alerts are generated if risk crosses threshold

Explainable AI shows factors that triggered the alert

Visit summary is produced for documentation

🛠️ Tech Stack
Technology	Purpose
Streamlit	Web-based medical interface
Pandas	Patient data handling
NumPy	Numerical processing
Scikit-learn	Machine learning model
