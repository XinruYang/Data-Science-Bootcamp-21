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

def read_folder(subset, train, batch_size=32): 

    """ This function reads the images from the folders: it creates the training and the validation
    set and resizes them to 180x180 """
    
    batch_size = batch_size
    img_height = 180
    img_width = 180

    data_dir = os.path.dirname(os.getcwd()) + os.sep + "data" + os.sep + train
    ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset=subset, 
    seed=235,
    image_size=(img_height, img_width),
    batch_size=batch_size)

    print(ds.class_names)
    
    return ds
