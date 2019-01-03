#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:14:30 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf

npx = np.random.uniform(-1, 1, (1000, 1))
npy = np.power(npx, 2) + np.random.normal(0, 0.1, size=npx.shape)
npx_train, npx_test = np.split(npx, [800])
npy_train, npy_test = np.split(npy, [800])

tfx = tf.placeholder(npx_train.dtype, npx_train.shape)
tfy = tf.placeholder(npy_train.dtype, npy_train.shape)

dataset=tf.data.Dataset.from_tensor_slices((tfx,tfy)).shuffle(buffer_size=100)
dataset=dataset.batch(32)
dataset=dataset.repeat(3)
iterator=dataset.make_initializable_iterator()

X,Y=iterator.get_next()
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
