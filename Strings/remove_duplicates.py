def func(s):
    hash={}
    ans = ''
    for i in s:
        if hash.get(i)!=None:
            hash[i]+=1
        else:
            hash[i]=1
            ans+=i
    return ans
    
s = "apple"
print(func(s))
