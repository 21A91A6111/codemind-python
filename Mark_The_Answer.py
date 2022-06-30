a,b=map(int,input().split())
arr=list(map(int,input().split()))
ma=sk=0
for i in arr:
    if i<=b:
        ma+=1
    elif i>b:
        if sk==1:
            break
        else:
            sk+=1
            continue
print(ma)