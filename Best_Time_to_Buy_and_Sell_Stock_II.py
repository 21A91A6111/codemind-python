a=int(input())
arr=list(map(int,input().split()))
m=0
for i in range(1,a):
    if arr[i]-arr[i-1]>0:
        m+=arr[i]-arr[i-1]
print(m)