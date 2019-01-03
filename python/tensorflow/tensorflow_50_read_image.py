#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:36:42 2018

@author: xsxsz
"""

import tensorflow as tf
import matplotlib.pyplot as plt

img_raw_data=tf.gfile.FastGFile('scenery.jpg','rb').read()

with tf.Session() as sess:
    img=tf.image.decode_png(img_raw_data)
    img=sess.run(img)
    plt.imshow(img)
    encoded_img=tf.image.encode_png(img)
    with tf.gfile.GFile('./output.png','wb') as f:
        f.write(encoded_img.eval())

