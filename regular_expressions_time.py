# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:47:42 2017

@author: James
"""
import pandas as pd


#Are the belmont stakes results normally distributed?
belmont_raw_data = pd.read_csv('belmont.csv')['Time']
#belmont_no_outliers = pd.to_datetime(belmont_no_outliers, format='%H:%M.%S', errors='ignore')

belmont_time = belmont_raw_data.str.extract('(\d+):(\d+).(\d+)', expand=True).astype(float)

belmont_no_outliers = belmont_time[0].mul(60).add(belmont_time[1]).add(belmont_time[2].div(100))

