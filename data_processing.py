import pandas as pd


def load_df(add_death_df, add_confirmed_df, add_recovered_df, add_summary_df):
    # TO DO: Lire les base de données a partir des adresses reçu en paramètres




    return ...


def summary_add_col(df, col, value):
    # TO DO: Ajouter une colonne au DataFrame (deux lignes)

    return ...


def summary_extract_col(df, cols):
    # TO DO: extraire les colonnes désirer de la base de donnée (une seul ligne)
    return ...


def summary_by_country(df):
    # TO DO: grouper le DataFrame par Country_Region (une seul ligne)
    return ...


def creat_dict_df(death_df, confirmed_df, recovered_df):
    # TODO: créer un dictionnaire de base de données (une seul ligne)
    return ...


def dict_remove_col(dict_df, cols):
    # TO DO: Supprimer une colonne de votre dictionnaire de DataFrame (une seul ligne)
    return ...


def dict_by_country(dict_df):
    # TO DO: grouper le dictionnaire de DataFrame par Country/Region et changer les colonnes en datetime



    return ...


def dict_add_key(dict_df):
    # TO DO: Ajouter les clés Active case et Closed Case a votre dictionnaire de DataFrame




    return ...


def dict_by_day(dict_df):
    # TO DO: grouper le dictionnaire de DataFrame par date (une seul ligne)
    return ...


def basic_inf_summary(summary_df):
    # TO DO: Afficher les information suivante: Somme des nombres de cas confirmée,
    # active, fermée, mort et rétabli dans le monde.






