#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:58:55 2018

@author: xsxsz
"""

import tensorflow as tf
sess=tf.Session()
init=tf.global_variables_initializer()
label=tf.constant([0,1,2,3,4,5,6,7])
a=tf.one_hot(label,10,1,0)
sess.run(init)
print(sess.run(label))
print('--------')
print(sess.run(a))
print('--------')
sess.close()