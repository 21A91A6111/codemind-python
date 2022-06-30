a=int(input())
arr=list(map(int,input().split()))
ma=c=mc=0
for i in range(a):
    c=1
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j]:
                c+=1
    if c==mc:
        mc=c
        if arr[i]<ma:
            ma=arr[i]
    elif c>mc:
        mc=c
        ma=arr[i]
print(ma)