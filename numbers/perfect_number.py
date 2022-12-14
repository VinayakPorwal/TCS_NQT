# if sum of factors of a number is equal to number ==> Perfect Number 
n=28
i=1
summ = 0
while(i<n):
    if n%i==0:
        summ += i
    i+=1
if summ == n:
    print(True)