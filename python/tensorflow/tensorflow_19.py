#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 18:10:32 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
matrix=np.linspace(-10,10,16,dtype='float64').reshape(4,4)
init=tf.global_variables_initializer()
mat=tf.constant(matrix)
det=tf.matrix_determinant(mat)
inverse=tf.matrix_inverse(mat)
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(mat))
    print('-------------')
    print(sess.run(det))
    print('-------------')
    print(sess.run(inverse))
    print('-------------')
    