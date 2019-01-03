import numpy as np
import copy
a=np.arange(1,20,2,dtype=int).reshape(2,5)
print a
print id(a)
b=copy.deepcopy(a)
print b,id(b)
print np.hstack((a,b))
print np.vstack((a,b))
