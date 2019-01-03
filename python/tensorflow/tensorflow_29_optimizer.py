#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:25:02 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

lr=0.1
batch_size=32
iteration=200

rand=np.random.RandomState(10)
x=np.linspace(-1,1,100)[:,np.newaxis]
noise=rand.normal(0,0.1,size=x.shape)
y=np.power(x,2)+noise

plt.figure(figsize=(6,5))
plt.scatter(x,y)
plt.grid()

#-------something_interesting------------
class net:
    def __init__(self,opt,**kwargs):
        self.x=tf.placeholder(tf.float32,shape=[None,1])
        self.y=tf.placeholder(tf.float32,shape=[None,1])
        layer=tf.layers.dense(self.x,20,tf.nn.relu)
        output=tf.layers.dense(layer,1)
        self.loss=tf.losses.mean_squared_error(output,self.y)
        self.train=opt(lr,**kwargs).minimize(self.loss)
#----------------------------------------

SGD=net(tf.train.GradientDescentOptimizer)
momentum=net(tf.train.MomentumOptimizer,momentum=0.8)
losses=[[],[]]
nets=[SGD,momentum]
init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)
for i in range(iteration):
    index=np.random.randint(0,x.shape[0],batch_size)
    X=x[index]
    Y=y[index]
    for net,l_his in zip(nets,losses):
        _,l=sess.run([net.train,net.loss],feed_dict={net.x:X,net.y:Y})
        l_his.append(l)
labels=['SGD','Momentum']
plt.figure(figsize=(6,5))
for i, l_his in enumerate(losses):
    plt.plot(l_his,label=labels[i])
plt.legend(loc='best')
plt.xlabel('Steps')
plt.ylabel('Loss')
plt.ylim((0, 0.2))
sess.close()