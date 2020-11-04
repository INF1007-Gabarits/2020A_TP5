#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Data_Processing
import world_wild_analysis
import Countries_analysis
import Forcasting_model

if __name__ == '__main__':

add_path         = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/';
add_death_df     = add_path + 'csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
add_confirmed_df = add_path + 'csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
add_recovered_df = add_path + 'csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
add_summury_df   = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv'

[death_df, confirmed_df,recovered_df, summury_df] = Data_Processing.Load_df(add_death_df, add_confirmed_df, 
                                                                          add_recovered_df, add_summury_df)
death_df.head(10)
confirmed_df.head(10)
recovered_df.head(10)
summury_df.head(10)

summury_df = Data_Processing.summuryaddcol(summury_df, "Closed", summury_df["Deaths"] + summury_df["Recovered"])
summury_df.head(10)

columns = ["Country_Region", "Confirmed", "Deaths", "Active", "Closed", "Recovered", "Mortality_Rate"]
summury_df = Data_Processing.summuryextractcol(summury_df, columns)
summury_df.head(10)

summury_df_by_country = Data_Processing.summurybycountry(summury_df)
summury_df_by_country.head(10)

dict_df = Data_Processing.creatdictdf(death_df,confirmed_df,recovered_df)
dict_df["Confirmed"].head(10)

dict_df = Data_Processing.dictdfremovecol(dict_df, ["Province/State","Lat","Long"])
dict_df["Deaths"].head(10)

dict_df_by_country = Data_Processing.dictdfbycountry(dict_df)
dict_df_by_country["Recovered"].head(10)


dict_df_by_country = Data_Processing.dictdfaddkey(dict_df_by_country)
dict_df_by_country["Active"].head(10)

dict_df_by_day = Data_Processing.dictdfbyday(dict_df_by_country)
dict_df_by_day["Closed"].head(10)

Data_Processing.basicinfsummury(summury_df)  

world_wild_analysis.summuryanalyseData(summury_df_by_country)

world_wild_analysis.summurysecteur(summury_df)

countries = ["Spain","Canada","Italy","China"]
world_wild_analysis.countriesbar(summury_df_by_country, countries)

word_pic = r"C:\Users\belga\Covid\World_Map\World_Map.shp"
Countries_analysis.worldmap(dict_df_by_country,"Confirmed",word_pic)

Countries_analysis.worldcases(dict_df_by_country)

Countries_analysis.dailyplotcountries(dict_df_by_day, countries)

Countries_analysis.weeklybar(dict_df_by_day,"Spain")

country_df, train_df = Forcasting_model.CreatCountryDataTrain(dict_df_by_day, "Spain")

model_df, dic_model, dic_score = Forcasting_model.train_model(train_df,["Confirmed"])

Forcasting_model.plotmodel(country_df, model_df)

model_pred_df = Forcasting_model.predictionmodel(country_df, train_df, model_df, dic_model)

Forcasting_model.plofforcasting(country_df, model_df, model_pred_df)
