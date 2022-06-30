s=input()
v="aeiou"
ma=c=0
for i in s:
    if i in v:
        c+=1
    else:
        if c>ma:
            ma=c
            c=0
print(ma)
