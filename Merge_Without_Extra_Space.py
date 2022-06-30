t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    for j in range(b):
        arr.append(arr2[j])
    l=len(arr)
    for j in range(l):
        for k in range(l-1):
            if arr[k]>arr[k+1]:
                arr[k],arr[k+1]=arr[k+1],arr[k]
    for i in range(l):
        if i==l-1:
            print(arr[i],end="")
        else:
            print(arr[i],end=" ")
    print(""),