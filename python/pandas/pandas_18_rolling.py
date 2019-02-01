#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:39:24 2019

@author: xsxsz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=np.random.randn(20)
se=pd.Series(data)
se.index=pd.date_range('2019-2-1',periods=20,freq='d')
print(se)
print('------------')
rm=se.rolling(window=5,center=False).mean()
plt.plot(se,color='g')
plt.plot(rm,color='b')
