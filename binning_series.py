# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:27:36 2017

@author: James
"""
   
def pmf_plot(samples_array):
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    samples = pd.DataFrame(samples_array, columns=['event'])

    samples_by_size = samples.groupby('event').size()

    samples_by_size = pd.DataFrame(samples_by_size, columns=['event'])

    samples_by_size['probability'] = samples_by_size.div(np.sum(samples_by_size))


    _ = plt.stem(samples_by_size['probability'], linefmt='b-', markerfmt='bo', basefmt='r-')

    _ = plt.margins(0.02)

    _ = plt.ylabel("probability")

    _ = plt.ylabel("discrete values")
    
    plt.show()

