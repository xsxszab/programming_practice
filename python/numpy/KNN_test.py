# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 07:31:44 2018

@author: Administrator
"""

import KNN
import numpy as np
import matplotlib.pyplot as plt
dataset,labels=KNN.createDataSet()
plt.figure(dpi=100,figsize=(5,4),facecolor='#ADD8E6',edgecolor='b')
plt.grid(linestyle='-.',alpha=0.5,linewidth=0.7)           
color=np.arctan2(dataset[:,0],dataset[:,1])
plt.scatter(dataset[:,0],dataset[:,1],c=color)
plt.title('KNN')
plt.xlabel('X')
plt.ylabel('Y')
input=np.array([0.4,2])
k=3
output=KNN.classify(input,dataset,labels,k)
p=plt.scatter(input[0],input[1],color='r',marker='^')
plt.legend([p],['sample'],loc='upper right')
print output
