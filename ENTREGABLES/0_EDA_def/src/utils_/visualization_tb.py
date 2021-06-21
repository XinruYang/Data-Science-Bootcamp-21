# ------ Import the necessary libraries ------

import pandas as pd 
import numpy as np 
from sklearn.datasets import load_iris, load_boston
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px

# --------------------------------------------------------------------------------------

# HEATMAP

# Visualize heatmap of correlations
def visualization_heatmap(df):
    fig = plt.figure(figsize=(15,10))
    sns.heatmap(df.corr(), annot=True)


# visualization_heatmap(gdp_mundo_sorted)


# --------------------------------------------------------------------------------------

# BAR PLOTS

# Visualize in two plots
def subplot_bar(x1, x2, y, data, title1, title2, size1, size2):

    fig = plt.figure(figsize=(size1,size2))

    plt.subplot(2,2,1) #filas, columnas, a cual de los dos lienzos quiero acceder
    sns.barplot(x=x1, y=y, data=data, color="b", alpha=0.6, label=x1).set(title=title1)
    plt.legend()

    plt.subplot(2,2,2) #filas, columnas, a cual de los dos lienzos quiero acceder
    sns.barplot(x=x2, y=y, data=data, color="m", alpha=0.6, label=x2).set(title=title2, ylabel=None, yticklabels=[])
    plt.legend()
    plt.subplots_adjust(wspace=0.02, hspace=0)


# Visualize in four plots, 2 of each row
def visualizacion_cuatro(data, suptitle, x1, x2, y, t1, t2, t3, t4, n):

    fig, axes = plt.subplots(2, 2, figsize=(20,20))
    fig.suptitle(suptitle)

    sns.barplot(ax=axes[0, 0], data=data.head(n), x=x1, y=y, color="b", alpha=0.5).set(xlabel=None)

    sns.barplot(ax=axes[0, 1], data=data.head(n), x=x2, y=y, color="m", alpha=0.5).set(xlabel=None, ylabel=None, yticklabels=[])

    sns.barplot(ax=axes[1, 0], data=data.tail(n), x=x1, y=y, color="b", alpha=0.5, label=x1)

    sns.barplot(ax=axes[1, 1], data=data.tail(n), x=x2, y=y, color="m", alpha=0.5, label=x2).set(ylabel=None, yticklabels=[])
    plt.legend()

    axes[0, 0].set_title(t1)
    axes[0, 1].set_title(t2)
    axes[1, 0].set_title(t3)
    axes[1, 1].set_title(t4)
    plt.subplots_adjust(wspace=0.02, hspace=0.1)


# Visualize in eight graphs, 4 for each row
def visualizacion_eight(data, suptitle, x1, x2, x3, x4, y, t1, t2, t3, t4, t5, t6,t7, t8, n, size1, size2):

    fig, axes = plt.subplots(2, 4, figsize=(size1,size2))
    fig.suptitle(suptitle)

    sns.barplot(ax=axes[0, 0], data=data.head(n), x=x1, y=y, color="b", alpha=0.5).set(xlabel=None)

    sns.barplot(ax=axes[0, 1], data=data.head(n), x=x2, y=y, color="m", alpha=0.5).set(xlabel=None, ylabel=None, yticklabels=[])

    sns.barplot(ax=axes[0, 2], data=data.head(n), x=x3, y=y, color="g", alpha=0.5).set(xlabel=None, ylabel=None, yticklabels=[])

    sns.barplot(ax=axes[0, 3], data=data.head(n), x=x4, y=y, color="c", alpha=0.5).set(xlabel=None, ylabel=None, yticklabels=[])

    sns.barplot(ax=axes[1, 0], data=data.tail(n), x=x1, y=y, color="b", alpha=0.5, label=x1)

    sns.barplot(ax=axes[1, 1], data=data.tail(n), x=x2, y=y, color="m", alpha=0.5, label=x2).set(ylabel=None, yticklabels=[])

    sns.barplot(ax=axes[1, 2], data=data.tail(n), x=x3, y=y, color="g", alpha=0.5, label=x3).set(xlabel=None, ylabel=None, yticklabels=[])

    sns.barplot(ax=axes[1, 3], data=data.tail(n), x=x4, y=y, color="c", alpha=0.5, label=x4).set(xlabel=None, ylabel=None, yticklabels=[])
    plt.legend()

    axes[0, 0].set_title(t1)
    axes[0, 1].set_title(t2)
    axes[0, 2].set_title(t3)
    axes[0, 3].set_title(t4)
    axes[1, 0].set_title(t5)
    axes[1, 1].set_title(t6)
    axes[1, 2].set_title(t7)
    axes[1, 3].set_title(t8)
    plt.subplots_adjust(wspace=0.02, hspace=0.1)


# --------------------------------------------------------------------------------------

# SCATTER GEO 

def scatter_geo(df, size, name, color, size_max=None,a_f=None): 
    fig = px.scatter_geo(df, locations="country", locationmode="country names", color=color, 
    size=size, # size of markers (one of the columns)
    title=(f'Map of {name}'), size_max=size_max, animation_frame=a_f)
    import plotly.io as pio
    pio.renderers.default = 'notebook'
    
    return fig

# --------------------------------------------------------------------------------------

# SCATTER GRAPH

def scatter(df, x, y, size, title, color="continent", n=40 ):
    fig = px.scatter(df, x=x, y=y, size=size, color=color,
            hover_name="country",log_x=True, size_max=n, title=title)

    return fig

# --------------------------------------------------------------------------------------

# BOX PLOT

def boxplot(x,y,df, title): 
    fig = plt.figure(figsize=(20,10))
    sns.boxplot(x=x, y=y, data=df).set_title(title, fontsize=20)

# -------------------------------------------------------------------------------------

# HISTOGRAM

def tendencias(df):
    df.hist(figsize=(20, 20), bins=5, color="c", edgecolor="k")
    plt.show()

# -------------------------------------------------------------------------------------

# PIE PLOT

def working_time():
    a = pd.DataFrame({'Find Data': np.arange(4)})
    b = pd.DataFrame({'Data Wragling and Data Mining':np.arange(20)})
    c = pd.DataFrame({'Checking Errors':np.arange(15)})
    d = pd.DataFrame({'Visualization': np.arange(25)})
    e = pd.DataFrame({'Streamlit':np.arange(15)})
    f = pd.DataFrame({'Documentation':np.arange(5)})
    g = pd.DataFrame({'Flask': np.arange(1)})
    h = pd.DataFrame({'Data Structuring':np.arange(15)})

    tiempo = pd.concat([a,b,c,d,e,f,g,h])
    tiempo = tiempo.count().sort_values(ascending=False)
    plt.figure(figsize=(8,8))

    sns.set()

    count_list = list(tiempo.values)
    labels = list(tiempo.index)
    plt.pie(count_list, labels=labels, autopct='%1.0f%%', explode= (0.02, 0.02,0.02, 0.02,0.02, 0.02, 0.02, 0.02,))


