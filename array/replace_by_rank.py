arr= [20,15,26,2,98,6]
arr2 = sorted(arr)
rank = {}
ans = []
j=1
for i in arr2:
    if rank.get(i)!=None:
        continue
    else:
        rank[i] = j
    j+=1
for i in arr:
    ans.append(rank[i])
print(ans)