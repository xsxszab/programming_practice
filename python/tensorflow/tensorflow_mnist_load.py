#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:03:07 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
x=tf.placeholder(tf.float32,[None,784])
y_=tf.placeholder(tf.float32,[None,10])
print(type(mnist))
print('----------------')
temp=mnist.train.next_batch(4)
print(type(temp))
print('----------------')
temp1=temp[0]
temp1=temp1.reshape(4,28,28)
plt.figure(figsize=(12,10))
print(temp1.shape)
print('----------------')
fig,ax=plt.subplots(nrows=2,ncols=2,sharex=True,sharey=True)
ax=ax.flatten()
for i in range(4):
    ax[i].imshow(temp1[i,:,:])
    