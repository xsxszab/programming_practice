#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:44:42 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
rand=np.random.RandomState(10)
matrix=(rand.rand(4,10)*10).astype('int64')
print(matrix.shape)
print('---------')
sess=tf.Session()
init=tf.global_variables_initializer()
sess.run(init)
mat1=sess.run(tf.argmax(matrix))
mat2=sess.run(tf.argmax(matrix,axis=0))
mat3=sess.run(tf.argmax(matrix,axis=1))
mean=sess.run(tf.reduce_mean(matrix))
sess.close()

print(matrix)
print('---------')
print(mat1)
print('---------')
print(mat2)
print('---------')
print(mat3)
print('---------')
print(mean)
print('---------')
