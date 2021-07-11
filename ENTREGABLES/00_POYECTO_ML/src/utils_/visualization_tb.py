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

# To plot the data contained in each folder

def pie_plot(x, y,w, z, title): # title = "Data count in each folder"
    
    pie, ax = plt.subplots(figsize=[10,6])
    labels = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
    data = [ x, y, w, z]
    colors = ['mediumblue', 'lightskyblue', 'lightcoral', "violet"]
    plt.pie(x=data, autopct='%1.2f%%', labels=labels, pctdistance=0.5, colors=colors)
    plt.title(title, fontsize=14)

# To plot the time I´ve spent in each section

def time(x, y,w, z, v, title): # title = "Data count in each folder"
    
    pie, ax = plt.subplots(figsize=[10,6])
    labels = ["data_searching", "data_mining", "flask", "streamlit", "documentation"]
    data = [ x, y, w, z, v]
    colors = ['Cyan', 'lightskyblue', "Thistle", 'violet', "LemonChiffon"]
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

# --------------------------------------------------------------------------------------

# SHOW THE PREDICTIONS 

def show_pred(n, n1, n2, test, train, preds):  # show_pred(40, 5, 8, x_test, train_ds, preds)
    
    plt.figure(figsize=(20, 10))
    for i in range(n):
        ax = plt.subplot(n1, n2, i + 1)
        plt.imshow(test[i])
        plt.title(train.class_names[np.argmax(preds[i])])
        plt.axis("off")

# --------------------------------------------------------------------------------------

# SHOW THE ACCURACY AND LOSS OF A MODEL

def show_accuracy(f, c, metrics_list, history): # metrics_list = ["acc", "auc", "loss"]
    
    fig, ax = plt.subplots(f, c, figsize = (30, 10))
    ax = ax.ravel()

    for i, metric in enumerate(metrics_list):
        ax[i].plot(history.history[metric])
        ax[i].plot(history.history["val_" + metric])
        ax[i].set_title("Model {}".format(metric))
        ax[i].set_xlabel("Epochs")
        ax[i].set_ylabel(metric)
        ax[i].legend(["train", "val"])






