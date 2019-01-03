#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:50:03 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
init=tf.global_variables_initializer()
A=np.linspace(-10,10,6,dtype='int32').reshape(2,3)
print(A)
print('--------------')
bias=np.linspace(0,16,3,dtype='int32')
print(bias)
print('--------------')
data=tf.placeholder(dtype=tf.int32,shape=[2,3])
b=tf.placeholder(dtype=tf.int32,shape=[3])
operator=tf.nn.bias_add(data,b)
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(operator,{data:A,b:bias}))
    