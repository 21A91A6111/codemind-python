def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
def near(a):
    l=f=df=dl=0
    for i in range(a,0,-1):
        if prime(i)==1:
            f=i
            df=a-i
            break
    for i in range(a,10000):
        if prime(i)==1:
            l=i
            dl=i-a
            break
    if df==dl:
        return f
    elif df>dl:
        return l
    elif df<dl:
        return f
t=int(input())
for i in range(t):
    a=int(input())
    print(near(a))