import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import random

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from datetime import timedelta
import plotly.io as pio


def CreatCountryDataTrain(dict_df, Country):
    #TO DO: création des données d'entrainement,
    #TO DO: Etape 1: creer un DataFrame avec deux colonne "Days Since" et "Date"

    #TO DO: Etape 2: Affecter a la colonne "Days Since"  l'indice de la base de donnee "Confirmed" du Country du dictionnaire dict_df

    #TO DO: Etape 3: convertire le contenue de la colonne "Days Since" en datetime format
    # utiliser le lien suivant: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day.html

    #TO DO: Etape 4: Affecter a la colonne "Date"  l'indice de la base de donnee "Confirmed" du dictionnaire dict_df

    #TO DO: Etape 5: grouper la base de donner creer a l'etape 1 par "Date"

    
    #TO DO: Etape 6: creer ajouter a la base de donner creer a l'etape 1 toutes donnees des cles du dictionnaire dict_df 
    # le nom des colonnes ajouter sera le meme que celui des cles du dictionnaire dict_df 

    
    
    #TO DO: Etape 7: generer de facon aleatoire les donner d'entrainement, qui represente 75% des donnees.
    # utiliser le lien suivant pour plus d'information: https://www.w3schools.com/python/ref_random_choices.asp

    
    # La fonction retourne la base de donnee cree a k'etape 1 ainsi que les donner d'entrainement
    return ...

# Fournie
def train_model(df,data_type):
    lin_reg = LinearRegression(normalize=True)
    svm     = SVR(C=2e6,degree=10, gamma='scale')

    X = np.array(df["Days Since"]).reshape(-1,1)
    y = np.array(df[data_type]).reshape(-1,1)

    lin_reg.fit(X, np.ravel(y))
    svm.fit(X, np.ravel(y))

    lin_reg_predict = lin_reg.predict(X)
    svm_predict = svm.predict(X)
    
    model_df = pd.DataFrame(zip(df.index,lin_reg_predict,svm_predict), columns=["Dates","LR","SVM"])
    dic_model = {"LR":lin_reg,"SVM":svm}
    dic_score = {"LR Train":lin_reg.score(X, y),"SVM Train ":svm.score(X, y)}
    print(dic_score)
    return model_df, dic_model, dic_score


def plotmodel(country_df, model_df):
    color = ["blue","red","green","gray","orange"]
    #TO DO: Creer une figure en utilisant la biblioteque plotly.graph_objects

    #TO DO: Tracer les courbes suivantes sur le meme graphe: l'evolution des cas confirmer et SVM/LR Model 

    
    fig.update_layout(xaxis_tickfont_size=14, yaxis=dict(title='Number of Cases'),
                      legend=dict( yanchor="top", y=0.99, xanchor="left", x=0.01))
    fig.show()
    pio.write_image(fig, 'Image/fig_07.svg', width=1000, height=500)
    
# Fournie
def predictionmodel(country_df, train_df, model_df, dic_model):

    new_date = []
    new_prediction_lr = []
    new_prediction_svm = []

    for i in range(1,50):
        new_date.append(train_df.index[-1] + timedelta(days=i))
        new_prediction_lr.append(int(dic_model["LR"].predict(np.array(country_df["Days Since"].max() + i).reshape(-1,1))))
        new_prediction_svm.append(int(dic_model["SVM"].predict(np.array(country_df["Days Since"].max() + i).reshape(-1,1))))

    model_pred_df = pd.DataFrame(zip(new_date,new_prediction_lr,new_prediction_svm), columns=["Dates","LR","SVM"])   
    return model_pred_df


def plofforcasting(country_df, model_df, model_pred_df):
    color = ["blue","red","green","gray","orange"]
    #TO DO: Creer une figure en utilisant la biblioteque plotly.graph_objects

    #TO DO: Tracer les courbes suivantes sur le meme graphe: l'evolution des cas confirmer, SVM/LR Model et SVM/LR predction  
    
    fig.update_layout(xaxis_tickfont_size=14, yaxis=dict(title='Number of Cases'),
                      legend=dict( yanchor="top", y=0.99, xanchor="left", x=0.01))
    fig.show()
    pio.write_image(fig, 'Image/fig_08.svg', width=1000, height=500)
    
