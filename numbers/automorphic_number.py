def check(n):
    m=n*n
    while(n>0):
        mod1 = n%10
        mod2 = m%10
        if mod1!=mod2:
            return False
        n=n//10
        m=m//10
    return True
n=10
print(check(n))