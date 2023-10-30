import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import load
import streamlit as st
from sklearn.metrics import r2_score,accuracy_score

# Load the trained model
random_forest_model = load('random_forest_modelnew.joblib')

# Create a Streamlit app
st.title("Lung Cancer Prediction")
st.write("Welcome to our Lung Cancer Prediction tool. Our goal is to assist you in assessing the likelihood of having lung cancer based on a set of input factors. By providing information about your gender, age, and various symptoms or lifestyle factors, we can offer insights into your potential risk. Please answer the questions below to the best of your knowledge, and our tool will provide you with a prediction regarding the presence of lung cancer. Keep in mind that this tool is for informational purposes only and should not replace professional medical advice. Let's get started")

# Input features via Streamlit widgets
GENDER = st.selectbox("Gender", ["Male", "Female"])
AGE = st.slider("Age", 0, 90, 30)
FATIGUE = st.selectbox("Fatigue", ["No", "Yes"])
ALLERGY = st.selectbox("Allergy", ["No", "Yes"])
SMOKING = st.selectbox("Smoking", ["No", "Yes"])
YELLOW_FINGERS = st.selectbox("Yellow Fingers", ["No", "Yes"])
CHRONIC_DISEASE = st.selectbox("Chronic Disease", ["No", "Yes"])
ALCOHOL_CONSUMING = st.selectbox("Alcohol Consuming", ["No", "Yes"])
COUGHING = st.selectbox("Coughing", ["No", "Yes"])
SHORTNESS_OF_BREATH = st.selectbox("Shortness of Breath", ["No", "Yes"])
SWALLOWING_DIFFICULTY = st.selectbox("Swallowing Difficulty", ["No", "Yes"])
CHEST_PAIN = st.selectbox("Chest Pain", ["No", "Yes"])
WHEEZING = st.selectbox("Wheezing", ["No", "Yes"])
PEER_PRESSURE = st.selectbox("Peer Pressure", ["No", "Yes"])
ANXIETY = st.selectbox("Anxiety", ["No", "Yes"])



# Map user input to numerical values
GENDER = 0 if GENDER == "Male" else 1
# After collecting AGE using the slider
if AGE <= 30:
    AGE_CATEGORY = 0
elif AGE <= 60:
    AGE_CATEGORY = 1
else:
    AGE_CATEGORY = 2



FATIGUE = 0 if FATIGUE == "No" else 1
ALLERGY = 0 if ALLERGY == "No" else 1
SMOKING = 0 if SMOKING == "No" else 1
YELLOW_FINGERS = 0 if YELLOW_FINGERS == "No" else 1
CHRONIC_DISEASE = 0 if CHRONIC_DISEASE == "No" else 1
ALCOHOL_CONSUMING = 0 if ALCOHOL_CONSUMING == "No" else 1
COUGHING = 0 if COUGHING == "No" else 1
SHORTNESS_OF_BREATH = 0 if SHORTNESS_OF_BREATH == "No" else 1
SWALLOWING_DIFFICULTY = 0 if SWALLOWING_DIFFICULTY == "No" else 1
CHEST_PAIN = 0 if CHEST_PAIN == "No" else 1
WHEEZING = 0 if WHEEZING == "No" else 1
PEER_PRESSURE = 0 if PEER_PRESSURE == "No" else 1
ANXIETY = 0 if ANXIETY == "No" else 1

# Create input features list
input_features = [GENDER, AGE, FATIGUE, ALLERGY, SMOKING, YELLOW_FINGERS, CHRONIC_DISEASE, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN, WHEEZING, PEER_PRESSURE, ANXIETY]

if st.button("Predict"):
    # Make a prediction using the trained model
    output = random_forest_model.predict([input_features])

    # Display the prediction result
    st.subheader("Prediction Result:")
    if output[0] == 0:
        st.write("No Lung Cancer (Negative)")
        
    else:
        st.write("Lung Cancer Test Posititve")
        st.write("There is a chance you may have lung cancer.")
        st.write("Please contact your doctor as soon as possible.")