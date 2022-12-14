arr = [1,4,5,6,8,9,7]
# BUBBLE SORT 
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)

# OR 
arr = sorted(arr)
print(arr)