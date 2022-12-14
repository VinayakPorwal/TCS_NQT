# roots of quadractic equation 
# equation - ax^2+bx+c=0 
# Discriminant = b^2 - 4ac
# if D > 0 :
#     root1 = -b + sqrt(b^2-4ac)/2a
#     root2 = -b - sqrt(b^2-4ac)/2a
# if D<0:
#     root1 = -b/2a + (i sqrt(-(b^2-4ac)))/2a
#     root2 = -b/2a - (i sqrt(-(b^2-4ac)))/2a
# if D=0:
    # root1=root2 = -b/2a

import math


a,b,c = 1,1,1
D = b*b - 4*a*c
if D>0:
    root1 = (-b + math.sqrt(D) )/(2*a)
    root2 = (-b - math.sqrt(D))/(2*a)
    print("Roots are Real and Different",root1,root2)
elif D==0:
    root1 = root2 = (-b /(2*a))
    print("Roots are real and Same",root1,root2)
elif D<0:
    print("Roots are complex",-b/(2*a) ,"+ i", round((math.sqrt(-D)/(2*a)),2),",",-b/(2*a) ,"- i", round((math.sqrt(-D)/(2*a)),2))