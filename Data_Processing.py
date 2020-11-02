import pandas as pd

def Load_df(add_death_df, add_confirmed_df, add_recovered_df, add_summury_df):
    #TO DO: Lire les base de donnees a partir des adresse recu en parametre
    
    return ...

def summuryaddcol(df, col, value):
    #TO DO: Ajouter une colonne au DataFrame. val represente le nom de la colonne et value les valeur de la colonne
    
    return ...

def summuryextractcol(df, cols):
    #TO DO: extraire les colomnes desirer de la base de donnee
    return ...

def summurybycountry(df):
    #TO DO: grouper le DataFrame par Country_Region
    return ...

def creatdictdf(death_df,confirmed_df,recovered_df):
    #TODO: creer un disctionnaire de base de donnees
    return ...

def dictdfremovecol(dict_df, cols):
    #TO DO: Supprimer une colonne de votre dictionnaire de DataFrame
    return ...

def dictdfbycountry(dict_df):
    #TO DO: grouper le dictionnaire de DataFrame par Country/Region et changer les colonnes en datetime 
    
    
    
    return ...

def dictdfaddkey(dict_df): 
    #TO DO: Ajouter les cles Active case et Closed Case a votre dictionnaire de DataFrame et les trier comme suit(Confirmed,Deaths,Active,Closed,Recovered)

    
    
    
    return ...

def dictdfbyday(dict_df):
    #TO DO: grouper le dictionnaire de DataFrame par date
    return ...

def basicinfsummury(summury_df):
    #TO DO: Afficher les information suivante: Somme des nombres de cas confirmée, active, fermée, mort et rétabli dans le monde.
   




