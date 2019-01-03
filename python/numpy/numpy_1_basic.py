import numpy as np
list=np.zeros((2,3))
print list
list[1,2]=1
print list
print np.__version__
print np.eye(4)
print np.diag([1,2,3],k=-2)
print np.random.random((4,6))
arr=np.diag([1,2],k=1)
print arr.max()
print np.tile([[1,3],[2,4]],(2,3))
