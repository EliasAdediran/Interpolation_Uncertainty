# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 22:21:07 2023

This function will remove edges where there is no data_processed assuming there are not holes in the middle

@author: Elias Adediran
"""

import numpy as np

def Remove_edge(data, ndv):
    data_processed = data.copy()
    shrink_idx = 0
    have_ndv = True
    while have_ndv:
        tmp = data_processed[:,0]
        if np.any(tmp == ndv):
            data_processed = data_processed[:,1:]
        tmp = data_processed[0,:]
        if np.any(tmp == ndv):
            data_processed = data_processed[1:,:]
        tmp = data_processed[:,-1]
        if np.any(tmp == ndv):
            data_processed = data_processed[:,:-1]
        tmp = data_processed[-1,:]
        if np.any(tmp == ndv):
            data_processed = data_processed[:-1,:]   
        shrink_idx +=1
        have_ndv = np.any(data_processed == ndv)
        if shrink_idx > 100:
            have_ndv = False

    if data.shape == data_processed.shape:
        print('no data removed from the boundary')
    else:
        print('data have been removed from the boundary')
    return data_processed