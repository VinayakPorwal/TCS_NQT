arr = [1,2,3,6,7,8,2,3,2,6]
hashmap = {}
arr2=[]
for i in arr:
    if hashmap.get(i) !=None:
        hashmap[i] +=1
    else:
        hashmap[i]=1
        arr2.append(i)
print(arr2)

# OR 

arr = set(arr)
print(arr)