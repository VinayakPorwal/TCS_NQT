# temp =n
# k = len(str(n))
# ans = 0
# while(n):
#         mod = n%10
#         ans += pow(mod,k)
#         n=n//10
# if temp == ans:
#     print(ans)
    

def armstrong(n):
    temp =n
    k = len(str(n))
    ans = 0
    while(n):
            mod = n%10
            ans += pow(mod,k)
            n=n//10
    if temp == ans:
        return True
n=153
print(armstrong(n))