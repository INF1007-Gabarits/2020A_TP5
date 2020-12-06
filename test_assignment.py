import unittest
import math
import numpy as np
import pandas as pd
import cv2
import os
import sys
import json
import py7zr
import pickle
import tarfile
import matplotlib.pyplot as plt
import plotly.io as pio
import data_processing as dp
import world_wild_analysis as wa
import countries_analysis as ca
import forcasting_model as fm


ADD_DEATH_DF =  'deaths.csv'
ADD_CONFIRMED_DF = 'confirmed.csv'
ADD_RECOVERED_DF = 'recovered.csv'
ADD_SUMMARY_DF = 'summary.csv'

COUNTRIES = ["Spain", "Canada", "Italy", "China"]
World_PIC = r"World_Map\World_Map.shp"
COLUMNS = ["Country_Region", "Confirmed", "Deaths", "Active", "Closed", "Recovered", "Mortality_Rate"]

with py7zr.SevenZipFile('data_exepected.7z', mode='r') as z:
    z.extractall()

filename = 'data_exepected.spydata'

tar = tarfile.open(filename, "r")
# extract all pickled files to the current working directory
tar.extractall()
extracted_files = tar.getnames()
for f in extracted_files:
    if f.endswith('.pickle'):
        with open(f, 'rb') as fdesc:
            data_exepected = pickle.loads(fdesc.read())


[death_df, confirmed_df, recovered_df, summary_df] = dp.load_df(ADD_DEATH_DF, ADD_CONFIRMED_DF, 
                                                                ADD_RECOVERED_DF, ADD_SUMMARY_DF)
summary_df_1 = summary_df.copy()
dp.summary_add_col(summary_df_1, "Closed", summary_df_1["Deaths"] + summary_df_1["Recovered"])
summary_df_2 = dp.summary_extract_col(summary_df_1, COLUMNS)
summary_df_by_country = dp.summary_by_country(summary_df_2)
dict_df_1 = dp.creat_dict_df(death_df, confirmed_df, recovered_df)
dict_df_2 = dp.dict_remove_col(dict_df_1, ["Province/State", "Lat", "Long"])
dict_df_by_country_1 = dict_df_2.copy()
dp.dict_by_country(dict_df_by_country_1)
dict_df_by_country_2 = dp.dict_add_key(dict_df_by_country_1)
dict_df_by_day = dp.dict_by_day(dict_df_by_country_2)
dict_df_by_day_1 = dp.dict_by_day(dict_df_by_country_2)

def imag_fram(fig_name):
    original = cv2.imread("Image/" + fig_name + ".png")
    duplicate = cv2.imread("Image_Expected/" + fig_name + ".png")
    return original, duplicate 

class test_data_processing(unittest.TestCase):

    def test_load_df_death_df(self):
        self.data_frame_test(death_df,data_exepected["death_df"])
    
    def test_load_df_confirmed_df(self):
        self.data_frame_test(confirmed_df,data_exepected["confirmed_df"])
        
    def test_load_df_recovered_df(self):
        self.data_frame_test(recovered_df,data_exepected["recovered_df"])
    
    def test_load_df_summary_df(self):
        self.data_frame_test(summary_df,data_exepected["summary_df"])    
        
    def test_summary_add_col(self):
        self.data_frame_test(summary_df_1,data_exepected["summary_df_1"])
        
    def test_summary_extract_col(self):
        self.data_frame_test(summary_df_2,data_exepected["summary_df_2"])
        
    def test_summary_by_country(self):
        self.data_frame_test(summary_df_by_country,data_exepected["summary_df_by_country"])
        
    def test_creat_dict_df(self):
        self.dict_test(dict_df_1, data_exepected["dict_df_1"])
        
    def test_dict_remove_col(self):
        self.dict_test(dict_df_2, data_exepected["dict_df_2"])
        
    def test_dict_remove_col(self):
        self.dict_test(dict_df_2, data_exepected["dict_df_2"])
        
    def test_dict_by_country(self):
        self.dict_by_country_test(dict_df_by_country_1, data_exepected["dict_df_by_country_1"])
    
    def test_dict_add_key(self):
        self.dict_by_country_test(dict_df_by_country_2, data_exepected["dict_df_by_country_2"])
        
    def test_dict_by_day(self):
        self.dict_by_day_test(dict_df_by_day, data_exepected["dict_df_by_day"])
    
    def data_frame_test(self, df, df_expected):
        with self.subTest():
            self.assertTrue(df.equals(df_expected))
        with self.subTest():
            self.assertTrue(all(df.columns==df_expected.columns))
        with self.subTest():
            self.assertTrue(all(df.index==df_expected.index))
            
    def dict_test(self, dict_df, dict_df_expected):
        for (key, value) in dict_df.items():
            with self.subTest():
                self.data_frame_test(value,dict_df_expected[key])
            
    def dict_by_country_test(self, dict_df, dict_df_expected):
        for (key, value) in dict_df.items():
            with self.subTest():
                self.data_frame_test(value,dict_df_expected[key])
            with self.subTest():
                self.assertTrue(pd.api.types.is_datetime64_ns_dtype(value.columns))
                           
    def dict_by_day_test(self, dict_df, dict_df_expected):
        for (key, value) in dict_df.items():
            with self.subTest():
                self.assertTrue(value.equals(dict_df_expected[key]))
            with self.subTest():
                self.assertTrue(all(value.columns==dict_df_expected[key].columns))
            with self.subTest():
                self.assertTrue(pd.api.types.is_datetime64_ns_dtype(value.index))

class test_world_wild_analysis(unittest.TestCase):
    
    def test_summary_analyse_data(self):
        wa.summary_analyse_data(summary_df_by_country)
        original, duplicate = imag_fram("fig_01")
        self.assertTrue(original.shape == duplicate.shape)
    
    def test_summary_secteur(self):
        wa.summary_secteur(summary_df_2)
        original, duplicate = imag_fram("fig_02")
        self.assertTrue(original.shape == duplicate.shape)
    
    def test_countries_bar(self):
        wa.countries_bar(summary_df_by_country, COUNTRIES)
        original, duplicate = imag_fram("fig_03")
        self.assertTrue(original.shape == duplicate.shape)


class test_countries_analysis(unittest.TestCase):
    
    def test_world_cases(self):
        ca.world_cases(dict_df_by_country_2)
        original, duplicate = imag_fram("fig_04")
        self.assertTrue(original.shape == duplicate.shape)
    
    def test_daily_plot_countries(self):
        ca.daily_plot_countries(dict_df_by_day_1, COUNTRIES)
        original, duplicate = imag_fram("fig_05")
        self.assertTrue(original.shape == duplicate.shape)
    
    def test_weekly_bar(self):
        ca.weekly_bar(dict_df_by_day_1, "US")
        original, duplicate = imag_fram("fig_06")
        self.assertTrue(original.shape == duplicate.shape)

class test_forcasting_model(unittest.TestCase):
    
    def test_creat_country_data_train(self):
        country_df, train_df = fm.creat_country_data_train(dict_df_by_day_1, "US")
        with self.subTest():
            self.assertTrue(country_df.equals(data_exepected["country_df"]))
        with self.subTest():
            self.assertTrue(all(country_df.columns==data_exepected["country_df"].columns))
        with self.subTest():
            self.assertTrue(pd.api.types.is_datetime64_ns_dtype(country_df.index))
        with self.subTest():
            self.assertTrue(all(train_df.columns==data_exepected["train_df"].columns))
        with self.subTest():
            self.assertTrue(pd.api.types.is_datetime64_ns_dtype(train_df.index))
        
    
    def test_plot_model(self):
        country_df, train_df = fm.creat_country_data_train(dict_df_by_day_1, "US")
        model_df, dic_model, dic_score = fm.train_model(train_df, ["Confirmed"])
        fm.plot_model(country_df, model_df)
        original, duplicate = imag_fram("fig_07")
        self.assertTrue(original.shape == duplicate.shape)
    
    def test_plot_forcasting(self):
        country_df, train_df = fm.creat_country_data_train(dict_df_by_day_1, "US")
        model_df, dic_model, dic_score = fm.train_model(train_df, ["Confirmed"])
        model_pred_df = fm.prediction_model(country_df, train_df, dic_model)
        fm.plot_forcasting(country_df, model_df, model_pred_df) 
        original, duplicate = imag_fram("fig_08")
        self.assertTrue(original.shape == duplicate.shape)
    

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
