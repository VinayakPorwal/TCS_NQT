arr = [1,1,2,2,2,3,3]
print(set(arr))

# OR 
arr2 = []
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        arr2.append(arr[i])
arr2.append(arr[len(arr)-1])
print(arr2)
