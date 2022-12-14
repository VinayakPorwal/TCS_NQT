def func(n):
    temp = n
    ans = 0
    while(n>0):
        mod = n%10
        ans+=mod
        n=n//10

    if temp%ans==0:
        return True
    else:
        return False
n=379
print(func(n))