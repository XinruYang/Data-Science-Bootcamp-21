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


from src.utils_.mining_data_tb import *
from src.utils_.folders_tb import *
from src.utils_.create_df import *
from src.utils_.visualization_tb import *

import plotly.express as px

covid_groupby = pd.read_csv(path1 + os.sep + "data" + os.sep + "covid_groupby.csv")

path = os.path.dirname(__file__)
df = None

st.set_page_config(layout="wide") 

menu = st.sidebar.selectbox('Menu:',
            options=["Welcome", "Maps", "Visualization", "Flask"])


st.title(' Título de mi DataFrame ')
st.write(' This is a web app to compare the people that have died around the world because of covid ')

if menu == 'Welcome':
    st.title('Welcome!')
    st.write("Hope you´ll enjoy it!")

if menu == "Maps":
    """st.table(covid_groupby)
    import os 
    covid_groupby.to_excel(os.path.dirname(__file__) + "Xinrupicopuerta.xlsx")"""

    """"fig = px.scatter_geo(covid_groupby, locations="country", locationmode="country names",
    color="total_deaths", title="total cases", size="gdp_per_capita")
    st.write(fig)"""

    """
    fig = px.scatter_geo(covid_groupby, locations=["country"], locationmode=["country names"], 
    color=["total_deaths"],  size=["gdp_per_capita"], title="total cases")
    """
    
    st.plotly_chart(scatter_geo(df=covid_groupby, size="gdp_per_capita", 
    name="total cases", color="total_deaths"), use_container_width=True)
    
    col1, col2 = st.beta_columns(2)
    with col1: 
        st.plotly_chart(scatter_geo(covid_groupby, "total_deaths", "total deaths", color="total_deaths"), use_container_width=True)    
    with col2:
        st.plotly_chart(scatter_geo(covid_groupby, "deaths_ratio", "deaths ratio", color="deaths_ratio"), use_container_width=True) 
    
    col1, col2 = st.beta_columns(2)
    with col1: 
        st.plotly_chart(scatter_geo(covid_groupby, "total_cases", "total cases", color="total_deaths"), use_container_width=True)    
    with col2:
        st.plotly_chart(scatter_geo(covid_groupby, "Poverty %", "Poverty ratio", color="Poverty %") , use_container_width=True) 
    

if menu == "Visualization":

    st.plotly_chart(boxplot("continent","gdp_per_capita",covid_groupby, "gdp per capita by continent"))
    pass

if menu == "Flask":
    r = requests.get("http://localhost:8080/give_me_id?token_id=T79045618").json()
    df = pd.DataFrame(r)
    st.write(df)
