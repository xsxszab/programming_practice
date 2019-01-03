#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:59:25 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

x=np.linspace(-10,10,100)

y_sigmoid=tf.nn.sigmoid(x)
y_relu=tf.nn.relu(x)
y_relu6=tf.nn.relu6(x)
y_softsign=tf.nn.softsign(x)
y_tanh=tf.nn.tanh(x)
y_softplus=tf.nn.softplus(x)

sess=tf.Session()
sess.run(tf.global_variables_initializer())
list=sess.run([y_sigmoid,y_relu,y_relu6,y_softsign,y_tanh,y_softplus])
labels=['sigmoid','relu','relu6','softsign','tanh','softplus']
plt.figure(figsize=(12,15))
for i in range(6):
    plt.subplot(321+i)
    plt.plot(x,list[i],label=labels[i])
    plt.grid()
    plt.legend(loc='best')
