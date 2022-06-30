a=int(input())
arr=list(map(int,input().split()))
for i in range(a-1):
    ma=0
    for j in range(i+1,a):
        if arr[j]>ma:
            ma=arr[j]
    print(ma,end=" ")
print(-1)