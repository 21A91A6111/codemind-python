a=int(input())
arr=list(map(int,input().split()))
mid=a//2
for i in range(a-1,mid-1,-1):
    print(arr[i],end=" ")
for i in range(mid):
    print(arr[i],end=" ")