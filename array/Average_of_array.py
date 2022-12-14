arr = [1,2,3,4,5]
ans = 0
for i in arr:
    ans+=i
ans = ans/len(arr)

# OR 
ans = sum(arr)/len(arr)

print(ans)