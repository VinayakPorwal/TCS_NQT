
# LCM(a,b) =  a*b/GCD(a,b)

def gcd(a,b):
    if b==0:
        return a 
    return gcd(a,a%b)

a,b= 3,6
print((a*b)//gcd(a,b))