def func(s):
    # for i in range(len(s)):
    #     for j in range(len(s)-i-1):
    #         if s[j] > s[j+1]:
    #             temp = s[j]
    #             s[j] = s[j+1]
    #             s[j+1]=temp 
    s = sorted(s)
    ans=""
    for i in s:
        ans+=i
    print(ans)

s = "bcda"
func(s)
