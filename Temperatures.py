a=int(input())
arr=list(map(int,input().split()))
for i in range(a):
    c=0
    for j in range(i+1,a):
        if arr[j]>arr[i]:
            c+=1
            break
        else:
            c+=1
            if j==a-1 and c>0:
                c=0
                break
    print(c,end=" ")