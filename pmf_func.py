# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:27:36 2017

@author: James
"""
#plots the probabilty mass functon of an array series of integers
 
def pmf_plot(samples_array):
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    samples = pd.DataFrame(samples_array, columns=['event'])

    samples_by_size = samples.groupby('event').size()
#group the pd series according to number of occurances
#group by creates an array
    samples_by_size = pd.DataFrame(samples_by_size, columns=['event'])
#convert the arrary to DataFrame to be able to add another column
    samples_by_size['probability'] = samples_by_size.div(np.sum(samples_by_size))
#add the probability column

    _ = plt.stem(samples_by_size['probability'], linefmt='b-', markerfmt='bo', basefmt='r-')
#set the plot to stem
    _ = plt.margins(0.02)

    _ = plt.ylabel("probability")

    _ = plt.xlabel("discrete values")
    
    plt.show()
    plt.close()
