#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 22:22:39 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
c=tf.constant(1)
print(c.graph)
print('----------')
print(type(c))
print('----------')
print(tf.get_default_graph())
print('----------')
g=tf.Graph()
print(g)
print('----------')
with g.as_default():
    d=tf.constant(1)
    print(d.graph)
    print('----------')

g1=tf.Graph()
print(g1)
print('----------')
g1.as_default()
a=tf.constant(1)
print(a.graph)
print('----------')
