arr = [1,2,4,7,7,5]
mini = arr[0]
maxi = arr[0]


for i in arr:
    if mini>i:
        mini = i
    elif maxi<i:
        maxi = i


secondmini = maxi
secondmaxi = mini

for i in arr:
    if secondmini > i and i!=mini:
        secondmini = i 
    elif secondmaxi < i  and i!=maxi:
        secondmaxi = i
print(maxi , mini)
print(secondmaxi,secondmini)

# OR 

arr = set(sorted(arr))
# print(arr[1],arr[-2])