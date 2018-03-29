# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:40:58 2017

@author: James
"""
#steps:  generate sample population multiple itmes
#       then plot distribution of the mean
#       calculate distribution of the p value with key statistic
#example:  what is the prop of getting 4 heads with 10000 repeated sampling?
 #  offical hacker stats probabilities:
 #1.  determine how to simulate data
 #2.  simulate many many times
 #3. Probability is approximately fraction of trials with the outcome of interest
 
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

random_numbers = np.random.random(size=4)

heads = random_numbers < 0.5

print(np.sum(heads))

#how many samples of 10000 give 4 heads
n_all_heads = 0 # intialize number of 4-head trials

for _ in range(10000):
    heads = np.random.random(size=4) < 0.5
    n_heads = np.sum(heads)
    if n_heads == 4:
        n_all_heads +=1
print(n_all_heads/10000)

#generating random numbers using the np.random module
# Seed the random number generator
np.random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(10000)

# Generate random numbers by looping over range(100000)
for i in range(10000):
    random_numbers[i] = np.random.random() 

# Plot a histogram
_ = plt.hist(random_numbers)

# Show the plot
plt.show()
plt.close()

#how many defaults might we expect/
# Seed random number generator
from bernoulli_func import perform_bernoulli_trials
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)


# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed = True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot
plt.show() #not optimal to plot histogram when results are integers, hard to read
plt.close()

#will the bank fail?
#ecdf is read: trials with 10 defaults OR LESS if ~100%
 # Compute ECDF: x, y
from ecdf_func import ecdf

x, y  = ecdf(n_defaults)

# Plot the ECDF with labeled axes
_ = plt.plot(x, y, marker = '.', linestyle = 'none' )
_ = plt.xlabel('number of defaults')
_ = plt.ylabel('percentage defaults')


# Show the plot
plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)
print(n_lose_money)
# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))
#interest rate is such that banks will lose money if 10 or more
#of its loans are daulted upon


