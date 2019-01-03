#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:02:31 2018

@author: xsxsz
"""

import numpy as np
list=np.linspace(0,10,10,dtype='int')
list1=np.clip(list,2,6,out=None)
print(list1)
print('----------')
