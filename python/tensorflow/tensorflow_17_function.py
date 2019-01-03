#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:40:59 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
init=tf.global_variables_initializer()
A=np.linspace(-100,100,20,dtype='float64').reshape((2,10))
print(A)
print('--------------')
data=tf.placeholder(dtype=tf.float64,shape=(2,10))
relu=tf.nn.relu(data)
relu6=tf.nn.relu6(data)
sigmoid=tf.nn.sigmoid(data)
tanh=tf.nn.tanh(data)
softsign=tf.nn.softsign(data)
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(relu,{data:A}))
    print('--------------')
    print(sess.run(relu6,{data:A}))
    print('--------------')
    print(sess.run(sigmoid,{data:A}))
    print('--------------')
    print(sess.run(tanh,{data:A}))
    print('--------------')
    print(sess.run(softsign,{data:A}))
    print('--------------')
    