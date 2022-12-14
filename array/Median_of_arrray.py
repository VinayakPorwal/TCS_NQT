arr = [2,1,5,7]
arr= sorted(arr)
n =len(arr)
if n%2==0:
    ans  = (arr[n//2] + arr[(n//2) -1])/2
else:
    ans = arr[n//2]
print(ans)
