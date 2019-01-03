#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:02:54 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf

a=np.linspace(-2,10,20).reshape(2,10)

b=tf.convert_to_tensor(a,dtype=tf.float32)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(b))
    print('----------------')

