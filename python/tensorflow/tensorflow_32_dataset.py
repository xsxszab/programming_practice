#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:08:43 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
list=np.array([1,2,3,4,5,6,6,78,99])
dataset=tf.data.Dataset.from_tensor_slices(list)
iterator=dataset.make_one_shot_iterator()
element=iterator.get_next()
sess=tf.Session()
sess.run(tf.global_variables_initializer())
#for i in range(9):
#    print(sess.run(element))

try:
    while True:
        print(sess.run(element))
except tf.errors.OutOfRangeError:
    print('end')

matrix=np.linspace(0,20,30,dtype='int').reshape(5,3,2)
dataset1=tf.data.Dataset.from_tensor_slices(matrix)
iterator1=dataset1.make_one_shot_iterator()
element1=iterator1.get_next()
try:
    while True:
        print(sess.run(element1))
except tf.errors.OutOfRangeError:
    print('end')

dataset2 = tf.data.Dataset.from_tensor_slices(
    {
        "a": np.array([1.0, 2.0, 3.0, 4.0, 5.0]),                                       
        "b": np.random.uniform(size=(5, 2))
    }
)
iterator2=dataset2.make_one_shot_iterator()
element2=iterator2.get_next()
try:
    while True:
        print(sess.run(element2))
except tf.errors.OutOfRangeError:
    print('end')
    
sess.close()