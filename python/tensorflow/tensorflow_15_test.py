#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:18:29 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
a = tf.constant([1.,2.,3.,0.,9.,])
b = tf.constant([[1,2,3],[3,2,1],[4,5,6],[6,5,4]])
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(a))
    print('----------------')
    print(sess.run(b))
    print('----------------')
    print(sess.run(tf.argmax(a,0)))
    print('----------------')
    print(sess.run(tf.argmax(b,0)))
    print('----------------')
    print(sess.run(tf.argmax(b,1)))
    print('----------------')
    print(sess.run(tf.reduce_mean(a,0)))
    print('----------------')
    print(sess.run(tf.reduce_mean(b,0)))
    print('----------------')
    print(sess.run(tf.reduce_mean(b,1)))
    print('----------------')
    print(sess.run(tf.reduce_max(b,0)))
    print('----------------')
    