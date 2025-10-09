import pickle as pk
import streamlit as st
import pandas as pd

# Title
st.title('Salary Prediction App')

# Load the trained model
with open('salary.pickle', 'rb') as dbfile:
model = pk.load(dbfile)

# User Inputs
age = st.number_input("Enter your age:", min_value=18, max_value=60)
exp = st.number_input("Enter your experience (years):", min_value=0, max_value=40)
gender = st.radio("Select Gender:", ["Male", "Female"])
education = st.selectbox("Select Education Level:", ["Bachelor's", "Master's", "PhD"])

# On button click
if st.button("Predict Salary"):
    
    # Convert gender to binary (assuming model was trained with 'Male' as True/False)
    is_male = True if gender == 'Male' else False

    # One-hot encode education (assuming model was trained with these columns)
    if education == "Bachelor's":
        b, m, p = 1, 0, 0
    elif education == "Master's":
        b, m, p = 0, 1, 0
    else:  # PhD
        b, m, p = 0, 0, 1

    # Create input DataFrame with correct column names
    df = pd.DataFrame({
        'Age': [age],
        'Years of Experience': [exp],
        'Male': [is_male],
        "Bachelor's": [b],
        "Master's": [m],
        "PhD": [p]
    })

    
    st.dataframe(df)

    # Make prediction
    result = round(model.predict(df)[0][0],2)

    # Show result
    st.write(result)
    print(result)
    st.balloons()
    st.snow()
    st.success("Prediction successful!")
