#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:16:02 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
rand=np.random.RandomState(10)
a=rand.randint(10,size=(2,4))
a=a.astype('int32')
print(a)
print('--------------')
print(a.shape)
print('--------------')
print(a.dtype)
print('--------------')
b=rand.randint(10,size=(4,2))
b=b.astype('int32')
print(b)
print('--------------')
print(b.shape)
print('--------------')
mul1=tf.matmul(a,b)
mul2=tf.matmul(b,a)
calc1=mul2+np.array([1,2,3,4]).transpose()
calc2=mul2+np.array([1,2,3,4])
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(mul1))
    print('--------------')
    print(sess.run(mul2))
    print('--------------')
    print(sess.run(calc1))
    print('--------------')
    print(sess.run(calc2))
    print('--------------')
    