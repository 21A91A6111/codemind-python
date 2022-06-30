a=int(input())
arr=list(map(int,input().split()))
r=int(input())
for i in range(r):
    temp=arr[0]
    arr[0]=arr[a-1]
    for j in range(1,a):
        val=arr[j]
        arr[j]=temp
        temp=val
for i in arr:
    print(i,end=" ")