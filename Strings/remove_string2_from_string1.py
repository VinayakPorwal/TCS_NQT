def func(s1,s2):
    hash = {}
    for i in s2:
        if hash.get(i)!=None:
            hash[i]+=1
        else:
            hash[i]=1
    ans = ''
    for i in s1:
        if hash.get(i)==None:
            ans+=i 
    return ans 

s1 = "abcdef"
s2 = "cefz"

print(func(s1,s2))