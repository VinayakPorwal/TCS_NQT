mini = 10
maxi = 50
out = []
def plaindrome(n):
    temp =n
    ans = 0
    while(n):
        mod = n%10
        n = n//10
        ans = ans*10 + mod
    if ans ==temp:
        return True
    else:
        return False
for i in range(mini,maxi):
    if plaindrome(i):
        out.append(i)
print(out)
