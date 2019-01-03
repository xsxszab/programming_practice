#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 14:50:39 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf

input_id=tf.placeholder(tf.int32,shape=[None])
embedding=tf.Variable(np.identity(5,dtype=np.int32))
input_embedding=tf.nn.embedding_lookup(embedding,input_id)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(embedding.eval())
    print('------------')
    print(sess.run(input_embedding,feed_dict={input_id:[1,2,2,4]}))
    print('------------')

