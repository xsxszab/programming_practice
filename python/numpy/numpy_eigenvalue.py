#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:50:54 2018

@author: xsxsz
"""

import numpy as np
A = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(np.linalg.eigvals(A))
print('------------')
print(np.linalg.eigvalsh(A))
print('------------')
eigvals,eigvectors = np.linalg.eig(A)
print(eigvals)
print('------------')
print(eigvectors)
print('------------')
