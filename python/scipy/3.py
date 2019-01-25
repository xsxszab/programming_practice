#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:18:34 2019

@author: xsxsz
"""

from scipy import stats
import numpy as np


generated = stats.norm.rvs(size=920)
mean,std = stats.norm.fit(generated)
skew,pvalue=stats.skewtest(generated)
print(std)