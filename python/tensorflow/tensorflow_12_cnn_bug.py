#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:44:09 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('../mnist', one_hot=True)
x=tf.placeholder(tf.float32,[None,784])
y_=tf.placeholder(tf.float32,[None,10])

def weight_var(shape):
    init=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(init)
def bias_var(shape):
    init=tf.constant(0.1,shape=shape)
    return tf.Variable(init)

def conv(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
def max_pooling(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

x_image=tf.reshape(x,[-1,28,28,1])

W_conv1=weight_var([5,5,32,64])
b_conv1=bias_var([64])
h_conv1=tf.nn.relu(tf.nn.conv2d(x_image,W_conv1)+b_conv1)
h_pool1=max_pooling(h_conv1)

W_conv2=weight_var([5,5,32,64])
b_conv2=bias_var([64])
h_conv2=tf.nn.relu(tf.nn.conv2d(h_pool1,W_conv2)+b_conv2)
h_pool2=max_pooling(h_conv2)

w_fc1=weight_var([7*7*64,1024])
b_fc1=bias_var([1024])
h_pool_flat=tf.reshape(h_pool2,[-1,7*7*64])
h_fc1=tf.nn.relu(tf.matmul(h_pool_flat,w_fc1)+b_fc1)

keep_prob = tf.placeholder(tf.float32)
h_fc1_dropout = tf.nn.dropout(h_fc1, keep_prob)

w_fc2=weight_var([1024,10])
b_fc2=bias_var([10])
y_conv=tf.matmul(h_fc1_dropout,w_fc2)+b_fc2

