c=0
d=0
n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        c=0
        for j in range(1,i+1):
            if(i%j==0):
                c=c+1
        if(c!=2):
            d=d+1
print(d)