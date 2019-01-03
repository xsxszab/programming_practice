#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:24:27 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
init=tf.global_variables_initializer()
A=tf.placeholder(dtype=tf.int32,shape=[1,4])
relu=tf.nn.relu(A)
with tf.Session() as sess:
    sess.run(init)
    rand=np.random.RandomState(10)
    data=(rand.rand(1,4)*-10).astype('int32')
    print(data)
    print('--------------')
    print(sess.run(relu,{A:data}))
    print('--------------')
    