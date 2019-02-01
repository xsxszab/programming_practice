#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 22:02:06 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack,signal

b=30
f_s=80
N=8000
t=np.linspace(0, 10, N, endpoint=False)
sq=signal.square(2*np.pi*5*t)

F = fftpack.fft(sq)
f = fftpack.fftfreq(N, 1.0/f_s)
F_filtered = F * (abs(f) < 5)
ift = fftpack.ifft(F_filtered)
mask = np.where(f >= 0)

fig, axes = plt.subplots(4,1)
axes[0].plot(t, sq)
axes[0].set_ylim(-2, 2)
axes[1].plot(f[mask], abs(F[mask])/N, label="freq")
axes[2].plot(t,ift.real, label="all")
axes[3].plot(t,ift.real, label="zoom")
axes[3].set_xlim(1, 2)
