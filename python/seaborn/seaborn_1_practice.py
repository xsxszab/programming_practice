#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:44:11 2018

@author: xsxsz
"""

import seaborn as sns
iris=sns.load_dataset('iris')
print(iris.shape)
print('----------')
sns.swarmplot(x='species',y='petal_length',data=iris)
