# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 00:40:06 2017

@author: James
"""

import numpy as np
from ecdf_func import ecdf

#exponential inter-incident times

inter_times = 500

mean = np.mean(inter_times)

samples = np.random.exponential(mean, size=10000)

x, y = ecdf(inter_times)

