num=raw_input('input:')
flag=1
for i in range(len(num)/2):
    if num[i]!=num[-i-1]:
        flag=0
        break
print flag