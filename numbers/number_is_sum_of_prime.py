import math


def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True 

n=11 
flag =1
for i in range(2,n):
    if isprime(n-i) and isprime(i):
        print("yes")
        flag = 0
        break
if flag:
    print("No")
