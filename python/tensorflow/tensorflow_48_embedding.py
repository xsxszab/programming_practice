#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 14:56:20 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf

input_id=tf.placeholder(tf.int32,shape=[None])
embedding=np.asarray([[0.1,0.2,0.3],[1.1,1.2,1.3],[2.1,2.2,2.3],[3.1,3.2,3.3],[4.1,4.2,4.3]])

input_embedding=tf.nn.embedding_lookup(embedding,input_id)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(input_embedding,feed_dict={input_id:[1,2,3,1]}))
    print('------------------')

