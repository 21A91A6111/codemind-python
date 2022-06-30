a=int(input())
arr=list(map(int,input().split()))
m=0
for i in range(a):
    for j in range(i,a):
        if m<arr[j]-arr[i]:
            m=arr[j]-arr[i]
print(m)