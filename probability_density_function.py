# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:36:18 2017

@author: James
"""

#continuous values
#area under curve give probability

import pandas as pd
import numpy as np
from ecdf_func import ecdf
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

michelson_speed_of_light = pd.read_csv('michelson_speed_of_light.csv')['velocity of light in air (km/s)']

mean = np.mean(michelson_speed_of_light)

std = np.std(michelson_speed_of_light)

samples = np.random.normal(mean, std, size=10000)

x, y = ecdf(michelson_speed_of_light)

x_theor, y_theor = ecdf(samples)

_ = plt.plot(x_theor, y_theor)

_ = plt.plot(x, y, marker='.', linestyle='none')

_ = plt.xlabel('speed of light (km/s)')

_ = plt.ylabel('CDF')

plt.show()

plt.close()

#the normal pdf
# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

# Make histograms
_ = plt.hist(samples_std1, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std3, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std10, bins=100, normed=True, histtype='step')

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
plt.close()

#the normal cdf
# Generate CDFs
x_std1, y_std1 = ecdf(samples_std1)
x_std3, y_std3 = ecdf(samples_std3)
x_std10, y_std10 = ecdf(samples_std10)

# Plot CDFs
_ = plt.plot(x_std1, y_std1, marker = '.', linestyle = 'none')
_ = plt.plot(x_std3, y_std3, marker = '.', linestyle = 'none')
_ = plt.plot(x_std10, y_std10, marker = '.', linestyle = 'none')

# Make 2% margin
plt.margins(0.02)

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()
plt.close()

#Are the belmont stakes results normally distributed?
belmont_raw_data = pd.read_csv('belmont.csv')['Time']
#belmont_no_outliers = pd.to_datetime(belmont_no_outliers, format='%H:%M.%S', errors='ignore')

belmont_time = belmont_raw_data.str.extract('(\d+):(\d+).(\d+)', expand=True).astype(float)

belmont_no_outliers = belmont_time[0].mul(60).add(belmont_time[1]).add(belmont_time[2].div(100))

# Compute mean and standard deviation: mu, sigma
mu = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers)


# Sample out of a normal distribution with this mu and sigma: samples
samples = np.random.normal(mu, sigma, size = 10000)

# Get the CDF of the samples and of the data
x_theor, y_theor = ecdf(samples)
x, y = ecdf(belmont_no_outliers)


# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()
plt.close()

#What are the chances of a hourse marching or beating Secretariat's record
# Take a million samples out of the Normal distribution: samples
mu = 149.22101123595507

signma = 1.627816471774816

samples = np.random.normal(mu, sigma, size = 1000000)

# Compute the fraction that are faster than 144 seconds: prob
prob = np.sum(samples <= 144)/len(samples)

# Print the result
print('Probability of besting Secretariat:', prob)