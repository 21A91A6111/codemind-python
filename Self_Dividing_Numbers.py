a=int(input())
b=int(input())
for i in range(a,b+1):
    v=i
    j=i
    s=0
    count=0
    while(i>0):
     s=i%10
     count=count+1
     i=i//10
    c=0
    while j>0:
     r=j%10
     if(r!=0 and v%r==0):
        c=c+1
     j=j//10
    if(count==c):
      print(v,end=" ")
