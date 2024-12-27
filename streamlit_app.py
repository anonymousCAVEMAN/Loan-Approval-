import streamlit as st
import requests
import json

# Title
st.title("Loan Application Form")

# Input 1: Person Age
person_age = st.number_input("Enter your age", min_value=18, max_value=100)

# Input 2: Person Income
person_income = st.number_input("Enter your annual income", min_value=1, max_value=1000000)

# Input 3: Person Home Ownership
person_home_ownership = st.selectbox("Select your home ownership status", ["RENT", "OWN", "MORTGAGE"])

# Input 4: Person Employment Length (in months)
person_emp_length = st.number_input("Enter your employment length (in months)", min_value=0, max_value=600)

# Input 5: Loan Grade
loan_grade = st.selectbox("Select the loan grade", ["A", "B", "C", "D", "E", "F", "G"])

# loan_amount 
loan_amnt = st.number_input("Enter the loan amount", min_value=1,max_value=38500)

# Input 6: Loan Intent
loan_intent = st.selectbox("Select the loan intent", ["DEBT CONSOLIDATION", "HOME IMPROVEMENT","VENTURE","PERSONAL","MEDICAL", "EDUCATION"])

# Input 7: Loan Interest Rate
loan_int_rate = st.number_input("Enter the loan interest rate", min_value=0.0, max_value=100.0)

# Input 8: Person Default on File
cb_person_default_on_file = st.selectbox("Have you ever defaulted on a loan?", ["Yes", "No"])

# Input 9: Person Credit History Length
cb_person_cred_hist_length = st.number_input("Enter your credit history length (in months)", min_value=0, max_value=600)

# Calculate Loan Percent Income
# Calculate Loan Percent Income
loan_percent_income = 0  # Default value to avoid potential errors
if loan_amnt and person_income:
    loan_percent_income = round((loan_amnt / person_income), 3)
    st.write("Loan Percent Income: ", loan_percent_income)
# Create a dictionary of the inputs
data = {
    "person_age": int(person_age),
    "person_income": float(person_income),
    "person_home_ownership": person_home_ownership,
    "person_emp_length": float(person_emp_length),
    "loan_intent": loan_intent,
    "loan_grade": loan_grade,
    "loan_amnt": int(loan_amnt),
    "loan_int_rate": float(loan_int_rate),
    "loan_percent_income": float(loan_percent_income),
    "cb_person_default_on_file": cb_person_default_on_file,
    "cb_person_cred_hist_length": int(cb_person_cred_hist_length) }

# Submit button
# if st.button("Submit"):
#     # Send the data to the API
#     url = "http://127.0.0.1:8000/predict"
#     st.write(data)
#     payload = data
#     response = requests.post(url=url, data=payload)
#     # Display the output of the ML model
#     if response.status_code == 200:
#         st.write("ML Model Output: ", response.json())
#     else:
#         st.write("Error: ", response.text)

if st.button("Submit"):
    # Send the data to FastAPI
    url = "http://127.0.0.1:8000/predict"  
    try:
        # Send the request as JSON payload
        response = requests.post(url, json=data)  # Use the 'json' argument instead of 'data'
        if response.status_code == 200:
            st.write("ML Model Output: ", response.json())
        else:
            st.error("Server returned an error: " + response.text)
    except Exception as e:
        st.error("Error occurred while communicating with server: " + str(e))
    st.write("Sending the following data to server: ", data)