def func(s1,s2):
    i=0
    j=-1
    while(i<len(s1)):
        
        if s1[i:]==s2:
            j=i
            break
        i+=1
    print(j)
s1 ="hello"
s2 = "az"
func(s1,s2)

