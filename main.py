# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import data_processing as dp
import world_wild_analysis as wa
import countries_analysis as ca
import forcasting_model as fm

Countries = ["Spain", "Canada", "Italy", "China"]
World_PIC = r"World_Map\World_Map.shp"

if __name__ == '__main__':

    # Partie 1: data_processing
    add_path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/'
    add_death_df = add_path + 'csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
    add_confirmed_df = add_path + 'csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    add_recovered_df = add_path + 'csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
    add_summury_df = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv'

    [death_df, confirmed_df, recovered_df, summury_df] = dp.load_df(add_death_df, add_confirmed_df, add_recovered_df,
                                                                    add_summury_df)
    print("\n Data death_df: \n", death_df.head(10))
    print("\n Data confirmed_df: \n", confirmed_df.head(10))
    print("\n Data recovered_df: \n", recovered_df.head(10))
    print("\n Data summury_df: \n", summury_df.head(10))
    
    summury_df = dp.summury_add_col(summury_df, "Closed", summury_df["Deaths"] + summury_df["Recovered"])
    print("\n Data summury_df: \n", summury_df.head(10))
    
    columns = ["Country_Region", "Confirmed", "Deaths", "Active", "Closed", "Recovered", "Mortality_Rate"]
    summury_df = dp.summury_extract_col(summury_df, columns)
    print("\n Data summury_df: \n", summury_df.head(10))
    
    summury_df_by_country = dp.summury_by_country(summury_df)
    print("\n Data summury_df_by_country: \n", summury_df_by_country.head(10))
    
    dict_df = dp.creat_dict_df(death_df, confirmed_df, recovered_df)
    print("\n Data dict_df (Confirmed): \n", dict_df["Confirmed"].head(10))
    
    dict_df = dp.dict_remove_col(dict_df, ["Province/State", "Lat", "Long"])
    print("\n Data dict_df (Deaths): \n", dict_df["Deaths"].head(10))
    
    dict_df_by_country = dp.dict_by_country(dict_df)
    print("\n Data dict_df (Recovered): \n", dict_df_by_country["Recovered"].head(10))

    dict_df_by_country = dp.dict_add_key(dict_df_by_country)
    print("\n Data dict_df (Active): \n", dict_df_by_country["Active"].head(10))
    
    dict_df_by_day = dp.dict_by_day(dict_df_by_country)
    print("\n Data dict_df (Closed): \n", dict_df_by_day["Closed"].head(10))
    
    dp.basic_inf_summury(summury_df)

    # Partie 2.1: world_wild_analysis
    wa.summury_analyse_data(summury_df_by_country)

    wa.summury_secteur(summury_df)

    wa.countries_bar(summury_df_by_country, Countries)

    # Partie 2.2: countries_analysis
    ca.world_map(dict_df_by_country, "Confirmed", World_PIC)

    ca.world_cases(dict_df_by_country)
    
    ca.daily_plot_countries(dict_df_by_day, Countries)
    
    ca.weekly_bar(dict_df_by_day, "Spain")

    # Partie 3: forcasting_model
    country_df, train_df = fm.creat_country_data_train(dict_df_by_day, "Spain")
    
    model_df, dic_model, dic_score = fm.train_model(train_df, ["Confirmed"])
    
    fm.plot_model(country_df, model_df)
    
    model_pred_df = fm.prediction_model(country_df, train_df, dic_model)
    
    fm.plot_forcasting(country_df, model_df, model_pred_df)
