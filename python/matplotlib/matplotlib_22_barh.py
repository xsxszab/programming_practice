# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:24:47 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()
print(plt.style.available)
print('------')
data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
plt.figure()
ax=plt.subplots(figsize=(5,5))
plt.barh(group_names,group_data)
plt.style.use('seaborn-poster')
plt.title('Bar')