arr = [1,-1,4]
total = sum(arr)
add = 0
for i in range(len(arr)):
    if add == total - add - arr[i]:
        print(i) 
        break
    else:
        add += arr[i]