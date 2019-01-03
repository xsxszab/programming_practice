#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 07:10:36 2018

@author: xsxsz
"""

#-------------------
#not so clear,still need to learn
#-------------------

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from tensorflow.examples.tutorials.mnist import input_data

iteration=1000000
mb_size = 128
Z_dim = 100

mnist = input_data.read_data_sets('../../mnist', one_hot=True)

def weight_var(shape, name):
    return tf.get_variable(name=name, shape=shape, initializer=tf.contrib.layers.xavier_initializer())

def bias_var(shape, name):
    return tf.get_variable(name=name, shape=shape, initializer=tf.constant_initializer(0))

X = tf.placeholder(tf.float32, shape=[None, 784], name='X')

D_W1 = weight_var([784, 128], 'D_W1')
D_b1 = bias_var([128], 'D_b1')
D_W2 = weight_var([128, 1], 'D_W2')
D_b2 = bias_var([1], 'D_b2')
theta_D = [D_W1, D_W2, D_b1, D_b2]


Z = tf.placeholder(tf.float32, shape=[None, 100], name='Z')

G_W1 = weight_var([100, 128], 'G_W1')
G_b1 = bias_var([128], 'G_B1')
G_W2 = weight_var([128, 784], 'G_W2')
G_b2 = bias_var([784], 'G_B2')
theta_G = [G_W1, G_W2, G_b1, G_b2]

def generator(z):
    G_h1 = tf.nn.relu(tf.matmul(z, G_W1) + G_b1)
    G_log_prob = tf.matmul(G_h1, G_W2) + G_b2
    G_prob = tf.nn.sigmoid(G_log_prob)
    return G_prob

def discriminator(x):
    D_h1 = tf.nn.relu(tf.matmul(x, D_W1) + D_b1)
    D_logit = tf.matmul(D_h1, D_W2) + D_b2
    D_prob = tf.nn.sigmoid(D_logit)
    return D_prob, D_logit

def sample_Z(m, n):
    return np.random.uniform(-1., 1., size=[m, n])

def plot(samples):
    fig = plt.figure(figsize=(4, 4))
    gs = gridspec.GridSpec(4, 4)
    gs.update(wspace=0.05, hspace=0.05)
    for i, sample in enumerate(samples):
        ax = plt.subplot(gs[i])
        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_aspect('equal')
        plt.imshow(sample.reshape(28, 28), cmap='Greys_r')
    return fig

generator=generator(Z)
D_real,D_real_logit=discriminator(X)
D_fake,D_fake_logit=discriminator(generator)

D_loss=-tf.reduce_mean(tf.log(D_real)+tf.log(1.-D_fake))
G_loss=-tf.reduce_mean(tf.log(D_fake))
D_optimizer=tf.train.AdamOptimizer().minimize(D_loss,var_list=theta_D)
G_optimizer=tf.train.AdamOptimizer().minimize(G_loss,var_list=theta_G)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(iteration):
        X_mb, _ = mnist.train.next_batch(mb_size)
        sess.run([D_optimizer, D_loss], feed_dict={
                              X: X_mb, Z: sample_Z(mb_size, Z_dim)})
        sess.run([G_optimizer, G_loss], feed_dict={
                              Z: sample_Z(mb_size, Z_dim)})
        if i % 1000 == 0:
            samples = sess.run(generator, feed_dict={Z: sample_Z(16, Z_dim)})
            fig = plot(samples)
            plt.savefig('./img/'+str(i/1000)+'.png',bbox_inches='tight')
            i+=1
            plt.close(fig)
