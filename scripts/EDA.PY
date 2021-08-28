# File operation
import os
import numpy as np
import pandas as pd
import logging
import missingno as msno
import scipy.stats as stats

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from IPython.display import Image
import plotly.io as pio

# Preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, plot_confusion_matrix
from sklearn.preprocessing import LabelEncoder

import warnings
pio.renderers
pio.renderers.default = "svg"

logger = logging.getLogger()
def read_data(data_path):
    
    '''this function read a csv file that we will be used in this project,
    and it takes one variable which is the location or file path to where the file is located'''
    
    try:
        logger.debug(" !!! reading the file !!!!! \n")
        data = pd.read_csv(data_path)
        
    except FileNotFoundError:
        print(" !!! Error File Not Found  !!!!! \n")
        logger.error(" !!! Error Program Failed !!!!! \n")
    
    except Exception as e:
        print(" !!! An exception occurred Error: {} ".format(e.__class__))
        logger.error(" !!! An exception occurred Error: {} ".format(e.__class__))
        
    return data

# how many missing values exist or better still what is the % of missing values in the dataset?
def percent_missing(df):
    try:

        # Calculate total number of cells in dataframe
        logger.debug(" !!! Calculate total number of cells in dataframe !!!!! \n")
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        logger.debug(" !!! Count number of missing values per column!!!!! \n")
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        logger.debug(" !!! Calculate total number of missing values !!!!! \n")
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        
        print("The Breast cancer dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")
        logger.info(" all nones from The Breast cancer dataset")
    except Exception as e:
        print("!!! An exception occurred Error: {} ".format(e.__class__))
        logger.error(" !!! An exception occurred Error: {} ".format(e.__class__))



def heat(data, color, size):#function to plot heatmaps

    ''' data: dataframe
    color: color of the graph
    size: size of the graph or figure
     '''
     
    try:
    
        corr = data.corr()
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(corr)] = True

        plt.figure(figsize=size)
        sns.heatmap(corr, mask=mask, annot=True, cmap=color)
        logger.debug(" !!! plotting the graph !!!!! \n")
        plt.show()
    except Exception as e:
            print("!!! An exception occurred Error: {} ".format(e.__class__))
            logger.error(" !!! An exception occurred Error: {} ".format(e.__class__))



def scatter_columns(feature1, feature2, df,title):
    '''function to plot the relatioship among 2 features
    takes dataset and two features to be plotted as arguments and returns a scatter plot '''
    try:
        
        fig = go.Figure()
        fig.update_layout(
            title=title,
            width=600,
            height=400,
            margin=dict(
                        l=20,
                        r=20,
                        t=40,
                        b=20,
                    )
        )

        fig.add_trace(go.Scatter(x=df[feature1+"_"+fields[0]], 
                                 y=df[feature2+"_"+fields[0]], 
                                 mode="markers", 
                                 name="mean",
                                 ))
        fig.add_trace(go.Scatter(x=df[feature1+"_"+fields[1]], 
                                 y=df[feature2+"_"+fields[1]], 
                                 mode="markers", 
                                 name="se",
                                 ))

        fig.add_trace(go.Scatter(x=df[feature1+"_"+fields[2]], 
                                 y=df[feature2+"_"+fields[2]], 
                                 mode="markers", 
                                 name="worst",
                                 ))
        
        logger.info(" !!! plotting scatter plot of: {} ".format(title))  
        
        Image(pio.to_image(fig, format='png', width=1200))
        pio.show(fig)
#         fig.show()
        
        
    except Exception as e:
#         print("!!! An exception occurred Error: {} ".format(e.__class__))
        logger.error(" !!! An exception occurred Error: {} ".format(e.__class__))
        
    

def remove_outlier(df_in, col_name):
    '''arg: dataframe, dataframe_column
    return: dataframe with no outliers'''
    
    try:
        logger.debug(" !!! calculating the first quantile of the column!!!!! \n")
        q1 = df_in[col_name].quantile(0.25) #calculating the first quantile of the column
        logger.debug(" !!! calculating the third quantile of the column!!!!! \n")
        q3 = df_in[col_name].quantile(0.75) #calculating the third quantile of the column
        logger.debug(" !!! finding Interquartile range!!!!! \n")
        iqr = q3-q1 #Interquartile range
        lower_bound  = q1-1.5*iqr
        upper_bound = q3+1.5*iqr
        
    
        logger.debug(" !!! creating the cleanded dataset with no outliers!!!!! \n")
        df_out = df_in.loc[(df_in[col_name] > lower_bound) & (df_in[col_name] < upper_bound)]
         
    except Exception as e:
        print(" !!! An exception occurred Error: {} ".format(e.__class__))
        logger.error(" !!! An exception occurred Error: {} ".format(e.__class__))
    
    return df_out 


#if (__name__== '__main__'):
    
    #
    