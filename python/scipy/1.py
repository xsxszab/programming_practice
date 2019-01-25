#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:12:25 2019

@author: xsxsz
"""

import scipy
import numpy as np
from scipy import io
import matplotlib.pyplot as plt

a=np.arange(10)
io.savemat('a.mat',{'arr':a})
a_load=io.loadmat('a.mat')['arr']
print(a_load)
print('-------------')
plt.plot(a)