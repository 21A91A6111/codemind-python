x,y=map(int,input().split())
for i in range(1,y+1):
    if i%2!=0:
        a=x*i
        print(x,'x',i,'=',a)