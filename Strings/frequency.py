def func(s):
    hashmap ={}
    for i in s:
        if hashmap.get(i)!=None:
            hashmap[i] +=1
        elif  i!=" ":
            hashmap[i]=1
    for i in hashmap:
        print(i,hashmap[i],end="  ")
s = "hello world"
func(s)