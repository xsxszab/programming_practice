#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:44:13 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
init=tf.global_variables_initializer()
x=tf.constant([1,2],dtype=tf.float32)
tf.cast(x,tf.int32)
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(x))
