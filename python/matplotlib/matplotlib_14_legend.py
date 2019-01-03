import matplotlib.pyplot as plt
import numpy as np
x = np.random.uniform(-1, 1, 4)
y = np.random.uniform(-1, 1, 4)
p1,= plt.plot([1,2,3])
p2,= plt.plot([3,2,1])
l1 = plt.legend([p2, p1], ["line 2", "line 1"], loc='upper left')
p3=plt.scatter(x[0:2],y[0:2],marker='D',c='r')
p4=plt.scatter(x[2:],y[2:],marker='D',c='g')
plt.legend([p3,p4],['label1','label2'],loc='lower right',scatterpoints=2)
plt.title('plot')