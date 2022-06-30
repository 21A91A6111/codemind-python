s=input()
v=0
v=len(s)
for i in range(v):
    x=0
    for j in range(v):
        if(i!=j):
            if(s[i]==s[j]):
                x+=1
                break
    if(x>0):
        break
    else:
        i+=1
if(x==0):
    print('Unique Number')
else:
    print('Not Unique Number')
    