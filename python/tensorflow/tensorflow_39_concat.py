#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:46:21 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
t1=np.array([[1,2], [2,3],[4,4],[5,3]])
t2=np.array([[7,4], [8,4],[2,10],[15,11]])
concat1=tf.concat([t1, t2], axis=0)
concat2=tf.concat([t1, t2], axis=1)
concat3=tf.concat([t1, t2], axis=-1)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(concat1))
    print('---------')
    print(sess.run(concat2))
    print('---------')
    print(sess.run(concat3))
    print('---------')
