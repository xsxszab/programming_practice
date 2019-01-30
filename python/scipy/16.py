#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:44:53 2019

@author: xsxsz
"""

import numpy as np
from scipy.fftpack import fft,ifft

x=np.array([1.0,2.0,1.0,-1.0,1.5])
y=fft(x)
print(y)
print('---------------')
yinv=ifft(y)
print(yinv)
print('---------------')
