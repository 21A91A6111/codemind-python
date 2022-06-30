a=int(input())
arr=list(map(int,input().split()))
pro=1
for i in range(a):
    pro=1
    for j in range(a):
        if i!=j:
            pro*=arr[j]
    print(pro,end=" ")