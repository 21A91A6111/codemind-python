n=int(input())
c=0
d=0
for i in range(2,n) :
    if(n%i==0) :
        c=1
rev=0
while n!=0 :
    r=n%10
    rev=rev*10+r
    n=n//10
for i in range(2,rev) :
    if(rev%i==0) :
        d=1
if c==0 and d==0 :
    print("circular prime")
elif c==0 and d!=0 :
    print("prime but not a circular prime")
else :
    print("not prime")