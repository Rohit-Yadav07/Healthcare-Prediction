import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Healthcare Multi-Disease Diagnosis",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Set background color and style
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .css-18e3th9 {
        padding-top: 2rem;
    }
    .stApp {
        background: linear-gradient(to bottom, #e0f7fa, #f3e5f5);
        color: #333333;
        font-family: Arial, sans-serif;
    }
    .css-1h0pbdl {
        color: #00796b;
    }
    </style>
    """, unsafe_allow_html=True)

# Get the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
mobility_disorder_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu("Healthcare Multi-Disease Diagnosis",
                           ["Diabetes Prediction", "Heart Disease Prediction", "Mobility Disorder Prediction"],
                           menu_icon="hospital-fill",
                           icons=["activity", "heart", "person"],
                           default_index=0)

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    with col2:
        Age = st.text_input("Age of the Person")

    # Code for Prediction
    diab_diagnosis = ""
    if st.button("Diabetes Test Result"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = "The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic"
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain types")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesterol in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")
    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca = st.text_input("Major vessels colored by fluoroscopy")
    with col1:
        thal = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversible defect")

    # Code for Prediction
    heart_diagnosis = ""
    if st.button("Heart Disease Test Result"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = "The person is having heart disease" if heart_prediction[0] == 1 else "The person does not have heart disease"
    st.success(heart_diagnosis)

# Mobility Disorder Prediction Page
if selected == "Mobility Disorder Prediction":
    st.title("Mobility Disorder Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col1:
        RAP = st.text_input("MDVP:RAP")
    with col2:
        PPQ = st.text_input("MDVP:PPQ")
    with col3:
        DDP = st.text_input("Jitter:DDP")
    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")
    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")
    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")
    with col3:
        APQ = st.text_input("MDVP:APQ")
    with col4:
        DDA = st.text_input("Shimmer:DDA")
    with col5:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("spread1")
    with col5:
        spread2 = st.text_input("spread2")
    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE = st.text_input("PPE")

    # Code for Prediction
    mobility_disorder_diagnosis = ""
    if st.button("Mobility Disorder Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        mobility_disorder_prediction = mobility_disorder_model.predict([user_input])
        mobility_disorder_diagnosis = "The person has a mobility disorder" if mobility_disorder_prediction[0] == 1 else "The person does not have a mobility disorder"
    st.success(mobility_disorder_diagnosis)
