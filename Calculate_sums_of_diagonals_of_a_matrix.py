a=int(input())
pd=sd=0
for i in range(a):
    arr=list(map(int,input().split()))
    for j in range(a):
        if i==j:
            pd+=arr[j]
        if i+j==a-1:
            sd+=arr[j]
print("Principal Diagonal:",end="")
print(pd)
print("Secondary Diagonal:",end="")
print(sd)