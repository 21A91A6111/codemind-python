s=input()
g=len(s)
v=0
for i in range (g):
    if s[i].isdigit():
        v+=ord(s[i])-48
print(v)