#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:30:13 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
v1=tf.Variable(tf.constant(1.0,shape=[1]))
v2=tf.Variable(tf.constant(2.0,shape=[1]))
result=v1+v2
init=tf.global_variables_initializer()
sess=tf.Session()
saver=tf.train.Saver()
sess.run(init)
saver.save(sess,'./model.ckpt')
sess.close()
