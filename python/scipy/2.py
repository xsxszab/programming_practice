#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:16:03 2019

@author: xsxsz
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x=stats.norm.rvs(size=20000)
print(x)
print('------------')
plt.hist(x)
