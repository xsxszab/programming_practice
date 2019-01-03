dict={'a':1,'b':2}
print dict['a']
print dict.get('b')
print dict.get('c','nothing')
dict['a']=3
print dict['a']
print dict.items()
print list(dict.items())