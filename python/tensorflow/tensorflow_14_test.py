#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:09:40 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
A = [[1,3,4,5,6]]
B = [[1,3,4,3,2]]
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(tf.equal(A,B)))
    print('-------------')
    ans=tf.cast(tf.equal(A,B),'int32')
    print('-------------')
    print(sess.run(ans))
    print('-------------')
    print(sess.run(tf.argmax(ans,axis=1)))
    print('-------------')
    