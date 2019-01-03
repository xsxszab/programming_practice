#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:09:56 2018

@author: xsxsz
"""

import numpy as np
from sklearn import metrics
y=np.array([1,1,2,2])
socres=np.array([0.15,0.4,0.35,0.8])
fpr,tpr,threshoulds=metrics.roc_curve(y,socres,pos_label=2)
print(metrics.auc(fpr,tpr))