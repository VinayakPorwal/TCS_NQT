

def func(s):
    s2 = ''
    for i in s:
    
        if i=='z':
            s2+='a'
        else:
            s2+= chr(ord(i)+1)
    print(s2)

s="abcdzyx"
func(s)
        


