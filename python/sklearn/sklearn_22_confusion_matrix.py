#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:04:31 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
y_true=[1,0,0,2,1,0,3,3,3]
y_pred=[1,1,0,2,1,0,1,3,3]
con_mat=confusion_matrix(y_true=y_true,y_pred=y_pred)
print(con_mat)
print('----------')
plt.matshow(con_mat,cmap='gray')
plt.colorbar()
target_names=['a','b','c','d']
print(classification_report(y_true=y_true,y_pred=y_pred,target_names=target_names))
print('----------')
