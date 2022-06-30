a=int(input())
arr=list(map(int,input().split()))
mid=a//2
for i in range(mid):
    print(arr[i],arr[mid+i],end=" ")