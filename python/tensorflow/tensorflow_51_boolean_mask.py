#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 07:38:14 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf

tensor_1=tf.Variable([1,2,3,4])
mask_1=tf.Variable([True,False,True,False])
boolean_mask_1=tf.boolean_mask(tensor_1,mask_1)
tensor_2=tf.Variable(np.linspace(1,100,24,dtype='int').reshape(2,3,4))
mask_2=tf.Variable([True,False])
boolean_mask_2=tf.boolean_mask(tensor_2,mask_2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(boolean_mask_1))
    print('-------------')
    print(sess.run(boolean_mask_2))
    print('-------------')

