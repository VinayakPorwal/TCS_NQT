arr = [1,2,3,4,2,3,2,4]

check = {}
ans = set()
for i in arr:
    if check.get(i)!=None:
        check[i]+=1
        ans.add(i)
    else:
        check[i]=1

print(ans)