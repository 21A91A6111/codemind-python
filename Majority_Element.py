a=int(input())
arr=list(map(int,input().split()))
c=0
ma=mc=0
for i in range(a):
    c=0
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j] and arr[i]!=-1:
                c+=1
                arr[j]=-1
    if mc<c:
        mc=c
        ma=arr[i]
print(ma)