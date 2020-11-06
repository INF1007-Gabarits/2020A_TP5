import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from datetime import timedelta
import plotly.io as pio

COLOR = ["blue", "red", "green", "gray", "orange"]


def creat_country_data_train(dict_df, country):
    # TO DO: création des données d'entrainement,
    # TO DO: Etape 1: créer un DataFrame avec deux colonne "Days Since" et "Date"

    # TO DO: Etape 2: Affecter a la colonne "Days Since"  l'indice de la base de données "Confirmed" du Country du
    # dictionnaire dict_df

    # TO DO: Etape 3: convertir le contenue de la colonne "Days Since" en datetime format
    # utiliser le lien suivant: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day.html

    # TO DO: Etape 4: Affecter a la colonne "Date"  l'indice de la base de donnee "Confirmed" du dictionnaire dict_df

    # TO DO: Etape 5: grouper la base de donner créer a l'étape 1 par "Date"


    # TO DO: Etape 6: ajouter a la base de donner créer a l'étape 1 toutes les données des clés du dictionnaire dict_df
    # le nom des colonnes ajouter sera le même que celui des clés du dictionnaire dict_df


    # TO DO: Etape 7: générer de façon aléatoire les donner d'entrainement, qui représente 75% des données.
    # utiliser le lien suivant pour plus d'information: https://www.w3schools.com/python/ref_random_choices.asp



    return ...


def train_model(df, data_type):
    lin_reg = LinearRegression(normalize=True)
    svm = SVR(C=2e6, degree=10, gamma='scale')

    x = np.array(df["Days Since"]).reshape(-1, 1)
    y = np.array(df[data_type]).reshape(-1, 1)

    lin_reg.fit(x, np.ravel(y))
    svm.fit(x, np.ravel(y))

    lin_reg_predict = lin_reg.predict(x)
    svm_predict = svm.predict(x)

    model_df = pd.DataFrame(zip(df.index, lin_reg_predict, svm_predict), columns=["Dates", "LR", "SVM"])
    dic_model = {"LR": lin_reg, "SVM": svm}
    dic_score = {"LR Train": lin_reg.score(x, y), "SVM Train ": svm.score(x, y)}
    print(dic_score)
    return model_df, dic_model, dic_score


def plot_model(country_df, model_df):
    # TO DO: Creer une figure en utilisant la biblioteque plotly.graph_objects

    # TO DO: Tracer les courbes suivantes sur le même graphe: l'évolution des cas confirmer et SVM/LR Model






    fig.update_layout(xaxis_tickfont_size=14, yaxis=dict(title='Number of Cases'),
                      legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    fig.show()


def prediction_model(country_df, train_df, dic_model):
    new_date = []
    new_prediction_lr = []
    new_prediction_svm = []

    for i in range(1, 30):
        new_date.append(train_df.index[-1] + timedelta(days=i))
        new_prediction_lr.append(int(dic_model["LR"].predict(np.array(country_df["Days Since"].max()
                                                                      + i).reshape(-1, 1))))
        new_prediction_svm.append(int(dic_model["SVM"].predict(np.array(country_df["Days Since"].max()
                                                                        + i).reshape(-1, 1))))

    model_pred_df = pd.DataFrame(zip(new_date, new_prediction_lr, new_prediction_svm), columns=["Dates", "LR", "SVM"])

    return model_pred_df


def plot_forcasting(country_df, model_df, model_pred_df):
    # TO DO: Créer une figure en utilisant la bibliothèque plotly.graph_objects

    # TO DO: Tracer les courbes suivantes sur le même graphe: l'évolution des cas confirmer,
    # SVM/LR Model et SVM/LR prédiction










    fig.update_layout(xaxis_tickfont_size=14, yaxis=dict(title='Number of Cases'),
                      legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    fig.show()
