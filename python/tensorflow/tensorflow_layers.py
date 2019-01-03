#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:04:22 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
from tensorflow.contrib.layers.python.layers import initializers
lstm_cell_1=tf.nn.rnn_cell.LSTMCell(name='1',num_units=128,use_peepholes=True,num_proj=64,initializer=initializers.xavier_initializer())
print(lstm_cell_1.output_size)
print('-------------')
print(lstm_cell_1.state_size)
print('-------------')
print(lstm_cell_1.state_size.c)
print('-------------')
print(lstm_cell_1.state_size.h)
print('-------------')
lstm_cell_2=tf.nn.rnn_cell.LSTMCell(name='2',num_units=128,use_peepholes=True,num_proj=64,initializer=initializers.xavier_initializer())
lstm_cell_3=tf.nn.rnn_cell.LSTMCell(name='3',num_units=128,use_peepholes=True,num_proj=64,initializer=initializers.xavier_initializer())
multi_cell=tf.nn.rnn_cell.MultiRNNCell(cells=[lstm_cell_1,lstm_cell_2,lstm_cell_3])
print(multi_cell.output_size)
print('-------------')
print(type(multi_cell.state_size))
print('-------------')
print(multi_cell.state_size)
print('-------------')
print(multi_cell.state_size[0])
print('-------------')
print(multi_cell.state_size[2].h)
print('-------------')
