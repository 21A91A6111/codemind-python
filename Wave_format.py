def pr(arr,n):
    ma=0
    for i in range(0,n):
        if(arr[i]>ma):
            ma=arr[i]
    return ma
n=int(input())
z=n
arr=list(map(int,input().split()))
arr.sort()
for i in range(z):
    while((n-1)>=0):
        v=pr(arr,n-1)
        if(v==0):
            print(pr(arr,n),end="")
        else:
            print(pr(arr,n-1),end=" ")
            print(pr(arr,n),end=" ")
        n-=2