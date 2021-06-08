

import pandas as pd 
from sklearn.datasets import load_iris, load_boston
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import dtale
import sys, os

dir = os.path.dirname

def lectura_data_inicial():
    # Leemos el DataFrame sobre el que vamos a trabajar
    # covid = pd.read_csv(""../)
    covid = pd.read_csv(dir(dir(dir(__file__))) + os.sep + "data" + os.sep + "owid-covid-data.csv")

    # Cambiamos el formato de la columna data a datetime
    covid['date'] = pd.to_datetime(covid['date'], format='%Y-%m-%d')

    # Renombramos la columna "location" y la llamamos "country" y "human_development_index": "HDI"
    covid.rename(columns={"location": "country", "human_development_index": "HDI"}, inplace=True)
    
    return covid

covid = lectura_data_inicial()

def filtrar_tabla():
    # Creamos un DataFrame con las columnas que queremos
    covid_data = covid.filter(["date", "continent", "country", "median_age", "aged_65_older", "aged_70_older", "total_cases", "total_deaths", "hospital_beds_per_thousand", "gdp_per_capita", "HDI"], axis=1)

    covid_data["deaths_ratio"] = covid_data["total_deaths"]/covid_data["total_cases"] * 100
    covid_data["non_risky_age"] = 100 - covid_data["aged_65_older"] - covid_data["aged_70_older"]
    covid_data["risky_age"] = 100 - covid_data["non_risky_age"]

    # Eliminamos los valores Nan y reseteamos el índice
    covid_data.dropna(inplace=True)
    covid_data.reset_index(drop=True, inplace=True)
    return covid_data

covid_data = filtrar_tabla()

# Function to read and change the df
def lectura_data_pobreza(): 

    # Read csv --> df
    # pobreza = pd.read_csv("../data/Pobreza.csv", sep=";")

    pobreza = pd.read_csv(dir(dir(dir(__file__))) + os.sep + "data" + os.sep + "Pobreza.csv", sep=";")

    # Split the icon from the values in column "country"
    pobreza["Country"] = pobreza["Country"].apply(lambda x: x[1:])
    pobreza.rename(columns={"2008-2021":"Poverty %"}, inplace=True)
    pobreza.drop("HDI Rank", axis=1, inplace=True)

    return pobreza

pobreza = lectura_data_pobreza()


def change_name(row_in,new_name):
    pobreza.loc[[row_in], ["Country"]] = new_name
    return pobreza

change_name(149, "Vietnam")
change_name(136, "Timor")
change_name(134, "Tanzania")
change_name(114, "Russia")
change_name(90, "Moldova")

countries = list(covid_data["country"])
dict_pobreza = dict(pobreza.values)
countries_pobreza = list(pobreza["Country"])


lista = []
for elem in countries: 
    if elem in countries_pobreza:
        lista.append(elem)
    else:
        lista.append(0)

def list_poverty():
    lista_poverty = [dict_pobreza.get(item,item)  for item in lista]
    return lista_poverty

lista_poverty = list_poverty()

covid_data["Poverty %"] = lista_poverty

