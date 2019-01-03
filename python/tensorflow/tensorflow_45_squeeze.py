#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:39:11 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf

rand=np.random.RandomState(10)
tensor=rand.randn(1,1,2,3,4,1)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    result1=tf.squeeze(tensor)
    print(result1)
    print('-------------')
    result2=tf.squeeze(tensor,[1,5])
    print(result2)
    print('-------------')

