n = 2746
ans = 0
mini = n%10
maxi = n%10
while(n>0):
    mod = n%10
    n=n//10
    if mod>maxi:
        maxi = mod
    if mini>mod:
        mini = mod
print(mini, maxi)