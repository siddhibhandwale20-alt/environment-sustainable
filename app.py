import streamlit as st
import pickle
import numpy as np


st.title("Check the environment")


#Input data
carbon_emissions=st.number_input("Carbon emission Amount :",min_value=0.0,format="%f")
energy_output=st.number_input("Energy Output Value:",min_value=0.0,format="%f")
renewability_index=st.number_input("renewability_index Amount:",min_value=0.0,format="%f")
cost_efficiency=st.number_input("cost_efficiency Amount:",min_value=0.0,format="%f")

#Model importing
with open('model.pkl','rb') as file:
    model=pickle.load(file)
#predict
if st.button ("Predict"):
    input_data=np.array([[carbon_emissions,energy_output,renewability_index,cost_efficiency]])

    prediction = model.predict(input_data)
    #Display the result
    if prediction[0]==1:
        st.success("Congrats ,This environment is sustainable")
    else:
        st.info("It is not sustainable")    