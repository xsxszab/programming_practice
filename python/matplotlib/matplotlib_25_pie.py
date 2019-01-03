# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:44:19 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
labels=['a','b','c','d']
parts= [15, 30.55, 44.44, 10]
explode = [0, 0.2, 0, 0]
plt.figure(figsize=(5,5))
plt.pie(x=parts,labels=labels,explode=explode,shadow=True,startangle=20,autopct='%.1f %%',pctdistance=0.6)
plt.title('Pie')
