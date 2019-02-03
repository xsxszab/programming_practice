#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:56:10 2019

@author: xsxsz
"""

import numpy as np
import scipy.sparse as sparse
import matplotlib.pyplot as plt
import random

rows=np.array(random.sample(range(0,9),5))
cols=np.array(random.sample(range(0,9),5))
value=np.array(random.sample(range(1,1000),5))
mat=sparse.coo_matrix((value,(rows,cols)))
print(mat)
print('----------------')
result=mat.todense()
print(result)
print('----------------')
plt.matshow(result)
plt.colorbar()
plt.title('$sparse matix$')
