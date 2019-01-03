#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:44:38 2018

@author: xsxsz
"""

import tensorflow as tf
import numpy as np
mat=tf.ones([2,3],dtype=tf.int32)
print(mat)
print('-------------')
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
print(sess.run(mat))
print('-------------')
mat_shape=np.array([[2,3,4],[2,8,6],[6,5,4]])
print(mat_shape)
print('-------------')
mat1=tf.ones_like(mat_shape)
print(sess.run(mat1))
print('-------------')
print(sess.run(tf.fill([3,4],2)))
print('-------------')