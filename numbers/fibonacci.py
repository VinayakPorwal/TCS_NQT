def fib(n):
    temp1 = 0
    temp2 =1
    for i in range(n+1):
        print(temp1)
        store = temp1
        temp1 = temp1+temp2
        temp2 = store

# fib(5)
 
# OR 

def fib2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib2(n-1)+fib2(n-2)
print(fib2(6))