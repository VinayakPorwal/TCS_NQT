def func(n):
    ans = 0
    i=1
    while(i<n):
       if n%i==0:
        ans+=i
       i+=1

    if n<ans:
        return True
    else:
        return False

n = 21
print(func(n))