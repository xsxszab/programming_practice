# coding: utf-8
"""
Created on Sat Dec  1 13:21:29 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle

def read_batch(filename):
    with open(filename,"rb") as file:
        data=pickle.load(file,encoding='latin1')
        X=np.array(data['data'])
        Y=np.array(data['labels'])
        return X,Y

X_train,Y_train=read_batch('data_batch_1')
for i in range(4):
    temp_x,temp_y=read_batch('data_batch_'+str(i+2))
    X_train=np.concatenate((X_train,temp_x),axis=0)
    Y_train=np.concatenate((Y_train,temp_y),axis=0)
X_test,Y_test=read_batch('test_batch')
X_test=X_test.reshape(-1,3,32,32)
X_test=np.transpose(X_test,[0,2,3,1])
print(X_train.shape)
print('---------')
print(Y_train.shape)
print('---------')
X_train=X_train.reshape(-1,3,32,32)
X_train=np.transpose(X_train,[0,2,3,1])
plt.figure(figsize=(10,5))
for i in range(4):
    plt.subplot(221+i)
    plt.imshow(X_train[i])
    plt.title(Y_train[i])

plt.figure(figsize=(10,5))
for i in range(4):
    plt.subplot(221+i)
    plt.imshow(X_test[i])
    plt.title(Y_test[i])
