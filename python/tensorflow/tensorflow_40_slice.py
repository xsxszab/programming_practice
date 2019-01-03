#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:52:26 2018

@author: xsxsz
"""


import tensorflow as tf
t=tf.constant([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]],[[5,5,5],[6,6,6]]])
s=tf.slice(t,[1,0,0],[2,1,3])
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(s))
    print('------------')
    