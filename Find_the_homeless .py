a=int(input())
pep=[]
hus=[]
for i in range(a):
    v=int(input())
    pep.append(v)
for i in range(a):
    v=int(input())
    hus.append(v)
for i in range(a):
    if pep[i]<=hus[i]:
        pep[i]=0
        hus[i]=0
    else:
        if i-1>=0:
            if hus[i-1]>pep[i]:
                hus[i-1]=0
                pep[i]=0
        elif i+1<=a:
            if hus[i+1]>pep[i]:
                hus[i+1]=0
                pep[i]=0
c=0
for i in pep:
    if i!=0:
        c+=1
print(c)