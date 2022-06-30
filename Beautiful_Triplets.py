a=int(input())
arr=list(map(int,input().split()))
while (len(arr)):
    c=f=0
    m=min(arr)
    for i in range(len(arr)):
        if arr[i]>=m:
            c+=1
        if arr[i]==m:
            f+=1
    for i in range(f):
        arr.remove(m)
    print(c)