#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 07:46:13 2018

@author: xsxsz
"""

import tensorflow as tf

a = tf.constant([  
    [[1.0,2.0,3.0,4.0],  
     [5.0,6.0,7.0,8.0],  
     [8.0,7.0,6.0,5.0],  
     [4.0,3.0,2.0,1.0]],  
    [[4.0,3.0,2.0,1.0],  
     [8.0,7.0,6.0,5.0],  
     [1.0,2.0,3.0,4.0],  
     [5.0,6.0,7.0,8.0]]  
])
a=tf.reshape(a,[1,2,2,8])
normal=tf.nn.lrn(a,2,0,1,1)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(normal))
    