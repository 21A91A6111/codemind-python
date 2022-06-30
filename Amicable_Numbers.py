a=int(input())
b=int(input())
s=0
t=0
for i in range (1,a) :
    if(a%i==0) :
        s=s+i
for i in range (1,b) :
    if(b%i==0) :
        t=t+i
if(t==a and s==b) :
    print('Amicable')
else :
    print('Not Amicable')