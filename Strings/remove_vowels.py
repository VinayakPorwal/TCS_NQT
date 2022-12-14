def func(str):
    i=0
    while i < (len(str)):
        if str[i]=='a' or str[i]=='A' or str[i]=='e' or str[i]=='E' or str[i]=='i' or str[i]=='I' or str[i]=='o' or str[i]=='O' or str[i]=='u' or str[i]=='U' :
            str = str[0:i] + str[i+1:len(str)]
            i-=1
        i+=1
    print(str)

# OR 

def func2(str):
    str2 = ''
    for i in str:
        if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U' :
            continue
        else:
            str2+=i 
    print(str2)       
s = "Appple is good"

func2(s)

