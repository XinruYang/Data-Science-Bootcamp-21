# ------------------------------ Import the necessary libraries ------------------------------------

import os, sys
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd
import cv2 as cv

# ---------------------------------------------------------------------------------------------------

# Create a variable

dir = os.path.dirname

# ---------------------------------------------------------------------------------------------------

# Create df from each folder 

# n = label / folder = folder´s names: "MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"

def img_array(n, train, folder):

    """ Reads a folder and creates a Dataframe with the following columns: ' array of the image' , 
    ' label of the image', the path of the image' and 'the name of the folder' """

    data_path = (dir(dir(dir(os.path.abspath(__file__)))) + os.sep + "data" + os.sep + 
                                                    train + os.sep + folder + os.sep )

    only_image_names = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    dictionary = {}

    df_dict = []

    for image_name in only_image_names:

            image_fullpath = data_path + image_name
            image_cv = cv.imread(image_fullpath) 
            image_cv = cv.resize(image_cv, (180, 180)) 

            if "jpg" in image_name:
                df_dict.append({"Image":image_cv, "Label":n, "Fullpath":image_fullpath, "Folder": folder,
                                                                                     "Size": "180x180" })
                dictionary[image_fullpath] = n

    return pd.DataFrame(df_dict) # Returns the dataframe with the arrays of the images


# ---------------------------------------------------------------------------------------------------

# Concatenate the dfs that we´ve created 

def concat(df1, df2, df3, df4): 

    df = pd.concat([df1, df2, df3, df4])
    return df

# ---------------------------------------------------------------------------------------------------


