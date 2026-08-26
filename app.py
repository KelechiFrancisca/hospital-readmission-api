import streamlit as st
import joblib
import pandas as pd

# Load model and preprocessor
model = joblib.load("backend/readmission_model.pkl")
preprocessor = joblib.load("backend/preprocessor.pkl")

st.set_page_config(page_title="Hospital Readmission Predictor", page_icon="🏥")

st.title("🏥 Hospital Readmission Predictor")
st.write("This app predicts whether a patient is likely to be readmitted based on clinical features.")

# Age mapping (convert string ranges to numeric midpoints)
age_map = {
    "[0-10)": 5, "[10-20)": 15, "[20-30)": 25, "[30-40)": 35,
    "[40-50)": 45, "[50-60)": 55, "[60-70)": 65, "[70-80)": 75,
    "[80-90)": 85, "[90-100)": 95
}

# Input fields (16 features)
age = st.selectbox("Age group", list(age_map.keys()), index=5)  # default: [50-60)
age_value = age_map[age]  # convert to numeric midpoint

time_in_hospital = st.slider("Time in hospital (days)", 1, 14, 3)
n_lab_procedures = st.slider("Number of lab procedures", 0, 150, 40)
n_procedures = st.slider("Number of procedures", 0, 20, 1)
n_medications = st.slider("Number of medications", 0, 50, 10)
n_outpatient = st.slider("Number of outpatient visits", 0, 20, 0)
n_inpatient = st.slider("Number of inpatient visits", 0, 20, 0)
n_emergency = st.slider("Number of emergency visits", 0, 20, 0)

medical_specialty = st.selectbox("Medical specialty", [
    "Cardiology", "Endocrinology", "Family/GeneralPractice", "InternalMedicine",
    "Surgery", "Orthopedics", "Other"
], index=0)

diag_1 = st.text_input("Primary diagnosis code (diag_1)", value="250")
diag_2 = st.text_input("Secondary diagnosis code (diag_2)", value="401")
diag_3 = st.text_input("Additional diagnosis code (diag_3)", value="414")

glucose_test = st.selectbox("Glucose test performed?", ["Yes", "No"], index=0)
A1Ctest = st.selectbox("A1C test performed?", ["Yes", "No"], index=0)
change = st.selectbox("Medication change?", ["Yes", "No"], index=0)
diabetes_med = st.selectbox("On diabetes medication?", ["Yes", "No"], index=0)

# Prediction button
if st.button("Predict Readmission"):
    # Build input as a DataFrame with correct column names
    X_input = pd.DataFrame([{
        "age": age_value,  # numeric midpoint
        "time_in_hospital": time_in_hospital,
        "n_lab_procedures": n_lab_procedures,
        "n_procedures": n_procedures,
        "n_medications": n_medications,
        "n_outpatient": n_outpatient,
        "n_inpatient": n_inpatient,
        "n_emergency": n_emergency,
        "medical_specialty": medical_specialty,
        "diag_1": diag_1,
        "diag_2": diag_2,
        "diag_3": diag_3,
        "glucose_test": glucose_test,
        "A1Ctest": A1Ctest,
        "change": change,
        "diabetes_med": diabetes_med
    }])

    # Transform and predict
    X_processed = preprocessor.transform(X_input)
    prediction = model.predict(X_processed)
    probability = model.predict_proba(X_processed)[0][1]

    # Determine risk level
    if probability >= 0.7:
        risk_level = "HIGH"
        recommendation = "Schedule follow-up call within 7 days."
    elif probability >= 0.4:
        risk_level = "MEDIUM"
        recommendation = "Monitor patient and schedule routine check-up."
    else:
        risk_level = "LOW"
        recommendation = "Standard care, no immediate action required."

    # Styled output
    if prediction[0] == 1:
        st.error(f"⚠️ Patient is **likely** to be readmitted.\n\n"
                 f"**Risk Level:** {risk_level}\n"
                 f"**Probability:** {probability:.0%}\n"
                 f"**Recommendation:** {recommendation}")
    else:
        st.success(f"✅ Patient is **not likely** to be readmitted.\n\n"
                   f"**Risk Level:** {risk_level}\n"
                   f"**Probability:** {probability:.0%}\n"
                   f"**Recommendation:** {recommendation}")

# Footer
st.markdown("---")
st.markdown("Built by **Kelechi Francisca** | Model: Logistic Regression | Data: Hospital Readmissions Dataset")
