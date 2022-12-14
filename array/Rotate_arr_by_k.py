arr = [1,2,3,4,5]
# k = 2
# i = 0
# while(i<k):
#     arr.append(arr[i])
#     i+=1
# for i in range(len(arr)-k):
#     arr[i]=arr[i+k] 
# while(k):
#     arr.pop()
#     k-=1
# print(arr)

# OR 
k=2
arr1 = arr[k:]
arr2 = arr[:k]
arr1.extend(arr2)
print(arr1)