# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 07:29:03 2018

@author: Administrator
"""

import numpy as np

def createDataSet():
    group = np.array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5],[0.2,2.3],[1.0,2.4],[1.1,0.5],
                      [0.1,0.2],[0.0,3.0],[0.8,1.5],[0.2,0.7],[0.9,1.0]])
    labels = ['A','A','B','B','B','A','A','B','B','A','B','A']
    return group,labels

def classify(input,dataSet,label,k):
    dataSize = dataSet.shape[0]
    diff = np.tile(input,(dataSize,1)) - dataSet
    sqdiff = diff ** 2
    squareDist = np.sum(sqdiff,axis = 1)
    dist = squareDist ** 0.5
    sortedDistIndex = np.argsort(dist)

    classCount={}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return classes