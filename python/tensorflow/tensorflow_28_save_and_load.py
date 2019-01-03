#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:44:47 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf

rand=np.random.RandomState(10)
x=np.linspace(-1,1,100)[:,np.newaxis]
noise=rand.normal(0,0.1,size=x.shape)
y=np.power(x,2)+noise
iterations=100
learning_rate=0.1

def save(x,y):
    '''
    save tensorfow model
    '''
    X=tf.placeholder(tf.float32, x.shape)
    Y=tf.placeholder(tf.float32, y.shape)
    l=tf.layers.dense(X, 10, tf.nn.relu)
    o=tf.layers.dense(l, 1)
    loss=tf.losses.mean_squared_error(Y,o)
    loss = tf.losses.mean_squared_error(Y, o)
    init=tf.global_variables_initializer()
    saver=tf.train.Saver()
    train=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
    with tf.Session() as sess:
        sess.run(init)
        for i in range(iterations):
            sess.run(train,feed_dict={X:x,Y:y})
        saver.save(sess,'./model',write_meta_graph=False)
    return

save(x,y)

def load():
    tf_x = tf.placeholder(tf.float32, x.shape) 
    tf_y = tf.placeholder(tf.float32, y.shape)
    l_ = tf.layers.dense(tf_x, 10, tf.nn.relu)
    o_ = tf.layers.dense(l_, 1)
    loss_ = tf.losses.mean_squared_error(tf_y, o_)
    sess=tf.Session()
    saver=tf.train.Saver()
    saver.restore(sess,'./model')