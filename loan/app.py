import streamlit as st
import pickle as pk
import pandas as pd
import numpy as np


st.title ('Loan Classification')
person_education = st.radio("person_education = ", [True, False])
person_income = st.radio("person_income = ",[True, False ])
person_emp_exp = st.radio("person_emp_exp = ", [True , False])
person_home_ownership = st.radio("person_home_ownership Enter = ", [True , False])
loan_amnt = st.radio("loan_amnt = ",[True , False])
loan_intent = st.radio("loan_intent = ",[True ,False])
loan_int_rate = st.radio("loan_int_rate =", [True , False])
loan_percent_income = st.selectbox()
cb_person_cred_hist_length = st.radio("cb_person_cred_hist_length = ", [True ,False])
credit_score= st.radio("credit_score = ", [True ,False])
previous_loan_default_on_file = st.radio("previous_loan_defaults_on_file = ",[True,False])