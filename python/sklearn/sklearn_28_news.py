#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 09:08:44 2018

@author: xsxsz
"""

import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import GaussianNB

train=datasets.fetch_20newsgroups(subset='train')
test=datasets.fetch_20newsgroups(subset='test',shuffle=True,random_state=10)

tfidf=TfidfTransformer()

X_tain_tfidf=tfidf.fit_transform(train)
X_test_tfidf=tfidf.transform(test)

clf=GaussianNB()
clf.fit(X_tain_tfidf,train.target)

predict=clf.predict(X_test_tfidf)
print(metrics.classification_report(train.target,predict,target_names=test.target_names))
