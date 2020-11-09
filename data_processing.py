import pandas as pd


def load_df(add_death_df, add_confirmed_df, add_recovered_df, add_summary_df):
    # TO DO: Lire les bases de données à partir des liens URL reçus en paramètres
	
    return ...


def summary_add_col(df, col, value):
    # TO DO: Ajouter une colonne à la base de données df reçue en paramètre (deux lignes)
    # le nom et la valeur de cette colonne se trouvent respectivement dans les variables col et value.

    return ...


def summary_extract_col(df, cols):
    # TO DO: Extraire les colonnes reçues en paramètre désirer de la base de données df (une seul ligne)
    return ...


def summary_by_country(df):
    # TO DO: Grouper le DataFrame par Country_Region (une seule ligne). Utiliser la méthode groupby()
    return ...


def creat_dict_df(death_df, confirmed_df, recovered_df):
    # TODO: Créer un dictionnaire avec des bases de données reçues en paramètre (une seule ligne)
    return ...


def dict_remove_col(dict_df, cols):
    # TO DO: Supprimer des colonnes cols du dictionnaire dict_df (une seule ligne) 
    # les colonnes doivent être supprimées de l’ensemble des clés du dictionnaire
    return ...


def dict_by_country(dict_df):
    # TO DO: Grouper le dictionnaire dict_df par Country/Region pour toutes les clés du dictionnaire 
    # et changer les colonnes en datetime, utiliser le lien suivant pour plus d'information
    # https://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.to_datetime.html    

    return ...


def dict_add_key(dict_df):
    # TO DO: Ajouter les clés Active case et Closed Case a votre dictionnaire de DataFrame
    # les cles du dictionnaire doivent être triés comme suit:{"Confirmed", "Deaths", "Active", "Closed", "Recovered"}

    return ...


def dict_by_day(dict_df):
    # TO DO: Grouper le dictionnaire de DataFrame par date (une seule ligne)
    # Utiliser le lien suivant: 
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html
    return ...


def basic_inf_summary(summary_df):
    # TO DO: Afficher les informations suivantes: Somme des nombres de cas confirmé,
    # active, fermée, mort et rétabli dans le monde.

