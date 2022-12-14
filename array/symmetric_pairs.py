arr = [[1,2],[2,1],[3,4],[4,5],[5,4]]
hashmap = {}
ans = []
for pair in arr:
    if hashmap.get(pair[1])!=None:
        if hashmap[pair[1]]==pair[0]:
            ans.append(pair)

    else:
        hashmap[pair[0]]=pair[1]
print(hashmap)
print(ans)