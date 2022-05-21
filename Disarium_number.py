x=eval(input())
c=len(str(x))
temp=x
s=0
while x!=0:
    a= x % 10
    x//=10
    m=a**c
    s+=m
    c-=1
if s==temp:
    print(True)
else:
    print(False)
    