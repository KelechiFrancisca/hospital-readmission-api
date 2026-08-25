# Hospital Readmission Prediction

## 📌 Project Overview
Hospital readmissions are a major global challenge — costing US hospitals $26B annually and wasting scarce beds in Nigeria.  
This project builds a **Logistic Regression pipeline** to predict readmission risk, and wraps it in a deployable app stack.

It combines:
- **Machine Learning (Logistic Regression)** trained in Google Colab.
- **Flask API** for serving predictions.
- **React Frontend** for user interaction.
- **Saved Models + Preprocessor** for deployment-ready reproducibility.

## 📂 Repository Structure
- `backend/` → Flask API + saved models (`readmission_model.pkl`, `preprocessor.pkl`)
- `notebooks/` → Colab training notebook (`hospital_readmissions.ipynb`)
- `README.md` → project documentation

## 🚀 How to Run
### Backend
```bash
cd backend
pip install -r requirements.txt
python run_readmission.py


Notebook
Open notebooks/hospital_readmissions.ipynb in Google Colab to retrain the model.

📊 Model Performance
Logistic Regression Accuracy: ~85% (depending on dataset split)

Stratified train/test split to handle class imbalance

Confusion Matrix + Classification Report included

Feature Importance: Top risk factors (e.g., number of medications, age group) extracted from coefficients

🌍 Deployment
Backend serves predictions via /predict endpoint

Frontend provides a dashboard for users

Ready for deployment on Render or Streamlit Cloud

💡 Impact
Problem: 30-day readmissions cost billions and waste hospital resources.

Solution: Predictive model to flag high-risk patients early.

Impact: Hospitals can intervene sooner, saving lives and reducing costs.

## 🚀 Usage

 Clone the repository:
   ```bash
   git clone https://github.com/KelechiFrancisca/hospital-readmission-api.git
   cd hospital-readmission-api


👥 Contributors
Kelechi Francisca (Lead Developer, Data Scientist)
