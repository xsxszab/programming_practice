#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 08:38:18 2019

@author: xsxsz
"""

import numpy as np

x1=[1,2,3,4]
x2=[4,5,6]
ans=np.outer(x1,x2)
print(ans)
print('------------')


x1 = [[1,2],[3,4]]
x2 = [[1,1],[1,1]]
ans=np.outer(x1,x2)
print(ans)
print('------------')

x1 = [1,2,3,4]
x2 = [1,1,1,1]
ans=np.outer(x1,x2)
print(ans)
print('------------')