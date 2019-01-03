#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:54:13 2018

@author: xsxsz
"""

import tensorflow as tf
hello=tf.constant('Hello world')
sess=tf.Session()
print(sess.run(hello))
a=tf.constant(12)
b=tf.constant(13)
print('---------')
print(sess.run(a+b))
print('---------')
mat=tf.constant([[3,3]])
mat1=tf.constant([[2],[2]])
print(mat)
print('---------')
mul=tf.matmul(mat,mat1)
print(mul)
print('---------')
