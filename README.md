\# 🚀 AI Lead Intelligence Engine



\## 📌 Overview

This project builds an end-to-end machine learning system to predict lead conversion probability and prioritize high-intent leads.



\## ❗ Problem

Lead prioritization often depends on manual judgment, leading to inefficient sales efforts.



\## 💡 Solution

An AI-driven system that:

\- Generates synthetic lead data

\- Stores data in PostgreSQL

\- Trains a machine learning model

\- Predicts lead conversion probability

\- Classifies leads into High / Medium / Low intent



\## ⚙️ Workflow

1\. Generate dataset → generate\_leads.py  

2\. Store in PostgreSQL → store\_leads\_postgres.py  

3\. Train ML model → train\_model.py  

4\. Save model (.pkl)  

5\. Build UI → app.py (Streamlit)



\## 🛠️ Tech Stack

\- Python

\- PostgreSQL

\- Pandas, NumPy

\- Scikit-learn

\- Streamlit



\## 📊 Dataset

Synthetic dataset simulating real-world lead behavior:

\- Company size

\- Industry

\- Website visits

\- Email opens

\- Budget

\- Decision maker presence



\## 🤖 Model

\- Logistic Regression

\- Feature encoding + scaling

\- Predicts conversion probability



\## 📈 Output

\- Lead Score (0–1 probability)

\- Intent classification:

&#x20; - High Intent 🔥

&#x20; - Medium Intent ⚠️

&#x20; - Low Intent ❌



\## 🚀 How to Run



```bash

pip install -r requirements.txt

python generate\_leads.py

python store\_leads\_postgres.py

python train\_model.py

streamlit run app.py

```



\## 🔐 Note

No real data is used. Dataset is synthetically generated.

