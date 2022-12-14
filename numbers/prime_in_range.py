import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    
    return True
    

m,n = 2 , 10
ans = []
for i in range(int(m),int(n)):
    if isPrime(i):
        ans.append(i)
print(ans)
