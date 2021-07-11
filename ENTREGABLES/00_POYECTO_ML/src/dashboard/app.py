# ------------------------------ Import the necessary libraries ------------------------------------

import re
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import requests
import os,sys
import plotly.express as px
import pymysql

# ---------------------------------------------------------------------------------------------------

# Create variables with the path

dir = os.path.dirname
path = os.path.dirname(os.path.abspath(__file__))
path1 = dir(dir(dir(os.path.abspath(__file__))))

# ---------------------------------------------------------------------------------------------------

# Append the path 
sys.path.append(path1)

# ----------------------------------- Import from our folders ---------------------------------------

from src.utils_.dashboard_tb import predict_image
from src.utils_.sql_tb import select_sql, MySQL
from src.utils_.apis_tb import read_json
from src.utils_.visualization_tb import time

# ------------------------------------------ Streamlit ----------------------------------------------

st.set_page_config(layout="wide") 

menu = st.sidebar.selectbox('Menu:',
            options=["Welcome", "Visualization", "Flask", "ML Models","SQL", "Conclusions"])


if menu == 'Welcome':

    imagen = Image.open(path1 + os.sep + 'resources' + os.sep + 'alzheimer-enfermedad.jpg')
    st.image (imagen,use_column_width=True) 
    st.title('Alzheimer detection from MRI ( Magnetic resonance imaging )')
    st.write("\n")
    st.markdown("#### DEFINITION: Alzheimer's disease is the most common type of dementia. It is a progressive disease beginning with mild memory loss and possibly leading to loss of the ability to carry on a conversation and respond to the environment. Alzheimer's disease involves parts of the brain that control thought, memory, and language")

if menu == "Visualization":
    
    st.title('VISUALIZATION')
    st.write(" In this section we can observe some graphics with the comparasion of the accuracy and the loss of each model we've trained ")
    
    checkbox_cnn = st.sidebar.checkbox("CNN", value=True)
    checkbox_vgg16 = st.sidebar.checkbox("VGG16", value=True)
    checkbox_resnet50 = st.sidebar.checkbox("ResNet50bv2", value=True)
    checkbox_resnet150 = st.sidebar.checkbox("ResNet152v2", value=True)

    if checkbox_cnn: 
        st.write("CNN")
        imagen = Image.open(path1 + os.sep + 'resources' + os.sep + 'cnn.png')
        st.image (imagen,use_column_width=True) 

    if checkbox_vgg16:
        st.write("VGG16")
        imagen = Image.open(path1 + os.sep + 'resources' + os.sep + 'vgg16.png')
        st.image (imagen,use_column_width=True) 

    if checkbox_resnet50:
        st.write("ResNet50V2")
        imagen = Image.open(path1 + os.sep + 'resources' + os.sep + 'res_hist.png')
        st.image (imagen,use_column_width=True) 
    
    if checkbox_resnet150:
        st.write("ResNet152v2")
        imagen = Image.open(path1 + os.sep + 'resources' + os.sep + 'resnet152.png')
        st.image (imagen,use_column_width=True) 


if menu == "Flask":

    st.title('DATAFRAME WITH THE INFORMATION OF OUR DATASET')
    st.write("\n")
    r = requests.get("http://localhost:8080/give_me_id?token_id=T79045618").json() # Load our API 
    df = pd.DataFrame(r)
    st.write(df)

if menu == "ML Models":

    st.title('MACHINE LEARNING MODELS')
    st.write("PREDICTION WITH THE BEST MODEL: CNN WITH VGG16")

    col1, col2 = st.beta_columns([2, 4])
    new_df_path = None

    with col1: 
        new_df_path = st.text_input('Image file path or url')
        uploaded_file = st.file_uploader("Choose an image:", type="jpg")
        if new_df_path:
            graph_slider_1 = None
            st.text(str(new_df_path))

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            st.write("")
            st.write("Classifying...")
            st.write("PREDICTION:")
            st.write("")
            st.write("0: 'MildDemented'")
            st.write("1: 'ModerateDemented'")
            st.write("2: 'NonDemented'")
            st.write("3: 'VeryMildDemented'")
            preds = predict_image(path1 + os.sep + "models" + os.sep + "vv16_1.h5", new_df_path)
            st.write(preds)
            names = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
            st.write("")
            st.write("Max probability: ", names[preds.argmax()])


if menu == "SQL":

    st.title('MACHINE LEARNING MODELS COMPARASION FROM SQL')

    settings_file = path1 + os.sep + "src" + os.sep + "utils_" + os.sep + "bd_info.json"
    json_readed = read_json(settings_file)
    df = select_sql(json_readed, MySQL, "model_comparasion")
    st.write(df)
    

if menu == "Conclusions":
    st.title('CONCLUSIONS')

    st.write("\n")
    st.markdown("### *a. What can you conclude about your data study?*")
    st.write("Our dataset is not maybe the best dataset to this classification. The model with the best accuracy has been a CNN pretrained netrwork: VGG16.")

    st.write("AD is the most common of many causes of dementia, and its prevalence is increasing worldwide. Disease pathology starts years before noticeable symptoms. Neuropsychological, imaging, and spinal fluid tests can establish the diagnosis with high accuracy. Although there are currently no treatments that slow the disease process, management of the cognitive and behavioral symptoms of AD dementia can significantly improve the lives of patients and their caregivers.")
    st.write("AD pathology consists of β-amyloid plaques and phospho-tau neurofibrillary tangles.")
    st.write("AD pathology can be present in asymptomatic, mildly affected (MCI), or demented individuals.")
    st.write("Although advanced age and genetics are the predominant risk factors, several preventable risk factors also contribute to the likelihood of developing AD dementia.")
    st.write("There is no perfect diagnostic test for AD, but neuropsychological testing, neuroimaging, and CSF analysis can substantially increase diagnostic accuracy.")
    st.write("There is no cure for AD. Ideal AD management includes a combination of symptomatic treatment for cognitive issues, detection and judicious control of behavioral issues, and caregiver support.")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.markdown("### *INFORMATION ABOUT THE TIME SPENT IN EACH SECTION*")
    st.write("\n")
    st.write("\n")
    imagen = Image.open(path1 + os.sep + 'resources' + os.sep + 'timespent.png')
    st.image (imagen,use_column_width=False) 
    