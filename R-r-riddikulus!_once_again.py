a,b=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(b):
    ft=arr[0]
    for j in range(a-1):
        arr[j]=arr[j+1]
    arr[a-1]=ft
for i in arr:
    print(i,end=" ")