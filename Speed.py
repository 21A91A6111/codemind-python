t=int(input())
for i in range(t):
    a=int(input())
    arr=list(map(int,input().split()))
    c=1
    for j in range(1,a):
        if arr[j]<arr[j-1]:
            c+=1
    print(c)