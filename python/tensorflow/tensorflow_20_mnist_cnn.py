#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:31:58 2018

@author: xsxsz
"""

# TODO  try cnn

import time
import numpy as np
import tensorflow as tf
import load_mnist

images,labels=load_mnist.load_mnist()
#images=images.reshape(60000,28,28)
labels=np.eye(10)[labels.reshape(-1)]
images=images.astype('float32')
labels=labels.astype('float32')
print(images.shape)
print('----------------')
print(labels.shape)
print('----------------')

learning_rate=0.0001

def weight_init(shape):
    init=tf.truncated_normal(shape,stddev=0.2)
    return tf.Variable(init)

def bias_init(shape):
    init=tf.constant(0.1,shape=shape)
    return tf.Variable(init)

def conv(x,W):
    return tf.nn.conv2d(x,W,strides=[1,2,2,1],padding='SAME')

def max_pooling(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

x=tf.placeholder(tf.float32,[None,784])
x_image=tf.reshape(x,[-1,28,28,1])

W_conv_1=weight_init([5,5,1,32])
b_conv_1=bias_init([32])
h_conv_1=tf.nn.relu((conv(x_image,W_conv_1))+b_conv_1)
h_pool_1=max_pooling(h_conv_1)

W_conv_2=weight_init([5,5,32,64])
b_conv_2=bias_init([64])
h_conv_2=tf.nn.relu(conv(h_pool_1,W_conv_2)+b_conv_2)
h_pool_2=max_pooling(h_conv_2)

W_fc1=weight_init([7*7*64,1024])
b_fc1=bias_init([1024])
h_pool_2_flat=tf.reshape(h_pool_2,[-1,7*7*64])
h_fc1=tf.nn.relu(tf.matmul(h_pool_2_flat,W_fc1)+b_fc1)

keep=tf.placeholder('float32')
h_fc1_drop=tf.nn.dropout(h_fc1,keep)
W_fc2=weight_init([1024,10])
b_fc2=bias_init([10])

y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)

y_=tf.placeholder('float32',[None,10])
cross_entropy=-tf.reduce_sum(y_*tf.log(y_conv))
train=tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)
correct=tf.equal(tf.argmax(y_conv,1),tf.argmax(y_,1))
acc=tf.reduce_mean(tf.cast(correct,'float32'))

start_time=time.clock()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        train.run(session=sess,feed_dict={x:images[i:i+50,:],y_:labels[i:i+50,:],keep:0.5})

    #print(acc.eval(session=sess,feed_dict={})
    print('--------------------------------------------------')
end_time=time.clock()
print('time:%f'%end_time-start_time)
print('--------------------------------------------------')
