# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:55:21 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

dataset=pd.read_csv('./train.csv')

def fill_nan(dataset,key):
    dataset[key]=dataset[key].fillna(dataset[key].median())

fill_nan(dataset,'Age')
dataset.loc[dataset['Sex'] == 'male',"Sex"]=0
dataset.loc[dataset['Sex'] == 'female','Sex']=1
dataset['Embarked']=dataset['Embarked'].fillna('S')
dataset.loc[dataset['Embarked'] == 'S', "Embarked"]=0
dataset.loc[dataset['Embarked'] == 'Q', "Embarked"]=1
dataset.loc[dataset['Embarked'] == 'C', "Embarked"]=2

"""
print(dataset.dtypes)
print(dataset['Age'].unique())
print('----------------')
print(dataset['Sex'].unique())
print('----------------')
print(dataset['Embarked'].unique())
print('----------------')
"""

predictors = ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]

model = RandomForestClassifier(random_state=1,n_estimators = 100,\
                             min_samples_split=4,min_samples_leaf=2)

kf=cross_validation.KFold(dataset.shape[0],n_folds=3,random_state=1)
scores=cross_validation.cross_val_score(model,dataset[predictors],\
                                        dataset['Survived'],cv=kf)
print(scores.mean())
print('----------------')