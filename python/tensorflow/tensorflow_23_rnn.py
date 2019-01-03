#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:11:44 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
from  tensorflow.examples.tutorials.mnist import  input_data
mnist=input_data.read_data_sets("../../mnist",one_hot=True)

#------------------
train_rate=0.001
train_step=1000
batch_size=128
display_step=10
frame_size=28
length=28
hidden_size=5
n_classes=10
#------------------

x=tf.placeholder(dtype=tf.float32,shape=[None,length*frame_size],name='input_X')
y=tf.placeholder(dtype=tf.float32,shape=[None,n_classes],name='label_Y')
weights=tf.Variable(tf.truncated_normal(shape=[hidden_size,n_classes]))
bias=tf.Variable(tf.zeros(shape=[n_classes]))

def RNN(x,weights,bias):
    x=tf.reshape(x,shape=[-1,length,frame_size])
    rnn_cell=tf.nn.rnn_cell.BasicRNNCell(hidden_size)
    output,states=tf.nn.dynamic_rnn(rnn_cell,x,dtype=tf.float32)
    return tf.nn.softmax(tf.matmul(output[:,-1,:],weights)+bias)

pred_y= RNN(x,weights,bias)
cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred_y,labels=y))
train=tf.train.AdamOptimizer(train_rate).minimize(cost)

correct_pred=tf.equal(tf.argmax(pred_y,1),tf.argmax(y,1))
acc=tf.reduce_mean(tf.cast(correct_pred,dtype=tf.float32))

init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    test_x,test_y=mnist.test.next_batch(batch_size)
    step=1
    while step<train_step:
        batch_x,batch_y=mnist.train.next_batch(batch_size)
        sess.run([cost,train],feed_dict={x:batch_x,y:batch_y})
        if step%display_step==0:
            acc,loss=sess.run([acc,cost],feed_dict={x:test_x,y:test_y})
            print(step,acc,loss)
            print('--------------------')