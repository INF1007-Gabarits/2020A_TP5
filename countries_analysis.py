import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import plotly.graph_objects as go
import PIL 
import io
import plotly.io as pio

COLOR = ["blue", "red", "green", "gray", "orange"]


def world_map(dict_df, case_type, word_pic):
    world = gpd.read_file(word_pic)

    world.replace("Brunei Darussalam", "Brunei", inplace=True)
    world.replace("Cape Verde", "Cabo Verde", inplace=True)
    world.replace("Congo", "Congo (Brazzaville)", inplace=True)
    world.replace("Democratic Republic of the Congo", "Congo (Kinshasa)", inplace=True)
    world.replace("Czech Republic", "Czechia", inplace=True)
    world.replace("Swaziland", "Eswatini", inplace=True)
    world.replace("Iran (Islamic Republic of)", "Iran", inplace=True)
    world.replace("Korea, Republic of", "Korea, South", inplace=True)
    world.replace("Libyan Arab Jamahiriya", "Libya", inplace=True)
    world.replace("Republic of Moldova", "Moldova", inplace=True)
    world.replace("Syrian Arab Republic", "Syria", inplace=True)
    world.replace("Taiwan", "Taiwan*", inplace=True)
    world.replace("United States", "US", inplace=True)
    world.replace("United Republic of Tanzania", "Tanzania", inplace=True)
    world.replace("The former Yugoslav Republic of Macedonia", "North Macedonia", inplace=True)
    world.replace("Lao People's Democratic Republic", "Laos", inplace=True)
    world.replace("Palestine", "West Bank and Gaza", inplace=True)
    world.replace("Holy See (Vatican City)", "Holy See", inplace=True)
    world.replace("Viet Nam", "Vietnam", inplace=True)

    merge = world.join(dict_df[case_type], on="NAME", how="right")
    image_frame = []

    for dates in merge.columns.to_list()[2:10]:
        ax = merge.plot(column=dates, cmap="OrRd", figsize=(15, 5), scheme="user_defined",
                        classification_kwds={"bins": [10, 100, 1000, 10000, 100000, 1000000, 10000000]},
                        legend=True, edgecolor="black", linewidth=0.6)
        ax.set_title(f"Total {case_type} Covid19 Cases:   {dates}", fontdict={"fontsize": 20}, pad=12.5)
        ax.set_axis_off()
        ax.get_legend().set_bbox_to_anchor((0.18, 0.6))

        img = ax.get_figure()

        plt.close()
        f = io.BytesIO()
        img.savefig(f, format="png")
        f.seek(0)
        image_frame.append(PIL.Image.open(f))

    image_frame[0].save("Image/" + case_type + ".gif", format="GIF", append_images=image_frame[1:],
                        save_all=True, duration=4, loop=0)


def world_cases(dict_df):
    # TO DO: visualiser l’évolution du nombre cumulé des cas confirmés, rétablis, morts, actif et fermé dans le monde.
    # TO DO: Créer une figure en utilisant la bibliothèque plotly.graph_objects

    # TO DO: Pour chacune des clés du dictionnaire dict_df visualiser l’évolution du nombre cumulé



    fig.update_layout(title='Worldwide COVID-19 Cases', xaxis_tickfont_size=14, yaxis=dict(title='Number of Cases'),
                      legend=dict(y=0.99, x=0.01), legend_orientation="h")
    fig.show()


def daily_plot_countries(dict_df, countries):
    # TO DO: visualiser l’évolution journalière du nombre cumulé des cas confirmés, morts, actifs et fermés pour un
    # certain nombre de pays sélectionner.
    # TO DO: Créer des subfigure de 2 ligne et 2 colonne de dimension 17*10

    # TO DO: Pour chacune des clés du dictionnaire dict_df visualiser l’évolution du nombre de cas pour chaque
    # Pays de countries







    # TO DO: Pour chaque pays de countries afficher un petit sommaire du nombre totales des cas confirmés, morts,
    # actifs et fermés




    fig.show()


def week_of_year(df):
    # TO DO: grouper les clés du dictionnaire dict_df par numéro de semaine
    # TO DO: ajouter une colonne "WeekofYear" a la base de données df

    # TO DO: créer une nouvelle base de données week_df avec les mêmes colonnes que df

    # TO DO: Pout toutes les semaines de la base de données calculer la somme des cas de cette semaine pour remplir
    # la base de données week_df
    # Exemple:
    # Jour 1: 10 cas ==> semaine 1
    # Jour 2: 30 cas ==> semaine 1
    # Jour 3: 40 cas ==> semaine 1
    # Jour 4: 20 cas ==> semaine 1
    # Jour 5: 50 cas ==> semaine 1
    # Jour 6: 80 cas ==> semaine 1
    # Jour 7: 70 cas ==> semaine 1
    # ==> semaine 1: 300 cas


    # TO DO: regrouper la base de donnee week_df par "WeekofYear"

    return ...


def weekly_bar(dict_df, country):
    # TO DO: visualiser l’évolution hebdomadaire des cas confirmés, morts, actifs et fermés pour un de pays.
    # TO DO: Pour l'ensemble des clés du dictionnaire dict_df regrouper les bases de donner par "WeekofYear" pensez a
    # utiliser la fonction week_of_year implémenter précédemment.

    # TO DO: Créer des subfigure de 2 ligne et 2 colonne de dimension 15*10

    # TO DO: Pour chacune des clés du dictionnaire dict_df visualiser l’évolution hebdomadaire









    fig.show()
