# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:23:02 2017

@author: James
"""

#empirical cumulative distribution functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_swing = pd.read_csv('2008_swing_states.csv')

x = np.sort(df_swing['dem_share'])

#y axis is evenly spaced with max of 1
y = np.arange(1, len(x)+1)/len(x)

_ = plt.plot(x, y, marker='.', linestyle='none')

_ = plt.xlabel('percent of vote for Obama')

_ = plt.ylabel('ECDF')

plt.margins(0.02)  #Keeps data off plot edges