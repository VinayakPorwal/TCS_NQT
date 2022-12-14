def func(s):
    s2=''
    for i in s:
        if i==i.lower():
            s2+=i.upper() 

        elif i==i.upper():
            s2+=i.lower()
    print(s2)
 
s="take u forward IS Awesome"
func(s)
