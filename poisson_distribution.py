# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:36:18 2017

@author: James
"""

import numpy as np
from ecdf_func import ecdf
from pmf_func import pmf_plot
import matplotlib.pyplot as plt

samples = np.random.poisson(6, size=10000)

x, y = ecdf(samples)

pmf_plot(samples)

_ = plt.plot(x, y, marker='.', linestyle='none')

plt.margins(0.02)

_ = plt.xlabel('number of sucesses')

_ = plt.ylabel('CDF')

plt.show()

plt.close()

#relationship between Binomial and Poisson distributions
# Draw 10,000 samples out of Poisson distribution: samples_poisson
samples_poisson = np.random.poisson(10, size = 10000)

# Print the mean and standard deviation
print('Poisson:     ', np.mean(samples_poisson),
                       np.std(samples_poisson))

# Specify values of n and p to consider for Binomial: n, p
n = [20, 100, 1000]
p = [0.5, 0.1, 0.01]

# Draw 10,000 samples for each n,p pair: samples_binomial
for i in range(3):
    samples_binomial = np.random.binomial(n[i], p[i], size =10000)
    
    # Print results
    print('n =', n[i], 'Binom:', np.mean(samples_binomial),
                                 np.std(samples_binomial))

#Probability of getting 7 or more no hitters
# Draw 10,000 samples out of Poisson distribution: n_nohitters
n_nohitters = np.random.poisson(251/115, size = 10000)

# Compute number of samples that are seven or greater: n_large
n_large = np.sum(n_nohitters >= 7)

# Compute probability of getting seven or more: p_large
p_large = n_large/10000

# Print the result
print('Probability of seven or more no-hitters:', p_large)
