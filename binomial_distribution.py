# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:15:41 2017

@author: James
"""

#pmf - probability mass function, set of probabilities of discrete outcomes

#the number r of success in n Bernoulli trials with probability p
#of success, is Binomially distributed

import numpy as np
import matplotlib.pyplot as plt

np.random.binomial(4, 0.5, size=10)  #repeat the 4 flip experiement 10 times

samples = np.random.binomial(60, 0.1, size = 10000)
_ = plt.hist(samples)
plt.show()
plt.close()

from ecdf_func import ecdf

import seaborn as sns

sns.set()

x,y = ecdf(samples)

_ = plt.plot(x, y, marker='.', linestyle='none')

plt.margins(0.2)

_ = plt.xlabel('number of successes')

_ = plt.ylabel('CDF')

plt.show()

plt.close()

#sampling out of the binoimal distribution
# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(100, 0.05, size=10000)

# Compute CDF: x, y
x,y = ecdf(n_defaults)

# Plot the CDF with axis labels
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel("number of defaults out of 100 loans")
_ = plt.ylabel("CDF")

# Show the plot
plt.show()
plt.close()

#plotting the Binomial PMF
# Compute bin edges: bins
bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

# Generate histogram
_ = plt.hist(n_defaults, normed=True, bins=bins)

# Set margins
_ = plt.margins(0.02)

# Label axes
_ = plt.xlabel("Number of Defaults")
_ = plt.ylabel("Probability of Default")

# Show the plot
plt.show()
plt.close()


#plotting the pmf of defaults
from pmf_func import pmf_plot
pmf_plot(n_defaults)