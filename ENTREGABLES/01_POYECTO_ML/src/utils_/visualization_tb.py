# ------ Import the necessary libraries ------

from cv2 import data
import pandas as pd 
import numpy as np 
from sklearn.datasets import load_iris, load_boston
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px

# --------------------------------------------------------------------------------------

# PIE PLOT

def to_percent(x, suma=5120):
    return x/suma * 100 

def pie_plot(x, y,w, z, title): # title = "Data count in each folder"
    pie, ax = plt.subplots(figsize=[10,6])
    labels = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
    data = [ x, y, w, z]
    colors = ['mediumblue', 'lightskyblue', 'lightcoral', "violet"]
    plt.pie(x=data, autopct='%1.2f%%', labels=labels, pctdistance=0.5, colors=colors)
    plt.title(title, fontsize=14)

# --------------------------------------------------------------------------------------

# SHOW THE IMAGES WITH THE LABELS

def show_train(train):
    plt.figure(figsize=(20, 10))
    for images, labels in train.take(1):
        for i in range(25):
            ax = plt.subplot(5, 5, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(train.class_names[labels[i]])
            plt.axis("off")






