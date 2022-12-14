n=274
ans = 0
while(n>0):
    mod = n%10
    n=n//10
    ans = ans*10 + mod

print(ans)
