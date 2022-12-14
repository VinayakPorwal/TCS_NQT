def func(s):
    s2 = ''
    for i in range(0,len(s)):
        if s[i]==" ":
            s+=s[i]
        
        if i==0:
                s2+=s[i].upper()
        elif i==len(s)-1 and s[i]!=" ":
                s2+=s[i].upper()
        else:
            if s[i+1] == " ":
                    s2+=s[i].upper()

            elif s[i-1]==" ":
                    s2+=s[i].upper()

            else:
                s2+=s[i]
    print(s2)
s= "take u forward is awesome"

print(s)
func(s)


