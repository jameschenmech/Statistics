# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:26:53 2017

@author: James
"""
import numpy as np

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]

