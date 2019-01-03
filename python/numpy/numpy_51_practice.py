#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:07:06 2018

@author: xsxsz
"""

import time
import numpy as np

arr=np.random.random(100000)

time1=time.time()
ans1=arr**3
time2=time.time()
ans2=np.power(arr,3)
time3=time.time()
print((time2-time1)/(time3-time2))
