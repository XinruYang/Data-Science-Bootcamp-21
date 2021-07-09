import re
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import requests
import os,sys

dir = os.path.dirname

path1 = dir(dir(dir(__file__)))
sys.path.append(path1)


""""from src.utils_.mining_data_tb import *
from src.utils_.folders_tb import *
from src.utils_.create_df import *
from src.utils_.visualization_tb import *""""

import plotly.express as px


path = os.path.dirname(__file__)
df = None

st.set_page_config(layout="wide") 

menu = st.sidebar.selectbox('Menu:',
            options=["Welcome", "Visualization", "Flask", "Model Prediction","SQL", "Conclusions"])


if menu == 'Welcome':
    imagen = Image.open(path1 + os.sep + 'resources' + os.sep + 'alzheimer-enfermedad.jpg')
    st.image (imagen,use_column_width=True) 
    st.title('Alzheimer detection from MRI ( Magnetic resonance imaging )')
    st.write("\n")
    st.markdown()
    st.markdown("#### Alzheimer's disease is the most common type of dementia. It is a progressive disease beginning with mild memory loss and possibly leading to loss of the ability to carry on a conversation and respond to the environment. Alzheimer's disease involves parts of the brain that control thought, memory, and language")

if menu == "Visualization":
    
    #submenu = st.sidebar.selectbox('Menu:',
            #options=["all maps", "gdp per capita", "Poverty %", "total cases", "total deaths", "deaths ratio"])
    st.title('VISUALIZATION')
    st.write("In this section you can observe in the maps the incidence of covid around the world")
    
  

if menu == "Flask":
    r = requests.get("http://localhost:8080/give_me_id?token_id=T79045618").json()
    df = pd.DataFrame(r)
    st.write(df)

if menu == "Model Predictions":
    pass

if menu == "SQL":
    pass

if menu == "Conclusions":
    st.title('CONCLUSIONS')

    st.write("\n")
    st.markdown("### *a. Was it possible to deamostrate the hypothesis? Why?*")
    st.write("The hypothesis has been partly demostrated as we have been working with all data without separating each parameter to achieve the best demostration as the time that we had to do the project was not very long.")
    
    st.write("\n")
    st.markdown("### *b. What can you conclude about your data study?*")
    st.write("If I would have to do another EDA project I would change a lot of things. First of all I would choose a topic in which I have more interest, and then I would use questions as tools to guide the investigation to develop an understanding of the data.")

    st.write("\n")
    st.markdown("### *b. What can you conclude about your data study?*")
    st.write("The hypotesis has been rejected because in the information given by the data we have seen that the death rate in countries where the gdp per capita is very low isn´t higher than the countries where the gdp per capita is very elevated in most of cases.")

    st.write("\n")
    st.markdown("### *c. What would you change if you need to do another EDA project?*")
    st.write("If I would have to do another EDA project I would change a lot of things. First of all I would choose a topic in which I have more interest, and then I would use questions as tools to guide the investigation to develop an understanding of the data.")
    
    st.write("\n")
    st.markdown("### *d. What do you learn doing this project?*")
    st.write("Doing this project I have learnt to calm down and to control the stress and also I have learnt that I have to schedule my time better and priorize somethings over others. \n As to theory I have learnt a lot of things such as detecting errors of my code faster, finding solutions on my own or how to be more effective coding.")
    