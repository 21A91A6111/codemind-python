x=int(input())
c=1
for i in range(2,x):
    if(x%i == 0):
        c+=1
if(c==1):
    print("prime")
else:
    print("not a prime")