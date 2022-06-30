def rev(a):
    s=0
    while a>0:
        rem=a%10
        s=(s*10)+rem
        a//=10
    return s
a=int(input())
p1=0
p2=0
d1=0
d2=0
for i in range(a-1,0,-1):
    if rev(i)==i:
        p1=i
        d1=a-i
        break
for i in range(a+1,10000):
    if rev(i)==i:
        p2=i
        d2=i-a
        break
if d1==d2:
    print(p1,p2)
elif d1>d2:
    print(p2)
elif d1<d2:
    print(p1)