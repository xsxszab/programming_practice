#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:25:21 2018

@author: xsxsz
"""

import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

def read_batch(filename):
    with open(filename,"rb") as file:
        data=pickle.load(file,encoding='latin1')
        X=np.array(data['data'])
        Y=np.array(data['labels'])
        return X,Y

n_neighbors=np.linspace(1,10,10,dtype='int')

X_train,Y_train=read_batch('data_batch_1')
for i in range(4):
    temp_x,temp_y=read_batch('data_batch_'+str(i+2))
    X_train=np.concatenate((X_train,temp_x),axis=0)
    Y_train=np.concatenate((Y_train,temp_y),axis=0)
X_test,Y_test=read_batch('test_batch')
for i in range(10):    
    clf=KNeighborsClassifier(n_neighbors=n_neighbors[i])
    clf.fit(X_train[:4000],Y_train[:4000])
    score=clf.score(X_test[:100],Y_test[:100])
    print(score)
    print('------------')
