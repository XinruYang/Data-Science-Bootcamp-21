# ------------------------------ Import the necessary libraries ------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import requests
import os,sys
import cv2
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.resnet_v2 import ResNet50V2, decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint, Callback  
from tensorflow.keras.preprocessing.image import ImageDataGenerator ,img_to_array

# ---------------------------------------------------------------------------------------------------

# Create variables for the path

dir = os.path.dirname
path = os.path.abspath(__file__)

path1 = dir(os.path.abspath(__file__))
sys.path.append(path1)

# ---------------------------------------------------------------------------------------------------

def predict_image(path_to_model, route):
    new_model = keras.models.load_model(path_to_model)
    image = cv2.imread(route, flags=cv2.IMREAD_COLOR)
    smallimage = cv2.resize(image, (180, 180))
    pred = new_model.predict(preprocess_input(np.array(smallimage).reshape(1, 180, 180, 3)))
    return pred

