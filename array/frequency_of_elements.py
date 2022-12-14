arr = [10,5,10,15,10,5]
freq = {}
for i in arr:
    if freq.get(i)!=None:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)