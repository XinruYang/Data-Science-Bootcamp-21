import re
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import requests
import os,sys

dir = os.path.dirname

path1 = dir(__file__)
sys.path.append(path1)
print("---------------path", sys.path)

from mining_data_tb import *
from folders_tb import *
from create_df import *
from visualization_tb import *

def gdp_map():
    return scatter_geo(covid_groupby, "gdp_per_capita", "total cases", color="total_deaths")


