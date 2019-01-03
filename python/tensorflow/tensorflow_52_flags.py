#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:44:33 2018

@author: xsxsz
"""

import tensorflow as tf

tf.app.flags.DEFINE_string('string', 'as you can see','this is a string')
tf.app.flags.DEFINE_integer('one',1,'this is a number')
tf.app.flags.DEFINE_boolean('boolean_value',True,'this is a boolean value')

flags=tf.app.flags.FLAGS

def main(_):
    print(flags.string)
    print('----------')
    print(flags.one)
    print('----------')
    print(flags.boolean_value)
    print('----------')

if __name__ == '__main__' :
    tf.app.run(main)

