#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:41:51 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("../../mnist", one_hot=True)

learning_rate=0.1
training_epochs=25
batch_size=100
display_step=1

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

predict=tf.nn.softmax(tf.matmul(x,W)+b)

cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(predict), reduction_indices=1))

train=tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(training_epochs):
        total_batch = int(mnist.train.num_examples/batch_size)
        for j in range(total_batch):
            batch_x,batch_y=mnist.train.next_batch(batch_size)
            sess.run([train, cost], feed_dict={x:batch_x,y:batch_y})
    correct_prediction=tf.equal(tf.argmax(predict,1),tf.argmax(y,1))
    acc=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    print(acc.eval({x: mnist.test.images, y: mnist.test.labels}))
    print('--------------')
