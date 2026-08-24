# Hospital Readmission Prediction

## 📌 Project Overview
This project predicts hospital readmissions using patient data.  
It combines:
- **Machine Learning (Logistic Regression)** trained in Google Colab.
- **Flask API** for serving predictions.
- **React Frontend** for user interaction.

## 📂 Repository Structure
- `backend/` → Flask API + saved models
- `notebooks/` → Colab training notebook
- `README.md` → project documentation

## 🚀 How to Run
### Backend
```bash
cd backend
pip install -r requirements.txt
python run_readmission.py

### Notebook
Open `notebooks/hospital_readmissions.ipynb` in Google Colab to retrain the model.

## 📊 Model Performance
- Logistic Regression Accuracy: ~85% (depending on dataset split)  
- Confusion Matrix visualization included in notebook.

## 🌍 Deployment
- The backend serves predictions via `/predict` endpoint.  
- Frontend provides a dashboard for users.

## 👥 Contributors
- **Kelechi Francisca** (Lead Developer, Data Scientist)
