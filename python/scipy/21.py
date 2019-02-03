#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:27:16 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
import scipy.misc as misc
img1=misc.face()[:,:,0]
u,s,vh=svd(img1)
img2=np.dot(u[:,0:10],np.dot(np.diag(s[0:10]),vh[0:10,:]))
img3=np.dot(u[:,0:50],np.dot(np.diag(s[0:50]),vh[0:50,:]))
img4=np.dot(u[:,0:100],np.dot(np.diag(s[0:100]),vh[0:100,:]))
plt.figure()
plt.gray()
plt.subplot(221)
plt.imshow(img1)
plt.subplot(222)
plt.imshow(img2)
plt.subplot(223)
plt.imshow(img3)
plt.subplot(224)
plt.imshow(img4)
