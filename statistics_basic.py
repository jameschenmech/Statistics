# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:26:53 2017

@author: James
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()

df = pd.DataFrame(data=data.data, columns=data.feature_names)
df['target'] = data.target

for idx, species in enumerate(data.target_names):
    df.target.replace(idx, species, inplace=True)
df.rename(columns={'target':'species'}, inplace=True)

setosa_petal_length = df.loc[df['species']=='setosa','petal length (cm)']
versicolor_petal_length = df.loc[df['species']=='versicolor','petal length (cm)']
versicolor_petal_width = df.loc[df['species']=='versicolor','petal width (cm)']
virginica_petal_length = df.loc[df['species']=='virginica','petal length (cm)']
# Compute the mean: mean_length_vers
mean_length_vers = np.mean(versicolor_petal_length)
# Print the result with some nice formatting
print('I. versicolor:', mean_length_vers, 'cm')

#computing percentiles
# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)

#comparing percentiles to ECDF
from ecdf_func import ecdf
x_vers, y_vers = ecdf(versicolor_petal_length)
# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
plt.margins(0.02)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker ='D', color ='red',
         linestyle = 'none')

# Show the plot
plt.show()
plt.close()

#percentiles, outliers, box plots
df_swing = pd.read_csv('2008_swing_states.csv')

print(np.percentile(df_swing['dem_share'], [25, 50, 75]))

#Generating a boxplot
import seaborn as sns

df_all_states = pd.read_csv('2008_all_states.csv')

_ = sns.boxplot(x='east_west', y='dem_share',
                data=df_all_states)

_ = plt.xlabel('region')

_ = plt.ylabel('percent of vote for Obama')

plt.show()
plt.close()

#create box plot
# Create box plot with Seaborn's default settings
# Label the axes
_ = sns.boxplot(x = 'species', y = 'petal length (cm)', data = df)
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
plt.close()

#computing variances
# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = np.square(differences)

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_explicit, variance_np)

#standard deviation and the variance
# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))


#scatter plots
# Make a scatter plot
# Label the axes
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker = '.', linestyle = 'none')
_ = plt.xlabel('petal length')
_ = plt.ylabel('petal width')

# Set margins
_ = plt.margins(0.02)

# Show the result
plt.show()
plt.close()

#computing the covariance
# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0,1]

# Print the length/width covariance
print(petal_cov)

#computing the Pearson correlation coefficient
from pearson_func import pearson_r
# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)