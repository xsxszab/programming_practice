import numpy as np
a=np.linspace(1,10,num=10,endpoint=True,dtype=int).reshape(2,5)
print a
print a.T
print
list1 = [[1, 3, 2], [3, 5, 4]]
array = np.array(list1)
print list1
print
array.sort(axis=1)
print(array)