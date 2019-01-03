import copy
a=[11,22,33,44]
b=a
print a,b
a.append(100)
print a,b,id(a),id(b)
a.remove(11)
print a
print id(a),id(b)
c=copy.copy(a)
print id(a),id(c)
print c
c.append(123)
print c
print a
print
list=[12,[2,4],245]
i=list
j=copy.copy(list)
k=copy.deepcopy(list)
print id(list),id(i),id(j),id(k)
list[1][0]=0
list[0]=1243546
print list
print i
print j
print k
