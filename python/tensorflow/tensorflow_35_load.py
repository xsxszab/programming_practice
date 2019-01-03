import tensorflow as tf 
var1 = tf.Variable([1.0], dtype=tf.float32, name='v1') 
var2 = tf.Variable([2.0], dtype=tf.float32, name='v2') 
addOp = var1+var2 
saver = tf.train.Saver() 
path_model = './checkpoint'
with tf.Session() as sess: 
    saver.restore(sess, path_model) 