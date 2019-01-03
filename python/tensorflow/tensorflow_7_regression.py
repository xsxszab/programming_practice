#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 07:26:22 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)
    W=tf.matmul(inputs,Weights)+biases
    if activation_function is None:
        outputs=W
    else:
        outputs=activation_function(W)
    return outputs

x_data=np.linspace(-1,1,300)[:,np.newaxis]
noise=np.random.normal(0,0.05,x_data.shape)
y_data=np.square(x_data)+noise-0.5
xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])
l1=add_layer(xs,1,10,activation_function=tf.nn.relu)
prediction=add_layer(l1,10,1,activation_function=None)
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    fig=plt.figure(figsize=(6,6))
    ax=fig.add_subplot(111)
    plt.title('Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    ax.scatter(x_data,y_data,alpha=0.7)
    plt.ion()
    for i in range(4000):
        sess.run(step,feed_dict={xs:x_data,ys:y_data})
        if i %50==0:
            #print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            prediction_value=sess.run(prediction,feed_dict={xs:x_data,ys:y_data})
            lines=ax.plot(x_data,prediction_value,color='r',linewidth=4)
    saver=tf.train.Saver()
    saver.save(sess,'tensorflow_save/tensorflow_7')            
plt.savefig('result.png')