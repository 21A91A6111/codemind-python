def rev(a):
    re=0
    while a>0:
        r=a%10
        re=(re*10)+r
        a//=10
    return re
a=int(input())
c=0
if a<0:
    c=1
    a*=-1
res=rev(a)
if c==1:
    print(res*-1)
else:
    print(res)