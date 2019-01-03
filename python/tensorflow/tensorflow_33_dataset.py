#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:30:55 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
list=np.linspace(0,20,20,dtype='int')
dataset=tf.data.Dataset.from_tensor_slices(list)
dataset=dataset.map(lambda x:x+1)
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
print(list)
print('------------')
iteration=dataset.make_one_shot_iterator()
element=iteration.get_next()
try:
    while True:
        print(sess.run(element))
except tf.errors.OutOfRangeError:
    print('end')
print('------------')
dataset1=dataset.batch(32)
iteration1=dataset1.make_one_shot_iterator()
element1=iteration1.get_next()
try:
    while True:
        print(sess.run(element1))
except tf.errors.OutOfRangeError:
    print('end')
print('------------')
dataset2=dataset.shuffle(buffer_size=10)
iteration2=dataset2.make_one_shot_iterator()
element2=iteration2.get_next()
try:
    while True:
        print(sess.run(element2))
except tf.errors.OutOfRangeError:
    print('end')
print('------------')
dataset3=dataset.repeat(2)
iteration3=dataset3.make_one_shot_iterator()
element3=iteration3.get_next()
try:
    while True:
        print(sess.run(element3))
except tf.errors.OutOfRangeError:
    print('end')
