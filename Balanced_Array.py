t=int(input())
for k in range(t):
    a=int(input())
    arr=list(map(int,input().split()))
    f=0
    for i in range(a):
        ls=sum(arr[:i])
        rs=sum(arr[i+1:])
        if ls==rs:
            f=1
            break
    if ls==rs:
        print("YES")
    else:
        print("NO")