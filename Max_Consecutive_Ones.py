a=int(input())
arr=list(map(int,input().split()))
c=m=0
for i in range(a):
    c=0
    for j in range(i,a):
        if arr[j]==1:
            c+=1
        else:
            break
    if m<c:
        m=c
print(m)