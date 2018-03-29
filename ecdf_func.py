# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:23:02 2017

@author: James
"""

#empirical cumulative distribution functions

def ecdf(data):
    import numpy as np
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n=len(data)

    # x-data for the ECDF: x
    x=np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y