s=input()
x=len(s)
c=v=iso=0
for i in range(x):
    c=0
    for j in range(x):
        if i!=j:
            if s[i]==s[j]:
                c+=1
    if(c==0):
        iso+=1
    else:
        break
if(iso==x):
    print(True)
else:
    print(False)