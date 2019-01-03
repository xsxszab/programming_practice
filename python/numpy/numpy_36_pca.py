#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:55:54 2018

@author: xsxsz
"""

#not_so_clear
import numpy as np
def pca(mat,k=5):
    meanVals=np.mean(mat,axis=0)
    mat1=mat-meanVals
    mat2=mat1/np.std(mat)
    covmat=np.cov(mat2,rowvar=0)
    eigVals,eigVectors=np.linalg.eig(np.mat(covmat))
    eigVals=np.argsort(eigVals)
    eigVals=eigVals[:-(k+1):-1]
    eigVectors=eigVectors[:,eigVals]
    mat_output=mat2*eigVectors
    recon_mat=(mat_output*eigVectors.T)*np.std(mat)+np.mean(mat,axis=0)
    return mat_output,recon_mat
