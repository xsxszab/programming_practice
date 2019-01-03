#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:20:36 2018

@author: xsxsz
"""

import tensorflow as tf
x=tf.placeholder(tf.float32)
W=tf.Variable(tf.zeros([1]))
b=tf.Variable(tf.zeros([1]))
y1=tf.placeholder(tf.float32)
y=W*x+b
lost=tf.reduce_mean(tf.square(y1-y))
optimizer=tf.train.GradientDescentOptimizer(0.000001)
train=optimizer.minimize(lost)
sess=tf.Session()
init=tf.global_variables_initializer()
sess.run(init)
steps=1000
for i in range(steps):
    xs=[i]
    ys=[3*i]
    feed={x:xs,y1:ys}
    sess.run(train,feed_dict=feed)
    if i%100==0:
        print("After %d iteration:" % i)
        print("W: %f" % sess.run(W))
        print("b: %f" % sess.run(b))
        print("lost: %f" % sess.run(lost, feed_dict=feed))