#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:55:08 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from  tensorflow.examples.tutorials.mnist  import  input_data
import tensorflow as tf
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

mnist = input_data.read_data_sets('../mnist/', one_hot=True)
labels=10
input_size=784
hidden_size_1=30
batch_size=100
training_iterations=20000
learning_rate=0.05

X = tf.placeholder (tf.float32, shape = [None, input_size])
Y = tf.placeholder (tf.float32, shape = [None,labels])

W1=tf.Variable(tf.random_normal([input_size,hidden_size_1],stddev=0.1))
B1=tf.Variable(tf.constant(0.1),[hidden_size_1])

W2=tf.Variable(tf.random_normal([hidden_size_1,labels],stddev=0.1))
B2=tf.Variable(tf.constant(0.1),[labels])

hidden_layer_operation=tf.nn.relu(tf.matmul(X,W1)+B1)
final_operation=tf.nn.relu(tf.matmul(hidden_layer_operation,W2)+B2)

loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y,logits=final_operation))
train_step=tf.train.AdadeltaOptimizer(learning_rate).minimize(loss)
correct_predict=tf.equal(tf.argmax(Y,1),tf.argmax(final_operation,1))
acc=tf.reduce_mean(tf.cast(correct_predict,'float'))

sess=tf.Session()
sess.run(tf.global_variables_initializer())
plt.figure(figsize=(8,7))
x=[]
y=[]
for i in range(training_iterations):
    batch=mnist.train.next_batch(batch_size)
    batch_input=batch[0]
    batch_labels=batch[1]
    train_loss=sess.run([train_step,loss],feed_dict={X:batch_input,Y:batch_labels})
    if i%200==0:
        training_accuracy=acc.eval(session=sess,feed_dict={X:batch_input,Y:batch_labels})
        print('epoch: %d ,training_accuracy: %g '%(i/200+1,training_accuracy))
        print('--------------')
        plt.title('bp_network')
        plt.xlabel('epoch')
        plt.ylabel('accuracy')
        plt.grid()
        plt.scatter(i/200+1,training_accuracy)
        x.append([i/200+1])
        y.append([training_accuracy])     

x=np.array(x).reshape(-1,1)
y=np.array(y)
poly=PolynomialFeatures(degree=5)
x_transformed=poly.fit_transform(x)
poly_linear_model=LinearRegression()
poly_linear_model.fit(x_transformed,y)

X=np.linspace(0,training_iterations/200,training_iterations/200)
X_transformed=poly.fit_transform(X.reshape(-1,1))
Y=poly_linear_model.predict(X_transformed)
plt.plot(X,Y,color='g')
plt.grid()