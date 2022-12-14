
import math


n = 6
flag =1 
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        flag=0
        break
if flag:
    print("YES")
else:
    print("NO")
