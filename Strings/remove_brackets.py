def func(s):
    s2 = ""
    for i in s:
        if i != "(" and i !=")":
            s2+= i
    print(s2)

s = "a+((b-c)+d)"
func(s)