n=5
ans  = 1
for i in range(1,n+1):
    ans*=i
print(ans)


# OR 

def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
print(fac(5))