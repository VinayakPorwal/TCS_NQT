def func(s):
    ans = 0
    for i in s:
        if i.isalpha() :
            continue
        else:
            ans += int(i)

    print(ans)
s = "1xyz23"
func(s)