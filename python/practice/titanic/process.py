# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:58:56 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression

training_set=pd.read_csv('./train.csv')
test_set=pd.read_csv('./test.csv')
"""
print(training_set.head())
print('-------------')
print(test_set.head())
print('-------------')
"""
def fill_nan(dataset,key):
    dataset[key]=dataset[key].fillna(dataset[key].median())

fill_nan(training_set,'Age')
fill_nan(test_set,'Age')


"""
plt.figure(figsize=(12,10))

plt.subplot(221)
male_num=(training_set['Sex'] == 'male').sum()
female_num=(training_set['Sex'] == 'female').sum()
plt.pie(x=[male_num,female_num],labels=['Male','Female'],colors=['b','r'])

plt.subplot(222)
df=training_set['Fare'].sort_values(ascending=False)
plt.hist(df,bins=np.arange(0,600,10),color='g')
plt.title('Fare')
plt.xlabel('Frequency')

plt.subplot(223)
Q_num=(training_set['Embarked'] == 'Q').sum()
S_num=(training_set['Embarked'] == 'S').sum()
C_num=(training_set['Embarked'] == 'C').sum()
plt.pie(x=[Q_num,S_num,C_num],labels=['Q','S','C'],colors=['r','g','b'])

plt.subplot(224)
df=training_set['Age'].sort_values(ascending=False)
plt.hist(df,bins=np.arange(0,80,1),color='b')
"""

"""
print(training_set.describe())
print('-----------------')
print(training_set.info())
print('-----------------')
"""

training_set.loc[training_set['Embarked'] == 'S', "Embarked"]=0
training_set.loc[training_set['Embarked'] == 'Q', "Embarked"]=1
training_set.loc[training_set['Embarked'] == 'C', "Embarked"]=2
training_set.loc[training_set['Sex'] == 'male',"Sex"]=0
training_set.loc[training_set['Sex'] == 'female','Sex']=1

predictors=["Pclass","Sex","Age","SibSp","Parch","Fare"]
model=LogisticRegression(random_state=1)
scores=cross_validation.cross_val_score(model,training_set[predictors],\
                                        training_set["Survived"],cv=3)
print(scores.mean())
print('----------------')
