#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:30:47 2018

@author: xsxsz
"""

import tensorflow as tf

k=tf.constant([
    [1,0,1],
    [2,1,0],
    [0,0,1]
],dtype=tf.float32,name='k')
i=tf.constant([
    [4,3,1,0],
    [2,1,0,1],
    [1,2,4,1],
    [3,1,0,2]
],dtype=tf.float32,name='i')

kernel=tf.reshape(k,[3,3,1,1],name='kernel')
image=tf.reshape(i,[1,4,4,1],name='image')

output=tf.nn.conv2d(image,kernel,strides=[1,1,1,1],padding='SAME')
output=tf.squeeze(output)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(output))
    print('------------')

