#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:36:52 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

sess=tf.Session()
init=tf.global_variables_initializer()
rand=tf.truncated_normal(shape=[4,10],mean=1.0,stddev=0.2)
sess.run(init)
matrix=sess.run(rand)
sess.close()
print(matrix.shape)
print('-----------')
plt.matshow(matrix,fignum=2)
plt.colorbar()