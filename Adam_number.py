n=int(input())
r=n*n
v=n
rev=0
while n!=0 :
    g=n%10
    rev=rev*10+g
    n=n//10
x=rev*rev
a=x
ver=0
while x!=0 :
    d=x%10
    ver=ver*10+d
    x=x//10
if(r==ver) :
    print(True)
else :
    print(False)