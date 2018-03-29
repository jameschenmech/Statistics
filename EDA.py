# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:16:25 2017

@author: James
"""

import pandas as pd

df_swing = pd.read_csv('2008_swing_states.csv')

df_swing[['state', 'county', 'dem_share']]


import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

data = load_iris()

df = pd.DataFrame(data['data'], columns=data['feature_names']) 
df['target'] = data['target']

#replace the 0,1,2 with species names
for idx,species in enumerate(data['target_names']):
    print(idx, species)
    df['target'].replace(idx, species, inplace=True)
df.rename(columns={'target':'species'}, inplace=True)

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(df['petal length (cm)'])

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()


#adjust number of bins
# Import numpy
import numpy as np

petal_length = df['petal length (cm)']
# Compute number of data points: n_data
n_data = len(petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
_ = plt.hist(petal_length, bins = n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()


#Bee Swarm Plots
_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)

_ = plt.xlabel('state')

_ = plt.ylabel('percent of vote for Obama')

plt.show()



# Create bee swarm plot with Seaborn's default settings
# Label the axes
# Show the plot
_ = sns.swarmplot(x='species', y='petal length (cm)', data=df)
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')
plt.show()