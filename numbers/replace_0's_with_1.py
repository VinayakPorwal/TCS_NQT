def func(n):
    ans = 0
    while(n>0):
        mod = n%10
        if mod==0:
            mod =1
        ans = ans*10 + mod
        n=n//10
    return ans 
n= 204
ans = func(n)
ans = func(ans)
print(ans)