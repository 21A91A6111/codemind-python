def prime(n):
    c=0
    for i in range(1,n+1,1):
        if n%i==0:
            c=c+1
    if c==2:
        return 1
    else:
        return 0
num = int(input())
if prime(num):
    r=0
    s=0
    while(num>0):
        d=num%10
        if prime(d):
            r=r+1
        s=s+1
        num = num//10
    if r==s:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")