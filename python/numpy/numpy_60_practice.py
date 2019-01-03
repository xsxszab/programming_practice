#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 18:49:37 2018

@author: xsxsz
"""

import numpy as np

W=np.random.randn(5,10)
x=np.random.randn(10,2)
D=W.dot(x)
dD=np.random.randn(*D.shape)
dW=dD.dot(x.T)
dx=W.T.dot(dD)
