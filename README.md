🏥 Hospital Readmission Prediction

https://img.shields.io/badge/Python-3.10%2B-blue?logo=python  
https://img.shields.io/badge/Streamlit-App-red?logo=streamlit  
https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn  
https://img.shields.io/badge/Deploy-Render-green?logo=render  
https://img.shields.io/badge/Build-Passing-brightgreen

🔗 Live Demo
👉 Hospital Readmission Predictor on Render (hospital-readmission-predictor.onrender.com in Bing)  

📌 Project Overview
Hospital readmissions are a major global challenge — costing US hospitals $26B annually and wasting scarce beds in Nigeria.
This project builds a Logistic Regression pipeline to predict readmission risk, and wraps it in a deployable app stack.

It combines:

Machine Learning (Logistic Regression) trained in Google Colab

Streamlit App for interactive demo and visualization

Saved Models + Preprocessor for deployment‑ready reproducibility

Backend folder with Flask API (optional, for REST endpoints)

📂 Repository Structure
backend/ → Flask API + saved models (readmission_model.pkl, preprocessor.pkl)

notebooks/ → Colab training notebook (hospital_readmissions.ipynb)

app.py → Streamlit app interface (latest demo)

images/ → Screenshots of the app

README.md → Project documentation

🚀 How to Run
1. Clone the repository
bash
git clone https://github.com/KelechiFrancisca/hospital-readmission-api.git
cd hospital-readmission-api
2. Install dependencies
bash
pip install -r requirements.txt
3. Run the Streamlit App (Interactive Demo)
bash
streamlit run app.py
This will open the app in the browser at http://localhost:8501.

(Optional) Run the Flask API:

bash
cd backend
python run_readmission.py

📊 Model Performance
Logistic Regression Accuracy: ~85% (depending on dataset split)

Stratified train/test split to handle class imbalance

Confusion Matrix + Classification Report included

Feature Importance: top risk factors (e.g., number of medications, age group) extracted from coefficients

🛠 Tech Stack
Python (pandas, scikit‑learn, joblib)

Streamlit (interactive demo app)

Flask (optional backend API)

Google Colab (model training)

Render / Streamlit Cloud (deployment)

🌍 Deployment
Streamlit App offers a lightweight demo interface

Backend API serves predictions via /predict endpoint

Ready for deployment on Render, Heroku, or Streamlit Cloud

💡 Impact
Problem: 30‑day readmissions cost billions and waste hospital resources.

Solution: Predictive model to flag high‑risk patients early.

Impact: Hospitals can intervene sooner, saving lives and reducing costs.

## 📸 Screenshots

### Streamlit App Inputs
![Hospital Readmission Predictor Inputs](images_streamlit_inputs.png)

### Prediction Result
![Hospital Readmission Predictor Result](images_streamlit_result.png)


👥 Contributors
Kelechi Francisca (Lead Developer, Data Scientist)

🔮 Future Work
This project is designed with long‑term impact in mind, extending well beyond its initial demonstration:

Hospital workflow integration → Embed predictions into discharge planning to flag high‑risk patients and schedule timely follow‑ups.

Healthcare cost reduction → Help hospitals avoid Medicare/insurance penalties and reduce billions in readmission costs.

Patient‑centered care → Extend the model to include social determinants of health (housing, food security, isolation).

Policy and public health → Governments and health systems could adopt predictive tools to monitor hospital performance.

Technology expansion → Integrate with EHRs via HL7 FHIR APIs, deploy on cloud platforms, or create mobile apps for patient reminders