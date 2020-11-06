import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


def summury_analyse_data(df):
    # TO DO: plot the 10 countries with the highest number of confirmed, deaths, active, closed, recovered,
    # and mortality rate
    # TO DO: Créer des subfigure de 3 ligne et 2 colonne de dimension 15*15 en utilisant la bibliothèque Seaborn

    # TO DO:  dessiner sur chaque subplot les 10 pays les plus toucher par la Covid_19 selon le nombre de cas confirmés,
    # mort, actif, fermé et rétabli ainsi que le taux de mortalité









    fig.tight_layout(pad=3.0)
    fig.show()


def summury_secteur(df):
    # TO DO: plot le pourcentage mondial des cas confirmés par pays
    # TO DO: dessiner le pourcentage mondial des cas confirmés par pays en utilisant la bibliothèque plotly.express


    fig.update_traces(textposition="inside")
    fig.show()


def countries_bar(df, countries):
    # TO DO: plot pour certains pays le nombre de cas confirmés, mort, actif, fermé et rétabli
    # TO DO: soustraire les données des pays reçus en paramètre

    # TO DO: Retirer la colonne "Mortality_Rate"

    # TO DO: Créer une figure en utilisant la bibliothèque plotly.graph_objects




    fig.update_layout(yaxis=dict(title='Cases', titlefont_size=16, tickfont_size=14), xaxis_tickfont_size=14,
                      barmode='group', bargap=0.15, bargroupgap=0.1, legend=dict(x=0.01, y=0.99),
                      legend_orientation="h")
    fig.show()
	