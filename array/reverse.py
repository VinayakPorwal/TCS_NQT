arr = [1,2,4,7,7,5]
i=0
n = len(arr)
arr2 = [0]*n
for i in range(n):
    arr2[i] = arr[n-i-1]
print(arr2)
    
# OR 
arr = arr[::-1]
print(arr)