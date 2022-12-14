def func(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

s1= "cat"
s2 = "act"

print(func(s1,s2))