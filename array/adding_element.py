arr = [1,2,3,4,5]

def insertatbegin(arr,n):
    arr.insert(0,n)
    print(arr)

def insertatend(arr,n):
    arr.append(n)
    print(arr)

def insertatpos(arr,n,k):
    arr.insert(k-1,n)
    print(arr)

insertatbegin(arr,6)
insertatend(arr,7)
insertatpos(arr,8,4)