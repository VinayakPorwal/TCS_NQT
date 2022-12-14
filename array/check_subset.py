arr1 = [1,3,4,5,2]
arr2 = [2,4,3,1,7,5,15]
hash={}
for i in arr2:
    if hash.get(i)!=None:
        hash[i]+=1
    else:
        hash[i]=1
flag =1   
for i in arr1:
    if hash.get(i)==None:
        print(False)
        flag = 0
        break

if flag : print(True)