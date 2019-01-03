#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:56:01 2018

@author: xsxsz
"""

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
iris=load_iris()
X_trainval,X_test,y_trainval,y_test = train_test_split(iris.data,iris.target,random_state=0)
X_train,X_val,y_train,y_val = train_test_split(X_trainval,y_trainval,random_state=1)
best_socre=0.000
for gamma in [1,0.1,0.01,0.001]:
    for C in [1,0.1,0.01,0.001]:
        svm=SVC(gamma=gamma,C=C)
        svm.fit(X_train,y_train)
        score=svm.score(X_val,y_val)
        if score>best_socre:
            best_socre=score
            best_combination=(gamma,C)

print('best socre:',best_socre)
print('----------------')
print('best combindation: gamma:',best_combination[0],'C:',best_combination[1])
print('----------------')
