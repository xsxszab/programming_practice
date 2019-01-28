#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:25:23 2019

@author: xsxsz
"""

import random
import matplotlib.pyplot as plt

size=1000

values=[]
values=[random.random() for _ in range(size)]
plt.figure(figsize=(10,10))
plt.subplot(621)
plt.hist(values,100,color='g')
plt.subplot(622)
values=[random.uniform(1,size) for _ in range (size)]
plt.hist(values,100,color='g')
plt.subplot(623)
low,high=1,size
values=[random.triangular(low,high) for _ in range(size)]
plt.hist(values,100,color='g')
plt.subplot(624)
alpha,beta=1,10
values=[random.betavariate(alpha,beta) for _ in range(size)]
plt.hist(values,100,color='g')
plt.subplot(625)
lam=1.0/((size+1)/2)
values=[random.expovariate(lam) for _ in range(size)]
plt.hist(values,100,color='g')
plt.subplot(626)
values=[random.gammavariate(alpha,beta) for _ in range(size)]
plt.hist(values,100,color='g')
plt.subplot(627)
mu,sigma=1,0.5
values=[random.lognormvariate(mu,sigma) for _ in range(size)]
plt.hist(values,100,color='g')
plt.subplot(628)
values=[random.normalvariate(mu,sigma) for _ in range(size)]
plt.hist(values,100,color='g')
plt.subplot(629)
alpha=1
values=[random.paretovariate(alpha) for _ in range(size)]
plt.hist(values,100,color='g')
plt.tight_layout()
