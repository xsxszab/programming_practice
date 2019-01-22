#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:01:47 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

STEP=1000

np.random.seed(200)
x=np.linspace(-10,10,1000)
np.random.shuffle(x)
y=0.5*x+2.5+np.random.normal(0,5.6,(1000,))

"lt.scatter(x,y,color='g')"

x_train=x[:800]
x_val=x[801:]
y_train=x[:800]
y_val=x[801:]

model=Sequential()
model.add(Dense(output_dim=1, input_dim=1))
model.compile(loss='mse',optimizer='sgd')

print('begin training')
for step in range(STEP):
    cost=model.train_on_batch(x_train,y_train)
    if step&100==0:
        print('current cost:',cost)
print('end training')
cost=model.evaluate(x_val,y_val,batch_size=40)
print('test cost:',cost)

W,b=model.layers[0].get_weights()
y_pred=model.predict(x_val)
plt.scatter(x_val,y_val,color='g')
plt.plot(x_val,y_pred,color='b')

print(model.summary())