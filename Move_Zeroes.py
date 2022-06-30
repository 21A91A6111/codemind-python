a=int(input())
arr=list(map(int,input().split()))
for j in range(a):
    for i in range(0,a-1):
        if arr[i]==0:
            arr[i],arr[i+1]=arr[i+1],arr[i]
for i in arr:
    print(i,end=" ")