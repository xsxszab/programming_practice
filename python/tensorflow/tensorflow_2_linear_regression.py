#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:01:26 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
x_data = np.float32(np.random.rand(2, 10)) 
y_data = np.dot([0.100, 0.200], x_data) + 0.300
print(x_data)
print('----------')
print(y_data)
print('**********')
b=tf.Variable(tf.zeros([1]))
W=tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y=tf.matmul(W,x_data)+b
loss=tf.reduce_mean(tf.square(y-y_data))
opti=tf.train.GradientDescentOptimizer(0.1)
train=opti.minimize(loss)
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
for step in range(0,200):
    sess.run(train)
    if step%10==0:
        print(sess.run(W))
        print('----------')
        print(sess.run(b))
        print('----------')


