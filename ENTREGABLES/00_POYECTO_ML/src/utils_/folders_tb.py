# ------------------------------ Import the necessary libraries ------------------------------------

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.resnet_v2 import ResNet50V2, decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras import datasets, layers, models
from skimage.io import imread
import cv2

import numpy as np
import os, sys
import PIL
import PIL.Image

# ---------------------------------------------------------------------------------------------------

# Read the images from the folders

# subset : "training"/ "validation" 
# batch_size: the size of the training

def read_folder(subset, folder, batch_size=32): 

    """ This function reads the images from the folders: it creates the training and the validation
    set and resizes them to 180x180 """
    if folder == "train" or "new_train":
        batch_size = batch_size
        img_height = 180
        img_width = 180

        data_dir = os.path.dirname(os.getcwd()) + os.sep + "data" + os.sep + folder
        ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset=subset, 
        seed=235,
        image_size=(img_height, img_width),
        batch_size=batch_size)
    
    else:
        batch_size = batch_size
        img_height = 180
        img_width = 180

        data_dir = os.path.dirname(os.getcwd()) + os.sep + "data" + os.sep + folder
        ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    print(ds.class_names)
    
    return ds

# ---------------------------------------------------------------------------------------------------

# This reads the images of a folder

def read_data(path): # dire = os.path.dirname(os.getcwd()) + os.sep + "data" + os.sep + "test" + os.sep + "VeryMildDemented"
    X = []
    for file in os.listdir(path):
        image = cv2.imread(path + '/' + file, flags=cv2.IMREAD_COLOR)
        smallimage = cv2.resize(image, (180, 180))
        
        X.append(smallimage)

    return np.array(X)

# x_test = read_data(dire)

# x_test = preprocess_input(x_test)

# ---------------------------------------------------------------------------------------------------

# This function saves our models in the folder that we choose 

def save_model(model, route):
    model.save(route)

