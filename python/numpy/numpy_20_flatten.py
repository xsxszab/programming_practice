# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:59:57 2018

@author: Administrator
"""

import numpy as np
a=np.arange(30).reshape(3,10)
print a
print'----------'
b=a.ravel()
print b
print'----------'
c=a.flatten()
print c 
print'----------'