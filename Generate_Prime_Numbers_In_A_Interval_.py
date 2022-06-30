a=int(input())
b=int(input())
if a==1:
    a=2
for i in range(a,b+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count=count+1
    if count==0:
        print(i)
