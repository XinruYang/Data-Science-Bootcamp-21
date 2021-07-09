# ------------------------------ Import the necessary libraries ------------------------------------

import pandas as pd 
from sklearn.datasets import load_iris, load_boston
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import sys, os
from keras.preprocessing.image import ImageDataGenerator

# ---------------------------------------------------------------------------------------------------

# Create a variable

dir = os.path.dirname

# ---------------------------------------------------------------------------------------------------

def data_generator(X_train, folder, length ):
    
    datagen  = ImageDataGenerator(
        rotation_range=180,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        fill_mode='nearest',
        brightness_range=[0.2,2.0])

    i = 0
    for batch in datagen.flow(X_train, batch_size=1,
                                    save_to_dir= dir(dir(dir((os.path.abspath(__file__))))) + os.sep + "data" + os.sep + "train" + os.sep + folder , save_format='jpg'):
        i += 1
        if i > 3000 - length:
            break


