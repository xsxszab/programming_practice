# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 07:23:09 2018

@author: Administrator
"""

import numpy as np
mat=np.mat([[1,2,3],[4,5,6],[7,8,9]])
print mat
print'--------'
print np.linalg.matrix_rank(mat)
print'--------'
mat1=np.eye(4)
print mat1
print'--------'
print np.linalg.matrix_rank(mat1)
print'--------'
print np.linalg.eigvals(mat)
print'--------'
print np.linalg.eig(mat)
print'--------'
print np.linalg.det(mat)
print'--------'
