#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:23:05 2018

@author: xsxsz
"""

import tensorflow as tf
a=tf.Variable(0,name='a')
b=tf.constant(1)
new=tf.add(a,b)
update=tf.assign(a,new)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(3):    
        sess.run(update)
        print(sess.run(a))
        print('-----------')

