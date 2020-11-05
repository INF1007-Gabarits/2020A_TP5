# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import Data_Processing as dp
import world_wild_analysis as wa
import Countries_analysis as ca
import Forcasting_model as fm

if __name__ == '__main__':
    ## Partie 1:
    add_path         =  'https://raw.githubusercontent.com/CSSEGISandData/'\
                        'COVID-19/master/csse_covid_19_data/';
    add_death_df     = add_path + 'csse_covid_19_time_series/'\
                        'time_series_covid19_deaths_global.csv'
    add_confirmed_df = add_path + 'csse_covid_19_time_series/'\
                        'time_series_covid19_confirmed_global.csv'
    add_recovered_df = add_path + 'csse_covid_19_time_series/'\
                        'time_series_covid19_recovered_global.csv'
    add_summury_df   = 'https://raw.githubusercontent.com/CSSEGISandData/'\
                        'COVID-19/web-data/data/cases_country.csv'

    [death_df, confirmed_df,recovered_df, summury_df] =  dp.Load_df(
        add_death_df, add_confirmed_df, add_recovered_df, add_summury_df)
    print("\n Data death_df: \n",death_df.head(10))
    print("\n Data confirmed_df: \n",confirmed_df.head(10))
    print("\n Data recovered_df: \n",recovered_df.head(10))
    print("\n Data summury_df: \n", summury_df.head(10))
    
    summury_df = dp.summuryaddcol(summury_df, "Closed", 
                                  summury_df["Deaths"] + 
                                  summury_df["Recovered"])
    print("\n Data summury_df: \n", summury_df.head(10))
    
    columns = ["Country_Region", "Confirmed", "Deaths", 
               "Active", "Closed", "Recovered", "Mortality_Rate"]
    summury_df = dp.summuryextractcol(summury_df, columns)
    print("\n Data summury_df: \n", summury_df.head(10))
    
    summury_df_by_country = dp.summurybycountry(summury_df)
    print("\n Data summury_df_by_country: \n", summury_df_by_country.head(10))
    
    dict_df = dp.creatdictdf(death_df,confirmed_df,recovered_df)
    print("\n Data dict_df (Confirmed): \n", dict_df["Confirmed"].head(10))
    
    dict_df = dp.dictdfremovecol(dict_df, ["Province/State","Lat","Long"])
    print("\n Data dict_df (Deaths): \n", dict_df["Deaths"].head(10))
    
    dict_df_by_country = dp.dictdfbycountry(dict_df)
    print("\n Data dict_df (Recovered): \n", 
          dict_df_by_country["Recovered"].head(10))
    
    
    dict_df_by_country = dp.dictdfaddkey(dict_df_by_country)
    print("\n Data dict_df (Active): \n", 
          dict_df_by_country["Active"].head(10))
    
    dict_df_by_day = dp.dictdfbyday(dict_df_by_country)
    print("\n Data dict_df (Closed): \n", dict_df_by_day["Closed"].head(10))
    
    dp.basicinfsummury(summury_df) 
    
    wa.summuryanalyseData(summury_df_by_country)

    wa.summurysecteur(summury_df)

    countries = ["Spain","Canada","Italy","China"]
    wa.countriesbar(summury_df_by_country, countries)
    
    word_pic = r"...\World_Map\World_Map.shp"
    wa.worldmap(dict_df_by_country,"Confirmed",word_pic)
    
    ca.worldcases(dict_df_by_country)
    
    ca.dailyplotcountries(dict_df_by_day, countries)
    
    ca.weeklybar(dict_df_by_day,"Spain")
    
    country_df, train_df = fm.CreatCountryDataTrain(dict_df_by_day, "Spain")
    
    model_df, dic_model, dic_score = fm.train_model(train_df,["Confirmed"])
    
    fm.plotmodel(country_df, model_df)
    
    model_pred_df = fm.predictionmodel(country_df, train_df, model_df, 
                                       dic_model)
    
    fm.plofforcasting(country_df, model_df, model_pred_df)
