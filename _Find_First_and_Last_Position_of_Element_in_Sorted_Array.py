a=int(input())
arr=list(map(int,input().split()))
b=int(input())
if b not in arr:
    print(-1,-1)
else:
    i1=i2=0
    for i in range(a):
        if arr[i]==b:
            i1=i
            break
    for i in range(a-1,-1,-1):
        if arr[i]==b:
            i2=i
            break
    print(i1,i2)