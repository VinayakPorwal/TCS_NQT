def func(str):
    str2 = ''
    for i in str:
        if i==" ":
            continue
        else:
            str2+=i
    print(str2)
s="helo  remove space"
func(s)