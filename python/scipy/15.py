#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:46:08 2019

@author: xsxsz
"""

import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

x=np.linspace(0,1,1400)
y=7*np.sin(2*np.pi*180*x) + 2.8*np.sin(2*np.pi*390*x)+5.1*np.sin(2*np.pi*600*x)
yy=fft(y)
yreal=yy.real
yimag=yy.imag
yf=abs(fft(y))
yf1=abs(fft(y))/len(x)
yf2 = yf1[range(int(len(x)/2))]
xf = np.arange(len(y))
xf1 = xf
xf2 = xf[range(int(len(x)/2))]
plt.subplot(221)
plt.plot(x[0:50],y[0:50])   

plt.subplot(222)
plt.plot(xf,yf,'r')

plt.subplot(223)
plt.plot(xf1,yf1,'g')

plt.subplot(224)
plt.plot(xf2,yf2,'b')
