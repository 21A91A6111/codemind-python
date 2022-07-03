num = int(input())
c=0
for i in range(1,num,1):
    sum = i*(i+1)
    if(num==sum):
        c=c+1
if c==1:
    print("YES")
else:
    print("NO")
        