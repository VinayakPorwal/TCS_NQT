def func(n):
    ans = 0
    while(n>0):
        mod = n%10
        ans+=mod
        n=n//10

    return ans

n=472
print(func(n))