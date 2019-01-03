import numpy as np
a= np.mat(np.arange(8).reshape(2,4))
print a
print a[0,0]
print a[0:2,1:3]
print '---------'
b=np.arange(24).reshape(2,3,4)
print b
print b[0,0:2,1:4]
