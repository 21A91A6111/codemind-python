a=int(input())
arr=list(map(int,input().split()))
arr2=[]
for i in range(a):
    arr2.append(arr[i]**2)
for i in range(a):
    for j in range(a-1):
        if arr2[j]>arr2[j+1]:
            arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
for i in arr2:
    print(i,end=" ")