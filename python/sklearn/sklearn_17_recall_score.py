#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:46:59 2018

@author: xsxsz
"""

import numpy as np
from sklearn.metrics import recall_score
y_true=np.array([0,1,2,0,1,2])
y_predicted=np.array([0,2,1,0,0,1])
print(recall_score(y_true=y_true,y_pred=y_predicted,average='macro'))
print('--------------')
print(recall_score(y_true=y_true,y_pred=y_predicted,average='micro'))
print('--------------')
