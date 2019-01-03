def judge(n):
    i=n%10
    j=(n%100-i)/10
    k=(n-i-10*j)/100
    if i**3+j**3+k**3==n:
        print n
judge(153)