from attr import has


arr = [1,2,3,2,4,3,1,2]
hash = {}
hash2= {}
ans  =''
arr = sorted(arr)
for i in arr:
    if hash.get(i)!=None:
        hash[i]+=1
    else:
        hash[i]=1
hash = sorted(hash.items(),key=lambda kv:
                 (kv[1], kv[0]),reverse=True)
for i in hash:
    hash2[i]= hash[i]
hash = {}
for i in sorted(hash2):
    hash[i] = hash2[i]

print(hash)