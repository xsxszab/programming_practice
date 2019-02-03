#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:30:41 2019

@author: xsxsz
"""

import numpy as np
import scipy.sparse  as sparse

indptr = np.array([0,0,1,2])
indices = np.array([2,3])
data = np.array([12, 22])
mat1=sparse.csr_matrix((data,indices,indptr),shape=(3,4))
print(mat1)
print('-------------')
print(mat1.todense())
print('-------------')
indptr = np.array([0,0,1,2])
indices = np.array([2,3])
data = np.array([12, 22]).repeat(6).reshape(2, 2, 3)
mat2=sparse.bsr_matrix((data,indices,indptr),shape=(6,12))
print(mat2)
print('-------------')
print(mat2.todense())
print('-------------')
