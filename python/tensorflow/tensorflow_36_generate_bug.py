#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:56:16 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

steps=10
batch_size=128
hidden_nums=1
learning_rate=0.01
epochs=10
train_examples=11000
test_examples=1100

def generate(seq):
    x=[]
    y=[]
    for i in range(len(seq)-steps):
        x.append([seq[i:i+steps]])
        y.append([seq[i+steps]])
    return np.array(x,dtype=np.float32),np.array(y,dtype=np.float32)

train=np.sin(np.linspace(0,100,num=train_examples,dtype=np.float32))
test=np.sin(np.linspace(100,110,num=test_examples,dtype=np.float32))

X_train,Y_train=generate(train)
X_test,Y_test=generate(test)
X_train=np.reshape(X_train,newshape=(-1,steps,1))
X_test=np.reshape(X_test,newshape=(-1,steps,1))
plt.plot(range(1000),Y_test[:1000,0],"r--")
g=tf.Graph()
with g.as_default():
    X_p=tf.placeholder(dtype=tf.float32,shape=(None,steps,1))
    y_p=tf.placeholder(dtype=tf.float32,shape=(None,1))
    
    lstm_cell=tf.contrib.rnn.BasicLSTMCell(num_units=hidden_nums)
    init_state=lstm_cell.zero_state(batch_size=batch_size,dtype=tf.float32)
    outputs,states=tf.nn.dynamic_rnn(cell=lstm_cell,inputs=X_p,initial_state=init_state,dtype=tf.float32)
    h=outputs[:,-1,:]
    mse=tf.losses.mean_squared_error(labels=y_p,predictions=h)
    optmizer=tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss=mse)
    init=tf.global_variables_initializer()

with tf.Session(graph=g) as sess:
    sess.run(init)
    for epochs in range(1,epochs+1):
        results=np.zeros(shape=[test_examples,1])
        train_losses=[]
        test_losses=[]
        print('epoch:',epochs)
        for j in range(train_examples//batch_size):
            _,train_loss=sess.run(fetches=(optmizer,mse),feed_dict={X_p:X_train[j*batch_size:(j+1)*batch_size],y_p:Y_train[j*batch_size:(j+1)*batch_size]})
            train_losses.append(train_loss)
            print("average training loss:", sum(train_losses) / len(train_losses))
            
            for j in range(test_examples//batch_size):
                result,test_loss=sess.run(
                    fetches=(h,mse),
                    feed_dict={
                            X_p:X_test[j*batch_size:(j+1)*batch_size],
                            y_p:Y_test[j*batch_size:(j+1)*batch_size]
                        }
            )
            results[j*batch_size:(j+1)*batch_size]=result
            test_losses.append(test_loss)
        print("average test loss:", sum(test_losses) / len(test_losses))
        plt.plot(range(1000),results[:1000,0])
