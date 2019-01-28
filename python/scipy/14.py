#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:04:19 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

plt.figure(figsize=(6,12))
x=np.linspace(0,1,100)
x[0::4]=1.5
plt.subplot(411)
plt.plot(x,color='g')
plt.subplot(412)
plt.plot(signal.medfilt(x,1),color='r')
plt.subplot(413)
plt.plot(signal.medfilt(x,3),color="b")
plt.subplot(414)
plt.plot(signal.medfilt(x,5),color='y')
