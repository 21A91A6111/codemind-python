a=int(input())
arr=list(map(int,input().split()))
for i in range(0,a,2):
    f=arr[i]
    v=arr[i+1]
    for j in range(f):
        print(v,end=" ")