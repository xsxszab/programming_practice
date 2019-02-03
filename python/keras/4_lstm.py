#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:51:06 2019

@author: xsxsz
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils

np.random.seed(10)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))
length=3
x=[]
y=[]
for i in range(0, len(alphabet)-length):
    seq_in = alphabet[i:i + length]
    seq_out = alphabet[i + length]
    x.append([char_to_int[char] for char in seq_in])
    y.append(char_to_int[seq_out])
X=np.reshape(x,(len(x),length,1))
X=X/float(len(alphabet))
Y=np_utils.to_categorical(y)

model=Sequential()
model.add(LSTM(32,input_shape=(X.shape[1],X.shape[2])))
model.add(Dense(Y.shape[1],activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,nb_epoch=500,batch_size=1,verbose=2)

scores=model.evaluate(X,Y,verbose=0)
print(scores)
print('----------------')
for pattern in x:
    x=np.reshape(pattern, (1, len(pattern), 1))
    x=x/float(len(alphabet))
    prediction=model.predict(x, verbose=0)
    index=np.argmax(prediction)
    result=int_to_char[index]
    seq_in=[int_to_char[value] for value in pattern]
    print(seq_in,"->",result)
print('----------------')
