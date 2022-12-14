def func(s):
    hash={}
    for i in s:
        if hash.get(i)!=None:
            hash[i]+=1
        else:
            hash[i]=1
    ans = 0
    char = ''
    for i in hash:
        if ans < hash[i]:
            ans = hash[i]
            char = i
    return char

s="apple"
print(func(s))