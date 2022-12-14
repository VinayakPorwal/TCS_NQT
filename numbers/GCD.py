# Euclidean’s theorem.
# Gcd is the greatest number which is divided by
# both a and b.If a number is divided by both a and b,
# it is should be divided by (a-b) and b as well.

# GCD(a,b) = GCD(b,a%b)
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

# OR 
def gcd2(a,b):
    gcd = 0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd

a,b=3,6
print(gcd2(3,6))
