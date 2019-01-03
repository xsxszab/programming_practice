#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:54:31 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
W=tf.Variable([.3],dtype=tf.float32)
sess=tf.Session()
init=tf.global_variables_initializer()
x=tf.placeholder(tf.float32)
sess.run(init)
print(sess.run(W))
print('--------')

