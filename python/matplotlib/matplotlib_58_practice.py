#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:53:53 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,1)
y=np.log(x)
xe=0.1*np.abs(np.random.randn(len(y)))
plt.bar(x,y,yerr=xe,width=0.4,align='center',ecolor='b',color='g',label='test')
plt.legend(loc='upper left')
