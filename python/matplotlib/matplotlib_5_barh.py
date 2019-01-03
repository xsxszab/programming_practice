# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:59:19 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
num=[1.2,3,2,7.2,12,4]
num1=[1,2,3,4,5,6]
list=['a','b','c','d','e','f']
#plt.xkcd()
plt.figure()
plt.title('Bar')
plt.barh(range(len(num)),num,color='r',tick_label=list,label='first')
plt.barh(range(len(num1)),num1,color='b',label='second')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
