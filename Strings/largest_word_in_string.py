def func(s):
    ans=""
    check =""
    for i in s:
        if i==" ":
            if len(ans)<len(check):
                ans = check 
            check=""
        else:
            check+=i
    print(ans)

s="Google doc"
func(s)
        