# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 13:37:30 2017

@author: James
"""

import pandas as pd
import numpy as np

df_swing = pd.read_csv('2008_swing_states.csv')

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

bin_edges = np.arange(0,101,5)

_ = plt.hist(df_swing['dem_share'], bins=bin_edges)

_ = plt.xlabel('percent of vote for Obama')

_ = plt.ylabel('number of countries')

plt.show()

#---
from sklearn.datasets import load_iris

data = load_iris()

X = pd.DataFrame(data.data)

X.columns = data.feature_names

y = data.target

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Show histogram
plt.show()