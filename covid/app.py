import streamlit as st
import pandas as pd 
import pickle as pk

st.title('covid classification')
Cough_symptoms = st.radio("Cough_symptoms = ", [True,False])
Fever = st.radio("Fever = ", [True, False])
Sore_throat = st.radio("Sore_throat = ", [True ,False])
Headache = st.radio("Headache = ", [True ,False])
Shortness_of_breath = st.radio ("Shortness_of_breath = ",[True ,False])
Known_contact = st.selectbox("Known_contact = ", ["Abroad","Contact with confirmed","Other"])


dbfile = open('Covid_Classification.Pickle','rb')
model = pk.load(dbfile)

if st.button('Predict'):
    if Known_contact == 'Abroad':
        Known_contact = 0
    elif Known_contact =='Contact with confirmed' :
        Known_contact = 1
    else:
        Known_contact = 2       



    df = pd.DataFrame({
        'Cough_symptoms':[Cough_symptoms],
        'Fever':[Fever],
        'Sore_throat':[Sore_throat],
        'Shortness_of_breath':[Shortness_of_breath],
        'Headache':[Headache],
        'Known_contact':[Known_contact]
         })
    st.write(df)

    result = model.predict(df)[0]
    if result == 1:
        st.write("Sorry! Tapai lai covid vayeko cha")
    else :
        st.write("congrats tapai lai covid vayeko chaina")    
    # print(result)
    # st.write(result)
    # st.write("Success!")
    # st.balloons()
    # st.snow()
    # st.write(df)


    

    

