a=int(input())
arr=list(map(int,input().split()))
for i in range(a):
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j] and arr[i]!=-1:
                arr[j]=-1
for i in arr:
    if i!=-1:
        print(i,end=" ")