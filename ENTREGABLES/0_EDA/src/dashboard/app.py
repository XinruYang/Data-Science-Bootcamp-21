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
            options=["Welcome", "Maps", "Graphics", "Flask", "Conclusions"])


if menu == 'Welcome':
    st.title('COVID - 19 DEATH TOLL VS. POVERTY: DETAILED ANALISYS')
    st.write("\n")
    st.markdown("#### ")

if menu == "Maps":
    
    #submenu = st.sidebar.selectbox('Menu:',
            #options=["all maps", "gdp per capita", "Poverty %", "total cases", "total deaths", "deaths ratio"])

    st.title('MAPS')
    st.write("In this section you can observe in the maps the incidence of covid around the world")
    
    #if submenu == "all maps":
    checkbox_gdp = st.sidebar.checkbox("GDP per capita", value=True)
    checkbox_poverty = st.sidebar.checkbox("Poverty %", value=True)
    checkbox_cases = st.sidebar.checkbox("Total cases", value=True)
    checkbox_deaths = st.sidebar.checkbox("Total deaths", value=True)
    checkbox_deaths_ratio = st.sidebar.checkbox("Deaths ratio", value=True)

    if checkbox_gdp:
        st.plotly_chart(scatter_geo(covid_groupby, "gdp_per_capita", "gdp per capita", 
        color="gdp_per_capita", size_max=15), use_container_width=True )

    if checkbox_poverty:
        st.plotly_chart(scatter_geo(covid_groupby, "Poverty %", "Poverty ratio",
         color="Poverty %"),  use_container_width=True )
    
    if checkbox_cases:
        st.plotly_chart(scatter_geo(covid_groupby, "total_cases", "total cases", 
        color="total_cases") , use_container_width=True)
    
    if checkbox_deaths:
        st.plotly_chart(scatter_geo(covid_groupby, "total_deaths", "total deaths",
            color="total_deaths"), use_container_width=True)

    if checkbox_deaths_ratio:
        st.plotly_chart(scatter_geo(covid_groupby, "deaths_ratio", "deaths ratio",
            color="deaths_ratio"), use_container_width=True)

if menu == "Graphics":

    st.title('GRAPHICS')
    st.write("\n")
    st.markdown(" ### In this section it can be observed different graphs that will allow us to contrast different parameters ")
    st.write("\n")

    submenu = st.sidebar.selectbox('Menu:',
            options=["Boxplot", "Barplot", "Scatterplot", "Heatmap"])

    if submenu == "Boxplot":

        st.title('Box Plot')
        st.write("\n")


        checkbox_gdp = st.sidebar.checkbox("GDP per capita", value=True)
        checkbox_poverty = st.sidebar.checkbox("Poverty %", value=True)
        checkbox_deaths_ratio = st.sidebar.checkbox("Deaths ratio", value=True)

        if checkbox_gdp:
            imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "boxplot" + os.sep + 'box_gdp_per_capita.png')
            st.image (imagen,use_column_width=True) 

        if checkbox_poverty:
            imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "boxplot" + os.sep + 'boxplot_poverty.png')
            st.image (imagen,use_column_width=True) 

        if checkbox_deaths_ratio:
            imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "boxplot" + os.sep + 'boxplot_deaths_plot.png')
            st.image (imagen,use_column_width=True) 

    if submenu == "Barplot":

        st.title('Bar Plot')
        st.write("\n")

        lilmenu = st.sidebar.selectbox('Menu:',
            options=["World", "Per Continent"])

        if lilmenu == "World":
            imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "barplot" + os.sep + '8_world.png')
            st.image (imagen,use_column_width=True)

        if lilmenu == "Per Continent":
            checkbox_europe = st.sidebar.checkbox("EUROPE", value=True)
            checkbox_africa = st.sidebar.checkbox("AFRICA")
            checkbox_asia = st.sidebar.checkbox("ASIA")
            checkbox_north_america = st.sidebar.checkbox("NORTH AMERICA")
            checkbox_south_america = st.sidebar.checkbox("SOUTH AMERICA")
            checkbox_oceania = st.sidebar.checkbox("OCEANIA")
    
            if checkbox_europe:
                imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "barplot" + os.sep + '8_europe.png')
                st.image (imagen,use_column_width=True)

            if checkbox_africa:
                imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "barplot" + os.sep + '8_africa.png')
                st.image (imagen,use_column_width=True)
            
            if checkbox_asia:
                imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "barplot" + os.sep + '8_asia.png')
                st.image (imagen,use_column_width=True)
            
            if checkbox_north_america:
                imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "barplot" + os.sep + '8_north_america.png')
                st.image (imagen,use_column_width=True)

            if checkbox_south_america:
                imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "barplot" + os.sep + '8_south_america.png')
                st.image (imagen,use_column_width=True)

            if checkbox_oceania:
                imagen = Image.open(path1 + os.sep + 'resources' + os.sep + "barplot" + os.sep + '8_oceania.png')
                st.image (imagen,use_column_width=True)
                

    if submenu == "Scatterplot":

        st.title('Scatter Plot')
        st.write("\n")

        st.plotly_chart(scatter(covid_groupby,"gdp_per_capita" , "risky_age", "deaths_ratio", 
        "deaths_ratio by gdp and risky age"), use_container_width=True)

        st.plotly_chart(scatter(covid_groupby,"Poverty %" , "risky_age", "deaths_ratio",
         "deaths_ratio by poverty and risky age"), use_container_width=True)

        st.plotly_chart(scatter(covid_groupby,"gdp_per_capita" , "hospital_beds_per_thousand",
         "deaths_ratio", "deaths_ratio by poverty and risky age"), use_container_width=True)
    
    if submenu == "Heatmap":
        imagen_heat = Image.open(path1 + os.sep + 'resources' + os.sep + "heatmap" + os.sep + 'heatmap.png')
        st.image (imagen_heat,use_column_width=True) 
  

if menu == "Flask":
    r = requests.get("http://localhost:8080/give_me_id?token_id=T79045618").json()
    df = pd.DataFrame(r)
    st.write(df)

if menu == "Conclusions":
    st.title('CONCLUSIONS')

