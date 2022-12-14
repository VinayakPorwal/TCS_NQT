import math


def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n= 60
for i in range(2,n+1):
    if n%i==0:
        if isPrime(i):
            print(i,end=" ")