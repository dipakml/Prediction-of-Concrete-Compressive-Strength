# -*- coding: utf-8 -*-
"""
Created on #### ##:##:## 2022

@author: DA
"""

# -*- coding: utf-8 -*-
"""

@Created by: DA
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("XGBoost.pkl","rb")
XGBoost=pickle.load(pickle_in)  

pickle_sc = open("sc.pkl","rb")
sc=pickle.load(pickle_sc)  



def main():
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Concrete Compressive Strength </h2>
    </div>
    """
        
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.markdown('**This is a web application built using Machine Learning for prediction of compressive strength for the concrete. Enter the composition of concrete, this web application will predict the compressive strength**')

    Cement = st.number_input("Cement,kg in a m^3 mixture (Enter any value between 100 to 550)")
    Blast_Furnace_Slag = st.number_input("Blast Furnace Slag, kg in a m^3 mixture (Enter any value between 0 to 360)")
    Fly_Ash = st.number_input("Fly_Ash, kg in a m^3 mixture (Enter any value between 0 to 200)")
    Water = st.number_input("Water, kg in a m^3 mixture (Enter any value between 120 to 250)")
    Super_Plasticizer = st.number_input("Super_Plasticizer, kg in a m^3 mixture (Enter any value between 0 to 32)")
    Coarse_Aggregate = st.number_input("Coarse_Aggregate, kg in a m^3 mixture (Enter any value between 800 to 1150)")
    Fine_Aggregate = st.number_input("Fine_Aggregate, kg in a m^3 mixture (Enter any value between 600 to 1000)")
    Age = st.number_input("Age, Days (Enter any value between 1 to 365)")



    result=""

    if st.button('Predict the compressive strength'):

        result=XGBoost.predict(sc.transform([[Cement,Blast_Furnace_Slag,Fly_Ash,Water,Super_Plasticizer,Coarse_Aggregate,Fine_Aggregate,Age]]))
        st.title("Predicted compressive strength between " +
             str(0.95*result)+"Mpa" + " to " + str(result*1.05)+"Mpa")

        st.markdown('**Note - Compressive stregth is predicted as range (+-5 percent of actual prediction)**')


  
if __name__=='__main__':
    main()
    
    
    