def prime(a):
    c=0
    for i in range(1,a):
        if(a%i==0):
            c+=1
    if(c==1):
        return 1
    else:
        return 0   
n=int(input())
v=r=d=x=f=0
x=n
while x>0:
    f+=1
    x=x//10
if(prime(n)==1):
    v=n
    while(v>0):
        r=v%10
        if(prime(r)==1):
            d+=1
        else :
            break
        v=v//10
    if(f==d):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")