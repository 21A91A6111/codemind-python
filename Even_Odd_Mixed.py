x=int(input())
s=0
d=0
while x!=0:
    n=x%10
    x=x//10
    if(n%2==0):
        s+=1
    else:
        d+=1
if d>0 and s>0:
    print('Mixed')
elif d>0 and s==0:
    print('Odd')
elif d==0 and s>0:
    print('Even')