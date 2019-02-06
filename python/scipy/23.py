#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:51:29 2019

@author: xsxsz
"""

import numpy as np
import scipy.optimize as optimize

c=np.array([-7,7,-2,-1,-6,0])
a=np.array([[3,-1,1,-2,0,0],[2,1,0,1,1,0],[-1,3,0,-3,0,1]])
b=np.array([-3,4,12])
ans=optimize.linprog(c,A_eq=a,b_eq=b,bounds=((0,None),(0,None),(0,None),(0,None),(0,None),(0,None)))
print(ans)
print('--------------')
