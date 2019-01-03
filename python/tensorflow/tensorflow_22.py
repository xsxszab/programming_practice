#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:54:13 2018

@author: xsxsz
"""

import tensorflow as tf
with tf.name_scope('tensorboard') as scope:
    mat1=tf.constant([[2,6]],name='matrix1')
    mat2=tf.constant([[5],[9]],name='matrix2')
    product=tf.matmul(mat1,mat2,name='product')

init=tf.global_variables_initializer()
sess=tf.Session()
writer=tf.summary.FileWriter('../logs/',sess.graph)
sess.run(init)
writer.close()