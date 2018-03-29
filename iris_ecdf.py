# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:34:49 2017

@author: James
"""

import matplotlib.pyplot as plt
import pandas as pd
from ecdf_func import ecdf

from sklearn.datasets import load_iris

data = load_iris()

df = pd.DataFrame(data['data'], columns=data['feature_names']) 
df['target'] = data['target']

#replace the 0,1,2 with species names
for idx,species in enumerate(data['target_names']):
    print(idx, species)
    df['target'].replace(idx, species, inplace=True)
df.rename(columns={'target':'species'}, inplace=True)

versicolor_petal_length = df[df['species']=='versicolor']['petal length (cm)'] 
setosa_petal_length = df[df['species']=='setosa']['petal length (cm)']
virginica_petal_length = df[df['species']=='virginica']['petal length (cm)']


# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')

# Make the margins nice
_ = plt.margins(0.02)

# Label the axes
_ = plt.xlabel("versicolor_petal_length")
_ = plt.ylabel("ECDF")

# Display the plot
plt.show()
plt.close()

#Comparisons of ECDF
# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker = '.', linestyle = 'none')
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')
_ = plt.plot(x_virg, y_virg, marker = '.', linestyle = 'none')

# Make nice margins
_ = plt.margins(0.02)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()