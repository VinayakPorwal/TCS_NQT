def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)

n=26
i=n
ans =0
while(i>0):
    mod = i%10
    ans+= fac(mod)
    i = i//10
if ans==n:
    print("Yes")
else:
    print("No")