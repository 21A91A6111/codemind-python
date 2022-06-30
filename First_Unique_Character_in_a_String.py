s=input()
v=len(s)
f=d=c=0
for i in range(v):
    c=0
    for j in range(v):
        if(i!=j):
            if(s[i]==s[j]):
                c+=1
                break
    if(c==0):
        print(i)
        break
if(c>0):
    print(-1)