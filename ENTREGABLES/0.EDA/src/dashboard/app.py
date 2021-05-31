import re
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import requests
import os

path = os.path.dirname(__file__)
df = None
    
menu = st.sidebar.selectbox('Menu:',
            options=["Welcome", "Visualization", "Flask"])

st.title(' Título de mi DataFrame ')
st.write(' This is a web app to compare the people that have died around the world because of covid ')

if menu == 'Welcome':
    st.title('Welcome!')
    st.write("Hope you´ll enjoy it!")

if menu == "Visualización":
    pass

if menu == "Flask":
    r = requests.get("http://localhost:8080/give_me_id?token_id=T79045618").json()
    df = pd.DataFrame(r)
    st.write(df)
