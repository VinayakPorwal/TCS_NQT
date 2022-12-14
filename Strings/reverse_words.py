def func(s):
    ans = []
    temp =''
    for i in s:
        if i==" ":
            ans.append(temp)
            temp =''
        else:
            temp+=i 
    ans.append(temp)
    for i in range(len(ans)):
        print(ans[len(ans)-i-1],end=" ")

s= "this is an amazing program"
func(s)
