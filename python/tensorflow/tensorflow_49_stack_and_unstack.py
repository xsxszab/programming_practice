#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:27:15 2018

@author: xsxsz
"""

import tensorflow as tf

a=tf.constant([1,2,3,4])
b=tf.constant([5,6,7,8])
c=tf.stack([a,b],axis=0)
d=tf.stack([a,b],axis=1)
e=tf.unstack([a,b],axis=0)
f=tf.unstack([a,b],axis=1)
g=tf.unstack(a)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(c))
    print('------------')
    print(sess.run(d))
    print('------------')
    print(sess.run(e))
    print('------------')
    print(sess.run(f))
    print('------------')
    print(sess.run(g))
    print('------------')

