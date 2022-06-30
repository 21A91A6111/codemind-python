n=int(input())
r=b=c=0
while n>0:
    r=n%10
    b+=pow(r,2)
    n=n//10
    if(n==0):
        if(b>0 and b<=9):
            break
        else:
            n=b
            b=0
if(b==1 or b==7):
    print(True)
else:
    print(False)