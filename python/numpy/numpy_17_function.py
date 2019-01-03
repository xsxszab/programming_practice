# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:22:04 2018

@author: Administrator
"""

import numpy as np
vec1=[1,3,2]
vec2=[-2,1,-1]
def cosine(vec1,vec2):
    x=np.array(vec1)
    y=np.array(vec2)
    lenx=np.sqrt(x.dot(x))
    lney=np.sqrt(y.dot(y))
    cos=x.dot(y)/(lenx*lney)
    print cos
    print'----------'
    angel=np.arccos(cos)
    print angel
    print'----------'
    angel1=angel*180/np.pi
    print angel1
    print'----------'
    return
cosine(vec1,vec2)