# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:09:23 2018

@author: Administrator
"""

import numpy as np
list=np.linspace(1,20,10)
print np.median(list)
print'----------'
print np.var(list)
print'----------'
print np.std(list)
mat=np.array([[2,3,4],[1,7,8]])
print np.var(mat,ddof=1)
print'----------'
print np.std(mat)
print'----------'
print np.std(mat,axis=0)
print'----------'
print np.std(mat,axis=1)
print'----------'
print np.std([1,2,3],ddof=1)
print'----------'
