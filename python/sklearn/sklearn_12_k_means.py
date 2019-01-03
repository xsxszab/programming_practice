#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:31:56 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data=np.random.random((100,2))
kmeans=KMeans(n_clusters=3,n_init=200,init='k-means++',precompute_distances=True,n_jobs=-1)
plt.figure(1,figsize=(12,5))
plt.subplot(121)
plt.scatter(data[:,0],data[:,1],color='b')
kmeans.fit(data)

print(kmeans.predict(data))
print('----------')
print(kmeans.cluster_centers_.shape)
print('----------')
ans=kmeans.predict(data)
ans=ans.tolist()

for i in range(len(ans)):
    if ans[i]==0:
        ans[i]='r'
        continue
    if ans[i]==1:
        ans[i]='g'
        continue
    if ans[i]==2:
        ans[i]='b'
print(ans)
print('----------')
plt.subplot(122)
for j in range(len(ans)):
    plt.scatter(data[j,0],data[j,1],color=ans[j])
print(kmeans.get_params)
print('----------')
