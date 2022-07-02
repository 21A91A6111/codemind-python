def prime(a):
    c=0
    for i in range(1,a):
        if(a%i==0):
            c+=1
    if(c==1):
        return 1
    else:
        return 0
a=int(input())
c=df=vf=0
for i in range(a,0,-1):
    if prime(i)==1:
        f=i
        df=a-f
        break
for j in range(a,10000):
    if prime(j)==1:
        g=j
        vf=g-a
        break
if df==vf:
    print(df)
elif df>vf:
    print(vf)
else:
    print(df)
