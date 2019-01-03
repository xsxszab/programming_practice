#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:14:48 2018

@author: xsxsz
"""

from caffe import layers as L,params as P,to_proto

path='./resource/'
train_lmdb=path+'train_db'                
val_lmdb=path+'val_db'                    
mean_file=path+'mean.binaryproto'         
train_proto=path+'train.prototxt'
val_proto=path+'val.prototxt'
def creat_net(lmdb,batch_size,include_acc=False):
    data, label = L.Data(source=lmdb, backend=P.Data.LMDB, batch_size=batch_size, ntop=2,
        transform_param=dict(crop_size=40,mean_file=mean_file,mirror=True))
    conv1=L.Convolution(data, kernel_size=5, stride=1,num_output=16, pad=2,weight_filler=dict(type='xavier'))
    relu1=L.ReLU(conv1, in_place=True)
    pool1=L.Pooling(relu1, pool=P.Pooling.MAX, kernel_size=3, stride=2)
    conv2=L.Convolution(pool1, kernel_size=3, stride=1,num_output=32, pad=1,weight_filler=dict(type='xavier'))
    relu2=L.ReLU(conv2, in_place=True)
    pool2=L.Pooling(relu2, pool=P.Pooling.MAX, kernel_size=3, stride=2)
    fc3=L.InnerProduct(pool2, num_output=1024,weight_filler=dict(type='xavier'))
    relu3=L.ReLU(fc3, in_place=True)
    drop3 = L.Dropout(relu3, in_place=True)
    fc4 = L.InnerProduct(drop3, num_output=10,weight_filler=dict(type='xavier'))
    loss = L.SoftmaxWithLoss(fc4, label)
    
    if include_acc:
        acc = L.Accuracy(fc4, label)
        return to_proto(loss, acc)
    else:
        return to_proto(loss)

def write():
    with open('train','w') as file:
        file.write(str(creat_net(train_lmdb,batch_size=64)))
        
    with open('val','w') as file:
        file.write(str(creat_net(val_lmdb,batch_size=32,include_acc=True)))

if __name__ == '__main__':
    write()
    