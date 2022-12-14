

arr = [1,2,3,4,5,0]
result = 0
for i in range(len(arr)):
    mul = 1
    for j in range(i,len(arr)):
        result=max(result,mul)
        mul*=arr[j]
    if result<mul:
        result=mul
print(result)
