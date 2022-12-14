#FORMULA -  n! / (n-r)!
def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)
n,r= 6,4
print(fac(n)//fac(n-r))