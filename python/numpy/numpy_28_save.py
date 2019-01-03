# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 06:59:53 2018

@author: Administrator
"""

import numpy as np
a=np.arange(200).reshape(10,20)
b=np.arange(100).reshape(4,25)
np.save('save',a)
np.savez('savez',x=a,y=b)
npz=np.load('savez.npz')
print npz['x']
print'----------'
print npz['y']
print'----------'
np.savez_compressed('save_compressed',a,b)
n=np.load('save_compressed.npz') 
print n['arr_0']
print'----------'
