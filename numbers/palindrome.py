n = 121
temp =n
ans = 0
while(n):
    mod = n%10
    n = n//10
    ans = ans*10 + mod
if ans ==temp:
    print(ans)


# OR 

if str(n)[::-1]==str(n):
    print(True)
else:
    print(False)