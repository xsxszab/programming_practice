#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:14:16 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf

inputs = tf.placeholder(np.float32, shape=(32,40,5))
lstm_cell_1 = tf.contrib.rnn.BasicLSTMCell(num_units=128)
print(lstm_cell_1.output_size)
print('-------------')
print(lstm_cell_1.state_size)
print('-------------')
#---important-------
output,state=tf.nn.dynamic_rnn(
    cell=lstm_cell_1,
    inputs=inputs,
    dtype=tf.float32
)
#-------------------
