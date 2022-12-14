def func(s):
    hash={}
    for i in s:
        if hash.get(i)!=None:
            hash[i]+=1
        else:
            hash[i]=1
    for i in hash:
        if hash[i]>1:
            print(i,hash[i]) 
s = "sinstriiintng"
func(s)